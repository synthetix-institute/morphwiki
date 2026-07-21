#!/usr/bin/env python3
"""Derive the logical constructor used by the quantum book from V2 evidence.

The report keeps three sources separate:

1. the V2 product DAG, which orders rows by constructor completion rank;
2. the grammar learner, which selects primitive factors and attached fibres;
3. the source-equation constructor graph, which records equation order inside papers.

This separation prevents a completion rank from being reported as physical time or
as the literal order in which authors write derivations.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Mapping


def load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError(f"Expected a JSON object in {path}")
    return data


def write_json(path: Path, data: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fraction(value: int | float, total: int | float) -> float:
    return float(value) / float(total) if total else 0.0


def md_scalar(text: str, label: str) -> int:
    match = re.search(rf"^- {re.escape(label)}: `([0-9]+)`", text, flags=re.MULTILINE)
    if not match:
        raise KeyError(f"Missing {label!r} in source-constructor report")
    return int(match.group(1))


def md_section_counts(text: str, heading: str) -> dict[str, int]:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise KeyError(f"Missing section {heading!r} in source-constructor report")
    counts: dict[str, int] = {}
    for key, value in re.findall(r"^- `([^`]+)`: `([0-9]+)`", match.group("body"), flags=re.MULTILINE):
        counts[key] = int(value)
    return counts


def source_constructor_summary(path: Path) -> dict[str, Any]:
    if path.suffix.lower() == ".json":
        data = load_json(path)
        status = data.get("constructor_status") or data.get("constructor_status_counts") or {}
        layers = data.get("completion_layers") or data.get("layer_counts") or {}
        edges = data.get("source_local_edges") or data.get("edge_counts") or {}
        nodes = int(data.get("nodes") or data.get("node_count") or sum(status.values()))
        edge_total = int(data.get("edges") or data.get("edge_count") or sum(edges.values()))
        groups = int(data.get("source_groups") or data.get("source_group_count") or 0)
    else:
        text = path.read_text(encoding="utf-8")
        nodes = md_scalar(text, "Nodes")
        edge_total = md_scalar(text, "Edges")
        groups = md_scalar(text, "Source groups")
        status = md_section_counts(text, "Constructor Status")
        layers = md_section_counts(text, "Completion Layers")
        edges = md_section_counts(text, "Source-Local Edges")

    completion = int(edges.get("source_sequence_role_completion", 0))
    projection = int(edges.get("source_sequence_role_projection", 0))
    lateral = int(edges.get("source_sequence_lateral", 0))
    return {
        "nodes": nodes,
        "edges": edge_total,
        "source_groups": groups,
        "constructor_status": dict(status),
        "constructor_status_fractions": {str(k): fraction(v, nodes) for k, v in status.items()},
        "completion_layers": {str(k): int(v) for k, v in layers.items()},
        "completion_layer_fractions": {str(k): fraction(v, nodes) for k, v in layers.items()},
        "source_local_edges": dict(edges),
        "source_local_edge_fractions": {str(k): fraction(v, edge_total) for k, v in edges.items()},
        "completion_to_projection_ratio": fraction(completion, projection),
        "completion_projection_balance": 1.0 - fraction(abs(completion - projection), completion + projection),
        "lateral_fraction": fraction(lateral, edge_total),
    }


def grammar_summary(grammar: Mapping[str, Any]) -> dict[str, Any]:
    candidates = grammar.get("candidate_scores") or []
    scores = {
        str(row.get("name")): float(row.get("mdl_score"))
        for row in candidates
        if row.get("name") and row.get("mdl_score") is not None
    }
    recommendation = grammar.get("recommendation") or {}
    correlations = grammar.get("energy_correlations") or {}
    overlaps = grammar.get("neighbor_overlaps") or {}
    completion_pairs = [
        "closure_constraints__readout_current",
        "closure_constraints__protocol_order",
        "protocol_order__readout_current",
    ]
    return {
        "rows_available": int(grammar.get("rows_available") or 0),
        "rows_sampled": int(grammar.get("rows_sampled") or 0),
        "selected_grammar": recommendation.get("selected_grammar"),
        "decision": recommendation.get("decision"),
        "completion_promotion": recommendation.get("completion_promotion"),
        "candidate_mdl_scores": scores,
        "three_factor_mdl_gain_over_fiber": recommendation.get("three_factor_mdl_gain_over_fiber"),
        "primitive_neighbor_overlap": (
            next(
                (
                    float(row.get("primitive_neighbor_overlap_mean"))
                    for row in candidates
                    if row.get("name") == recommendation.get("selected_grammar")
                ),
                None,
            )
        ),
        "completion_effective_rank": recommendation.get("completion_effective_rank"),
        "completion_zero_row_fraction": recommendation.get("completion_zero_row_fraction"),
        "completion_pair_energy_correlations": {
            key: correlations.get(key) for key in completion_pairs if key in correlations
        },
        "completion_pair_neighbor_overlaps": {
            key: overlaps.get(key) for key in completion_pairs if key in overlaps
        },
        "operator_substrate_energy_correlation": correlations.get("operator_core__substrate_core"),
        "operator_substrate_neighbor_overlap": overlaps.get("operator_core__substrate_core"),
        "protocol_zero_row_fraction": ((grammar.get("block_stats") or {}).get("protocol_order") or {}).get(
            "zero_row_fraction"
        ),
    }


def dag_summary(dag: Mapping[str, Any]) -> dict[str, Any]:
    rows = int(dag.get("rows") or 0)
    mechanism_edges = int(dag.get("input_mechanism_edge_total") or 0)
    directed = int(dag.get("directed_edge_total") or 0)
    role_counts = {str(k): int(v) for k, v in (dag.get("role_counts") or {}).items()}
    orientation = dag.get("edge_orientation_stats") or {}
    coupled = orientation.get("coupled_operator_substrate") or {}
    sequence = orientation.get("within_paper_sequence") or {}
    transfer_edges = {
        key: int((orientation.get(key) or {}).get("kept_as_transfer_frontier") or 0)
        for key in ("operator_transfer_candidate", "substrate_transfer_candidate")
    }
    return {
        "rows": rows,
        "role_counts": role_counts,
        "role_fractions": {key: fraction(value, rows) for key, value in role_counts.items()},
        "layer_statistics": dag.get("layer_statistics") or [],
        "mechanism_edges": mechanism_edges,
        "directed_edges": directed,
        "directed_fraction": fraction(directed, mechanism_edges),
        "lateral_or_frontier_edges": int(dag.get("lateral_or_frontier_edge_total") or 0),
        "directed_edge_counts": dag.get("directed_edge_counts") or {},
        "within_paper_sequence_directed_fraction": fraction(
            int(sequence.get("directed_edges") or 0), int(sequence.get("input_edges") or 0)
        ),
        "coupled_operator_substrate_lateral_fraction": fraction(
            int(coupled.get("lateral_edges") or 0), int(coupled.get("input_edges") or 0)
        ),
        "coupled_operator_substrate_directed_fraction": fraction(
            int(coupled.get("directed_edges") or 0), int(coupled.get("input_edges") or 0)
        ),
        "transfer_frontier_edges": transfer_edges,
        "orientation_rule": dag.get("orientation_rule"),
    }


def build(args: argparse.Namespace) -> dict[str, Any]:
    dag = dag_summary(load_json(Path(args.dag_json)))
    grammar = grammar_summary(load_json(Path(args.grammar_json)))
    source = source_constructor_summary(Path(args.source_constructor))

    protocol_fraction = (dag.get("role_fractions") or {}).get("protocol", 0.0)
    layer_five = next(
        (float(row.get("fraction")) for row in dag.get("layer_statistics") or [] if int(row.get("layer", -1)) == 5),
        0.0,
    )
    report = {
        "schema_version": 1,
        "report_type": "quantum_constructor_dependency_audit",
        "readiness": "usable",
        "inputs": {
            "dag": args.dag_json,
            "grammar": args.grammar_json,
            "source_constructor": args.source_constructor,
        },
        "v2_completion_dag": dag,
        "grammar_factorization": grammar,
        "source_constructor": source,
        "logical_structure": {
            "identity_base": {
                "factors": ["carrier_or_substrate_context", "operator_apparatus"],
                "relation": "jointly typed rather than temporally ordered",
                "reason": "An operator is defined on a carrier and domain; the grammar learner retains these as two primitive factors.",
            },
            "completion_fibre": {
                "modes": ["closure_or_compatibility", "readout", "protocol"],
                "relation": "optional attached modes rather than a third primitive space or a universal time sequence",
                "reason": "The minimum-description-length model favours one attached completion fibre over a third primitive factor.",
            },
            "realization_and_transfer": {
                "modes": ["operator_preserving_substrate_change", "substrate_preserving_operator_change"],
                "relation": "lateral roads across the product space",
                "reason": "Transfer edges are excluded from monotone completion orientation and retained as frontiers.",
            },
            "source_derivation": {
                "moves": ["role_completion", "role_projection", "lateral_rewrite"],
                "relation": "bidirectional traversal of the completion structure",
                "reason": "Source-local completion and projection counts are nearly balanced, while lateral rewrites are the largest class.",
            },
        },
        "supported_findings": [
            {
                "id": "two_factor_identity",
                "statement": "The compact identity is a typed carrier-operator pair with an attached completion fibre.",
                "evidence": {
                    "selected_grammar": grammar.get("selected_grammar"),
                    "selected_mdl": (grammar.get("candidate_mdl_scores") or {}).get(
                        str(grammar.get("selected_grammar"))
                    ),
                    "three_factor_mdl": (grammar.get("candidate_mdl_scores") or {}).get(
                        "three_factor_completion"
                    ),
                    "primitive_neighbor_overlap": grammar.get("primitive_neighbor_overlap"),
                },
            },
            {
                "id": "completion_is_local",
                "statement": "Most equations specify only part of a mechanism; a complete five-role frame is rare.",
                "evidence": {
                    "v2_layer_five_fraction": layer_five,
                    "source_complete_frame_fraction": (source.get("constructor_status_fractions") or {}).get(
                        "complete_constructor_frame", 0.0
                    ),
                    "protocol_role_fraction": protocol_fraction,
                    "protocol_zero_row_fraction": grammar.get("protocol_zero_row_fraction"),
                },
            },
            {
                "id": "derivation_is_bidirectional",
                "statement": "Published derivations alternate between adding roles and projecting a complete relation onto a simpler equation.",
                "evidence": {
                    "completion_edges": (source.get("source_local_edges") or {}).get(
                        "source_sequence_role_completion", 0
                    ),
                    "projection_edges": (source.get("source_local_edges") or {}).get(
                        "source_sequence_role_projection", 0
                    ),
                    "completion_projection_balance": source.get("completion_projection_balance"),
                    "lateral_fraction": source.get("lateral_fraction"),
                },
            },
            {
                "id": "coupling_preserves_rank",
                "statement": "Joint carrier-operator similarity usually preserves completion rank rather than advancing it.",
                "evidence": {
                    "coupled_lateral_fraction": dag.get("coupled_operator_substrate_lateral_fraction"),
                    "coupled_directed_fraction": dag.get("coupled_operator_substrate_directed_fraction"),
                },
            },
            {
                "id": "routes_are_relations",
                "statement": "Transport, spectral resolution, boundary change, closure, protocol and incompatibility are relation types, not six mandatory stages.",
                "evidence": {
                    "directed_fraction": dag.get("directed_fraction"),
                    "within_paper_sequence_directed_fraction": dag.get(
                        "within_paper_sequence_directed_fraction"
                    ),
                    "transfer_frontier_edges": dag.get("transfer_frontier_edges"),
                },
            },
        ],
        "unsupported_or_overstated_readings": [
            "The DAG does not establish physical causation or physical time.",
            "Role prevalence does not prove that context temporally precedes an operator in an author's derivation.",
            "Closure, readout and protocol are not supported as three mandatory successive stages.",
            "A page-level source-card link alone does not prove that the linked equation expresses the page topic.",
        ],
        "book_structure": {
            "part_1": "Typed identity: carrier/context and operator apparatus",
            "part_2": "Completion: closure/compatibility, readout and optional protocol",
            "part_3": "Realization and transfer: boundaries, fields, particles and implementations",
            "appendix": "Historical and interpretive annotations",
            "page_policy": "Retain every topic entry. Mark whether its equations are topic-native or inherited from a branch constructor, and consolidate shared laws without deleting the topic discussion.",
        },
        "claim_scope": (
            "Dependency audit over the supplied V2 DAG, grammar-selection report and source-equation constructor summary. "
            "It distinguishes measured corpus organization from mathematical dependencies imposed by quantum theory."
        ),
    }
    return report


def render_markdown(report: Mapping[str, Any]) -> str:
    dag = report["v2_completion_dag"]
    grammar = report["grammar_factorization"]
    source = report["source_constructor"]
    lines = [
        "# Quantum Constructor Dependency Audit",
        "",
        f"- Readiness: `{report.get('readiness')}`",
        f"- V2 rows: `{dag.get('rows')}`",
        f"- Source-equation nodes: `{source.get('nodes')}`",
        f"- Selected grammar: `{grammar.get('selected_grammar')}`",
        "",
        "## Logical Structure",
        "",
        "The evidence supports a typed carrier-operator identity with an attached completion fibre. "
        "Closure, readout and protocol are completion modes. They are not a third primitive space and do not form a mandatory temporal sequence.",
        "",
        "The completion DAG orders equations by how many constructor roles are present. The source constructor follows equations inside papers and is bidirectional: authors add roles, project complete relations onto simpler equations and make lateral rewrites.",
        "",
        "## Quantitative Findings",
        "",
        f"- Directed completion edges: `{dag.get('directed_edges')}` / `{dag.get('mechanism_edges')}` ({dag.get('directed_fraction'):.4f}).",
        f"- Coupled carrier-operator edges that remain lateral: `{dag.get('coupled_operator_substrate_lateral_fraction'):.4f}`.",
        f"- Source-local completion edges: `{source['source_local_edges'].get('source_sequence_role_completion', 0)}`.",
        f"- Source-local projection edges: `{source['source_local_edges'].get('source_sequence_role_projection', 0)}`.",
        f"- Completion/projection balance: `{source.get('completion_projection_balance'):.4f}`.",
        f"- Source-local lateral rewrites: `{source['source_local_edges'].get('source_sequence_lateral', 0)}` ({source.get('lateral_fraction'):.4f}).",
        f"- Complete source frames: `{source['constructor_status'].get('complete_constructor_frame', 0)}` ({source['constructor_status_fractions'].get('complete_constructor_frame', 0.0):.4f}).",
        "",
        "## Consequence For The Book",
        "",
        "The book should begin with a jointly typed carrier and operator, then attach closure, readout or protocol as required by the topic. Boundary changes, field extensions and engineered implementations belong to realization and transfer. The six operational routes describe allowed relations between constructions; they are not chapters in a universal derivation sequence.",
        "",
        "Every topic page remains in the book. Topic-native equations are distinguished from shared branch constructors, while the DAG and source graph provide cross-references rather than replacing topic content.",
        "",
        "## Unsupported Readings",
        "",
    ]
    lines.extend(f"- {item}" for item in report.get("unsupported_or_overstated_readings") or [])
    lines.extend(["", "## Scope", "", str(report.get("claim_scope") or ""), ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dag-json", required=True)
    parser.add_argument("--grammar-json", required=True)
    parser.add_argument("--source-constructor", required=True)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md", required=True)
    args = parser.parse_args()
    report = build(args)
    write_json(Path(args.out_json), report)
    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text(render_markdown(report), encoding="utf-8")
    print(
        json.dumps(
            {"json": args.out_json, "markdown": args.out_md, "readiness": report["readiness"]},
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
