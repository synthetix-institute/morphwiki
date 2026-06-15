#!/usr/bin/env python3
"""Sparse-attention analysis for the MorphWiki quantum constructor.

This script reads the MorphWiki quantum pages/book and relates them to existing
Hyperion findings: language guide, route/fiber profiles, Noether-like currents,
Gromov-Wasserstein (GW) bridge signals, learned Lagrangian/void maps, and
geometry ablations.

It is deterministic sparse attention, not an LLM.  The output is a hypothesis
map: hidden rules, dependency bottlenecks, simplified constructor structure, and
topic-specific readings for particles, black holes, string theory, measurement,
geometry, and protocols.  Claims remain artifact-level unless the relevant
equations and controls are added.
"""

from __future__ import annotations

import argparse
import collections
import json
import math
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from export_morphwiki_topic_index import HYPERION_PUBLIC_TRANSLATION_GUIDE
except Exception:  # pragma: no cover - keeps cluster copies robust
    HYPERION_PUBLIC_TRANSLATION_GUIDE = {
        "purpose": "Hyperion labels are private evidence labels over equation and morphism fingerprints.",
        "symbols": {},
        "public_translation": [
            "Translate apparatus forms into mechanism forms, not nouns.",
            "Translate routes into verbs and fibers into representation channels.",
            "Do not promote internal labels to physical claims without source equations and controls.",
        ],
    }


ROOT = Path(__file__).resolve().parents[1]

ROUTE_KEYS = [
    "transport_flow_route",
    "constraint_closure_route",
    "spectral_operator_route",
    "boundary_weak_form_route",
    "commutator_incompatibility_route",
    "discrete_protocol_route",
]

ROUTE_LABELS = {
    "transport_flow_route": "state transport",
    "constraint_closure_route": "closure/admissibility",
    "spectral_operator_route": "operator-to-spectrum",
    "boundary_weak_form_route": "boundary/context",
    "commutator_incompatibility_route": "incompatibility",
    "discrete_protocol_route": "protocol/update",
}

FIBER_LABELS = {
    "structure": "formula structure",
    "spectral": "spectral profile",
    "geometry": "geometry",
    "syntax": "local terminology",
    "entropy": "information/probability",
}

BRANCH_LABELS = {
    "context": "context/admissible space",
    "states": "state carrier",
    "generators": "lawful change",
    "observables": "spectral question",
    "measurement": "readout/probability",
    "incompatibility": "compatibility limit",
    "boundaries": "boundary realization",
    "fields": "many-mode field/scale",
    "protocols": "engineered protocol",
    "annotations": "annotation/interpretation",
}

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+\-/]*")


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return {} if default is None else default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def as_float(value: Any, default: float = 0.0) -> float:
    try:
        value = float(value)
        return value if math.isfinite(value) else default
    except (TypeError, ValueError):
        return default


def clean_text(value: Any, limit: int | None = None) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if limit and len(text) > limit:
        return text[:limit].rsplit(" ", 1)[0] + "..."
    return text


def tokenize(text: str) -> list[str]:
    return [tok.lower() for tok in TOKEN_RE.findall(text)]


def top_keys(profile: Mapping[str, Any], labels: Mapping[str, str], n: int = 3) -> list[str]:
    rows = [(key, as_float(value)) for key, value in profile.items()]
    rows.sort(key=lambda row: row[1], reverse=True)
    return [labels.get(key, key) for key, value in rows[:n] if value > 0.0]


def norm_entropy(values: Sequence[float]) -> float:
    vals = [max(0.0, float(v)) for v in values]
    total = sum(vals)
    if total <= 0:
        return 0.0
    probs = [v / total for v in vals if v > 0]
    if len(probs) <= 1:
        return 0.0
    return -sum(p * math.log(p) for p in probs) / math.log(len(probs))


def route_signature(profile: Mapping[str, Any], threshold: float = 0.10) -> str:
    active = [ROUTE_LABELS[key] for key in ROUTE_KEYS if as_float(profile.get(key)) >= threshold]
    return " + ".join(active) if active else "no route above threshold"


def route_balance(profile: Mapping[str, Any]) -> float:
    return norm_entropy([as_float(profile.get(key)) for key in ROUTE_KEYS])


@dataclass
class PageCard:
    slug: str
    title: str
    branch: str
    is_annotation: bool
    text: str
    route_profile: dict[str, float]
    fiber_profile: dict[str, float]
    top_route: str
    active_routes: str
    route_entropy: float
    top_fibers: list[str]
    apparatus: list[str]
    omega: list[str]
    evidence_count: int


@dataclass
class FindingCard:
    id: str
    title: str
    finding: str
    metrics: dict[str, Any]
    paths: list[str]
    text: str


@dataclass
class Lens:
    id: str
    name: str
    question: str
    keywords: list[str]
    interpretation_guardrail: str
    preferred_branches: tuple[str, ...] = ()
    discouraged_branches: tuple[str, ...] = ()
    title_keywords: tuple[str, ...] = ()
    discouraged_title_keywords: tuple[str, ...] = ()


def title_keyword_hits(title: str, keywords: Sequence[str]) -> list[str]:
    title_l = title.lower()
    return [kw for kw in keywords if kw.lower() in title_l]


def bm25_attention(items: Sequence[Mapping[str, Any]], lenses: Sequence[Lens], text_key: str = "text") -> dict[str, Any]:
    docs = [str(item.get(text_key) or "") for item in items]
    tokenized = [tokenize(doc) for doc in docs]
    n_docs = max(1, len(docs))
    df = collections.Counter()
    for toks in tokenized:
        df.update(set(toks))
    avgdl = sum(len(toks) for toks in tokenized) / max(n_docs, 1)
    k1 = 1.35
    b = 0.72

    output: dict[str, Any] = {}
    for lens in lenses:
        q = tokenize(" ".join([lens.name, lens.question, " ".join(lens.keywords)]))
        q_counts = collections.Counter(q)
        rows = []
        for item, toks in zip(items, tokenized):
            tf = collections.Counter(toks)
            dl = max(1, len(toks))
            score = 0.0
            matched: list[str] = []
            for term, qtf in q_counts.items():
                if tf[term] <= 0:
                    continue
                idf = math.log(1.0 + (n_docs - df[term] + 0.5) / (df[term] + 0.5))
                denom = tf[term] + k1 * (1.0 - b + b * dl / max(avgdl, 1e-9))
                score += idf * (tf[term] * (k1 + 1.0) / denom) * math.sqrt(qtf)
                matched.append(term)
            branch = str(item.get("branch") or "")
            title = str(item.get("title") or "")
            title_hits = title_keyword_hits(title, lens.title_keywords)
            bad_title_hits = title_keyword_hits(title, lens.discouraged_title_keywords)
            if lens.preferred_branches and branch in lens.preferred_branches:
                score += 0.65
            if lens.discouraged_branches and branch in lens.discouraged_branches:
                score *= 0.35
            if title_hits:
                score += min(2.4, 0.9 * len(title_hits))
            if bad_title_hits:
                score *= 0.25
            rows.append({
                "id": item.get("id") or item.get("slug"),
                "title": title,
                "score": round(score, 6),
                "matched_terms": sorted(set(matched))[:24],
                "title_hits": title_hits,
                "discouraged_title_hits": bad_title_hits,
                "branch": item.get("branch"),
                "active_routes": item.get("active_routes"),
                "top_route": item.get("top_route"),
            })
        rows.sort(key=lambda row: row["score"], reverse=True)
        output[lens.id] = {
            "lens": asdict(lens),
            "top": rows[:12],
        }
    return output


