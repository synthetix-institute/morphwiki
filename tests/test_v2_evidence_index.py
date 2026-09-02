from __future__ import annotations

import argparse
import json
from pathlib import Path

from scripts.audit_morphwiki_v2_quantum_evidence_index import build as audit_index
from scripts.build_morphwiki_v2_quantum_evidence_index import (
    align_source_first_candidates,
    empty_page,
    finalize,
    source_first_topic_candidates,
)


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8"
    )


def test_source_first_grounding_joins_topic_card_to_exact_v2_row(tmp_path: Path):
    metadata = {
        "fermion": {
            "title": "Fermion",
            "topic_terms": ["fermion"],
            "legacy_witness_count": 0,
            "legacy_arxiv_ids": [],
        },
        "gauge_theory": {
            "title": "Gauge theory",
            "topic_terms": ["gauge"],
            "legacy_witness_count": 0,
            "legacy_arxiv_ids": [],
        },
    }
    cards = tmp_path / "cards.jsonl"
    write_jsonl(
        cards,
        [
            {
                "equation_card_id": "fermion-card",
                "source_id": "2401.00001",
                "canonical_equation": r"\{a_i,a_j^\dagger\}=\delta_{ij}",
                "context_before": "Fermionic anticommutation enforces Pauli exclusion.",
                "context_after": "",
                "quality_flags": ["has_relation", "has_math_token"],
                "clean_endpoint": True,
            },
            {
                "equation_card_id": "gauge-card",
                "source_id": "2401.00002",
                "canonical_equation": r"[D_\mu,D_\nu]=igF_{\mu\nu}",
                "context_before": "Gauge theory identifies the field strength.",
                "context_after": "The covariant derivative defines local transport.",
                "quality_flags": ["has_relation", "has_math_token"],
                "clean_endpoint": True,
            },
        ],
    )
    candidates, scan = source_first_topic_candidates(
        metadata,
        {"fermion": "fields", "gauge_theory": "fields"},
        cards,
        max_per_page=4,
        aligned_card_ids={"fermion-card", "gauge-card"},
    )
    assert scan["pages_with_candidates"] == 2

    alignment = tmp_path / "alignment.jsonl"
    write_jsonl(
        alignment,
        [
            {"equation_card_id": "fermion-card", "v2_row_id": 11},
            {"equation_card_id": "gauge-card", "v2_row_id": 12},
        ],
    )
    pages = {slug: empty_page(meta, 4) for slug, meta in metadata.items()}
    joined = align_source_first_candidates(pages, candidates, alignment, 4)
    finalize(pages)

    assert joined["matched_candidate_cards"] == 2
    assert pages["fermion"]["status"] == "v2_source_grounded"
    assert pages["fermion"]["source_examples"][0]["row_ids"] == [11]
    assert pages["gauge_theory"]["source_examples"][0][
        "relation_relevance"
    ] == "relation_context_match"


def test_source_first_candidates_are_alignment_filtered_and_paper_diverse(tmp_path: Path):
    metadata = {
        "fermion": {
            "title": "Fermion",
            "topic_terms": ["fermion"],
            "legacy_witness_count": 0,
            "legacy_arxiv_ids": [],
        }
    }
    cards = tmp_path / "cards.jsonl"
    write_jsonl(
        cards,
        [
            {
                "equation_card_id": "not-aligned",
                "source_id": "paper-a",
                "canonical_equation": r"\{a_i,a_j^\dagger\}=\delta_{ij}",
                "context_before": "Fermionic anticommutation relation.",
                "quality_flags": ["has_relation"],
                "clean_endpoint": True,
            },
            {
                "equation_card_id": "aligned-a1",
                "source_id": "paper-a",
                "canonical_equation": r"\{a_i,a_j^\dagger\}=\delta_{ij}",
                "context_before": "Fermionic anticommutation relation.",
                "quality_flags": ["has_relation"],
                "clean_endpoint": True,
            },
            {
                "equation_card_id": "aligned-a2",
                "source_id": "paper-a",
                "canonical_equation": r"n_i\in\{0,1\}",
                "context_before": "Fermionic Pauli exclusion.",
                "quality_flags": ["has_relation"],
                "clean_endpoint": True,
            },
            {
                "equation_card_id": "aligned-b",
                "source_id": "paper-b",
                "canonical_equation": r"\Psi(x_1,x_2)=-\Psi(x_2,x_1)",
                "context_before": "Fermionic antisymmetry.",
                "quality_flags": ["has_relation"],
                "clean_endpoint": True,
            },
        ],
    )
    candidates, scan = source_first_topic_candidates(
        metadata,
        {"fermion": "fields"},
        cards,
        max_per_page=4,
        aligned_card_ids={"aligned-a1", "aligned-a2", "aligned-b"},
    )

    assert set(candidates) == {"aligned-a1", "aligned-b"}
    assert scan["candidate_paper_counts_by_page"]["fermion"] == 2


def test_evidence_audit_requires_tree_identity_and_core_relations(tmp_path: Path):
    core = (
        "fermion", "gauge_theory", "quantum_decoherence", "commutator",
        "quantum_entanglement", "renormalization",
    )
    example = {
        "topic_relevance": "local_context_match",
        "relation_relevance": "relation_context_match",
        "row_ids": [1],
        "card_ids": ["card"],
    }
    index = tmp_path / "index.json"
    index.write_text(
        json.dumps(
            {
                "coverage": {"pages_total": len(core)},
                "source_first_scan": {"cards_seen": 20},
                "pages": {
                    slug: {
                        "status": "v2_source_grounded",
                        "source_examples": [example],
                    }
                    for slug in core
                },
            }
        ),
        encoding="utf-8",
    )
    tree = tmp_path / "tree.json"
    tree.write_text(
        json.dumps({"branches": {"physics": {"pages": [{"slug": s} for s in core]}}}),
        encoding="utf-8",
    )
    report = audit_index(
        argparse.Namespace(
            index=str(index),
            tree=str(tree),
            minimum_grounded=6,
            required_core_topics=",".join(core),
        )
    )

    assert report["readiness"] == "usable"
    assert all(report["checks"].values())
