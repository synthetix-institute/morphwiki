#!/usr/bin/env python3
"""Rewrite existing MorphWiki quantum pages into quantum-native public prose.

This is an offline repair pass. It does not fetch Wikipedia and does not rerank
Hyperion evidence. It only replaces public-facing mechanism prose that leaked
Hyperion route/fiber language into the body text.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence

from export_morphwiki_topic_index import (
    fiber_label,
    grammar_terms,
    join_terms,
    quantum_native_mechanism_text,
    quantum_native_takeaway,
    render_markdown,
    route_label,
)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def update_conversion_form(grammar: Mapping[str, Sequence[str]]) -> list[str]:
    states = join_terms(grammar_terms(grammar, "state", ("wave function", "state vector", "density operator"), 3))
    operators = join_terms(grammar_terms(grammar, "operator", ("Hamiltonian", "observable", "unitary operator"), 3))
    spectra = join_terms(grammar_terms(grammar, "spectrum", ("eigenvalue", "eigenstate", "measurement outcome"), 3))
    boundaries = join_terms(grammar_terms(grammar, "boundary", ("preparation condition", "basis", "domain"), 3))
    incompat = join_terms(grammar_terms(grammar, "incompatibility", ("commutator", "non-commuting observables"), 3))
    protocols = join_terms(grammar_terms(grammar, "protocol", ("Born rule", "trace rule", "projection update"), 3))
    return [
        f"Preparation, basis, or domain terms ({boundaries}) determine which states are admissible.",
        f"State terms ({states}) name the predictive carrier: vector, wave function, density operator, field state, or register state.",
        f"Physical-question terms ({operators}) name the observable, Hamiltonian, unitary, or constraint being applied.",
        f"Spectral terms ({spectra}) name possible outcomes and the projectors or effects that define readout channels.",
        "Probability terms map states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.",
        f"Compatibility terms ({incompat}) mark cases where observables do not admit one common sharp readout basis.",
    ]


def update_public_lists() -> Dict[str, list[str]]:
    return {
        "what_this_adds": [
            "The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.",
            "It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.",
            "It treats non-commutativity as a constraint on which observables can share a spectral resolution.",
            "It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.",
        ],
        "what_survives": [
            "the relation between prepared states, observables, and spectral probability measures",
            "the use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations",
            "the dependence of the readout on basis, domain, potential, preparation, or measurement context",
            "the commutator structure that limits which observables can be jointly diagonalized",
        ],
        "what_changes": [
            "the physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation",
            "the representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields",
            "where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight",
            "the implementation of preparation, boundary condition, detector, or readout channel",
        ],
        "missing_experiments": [
            "A transfer target provides a state space, a transformation law, and a spectral or categorical readout, with one compatibility relation experimentally unresolved.",
            "A useful validation varies the basis, domain, or measurement context and measures whether the allowed readout changes while the underlying transformation law remains identifiable.",
            "A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.",
        ],
    }


def conservative_public_lists() -> Dict[str, list[str]]:
    return {
        "what_this_adds": [
            "This page reports route/fiber placement from the public Hyperion evidence instead of inventing a topic-native mechanism.",
            "It marks what still has to be constructed: a state carrier, an operator or generator, an admissibility condition, a readout, and a falsifier.",
            "It prevents broad quantum vocabulary from being mistaken for a page-level derivation.",
        ],
        "what_survives": [
            "only the measured route/fiber placement in this public export",
            "the Wikipedia topic scaffold and the linked Hyperion witness records",
            "the requirement that any future constructor must specify state, operator, admissibility, readout, and falsifier",
        ],
        "what_changes": [
            "the page does not yet decide the native variables or equations",
            "the page does not yet distinguish representation-specific vocabulary from a validated constructor",
            "the page becomes a constructed mechanism only when source-backed or topic-native equations are attached",
        ],
        "missing_experiments": [
            "The missing formal skeleton is a topic-native state carrier, operator or map, admissibility condition, readout, and falsifier.",
            "The proposed constructor must explain the witness links better than a shuffled topic assignment.",
            "Those elements make the page directly usable as a quantum mechanism.",
        ],
    }


def ranked_profile_terms(profile: Mapping[str, Any], labeler, limit: int = 4, threshold: float = 0.04) -> str:
    rows = []
    for key, value in (profile or {}).items():
        try:
            score = float(value or 0.0)
        except (TypeError, ValueError):
            continue
        if score >= threshold:
            rows.append((key, score))
    rows.sort(key=lambda item: item[1], reverse=True)
    if not rows:
        return "no dominant measured role"
    return ", ".join(f"{labeler(key)} ({score:.2f})" for key, score in rows[:limit])


def conservative_takeaway(title: str, page: Mapping[str, Any]) -> str:
    hyperion = page.get("hyperion") or {}
    route_terms = ranked_profile_terms(hyperion.get("route_profile") or {}, route_label, 3)
    return (
        f"{title} is read through the quantum constructor near {route_terms}. "
        "The page is useful when its state carrier, operator or map, admissibility condition, and readout are made explicit."
    )


def conservative_mechanism_view(title: str, page: Mapping[str, Any]) -> str:
    hyperion = page.get("hyperion") or {}
    route_terms = ranked_profile_terms(hyperion.get("route_profile") or {}, route_label, 4)
    fiber_terms = ranked_profile_terms(hyperion.get("fiber_profile") or {}, fiber_label, 3)
    return (
        f"Operationally, {title} is read through {route_terms}. "
        f"The carrier profile emphasizes {fiber_terms}. "
        "To use the page constructively, name the state space or state variable, the operator or generator, "
        "the admissibility condition, the readout channel, and the comparison that separates this role from a neighboring one."
    )


def conservative_conversion_form() -> list[str]:
    return [
        "Carrier: specify the topic-native state space or state variable.",
        "Map: specify the operator, generator, constraint, or transformation acting on that carrier.",
        "Admissibility: specify the boundary, gauge, preparation, symmetry, or conservation law.",
        "Readout: specify the spectrum, probability distribution, correlation, scattering amplitude, or detector event.",
        "Comparison: specify the condition that distinguishes this role from an adjacent branch assignment.",
    ]


def sanitize_object_view(text: str) -> str:
    sentences = []
    for part in str(text or "").replace("\n", " ").split(". "):
        sentence = part.strip()
        if not sentence:
            continue
        lower = sentence.lower()
        if "morphwiki" in lower:
            continue
        if "operator-spectral construction" in lower:
            continue
        if "mechanism roles" in lower:
            continue
        sentences.append(sentence.rstrip("."))
    cleaned = ". ".join(sentences).strip()
    if cleaned and not cleaned.endswith("."):
        cleaned += "."
    return cleaned


TOPIC_PUBLIC_OVERRIDES = {
    "quantum_mechanics": {
        "takeaway": (
            "Quantum mechanics is the formalism that assigns probabilities to the possible outcomes of physical questions by representing states in Hilbert space and representing observable questions by operators with spectra."
        ),
        "mechanism_view": (
            "The core construction is not a list of quantum objects. A preparation gives a state vector or density operator. A physical question is represented by a self-adjoint operator or by a measurement operator family. The spectrum of that operator supplies the possible outcome labels, and the Born or trace rule assigns probabilities to the corresponding projectors. Time evolution is generated by the Hamiltonian through a unitary map. Non-commuting observables mark questions that cannot be resolved in one common sharp basis."
        ),
        "conversion_form": [
            "A prepared state lives in a Hilbert space.",
            "The observable, Hamiltonian, or measurement operator represents the physical question.",
            "The operator resolves into spectral projectors or measurement effects.",
            "The Born or trace rule assigns probabilities.",
            "Commutators decide which questions can share a sharp readout.",
        ],
        "grammar": {
            "state": ["state vector", "wave function", "density operator"],
            "operator": ["self-adjoint observable", "Hamiltonian", "measurement operator"],
            "spectrum": ["eigenvalue", "projector", "measurement outcome"],
            "boundary": ["preparation", "basis", "experimental arrangement"],
            "incompatibility": ["commutator", "non-common eigenbasis"],
            "protocol": ["Born rule", "trace rule", "unitary evolution"],
        },
        "mathematical_skeleton": (
            "\\rho\\ge 0,\\quad \\operatorname{Tr}\\rho=1\n"
            "A=\\sum_a aP_a,\\quad p(a)=\\operatorname{Tr}(\\rho P_a)\n"
            "\\rho(t)=U(t)\\rho(0)U(t)^\\dagger,\\quad U(t)=e^{-iHt/\\hbar}\n"
            "[A,B]\\ne 0\\quad\\Rightarrow\\quad \\text{no generic common sharp eigenbasis}"
        ),
    },
    "photon": {
        "takeaway": (
            "A photon is the one-quantum excitation of an electromagnetic field mode: its identity is fixed by field quantization, massless dispersion, polarization, gauge constraints, and detector readout."
        ),
        "mechanism_view": (
            "The photon page should not be reduced to a generic prepared-state template. The native construction starts with the electromagnetic field decomposed into modes. Quantization assigns creation and annihilation operators to those modes; applying a creation operator to the vacuum gives a one-photon state. The readouts are mode occupation, frequency or energy, momentum, polarization, and detection events. The admissibility constraints include massless dispersion and transversality or gauge conditions, which distinguish the photon from a generic quantum particle."
        ),
        "conversion_form": [
            "The electromagnetic field decomposes into modes labelled by wave vector and polarization.",
            "Each mode is quantized with creation and annihilation operators.",
            "A one-photon state is the result of applying a creation operator to the vacuum.",
            "Occupation number, energy, momentum, polarization, and detector clicks are readout channels.",
            "Massless dispersion and transverse or gauge-compatible polarization define admissibility.",
        ],
        "grammar": {
            "state": ["one-photon Fock state", "electromagnetic mode", "polarization state"],
            "operator": ["creation operator", "annihilation operator", "number operator", "field operator"],
            "spectrum": ["frequency", "energy", "momentum", "polarization", "detection count"],
            "boundary": ["mode boundary", "cavity", "free-space asymptotic condition", "gauge constraint"],
            "incompatibility": ["number-phase relation", "polarization basis choice", "gauge constraint"],
            "protocol": ["emission", "absorption", "photodetection", "interferometry"],
        },
        "mathematical_skeleton": (
            "E=\\hbar\\omega,\\quad \\mathbf p=\\hbar\\mathbf k,\\quad \\omega=c|\\mathbf k|\n"
            "|1_{\\mathbf k,\\lambda}\\rangle=a_{\\mathbf k,\\lambda}^{\\dagger}|0\\rangle\n"
            "\\hat N_{\\mathbf k,\\lambda}=a_{\\mathbf k,\\lambda}^{\\dagger}a_{\\mathbf k,\\lambda}\n"
            "\\mathbf k\\cdot\\boldsymbol\\epsilon_{\\mathbf k,\\lambda}=0"
        ),
    },
    "electron": {
        "takeaway": (
            "An electron is a stable charged spin-1/2 excitation whose operational identity is fixed by charge, mass, spin, fermionic statistics, and its coupling to electromagnetic fields."
        ),
        "mechanism_view": (
            "The electron page has a native constructor that combines a spinor state, a relativistic generator, a conserved charge, and fermionic anticommutation. In nonrelativistic settings this appears as a Schrödinger or Pauli state under electromagnetic coupling; in relativistic field theory it appears as a Dirac field excitation. The readouts are charge, mass-energy, spin, momentum, and scattering or detector events."
        ),
        "conversion_form": [
            "The spinor or field state carries electron quantum numbers.",
            "The Schrödinger, Pauli, or Dirac generator defines the regime-specific evolution.",
            "Charge conservation and fermionic exchange statistics define admissibility.",
            "Electromagnetic potentials couple through minimal coupling.",
            "Energy, momentum, spin, charge, and scattering response are readout channels.",
        ],
        "grammar": {
            "state": ["spinor state", "Dirac field excitation", "electron wave packet"],
            "operator": ["Dirac operator", "Pauli Hamiltonian", "charge operator"],
            "spectrum": ["energy", "momentum", "spin projection", "charge"],
            "boundary": ["electromagnetic potential", "scattering boundary", "confining potential"],
            "incompatibility": ["fermionic anticommutation", "spin measurement basis"],
            "protocol": ["scattering", "spectroscopy", "charge detection"],
        },
        "mathematical_skeleton": (
            "(i\\hbar\\gamma^{\\mu}D_{\\mu}-mc)\\psi=0\n"
            "D_{\\mu}=\\partial_{\\mu}+\\frac{ie}{\\hbar c}A_{\\mu}\n"
            "\\{\\psi_{\\alpha}(x),\\psi_{\\beta}^{\\dagger}(y)\\}=\\delta_{\\alpha\\beta}\\delta(x-y)"
        ),
    },
    "fermion": {
        "takeaway": (
            "A fermion is a quantum excitation whose defining mechanism is antisymmetric exchange: two identical fermions cannot occupy the same one-particle state."
        ),
        "mechanism_view": (
            "The fermion constructor is an exchange constraint on state space, not a generic particle label. Many-body states are antisymmetrized, field operators anticommute, and occupation numbers are restricted to zero or one for each mode. This exchange rule explains why the same operator/spectrum machinery produces Pauli exclusion, Fermi surfaces, and fermionic field excitations."
        ),
        "conversion_form": [
            "The many-particle state lives in an antisymmetric sector.",
            "Creation and annihilation operators anticommute.",
            "Mode occupation is restricted to zero or one.",
            "Number, energy, momentum, spin, or charge provide field-dependent readouts.",
            "Exchange of identical particles changes the sign of the state.",
        ],
        "grammar": {
            "state": ["antisymmetric many-body state", "fermionic Fock state", "occupied mode"],
            "operator": ["fermionic creation operator", "fermionic annihilation operator", "number operator"],
            "spectrum": ["occupation number", "energy", "momentum", "spin"],
            "boundary": ["exchange symmetry sector", "mode basis"],
            "incompatibility": ["anticommutation", "Pauli exclusion"],
            "protocol": ["mode filling", "fermionic quantization"],
        },
        "mathematical_skeleton": (
            "\\mathcal F_{-}(\\mathcal H)=\\bigoplus_{n=0}^{\\infty}\\wedge^n\\mathcal H\n"
            "\\{a_i,a_j^{\\dagger}\\}=\\delta_{ij},\\quad \\{a_i,a_j\\}=0\n"
            "n_i=a_i^{\\dagger}a_i\\in\\{0,1\\}"
        ),
    },
    "boson": {
        "takeaway": (
            "A boson is a quantum excitation whose defining mechanism is symmetric exchange: many identical quanta may occupy the same mode."
        ),
        "mechanism_view": (
            "The boson constructor is the symmetric counterpart of the fermion constructor. Many-body states live in symmetric sectors, creation and annihilation operators commute, and a single mode can carry any nonnegative occupation number. This is the mechanism behind field modes, coherent states, Bose-Einstein condensation, and photon-like occupation readouts."
        ),
        "conversion_form": [
            "The many-particle state lives in a symmetric sector.",
            "Creation and annihilation operators commute.",
            "Each mode allows arbitrary nonnegative occupation.",
            "Number, energy, momentum, phase-sensitive field amplitude, or correlations provide readouts.",
            "Exchange of identical particles leaves the state unchanged.",
        ],
        "grammar": {
            "state": ["symmetric many-body state", "bosonic Fock state", "mode occupation"],
            "operator": ["bosonic creation operator", "bosonic annihilation operator", "number operator"],
            "spectrum": ["occupation number", "mode energy", "correlation spectrum"],
            "boundary": ["exchange symmetry sector", "mode basis"],
            "incompatibility": ["commutation relation", "number-phase relation"],
            "protocol": ["mode occupation", "bosonic quantization", "coherent-state preparation"],
        },
        "mathematical_skeleton": (
            "\\mathcal F_{+}(\\mathcal H)=\\bigoplus_{n=0}^{\\infty}\\operatorname{Sym}^n\\mathcal H\n"
            "[a_i,a_j^{\\dagger}]=\\delta_{ij},\\quad [a_i,a_j]=0\n"
            "n_i=a_i^{\\dagger}a_i\\in\\{0,1,2,\\ldots\\}"
        ),
    },
    "creation_and_annihilation_operators": {
        "takeaway": (
            "Creation and annihilation operators are the algebraic moves that change mode occupation; they are the mechanism by which fixed-particle quantum mechanics becomes field or many-body quantum theory."
        ),
        "mechanism_view": (
            "This page is about the operation that moves a state between occupation sectors. A creation operator adds one quantum to a mode, an annihilation operator removes one, and their commutation or anticommutation relation selects bosonic or fermionic statistics. The number operator then supplies the spectral readout of occupation. The central mechanism is therefore sector-changing algebra, not a generic Hamiltonian question."
        ),
        "conversion_form": [
            "The mode basis defines the occupation sectors.",
            "Creation and annihilation operators add or remove one quantum in a mode.",
            "Commutation or anticommutation selects the particle statistics.",
            "Number operators are constructed from creation-annihilation pairs.",
            "The occupation spectrum is the readout.",
        ],
        "grammar": {
            "state": ["occupation-number state", "Fock state", "mode state"],
            "operator": ["creation operator", "annihilation operator", "number operator"],
            "spectrum": ["occupation number", "mode population"],
            "boundary": ["mode basis", "statistics sector"],
            "incompatibility": ["commutation relation", "anticommutation relation"],
            "protocol": ["add one quantum", "remove one quantum", "normal ordering"],
        },
        "mathematical_skeleton": (
            "a_i^{\\dagger}|\\ldots,n_i,\\ldots\\rangle=\\sqrt{n_i+1}|\\ldots,n_i+1,\\ldots\\rangle\n"
            "a_i|\\ldots,n_i,\\ldots\\rangle=\\sqrt{n_i}|\\ldots,n_i-1,\\ldots\\rangle\n"
            "N_i=a_i^{\\dagger}a_i"
        ),
    },
    "fock_space": {
        "takeaway": (
            "Fock space is the occupation-number version of quantum state space: it replaces a fixed-particle Hilbert space with a direct sum over sectors containing zero, one, two, or more identical quanta."
        ),
        "mechanism_view": (
            "Fock space changes the carrier of the theory. A single-particle Hilbert space is lifted to a many-sector space, and the exchange rule selects bosonic or fermionic sectors. Creation and annihilation operators then become the native operations: they move the state between particle-number sectors, while the number operator provides the spectral readout of occupation. The important mechanism is therefore not a generic state-to-spectrum template, but the conversion from fixed-particle description to occupation-number dynamics."
        ),
        "conversion_form": [
            "The one-particle Hilbert space H is the seed carrier.",
            "The full carrier is a direct sum of n-particle sectors, symmetrized for bosons or antisymmetrized for fermions.",
            "Creation and annihilation operators move states between occupation sectors.",
            "The number operator or mode observables provide the spectral readout.",
            "The commutation or anticommutation rule encodes the particle statistics.",
        ],
        "grammar": {
            "state": ["occupation-number state", "Fock vector", "n-particle sector"],
            "operator": ["creation operator", "annihilation operator", "number operator"],
            "spectrum": ["occupation number", "mode population", "particle-number sector"],
            "boundary": ["bosonic symmetrization", "fermionic antisymmetrization"],
            "incompatibility": ["commutation relation", "anticommutation relation"],
            "protocol": ["sector-changing operation", "mode expansion"],
        },
        "mathematical_skeleton": (
            "\\mathcal F_{\\pm}(\\mathcal H)=\\bigoplus_{n=0}^{\\infty}\\mathcal S_{\\pm}\\mathcal H^{\\otimes n}\n"
            "[a_i,a_j^\\dagger]_{\\mp}=\\delta_{ij},\\quad [a_i,a_j]_{\\mp}=0\n"
            "N=\\sum_i a_i^\\dagger a_i"
        ),
    },
    "quantum_geometry": {
        "takeaway": (
            "Quantum geometry treats geometric quantities as quantum observables: geometry is not only a background stage, but a state-dependent structure with possible spectral readouts."
        ),
        "mechanism_view": (
            "Quantum geometry is not the same mechanism as Fock space. Its carrier is a quantum state of geometry, often represented by graph or spin-network data. The operator-to-spectrum step asks for eigenvalues of geometric observables such as area or volume. The mechanism therefore sits at the geometry/boundary frontier: a geometric quantity is promoted to an operator, and the readout is a spectrum of admissible geometric values."
        ),
        "conversion_form": [
            "The graph, spin-network, or quantum-gravity state space is the carrier.",
            "Geometric data are represented as quantum labels or states rather than as a fixed smooth background.",
            "Area, volume, or metric-related quantities become operators.",
            "The spectra of those geometric operators provide readouts.",
            "The invariant content is the part of the geometric readout that survives changes of graph, gauge, or boundary description.",
        ],
        "grammar": {
            "state": ["spin-network state", "quantum geometry state", "graph-labelled state"],
            "operator": ["area operator", "volume operator", "geometric observable"],
            "spectrum": ["area spectrum", "volume spectrum", "geometry eigenvalue"],
            "boundary": ["graph boundary", "spin-network graph", "Planck-scale domain"],
            "incompatibility": ["non-commuting geometric observables", "constraint algebra"],
            "protocol": ["geometric measurement", "coarse graining", "spin-foam transition"],
        },
        "mathematical_skeleton": (
            "\\mathcal H_{\\Gamma}=L^2(SU(2)^E/SU(2)^V),\\quad |\\Gamma,j_e,\\iota_v\\rangle\n"
            "\\hat A(S)|\\Gamma,j,\\iota\\rangle=8\\pi\\gamma\\ell_P^2\\sum_{e\\cap S}\\sqrt{j_e(j_e+1)}|\\Gamma,j,\\iota\\rangle\n"
            "\\hat G|g_i\\rangle=g_i|g_i\\rangle"
        ),
    },
}


def rewrite_page(path: Path) -> bool:
    page = load_json(path)
    morph = page.get("morphwiki")
    wiki = page.get("wikipedia")
    if not isinstance(morph, dict) or not isinstance(wiki, dict):
        return False
    title = str(wiki.get("title") or path.stem.replace("_", " "))
    grammar = morph.get("grammar") or {}
    if not isinstance(grammar, dict):
        return False
    text = " ".join(
        str(value or "")
        for value in (wiki.get("title"), wiki.get("description"), wiki.get("summary"), morph.get("object_view"))
    )
    override = TOPIC_PUBLIC_OVERRIDES.get(path.stem)
    if override:
        morph.update({key: value for key, value in override.items() if key != "grammar"})
        morph["grammar"] = override["grammar"]
        grammar = morph["grammar"]
        morph["mathematical_skeleton_is_source_backed"] = False
        morph["mathematical_skeleton_is_topic_native"] = True
        morph.update(update_public_lists())
    else:
        morph["object_view"] = sanitize_object_view(str(morph.get("object_view") or wiki.get("summary") or ""))
        morph["takeaway"] = conservative_takeaway(title, page)
        morph["mechanism_view"] = conservative_mechanism_view(title, page)
        morph["conversion_form"] = conservative_conversion_form()
        morph["mathematical_skeleton"] = ""
        morph["mathematical_skeleton_is_source_backed"] = False
        morph["mathematical_skeleton_is_topic_native"] = False
        morph.update(conservative_public_lists())
    if isinstance(morph.get("mathematical_skeleton"), str) and not override:
        morph["mathematical_skeleton"] = ""
        morph["mathematical_skeleton_is_source_backed"] = False
    morph["public_language_rewritten"] = True
    morph["public_language_rewritten_at"] = datetime.now(timezone.utc).isoformat()
    write_json(path, page)
    write_text(path.with_suffix(".md"), render_markdown(page))
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pages-dir", type=Path, default=Path("discoveries/morphwiki_quantum/pages"))
    args = parser.parse_args()
    count = 0
    for path in sorted(args.pages_dir.glob("*.json")):
        if rewrite_page(path):
            count += 1
    print(json.dumps({"pages_dir": str(args.pages_dir), "rewritten": count}, indent=2))


if __name__ == "__main__":
    main()