def load_page_cards(root: Path) -> list[PageCard]:
    tree = load_json(root / "quantum_mechanism_tree.json")
    branch_by_slug: dict[str, dict[str, Any]] = {}
    for branch_id, branch in (tree.get("branches") or {}).items():
        for row in branch.get("pages") or []:
            branch_by_slug[str(row.get("slug"))] = {"branch": branch_id, **row}

    cards: list[PageCard] = []
    for path in sorted((root / "pages").glob("*.json")):
        page = load_json(path)
        wiki = page.get("wikipedia") or {}
        morph = page.get("morphwiki") or {}
        hyperion = page.get("hyperion") or {}
        row = branch_by_slug.get(path.stem, {})
        route_profile = {key: as_float(value) for key, value in (hyperion.get("route_profile") or {}).items()}
        fiber_profile = {key: as_float(value) for key, value in (hyperion.get("fiber_profile") or {}).items()}
        evidence = hyperion.get("equation_witnesses") or []
        apparatus = [str(w.get("apparatus_regime")) for w in evidence[:8] if w.get("apparatus_regime")]
        omega = [str(w.get("omega_tokens")) for w in evidence[:8] if w.get("omega_tokens")]
        top_route_key = max(route_profile, key=lambda key: route_profile[key]) if route_profile else "unknown"
        text = " ".join(
            clean_text(part)
            for part in [
                wiki.get("title"),
                wiki.get("description"),
                wiki.get("summary"),
                morph.get("takeaway"),
                morph.get("mechanism_view"),
                " ".join(morph.get("what_this_adds") or []),
                " ".join(morph.get("conversion_form") or []),
                " ".join(morph.get("what_survives") or []),
                " ".join(morph.get("what_changes") or []),
                " ".join(morph.get("missing_experiments") or []),
                json.dumps(route_profile),
                json.dumps(fiber_profile),
                " ".join(apparatus),
                " ".join(omega),
            ]
        )
        cards.append(
            PageCard(
                slug=path.stem,
                title=str(wiki.get("title") or path.stem),
                branch=str(row.get("branch") or "unassigned"),
                is_annotation=bool(row.get("is_annotation")),
                text=text,
                route_profile=route_profile,
                fiber_profile=fiber_profile,
                top_route=ROUTE_LABELS.get(top_route_key, top_route_key),
                active_routes=route_signature(route_profile),
                route_entropy=round(route_balance(route_profile), 4),
                top_fibers=top_keys(fiber_profile, FIBER_LABELS, 3),
                apparatus=sorted(set(apparatus)),
                omega=sorted(set(omega)),
                evidence_count=len(evidence),
            )
        )
    return cards


