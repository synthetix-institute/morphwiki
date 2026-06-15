#!/usr/bin/env python3
"""Build a mechanism-first tree over MorphWiki quantum pages.

The topic pages are generated from Wikipedia article boundaries.  This script
adds a second layer: a quantum-theory tree organized by operational roles rather
than page names or historical taxonomy.  It uses only the exported MorphWiki
JSON pages: route profiles, grammar terms, witness scores, and public summaries.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


ROUTE_LABELS = {
    "transport_flow_route": "state evolution",
    "constraint_closure_route": "normalization and admissibility",
    "spectral_operator_route": "observables and spectra",
    "boundary_weak_form_route": "preparation and boundary context",
    "commutator_incompatibility_route": "incompatible questions",
    "discrete_protocol_route": "controlled update protocol",
}

ROUTE_TO_LAGRANGIAN_BAND = {
    "transport_flow_route": "flow",
    "constraint_closure_route": "constraint",
    "spectral_operator_route": "spectral",
    "boundary_weak_form_route": "boundary",
}

LAGRANGIAN_CLASS_WEIGHTS = {
    "canonical_transfer_path": 0.08,
    "canonical_multiband_transfer_path": 0.06,
    "local_formal_rewrite_or_near_duplicate": 0.035,
    "void_boundary_candidate": 0.045,
    "review_required": -0.025,
}

LAGRANGIAN_CLASS_LABELS = {
    "canonical_transfer_path": "low-action transfer road",
    "canonical_multiband_transfer_path": "multi-band translation road",
    "local_formal_rewrite_or_near_duplicate": "local rewrite basin",
    "void_boundary_candidate": "void-boundary construction target",
    "review_required": "high-tension review path",
}

BRANCHES = {
    "root": {
        "title": "The quantum prediction problem",
        "definition": (
            "Given a context-selected Hilbert space, an admissible state, and a permitted observable, "
            "quantum theory determines which numerical outcomes can occur, assigns probabilities to "
            "those outcomes, and marks which questions cannot be made simultaneously sharp."
        ),
        "query": {
            "spectral_operator_route": 1.0,
            "transport_flow_route": 0.35,
            "commutator_incompatibility_route": 0.25,
            "boundary_weak_form_route": 0.2,
            "constraint_closure_route": 0.15,
            "discrete_protocol_route": 0.05,
        },
        "keywords": [
            "quantum mechanics",
            "mathematical formulation",
            "observable",
            "operator",
            "spectrum",
            "state",
            "probability",
        ],
    },
    "context": {
        "title": "Hilbert-space context: admissible carrier and basis",
        "definition": (
            "A quantum calculation first fixes the Hilbert space, operator domain, basis, preparation "
            "context, representation, gauge, or boundary condition. This is not the measured answer; "
            "it is the legal carrier on which states, transformations, observables, and probabilities "
            "can be defined."
        ),
        "query": {"boundary_weak_form_route": 0.55, "constraint_closure_route": 0.45, "spectral_operator_route": 0.45},
        "keywords": ["hilbert", "basis", "preparation", "representation", "formalism", "domain", "space", "gauge"],
    },
    "states": {
        "title": "State carrier inside Hilbert space",
        "definition": (
            "A state is the probability-bearing element of the selected Hilbert space or its density-operator "
            "state space. Wave functions, density matrices, superpositions, and coherent states are "
            "different representations of this predictive carrier."
        ),
        "query": {"spectral_operator_route": 0.55, "transport_flow_route": 0.25, "constraint_closure_route": 0.25},
        "keywords": ["state", "wave function", "density matrix", "superposition", "coherence", "decoherence"],
    },
    "generators": {
        "title": "Generator: lawful change before readout",
        "definition": (
            "Hamiltonians, unitary maps, equations of motion, and path weights describe the lawful "
            "transport of the state before a question is resolved."
        ),
        "query": {"transport_flow_route": 0.8, "spectral_operator_route": 0.55, "constraint_closure_route": 0.2},
        "keywords": ["hamiltonian", "schrodinger", "unitary", "dynamics", "path integral", "perturbation", "evolution"],
    },
    "observables": {
        "title": "Spectral question: what can be asked",
        "definition": (
            "An observable is a permitted question whose operator form determines the possible numerical answers."
        ),
        "query": {"spectral_operator_route": 1.0, "commutator_incompatibility_route": 0.25},
        "keywords": ["observable", "operator", "self-adjoint", "eigenvalue", "eigenvector", "spectrum", "pauli"],
    },
    "measurement": {
        "title": "Readout rule: how answers become probabilities",
        "definition": (
            "Measurement connects a state and an observable to recorded frequencies.  Projection, "
            "POVMs, Born weights, and collapse language are alternative ways of presenting this "
            "state-to-spectrum readout step."
        ),
        "query": {
            "spectral_operator_route": 0.8,
            "discrete_protocol_route": 0.45,
            "boundary_weak_form_route": 0.25,
            "commutator_incompatibility_route": 0.2,
        },
        "keywords": ["measurement", "born", "povm", "projection", "collapse", "quantum jump", "readout"],
    },
    "incompatibility": {
        "title": "Compatibility limit: what cannot be jointly sharp",
        "definition": (
            "The non-classical part of the theory appears when two otherwise legal questions do "
            "not compose into one common sharp question.  Commutators, uncertainty relations, "
            "contextuality, Bell tests, and entanglement live here."
        ),
        "query": {
            "commutator_incompatibility_route": 0.85,
            "spectral_operator_route": 0.7,
            "constraint_closure_route": 0.35,
            "boundary_weak_form_route": 0.25,
        },
        "keywords": ["commutator", "uncertainty", "entanglement", "bell", "contextual", "epr", "nonlocal"],
    },
    "boundaries": {
        "title": "Boundary realization: how effects appear",
        "definition": (
            "Many named quantum effects are boundary realizations of the same construction.  A "
            "potential, barrier, box, cavity, detector, or medium changes the allowed spectral "
            "channels without changing the basic prediction problem."
        ),
        "query": {"boundary_weak_form_route": 0.85, "spectral_operator_route": 0.65, "transport_flow_route": 0.35},
        "keywords": ["potential", "barrier", "tunnelling", "box", "well", "cavity", "optics", "interference", "scattering"],
    },
    "fields": {
        "title": "Many-mode extension: fields, particles, and scaling",
        "definition": (
            "Quantum field theory, gauge theory, renormalization, photons, fermions, and related "
            "topics extend the same state-operator-spectrum logic to variable particle number, "
            "local fields, and scale-dependent descriptions."
        ),
        "query": {
            "transport_flow_route": 0.65,
            "spectral_operator_route": 0.65,
            "boundary_weak_form_route": 0.45,
            "commutator_incompatibility_route": 0.35,
        },
        "keywords": ["field", "gauge", "renormalization", "photon", "fermion", "boson", "dirac", "electrodynamics", "vacuum"],
    },
    "protocols": {
        "title": "Protocol layer: engineered transformations",
        "definition": (
            "Quantum computing, channels, circuits, algorithms, networks, sensors, and error "
            "correction turn the same formal machinery into controlled sequences of operations."
        ),
        "query": {"discrete_protocol_route": 0.85, "spectral_operator_route": 0.45, "transport_flow_route": 0.35},
        "keywords": ["computing", "circuit", "gate", "algorithm", "channel", "network", "sensor", "information", "error"],
    },
    "annotations": {
        "title": "Annotations: history, interpretations, and popular frames",
        "definition": (
            "Some pages help readers navigate the subject but do not form steps in the mechanism. "
            "They are kept as annotations so books, historical figures, interpretations, and popular "
            "frames do not distort the constructive tree."
        ),
        "query": {"spectral_operator_route": 0.2, "transport_flow_route": 0.2},
        "keywords": ["history", "interpretation", "book", "introduction", "mysticism", "mind", "erwin", "hilbert"],
    },
}

BRANCH_ORDER = [
    "context",
    "states",
    "generators",
    "observables",
    "measurement",
    "incompatibility",
    "boundaries",
    "fields",
    "protocols",
    "annotations",
]

ANNOTATION_RE = re.compile(
    r"\b(history|book|gentle introduction|the quantum universe|mysticism|mind|interpretations|interpretation|qbism|quantum bayesian|relational quantum mechanics|"
    r"copenhagen|many-worlds|consistent histories|erwin|david hilbert|concepts and methods|modern quantum mechanics)\b",
    re.IGNORECASE,
)

CORE_TITLE_PATTERNS = {
    "context": r"\b(hilbert space|basis|mathematical formulation|transformation theory|representation|gauge choice)\b",
    "states": r"\b(quantum state|wave function|density matrix|superposition|decoherence|coherence)\b",
    "generators": r"\b(hamiltonian|schrodinger|unitary|path integral|dynamics|perturbation)\b",
    "observables": r"\b(observable|self-adjoint|operator|spectral theory|eigenvalue|pauli|hilbert)\b",
    "measurement": r"\b(born rule|povm|measurement|collapse|quantum jump)\b",
    "incompatibility": r"\b(entanglement|bell|commutator|uncertainty|nonlocality|epr|einstein.podolsky)\b",
    "boundaries": r"\b(tunnell|particle in a box|potential well|scattering|interference|optics|spectral line)\b",
    "fields": r"\b(quantum field theory|gauge|renormalization|dirac|electrodynamics|chromodynamics|fermion|boson|photon)\b",
    "protocols": r"\b(channel|logic gate|error correction|circuit|algorithm|computing|network|information|key distribution)\b",
    "annotations": r"\b(history|book|introduction|interpretations|mysticism|mind|erwin|hilbert)\b",
}


def load_pages(root: Path) -> List[Dict[str, Any]]:
    page_dir = root / "pages"
    pages = []
    for path in sorted(page_dir.glob("*.json")):
        page = json.loads(path.read_text(encoding="utf-8"))
        page["_path"] = str(path)
        page["_slug"] = path.stem
        pages.append(page)
    return pages


def words(*values: Any) -> Counter:
    text = " ".join(str(v or "") for v in values)
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{2,}", text.lower())
    stop = {
        "the",
        "and",
        "that",
        "with",
        "for",
        "from",
        "this",
        "into",
        "through",
        "which",
        "when",
        "are",
        "not",
        "can",
        "quantum",
        "mechanics",
        "theory",
        "formulation",
    }
    return Counter(t for t in tokens if t not in stop)


def route_vector(page: Mapping[str, Any]) -> Dict[str, float]:
    return {k: float(v or 0.0) for k, v in (page.get("hyperion", {}).get("route_profile") or {}).items()}


def fiber_vector(page: Mapping[str, Any]) -> Dict[str, float]:
    return {k: float(v or 0.0) for k, v in (page.get("hyperion", {}).get("fiber_profile") or {}).items()}


def load_lagrangian_model(root: Path) -> Dict[str, Any]:
    """Load atlas-level Lagrangian paths used as a construction prior.

    The Lagrangian report is not page-indexed.  Pages are therefore projected
    onto the atlas road map by route-band and dominant-fiber compatibility.
    """

    path = root.parent / "operational_geometry" / "atlas_void_lagrangian_report.json"
    if not path.exists():
        return {"available": False, "page_projection_available": False, "path_rows": [], "source": str(path)}
    report = json.loads(path.read_text(encoding="utf-8"))
    rows = report.get("path_rows") or []
    route_signatures = {tuple(row.get("shared_route_bands") or []) for row in rows}
    return {
        "available": True,
        # The current atlas report is path-level, not page-level.  If all path
        # rows share the same route-band signature, projecting Wikipedia pages
        # onto individual road classes would be non-identifiable.
        "page_projection_available": len(route_signatures) > 1,
        "source": str(path),
        "claim_boundary": report.get("claim_boundary", ""),
        "path_rows": rows,
        "summary": report.get("summary") or {},
    }


def active_lagrangian_bands(routes: Mapping[str, float], threshold: float = 0.10) -> set[str]:
    bands = {
        ROUTE_TO_LAGRANGIAN_BAND[key]
        for key, value in routes.items()
        if key in ROUTE_TO_LAGRANGIAN_BAND and float(value or 0.0) >= threshold
    }
    if bands:
        return bands
    best = max(
        ((key, value) for key, value in routes.items() if key in ROUTE_TO_LAGRANGIAN_BAND),
        key=lambda item: float(item[1] or 0.0),
        default=(None, 0.0),
    )
    return {ROUTE_TO_LAGRANGIAN_BAND[best[0]]} if best[0] else set()


def dominant_primary_fiber(fibers: Mapping[str, float]) -> str:
    candidates = {key: float(fibers.get(key, 0.0) or 0.0) for key in ("structure", "spectral", "geometry")}
    if not any(candidates.values()):
        return "unknown"
    return max(candidates.items(), key=lambda item: item[1])[0]


def lagrangian_path_signal(
    routes: Mapping[str, float],
    fibers: Mapping[str, float],
    model: Mapping[str, Any],
) -> Dict[str, Any]:
    bands = active_lagrangian_bands(routes)
    dominant_fiber = dominant_primary_fiber(fibers)
    rows = model.get("path_rows") or []
    if not model.get("available") or not rows:
        return {
            "available": False,
            "global_only": False,
            "active_bands": sorted(bands),
            "dominant_fiber": dominant_fiber,
            "path_class": "unavailable",
            "road_label": "no Lagrangian road map available",
            "road_score": 0.0,
            "branch_bonus": 0.0,
        }
    if not model.get("page_projection_available"):
        return {
            "available": True,
            "global_only": True,
            "active_bands": sorted(bands),
            "dominant_fiber": dominant_fiber,
            "path_class": "global_prior_only",
            "road_label": "global Lagrangian prior only",
            "road_score": 0.0,
            "branch_bonus": 0.0,
            "note": (
                "The atlas Lagrangian report has no discriminative page-level route signature; "
                "true page-level action requires exported 366D page coordinates or witness transition vectors."
            ),
        }

    best_row: Optional[Mapping[str, Any]] = None
    best_score = -1.0
    for row in rows:
        shared = set(str(item) for item in (row.get("shared_route_bands") or []))
        union = bands | shared
        route_match = (len(bands & shared) / len(union)) if union else 0.0
        fiber_pair = {str(row.get("source_dominant_band") or ""), str(row.get("target_dominant_band") or "")}
        fiber_match = 1.0 if dominant_fiber in fiber_pair else 0.35
        transfer = float(row.get("transfer_score") or row.get("gw_score") or 0.0)
        direct = row.get("direct_action") or {}
        action = direct.get("transition_action", direct.get("static_action", row.get("proxy_action_score", 1.0)))
        try:
            action_quality = max(0.0, 1.0 - min(1.0, float(action)))
        except (TypeError, ValueError):
            action_quality = 0.0
        score = 0.52 * route_match + 0.22 * fiber_match + 0.18 * transfer + 0.08 * action_quality
        if score > best_score:
            best_row = row
            best_score = score

    if not best_row:
        return {
            "available": True,
            "active_bands": sorted(bands),
            "dominant_fiber": dominant_fiber,
            "path_class": "unmatched",
            "road_label": "unmatched Lagrangian road",
            "road_score": 0.0,
            "branch_bonus": 0.0,
        }

    path_class = str(best_row.get("path_class") or "unclassified")
    direct = best_row.get("direct_action") or {}
    action_value = direct.get("transition_action", direct.get("static_action", best_row.get("proxy_action_score")))
    return {
        "available": True,
        "active_bands": sorted(bands),
        "dominant_fiber": dominant_fiber,
        "path_class": path_class,
        "road_label": LAGRANGIAN_CLASS_LABELS.get(path_class, path_class.replace("_", " ")),
        "territory_role": best_row.get("territory_role"),
        "road_score": round(best_score, 4),
        "matched_shared_route_bands": best_row.get("shared_route_bands") or [],
        "source_dominant_band": best_row.get("source_dominant_band"),
        "target_dominant_band": best_row.get("target_dominant_band"),
        "transfer_score": round(float(best_row.get("transfer_score") or 0.0), 4),
        "gw_score": round(float(best_row.get("gw_score") or 0.0), 4),
        "action": round(float(action_value), 4) if action_value is not None else None,
        "source_id": best_row.get("source_id"),
        "target_id": best_row.get("target_id"),
    }


def branch_lagrangian_bonus(branch_id: str, signal: Mapping[str, Any]) -> float:
    if not signal.get("available") or signal.get("global_only"):
        return 0.0
    branch_bands = {
        ROUTE_TO_LAGRANGIAN_BAND[key]
        for key in (BRANCHES[branch_id].get("query") or {})
        if key in ROUTE_TO_LAGRANGIAN_BAND
    }
    path_bands = set(str(item) for item in (signal.get("matched_shared_route_bands") or signal.get("active_bands") or []))
    union = branch_bands | path_bands
    overlap = len(branch_bands & path_bands) / len(union) if union else 0.0
    class_weight = LAGRANGIAN_CLASS_WEIGHTS.get(str(signal.get("path_class")), 0.0)
    return class_weight * overlap


def route_dot(left: Mapping[str, float], right: Mapping[str, float]) -> float:
    keys = set(left) | set(right)
    dot = sum(float(left.get(k, 0.0)) * float(right.get(k, 0.0)) for k in keys)
    ln = math.sqrt(sum(float(left.get(k, 0.0)) ** 2 for k in keys))
    rn = math.sqrt(sum(float(right.get(k, 0.0)) ** 2 for k in keys))
    return dot / (ln * rn) if ln and rn else 0.0


def page_counter(page: Mapping[str, Any]) -> Counter:
    mw = page.get("morphwiki", {})
    wiki = page.get("wikipedia", {})
    return words(
        wiki.get("title"),
        wiki.get("description"),
        wiki.get("summary"),
        mw.get("object_view"),
        mw.get("takeaway"),
    )


def title_text(page: Mapping[str, Any]) -> str:
    wiki = page.get("wikipedia", {})
    return " ".join(str(wiki.get(key) or "") for key in ("title", "description")).lower()


def explicit_branch(page: Mapping[str, Any]) -> Optional[str]:
    wiki = page.get("wikipedia", {})
    title_only = str(wiki.get("title") or "").lower()
    text = title_text(page)
    if is_annotation_title(text):
        return "annotations"
    title_overrides = [
        ("states", r"^(quantum state|wave function|density matrix|superposition principle|quantum superposition|coherence|quantum decoherence|two-state quantum system|qubit|quantum fluctuation)$"),
        ("generators", r"^(unitary operator|hamiltonian|hamiltonian \(quantum mechanics\)|schrödinger equation|schrodinger equation|schrödinger picture|path integral|path integral formulation|quantum dynamics|perturbation theory.*|creation and annihilation operators)$"),
        ("observables", r"^(observable|self-adjoint operator|operator theory|operator \(physics\)|spectral theory|eigenvalues and eigenvectors|pauli matrices|angular momentum operator|von neumann algebra)$"),
        ("measurement", r"^(born rule|povm|projection-valued measure|measurement in quantum mechanics|measurement problem|wave function collapse|quantum jump|delayed-choice quantum eraser|quantum eraser experiment)$"),
        ("incompatibility", r"^(bell's theorem|quantum entanglement|commutator|uncertainty principle|einstein.*podolsky.*rosen paradox|quantum nonlocality|wave.*particle duality)$"),
        ("boundaries", r"^(potential well|particle in a box|quantum tunnelling|quantum tunneling|scattering|wave interference|quantum optics|spectral line|s-matrix|quantum imaging|quantum metamaterial|quantum harmonic oscillator|macroscopic quantum phenomena)$"),
        ("fields", r"^(quantum field theory|quantum electrodynamics|quantum chromodynamics|gauge theory|renormalization|dirac equation|klein.*gordon equation|fock space|photon|electron|fermion|boson|string theory|ads/cft correspondence|quantum gravity|loop quantum gravity|quantum geometry|spin network|spin foam|quantum cosmology)$"),
        ("protocols", r"^(quantum information|quantum information science|quantum computing|quantum algorithm|quantum circuit|quantum logic gate|quantum channel|quantum network|quantum error correction|quantum key distribution|quantum teleportation|quantum sensor|quantum metrology|quantum programming|quantum image processing|quantum complexity theory)$"),
    ]
    for branch_id, pattern in title_overrides:
        if re.search(pattern, title_only, re.IGNORECASE):
            return branch_id
    priority_patterns = [
        (
            "context",
            r"\b(hilbert space|mathematical formulation|transformation theory|basis|representation|canonical quantization)\b",
        ),
        (
            "incompatibility",
            r"\b(entanglement|bell|epr|einstein.podolsky|nonlocality|uncertainty|commutator|contextual|complementarity|wave.particle)\b",
        ),
        (
            "measurement",
            r"\b(measurement|povm|collapse|quantum jump|eraser|delayed.choice|detector|born rule)\b",
        ),
        (
            "protocols",
            r"\b(computing|computer|circuit|gate|algorithm|channel|network|cryptography|key distribution|teleportation|sensor|information|programming|finite automaton|error)\b",
        ),
        (
            "boundaries",
            r"\b(tunnell|barrier|particle in a box|potential well|well|box|cavity|optics|interference|scattering|spectral line|metamaterial|imaging)\b",
        ),
        (
            "fields",
            r"\b(field theory|qft|gauge|renormalization|electrodynamics|chromodynamics|dirac|klein.gordon|photon|fermion|boson|fock|ads/cft|spacetime|cosmology|foam)\b",
        ),
        (
            "generators",
            r"\b(hamiltonian|schrodinger|dynamics|path integral|perturbation|unitary|evolution|annihilation|creation)\b",
        ),
        (
            "states",
            r"\b(state|wave function|density matrix|superposition|coherence|decoherence|qubit|spin network|spin foam)\b",
        ),
        (
            "observables",
            r"\b(observable|operator|self.adjoint|eigenvalue|eigenvector|pauli|spectral)\b",
        ),
    ]
    for branch_id, pattern in priority_patterns:
        if re.search(pattern, text):
            return branch_id
    return None


def keyword_score(counter: Counter, keywords: Sequence[str]) -> float:
    if not keywords:
        return 0.0
    hits = 0.0
    for phrase in keywords:
        parts = [p.lower() for p in re.findall(r"[A-Za-z][A-Za-z0-9_+-]{2,}", phrase)]
        if not parts:
            continue
        hits += sum(counter.get(part, 0) for part in parts) / len(parts)
    return min(1.0, math.log1p(hits) / math.log(8.0))


def top_route_name(routes: Mapping[str, float]) -> str:
    if not routes:
        return "unknown"
    key, value = max(routes.items(), key=lambda item: item[1])
    return f"{ROUTE_LABELS.get(key, key)} ({value:.2f})"


def title(page: Mapping[str, Any]) -> str:
    return str(page.get("wikipedia", {}).get("title") or page.get("_slug") or "Untitled")


def is_annotation_title(name: str) -> bool:
    return bool(ANNOTATION_RE.search(name))


def core_priority(branch_id: str, name: str) -> float:
    pattern = CORE_TITLE_PATTERNS.get(branch_id)
    if pattern and re.search(pattern, name, re.IGNORECASE):
        return 1.0
    return 0.0


def assign_pages(
    pages: Sequence[Mapping[str, Any]],
    lagrangian_model: Optional[Mapping[str, Any]] = None,
) -> Tuple[Dict[str, List[Dict[str, Any]]], List[Dict[str, Any]]]:
    assignments: Dict[str, List[Dict[str, Any]]] = {key: [] for key in BRANCH_ORDER}
    page_rows = []
    lagrangian_model = lagrangian_model or {"available": False, "path_rows": []}
    for page in pages:
        counter = page_counter(page)
        routes = route_vector(page)
        fibers = fiber_vector(page)
        lagrangian = lagrangian_path_signal(routes, fibers, lagrangian_model)
        scores = {}
        for branch_id in BRANCH_ORDER:
            branch = BRANCHES[branch_id]
            score = 0.42 * route_dot(routes, branch["query"]) + 0.58 * keyword_score(counter, branch["keywords"])
            score += branch_lagrangian_bonus(branch_id, lagrangian)
            scores[branch_id] = score
        explicit = explicit_branch(page)
        if explicit:
            scores[explicit] += 0.55
        primary = max(scores.items(), key=lambda item: item[1])[0]
        secondary = sorted(scores.items(), key=lambda item: item[1], reverse=True)[1][0]
        page_title = title(page)
        row = {
            "title": page_title,
            "slug": page.get("_slug"),
            "score": round(scores[primary], 4),
            "secondary": secondary,
            "secondary_score": round(scores[secondary], 4),
            "core_priority": core_priority(primary, page_title),
            "is_annotation": is_annotation_title(page_title),
            "top_route": top_route_name(routes),
            "routes": routes,
            "fibers": fibers,
            "lagrangian": lagrangian,
            "takeaway": page.get("morphwiki", {}).get("takeaway", ""),
            "witnesses": len(page.get("hyperion", {}).get("equation_witnesses") or []),
        }
        assignments[primary].append(row)
        page_rows.append(row | {"branch": primary})
    for branch_id, branch_pages in assignments.items():
        branch_pages.sort(
            key=lambda row: (
                not row["is_annotation"],
                row["core_priority"],
                float((row.get("lagrangian") or {}).get("road_score") or 0.0),
                row["score"],
            ),
            reverse=True,
        )
    return assignments, page_rows


def route_stats(pages: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    counts = Counter()
    means: Dict[str, float] = {}
    all_routes = [route_vector(page) for page in pages]
    for key in ROUTE_LABELS:
        vals = [routes.get(key, 0.0) for routes in all_routes]
        means[key] = sum(vals) / max(1, len(vals))
        counts[key] = sum(1 for value in vals if value > 0.1)
    dominant = Counter(max(routes.items(), key=lambda item: item[1])[0] for routes in all_routes if routes)
    return {
        "mean_routes": {key: round(value, 4) for key, value in means.items()},
        "count_gt_0_1": dict(counts),
        "dominant_route_counts": dict(dominant),
    }


ANOMALY_LABEL_EXPLANATIONS = {
    "weak spectral anchor": (
        "another construction step carries the topic before spectra become meaningful"
    ),
    "boundary-driven dynamics": (
        "the experimental context, boundary, apparatus, or representation is part of the mechanism rather than background description"
    ),
    "compatibility/closure junction": (
        "the page joins the rules that make a state legal with the rules that limit which questions can be resolved together"
    ),
    "protocol is unusually explicit": (
        "the order of operations is itself mechanistic; changing the sequence changes what can be inferred or observed"
    ),
    "multi-role hub": (
        "several construction steps meet in one topic, so the page is a junction rather than a clean leaf in the tree"
    ),
    "branch-ambiguous": (
        "the topic belongs at an interface between two explanatory roles and should be read as a bridge, not assigned to one branch too early"
    ),
}


def route_phrase(route_names: Sequence[str]) -> str:
    names = [name for name in route_names if name]
    if not names:
        return "several constructor roles"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f", and {names[-1]}"


def anomaly_context(
    title_value: str,
    labels: Sequence[str],
    branch: Any,
    secondary: Any,
    routes: Mapping[str, float],
    row: Mapping[str, Any],
    entropy: float,
) -> str:
    norm_title = re.sub(r"[^a-z0-9]+", "_", title_value.lower()).strip("_")
    specific = {
        "einstein_podolsky_rosen_paradox": (
            "EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails."
        ),
        "quantum_biology": (
            "Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control."
        ),
        "measurement_problem": (
            "The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning."
        ),
        "quantum_gravity": (
            "Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization."
        ),
        "scattering": (
            "Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints."
        ),
        "quantum_state": (
            "Quantum state is the carrier rather than the final prediction. It precedes admissibility, evolution, observable choice, and probability readout. State whether the carrier is a vector, density operator, field state, or register, and which transformations preserve it."
        ),
        "schr_dinger_s_cat": (
            "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned."
        ),
        "wave_particle_duality": (
            "Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel."
        ),
        "quantum_entanglement": (
            "Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. Separate the joint state, subsystem observables, and correlation test."
        ),
        "fermi_dirac_statistics": (
            "Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. Expose anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space."
        ),
        "hamiltonian_quantum_mechanics": (
            "The Hamiltonian has two roles: it generates time evolution and, as an observable, supplies an energy spectrum. Separate domain/self-adjointness, unitary transport, conserved energy, and spectral readout."
        ),
        "wave_function": (
            "The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. Separate representation, admissibility, evolution, and Born readout."
        ),
        "delayed_choice_quantum_eraser": (
            "The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified."
        ),
        "introduction_to_quantum_mechanics": (
            "An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims."
        ),
        "quantum_simulator": (
            "A quantum simulator is an engineered realization of another Hamiltonian or channel. It is both an observable system and a protocol for representing a target system. Name the simulated target, physical carrier, encoding map, and validation observable."
        ),
        "quantum_cellular_automaton": (
            "A quantum cellular automaton is a locality-preserving update rule. The lattice, neighborhood rule, unitarity or channel condition, and update protocol define the mechanism together."
        ),
        "relativistic_quantum_mechanics": (
            "Relativistic quantum mechanics is a compatibility junction between quantum state evolution and spacetime symmetry. It must preserve relativistic covariance, define the correct state carrier, and explain how spin, energy, and causality constraints enter the operator algebra."
        ),
        "quantum_electrodynamics": (
            "Quantum electrodynamics is a field-interaction constructor. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. Derive it through field operators, gauge constraints, interaction terms, and observable amplitudes."
        ),
    }
    if norm_title in specific:
        return specific[norm_title]
    label_set = set(labels)
    route_rows = sorted(
        ((ROUTE_LABELS.get(key, key), float(value)) for key, value in routes.items()),
        key=lambda item: item[1],
        reverse=True,
    )
    top_roles = route_phrase([label for label, value in route_rows[:3] if value > 0])
    branch_title = BRANCHES.get(str(branch), {}).get("title", str(branch or "the assigned branch"))
    secondary_title = BRANCHES.get(str(secondary), {}).get("title", str(secondary or "the neighboring branch"))
    branch_id = str(branch or "")
    if branch_id == "fields":
        return f"This field-level page mixes {top_roles}. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable."
    if branch_id == "boundaries":
        return f"This boundary page mixes {top_roles}. Read it as a change in domain, interface, potential, or asymptotic channel that changes the allowed readout."
    if branch_id == "measurement":
        return f"This measurement page mixes {top_roles}. Separate the state before readout, the detector or measurement map, the recorded outcome, and the update or conditioning rule."
    if branch_id == "incompatibility":
        return f"This incompatibility page mixes {top_roles}. State which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure."
    if branch_id == "states":
        return f"This state page mixes {top_roles}. Specify the state carrier, then distinguish representation, evolution, admissibility, and later readout."
    if branch_id == "protocols":
        return f"This protocol page mixes {top_roles}. Write it as an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters."
    if "branch-ambiguous" in label_set:
        return f"This page sits between {branch_title} and {secondary_title}. The ambiguity is useful: it marks a place where two constructor roles meet and should be separated before the page is used as a derivation."
    return f"This page activates {top_roles}. Read it as a constructor junction until a topic-native derivation identifies its state carrier, transformation, readout, and compatibility condition."


def anomalies(pages: Sequence[Mapping[str, Any]], page_rows: Sequence[Mapping[str, Any]]) -> List[Dict[str, Any]]:
    rows = []
    for page, row in zip(pages, page_rows):
        if is_annotation_title(title(page)):
            continue
        routes = route_vector(page)
        spectral = routes.get("spectral_operator_route", 0.0)
        transport = routes.get("transport_flow_route", 0.0)
        boundary = routes.get("boundary_weak_form_route", 0.0)
        commutator = routes.get("commutator_incompatibility_route", 0.0)
        protocol = routes.get("discrete_protocol_route", 0.0)
        closure = routes.get("constraint_closure_route", 0.0)
        route_values = list(routes.values())
        entropy = 0.0
        total = sum(route_values)
        if total:
            probs = [v / total for v in route_values if v > 0]
            entropy = -sum(p * math.log(p) for p in probs) / math.log(len(route_values))
        labels = []
        score = 0.0
        if spectral < 0.32:
            labels.append("weak spectral anchor")
            score += 0.5
        if boundary > 0.14 and transport > 0.14:
            labels.append("boundary-driven dynamics")
            score += boundary + transport
        if commutator > 0.13 and closure > 0.07:
            labels.append("compatibility/closure junction")
            score += commutator + closure
        if protocol > 0.07:
            labels.append("protocol is unusually explicit")
            score += 0.5 + protocol
        if entropy > 0.72:
            labels.append("multi-role hub")
            score += entropy
        if row.get("score", 0) - row.get("secondary_score", 0) < 0.035:
            labels.append("branch-ambiguous")
            score += 0.35
        if labels:
            rows.append(
                {
                    "title": title(page),
                    "slug": page.get("_slug"),
                    "labels": labels,
                    "score": round(score, 4),
                    "branch": row.get("branch"),
                    "secondary": row.get("secondary"),
                    "routes": {k: round(v, 4) for k, v in sorted(routes.items())},
                    "takeaway": page.get("morphwiki", {}).get("takeaway", ""),
                    "explanation": anomaly_context(
                        title(page),
                        labels,
                        row.get("branch"),
                        row.get("secondary"),
                        routes,
                        row,
                        entropy,
                    ),
                }
            )
    rows.sort(key=lambda item: item["score"], reverse=True)
    return rows[:24]


def branch_insights(assignments: Mapping[str, Sequence[Mapping[str, Any]]]) -> Dict[str, str]:
    return {
        "context": (
            "This branch is the first step because quantum mechanics is not defined on raw objects. "
            "It begins by specifying the space, basis, representation, or admissibility condition in which states and questions make sense."
        ),
        "states": (
            "The state branch should be introduced before particles.  It is the predictive carrier; particles, "
            "waves, fields, and qubits are later realizations of that carrier."
        ),
        "generators": (
            "Time evolution is a transport problem over states.  The Hamiltonian and path integral are two "
            "views of the same generator role rather than unrelated formalisms."
        ),
        "observables": (
            "The central unit is not a microscopic entity but a legal question.  Spectra make the possible "
            "answers visible."
        ),
        "measurement": (
            "Measurement is best placed after observables and spectra: it is the rule that turns spectral "
            "resolution into recorded probability, not the mystical starting point of the theory."
        ),
        "incompatibility": (
            "The non-classical core appears as failure of joint sharpness.  Entanglement, Bell phenomena, and "
            "uncertainty are different faces of this compatibility structure."
        ),
        "boundaries": (
            "Named effects such as tunnelling and particle-in-a-box are boundary realizations.  They are not "
            "separate conceptual primitives."
        ),
        "fields": (
            "Field theory and gauge theory extend the same construction to many modes, local generators, and "
            "scale-dependent descriptions."
        ),
        "protocols": (
            "Quantum information is the engineering layer: the same state-operator-readout machinery becomes "
            "a controlled sequence of transformations."
        ),
        "annotations": (
            "These pages remain useful for orientation, but they are deliberately not treated as construction steps. "
            "This prevents biographies, books, and interpretations from becoming false roots of the mechanism."
        ),
    }


def render_markdown(report: Mapping[str, Any]) -> str:
    lines = []
    lines.append("# Quantum Theory As A Mechanism Tree")
    lines.append("")
    lines.append("## Root")
    lines.append(report["root"]["definition"])
    lines.append("")
    lines.append("This reorders the topic away from historical names and toward the construction that recurs across the pages:")
    lines.append("")
    lines.append("```text")
    lines.append("SELECTOR -> CARRIER -> MAP -> QUESTION -> READOUT")
    lines.append("    |          |        |         |          |")
    lines.append("    |          |        |         |          +-- probabilities")
    lines.append("    |          |        |         +------------- spectrum / effects")
    lines.append("    |          |        +----------------------- generator or channel")
    lines.append("    |          +-------------------------------- state or density operator")
    lines.append("    +------------------------------------------- Hilbert space and operator domain")
    lines.append("")
    lines.append("COMPATIBILITY constrains which questions can be jointly sharp.")
    lines.append("REALIZATION adds boundaries, fields, detectors, protocols, and scaling limits.")
    lines.append("```")
    lines.append("")
    lines.append("## Re-Derivation Path")
    lines.append("1. **Selector.** A context selects the Hilbert space and operator domain. Euclidean space may label a representation, but Hilbert space is the admissible carrier.")
    lines.append("2. **Carrier.** The state, density operator, field state, or register state carries predictive information on that selected space.")
    lines.append("3. **Map.** A Hamiltonian, unitary, channel, constraint, or action transports the carrier before readout.")
    lines.append("4. **Question.** An observable, effect family, or spectral measure defines the possible answer channels.")
    lines.append("5. **Readout.** The Born or trace rule turns the state and answer channels into probabilities.")
    lines.append("6. **Compatibility and realization.** Commutators, contextuality, uncertainty, boundaries, fields, detectors, and protocols constrain or embody the five-step constructor.")
    lines.append("")
    lines.append("```math")
    lines.append("B \\longmapsto (\\mathcal H_B,\\mathcal D_B)")
    lines.append("\\rho_B\\in\\mathcal S(\\mathcal H_B),\\quad \\rho_B\\ge0,\\quad \\operatorname{Tr}\\rho_B=1")
    lines.append("\\rho_t = U_t \\rho_B U_t^\\dagger")
    lines.append("O = \\sum_i \\lambda_i P_i")
    lines.append("p_i = \\operatorname{Tr}(P_i \\rho_t)")
    lines.append("[O_1,O_2] \\ne 0")
    lines.append("```")
    lines.append("")
    lines.append("## Sparse Attention Summary")
    stats = report["sparse_attention"]
    route_lines = []
    for key, label in ROUTE_LABELS.items():
        route_lines.append(f"{label}: mean {stats['mean_routes'].get(key, 0):.3f}, pages above 0.10 = {stats['count_gt_0_1'].get(key, 0)}")
    lines.extend(f"- {line}" for line in route_lines)
    lines.append("")
    lines.append("Interpretation: the stable evidence signal is observables-and-spectra, but the mechanism tree is not the same object as the evidence ranking.  The tree orders quantum theory by construction role; the route scores explain why each role is supported.")
    lines.append("")
    lag_prior = report.get("lagrangian_construction_prior") or {}
    if lag_prior.get("available"):
        lines.append("## Lagrangian Construction Prior")
        lines.append("")
        lines.append(lag_prior.get("method", ""))
        lines.append("")
        if lag_prior.get("page_projection_available"):
            lines.append("Road classes assigned to pages:")
            for key, count in sorted((lag_prior.get("path_class_counts") or {}).items(), key=lambda item: str(item[0])):
                label = LAGRANGIAN_CLASS_LABELS.get(str(key), str(key).replace("_", " "))
                lines.append(f"- {label}: {count}")
        else:
            lines.append(
                "Page-level road classes are not assigned in this export. The Lagrangian report is used as a global road map; "
                "direct page-level action requires full 366D page coordinates or witness transition vectors."
            )
        lines.append("")
    lines.append("## Tree")
    for branch_id in BRANCH_ORDER:
        branch = report["branches"][branch_id]
        lines.append(f"### {branch['title']}")
        lines.append(branch["definition"])
        lines.append("")
        lines.append(f"Why it belongs here: {branch['insight']}")
        lines.append("")
        lines.append("Representative pages:")
        representatives = [page for page in branch["pages"] if not page.get("is_annotation")]
        if not representatives:
            representatives = branch["pages"]
        show_page_lagrangian = bool((report.get("lagrangian_construction_prior") or {}).get("page_projection_available"))
        for page in representatives[:8]:
            if show_page_lagrangian:
                lag = page.get("lagrangian") or {}
                road = lag.get("road_label", "no Lagrangian road")
                lines.append(f"- {page['title']} - evidence route: {page['top_route']}; Lagrangian road: {road}; assignment score {page['score']:.2f}")
            else:
                lines.append(f"- {page['title']} - evidence route: {page['top_route']}; assignment score {page['score']:.2f}")
        hidden = len(branch["pages"]) - min(len(representatives), 8)
        annotation_count = sum(1 for page in branch["pages"] if page.get("is_annotation"))
        if hidden > 0:
            lines.append(f"- {hidden} more pages in this branch")
        if annotation_count:
            lines.append(f"- {annotation_count} historical, interpretive, or popular pages are treated as annotations, not as conceptual roots")
        lines.append("")
    lines.append("## A New Reading Of Quantum Mechanics")
    lines.append("")
    lines.append(
        "Quantum mechanics can be introduced through a direct constructor order: "
        "first define the Hilbert space, operator domain, and basis; then define a state as a predictive carrier; then define lawful change; "
        "then define legal questions as operators; then show that each question exposes a spectrum of possible answers; "
        "then add the probability rule; only then introduce particles, waves, detectors, barriers, fields, and computers as realizations of this construction."
    )
    lines.append("")
    lines.append(
        "In this reading, the measurement problem is not the root of the subject.  It is a junction where the readout "
        "protocol, context dependence, and incompatible questions meet.  Likewise, tunnelling is not a paradox about a "
        "particle crossing a wall; it is a boundary-shaped spectral channel with non-zero amplitude in a region that "
        "the classical energy description would exclude."
    )
    lines.append("")
    lines.append("## Anomalies And Discovery Leads")
    lines.append("")
    lines.append(
        "These labels describe the role of a page in the mechanism tree, not the physical object named by the page. "
        "For example, a page can be structurally anomalous because context, protocol, or compatibility carries the explanation "
        "before spectra are read out."
    )
    lines.append("")
    lines.append("Label guide:")
    for label, explanation in ANOMALY_LABEL_EXPLANATIONS.items():
        lines.append(f"- **{label}**: {explanation}.")
    lines.append("")
    for item in report["anomalies"][:12]:
        labels = route_phrase(item["labels"])
        explanation = item.get("explanation") or ""
        lines.append(
            f"- **{item['title']}**. {explanation} Flags: {labels}. Branch: {report['branches'][item['branch']]['title']}; "
            f"secondary: {report['branches'][item['secondary']]['title']}."
        )
    lines.append("")
    lines.append("Possible leads:")
    for lead in report["discovery_leads"]:
        lines.append(f"- {lead}")
    lines.append("")
    lines.append("## Boundary")
    lines.append(
        "This tree is a mechanism-indexed synthesis from MorphWiki pages and Hyperion witness profiles.  It supports reading, hypothesis generation, and constructor-target selection; formal derivation and experimental validation promote a proposed mechanism into a physical claim."
    )
    lines.append("")
    return "\n".join(lines)


def build_report(root: Path) -> Dict[str, Any]:
    pages = load_pages(root)
    lagrangian_model = load_lagrangian_model(root)
    assignments, page_rows = assign_pages(pages, lagrangian_model)
    stats = route_stats(pages)
    anomaly_rows = anomalies(pages, page_rows)
    insights = branch_insights(assignments)
    branches = {}
    for branch_id in BRANCH_ORDER:
        branch = BRANCHES[branch_id]
        branches[branch_id] = {
            "title": branch["title"],
            "definition": branch["definition"],
            "insight": insights[branch_id],
            "pages": assignments[branch_id],
        }
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": str(root),
        "root": {
            "title": BRANCHES["root"]["title"],
            "definition": BRANCHES["root"]["definition"],
        },
        "sparse_attention": stats,
        "lagrangian_construction_prior": {
            "available": bool(lagrangian_model.get("available")),
            "page_projection_available": bool(lagrangian_model.get("page_projection_available")),
            "source": lagrangian_model.get("source"),
            "method": (
                "The atlas Lagrangian is used as a global construction constraint: it identifies low-action roads, high-tension paths, and void-boundary targets in the operational atlas. "
                "The current MorphWiki quantum export does not contain 366D page coordinates, so page branches are not directly action-scored. Page-level Lagrangian construction requires exporting full fingerprints or witness transition vectors for each page."
            ),
            "path_class_counts": dict(Counter(str((row.get("lagrangian") or {}).get("path_class")) for row in page_rows)),
        },
        "branches": branches,
        "anomalies": anomaly_rows,
        "discovery_leads": [
            "Search for systems where a state-like carrier and a legal-question operator exist, but the incompatibility relation has not been tested.  Those systems are candidates for quantum-like contextual behavior without importing quantum ontology.",
            "Treat tunnelling, particle-in-a-box, cavity optics, and spectral lines as one family of boundary-shaped spectra.  This suggests looking for overlooked boundary controls in systems currently described only by bulk evolution.",
            "Quantum computing should be read as an engineering layer over the state-operator-readout constructor, not as a separate foundation. New protocols should be searched by composing lawful quantum questions and controlled maps, not by naming new qubit objects.",
            "Pages that are branch-ambiguous are useful: they often mark junctions where two constructions meet, such as field theory joining transport, incompatibility, and boundary context.",
            "Historical, interpretive, and object-name pages should be demoted to annotations.  The conceptual spine is context, state, generator, spectral question, probability, compatibility, realization.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="discoveries/morphwiki_quantum", help="MorphWiki quantum output directory")
    parser.add_argument("--out-json", default=None)
    parser.add_argument("--out-md", default=None)
    args = parser.parse_args()

    root = Path(args.root)
    report = build_report(root)
    out_json = Path(args.out_json) if args.out_json else root / "quantum_mechanism_tree.json"
    out_md = Path(args.out_md) if args.out_md else root / "quantum_mechanism_tree.md"
    out_json.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    out_md.write_text(render_markdown(report), encoding="utf-8")
    print(json.dumps({"json": str(out_json), "markdown": str(out_md), "pages": sum(len(b["pages"]) for b in report["branches"].values())}, indent=2))


if __name__ == "__main__":
    main()
