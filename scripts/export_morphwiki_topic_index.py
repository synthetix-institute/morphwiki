#!/usr/bin/env python3
"""Export MorphWiki pages from Wikipedia topics and Hyperion evidence.

MorphWiki is deliberately not a Wikipedia paraphraser.  Wikipedia
supplies the public noun/topic scaffold; Hyperion supplies the operational
mechanism evidence.  An optional LLM may turn selected evidence into smoother
prose, but the exported JSON keeps the source boundary explicit.

Example:

    python -B scripts/export_morphwiki_topic_index.py \
      --topic-preset quantum \
      --hyperion-index discoveries/fieldbridge_static_index/hyperion_static_index.json \
      --out-dir discoveries/morphwiki_quantum

Larger live Wikipedia expansion:

    python -B scripts/export_morphwiki_topic_index.py \
      --topic-preset quantum \
      --expand-wikipedia-links \
      --max-expanded-topics 200 \
      --out-dir discoveries/morphwiki_quantum_expanded

Optional evidence-only LLM synthesis:

    OPENROUTER_API_KEY=sk-or-v1-... \
    python -B scripts/export_morphwiki_topic_index.py ... \
      --openrouter-model openai/gpt-4.1

The LLM step is optional.  If it fails or returns invalid JSON, deterministic
Hyperion evidence synthesis is used.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import socket
import time
import urllib.parse
import urllib.request
import urllib.error
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


ROUTE_KEYS = (
    "transport_flow_route",
    "constraint_closure_route",
    "spectral_operator_route",
    "boundary_weak_form_route",
    "commutator_incompatibility_route",
    "discrete_protocol_route",
)

FIBER_KEYS = ("structure", "spectral", "geometry", "syntax", "entropy")

ROUTE_LABELS = {
    "transport_flow_route": "state evolution / transport",
    "constraint_closure_route": "closure / conservation",
    "spectral_operator_route": "operator and spectrum",
    "boundary_weak_form_route": "boundary or preparation",
    "commutator_incompatibility_route": "non-commuting transformations",
    "discrete_protocol_route": "update protocol",
}

FIBER_LABELS = {
    "structure": "symbolic structure",
    "spectral": "spectral profile",
    "geometry": "geometric realization",
    "syntax": "field-specific vocabulary",
    "entropy": "probability / information",
}

HYPERION_PUBLIC_TRANSLATION_GUIDE = {
    "purpose": (
        "Hyperion labels are a private evidence language over measured equation and morphism fingerprints. "
        "They guide synthesis, but they are not public theory names."
    ),
    "symbols": {
        "Α": "apparatus form: a reusable mechanism role assembled from operator atoms, routes, fibers, and a transformation family",
        "Ω": "operator atom: a local operator or equation motif, not a public noun",
        "R": "route: the operational action carried by a mechanism, such as transport, closure, operator/spectrum, boundary, incompatibility, or protocol",
        "F": "fiber: the evidence carrier or representation channel, such as symbolic structure, spectral profile, geometric realization, field vocabulary, or information profile",
        "Λ": "transformation family: local rewrite or conversion family",
        "Τ": "directed transition: only public when promoted by directed edge evidence",
        "J": "invariant checkpoint: private conservation-candidate diagnostic, not a physical Noether law without equation validation",
    },
    "public_translation": [
        "Translate apparatus forms into mechanism forms, not nouns.",
        "Translate routes into verbs: evolve, close, resolve spectrally, impose a boundary, detect incompatibility, or update by protocol.",
        "Translate fibers into what is preserved or changed by representation: symbolic form, spectral profile, geometric realization, local vocabulary, or information profile.",
        "Keep raw IDs and Greek labels out of public prose. They may appear only in bounded audit evidence or JSON.",
        "Do not claim physical geometry, spectral theory, or a conservation law from an internal band alone; require source equations or explicit witnesses.",
        "Turn a void or missing edge into a constructive transfer experiment: name the state, operator, boundary, readout, and falsifier.",
    ],
}

ROUTE_PATTERNS: Mapping[str, Sequence[str]] = {
    "transport_flow_route": (
        r"\bevolution\b|\bdynamics\b|\bpropagat|\bflow\b|\btransport\b|\bcurrent\b|\bfield equation\b",
        r"\\partial_t|partial_t|Schr[oö]dinger|Hamiltonian|unitary",
    ),
    "constraint_closure_route": (
        r"\bconstraint\b|\bnormalization\b|\bconserved\b|\bconservation\b|\bgauge\b|\bclosure\b|\binvariant\b",
        r"\bprobability\b|\bBorn rule\b|\bunitarity\b|\bsymmetry\b",
    ),
    "spectral_operator_route": (
        r"\boperator\b|\bHamiltonian\b|\bobservable\b|\beigen|\bspectrum\b|\bspectral\b|\bHilbert\b",
        r"\bmode\b|\benergy level\b|\bbasis\b|\bself-adjoint\b",
    ),
    "boundary_weak_form_route": (
        r"\bboundary\b|\bcondition\b|\bapparatus\b|\bmeasurement setup\b|\bpotential\b|\bdomain\b|\bpreparation\b",
        r"\binteraction\b|\bcontext\b|\binterface\b|\bdetector\b",
    ),
    "commutator_incompatibility_route": (
        r"\bcommutator\b|\bnon-commuting\b|\bnoncommuting\b|\buncertainty\b|\bincompatib|\bcomplementarity\b",
        r"\[[^\]]+,[^\]]+\]|\bHeisenberg\b",
    ),
    "discrete_protocol_route": (
        r"\bmeasurement\b|\bupdate\b|\bprojection\b|\bcollapse\b|\bprotocol\b|\biteration\b|\bfeedback\b",
        r"\bstate preparation\b|\bexperiment\b|\bBorn rule\b",
    ),
}

FIBER_PATTERNS: Mapping[str, Sequence[str]] = {
    "structure": (r"\bequation\b|\balgebra\b|\bformalism\b|\boperator\b|\bstate\b|\bcommutator\b",),
    "spectral": (r"\bspectrum\b|\beigen|\bHamiltonian\b|\benergy level\b|\bfrequency\b|\bmode\b",),
    "geometry": (r"\bspace\b|\bspacetime\b|\bmanifold\b|\bcoordinate\b|\bdomain\b|\bboundary\b|\bgeometry\b",),
    "syntax": (r"\bparticle\b|\bwave\b|\belectron\b|\bphoton\b|\bfield\b|\bspin\b|\bqubit\b",),
    "entropy": (r"\bprobability\b|\bdensity matrix\b|\bentropy\b|\binformation\b|\buncertainty\b|\bensemble\b",),
}

ROLE_PATTERNS: Mapping[str, Sequence[str]] = {
    "state": (
        r"\bwave function\b|\bwavefunction\b|\bstate vector\b|\bdensity matrix\b|\bquantum state\b",
        r"\bprobability amplitude\b|\bsuperposition\b|\bfield configuration\b|\bstate\b",
    ),
    "operator": (
        r"\boperator\b|\bHamiltonian\b|\bobservable\b|\bgenerator\b|\bLaplacian\b|\bmatrix\b",
        r"\bcommutator\b|\bunitary\b",
    ),
    "spectrum": (
        r"\beigenvalue\b|\beigenstate\b|\bspectrum\b|\benergy level\b|\bmode\b|\bmeasurement outcome\b",
    ),
    "boundary": (
        r"\bmeasurement apparatus\b|\bdetector\b|\bpotential\b|\bboundary condition\b|\bpreparation\b",
        r"\bexperimental setup\b|\bbasis\b|\bcontext\b|\bdomain\b",
    ),
    "incompatibility": (
        r"\bcommutator\b|\buncertainty\b|\bnon-commuting\b|\bcomplementarity\b|\bincompatible\b",
    ),
    "protocol": (
        r"\bmeasurement\b|\bprojection\b|\bcollapse\b|\bupdate\b|\bBorn rule\b|\bpath integral\b|\bunitary evolution\b",
    ),
}

STOPWORDS = {
    "about",
    "also",
    "and",
    "are",
    "because",
    "been",
    "between",
    "both",
    "but",
    "can",
    "could",
    "does",
    "from",
    "have",
    "into",
    "more",
    "not",
    "only",
    "over",
    "such",
    "that",
    "the",
    "then",
    "there",
    "these",
    "this",
    "those",
    "through",
    "under",
    "using",
    "when",
    "where",
    "which",
    "with",
}

TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9_+-]{2,}")
SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")
BAD_WITNESS_PATTERNS = (
    r"newacronym",
    r"rotatebox",
    r"begin\s*\{tabular\}",
    r"multicolumn",
    r"includegraphics",
    r"bibliograph",
    r"acknowledg",
    r"\\section",
    r"\\caption",
    r"\\label",
)

TOPIC_PRESETS: Mapping[str, Sequence[str]] = {
    "quantum": (
        "Quantum mechanics",
        "Quantum physics",
        "Wave function",
        "Schrödinger equation",
        "Schrödinger picture",
        "Heisenberg picture",
        "Path integral formulation",
        "Path integral",
        "Born rule",
        "Quantum measurement",
        "Measurement problem",
        "Quantum state",
        "Density matrix",
        "Hilbert space",
        "Observable",
        "Hamiltonian mechanics",
        "Hamiltonian operator",
        "Commutator",
        "Canonical commutation relation",
        "Uncertainty principle",
        "Wave–particle duality",
        "Superposition principle",
        "Quantum entanglement",
        "Bell's theorem",
        "EPR paradox",
        "Quantum decoherence",
        "Quantum information",
        "Quantum computation",
        "Qubit",
        "Quantum circuit",
        "Quantum algorithm",
        "Quantum logic gate",
        "Quantum cryptography",
        "Quantum teleportation",
        "Quantum error correction",
        "Quantum field theory",
        "Gauge theory",
        "Quantum electrodynamics",
        "Quantum chromodynamics",
        "Standard Model",
        "Dirac equation",
        "Klein–Gordon equation",
        "Pauli matrices",
        "Spin (physics)",
        "Angular momentum operator",
        "Creation and annihilation operators",
        "Fock space",
        "Eigenvalues and eigenvectors",
        "Spectral theory",
        "Operator theory",
        "Self-adjoint operator",
        "Unitary operator",
        "Projection-valued measure",
        "Positive operator-valued measure",
        "Von Neumann algebra",
        "Heisenberg group",
        "Fourier transform",
        "Quantum harmonic oscillator",
        "Particle in a box",
        "Quantum tunnelling",
        "Potential well",
        "Scattering theory",
        "S-matrix",
        "Perturbation theory",
        "Renormalization",
        "Quantum statistical mechanics",
        "Bose–Einstein statistics",
        "Fermi–Dirac statistics",
        "Boson",
        "Fermion",
        "Photon",
        "Electron",
        "Quantum optics",
        "Quantum gravity",
        "AdS/CFT correspondence",
        "String theory",
    ),
}

RELATED_FILTER_PRESETS: Mapping[str, Sequence[str]] = {
    "quantum": (
        "quantum",
        "wave function",
        "schrödinger",
        "schrodinger",
        "heisenberg",
        "hilbert",
        "hamiltonian",
        "operator",
        "eigen",
        "spectral",
        "commut",
        "uncertainty",
        "born rule",
        "measurement",
        "entangle",
        "decoherence",
        "qubit",
        "fermion",
        "boson",
        "photon",
        "electron",
        "spin",
        "gauge",
        "field theory",
        "path integral",
        "density matrix",
        "fock",
        "unitary",
        "observable",
    ),
}


def compact(value: Any, limit: int = 520) -> str:
    text = " ".join(str(value or "").replace("\r", " ").replace("\n", " ").split())
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def public_text(value: Any) -> str:
    """Normalize public prose without truncating or adding ellipses."""
    return " ".join(str(value or "").replace("\r", " ").replace("\n", " ").split())


def first_public_sentences(value: Any, limit: int = 2) -> str:
    text = public_text(value)
    if not text:
        return ""
    sentences = [sentence.strip() for sentence in SENTENCE_RE.split(text) if sentence.strip()]
    return " ".join(sentences[:limit]) if sentences else text


PUBLIC_INTERNAL_LABEL_RE = re.compile(
    r"(?:[ΑΩΞΛΤ]\d{2}|[ΑΩΞΛΤ]|Λ\d+|Ω\d+|Ξ\d+|J_flat|"
    r"\b(?:transport_flow|constraint_closure|spectral_operator|boundary_weak_form|"
    r"commutator_incompatibility|discrete_protocol)_route\b|"
    r"\b(?:syntax|entropy|geometry|spectral|structure)_fiber\b)"
)
PUBLIC_OVERCLAIM_RE = re.compile(
    r"\b(?:witness|evidence|data)\s+(?:establish(?:es|ed)?|confirm(?:s|ed|ing)?|prov(?:es|ed|ing)?)\b|"
    r"\b(?:confirming|proving)\s+that\b",
    re.IGNORECASE,
)


def public_field_is_safe(value: Any, allow_math: bool = False) -> bool:
    text = str(value or "").strip()
    if not text:
        return False
    if "..." in text or "…" in text:
        return False
    if PUBLIC_INTERNAL_LABEL_RE.search(text):
        return False
    if PUBLIC_OVERCLAIM_RE.search(text):
        return False
    if allow_math and text.count(".") >= 2 and text.count("\n") < 2:
        return False
    if not allow_math and re.search(r"\b[a-z]+_[a-z0-9_]+\b", text):
        return False
    return True


def load_text_excerpt(path: Path, limit: int) -> str:
    if not path or not path.exists() or limit <= 0:
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    return text[:limit].rstrip()


def witness_text(record: Mapping[str, Any]) -> str:
    return " ".join(
        [str(record.get("summary") or ""), str(record.get("invariant") or "")]
        + [str(value) for value in record.get("equations") or []]
    )


def bad_witness_score(text: str) -> float:
    if not text:
        return 1.0
    lower = text.lower()
    pattern_hits = sum(1 for pattern in BAD_WITNESS_PATTERNS if re.search(pattern, lower, re.IGNORECASE))
    brace_rate = (lower.count("{") + lower.count("}")) / max(1, len(lower))
    command_rate = len(re.findall(r"\\[a-zA-Z]{4,}", lower)) / max(1, len(lower.split()))
    nonword_rate = len(re.findall(r"[^A-Za-z0-9\s,.;:()\[\]{}_=+\-*/^\\]", lower)) / max(1, len(lower))
    return min(1.0, 0.24 * pattern_hits + 1.8 * brace_rate + 0.42 * command_rate + 1.2 * nonword_rate)


def clean_enough_witness(record: Mapping[str, Any]) -> bool:
    text = witness_text(record)
    if len(text) < 30:
        return False
    if bad_witness_score(text) > 0.18:
        return False
    return True


def readable_equation_excerpt(record: Mapping[str, Any], limit: int = 180) -> str:
    equations = record.get("equations") or []
    if not equations:
        return ""
    equation = compact(equations[0], limit)
    if re.search(r"\b(begin|end)\s*\{|\brangle\b|\blangle\b|\bfrac\b|\bpartial\b|\blenumi\b|\bmathrm\b", equation, re.IGNORECASE):
        return ""
    if bad_witness_score(equation) > 0.08:
        return ""
    return equation


def slugify(value: str, fallback: str = "topic") -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    return text or fallback


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_env_file(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'\"")
        if key and key not in os.environ:
            os.environ[key] = value


def tokenize(value: Any) -> List[str]:
    return [
        token.lower()
        for token in TOKEN_RE.findall(str(value or ""))
        if token.lower() not in STOPWORDS and not token.lower().startswith("http")
    ]


def counter_from_values(values: Iterable[Any]) -> Counter:
    counts: Counter = Counter()
    for value in values:
        counts.update(tokenize(value))
    return counts


def score_patterns(text: str, patterns: Sequence[str]) -> float:
    hits = sum(1 for pattern in patterns if re.search(pattern, text, re.IGNORECASE))
    return round(max(0.0, min(1.0, 1.0 - math.exp(-0.44 * hits))), 4)


def score_text_routes(text: str) -> Dict[str, float]:
    return {key: score_patterns(text, ROUTE_PATTERNS[key]) for key in ROUTE_KEYS}


def score_text_fibers(text: str) -> Dict[str, float]:
    return {key: score_patterns(text, FIBER_PATTERNS[key]) for key in FIBER_KEYS}


def top_keys(scores: Mapping[str, float], limit: int = 4, threshold: float = 0.05) -> List[str]:
    return [
        key
        for key, value in sorted(scores.items(), key=lambda item: item[1], reverse=True)
        if float(value or 0.0) >= threshold
    ][:limit]


def route_label(route_id: str) -> str:
    return ROUTE_LABELS.get(route_id, route_id.replace("_route", "").replace("_", " "))


def fiber_label(fiber_id: str) -> str:
    return FIBER_LABELS.get(fiber_id, fiber_id.replace("_", " "))


def readable_key_list(keys: Sequence[str], labeler) -> str:
    labels = [labeler(key) for key in keys]
    if not labels:
        return "no dominant mechanism"
    if len(labels) == 1:
        return labels[0]
    return ", ".join(labels[:-1]) + f", and {labels[-1]}"


def normalize_omega_tokens(value: Any) -> List[str]:
    """Return operator-atom ids as complete tokens, not characters.

    Static Hyperion exports may store omega tokens either as a display string
    such as "Ω02 ⊕ Ω07" or as a list.  Treating the display string as an
    iterable produces character-level atoms in public JSON, so normalize before
    counting or indexing.
    """
    if value is None:
        return []
    if isinstance(value, str):
        return re.findall(r"Ω\d+", value)
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        tokens: List[str] = []
        for item in value:
            tokens.extend(normalize_omega_tokens(item))
        return tokens
    return []


def fingerprint_fiber_values(record: Mapping[str, Any]) -> Optional[Dict[str, float]]:
    """Extract real fiber scores from Hyperion band_profile fingerprint data.

    Returns None when the record has no fingerprint band_profile, so callers
    can fall back to regex-scored fibers.
    """
    hyperion = record.get("hyperion") if isinstance(record.get("hyperion"), Mapping) else {}
    band_profile = hyperion.get("band_profile") if isinstance(hyperion.get("band_profile"), Mapping) else {}
    if not band_profile:
        return None
    primary = band_profile.get("primary_ratios") if isinstance(band_profile.get("primary_ratios"), Mapping) else {}
    context = band_profile.get("context_ratios") if isinstance(band_profile.get("context_ratios"), Mapping) else {}
    if not primary and not context:
        return None
    fibers: Dict[str, float] = {}
    for key in FIBER_KEYS:
        fibers[key] = float((primary if key in primary else context).get(key, 0.0) or 0.0)
    # Only return if at least one fiber is non-zero (real data, not empty profile)
    if any(v > 0.0 for v in fibers.values()):
        return fibers
    return None


def vector(record: Mapping[str, Any]) -> List[float]:
    """Build an 11D route+fiber vector for cosine ranking.

    Prefers real fingerprint band_profile data for fibers when available,
    falling back to regex-scored record fibers otherwise.
    """
    routes = record.get("routes") or {}
    fp_fibers = fingerprint_fiber_values(record)
    fibers = fp_fibers if fp_fibers is not None else (record.get("fibers") or {})
    return [float(routes.get(key, 0.0) or 0.0) for key in ROUTE_KEYS] + [
        float(fibers.get(key, 0.0) or 0.0) for key in FIBER_KEYS
    ]


def topic_vector(routes: Mapping[str, float], fibers: Mapping[str, float]) -> List[float]:
    return [float(routes.get(key, 0.0) or 0.0) for key in ROUTE_KEYS] + [
        float(fibers.get(key, 0.0) or 0.0) for key in FIBER_KEYS
    ]


def cosine(left: Sequence[float], right: Sequence[float]) -> float:
    dot = sum(a * b for a, b in zip(left, right))
    ln = math.sqrt(sum(a * a for a in left))
    rn = math.sqrt(sum(b * b for b in right))
    return dot / (ln * rn) if ln and rn else 0.0


def lexical_overlap(left: Counter, right: Counter) -> float:
    if not left or not right:
        return 0.0
    overlap = sum(min(weight, right.get(term, 0)) for term, weight in left.items())
    denom = sum(left.values())
    return overlap / denom if denom else 0.0


def fetch_url_json(
    url: str,
    user_agent: str,
    timeout: int = 60,
    retries: int = 4,
    backoff_seconds: float = 2.0,
) -> Any:
    last_error: Optional[BaseException] = None
    for attempt in range(max(1, retries)):
        request = urllib.request.Request(url, headers={"User-Agent": user_agent})
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, socket.timeout, OSError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt + 1 >= max(1, retries):
                break
            sleep_for = backoff_seconds * (attempt + 1)
            print(f"[MorphWiki] fetch retry {attempt + 2}/{retries} after {type(exc).__name__}: {url}")
            time.sleep(sleep_for)
    raise RuntimeError(f"Could not fetch {url}: {last_error}")


def wikipedia_action_url(title: str, lang: str) -> str:
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|info",
        "explaintext": "1",
        "redirects": "1",
        "inprop": "url",
        "titles": title,
    }
    return f"https://{lang}.wikipedia.org/w/api.php?{urllib.parse.urlencode(params)}"


def wikipedia_summary_url(title: str, lang: str) -> str:
    encoded = urllib.parse.quote(title.replace(" ", "_"))
    return f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{encoded}"


def wikipedia_links_url(title: str, lang: str, plcontinue: str = "") -> str:
    params = {
        "action": "query",
        "format": "json",
        "prop": "links",
        "plnamespace": "0",
        "pllimit": "max",
        "redirects": "1",
        "titles": title,
    }
    if plcontinue:
        params["continue"] = ""
        params["plcontinue"] = plcontinue
    return f"https://{lang}.wikipedia.org/w/api.php?{urllib.parse.urlencode(params)}"


def fetch_wikipedia_links(
    title: str,
    lang: str,
    user_agent: str,
    max_links: int = 500,
    sleep_seconds: float = 0.1,
    timeout: int = 60,
    retries: int = 4,
) -> List[str]:
    links: List[str] = []
    plcontinue = ""
    while len(links) < max_links:
        payload = fetch_url_json(wikipedia_links_url(title, lang, plcontinue), user_agent, timeout=timeout, retries=retries)
        pages = (payload.get("query") or {}).get("pages") or {}
        for page in pages.values():
            for link in page.get("links") or []:
                linked_title = link.get("title")
                if linked_title:
                    links.append(str(linked_title))
                    if len(links) >= max_links:
                        break
            if len(links) >= max_links:
                break
        cont = payload.get("continue") or {}
        plcontinue = str(cont.get("plcontinue") or "")
        if not plcontinue:
            break
        if sleep_seconds:
            time.sleep(sleep_seconds)
    return links


def fetch_cached_wikipedia_links(
    title: str,
    cache_dir: Path,
    lang: str,
    user_agent: str,
    max_links: int,
    use_cache: bool = True,
    timeout: int = 60,
    retries: int = 4,
) -> List[str]:
    cache_path = cache_dir / f"{lang}_{slugify(title)}_links.json"
    if use_cache and cache_path.exists():
        payload = read_json(cache_path)
        links = payload.get("links") if isinstance(payload, Mapping) else None
        if isinstance(links, list):
            return [str(link) for link in links]
    links = fetch_wikipedia_links(title, lang, user_agent, max_links=max_links, timeout=timeout, retries=retries)
    write_json(cache_path, {"title": title, "lang": lang, "links": links})
    return links


def title_matches_filters(title: str, filters: Sequence[str]) -> bool:
    low = title.lower()
    if any(ns in low for ns in ("list of", "glossary of", "timeline of", "index of", "outline of")):
        return False
    if re.search(r"\b(category|template|portal|help|file|wikipedia):", low):
        return False
    return any(term.lower() in low for term in filters)


def fetch_wikipedia_topic(
    title: str,
    cache_dir: Path,
    lang: str,
    user_agent: str,
    use_cache: bool = True,
    sleep_seconds: float = 0.1,
    timeout: int = 60,
    retries: int = 4,
) -> Dict[str, Any]:
    cache_path = cache_dir / f"{lang}_{slugify(title)}.json"
    if use_cache and cache_path.exists():
        return read_json(cache_path)

    summary: Dict[str, Any] = {}
    action: Dict[str, Any] = {}
    summary_error: Optional[BaseException] = None
    action_error: Optional[BaseException] = None
    try:
        summary = fetch_url_json(wikipedia_summary_url(title, lang), user_agent, timeout=timeout, retries=retries)
    except Exception as exc:
        summary_error = exc
        print(f"[MorphWiki] warning: Wikipedia summary failed for {title}: {exc}")
    if sleep_seconds:
        time.sleep(sleep_seconds)
    try:
        action = fetch_url_json(wikipedia_action_url(title, lang), user_agent, timeout=timeout, retries=retries)
    except Exception as exc:
        action_error = exc
        print(f"[MorphWiki] warning: Wikipedia content failed for {title}: {exc}")
    if not summary and not action:
        raise RuntimeError(f"Wikipedia fetch failed for {title}: summary={summary_error}; content={action_error}")
    pages = (action.get("query") or {}).get("pages") or {}
    page = next(iter(pages.values()), {})
    payload = {
        "title": page.get("title") or summary.get("title") or title,
        "pageid": page.get("pageid") or summary.get("pageid"),
        "url": page.get("fullurl") or (summary.get("content_urls") or {}).get("desktop", {}).get("page"),
        "summary": summary.get("extract") or "",
        "description": summary.get("description") or "",
        "extract": page.get("extract") or summary.get("extract") or "",
        "lang": lang,
        "license_note": "Wikipedia text is CC BY-SA; this export uses Wikipedia as the topic scaffold and keeps attribution metadata.",
        "source_api": {
            "summary": wikipedia_summary_url(title, lang),
            "content": wikipedia_action_url(title, lang),
        },
    }
    write_json(cache_path, payload)
    return payload


def record_counter(record: Mapping[str, Any]) -> Counter:
    values: List[Any] = []
    for key in ("title", "summary", "invariant"):
        values.append(record.get(key))
    for key in ("keywords", "variables", "equations", "measurements", "controls", "references"):
        values.extend(record.get(key) or [])
    hyperion = record.get("hyperion") or {}
    for key in ("paper_id", "apparatus_regime", "display_name", "fiber_profile"):
        values.append(hyperion.get(key))
    values.extend(normalize_omega_tokens(hyperion.get("omega_tokens")))
    return counter_from_values(values)


def rank_records(topic: Mapping[str, Any], records: Sequence[Mapping[str, Any]], limit: int) -> Tuple[List[Dict[str, Any]], Dict[str, float], Dict[str, float]]:
    topic_text = " ".join([topic.get("title", ""), topic.get("description", ""), topic.get("summary", ""), topic.get("extract", "")[:14000]])
    topic_routes = score_text_routes(topic_text)
    topic_fibers = score_text_fibers(topic_text)
    topic_terms = counter_from_values([topic_text])
    tv = topic_vector(topic_routes, topic_fibers)
    ranked: List[Dict[str, Any]] = []
    for record in records:
        if not clean_enough_witness(record):
            continue
        rv = vector(record)
        route_score = cosine(tv, rv)
        text_score = lexical_overlap(topic_terms, record_counter(record))
        equation_bonus = 0.0
        equations = " ".join(record.get("equations") or [])
        if re.search(r"Hamiltonian|Schr[oö]dinger|wavefunction|wave function|density matrix|commutator|eigen", equations, re.I):
            equation_bonus = 0.08
        quality_penalty = 0.12 * bad_witness_score(witness_text(record))
        total = 0.55 * route_score + 0.37 * text_score + equation_bonus - quality_penalty
        row = dict(record)
        row["_morphwiki_score"] = round(total, 6)
        row["_route_score"] = round(route_score, 6)
        row["_lexical_score"] = round(text_score, 6)
        ranked.append(row)
    ranked.sort(key=lambda row: row["_morphwiki_score"], reverse=True)
    return ranked[:limit], topic_routes, topic_fibers


def average_profile(records: Sequence[Mapping[str, Any]], kind: str, keys: Sequence[str]) -> Dict[str, float]:
    if not records:
        return {key: 0.0 for key in keys}
    out: Dict[str, float] = {}
    for key in keys:
        total = 0.0
        for record in records:
            if kind == "fibers":
                values = fingerprint_fiber_values(record) or (record.get("fibers") or {})
            else:
                values = record.get(kind) or {}
            total += float(values.get(key, 0.0) or 0.0)
        out[key] = round(total / len(records), 4)
    return out


def role_phrases(text: str, role: str, limit: int = 8) -> List[str]:
    phrases: List[str] = []
    for pattern in ROLE_PATTERNS[role]:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            phrase = re.sub(r"\s+", " ", match.group(0)).strip(" .,:;")
            if 3 <= len(phrase) <= 90:
                phrases.append(phrase)
    if not phrases:
        for sentence in SENTENCE_RE.split(text):
            if len(phrases) >= limit:
                break
            if score_patterns(sentence, ROLE_PATTERNS[role]) <= 0:
                continue
            words = sentence.split()
            if len(words) <= 10:
                clean = compact(sentence, 90)
                if 12 <= len(clean) <= 90 and "==" not in clean:
                    phrases.append(clean)
    out = []
    seen = set()
    for phrase in phrases:
        text_phrase = re.sub(r"\s+", " ", phrase).strip()
        if text_phrase.lower() in {"state", "operator", "measurement", "update"}:
            continue
        if len(text_phrase.split()) > 5:
            continue
        key = text_phrase.lower()
        if key not in seen:
            seen.add(key)
            out.append(text_phrase)
        if len(out) >= limit:
            break
    return out


def mechanism_grammar(topic: Mapping[str, Any], records: Sequence[Mapping[str, Any]]) -> Dict[str, List[str]]:
    text = " ".join(
        [topic.get("title", ""), topic.get("summary", ""), topic.get("extract", "")[:12000]]
    )
    fallbacks = {
        "state": ["quantum state", "wave function", "density operator"],
        "operator": ["Hamiltonian", "observable operator", "generator"],
        "spectrum": ["eigenvalue", "energy level", "measurement outcome"],
        "boundary": ["preparation condition", "measurement setup", "potential or domain"],
        "incompatibility": ["commutator", "uncertainty relation", "non-commuting transformations"],
        "protocol": ["unitary evolution", "projection or measurement update", "path integral weighting"],
    }
    grammar: Dict[str, List[str]] = {}
    for role in ROLE_PATTERNS:
        values = role_phrases(text, role, 8)
        if not values:
            values = fallbacks[role]
        grammar[role] = values[:8]
    return grammar


def normalize_role_term(value: str) -> str:
    lower = value.lower().strip()
    replacements = {
        "observable": "observable operator",
        "unitary": "unitary operator",
        "uncertainty": "uncertainty relation",
        "incompatible": "incompatible observables",
        "collapse": "projection update",
        "projection": "projection update",
        "potential": "potential or domain condition",
        "potential or domain": "potential or domain condition",
    }
    if "non-commuting" in lower or "noncommuting" in lower:
        return "non-commuting observables"
    return replacements.get(lower, value)


def grammar_terms(grammar: Mapping[str, Sequence[str]], role: str, fallback: Sequence[str], limit: int = 3) -> List[str]:
    candidates = [str(value).strip() for value in grammar.get(role, []) if str(value).strip()]
    candidates.extend(str(value).strip() for value in fallback if str(value).strip())
    out: List[str] = []
    seen = set()
    for candidate in candidates:
        value = normalize_role_term(candidate)
        if value.lower() in {"state", "operator", "measurement", "update"}:
            continue
        key = value.lower()
        if key not in seen:
            seen.add(key)
            out.append(value)
        if len(out) >= limit:
            break
    return out


def join_terms(values: Sequence[str]) -> str:
    if not values:
        return ""
    if len(values) == 1:
        return values[0]
    if len(values) == 2:
        return f"{values[0]} or {values[1]}"
    return ", ".join(values[:-1]) + f", or {values[-1]}"


def lower_first(value: str) -> str:
    value = str(value or "").strip()
    if not value:
        return value
    return value[0].lower() + value[1:]


INTERPRETATION_RE = re.compile(
    r"\b(qbism|quantum bayesian|relational quantum mechanics|copenhagen interpretation|many-worlds|many worlds|"
    r"consistent histories|quantum mind|quantum mysticism|interpretation of quantum mechanics)\b",
    re.IGNORECASE,
)


def is_interpretation_topic(title: str, text: str = "") -> bool:
    return bool(INTERPRETATION_RE.search(f"{title} {text}"))


def quantum_topic_phrase(title: str) -> str:
    clean = str(title or "the topic").strip()
    low = clean.lower()
    special = {
        "qbism": "QBism",
        "ads/cft correspondence": "the AdS/CFT correspondence",
    }
    if low in special:
        return special[low]
    if low.startswith(("a ", "an ", "the ")):
        return clean
    if low in {
        "quantum mechanics",
        "quantum physics",
        "quantum computation",
        "quantum computing",
        "quantum programming",
        "quantum chemistry",
        "quantum biology",
        "quantum optics",
        "quantum cosmology",
        "quantum chromodynamics",
        "quantum electrodynamics",
        "quantum technology",
        "quantum information science",
        "renormalization",
        "gauge theory",
        "string theory",
        "operator theory",
        "spectral theory",
        "perturbation theory",
        "wave-particle duality",
        "wave–particle duality",
    }:
        return low
    if low.endswith(
        (
            "equation",
            "operator",
            "principle",
            "rule",
            "theorem",
            "problem",
            "relation",
            "formulation",
            "algebra",
            "space",
            "matrix",
            "matrices",
            "picture",
            "model",
            "correspondence",
            "paradox",
        )
    ):
        return f"the {clean}"
    if low[0] in "aeiou":
        return f"an {lower_first(clean)}"
    return f"a {lower_first(clean)}"


def quantum_public_frame(title: str, text: str) -> Dict[str, str]:
    title_low = str(title or "").lower()
    low = f"{title} {text}".lower()
    if is_interpretation_topic(title, text):
        return {
            "state_space": "the usual state-assignment formalism rather than a new physical state space",
            "dynamics": "the existing operator and update rules of quantum mechanics, with their interpretation changed",
            "readout": "Born probabilities and measurement outcomes as the interpreted layer",
            "context": "the agent, measurement context, or interpretive stance attached to the formalism",
        }
    if any(word in low for word in ("two-state", "two state", "qubit", "pauli", "spin-1/2", "bloch sphere")):
        return {
            "state_space": "a two-dimensional Hilbert space, usually written as a qubit state or a density matrix",
            "dynamics": "a Hamiltonian or unitary matrix rotating that state between preparation and measurement",
            "readout": "projectors onto the two eigenstates of the measured observable",
            "context": "the chosen basis, pulse sequence, or measurement axis",
        }
    if any(word in low for word in ("schrödinger", "schrodinger", "hamiltonian", "unitary operator", "time evolution")):
        return {
            "state_space": "a wave function or density operator defined on the Hilbert space allowed by the system's domain",
            "dynamics": "the Hamiltonian, whose exponential gives unitary time evolution",
            "readout": "the eigenvalues and eigenfunctions of the relevant observable",
            "context": "the potential, domain, initial condition, or boundary condition",
        }
    if any(word in low for word in ("measurement", "born rule", "observable", "spectral", "eigenstate", "eigenvalue")):
        return {
            "state_space": "a prepared quantum state before the measurement",
            "dynamics": "the self-adjoint observable being asked of that state",
            "readout": "the observable's spectral projectors and the Born probabilities assigned to them",
            "context": "the measurement basis and experimental arrangement",
        }
    if any(word in low for word in ("path integral", "feynman", "action")):
        return {
            "state_space": "boundary states or field configurations at the endpoints of a process",
            "dynamics": "the action functional assigning phases to histories",
            "readout": "transition amplitudes and probabilities obtained by summing over histories",
            "context": "the boundary conditions that define which histories are included",
        }
    if any(word in title_low for word in ("field theory", "gauge", "relativistic", "string", "loop quantum gravity", "standard model")):
        return {
            "state_space": "a space of admissible field states constrained by symmetry and gauge conditions",
            "dynamics": "Hamiltonian, constraint, or field operators acting on those states",
            "readout": "spectra, correlation functions, scattering amplitudes, or other observable quantities",
            "context": "gauge choice, domain condition, asymptotic boundary, or regularity constraint",
        }
    if any(word in low for word in ("entanglement", "teleportation", "bell", "network", "channel")):
        return {
            "state_space": "a joint state on a tensor-product Hilbert space",
            "dynamics": "local unitaries, channels, and measurements acting on the subsystems",
            "readout": "correlations, reduced density matrices, and measurement probabilities",
            "context": "which subsystems are prepared, measured, traced out, or classically communicated",
        }
    if any(word in low for word in ("algorithm", "programming", "circuit", "computation", "automaton", "machine")):
        return {
            "state_space": "a register state in a finite-dimensional Hilbert space",
            "dynamics": "a sequence of unitary gates or quantum channels",
            "readout": "measurement probabilities over computational-basis outcomes",
            "context": "the input encoding, circuit architecture, and final measurement basis",
        }
    if any(word in low for word in ("uncertainty", "commutator", "heisenberg group", "noncommutative")):
        return {
            "state_space": "a quantum state on which two or more observables may be evaluated",
            "dynamics": "the non-commuting operators representing those observables",
            "readout": "spectral distributions that cannot generally be made sharp at the same time",
            "context": "the measurement basis chosen for one observable rather than another",
        }
    return {
        "state_space": "a prepared quantum state, represented by a vector, wave function, or density operator",
        "dynamics": "a Hamiltonian, unitary evolution, observable, or constraint operator",
        "readout": "a spectral decomposition whose projectors receive Born probabilities",
        "context": "the preparation, basis, potential, domain, or measurement arrangement",
    }


def quantum_frame_is_generic(frame: Mapping[str, str]) -> bool:
    return (
        frame.get("state_space") == "a prepared quantum state, represented by a vector, wave function, or density operator"
        and frame.get("dynamics") == "a Hamiltonian, unitary evolution, observable, or constraint operator"
        and frame.get("readout") == "a spectral decomposition whose projectors receive Born probabilities"
    )


def quantum_native_mechanism_text(title: str, text: str, grammar: Mapping[str, Sequence[str]]) -> str:
    frame = quantum_public_frame(title, text)
    phrase = quantum_topic_phrase(title)
    states = join_terms(grammar_terms(grammar, "state", ("wave function", "state vector", "density operator"), 2))
    operators = join_terms(grammar_terms(grammar, "operator", ("Hamiltonian", "observable", "unitary operator"), 2))
    spectra = join_terms(grammar_terms(grammar, "spectrum", ("eigenvalue", "eigenstate", "measurement outcome"), 2))
    incompat = join_terms(grammar_terms(grammar, "incompatibility", ("commutator", "non-commuting observables"), 2))
    if is_interpretation_topic(title, text):
        return (
            f"{phrase} acts on the readout layer of the quantum constructor. "
            f"The formal ingredients remain the state assignment, the operator or measurement being applied, and the Born-rule map from projectors to probabilities. "
            f"What changes is the status assigned to those ingredients: for this topic, the state or probability is treated through {frame['context']}. "
            "The page should therefore be read as a statement about the interpretation of state, probability, update, or recorded outcome while the Hamiltonian, spectral resolution, and commutator structure remain the formal reference layer."
        )
    if quantum_frame_is_generic(frame):
        roles = []
        if states:
            roles.append(f"state terms such as {states}")
        if operators:
            roles.append(f"operator terms such as {operators}")
        if spectra:
            roles.append(f"spectral terms such as {spectra}")
        role_sentence = "; ".join(roles) if roles else "broad quantum vocabulary"
        return (
            f"{phrase} is read through the compact quantum constructor. "
            f"The available language supplies {role_sentence}. "
            "The mechanism should be completed by naming the state carrier, the operator or generator that acts on it, the admissibility condition, the readout, and the comparison that would distinguish this role from a neighboring one."
        )
    detail = (
        f"In quantum-mechanical terms, {phrase} is described by {frame['state_space']}. "
        f"The physical question is represented by {frame['dynamics']}; the experimental or mathematical setting is "
        f"{frame['context']}. The observable content is obtained from {frame['readout']}. "
    )
    if states or operators or spectra:
        detail += (
            f"In the local terminology of this topic, the same construction appears through {states or 'state vectors'}, "
            f"{operators or 'operators'}, and {spectra or 'spectral outcomes'}. "
        )
    detail += (
        "Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, "
        "not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; "
        "the limitation is therefore a statement about jointly available spectra, not about detector imperfection."
    )
    if incompat:
        detail += f" In this page the compatibility condition is expressed through {incompat}."
    return detail


def quantum_native_takeaway(title: str, text: str) -> str:
    frame = quantum_public_frame(title, text)
    phrase = quantum_topic_phrase(title)
    if is_interpretation_topic(title, text):
        return (
            f"{phrase} modifies the interpretation of the probability/readout layer while preserving the formal quantum dynamics."
        )
    if quantum_frame_is_generic(frame):
        return (
            f"{phrase.capitalize()} is placed by route/fiber evidence in the public MorphWiki export. A complete mechanism names its state carrier, operator or map, admissibility condition, readout, and falsifier."
        )
    return (
        f"{phrase.capitalize()} can be read as a quantum construction: {frame['context']} fixes the admissible state space; "
        f"{frame['dynamics']} defines the transformation or question; and spectral projectors with the Born rule determine "
        "the recorded probability distribution."
    )


def quantum_mechanism_profile(
    topic: Mapping[str, Any],
    grammar: Mapping[str, Sequence[str]],
    active_routes: str,
    active_fibers: str,
) -> Optional[Dict[str, Any]]:
    title = str(topic.get("title") or "the topic")
    text = " ".join([title, str(topic.get("summary") or ""), str(topic.get("extract") or "")[:16000]])
    if not re.search(
        r"\bquantum\b|Schr[oö]dinger|Hamiltonian|Hilbert|Born rule|wave function|density matrix|commutator|"
        r"uncertainty|entanglement|qubit|observable|eigenstate|path integral|gauge theory|field theory",
        text,
        re.IGNORECASE,
    ):
        return None

    states = grammar_terms(grammar, "state", ("wave function", "quantum state", "density operator"))
    operators = grammar_terms(grammar, "operator", ("Hamiltonian", "observable", "unitary operator"))
    spectra = grammar_terms(grammar, "spectrum", ("eigenvalue", "eigenstate", "measurement outcome"))
    boundaries = grammar_terms(grammar, "boundary", ("preparation context", "measurement basis", "potential"))
    incompat = grammar_terms(grammar, "incompatibility", ("commutator", "uncertainty relation", "incompatible observable"))
    protocols = grammar_terms(grammar, "protocol", ("Born rule", "unitary evolution", "projection update"))

    mechanism_view = quantum_native_mechanism_text(title, text, grammar)
    takeaway = quantum_native_takeaway(title, text)
    generic_frame = quantum_frame_is_generic(quantum_public_frame(title, text))
    if generic_frame:
        what_this_adds = [
            "The page records a measured route/fiber placement and states which constructor roles are active.",
            "Constructor completion requires a specific state carrier, operator or generator, admissibility condition, readout, and falsifier.",
            "The page separates generic quantum vocabulary from a completed mechanism.",
        ]
        conversion_form = [
            "Carrier: name the topic-native state space or state variable.",
            "Map: name the operator, generator, constraint, or transformation acting on that carrier.",
            "Admissibility: name the boundary, gauge, preparation, symmetry, or conservation rule.",
            "Readout: name the spectrum, probability distribution, correlation, scattering amplitude, or detector event.",
            "Falsifier: name the condition that would break the proposed role assignment.",
        ]
        skeleton = ""
    else:
        what_this_adds = [
            "The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.",
            "It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.",
            "It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.",
            "It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.",
        ]

        conversion_form = [
            f"Preparation or domain terms ({join_terms(boundaries)}) determine which states are admissible.",
            f"State terms ({join_terms(states)}) name the predictive carrier: vector, wave function, density operator, field state, or register state.",
            f"Operator terms ({join_terms(operators)}) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.",
            f"Spectral terms ({join_terms(spectra)}) name the outcome labels and projectors that define readout channels.",
            "The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.",
            f"Compatibility terms ({join_terms(incompat)}) mark cases where observables do not admit one common sharp readout basis.",
        ]

        skeleton = "\n".join(
            [
                r"B \longmapsto \rho_B \quad \text{(context specifies an admissible state)}",
                r"\rho_t = U_t \rho_B U_t^\dagger \quad \text{(unitary evolution from preparation to readout)}",
                r"O = \sum_i \lambda_i P_i,\quad p_i=\operatorname{Tr}(P_i\rho_t) \quad \text{(spectral probability measure)}",
                r"[O_1,O_2]\neq 0 \quad \text{(incompatible observables: no common sharp basis)}",
            ]
        )

    what_survives = [
        "the rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation",
        "the operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels",
        "the dependence of admissible readout on measurement context or boundary condition",
        "the non-commuting compatibility structure, which survives changes of representation",
    ]
    what_changes = [
        "the name of the carrier: particle, wave, field, qubit, or excitation",
        "where time dependence is represented: on the state, on the operator, or in a path weight",
        "the coordinate system, basis, or geometric picture used to display the same relation",
        "the physical implementation of detector, boundary, preparation, or readout",
    ]
    missing_experiments = [
        (
            "A concrete transfer target is a material, biological, or collective system with a state, a transformation, "
            "and a spectral or categorical readout, but without a tested incompatibility relation."
        ),
        (
            "The validation criterion is that varying the context changes the admissible readout while the "
            "transformation law remains identifiable; shuffled or erased contexts should weaken the effect."
        ),
    ]
    return {
        "takeaway": takeaway,
        "mechanism_view": mechanism_view,
        "what_this_adds": what_this_adds,
        "conversion_form": conversion_form,
        "mathematical_skeleton": skeleton,
        "what_survives": what_survives,
        "what_changes": what_changes,
        "missing_experiments": missing_experiments,
        "public_evidence_summary": (
            f"Hyperion evidence ranks this page near {active_routes}, with strongest public fingerprints in {active_fibers}."
        ),
    }


def evidence_rows(records: Sequence[Mapping[str, Any]], limit: int = 24) -> List[Dict[str, Any]]:
    rows = []
    for record in records[:limit]:
        hyperion = record.get("hyperion") or {}
        fp_fibers = fingerprint_fiber_values(record)
        rows.append(
            {
                "record_id": record.get("record_id"),
                "title": record.get("title"),
                "score": record.get("_morphwiki_score"),
                "route_score": record.get("_route_score"),
                "lexical_score": record.get("_lexical_score"),
                "equation": (record.get("equations") or [""])[0],
                "equation_excerpt": readable_equation_excerpt(record),
                "witness_quality": round(1.0 - bad_witness_score(witness_text(record)), 4),
                "invariant": record.get("invariant"),
                "apparatus_regime": hyperion.get("apparatus_regime"),
                "omega_tokens": hyperion.get("omega_tokens"),
                "paper_id": hyperion.get("paper_id"),
                "arxiv_url": hyperion.get("arxiv_url"),
                "routes": record.get("routes") or {},
                "fibers": fp_fibers if fp_fibers is not None else (record.get("fibers") or {}),
            }
        )
    return rows


def deterministic_morphwiki(topic: Mapping[str, Any], grammar: Mapping[str, Sequence[str]], records: Sequence[Mapping[str, Any]], routes: Mapping[str, float], fibers: Mapping[str, float]) -> Dict[str, Any]:
    active_route_keys = top_keys(routes, 4)
    active_fiber_keys = top_keys(fibers, 3)
    active_routes = readable_key_list(active_route_keys, route_label)
    active_fibers = readable_key_list(active_fiber_keys, fiber_label)
    operator_atoms = []
    apparatus = []
    for record in records[:18]:
        hyperion = record.get("hyperion") or {}
        if hyperion.get("apparatus_regime"):
            apparatus.append(str(hyperion["apparatus_regime"]))
        for token in normalize_omega_tokens(hyperion.get("omega_tokens")):
            operator_atoms.append(str(token))
    apparatus_counts = Counter(apparatus)
    omega_counts = Counter(operator_atoms)
    title = topic.get("title") or "Topic"
    state_terms = ", ".join((grammar.get("state") or ["state"])[:3])
    operator_terms = ", ".join((grammar.get("operator") or ["operator"])[:3])
    boundary_terms = ", ".join((grammar.get("boundary") or ["boundary"])[:3])
    spectrum_terms = ", ".join((grammar.get("spectrum") or ["spectrum"])[:3])
    page = {
        "takeaway": (
            f"{title} can be represented as an operational construction: a context specifies a state, "
            f"an operator transforms it, and admissible outcomes are read through a spectrum."
        ),
        "object_view": first_public_sentences(topic.get("summary") or topic.get("extract"), 2),
        "mechanism_view": (
            f"Operationally, {title} is organized by the relation between state terms ({state_terms}), "
            f"operator terms ({operator_terms}), context or boundary terms ({boundary_terms}), and spectral "
            f"readout terms ({spectrum_terms}). The local vocabulary can change across formulations, but "
            f"the same state-to-transformation-to-readout structure can remain identifiable. "
            f"Across equation-level evidence the dominant pattern is {active_routes}, "
            f"carried by {active_fibers}."
        ),
        "what_this_adds": [
            "The standard topic view organizes concepts by names; MorphWiki organizes them by the operations needed to construct a theory.",
            "It identifies which roles survive a change of notation: state, transformation, context, readout, and compatibility.",
            "It separates local field vocabulary from portable mechanism structure.",
        ],
        "what_survives": [
            "the conversion law: a state is transformed and a readout is resolved",
            "context dependence: admissible readouts depend on preparation or boundary conditions",
            "compatibility constraints: some transformations cannot be jointly resolved regardless of notation",
        ],
        "what_changes": [
            "the local terms used for mechanism roles, such as particle, wave, detector, field, or qubit",
            "the coordinate system or representation used to write the same relation",
            "the physical hardware that plays the role of boundary or readout",
        ],
        "active_apparatus": [name for name, _ in apparatus_counts.most_common(8)],
        "active_operator_atoms": [name for name, _ in omega_counts.most_common(12)],
        "missing_experiments": [
            (
                f"Candidate transfer targets are systems where the same state-to-operator-to-spectrum conversion appears, "
                f"but one edge of the construction remains experimentally unresolved."
            ),
            (
                "A valid transfer test varies the context and shows that the readout changes while the "
                "transformation law remains identifiable."
            ),
        ],
        "public_evidence_summary": (
            f"Dominant evidence pattern: {active_routes}, carried by {active_fibers}."
        ),
        "claim_boundary": (
            f"Synthesis from Wikipedia scaffold + {len(records)} Hyperion equation witnesses. "
            "Not a claim of physical reduction."
        ),
    }
    quantum_profile = quantum_mechanism_profile(topic, grammar, active_routes, active_fibers)
    if quantum_profile:
        page.update(quantum_profile)
    return page


def call_llm(command: str, payload: Mapping[str, Any], timeout: int = 180) -> Optional[Dict[str, Any]]:
    if not command:
        return None
    try:
        result = subprocess.run(
            command,
            input=json.dumps(payload, ensure_ascii=False),
            capture_output=True,
            text=True,
            shell=True,
            timeout=timeout,
            check=False,
        )
    except Exception:
        return None
    if result.returncode != 0 or not result.stdout.strip():
        return None
    return extract_json_object(result.stdout)


def extract_json_object(text: str) -> Optional[Dict[str, Any]]:
    clean = text.strip()
    if clean.startswith("```"):
        clean = re.sub(r"^```(?:json)?\s*", "", clean)
        clean = re.sub(r"\s*```$", "", clean).strip()
    try:
        obj = json.loads(clean)
        return obj if isinstance(obj, dict) else None
    except json.JSONDecodeError:
        pass
    start = clean.find("{")
    end = clean.rfind("}")
    if start >= 0 and end > start:
        try:
            obj = json.loads(clean[start : end + 1])
            return obj if isinstance(obj, dict) else None
        except json.JSONDecodeError:
            return None
    return None


def call_openrouter(payload: Mapping[str, Any], args: argparse.Namespace) -> Optional[Dict[str, Any]]:
    if not args.openrouter_model:
        return None
    api_key = os.environ.get(args.openrouter_api_key_env)
    if not api_key:
        return None

    system = (
        "You are MorphWiki's science writer. Your job: take a Wikipedia topic and Hyperion evidence "
        "and write a rigorous mechanism page for scientifically literate readers. "
        "Lead with the operational construction, not the textbook definition. "
        "Make the result clear and memorable without clickbait, metaphor inflation, or overclaim. "
        "Use the supplied Hyperion translation guide to understand the private evidence language, "
        "then translate it into precise ordinary-language scientific prose. "
        "Do not add facts, examples, claims, papers, or equations not present in the input. "
        "Do not mention apparatus IDs, Greek labels, operator atom IDs, raw route IDs, or raw fiber IDs in public prose; those stay in JSON evidence. "
        "Return valid JSON only."
    )
    user = json.dumps(payload, ensure_ascii=False)
    request_payload = {
        "model": args.openrouter_model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": args.openrouter_temperature,
        "max_tokens": args.openrouter_max_tokens,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if args.openrouter_site_url:
        headers["HTTP-Referer"] = args.openrouter_site_url
    if args.openrouter_app_name:
        headers["X-Title"] = args.openrouter_app_name
    request = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(request_payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=args.llm_timeout) as response:
            result = json.loads(response.read().decode("utf-8"))
    except Exception:
        return None

    choices = result.get("choices") or []
    if not choices:
        return None
    message = choices[0].get("message") or {}
    content = message.get("content")
    if isinstance(content, list):
        content = "\n".join(str(part.get("text") if isinstance(part, Mapping) else part) for part in content)
    if not isinstance(content, str):
        return None
    return extract_json_object(content)


def llm_payload(topic: Mapping[str, Any], grammar: Mapping[str, Sequence[str]], records: Sequence[Mapping[str, Any]], deterministic: Mapping[str, Any], args: argparse.Namespace) -> Dict[str, Any]:
    return {
        "task": (
            "Rewrite this topic as a rigorous MorphWiki mechanism page. "
            "Lead with an evidence-bound one-sentence operational thesis. "
            "Use only the supplied Wikipedia scaffold, grammar, and Hyperion evidence. "
            "Do not invent examples, experiments, apparatus IDs, or claims. "
            "Return JSON with keys: takeaway, object_view, mechanism_view, what_this_adds, conversion_form, "
            "mathematical_skeleton, what_survives, what_changes, missing_experiments, readable_summary."
        ),
        "hyperion_translation_guide": HYPERION_PUBLIC_TRANSLATION_GUIDE,
        "hyperion_language_skill_excerpt": getattr(args, "hyperion_language_skill_excerpt", ""),
        "hyperion_language_examples_excerpt": getattr(args, "hyperion_language_examples_excerpt", ""),
        "rules": [
            "Write clear scientific prose, not an audit report and not promotional copy.",
            "Lead with the operational construction, not with the Wikipedia definition.",
            "The opening should be memorable because it is precise, not because it exaggerates novelty.",
            "Translate private Hyperion evidence into precise ordinary-language science writing.",
            "No raw labels (Α07, Ω12, spectral_operator_route, etc.) in public prose — those stay in JSON.",
            "Do not write route ids, fiber ids, apparatus ids, operator atom ids, or invariant-checkpoint ids in public prose.",
            "Use evidence-bound language: the witness set supports, ranks, is consistent with, or emphasizes. It does not prove or confirm a physical reduction.",
            "what_survives should name representation-stable mechanism roles, not philosophical absolutes.",
            "what_changes should name representation-dependent terms, not dismissive metaphors.",
            "missing_experiments should state concrete transfer tests.",
            "No mystical observer language. No 'it is interesting to note that...' filler.",
            "Do not quote long Wikipedia passages; one sharp sentence of context is enough.",
        ],
        "wikipedia": {
            "title": topic.get("title"),
            "url": topic.get("url"),
            "description": topic.get("description"),
            "summary": public_text(topic.get("summary")),
        },
        "grammar": grammar,
        "deterministic_page": deterministic,
        "evidence": evidence_rows(records, 12),
    }


def merge_llm_page(deterministic: Dict[str, Any], llm_page: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    if not llm_page:
        return deterministic
    merged = dict(deterministic)
    rejected_fields: List[str] = []
    for key in ("takeaway", "object_view", "mechanism_view", "readable_summary", "mathematical_skeleton"):
        value = llm_page.get(key)
        if isinstance(value, str) and public_field_is_safe(value, allow_math=(key == "mathematical_skeleton")):
            merged[key] = public_text(value) if key != "mathematical_skeleton" else value.strip()
        elif isinstance(value, str) and value.strip():
            rejected_fields.append(key)
    for key in ("what_this_adds", "conversion_form", "what_survives", "what_changes", "missing_experiments"):
        values = llm_page.get(key)
        if isinstance(values, list) and all(isinstance(value, str) for value in values):
            clean_values = [public_text(value) for value in values if public_field_is_safe(value)]
            if clean_values:
                merged[key] = clean_values[:8]
            else:
                rejected_fields.append(key)
    merged["llm_used"] = True
    if rejected_fields:
        merged["llm_rejected_fields"] = rejected_fields
    return merged


def render_markdown(page: Mapping[str, Any]) -> str:
    title = page["wikipedia"]["title"]
    morph = page["morphwiki"]
    routes = page["hyperion"]["route_profile"]
    fibers = page["hyperion"]["fiber_profile"]
    route_line = ", ".join(f"{route_label(key)}: {value:.2f}" for key, value in sorted(routes.items(), key=lambda item: item[1], reverse=True)[:6])
    fiber_line = ", ".join(f"{fiber_label(key)}: {value:.2f}" for key, value in sorted(fibers.items(), key=lambda item: item[1], reverse=True)[:5])
    grammar = page["morphwiki"]["grammar"]
    evidence = page["hyperion"]["equation_witnesses"][:10]
    lines = [
        f"# {title}",
        "",
    ]
    if morph.get("takeaway"):
        claim_heading = (
            "Central Claim"
            if morph.get("mathematical_skeleton_is_source_backed") or morph.get("mathematical_skeleton_is_topic_native")
            else "Evidence Status"
        )
        lines.extend([f"## {claim_heading}", morph.get("takeaway", ""), ""])
    lines.extend([
        "## The Standard Story",
        morph.get("object_view", ""),
        "",
        "## Mechanism Reading",
        morph.get("mechanism_view", ""),
        "",
    ])
    if morph.get("what_this_adds"):
        lines.extend(["## Operational Contribution"])
        lines.extend(f"- {item}" for item in morph.get("what_this_adds", []))
        lines.append("")
    if morph.get("conversion_form"):
        lines.extend(["## Mechanism Form"])
        lines.extend(f"- {item}" for item in morph.get("conversion_form", []))
        lines.append("")
    if morph.get("mathematical_skeleton") and morph.get("mathematical_skeleton_is_source_backed"):
        lines.extend(["## Formal Skeleton", "```math", str(morph.get("mathematical_skeleton", "")).strip(), "```", ""])
    elif morph.get("mathematical_skeleton") and morph.get("mathematical_skeleton_is_topic_native"):
        lines.extend([
            "## Topic-Native Formal Skeleton",
            "This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw Hyperion parser excerpt.",
            "```math",
            str(morph.get("mathematical_skeleton", "")).strip(),
            "```",
            "",
        ])
    lines.append("## Mechanism Roles")
    for role, values in grammar.items():
        rendered_values: List[str] = []
        seen_values = set()
        for value in values:
            clean_value = normalize_role_term(str(value))
            key = clean_value.lower()
            if key not in seen_values:
                seen_values.add(key)
                rendered_values.append(clean_value)
            if len(rendered_values) >= 4:
                break
        lines.append(f"- **{role}:** " + "; ".join(rendered_values))
    lines.extend(
        [
            "",
            "## Evidence Profile",
            f"- Routes: {route_line}",
            f"- Fibers: {fiber_line}",
            "",
            "## Representation-Stable Content",
        ]
    )
    lines.extend(f"- {item}" for item in morph.get("what_survives", []))
    lines.extend(["", "## Representation-Dependent Content"])
    lines.extend(f"- {item}" for item in morph.get("what_changes", []))
    lines.extend(["", "## Validation Boundary"])
    lines.extend(f"- {item}" for item in morph.get("missing_experiments", []))
    lines.extend(["", "## Evidence Links"])
    for row in evidence:
        link = f"[{row['paper_id']}]({row['arxiv_url']})" if row.get("arxiv_url") and row.get("paper_id") else ""
        score = row.get('score')
        score_str = f"{score:.3f}" if isinstance(score, float) else str(score)
        lines.append(f"- {link} — score {score_str}" if link else f"- score {score_str}")
    wiki_url = page['wikipedia'].get('url') or ''
    lines.extend(
        [
            "",
            "---",
            f"Wikipedia scaffold: [{page['wikipedia']['title']}]({wiki_url}) (CC BY-SA). {morph.get('claim_boundary', '')}",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def build_page(topic: Mapping[str, Any], records: Sequence[Mapping[str, Any]], args: argparse.Namespace) -> Dict[str, Any]:
    ranked, topic_routes, topic_fibers = rank_records(topic, records, args.max_witnesses)
    selected = ranked[: args.page_witnesses]
    route_profile = average_profile(selected, "routes", ROUTE_KEYS)
    fiber_profile = average_profile(selected, "fibers", FIBER_KEYS)
    if not selected:
        route_profile = topic_routes
        fiber_profile = topic_fibers
    grammar = mechanism_grammar(topic, selected)
    deterministic = deterministic_morphwiki(topic, grammar, selected, route_profile, fiber_profile)
    synthesis_payload = llm_payload(topic, grammar, selected, deterministic, args)
    llm_page = call_llm(args.llm_command, synthesis_payload, args.llm_timeout)
    if llm_page is None:
        llm_page = call_openrouter(synthesis_payload, args)
    morphwiki = merge_llm_page(deterministic, llm_page)
    morphwiki["grammar"] = grammar
    morphwiki["llm_used"] = bool(llm_page)
    return {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "wikipedia": {
            "title": topic.get("title"),
            "pageid": topic.get("pageid"),
            "url": topic.get("url"),
            "description": topic.get("description"),
            "summary": compact(topic.get("summary"), 900),
            "lang": topic.get("lang"),
            "license_note": topic.get("license_note"),
        },
        "hyperion": {
            "source_index": str(args.hyperion_index),
            "route_profile": route_profile,
            "fiber_profile": fiber_profile,
            "topic_route_profile_from_wikipedia": topic_routes,
            "topic_fiber_profile_from_wikipedia": topic_fibers,
            "equation_witnesses": evidence_rows(selected, args.page_witnesses),
            "candidate_pool_size": len(records),
        },
        "morphwiki": morphwiki,
    }


def load_records(path: Path) -> List[Mapping[str, Any]]:
    payload = read_json(path)
    records = payload.get("records") if isinstance(payload, Mapping) else None
    if not isinstance(records, list):
        raise ValueError(f"{path} does not contain a records[] Hyperion index")
    return [record for record in records if isinstance(record, Mapping)]


def split_csv(value: str) -> List[str]:
    return [item.strip() for item in str(value or "").split(",") if item.strip()]


def related_filters_for(args: argparse.Namespace) -> List[str]:
    filters: List[str] = []
    for preset in split_csv(args.topic_preset):
        filters.extend(RELATED_FILTER_PRESETS.get(preset, ()))
    filters.extend(split_csv(args.related_filter))
    if args.expand_wikipedia_links and not filters:
        filters.extend(RELATED_FILTER_PRESETS["quantum"])
    seen = set()
    out = []
    for value in filters:
        key = value.lower()
        if key not in seen:
            seen.add(key)
            out.append(value)
    return out


def parse_topics(args: argparse.Namespace, cache_dir: Path) -> List[str]:
    topics: List[str] = []
    for preset in split_csv(args.topic_preset):
        if preset not in TOPIC_PRESETS:
            raise SystemExit(f"Unknown topic preset '{preset}'. Available presets: {', '.join(sorted(TOPIC_PRESETS))}")
        topics.extend(TOPIC_PRESETS[preset])
    if args.topics:
        topics.extend(split_csv(args.topics))
    if args.topic_file:
        topics.extend(line.strip() for line in Path(args.topic_file).read_text(encoding="utf-8").splitlines() if line.strip() and not line.strip().startswith("#"))

    if args.expand_wikipedia_links:
        filters = related_filters_for(args)
        seed_topics = list(topics)
        expanded: List[str] = []
        for seed in seed_topics[: args.max_expansion_seed_topics]:
            try:
                links = fetch_cached_wikipedia_links(
                    seed,
                    cache_dir,
                    args.lang,
                    args.user_agent,
                    max_links=args.max_links_per_topic,
                    use_cache=not args.no_cache,
                    timeout=args.wikipedia_timeout,
                    retries=args.wikipedia_retries,
                )
            except Exception as exc:
                print(f"[MorphWiki] warning: could not expand links from {seed}: {exc}")
                continue
            for link in links:
                if title_matches_filters(link, filters):
                    expanded.append(link)
                    if len(expanded) >= args.max_expanded_topics:
                        break
            if len(expanded) >= args.max_expanded_topics:
                break
        topics.extend(expanded)

    seen = set()
    out = []
    for topic in topics:
        key = topic.lower()
        if key not in seen:
            seen.add(key)
            out.append(topic)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topics", default="", help="Comma-separated Wikipedia topics.")
    parser.add_argument("--topic-file", default="", help="Optional newline-separated topic list.")
    parser.add_argument("--topic-preset", default="", help="Comma-separated presets. Currently available: quantum.")
    parser.add_argument("--expand-wikipedia-links", action="store_true", help="Expand seeds through real Wikipedia outgoing links, filtered by related terms.")
    parser.add_argument("--max-expanded-topics", type=int, default=160)
    parser.add_argument("--max-expansion-seed-topics", type=int, default=24)
    parser.add_argument("--max-links-per-topic", type=int, default=500)
    parser.add_argument("--wikipedia-timeout", type=int, default=90)
    parser.add_argument("--wikipedia-retries", type=int, default=5)
    parser.add_argument("--related-filter", default="", help="Comma-separated title substrings used when --expand-wikipedia-links is enabled.")
    parser.add_argument("--print-topics", action="store_true", help="Print resolved topics and exit without building pages.")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--hyperion-index", default="discoveries/fieldbridge_static_index/hyperion_static_index.json")
    parser.add_argument("--out-dir", default="discoveries/morphwiki_topic_index")
    parser.add_argument("--cache-dir", default="", help="Wikipedia cache directory. Defaults to OUT/wiki_cache.")
    parser.add_argument("--env-file", default=".env", help="Optional env file for OPENROUTER_API_KEY, HYPERION_MODEL, or MORPHWIKI_MODEL.")
    parser.add_argument("--user-agent", default=os.environ.get("WIKIPEDIA_USER_AGENT", "HyperionMorphWiki/0.1 (research export; contact: synthetix.institute)"))
    parser.add_argument("--max-witnesses", type=int, default=300)
    parser.add_argument("--page-witnesses", type=int, default=32)
    parser.add_argument("--llm-command", default="", help="Optional command that reads JSON prompt on stdin and returns JSON page fields.")
    parser.add_argument("--llm-timeout", type=int, default=180)
    parser.add_argument("--openrouter-model", default="", help="Optional OpenRouter model id, e.g. openai/gpt-4.1 or anthropic/claude-sonnet-4.5.")
    parser.add_argument("--openrouter-api-key-env", default="OPENROUTER_API_KEY")
    parser.add_argument("--openrouter-temperature", type=float, default=0.2)
    parser.add_argument("--openrouter-max-tokens", type=int, default=1800)
    parser.add_argument("--openrouter-site-url", default="https://synthetix.institute")
    parser.add_argument("--openrouter-app-name", default="MorphWiki")
    parser.add_argument("--hyperion-language-skill", default="skills/hyperion-language/SKILL.md")
    parser.add_argument("--hyperion-language-examples", default="skills/hyperion-language/EXPLANATORY_TEXTS.md")
    parser.add_argument("--hyperion-language-max-chars", type=int, default=9000)
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args()
    load_env_file(Path(args.env_file))
    if not args.openrouter_model:
        args.openrouter_model = os.environ.get("MORPHWIKI_MODEL") or os.environ.get("HYPERION_MODEL", "")
    args.hyperion_language_skill_excerpt = load_text_excerpt(
        Path(args.hyperion_language_skill), args.hyperion_language_max_chars
    )
    args.hyperion_language_examples_excerpt = load_text_excerpt(
        Path(args.hyperion_language_examples), args.hyperion_language_max_chars
    )

    out_dir = Path(args.out_dir)
    cache_dir = Path(args.cache_dir) if args.cache_dir else out_dir / "wiki_cache"
    topics = parse_topics(args, cache_dir)
    if not topics:
        raise SystemExit("No topics supplied. Use --topics, --topic-file, or --topic-preset quantum.")
    if args.print_topics:
        print(json.dumps({"topic_count": len(topics), "topics": topics}, indent=2, ensure_ascii=False))
        return

    records = load_records(Path(args.hyperion_index))
    pages = []
    page_by_slug: Dict[str, int] = {}
    skipped_topics = []

    def write_manifest(path: Path, status: str) -> None:
        manifest = {
            "schema_version": 1,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "source": "Hyperion MorphWiki topic export",
            "status": status,
            "claim_boundary": (
                "Wikipedia is used as a public topic scaffold. Mechanism claims are ranked from Hyperion "
                "route/fiber witnesses. Optional LLM synthesis is evidence-constrained and non-authoritative."
            ),
            "hyperion_index": str(args.hyperion_index),
            "requested_topics": topics,
            "pages": pages,
            "skipped_topics": skipped_topics,
        }
        write_json(path, manifest)

    for topic_title in topics:
        try:
            topic = fetch_wikipedia_topic(
                topic_title,
                cache_dir,
                args.lang,
                args.user_agent,
                use_cache=not args.no_cache,
                timeout=args.wikipedia_timeout,
                retries=args.wikipedia_retries,
            )
            page = build_page(topic, records, args)
        except Exception as exc:
            skipped_topics.append({"topic": topic_title, "reason": compact(f"{type(exc).__name__}: {exc}", 360)})
            print(f"[MorphWiki] skipped {topic_title}: {exc}")
            write_manifest(out_dir / "manifest_partial.json", "partial")
            continue
        slug = slugify(str(page["wikipedia"]["title"] or topic_title))
        page_entry = {
            "topic": page["wikipedia"]["title"],
            "slug": slug,
            "json": f"pages/{slug}.json",
            "markdown": f"pages/{slug}.md",
            "wikipedia_url": page["wikipedia"].get("url"),
            "top_routes": top_keys(page["hyperion"]["route_profile"], 4),
            "top_fibers": top_keys(page["hyperion"]["fiber_profile"], 3),
            "witnesses": len(page["hyperion"]["equation_witnesses"]),
            "llm_used": page["morphwiki"].get("llm_used", False),
        }
        existing_index = page_by_slug.get(slug)
        if existing_index is not None:
            existing_entry = pages[existing_index]
            if page_entry["llm_used"] and not existing_entry.get("llm_used", False):
                write_json(out_dir / "pages" / f"{slug}.json", page)
                write_text(out_dir / "pages" / f"{slug}.md", render_markdown(page))
                pages[existing_index] = page_entry
                skipped_topics.append(
                    {
                        "topic": topic_title,
                        "reason": f"duplicate_slug_replaced_deterministic:{slug}",
                        "kept_topic": page_entry["topic"],
                    }
                )
            else:
                skipped_topics.append(
                    {
                        "topic": topic_title,
                        "reason": f"duplicate_slug:{slug}",
                        "kept_topic": existing_entry.get("topic"),
                    }
                )
            write_manifest(out_dir / "manifest_partial.json", "partial")
            continue
        write_json(out_dir / "pages" / f"{slug}.json", page)
        write_text(out_dir / "pages" / f"{slug}.md", render_markdown(page))
        page_by_slug[slug] = len(pages)
        pages.append(page_entry)
        write_manifest(out_dir / "manifest_partial.json", "partial")

    write_manifest(out_dir / "manifest.json", "complete")
    print(json.dumps({"out_dir": str(out_dir), "pages": len(pages), "manifest": str(out_dir / "manifest.json")}, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