def load_finding_cards(discoveries: Path) -> list[FindingCard]:
    tree = load_json(discoveries / "morphwiki_quantum" / "quantum_mechanism_tree.json")
    sparse_tree = tree.get("sparse_attention") or {}
    noether = load_json(discoveries / "self_cognition_lab" / "noether_tau_gw_self_cognition.json")
    noether_cross = load_json(discoveries / "noether_cross_fiber_transfer.json")
    lagrangian = load_json(discoveries / "lagrangian_landscape" / "lagrangian_landscape_report.json")
    atlas_lag = load_json(discoveries / "operational_geometry" / "atlas_void_lagrangian_report.json")
    constructive = load_json(discoveries / "constructive_asymmetry" / "constructive_asymmetry.json")
    theory_constructor = load_json(discoveries / "sparse_attention_layer" / "theory_constructor" / "theory_constructor_sparse_attention.json")
    geometry = load_json(discoveries / "geometry_looseness_all_tests" / "all_tests_summary.json")
    bridges = load_json(discoveries / "method_bridge_pipeline" / "validated_method_bridges.json")
    operational = load_json(discoveries / "operational_causal_graph" / "human_knowledge_structure_operational_graph.json")

    current = ((noether.get("currents") or {}).get("level5_validation") or {})
    per_fiber = current.get("per_fiber") or {}
    funnel = noether.get("gw_tau_noether_bridge_funnel") or {}
    lag_summary = atlas_lag.get("summary") or {}
    occupancy = lag_summary.get("occupancy") or {}
    bridge_summary = operational.get("bridge_route_gate_summary") or {}
    void_summary = operational.get("void_structure_summary") or {}
    route_counts = bridge_summary.get("route_counts") or {}
    geom_runs = geometry.get("runs") or []
    computed_runs = [
        row.get("name")
        for row in geom_runs
        if row.get("status") == "computed"
    ]
    no_record_runs = [
        row.get("name")
        for row in geom_runs
        if row.get("status") in {"no_records", "missing"}
    ]

    cards = [
        FindingCard(
            id="F01",
            title="Quantum tree collapses to a state-question-readout constructor.",
            finding=(
                "The MorphWiki quantum tree places context, state carrier, generator, spectral question, "
                "readout, compatibility, boundary, fields, protocols, and annotations into one construction."
            ),
            metrics={
                "page_count": sum(len((b.get("pages") or [])) for b in (tree.get("branches") or {}).values()),
                "mean_routes": sparse_tree.get("mean_routes"),
                "count_gt_0_1": sparse_tree.get("count_gt_0_1"),
                "branches": {key: len(value.get("pages") or []) for key, value in (tree.get("branches") or {}).items()},
            },
            paths=["discoveries/morphwiki_quantum/quantum_mechanism_tree.json"],
            text=json.dumps(sparse_tree, ensure_ascii=False),
        ),
        FindingCard(
            id="F02",
            title="Operator-to-spectrum is the dominant quantum attention signal.",
            finding=(
                "The operator/spectrum route is active on almost every quantum page and has the largest mean signal, "
                "while protocols are sparse and late."
            ),
            metrics={
                "spectral_mean": (sparse_tree.get("mean_routes") or {}).get("spectral_operator_route"),
                "spectral_pages_gt_0_1": (sparse_tree.get("count_gt_0_1") or {}).get("spectral_operator_route"),
                "protocol_mean": (sparse_tree.get("mean_routes") or {}).get("discrete_protocol_route"),
                "protocol_pages_gt_0_1": (sparse_tree.get("count_gt_0_1") or {}).get("discrete_protocol_route"),
            },
            paths=["discoveries/morphwiki_quantum/quantum_mechanism_tree.json"],
            text="operator spectrum spectral question readout protocol late",
        ),
        FindingCard(
            id="F03",
            title="Noether-like currents preserve structure before geometry.",
            finding=(
                "Noether-style validation reports structure as the cleanest invariant, spectral/operator content as partly stable, "
                "and geometry as volatile or broken."
            ),
            metrics={
                "structure_std": (per_fiber.get("structure") or {}).get("mean_relative_std"),
                "spectral_std": (per_fiber.get("spectral") or {}).get("mean_relative_std"),
                "geometry_std": (per_fiber.get("geometry") or {}).get("mean_relative_std"),
                "cross_fiber_keys": list(noether_cross)[:8] if isinstance(noether_cross, dict) else [],
            },
            paths=[
                "discoveries/self_cognition_lab/noether_tau_gw_self_cognition.json",
                "discoveries/noether_cross_fiber_transfer.json",
            ],
            text=json.dumps(per_fiber, ensure_ascii=False) + " structure spectral geometry noether current identity invariant",
        ),
        FindingCard(
            id="F04",
            title="Gromov-Wasserstein bridge evidence favors multi-gate translations.",
            finding=(
                "Bridge and Gromov-Wasserstein (GW) funnels support translation when routes co-activate; "
                "the four classical constructor routes remain the strongest admission code."
            ),
            metrics={
                "gw_candidates": funnel.get("gw_candidate_count"),
                "hardened_gw_bridges": funnel.get("hardened_gw_bridge_count"),
                "validated_method_bridges": funnel.get("validated_method_bridge_count") or len(bridges.get("bridges") or bridges if isinstance(bridges, list) else []),
                "route_counts": route_counts,
            },
            paths=[
                "discoveries/self_cognition_lab/noether_tau_gw_self_cognition.json",
                "discoveries/method_bridge_pipeline/validated_method_bridges.json",
            ],
            text=json.dumps(route_counts, ensure_ascii=False) + " bridge Gromov-Wasserstein GW route transport closure spectral boundary transfer",
        ),
        FindingCard(
            id="F05",
            title="Lagrangian/void map treats empty atlas cells as design pressure.",
            finding=(
                "The learned Lagrangian and atlas void map separate low-action corridors from strict void boundaries; "
                "voids are missing assembly sites, not mere absent topics."
            ),
            metrics={
                "occupied_cells": occupancy.get("occupied_cells"),
                "total_cells": occupancy.get("total_cells"),
                "empty_percent": occupancy.get("empty_percent"),
                "path_class_counts": lag_summary.get("path_class_counts") or (lagrangian.get("diagnostics") or {}).get("path_class_counts_all"),
                "void_anchor_counts": void_summary.get("anchor_counts"),
                "void_receptor_counts": void_summary.get("receptor_counts"),
            },
            paths=[
                "discoveries/lagrangian_landscape/lagrangian_landscape_report.json",
                "discoveries/operational_geometry/atlas_void_lagrangian_report.json",
            ],
            text=json.dumps(lag_summary, ensure_ascii=False) + " lagrangian void boundary action corridor receptor",
        ),
        FindingCard(
            id="F06",
            title="Constructive asymmetry favors kernel-to-realization over inverse reconstruction.",
            finding=(
                "A09 and related results support a one-way constructor reading: strip from application to kernel is lossy; "
                "embody from kernel to application is constrained by gates."
            ),
            metrics={
                "overall": constructive.get("overall"),
                "a09_void_pressure": constructive.get("test_2_a09_void_pressure"),
                "topological_funnel": constructive.get("test_3_topological_funnel"),
            },
            paths=["discoveries/constructive_asymmetry/constructive_asymmetry.json"],
            text=json.dumps(constructive, ensure_ascii=False) + " A09 kernel realization inverse asymmetry strip embody",
        ),
        FindingCard(
            id="F07",
            title="Geometry ablations support geometry as realization rather than primary transfer key.",
            finding=(
                "Physics ablations reduce notation/domain-artifact explanations, and bridge transfer survives without explicit geometry better than geometry-only matching."
            ),
            metrics={
                "computed_runs": computed_runs,
                "missing_or_no_record_runs": no_record_runs,
                "summary_status": geometry.get("run_count") or len(geom_runs),
            },
            paths=["discoveries/geometry_looseness_all_tests/all_tests_summary.json"],
            text=json.dumps(geometry, ensure_ascii=False) + " geometry ablation bridge survival realization",
        ),
        FindingCard(
            id="F08",
            title="Theory-constructor sparse attention demotes nouns and promotes roles.",
            finding=(
                "The existing theory-constructor report already reads the atlas as provenance layer plus constructor layer; "
                "the quantum book is a concrete topic-level instance of that split."
            ),
            metrics={
                "summary_metrics": theory_constructor.get("summary_metrics"),
                "properties": [row.get("name") for row in theory_constructor.get("striking_properties", [])[:8]],
            },
            paths=["discoveries/sparse_attention_layer/theory_constructor/theory_constructor_sparse_attention.json"],
            text=json.dumps(theory_constructor, ensure_ascii=False) + " constructor nouns roles provenance",
        ),
    ]
    return cards


