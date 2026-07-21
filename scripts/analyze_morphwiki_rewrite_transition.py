#!/usr/bin/env python3
"""Sparse-attention analysis of the MorphWiki quantum rewrite transition.

The transition studied here is:

    Wikipedia/topic view -> derivation-ordered quantum view.

The analysis is deliberately deterministic. It does not claim to infer new
physics by itself; it identifies what became visible when the same topic set was
rewritten by formal quantum roles and cross-checked against exported route/fiber
profiles.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple


ROUTE_LABELS = {
    "transport_flow_route": "state evolution / transport",
    "constraint_closure_route": "normalization / admissibility",
    "spectral_operator_route": "operator-to-spectrum readout",
    "boundary_weak_form_route": "context / boundary realization",
    "commutator_incompatibility_route": "compatibility / non-commutation",
    "discrete_protocol_route": "protocol / engineered sequence",
}

ROLE_KEYWORDS = {
    "context": [
        "context",
        "basis",
        "hilbert",
        "domain",
        "preparation",
        "representation",
        "admissible",
        "gauge",
    ],
    "state": [
        "state",
        "wave function",
        "density",
        "rho",
        "superposition",
        "coherence",
        "qubit",
        "carrier",
    ],
    "generator": [
        "generator",
        "hamiltonian",
        "unitary",
        "evolution",
        "schrodinger",
        "path integral",
        "propagator",
        "transport",
    ],
    "observable": [
        "observable",
        "operator",
        "spectrum",
        "spectral",
        "eigenvalue",
        "projector",
        "measurement operator",
        "self-adjoint",
    ],
    "measurement": [
        "born",
        "probability",
        "readout",
        "measurement",
        "povm",
        "collapse",
        "trace rule",
        "outcome",
    ],
    "incompatibility": [
        "commutator",
        "non-commuting",
        "uncertainty",
        "bell",
        "entanglement",
        "contextual",
        "incompatibility",
        "jointly",
    ],
    "boundary": [
        "boundary",
        "potential",
        "barrier",
        "cavity",
        "box",
        "scattering",
        "tunnelling",
        "interface",
    ],
    "fields": [
        "field",
        "mode",
        "particle",
        "photon",
        "electron",
        "fermion",
        "boson",
        "renormalization",
        "gauge theory",
        "ads/cft",
        "string",
    ],
    "protocol": [
        "protocol",
        "circuit",
        "algorithm",
        "channel",
        "error correction",
        "computing",
        "cryptography",
        "gate",
        "teleportation",
    ],
    "annotation": [
        "interpretation",
        "history",
        "book",
        "mind",
        "mysticism",
        "qbism",
        "relational",
        "observer",
    ],
}

OBJECT_NOUNS = [
    "particle",
    "wave",
    "electron",
    "photon",
    "fermion",
    "boson",
    "atom",
    "molecule",
    "detector",
    "cat",
    "string",
    "field",
    "system",
]

OPERATION_TERMS = [
    "state",
    "operator",
    "spectrum",
    "projector",
    "probability",
    "readout",
    "commutator",
    "boundary",
    "context",
    "generator",
    "evolution",
    "constraint",
    "closure",
    "admissible",
]


def read_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def public_explanation(value: Any) -> str:
    text = clean_text(value)
    replacements = {
        "A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control.": (
            "The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control."
        ),
        "A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control that would remove the quantum contribution.": (
            "The unresolved formal fields are the state carrier, environmental coupling, coherence or transport observable, and the classical control that would remove the quantum contribution."
        ),
        "A rigorous constructor must name the simulated target, the physical carrier, the encoding map, and the validation observable.": (
            "The formal fields are the simulated target, physical carrier, encoding map, and validation observable."
        ),
        "Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning.": (
            "The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning."
        ),
        "Decompose it into mechanism branches before using it for technical claims.": (
            "Its technical content separates into individual branches before supporting specific derivations."
        ),
        "Start from the joint state and local observables, then ask which correlation constraint fails.": (
            "The formal starting point is the joint state and local observables; the question is which correlation constraint fails."
        ),
        "Write it as context selection plus readout channel.": (
            "Its compact form is context selection plus readout channel."
        ),
        "Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.": (
            "The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints."
        ),
        "Specify the state carrier, then distinguish representation, evolution, admissibility, and later readout.": (
            "The relevant fields are the state carrier, representation, evolution, admissibility, and later readout."
        ),
        "Write it as an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters.": (
            "Its formal content is an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters."
        ),
        "two constructor roles meet and should be separated before the page is used as a derivation": (
            "two formal roles meet and require separate treatment before the page supports a derivation"
        ),
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def token_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z][A-Za-z0-9_-]*", text))


def count_terms(text: str, terms: Sequence[str]) -> int:
    low = text.lower()
    total = 0
    for term in terms:
        pat = r"\b" + re.escape(term.lower()).replace(r"\ ", r"\s+") + r"\b"
        total += len(re.findall(pat, low))
    return total


def role_scores(text: str) -> Dict[str, float]:
    denom = max(1, token_count(text) / 250.0)
    scores = {}
    for role, terms in ROLE_KEYWORDS.items():
        scores[role] = round(count_terms(text, terms) / denom, 6)
    return scores


def normalize(scores: Mapping[str, float]) -> Dict[str, float]:
    total = sum(max(0.0, float(v)) for v in scores.values())
    if total <= 0:
        return {k: 0.0 for k in scores}
    return {k: float(v) / total for k, v in scores.items()}


def entropy(prob: Mapping[str, float]) -> float:
    vals = [v for v in prob.values() if v > 0]
    if not vals:
        return 0.0
    return -sum(v * math.log(v) for v in vals)


def top_items(scores: Mapping[str, float], n: int = 3) -> List[Tuple[str, float]]:
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)[:n]


def route_profile(page: Mapping[str, Any]) -> Dict[str, float]:
    routes = page.get("hyperion", {}).get("route_profile") or {}
    return {key: float(routes.get(key, 0.0)) for key in ROUTE_LABELS}


def fiber_profile(page: Mapping[str, Any]) -> Dict[str, float]:
    fibers = page.get("hyperion", {}).get("fiber_profile") or {}
    return {str(k): float(v) for k, v in fibers.items()}


def wikipedia_text(page: Mapping[str, Any]) -> str:
    wiki = page.get("wikipedia") or {}
    morph = page.get("morphwiki") or {}
    pieces = [
        wiki.get("title"),
        wiki.get("description"),
        wiki.get("summary"),
        wiki.get("extract"),
        morph.get("object_view"),
    ]
    return clean_text(" ".join(str(p or "") for p in pieces))


def rewrite_text(page: Mapping[str, Any], derivation_text: str) -> str:
    morph = page.get("morphwiki") or {}
    pieces = [
        morph.get("takeaway"),
        morph.get("mechanism_view"),
        morph.get("what_survives"),
        morph.get("what_changes"),
        morph.get("conversion_form"),
        morph.get("mathematical_skeleton"),
        derivation_text,
    ]
    return clean_text(" ".join(json.dumps(p, ensure_ascii=False) if isinstance(p, (list, dict)) else str(p or "") for p in pieces))


def load_branch_lookup(tree: Mapping[str, Any]) -> Dict[str, Mapping[str, Any]]:
    lookup: Dict[str, Mapping[str, Any]] = {}
    for branch_id, branch in (tree.get("branches") or {}).items():
        for row in branch.get("pages") or []:
            slug = str(row.get("slug") or "")
            if slug:
                merged = dict(row)
                merged["branch"] = branch_id
                merged["branch_title"] = branch.get("title")
                lookup[slug] = merged
    return lookup


def load_anomaly_lookup(tree: Mapping[str, Any]) -> Dict[str, Mapping[str, Any]]:
    return {str(row.get("slug")): row for row in tree.get("anomalies") or [] if row.get("slug")}


def softmax(rows: Sequence[Mapping[str, Any]], key: str) -> List[float]:
    if not rows:
        return []
    vals = [float(row.get(key, 0.0)) for row in rows]
    mx = max(vals)
    exp = [math.exp(v - mx) for v in vals]
    total = sum(exp) or 1.0
    return [v / total for v in exp]


def normalize_status(status: str) -> str:
    """Map legacy and current derivation-page statuses to two audit classes."""
    value = str(status or "").strip()
    if value in {"constructed", "topic_specific", "topic-specific", "topic_specific mechanism"}:
        return "constructed"
    if value in {"evidence_placement", "core_derived", "core-derived", "core_derived mechanism"}:
        return "evidence_placement"
    return value


def make_page_rows(root: Path) -> List[Dict[str, Any]]:
    tree = read_json(root / "quantum_mechanism_tree.json", {})
    branch_lookup = load_branch_lookup(tree)
    anomaly_lookup = load_anomaly_lookup(tree)
    manifest = read_json(root / "derivation_pages" / "manifest.json", {})
    manifest_status = {
        str(row.get("slug")): str(row.get("status") or "")
        for row in manifest.get("pages") or []
        if row.get("slug")
    }
    derivation_dir = root / "derivation_pages"

    rows: List[Dict[str, Any]] = []
    for json_path in sorted((root / "pages").glob("*.json")):
        slug = json_path.stem
        if branch_lookup and slug not in branch_lookup:
            continue
        page = read_json(json_path, {})
        derivation_path = derivation_dir / f"{slug}.md"
        derivation = derivation_path.read_text(encoding="utf-8") if derivation_path.exists() else ""
        pre_text = wikipedia_text(page)
        post_text = rewrite_text(page, derivation)
        pre_roles = role_scores(pre_text)
        post_roles = role_scores(post_text)
        pre_norm = normalize(pre_roles)
        post_norm = normalize(post_roles)
        routes = route_profile(page)
        fibers = fiber_profile(page)
        branch = branch_lookup.get(slug, {})
        anomaly = anomaly_lookup.get(slug)
        object_pre = count_terms(pre_text, OBJECT_NOUNS) / max(1.0, token_count(pre_text) / 250.0)
        object_post = count_terms(post_text, OBJECT_NOUNS) / max(1.0, token_count(post_text) / 250.0)
        operation_pre = count_terms(pre_text, OPERATION_TERMS) / max(1.0, token_count(pre_text) / 250.0)
        operation_post = count_terms(post_text, OPERATION_TERMS) / max(1.0, token_count(post_text) / 250.0)
        role_focus_gain = max(post_norm.values() or [0.0]) - max(pre_norm.values() or [0.0])
        role_entropy_drop = entropy(pre_norm) - entropy(post_norm)
        operation_gain = operation_post - operation_pre
        object_shift = object_post - object_pre
        route_strength = max(routes.values() or [0.0])
        route_balance = entropy(normalize(routes))
        anomaly_score = float(anomaly.get("score", 0.0)) if anomaly else 0.0
        status = manifest_status.get(slug)
        if not status:
            status = (
                "constructed"
                if "## Topic Equations" in derivation or "## Role-Level Equations" in derivation
                else "evidence_placement"
            )
        status = normalize_status(status)
        rows.append(
            {
                "slug": slug,
                "title": page.get("wikipedia", {}).get("title") or slug,
                "status": status,
                "branch": branch.get("branch") or "unresolved",
                "branch_title": branch.get("branch_title") or "Unresolved",
                "secondary": branch.get("secondary"),
                "routes": routes,
                "fibers": fibers,
                "pre_role_scores": pre_roles,
                "post_role_scores": post_roles,
                "pre_role_distribution": pre_norm,
                "post_role_distribution": post_norm,
                "top_pre_roles": top_items(pre_norm, 3),
                "top_post_roles": top_items(post_norm, 3),
                "object_density_pre": round(object_pre, 4),
                "object_density_post": round(object_post, 4),
                "operation_density_pre": round(operation_pre, 4),
                "operation_density_post": round(operation_post, 4),
                "operation_gain": round(operation_gain, 4),
                "object_shift": round(object_shift, 4),
                "role_focus_gain": round(role_focus_gain, 4),
                "role_entropy_drop": round(role_entropy_drop, 4),
                "route_strength": round(route_strength, 4),
                "route_balance_entropy": round(route_balance, 4),
                "anomaly_score": round(anomaly_score, 4),
                "anomaly_labels": anomaly.get("labels", []) if anomaly else [],
                "anomaly_explanation": public_explanation(anomaly.get("explanation", "")) if anomaly else "",
                "anomaly_routes": anomaly.get("routes", {}) if anomaly else {},
                "hyperion_witness_count": len(page.get("hyperion", {}).get("equation_witnesses") or []),
            }
        )

    # Sparse attention: transition gain + evidence + anomaly pressure.
    max_gain = max([abs(r["operation_gain"]) for r in rows] + [1.0])
    max_focus = max([abs(r["role_focus_gain"]) for r in rows] + [1.0])
    max_anomaly = max([r["anomaly_score"] for r in rows] + [1.0])
    for row in rows:
        gain = max(0.0, row["operation_gain"]) / max_gain
        focus = max(0.0, row["role_focus_gain"]) / max_focus
        evidence = row["route_strength"]
        anomaly = row["anomaly_score"] / max_anomaly if max_anomaly else 0.0
        constructed_bonus = 0.05 if row["status"] == "constructed" else 0.0
        row["transition_attention_score"] = round(
            0.35 * gain + 0.2 * focus + 0.25 * evidence + 0.15 * anomaly + constructed_bonus,
            6,
        )
    weights = softmax(rows, "transition_attention_score")
    for row, attn in zip(rows, weights):
        row["transition_attention"] = round(attn, 8)
    return sorted(rows, key=lambda r: r["transition_attention_score"], reverse=True)


def branch_summary(rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    grouped: Dict[str, List[Mapping[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("branch"))].append(row)
    out = []
    for branch, items in sorted(grouped.items(), key=lambda kv: len(kv[1]), reverse=True):
        route_means = {
            key: round(sum(float(item["routes"].get(key, 0.0)) for item in items) / max(1, len(items)), 4)
            for key in ROUTE_LABELS
        }
        out.append(
            {
                "branch": branch,
                "branch_title": items[0].get("branch_title"),
                "count": len(items),
                "constructed": sum(1 for item in items if item.get("status") == "constructed"),
                "mean_operation_gain": round(sum(float(item.get("operation_gain", 0.0)) for item in items) / len(items), 4),
                "mean_route_profile": route_means,
                "top_transition_pages": [
                    {
                        "title": item["title"],
                        "score": item["transition_attention_score"],
                        "top_post_roles": item["top_post_roles"],
                    }
                    for item in sorted(items, key=lambda r: r["transition_attention_score"], reverse=True)[:5]
                ],
            }
        )
    return out


def derive_rules(rows: Sequence[Mapping[str, Any]], tree: Mapping[str, Any]) -> List[Dict[str, Any]]:
    branch_counts = Counter(str(r["branch"]) for r in rows)
    constructed = sum(1 for r in rows if r["status"] == "constructed")
    evidence = len(rows) - constructed
    route_means = {
        key: sum(float(r["routes"].get(key, 0.0)) for r in rows) / max(1, len(rows))
        for key in ROUTE_LABELS
    }
    anomalies = sorted([r for r in rows if r.get("anomaly_labels")], key=lambda r: r["anomaly_score"], reverse=True)

    particle_pages = [
        r for r in rows if re.search(r"\b(photon|electron|fermion|boson|particle|fock|field)\b", str(r["title"]).lower())
    ]
    interpretation_pages = [
        r for r in rows if str(r["branch"]) == "annotations" or re.search(r"\b(qbism|interpretation|relational|mysticism|mind)\b", str(r["title"]).lower())
    ]
    boundary_pages = [r for r in rows if str(r["branch"]) == "boundaries"]
    protocol_pages = [r for r in rows if str(r["branch"]) == "protocols"]

    return [
        {
            "rule": "The rewrite converts a noun-indexed encyclopedia into a derivation graph.",
            "evidence": {
                "page_count": len(rows),
                "branch_counts": dict(branch_counts),
                "constructed_pages": constructed,
                "evidence_placements": evidence,
            },
            "new_information": "The new object is not a better summary of each topic; it is an ordering relation: which topic plays context, state, generator, observable, readout, compatibility, boundary, field, protocol, or annotation.",
        },
        {
            "rule": "The dominant stable role is operator-to-spectrum readout, not object naming.",
            "evidence": {
                "spectral_operator_mean": round(route_means["spectral_operator_route"], 4),
                "transport_mean": round(route_means["transport_flow_route"], 4),
                "closure_mean": round(route_means["constraint_closure_route"], 4),
            },
            "new_information": "The rewrite makes explicit that many named quantum topics become different ways of asking a legal spectral question of a state.",
        },
        {
            "rule": "Particles become stable role-realizations inside field/mode/readout machinery.",
            "evidence": {
                "particle_like_pages": [r["title"] for r in particle_pages[:12]],
                "field_branch_count": branch_counts.get("fields", 0),
            },
            "new_information": "The particle pages are not discarded; they are relocated as field/mode/statistics/readout constructions. This is a more precise statement than 'particles are not fundamental'.",
        },
        {
            "rule": "Interpretations mostly act on state, probability, and update semantics.",
            "evidence": {
                "interpretation_like_pages": [r["title"] for r in interpretation_pages[:12]],
                "annotation_count": branch_counts.get("annotations", 0),
            },
            "new_information": "QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.",
        },
        {
            "rule": "Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.",
            "evidence": {
                "boundary_count": len(boundary_pages),
                "boundary_pages": [r["title"] for r in boundary_pages[:12]],
            },
            "new_information": "Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.",
        },
        {
            "rule": "Protocol pages compose state preparation, maps, and readouts.",
            "evidence": {
                "protocol_count": len(protocol_pages),
                "protocol_pages": [r["title"] for r in protocol_pages[:12]],
                "protocol_route_mean": round(route_means["discrete_protocol_route"], 4),
            },
            "new_information": "Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.",
        },
        {
            "rule": "Anomalies identify where several formal roles coincide.",
            "evidence": {
                "top_anomalies": [
                    {
                        "title": r["title"],
                        "labels": r["anomaly_labels"],
                        "score": r["anomaly_score"],
                        "explanation": r.get("anomaly_explanation", ""),
                        "routes": r.get("anomaly_routes", {}),
                    }
                    for r in anomalies[:8]
                ]
            },
            "new_information": "EPR, the measurement problem, quantum gravity, quantum biology, and related pages combine several formal questions in one topic: state preparation, compatibility, boundary or environmental coupling, protocol order, and readout.",
        },
    ]


def markdown_report(report: Mapping[str, Any]) -> str:
    lines: List[str] = []
    lines.append("# Quantum Rewrite Transition Analysis")
    lines.append("")
    lines.append(
        "This run treats the rewrite itself as the transition from article ordering to derivation ordering. "
        "It asks what becomes visible after quantum pages are sorted by formal role."
    )
    lines.append("")
    metrics = report["summary"]
    lines.append("## Summary")
    lines.append("")
    for key in ["page_count", "constructed_pages", "evidence_placements", "mean_operation_gain", "mean_object_shift"]:
        lines.append(f"- `{key}`: `{metrics[key]}`")
    lines.append("")
    lines.append("### Mean Route Profile")
    lines.append("")
    for key, value in metrics["route_means"].items():
        lines.append(f"- {ROUTE_LABELS.get(key, key)}: `{value}`")
    lines.append("")

    lines.append("## Consequences For The Quantum Presentation")
    lines.append("")
    uses = report["uses"]
    for row in uses:
        lines.append(f"### {row['name']}")
        lines.append("")
        lines.append(row["why_useful"])
        lines.append("")
        lines.append(f"**Required evidence.** {row['evidence_needed']}")
        lines.append("")

    lines.append("## New Information Produced By The Rewrite")
    lines.append("")
    for idx, rule in enumerate(report["rules"], 1):
        lines.append(f"### {idx}. {rule['rule']}")
        lines.append("")
        lines.append(rule["new_information"])
        lines.append("")
        lines.append("Evidence:")
        for k, v in rule["evidence"].items():
            if isinstance(v, list):
                lines.append(f"- `{k}`: " + "; ".join(str(x) for x in v[:12]))
            else:
                lines.append(f"- `{k}`: `{v}`")
        lines.append("")

    lines.append("## Sparse Transition Hotspots")
    lines.append("")
    for row in report["top_transition_pages"][:20]:
        post = ", ".join(f"{name}={score:.2f}" for name, score in row["top_post_roles"])
        labels = ", ".join(row.get("anomaly_labels") or [])
        lines.append(
            f"- **{row['title']}** ({row['branch']}): attention `{row['transition_attention_score']}`, "
            f"operation gain `{row['operation_gain']}`, top roles {post}"
            + (f"; anomaly: {labels}" if labels else "")
        )
        if row.get("anomaly_explanation"):
            lines.append(f"  - Interpretation: {row['anomaly_explanation']}")
    lines.append("")

    lines.append("## Branch-Level Transition")
    lines.append("")
    for branch in report["branch_summary"]:
        lines.append(
            f"- **{branch['branch_title']}**: `{branch['count']}` pages, "
            f"`{branch['constructed']}` constructed, mean operation gain `{branch['mean_operation_gain']}`."
        )
    lines.append("")

    lines.append("## Structural Conclusion")
    lines.append("")
    lines.append(report["practical_conclusion"])
    lines.append("")
    return "\n".join(lines)


def build_report(root: Path) -> Dict[str, Any]:
    tree = read_json(root / "quantum_mechanism_tree.json", {})
    rows = make_page_rows(root)
    route_means = {
        key: round(sum(float(r["routes"].get(key, 0.0)) for r in rows) / max(1, len(rows)), 4)
        for key in ROUTE_LABELS
    }
    constructed = sum(1 for r in rows if r["status"] == "constructed")
    summary = {
        "page_count": len(rows),
        "constructed_pages": constructed,
        "evidence_placements": len(rows) - constructed,
        "mean_operation_gain": round(sum(float(r["operation_gain"]) for r in rows) / max(1, len(rows)), 4),
        "mean_object_shift": round(sum(float(r["object_shift"]) for r in rows) / max(1, len(rows)), 4),
        "route_means": route_means,
    }
    uses = [
        {
            "name": "Derivation order",
            "why_useful": "The domain or Hilbert space precedes the state; the state precedes the generator or measurement map; the spectrum and probability rule precede interpretation. This order keeps particles, protocols, and interpretations downstream of the formal construction they use.",
            "evidence_needed": "A page needs local equations or a clear route placement showing which formal role is being used.",
        },
        {
            "name": "Pages that need explicit equations",
            "why_useful": (
                f"The {constructed} topic-specific pages already supply local equation skeletons. The {len(rows) - constructed} core-derived pages "
                "mark topics where the book can state the expected quantum ingredients, but still needs a page-native state, operator or map, spectrum or readout, compatibility condition, and realization."
            ),
            "evidence_needed": "Clean equation witnesses and page-local role rows linked to the source text.",
        },
        {
            "name": "Role-based topic comparison",
            "why_useful": "Two topics can be compared when they preserve the same state-operator-readout pattern, even if their historical names differ. A valid comparison should keep track of the Hilbert space or domain, operator class, spectrum, probability rule, and compatibility condition.",
            "evidence_needed": "Route profiles, equation witnesses, and a check that the compared topics share the relevant formal roles.",
        },
        {
            "name": "Mixed-role topics",
            "why_useful": "Pages such as EPR, the measurement problem, quantum gravity, and quantum biology combine compatibility, boundary, protocol, and transport roles. They require decomposition into separate formal questions before they can be presented as derivations.",
            "evidence_needed": "Targeted source-equation checks for each role claimed on the page.",
        },
        {
            "name": "Interpretation layer",
            "why_useful": "Interpretive pages change the status assigned to state vectors, probabilities, updates, observers, or recorded outcomes. They do not by themselves replace the Hamiltonian, operator algebra, spectral decomposition, or Born-rule assignment.",
            "evidence_needed": "Explicit separation between formal equations and claims about state, probability, update, or ontology.",
        },
    ]
    report = {
        "schema_version": 1,
        "source": "MorphWiki quantum rewrite transition sparse attention",
        "root": str(root),
        "summary": summary,
        "rules": derive_rules(rows, tree),
        "branch_summary": branch_summary(rows),
        "top_transition_pages": rows[:30],
        "uses": uses,
        "practical_conclusion": (
            "The transition map separates pages with local equation support from pages that still require local equations. "
            "It also identifies mixed-role pages and role-preserving comparisons across topics. The new information is structural: "
            "the topic encyclopedia becomes an ordered set of formal questions and unresolved derivations."
        ),
    }
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="discoveries/morphwiki_quantum")
    parser.add_argument(
        "--out-json",
        default="discoveries/morphwiki_quantum/sparse_attention/morphwiki_rewrite_transition_sparse_attention.json",
    )
    parser.add_argument(
        "--out-md",
        default="discoveries/morphwiki_quantum/sparse_attention/morphwiki_rewrite_transition_sparse_attention.md",
    )
    args = parser.parse_args()

    root = Path(args.root)
    report = build_report(root)
    write_json(Path(args.out_json), report)
    Path(args.out_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_md).write_text(markdown_report(report), encoding="utf-8")
    print(
        json.dumps(
            {
                "json": args.out_json,
                "markdown": args.out_md,
                "pages": report["summary"]["page_count"],
                "constructed_pages": report["summary"]["constructed_pages"],
                "evidence_placements": report["summary"]["evidence_placements"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
