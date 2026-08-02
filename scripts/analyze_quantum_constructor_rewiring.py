#!/usr/bin/env python3
"""Build evidence-backed cross-topic connections from the quantum constructor."""

from __future__ import annotations

import argparse
import json
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


ROUTES = [
    "transport_flow_route",
    "constraint_closure_route",
    "spectral_operator_route",
    "boundary_weak_form_route",
    "commutator_incompatibility_route",
    "discrete_protocol_route",
]


CONNECTIONS: List[Dict[str, Any]] = [
    {
        "id": "generator_observable_duality",
        "title": "One operator, two roles: generator and observable",
        "topics": ["hamiltonian_quantum_mechanics", "observable", "spectral_theory"],
        "move": "dual_role_split",
        "invariant": "the self-adjoint operator and its domain",
        "rewiring": "read the same operator through its exponential for transport and through its spectral measure as an energy observable",
        "equations": [r"U(t)=e^{-iHt/\hbar}", r"H=\int_{\sigma(H)}E\,dP_H(E)"],
        "test": "Check domain and self-adjointness once, then verify separately that the generated dynamics is unitary and that the spectral measure reproduces energy statistics.",
    },
    {
        "id": "representation_triangle",
        "title": "Schrodinger, Heisenberg, and path-integral representations",
        "topics": ["schr_dinger_picture", "heisenberg_picture", "path_integral_formulation"],
        "move": "representation_change",
        "invariant": "transition amplitudes and expectation values",
        "rewiring": "move time dependence between states and operators, or replace the propagator by an action-weighted integral",
        "equations": [r"A_H(t)=U(t)^\dagger A_SU(t)", r"\langle q_f|U(t_f-t_i)|q_i\rangle=\int\mathcal Dq\,e^{iS[q]/\hbar}"],
        "test": "Specify domains, measure, boundary conditions, and regularization; the formulations are connected only where they yield the same amplitudes or correlators.",
    },
    {
        "id": "factorization_locality",
        "title": "Carrier factorization defines locality",
        "topics": ["quantum_entanglement", "quantum_information", "quantum_field_theory"],
        "move": "carrier_refactorization",
        "invariant": "the global state and algebraic predictions",
        "rewiring": "change the tensor-product or algebraic subsystem decomposition and track which observables remain local",
        "equations": [r"\mathcal H=\mathcal H_A\otimes\mathcal H_B", r"\rho_A=\operatorname{Tr}_B\rho_{AB}"],
        "test": "State the subsystem algebra or tensor factorization explicitly; entanglement and locality claims are not invariant under arbitrary refactorization.",
    },
    {
        "id": "constraint_before_readout",
        "title": "Constraints define physical observables",
        "topics": ["gauge_theory", "quantum_gravity", "measurement_in_quantum_mechanics"],
        "move": "completion_attachment",
        "invariant": "predictions on the physical state space",
        "rewiring": "attach gauge or diffeomorphism closure before assigning outcome effects to physical observables",
        "equations": [r"\widehat{\mathcal C}_a|\psi_{\rm phys}\rangle=0", r"[\widehat O_{\rm phys},\widehat{\mathcal C}_a]|\psi_{\rm phys}\rangle=0"],
        "test": "Verify that candidate effects descend to the constrained or quotient state space; gauge-dependent quantities cannot be promoted directly to physical records.",
    },
    {
        "id": "boundary_spectrum_family",
        "title": "Boundary conditions are spectral control variables",
        "topics": ["particle_in_a_box", "quantum_tunnelling", "scattering", "spectral_theory"],
        "move": "realization_change",
        "invariant": "the differential operator family and probability conservation",
        "rewiring": "change domain, boundary conditions, or asymptotic channels and follow the induced spectrum or transmission map",
        "equations": [r"H_D=-\frac{\hbar^2}{2m}\Delta_D+V", r"S:\mathcal H_{\rm in}\to\mathcal H_{\rm out}"],
        "test": "A claimed connection must identify the operator domain and conserved flux; similar-looking wave equations with different domains need not have comparable spectra.",
    },
    {
        "id": "channel_instrument_correction",
        "title": "Measurement, channels, and error correction share an instrument calculus",
        "topics": ["quantum_channel", "measurement_in_quantum_mechanics", "quantum_error_correction"],
        "move": "protocol_attachment",
        "invariant": "complete positivity and total probability",
        "rewiring": "retain or discard the classical outcome of a quantum instrument, then condition a recovery channel on that outcome",
        "equations": [r"\mathcal I_i(\rho)=\sum_\alpha K_{i\alpha}\rho K_{i\alpha}^\dagger", r"\mathcal E=\sum_i\mathcal I_i", r"\mathcal R_i\circ\mathcal I_i"],
        "test": "Check complete positivity, normalization, and recovery fidelity with a reference system; state-update rules alone are insufficient.",
    },
    {
        "id": "encoding_intertwiner",
        "title": "Duality and simulation require an intertwining map",
        "topics": ["quantum_simulator", "ads_cft_correspondence", "quantum_error_correction"],
        "move": "carrier_transfer",
        "invariant": "a selected operator algebra and its correlators",
        "rewiring": "encode one carrier in another and require the encoding to intertwine the relevant dynamics and observables",
        "equations": [r"VH_{\rm target}\simeq H_{\rm carrier}V", r"VO_{\rm target}\simeq O_{\rm carrier}V"],
        "test": "Validate more than state overlap: compare a generating set of observables or correlators and report the approximation regime and error bounds.",
    },
]