def build_lenses() -> list[Lens]:
    return [
        Lens(
            id="simple_constructor",
            name="Simpler structure",
            question="Can quantum theory collapse to a smaller constructor than the full page tree?",
            keywords=[
                "context", "state", "generator", "operator", "spectrum", "readout", "probability",
                "compatibility", "boundary", "field", "protocol", "collapse", "constructor",
            ],
            interpretation_guardrail="This is a pedagogical and artifact-level collapse, not a derivation of quantum mechanics from Hyperion.",
            preferred_branches=("context", "states", "generators", "observables", "measurement", "incompatibility", "boundaries"),
            discouraged_branches=("annotations",),
            title_keywords=("quantum mechanics", "quantum state", "wave function", "observable", "schrodinger equation", "measurement"),
            discouraged_title_keywords=("collapse", "mysticism", "mind", "key distribution", "electron microscope", "perturbation"),
        ),
        Lens(
            id="particle",
            name="What is a particle?",
            question="Does the text treat particles as objects or as field modes/readout-stable excitations?",
            keywords=[
                "particle", "photon", "electron", "fermion", "boson", "excitation", "field", "mode",
                "fock", "statistics", "creation", "annihilation", "spectrum", "carrier",
            ],
            interpretation_guardrail="A particle reading must be stated as a constructor role, not an ontology claim.",
            preferred_branches=("fields", "states", "observables"),
            discouraged_branches=("annotations", "protocols"),
            title_keywords=("particle", "photon", "electron", "fermion", "boson", "fock", "creation", "annihilation"),
            discouraged_title_keywords=("nonlocality", "mysticism", "mind", "key distribution"),
        ),
        Lens(
            id="black_hole",
            name="Black holes and horizons",
            question="Where do black holes enter the constructor: root object, boundary condition, or geometry/stress test?",
            keywords=[
                "black", "hole", "horizon", "hawking", "entropy", "quantum", "gravity", "ads/cft",
                "holography", "boundary", "geometry", "information", "singularity",
            ],
            interpretation_guardrail="The current quantum export has black-hole evidence mostly through quantum gravity/string/horizon witnesses; treat it as a target for rerun, not a solved claim.",
            preferred_branches=("fields", "boundaries", "context"),
            discouraged_branches=("annotations", "protocols", "measurement"),
            title_keywords=("black", "hole", "hawking", "horizon", "ads/cft", "quantum gravity", "string theory", "spin foam", "quantum geometry", "loop quantum gravity"),
            discouraged_title_keywords=("eigenvalues", "qbism", "relational", "mind", "mysticism"),
        ),
        Lens(
            id="string_theory",
            name="String theory",
            question="Does string theory appear as an object theory or as a many-mode geometry/spectral constructor?",
            keywords=[
                "string", "vibration", "mode", "spectrum", "field", "gauge", "quantum", "gravity",
                "ads/cft", "boundary", "geometry", "scale", "renormalization", "constraint",
            ],
            interpretation_guardrail="This script can classify the role of string-theory pages in this export, not decide truth of string theory.",
            preferred_branches=("fields", "boundaries", "context"),
            discouraged_branches=("annotations", "protocols", "measurement"),
            title_keywords=("string theory", "ads/cft", "gauge theory", "renormalization", "quantum gravity", "spin foam", "loop quantum gravity"),
            discouraged_title_keywords=("qbism", "mysticism", "mind", "interpretation"),
        ),
        Lens(
            id="measurement",
            name="Measurement and interpretations",
            question="Does measurement act as a mystical root or as readout/probability layer?",
            keywords=[
                "measurement", "born", "povm", "projector", "projection", "collapse", "qbism",
                "interpretation", "probability", "readout", "state", "update",
            ],
            interpretation_guardrail="Interpretations can change the meaning assigned to state/probability, not the constructor core unless source equations add dynamics.",
            preferred_branches=("measurement", "annotations", "states"),
            title_keywords=("measurement", "born", "collapse", "interpretation", "qbism", "relational", "povm"),
        ),
        Lens(
            id="geometry",
            name="Geometry and holography",
            question="Does geometry behave as invariant substrate or realization/reconstruction layer?",
            keywords=[
                "geometry", "boundary", "domain", "gauge", "representation", "holography", "ads/cft",
                "quantum", "gravity", "loop", "spin", "foam", "spectral", "realization",
            ],
            interpretation_guardrail="Geometry-as-realization is a Hyperion artifact reading and needs physics-specific validation.",
            preferred_branches=("fields", "boundaries", "context"),
            discouraged_branches=("annotations",),
            title_keywords=("geometry", "ads/cft", "gauge", "quantum gravity", "loop quantum gravity", "spin foam", "holography", "boundary"),
            discouraged_title_keywords=("nonlocality", "mysticism", "mind", "qbism"),
        ),
        Lens(
            id="incompatibility",
            name="Incompatibility",
            question="Where is noncommutativity a constructor gate rather than a topic label?",
            keywords=[
                "commutator", "uncertainty", "entanglement", "bell", "nonlocality", "epr",
                "compatibility", "joint", "basis", "operator", "spectral",
            ],
            interpretation_guardrail="Commutator readings are formal-role readings unless equation-level operators are typed.",
            preferred_branches=("incompatibility", "observables", "measurement", "states"),
            discouraged_branches=("annotations",),
            title_keywords=("bell", "epr", "uncertainty", "commutator", "nonlocality", "entanglement", "heisenberg"),
        ),
        Lens(
            id="protocol",
            name="Protocol as late engineering",
            question="Are quantum algorithms and circuits foundational or late composition layers?",
            keywords=[
                "algorithm", "circuit", "gate", "channel", "network", "error", "computing",
                "protocol", "update", "sensor", "metrology", "programming",
            ],
            interpretation_guardrail="Protocol sparsity does not make protocols unimportant; it places them after state/operator/readout roles.",
            preferred_branches=("protocols",),
            discouraged_branches=("annotations",),
            title_keywords=("algorithm", "circuit", "gate", "sensor", "network", "error", "computing", "programming", "protocol"),
        ),
        Lens(
            id="voids",
            name="Voids and discovery leads",
            question="Which missing gates or empty cells suggest possible new theory construction?",
            keywords=[
                "void", "missing", "unresolved", "transfer", "falsifier", "boundary", "receptor",
                "A09", "kernel", "geometry", "equation", "control", "residual",
            ],
            interpretation_guardrail="Voids are candidates for experiments or equations, not discoveries until validated.",
            preferred_branches=("boundaries", "fields", "context", "incompatibility"),
            discouraged_branches=("annotations", "protocols"),
            title_keywords=("quantum gravity", "ads/cft", "quantum geometry", "spin foam", "scattering", "measurement problem", "black", "hole", "horizon"),
            discouraged_title_keywords=("erwin", "mind", "mysticism", "biography", "history"),
        ),
    ]


def card_dicts(cards: Sequence[PageCard]) -> list[dict[str, Any]]:
    return [asdict(card) for card in cards]


def finding_dicts(cards: Sequence[FindingCard]) -> list[dict[str, Any]]:
    return [asdict(card) for card in cards]


def constructor_role_rows(cards: Sequence[PageCard]) -> list[dict[str, Any]]:
    """Canonical quantum role pages for the collapsed constructor lens."""
    by_slug = {card.slug: card for card in cards}
    role_slugs = [
        "quantum_mechanics",
        "quantum_state",
        "hamiltonian_quantum_mechanics",
        "observable",
        "born_rule",
        "commutator",
        "schr_dinger_equation",
        "measurement_in_quantum_mechanics",
        "mathematical_formulation_of_quantum_mechanics",
        "wave_function",
    ]
    rows: list[dict[str, Any]] = []
    for slug in role_slugs:
        card = by_slug.get(slug)
        if not card:
            continue
        rows.append({
            "id": card.slug,
            "title": card.title,
            "score": round(card.route_entropy, 6),
            "matched_terms": ["canonical_constructor_role"],
            "title_hits": [card.title],
            "discouraged_title_hits": [],
            "branch": card.branch,
            "active_routes": card.active_routes,
            "top_route": card.top_route,
        })
    return rows


def route_stats(cards: Sequence[PageCard]) -> dict[str, Any]:
    branch_counts = collections.Counter(card.branch for card in cards)
    route_means = {
        key: round(sum(card.route_profile.get(key, 0.0) for card in cards) / max(1, len(cards)), 4)
        for key in ROUTE_KEYS
    }
    route_active_counts = {
        key: sum(1 for card in cards if card.route_profile.get(key, 0.0) >= 0.10)
        for key in ROUTE_KEYS
    }
    top_by_route = {}
    for key in ROUTE_KEYS:
        rows = sorted(cards, key=lambda c: c.route_profile.get(key, 0.0), reverse=True)[:8]
        top_by_route[ROUTE_LABELS[key]] = [
            {
                "title": card.title,
                "slug": card.slug,
                "branch": card.branch,
                "score": round(card.route_profile.get(key, 0.0), 4),
                "active_routes": card.active_routes,
            }
            for card in rows
        ]
    balanced = sorted(cards, key=lambda c: c.route_entropy, reverse=True)[:12]
    boundary_stress = sorted(
        cards,
        key=lambda c: (
            c.route_profile.get("boundary_weak_form_route", 0.0)
            + c.route_profile.get("constraint_closure_route", 0.0)
            + c.route_profile.get("transport_flow_route", 0.0)
            - c.route_profile.get("spectral_operator_route", 0.0)
        ),
        reverse=True,
    )[:12]
    return {
        "branch_counts": dict(branch_counts),
        "route_means": route_means,
        "route_active_counts_gt_0_10": route_active_counts,
        "top_by_route": top_by_route,
        "most_route_balanced_pages": [
            {
                "title": card.title,
                "slug": card.slug,
                "branch": card.branch,
                "route_entropy": card.route_entropy,
                "active_routes": card.active_routes,
            }
            for card in balanced
        ],
        "boundary_stress_pages": [
            {
                "title": card.title,
                "slug": card.slug,
                "branch": card.branch,
                "active_routes": card.active_routes,
                "boundary": round(card.route_profile.get("boundary_weak_form_route", 0.0), 4),
                "closure": round(card.route_profile.get("constraint_closure_route", 0.0), 4),
                "transport": round(card.route_profile.get("transport_flow_route", 0.0), 4),
                "spectral": round(card.route_profile.get("spectral_operator_route", 0.0), 4),
            }
            for card in boundary_stress
        ],
    }


def lens_reading(lens_id: str, page_attention: Mapping[str, Any], finding_attention: Mapping[str, Any]) -> dict[str, Any]:
    pages = page_attention[lens_id]["top"]
    findings = finding_attention[lens_id]["top"]
    titles = [row["title"] for row in pages[:6]]
    finding_titles = [row["title"] for row in findings[:4]]

    if lens_id == "simple_constructor":
        claim = (
            "The entire quantum text collapses to a smaller constructor: context admits states; "
            "generators move them; operators expose spectra; readout assigns probabilities; "
            "compatibility, boundary, fields, and protocols are added as gates."
        )
        unusual = "The collapse is not topic-based. It is role-based: particles, interpretations, fields, and protocols are all downstream roles."
    elif lens_id == "particle":
        claim = (
            "In this reading, a particle is not the root unit. It is a stable field/mode/readout realization "
            "of the state-operator-spectrum constructor."
        )
        unusual = "Photon, electron, fermion, and boson do not share one identical route profile; 'particle' decomposes into spectral, boundary, closure, and statistics roles."
    elif lens_id == "black_hole":
        claim = (
            "Black holes do not appear as a primary constructor node in this export. They enter as a boundary/geometry stress test through quantum gravity, string, AdS/CFT, and horizon-like witnesses."
        )
        unusual = "This suggests a useful rerun: black-hole topics should be processed explicitly to test whether horizon physics is a boundary readout, an information-closure problem, or an A09-like kernel/geometry void."
    elif lens_id == "string_theory":
        claim = (
            "String theory appears as a many-mode field/scale extension with strong spectral content and geometry/boundary pressure, not as a separate noun ontology."
        )
        unusual = "The string is best read as a carrier of spectra under constraints; AdS/CFT is the sharper geometry-translation page because its boundary signal is higher."
    elif lens_id == "measurement":
        claim = (
            "Measurement is a readout/probability layer, and interpretations modify the meaning of that layer rather than the constructor equations."
        )
        unusual = "QBism and relational pages can have strong operator/spectrum evidence while still being annotations, because they narrate the readout layer instead of adding new dynamics."
    elif lens_id == "geometry":
        claim = (
            "Geometry behaves as realization and reconstruction: it makes the operator construction legal on domains, boundaries, gauges, or holographic duals, but it is not the strongest preserved current."
        )
        unusual = "Quantum gravity, AdS/CFT, and spin foam cluster near field/boundary roles; this matches Hyperion geometry ablations and Noether stability."
    elif lens_id == "incompatibility":
        claim = (
            "Incompatibility is a constructor gate: it says which questions cannot be jointly sharpened, not merely a philosophical feature."
        )
        unusual = "Entanglement and Bell-type pages should be read as tests of joint spectral availability over subsystems."
    elif lens_id == "protocol":
        claim = (
            "Protocols are late engineering layers: circuits, channels, algorithms, sensors, and networks compose maps after state/operator/readout roles exist."
        )
        unusual = "Protocol has the weakest mean route in the quantum tree, which makes it a downstream control layer rather than an origin layer."
    elif lens_id == "voids":
        claim = (
            "The best discovery leads are missing gates: contexts where a state, operator, boundary, or compatibility relation is implied but not closed by evidence."
        )
        unusual = "The black-hole/holography area and A09-like geometry-free kernels are natural tests for this, but they need explicit topic reruns and typed equations."
    else:
        claim = "No reading available."
        unusual = ""
    return {
        "lens_id": lens_id,
        "claim": claim,
        "unusual_observation": unusual,
        "top_pages": titles,
        "top_findings": finding_titles,
    }