def load_json(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def cosine(a: Sequence[float], b: Sequence[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


def branch_lookup(tree: Mapping[str, Any]) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for branch_id, branch in (tree.get("branches") or {}).items():
        for row in branch.get("pages") or []:
            if row.get("slug"):
                result[str(row["slug"])] = str(branch_id)
    return result


def build(args: argparse.Namespace) -> Dict[str, Any]:
    root = Path(args.root)
    tree = load_json(root / "quantum_mechanism_tree.json")
    branches = branch_lookup(tree)
    pages: Dict[str, Dict[str, Any]] = {}
    for path in (root / "pages").glob("*.json"):
        if path.stem in branches:
            pages[path.stem] = load_json(path)

    rows: List[Dict[str, Any]] = []
    missing: List[str] = []
    for definition in CONNECTIONS:
        topics = list(definition["topics"])
        absent = [slug for slug in topics if slug not in pages]
        missing.extend(absent)
        vectors = []
        titles = []
        topic_branches = []
        for slug in topics:
            page = pages.get(slug) or {}
            profile = (page.get("hyperion") or {}).get("route_profile") or {}
            vectors.append([float(profile.get(key) or 0.0) for key in ROUTES])
            titles.append(str((page.get("wikipedia") or {}).get("title") or slug))
            topic_branches.append(branches.get(slug, "unresolved"))
        overlaps = [cosine(vectors[i], vectors[j]) for i in range(len(vectors)) for j in range(i + 1, len(vectors))]
        row = dict(definition)
        row.update(
            {
                "topic_titles": titles,
                "branches": topic_branches,
                "mean_route_overlap": sum(overlaps) / len(overlaps) if overlaps else 0.0,
                "minimum_route_overlap": min(overlaps) if overlaps else 0.0,
                "cross_branch": len(set(topic_branches)) > 1,
                "status": "candidate_connection" if not absent else "incomplete_evidence",
            }
        )
        rows.append(row)

    report = {
        "schema_version": 1,
        "report_type": "quantum_constructor_rewiring",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "readiness": "usable" if not missing else "partial",
        "connection_count": len(rows),
        "connections": rows,
        "missing_topics": sorted(set(missing)),
        "interpretation": "Connections are type-preserving constructor hypotheses. Route overlap is supporting corpus evidence, not proof of mathematical equivalence.",
    }
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Quantum Constructor Rewiring", "", f"- Readiness: `{report['readiness']}`", f"- Connections: `{len(rows)}`", ""]
    for row in rows:
        lines.extend(
            [
                f"## {row['title']}",
                "",
                f"- Topics: {', '.join(row['topic_titles'])}",
                f"- Move: `{row['move']}`",
                f"- Invariant: {row['invariant']}",
                f"- Mean route overlap: `{row['mean_route_overlap']:.3f}`",
                "",
                row["rewiring"].capitalize() + ".",
                "",
                "Equations:",
                "",
                "```math",
                "\n".join(row["equations"]),
                "```",
                "",
                "Test: " + row["test"],
                "",
            ]
        )
    Path(args.out_md).write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"json": args.out_json, "markdown": args.out_md, "readiness": report["readiness"]}, indent=2))
    return report


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser()
    p.add_argument("--root", default="discoveries/morphwiki_quantum")
    p.add_argument("--out-json", default="discoveries/morphwiki_quantum/quantum_constructor_rewiring.json")
    p.add_argument("--out-md", default="discoveries/morphwiki_quantum/quantum_constructor_rewiring.md")
    return p


if __name__ == "__main__":
    build(parser().parse_args())