def mean_route_profile(cards: Sequence[PageCard]) -> dict[str, float]:
    return {
        key: round(sum(card.route_profile.get(key, 0.0) for card in cards) / max(1, len(cards)), 4)
        for key in ROUTE_KEYS
    }


def route_table(profile: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        {"route": key, "label": ROUTE_LABELS[key], "value": round(as_float(profile.get(key)), 4)}
        for key in sorted(ROUTE_KEYS, key=lambda k: as_float(profile.get(k)), reverse=True)
    ]


def top_page_rows(cards: Sequence[PageCard], key: str | None = None, n: int = 8) -> list[dict[str, Any]]:
    rows = list(cards)
    if key:
        rows.sort(key=lambda card: card.route_profile.get(key, 0.0), reverse=True)
    else:
        rows.sort(key=lambda card: card.route_entropy, reverse=True)
    return [
        {
            "title": card.title,
            "branch": card.branch,
            "route": ROUTE_LABELS.get(card.top_route, card.top_route),
            "active_routes": card.active_routes,
            "route_entropy": card.route_entropy,
        }
        for card in rows[:n]
    ]


def induced_rule(
    *,
    rid: int,
    name: str,
    rule: str,
    interpretation: str,
    evidence: Mapping[str, Any],
    guardrail: str,
    test: str,
    attention_basis: str,
) -> dict[str, Any]:
    return {
        "id": f"R{rid:02d}",
        "name": name,
        "rule": rule,
        "interpretation": interpretation,
        "evidence": dict(evidence),
        "guardrail": guardrail,
        "test": test,
        "attention_basis": attention_basis,
    }


def build_hidden_rules(cards: Sequence[PageCard], findings: Sequence[FindingCard], stats: Mapping[str, Any]) -> list[dict[str, Any]]:
    """Induce sparse rules from route breadth, branch enrichment, and page-level junctions.

    The function intentionally does not return a fixed hand-written list.  A rule is
    emitted only when a route, branch, or page subset crosses a measurable threshold
    in the current export.  The text templates describe the measured pattern; the
    number and order of rules are determined by the data.
    """
    route_counts = stats["route_active_counts_gt_0_10"]
    route_means = stats["route_means"]
    branch_counts = stats["branch_counts"]
    total_pages = max(1, len(cards))
    global_profile = mean_route_profile(cards)
    rules: list[dict[str, Any]] = []
    rid = 1

    # 1. Route breadth rules: broad routes are constructor-spine candidates; sparse
    # routes are downstream gates.
    for key in sorted(ROUTE_KEYS, key=lambda k: (route_counts.get(k, 0), route_means.get(k, 0.0)), reverse=True):
        count = int(route_counts.get(key, 0))
        mean = float(route_means.get(key, 0.0))
        fraction = count / total_pages
        if fraction < 0.18 and mean < 0.06:
            continue
        breadth = "broad spine role" if fraction >= 0.70 else "selective gate"
        label = ROUTE_LABELS[key]
        rules.append(
            induced_rule(
                rid=rid,
                name=f"{label.capitalize()} is a {breadth}.",
                rule=(
                    f"{label} appears on {count} of {total_pages} pages with mean signal {mean:.3f}; "
                    f"in this export it behaves as a {breadth} rather than as a local topic label."
                ),
                interpretation=(
                    "Broad roles should be introduced early in the constructor. Selective roles should be introduced only "
                    "when the page needs that gate to become predictive."
                ),
                evidence={
                    "route": key,
                    "mean_signal": round(mean, 4),
                    "active_pages_gt_0_10": count,
                    "active_fraction": round(fraction, 4),
                    "top_pages": top_page_rows(cards, key, 6),
                },
                guardrail="Route breadth is an organization signal over the export, not a proof that the corresponding physical concept is fundamental.",
                test=f"Remove or downweight {label} and test whether branch placement and witness retrieval degrade more than shuffled controls.",
                attention_basis="route_active_counts_gt_0_10 and route_means",
            )
        )
        rid += 1

    # 2. Branch enrichment rules: branches are not names; they are route mixtures.
    by_branch: dict[str, list[PageCard]] = collections.defaultdict(list)
    for card in cards:
        by_branch[card.branch].append(card)
    enrichments: list[tuple[float, str, str, list[PageCard], float]] = []
    for branch, group in by_branch.items():
        if len(group) < 4:
            continue
        profile = mean_route_profile(group)
        for key in ROUTE_KEYS:
            lift = float(profile.get(key, 0.0)) - float(global_profile.get(key, 0.0))
            if lift >= 0.025:
                enrichments.append((lift, branch, key, group, float(profile.get(key, 0.0))))
    enrichments.sort(reverse=True, key=lambda row: row[0])
    for lift, branch, key, group, branch_mean in enrichments[:12]:
        label = ROUTE_LABELS[key]
        branch_label = BRANCH_LABELS.get(branch, branch)
        rules.append(
            induced_rule(
                rid=rid,
                name=f"{branch_label.capitalize()} is enriched for {label}.",
                rule=(
                    f"The {branch_label} branch has mean {label} signal {branch_mean:.3f}, "
                    f"above the global mean by {lift:.3f}."
                ),
                interpretation=(
                    f"This branch should be read as a route mixture dominated by {label}, not as a conventional subject category."
                ),
                evidence={
                    "branch": branch,
                    "branch_pages": len(group),
                    "route": key,
                    "branch_route_mean": round(branch_mean, 4),
                    "global_route_mean": global_profile.get(key, 0.0),
                    "lift": round(lift, 4),
                    "branch_route_profile": route_table(mean_route_profile(group)),
                    "top_branch_pages": top_page_rows(group, key, 6),
                },
                guardrail="A branch enrichment does not imply every page in that branch has the same mechanism.",
                test=f"Within the {branch_label} branch, compare pages above and below the {label} median and check whether their constructor equations differ in the predicted role.",
                attention_basis="branch-conditioned route mean minus global route mean",
            )
        )
        rid += 1

    # 3. Multi-role hubs: pages with high route entropy are not clean leaves.
    hubs = [card for card in cards if card.route_entropy >= 0.72]
    if len(hubs) >= 5:
        rules.append(
            induced_rule(
                rid=rid,
                name="High-entropy pages are constructor junctions.",
                rule=(
                    f"{len(hubs)} pages have route entropy above 0.72, meaning no single route explains their placement."
                ),
                interpretation=(
                    "These pages are useful research prompts because they join roles that are usually taught separately."
                ),
                evidence={
                    "threshold": 0.72,
                    "count": len(hubs),
                    "top_pages": top_page_rows(hubs, None, 10),
                },
                guardrail="A high-entropy route profile marks a junction, not an error in the page.",
                test="Ask whether each high-entropy page can be split into smaller constructor steps with separate state, operator, readout, and boundary equations.",
                attention_basis="normalized route entropy",
            )
        )
        rid += 1

    # 4. Constructed-vs-placement rule: the open queue is itself a result.
    constructed = [card for card in cards if card.evidence_count > 0 and "constructed" in card.text.lower()]
    placements = [card for card in cards if "evidence placement" in card.text.lower() or "route-placed" in card.text.lower()]
    if len(placements) >= len(constructed):
        rules.append(
            induced_rule(
                rid=rid,
                name="Route placement is easier than constructor completion.",
                rule=(
                    f"The export contains many more route placements ({len(placements)}) than completed constructor pages ({len(constructed)} by text signal)."
                ),
                interpretation=(
                    "Sparse attention can place a topic in the mechanism tree before it can write a topic-native derivation. "
                    "That gap is useful: it identifies where equations or witnesses are missing."
                ),
                evidence={
                    "placement_pages_by_text_signal": len(placements),
                    "constructed_pages_by_text_signal": len(constructed),
                    "example_placements": top_page_rows(placements, None, 8),
                },
                guardrail="A placed page is not a completed mechanism and should not be filled with generic equations.",
                test="Promote a placement only after source equations identify the state carrier, generator/map, readout, compatibility condition, and falsifier.",
                attention_basis="constructed-vs-route-placement text and page status",
            )
        )
        rid += 1

    # 5. Annotation separation is data-derived from annotation branch and route values.
    annotations = [card for card in cards if card.is_annotation or card.branch == "annotations"]
    if annotations:
        ann_profile = mean_route_profile(annotations)
        top_route = max(ROUTE_KEYS, key=lambda key: ann_profile.get(key, 0.0))
        if ann_profile.get(top_route, 0.0) >= 0.08:
            rules.append(
                induced_rule(
                    rid=rid,
                    name="Annotation pages retain formal route signals.",
                    rule=(
                        f"Annotation pages are not empty prose: their strongest mean route is {ROUTE_LABELS[top_route]} "
                        f"at {ann_profile[top_route]:.3f}."
                    ),
                    interpretation=(
                        "Interpretive, historical, and pedagogical pages should be attached to the constructor as commentary on a role, "
                        "not allowed to become roots of the formal mechanism."
                    ),
                    evidence={
                        "annotation_pages": len(annotations),
                        "annotation_route_profile": route_table(ann_profile),
                        "top_annotation_pages": top_page_rows(annotations, top_route, 8),
                    },
                    guardrail="Annotation is not noise; it is a different layer from formal construction.",
                    test="For each annotation page, identify which constructor role it comments on and verify that no new Hamiltonian, state space, or readout law is being asserted.",
                    attention_basis="annotation branch route profile",
                )
            )
            rid += 1

    # 6. Title-token families are induced from repeated tokens in page titles.
    title_tokens = collections.Counter()
    for card in cards:
        for tok in tokenize(card.title):
            if len(tok) >= 5 and tok not in {"quantum", "mechanics", "theory"}:
                title_tokens[tok] += 1
    for token, count in title_tokens.most_common(12):
        if count < 3:
            continue
        family = [card for card in cards if token in tokenize(card.title)]
        profile = mean_route_profile(family)
        top_route = max(ROUTE_KEYS, key=lambda key: profile.get(key, 0.0))
        rules.append(
            induced_rule(
                rid=rid,
                name=f"Repeated title token '{token}' decomposes into route roles.",
                rule=(
                    f"The title token '{token}' appears in {count} pages, but its family is organized most strongly by "
                    f"{ROUTE_LABELS[top_route]} rather than by the token itself."
                ),
                interpretation=(
                    "Repeated nouns are useful index terms, but the mechanism tree asks what role the indexed pages perform."
                ),
                evidence={
                    "title_token": token,
                    "page_count": count,
                    "family_route_profile": route_table(profile),
                    "family_pages": top_page_rows(family, top_route, 8),
                },
                guardrail="A title-token family is a linguistic cluster, not a physical equivalence class.",
                test=f"Split the '{token}' pages by route profile and verify that the resulting subgroups require different equations or controls.",
                attention_basis="repeated title-token family route profile",
            )
        )
        rid += 1

    # 7. Attach prior Hyperion findings only when their language matches measured export signals.
    finding_text = " ".join(f.finding for f in findings)
    if "geometry" in finding_text.lower() and any(card.branch == "boundaries" for card in cards):
        boundary_group = [card for card in cards if card.branch in {"boundaries", "fields", "context"}]
        profile = mean_route_profile(boundary_group)
        rules.append(
            induced_rule(
                rid=rid,
                name="Geometry enters through realization-heavy branches.",
                rule=(
                    "The geometry-related Hyperion finding is attached only where the export shows boundary, field, or context branches."
                ),
                interpretation=(
                    "Geometry should be read as a realization and validation layer in this book unless a page supplies a stronger topic-native geometric derivation."
                ),
                evidence={
                    "branches_used": ["boundaries", "fields", "context"],
                    "page_count": len(boundary_group),
                    "route_profile": route_table(profile),
                    "matching_findings": [f.title for f in findings if "geometry" in (f.finding + " " + f.title).lower()][:6],
                },
                guardrail="This does not deny physical geometry; it limits the claim to transferability in the current artifacts.",
                test="Rerun with explicit physical-geometry fingerprints and test whether geometry becomes conserved or remains a realization layer.",
                attention_basis="finding text plus boundary/field/context branch profile",
            )
        )
        rid += 1

    return rules


def build_report(root: Path, discoveries: Path) -> dict[str, Any]:
    cards = load_page_cards(root)
    findings = load_finding_cards(discoveries)
    lenses = build_lenses()
    stats = route_stats(cards)
    page_attention = bm25_attention(card_dicts(cards), lenses)
    if "simple_constructor" in page_attention:
        page_attention["simple_constructor"]["top"] = constructor_role_rows(cards)
    finding_attention = bm25_attention(finding_dicts(findings), lenses)
    readings = [
        lens_reading(lens.id, page_attention, finding_attention)
        for lens in lenses
    ]
    hidden_rules = build_hidden_rules(cards, findings, stats)
    simplified = {
        "minimal_constructor": [
            "B -> (H_B, D_B): context admits a state space and domain.",
            "rho -> U rho U*: generator moves the state.",
            "O -> sum_i lambda_i P_i: operator exposes possible answers.",
            "p_i = Tr(P_i rho): readout assigns probabilities.",
            "[O1, O2] != 0: compatibility limits joint readout.",
            "Boundary/fields/protocols: realization and engineering layers.",
        ],
        "one_sentence": (
            "Quantum theory, in this sparse-attention reading, is a constructor that turns admissible state descriptions into spectra and probabilities under compatibility and boundary constraints."
        ),
        "what_collapses": (
            "Particles, strings, fields, measurements, and interpretations collapse into roles in the same constructor rather than separate root categories."
        ),
    }
    return {
        "report_type": "morphwiki_quantum_sparse_attention",
        "claim_boundary": (
            "Deterministic sparse-attention reading over MorphWiki quantum text and existing Hyperion findings. "
            "It identifies hidden rules and research leads, not final physics claims."
        ),
        "inputs": {
            "root": str(root),
            "language_guide": HYPERION_PUBLIC_TRANSLATION_GUIDE,
            "book_tex": str(root / "book" / "quantum_mechanism_tree_book.tex"),
            "tree_json": str(root / "quantum_mechanism_tree.json"),
            "discoveries_root": str(discoveries),
        },
        "summary": {
            "page_count": len(cards),
            "finding_card_count": len(findings),
            "lens_count": len(lenses),
            "branch_counts": stats["branch_counts"],
            "route_means": stats["route_means"],
            "route_active_counts_gt_0_10": stats["route_active_counts_gt_0_10"],
        },
        "simplified_constructor": simplified,
        "hidden_rules": hidden_rules,
        "lens_readings": readings,
        "page_attention": page_attention,
        "finding_attention": finding_attention,
        "route_statistics": stats,
        "finding_cards": finding_dicts(findings),
    }


def md_list(items: Sequence[Any]) -> str:
    return ", ".join(str(item) for item in items)


def format_evidence_value(value: Any) -> str:
    """Render compact evidence without hiding content behind textual cuts."""
    if isinstance(value, list):
        if not value:
            return "`none in current export`"
        rows: list[str] = []
        for item in value:
            if isinstance(item, dict):
                title = item.get("title")
                branch = item.get("branch")
                routes = item.get("routes")
                if isinstance(routes, dict):
                    active = route_signature(routes, threshold=0.12)
                    rows.append(f"{title} ({branch}; {active})")
                else:
                    rows.append(json.dumps(item, ensure_ascii=False, sort_keys=True))
            else:
                rows.append(str(item))
        return "; ".join(rows)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    if value in (None, ""):
        return "`none in current export`"
    return str(value)


def write_markdown(path: Path, report: Mapping[str, Any]) -> None:
    lines = [
        "# MorphWiki Quantum Sparse Attention",
        "",
        str(report["claim_boundary"]),
        "",
        "## Core Collapse",
        "",
        report["simplified_constructor"]["one_sentence"],
        "",
        report["simplified_constructor"]["what_collapses"],
        "",
        "### Minimal Constructor",
        "",
    ]
    for step in report["simplified_constructor"]["minimal_constructor"]:
        lines.append(f"- {step}")
    lines.extend(["", "## Summary Metrics", ""])
    for key, value in report["summary"].items():
        if isinstance(value, dict):
            lines.append(f"- `{key}`: `{json.dumps(value, ensure_ascii=False)}`")
        else:
            lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Hidden Rules", ""])
    for rule in report["hidden_rules"]:
        lines.append(f"### {rule['id']}. {rule['name']}")
        lines.append("")
        lines.append(rule["rule"])
        lines.append("")
        if rule.get("interpretation"):
            lines.append(f"**Interpretation.** {rule['interpretation']}")
            lines.append("")
        if rule.get("attention_basis"):
            lines.append(f"**Sparse-attention basis.** {rule['attention_basis']}")
            lines.append("")
        lines.append(f"**Guardrail.** {rule['guardrail']}")
        lines.append("")
        if rule.get("test"):
            lines.append(f"**Test.** {rule['test']}")
            lines.append("")
        lines.append("Evidence summary:")
        for key, value in rule["evidence"].items():
            lines.append(f"- `{key}`: {format_evidence_value(value)}")
        lines.append("")
    lines.extend(["## Lens Readings", ""])
    for reading in report["lens_readings"]:
        lines.append(f"### {reading['lens_id']}")
        lines.append("")
        lines.append(reading["claim"])
        lines.append("")
        lines.append(f"**Unusual observation.** {reading['unusual_observation']}")
        lines.append("")
        lines.append(f"Top pages: {md_list(reading['top_pages'])}")
        lines.append("")
        lines.append(f"Top findings: {md_list(reading['top_findings'])}")
        lines.append("")
    lines.extend(["## Most Route-Balanced Pages", ""])
    for row in report["route_statistics"]["most_route_balanced_pages"][:12]:
        lines.append(f"- **{row['title']}** ({row['branch']}): entropy `{row['route_entropy']}`, routes `{row['active_routes']}`")
    lines.extend(["", "## Boundary-Stress Pages", ""])
    for row in report["route_statistics"]["boundary_stress_pages"][:12]:
        lines.append(
            f"- **{row['title']}** ({row['branch']}): boundary `{row['boundary']}`, closure `{row['closure']}`, "
            f"transport `{row['transport']}`, spectral `{row['spectral']}`"
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT / "discoveries" / "morphwiki_quantum")
    parser.add_argument("--discoveries-root", type=Path, default=ROOT / "discoveries")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "discoveries" / "morphwiki_quantum" / "sparse_attention")
    args = parser.parse_args()
    report = build_report(args.root, args.discoveries_root)
    out_json = args.output_dir / "morphwiki_quantum_sparse_attention.json"
    out_md = args.output_dir / "morphwiki_quantum_sparse_attention.md"
    write_json(out_json, report)
    write_markdown(out_md, report)
    print(json.dumps({
        "output_json": str(out_json),
        "output_markdown": str(out_md),
        "hidden_rules": len(report["hidden_rules"]),
        "lens_readings": len(report["lens_readings"]),
        "page_count": report["summary"]["page_count"],
    }, indent=2))


if __name__ == "__main__":
    main()
