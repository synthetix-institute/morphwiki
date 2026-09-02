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
            "Fermionic exchange constrains the global many-body state: antisymmetry removes coincidence states and thereby produces exclusion, exchange holes, Fermi surfaces, and degeneracy pressure before a repulsive interaction is introduced."
        ),
        "mechanism_view": (
            "The fermion construction is an exchange constraint on state space, not a particle label. The wave function changes sign under exchange and vanishes when identical one-particle states coincide. Exterior Fock space and canonical anticommutation preserve that nodal restriction when particle number changes. At finite density, distinct modes fill to a Fermi surface and generate degeneracy pressure without pairwise repulsion. Pairing can move the state into an even-parity collective sector, while mappings to spins or hard-core bosons preserve selected spectra only by changing locality or correlation observables."
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
            "\\Psi(\\ldots,x_i,\\ldots,x_j,\\ldots)=-\\Psi(\\ldots,x_j,\\ldots,x_i,\\ldots)\n"
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
    "commutator": {
        "takeaway": (
            "A commutator measures the physical consequence of exchanging two operations: it governs joint measurability, generated motion, and the leading difference between reversed protocols."
        ),
        "mechanism_view": (
            "For two operators defined on a common domain, [A,B]=AB-BA compares the two possible orders. For observables, a nonzero commutator obstructs a common sharp spectral resolution and enters uncertainty bounds. For a Hamiltonian H, [H,A] gives the dynamical change of A in the Heisenberg picture. For short control pulses, [A,B] is the first term that distinguishes the protocols exp(epsilon A)exp(epsilon B) and exp(epsilon B)exp(epsilon A). The same algebraic object therefore connects compatibility, dynamics, and order-sensitive response."
        ),
        "conversion_form": [
            "Both operators are defined on a stated common domain.",
            "The ordered products AB and BA are formed on that domain.",
            "Their difference determines joint spectral compatibility or order sensitivity.",
            "A state and observable convert the algebraic difference into a measurable bound or response.",
        ],
        "grammar": {
            "state": ["common operator domain", "prepared quantum state"],
            "operator": ["ordered product", "commutator", "Hamiltonian generator"],
            "spectrum": ["common eigenspace", "uncertainty bound", "order-dependent response"],
            "boundary": ["operator domain", "control-pulse duration"],
            "incompatibility": ["nonzero commutator", "absence of common sharp refinement"],
            "protocol": ["AB ordering", "BA ordering", "short-pulse sequence"],
        },
        "mathematical_skeleton": (
            "[A,B]=AB-BA\n"
            "\\frac{dA}{dt}=\\frac{i}{\\hbar}[H,A]+\\left(\\frac{\\partial A}{\\partial t}\\right)\n"
            "\\Delta A\\,\\Delta B\\geq\\frac12|\\langle[A,B]\\rangle|\n"
            "e^{\\epsilon A}e^{\\epsilon B}e^{-\\epsilon A}e^{-\\epsilon B}=I+\\epsilon^2[A,B]+O(\\epsilon^3)"
        ),
        "what_survives": [
            "The commutator transforms covariantly under a simultaneous unitary change of representation.",
            "Joint spectral compatibility is unchanged by a consistent representation change.",
            "The leading order-sensitive response survives when different physical controls realize the same operator algebra.",
        ],
        "what_changes": [
            "The matrix entries, basis, carrier, and physical implementation of the two operations may change.",
            "Domains can change the meaning of formal commutation relations for unbounded operators.",
            "The observable consequence depends on the prepared state and on how the operator difference is read out.",
        ],
        "missing_experiments": [
            "Reversing two calibrated operations isolates the part of the response proportional to their commutator.",
            "A commuting control pair removes the order-sensitive contribution without changing the individual operations.",
            "Agreement requires the same domain and the same measured observable, not merely similar operator notation.",
        ],
    },
    "quantum_entanglement": {
        "takeaway": (
            "Entanglement is a property of a composite state that cannot be written as a classical mixture of product states across a chosen subsystem decomposition; for a pure state, this reduces to failure to factor."
        ),
        "mechanism_view": (
            "The tensor-product decomposition specifies what counts as subsystem A and subsystem B. A pure state is entangled when its Schmidt rank exceeds one. Each subsystem can then be mixed even though the joint state is pure, because partial tracing discards the correlations that purify it. Local basis changes preserve the Schmidt coefficients, while a different physical factorization can change whether the same vector is called entangled. Bell measurements test whether the resulting correlations admit a local hidden-variable model."
        ),
        "conversion_form": [
            "A physical subsystem algebra or tensor-product factorization is stated.",
            "The joint state is decomposed into Schmidt modes or tested for separability.",
            "Partial traces give the states available to local observers.",
            "Correlation observables distinguish the joint state from independent local preparations.",
        ],
        "grammar": {
            "state": ["bipartite state", "Schmidt decomposition", "reduced density operator"],
            "operator": ["partial trace", "local observable", "correlation operator"],
            "spectrum": ["Schmidt spectrum", "entanglement entropy", "Bell correlator"],
            "boundary": ["subsystem algebra", "tensor-product factorization"],
            "incompatibility": ["nonseparability", "Bell inequality violation"],
            "protocol": ["local preparation", "separated measurement", "correlation readout"],
        },
        "mathematical_skeleton": (
            "|\\Psi\\rangle=\\sum_k\\sqrt{\\lambda_k}|k_A\\rangle|k_B\\rangle,\\quad \\sum_k\\lambda_k=1\n"
            "\\rho_A=\\operatorname{Tr}_B|\\Psi\\rangle\\langle\\Psi|\n"
            "S(\\rho_A)=-\\operatorname{Tr}(\\rho_A\\log\\rho_A)\n"
            "|S_{\\mathrm{CHSH}}|\\leq2,\\qquad |S_{\\mathrm{CHSH}}|_{\\mathrm{QM}}\\leq2\\sqrt2"
        ),
        "what_survives": [
            "Schmidt coefficients and entanglement entropy are invariant under local unitary changes of basis.",
            "The reduced-state spectra preserve the amount of pure-state bipartite entanglement.",
            "Correlations remain joint properties even when neither subsystem has a pure local state.",
        ],
        "what_changes": [
            "The chosen subsystem factorization and accessible observable algebra determine which correlations count as entanglement.",
            "Noise, loss, and coarse graining can convert pure-state entanglement into mixed-state correlations.",
            "Different platforms realize the same Schmidt structure with photons, spins, atoms, modes, or encoded qubits.",
        ],
        "missing_experiments": [
            "Local measurements reconstruct a correlation witness or Bell parameter that product preparations cannot reproduce.",
            "Independent local-unitary rotations leave the inferred Schmidt spectrum unchanged.",
            "A separable-state control fixes the correlation background of the apparatus.",
        ],
    },
    "gauge_theory": {
        "takeaway": (
            "Gauge theory defines how internal states are compared at different spacetime points: a connection relates neighboring frames, and curvature records the path dependence that no single gauge choice can remove."
        ),
        "mechanism_view": (
            "A local gauge transformation changes the field coordinates used at each point without changing the physical state. Ordinary derivatives compare fields in different local frames and therefore cease to transform covariantly. The gauge connection repairs that comparison. Its commutator gives the field strength, while Wilson loops measure the accumulated transport around a closed path. Gauss constraints select physical states and charges. The connection is representation dependent; curvature, loop observables, and gauge-invariant amplitudes carry the physical content."
        ),
        "conversion_form": [
            "A local symmetry group acts on matter or field variables.",
            "A connection defines covariant comparison between neighboring points.",
            "The commutator of covariant derivatives gives the field strength.",
            "Constraints remove gauge-equivalent descriptions from the physical state space.",
            "Wilson loops, charges, scattering amplitudes, or field strengths provide observables.",
        ],
        "grammar": {
            "state": ["gauge-equivalence class", "matter field", "physical constraint sector"],
            "operator": ["covariant derivative", "connection", "Gauss constraint"],
            "spectrum": ["charge sector", "Wilson loop", "gauge-invariant amplitude"],
            "boundary": ["gauge choice", "bundle patch", "boundary charge"],
            "incompatibility": ["curvature", "nontrivial holonomy", "constraint anomaly"],
            "protocol": ["parallel transport", "closed-loop transport", "gauge fixing"],
        },
        "mathematical_skeleton": (
            "D_\\mu=\\partial_\\mu+igA_\\mu\n"
            "[D_\\mu,D_\\nu]=igF_{\\mu\\nu}\n"
            "W(\\gamma)=\\operatorname{Tr}\\,\\mathcal P\\exp\\left(ig\\oint_\\gamma A_\\mu dx^\\mu\\right)\n"
            "G^a|\\Psi_{\\mathrm{phys}}\\rangle=0"
        ),
        "what_survives": [
            "Gauge-equivalent potentials give the same gauge-invariant amplitudes, field strengths, charges, and loop observables.",
            "Curvature records the infinitesimal holonomy of the connection and cannot be removed by a local gauge choice.",
            "The physical state belongs to the constraint sector rather than to an arbitrary field coordinate representation.",
        ],
        "what_changes": [
            "The gauge potential, local basis, gauge-fixing condition, and coordinate description may change.",
            "The gauge group, representation, matter content, dimension, and boundary conditions specify different physical theories.",
            "Topological sectors and boundary charges can survive even where the local field strength vanishes.",
        ],
        "missing_experiments": [
            "A closed-loop phase or Wilson observable distinguishes nontrivial holonomy from a removable local gauge choice.",
            "Gauge-related descriptions must give identical probabilities for the same physical preparation and readout.",
            "A proposed extra field or interaction must change a gauge-invariant observable rather than only the gauge potential.",
        ],
    },
    "quantum_decoherence": {
        "takeaway": (
            "Quantum decoherence is the loss of observable phase coherence in a subsystem when information about alternative amplitudes becomes encoded in environmental correlations."
        ),
        "mechanism_view": (
            "The combined system and environment may evolve unitarily while the reduced system loses interference. Interaction correlates different system alternatives with distinguishable environmental states; tracing over the environment then suppresses off-diagonal terms in the selected pointer basis. Decoherence does not by itself select one outcome, and it is not identical to memory. Markovian decoherence is possible when the reduced state still determines its future. Memory begins when discarded correlations return and two preparations with the same reduced state acquire different later statistics."
        ),
        "conversion_form": [
            "A joint system-environment state and interaction are specified.",
            "Unitary evolution creates correlations between system alternatives and environmental states.",
            "Partial tracing gives the reduced density operator available to the observer.",
            "Interference visibility or off-diagonal coherence provides the readout.",
            "A divisibility or history test distinguishes Markovian decoherence from memory.",
        ],
        "grammar": {
            "state": ["joint system-environment state", "reduced density operator", "pointer basis"],
            "operator": ["interaction Hamiltonian", "partial trace", "reduced dynamical map"],
            "spectrum": ["coherence", "interference visibility", "purity"],
            "boundary": ["initial environmental state", "system-environment partition"],
            "incompatibility": ["returning correlations", "failure of divisible reduced dynamics"],
            "protocol": ["prepare", "couple", "trace environment", "measure interference"],
        },
        "mathematical_skeleton": (
            "\\rho_S(t)=\\operatorname{Tr}_E[U_{SE}(t)\\rho_{SE}(0)U_{SE}^{\\dagger}(t)]\n"
            "\\frac{|0\\rangle|E_0\\rangle+|1\\rangle|E_1\\rangle}{\\sqrt2},\\quad \\rho_{01}\\propto\\langle E_1|E_0\\rangle\n"
            "\\dot\\rho_S=-\\frac{i}{\\hbar}[H_S,\\rho_S]+\\sum_k\\gamma_k\\mathcal D[L_k]\\rho_S\n"
            "V_{t+s}=V_tV_s\\quad\\text{only in the time-homogeneous Markov limit}"
        ),
        "what_survives": [
            "The joint state retains the phase information transferred from the subsystem into system-environment correlations.",
            "The reduced interference visibility is fixed by the overlap of the corresponding environmental states.",
            "Equivalent dilations give the same reduced channel and the same system observables.",
        ],
        "what_changes": [
            "The preferred basis, decay rate, and recoherence depend on the interaction, environmental spectrum, and initial correlations.",
            "Changing the system-environment partition changes which correlations are hidden.",
            "A Markov approximation removes returning correlations; retaining them introduces auxiliary coordinates or a memory kernel.",
        ],
        "missing_experiments": [
            "Interference visibility is compared with a control in which the environment cannot distinguish the alternatives.",
            "Two preparations with the same reduced state test whether hidden correlations alter later observables.",
            "Reversing or decoupling the interaction tests whether the lost coherence remains recoverable in the joint state.",
        ],
    },
    "renormalization": {
        "takeaway": (
            "Renormalization relates physical descriptions at different resolutions by changing couplings and operator weights while preserving long-distance predictions."
        ),
        "mechanism_view": (
            "Coarse graining removes short-distance variables and generates every operator allowed by the remaining symmetries. Their coefficients flow with scale. Relevant directions grow, irrelevant directions decay, and fixed points organize scale-invariant behaviour. Microscopically different systems can therefore share critical exponents and scaling functions when their flows approach the same fixed point. Universality is the invariance class of this scale transformation, not a visual similarity between equations."
        ),
        "conversion_form": [
            "A resolution scale and a set of effective operators are specified.",
            "Short-distance degrees of freedom are integrated out or coarse grained.",
            "Couplings flow so that observables remain independent of the arbitrary renormalization scale.",
            "Fixed points and relevant directions determine the long-distance universality class.",
        ],
        "grammar": {
            "state": ["effective degrees of freedom", "coarse-grained field", "critical state"],
            "operator": ["renormalization map", "beta function", "effective operator expansion"],
            "spectrum": ["scaling dimension", "critical exponent", "running coupling"],
            "boundary": ["cutoff", "renormalization condition", "coarse-graining scale"],
            "incompatibility": ["relevant perturbation", "anomalous dimension", "operator mixing"],
            "protocol": ["integrate short scales", "rescale", "compare observables"],
        },
        "mathematical_skeleton": (
            "\\mu\\frac{dg_i}{d\\mu}=\\beta_i(\\{g\\})\n"
            "\\left(\\mu\\partial_\\mu+\\beta_i\\partial_{g_i}+n\\gamma\\right)G^{(n)}=0\n"
            "\\beta_i(g_*)=0,\\qquad \\delta g_i(b)=b^{y_i}\\delta g_i\n"
            "\\mathcal L_{\\mathrm{eff}}(\\mu)=\\sum_i c_i(\\mu)\\mathcal O_i"
        ),
        "what_survives": [
            "Observable predictions remain independent of the arbitrary renormalization scale when couplings and fields flow consistently.",
            "Critical exponents and scaling functions are shared by systems approaching the same fixed point with the same relevant directions.",
            "Symmetry and dimensionality constrain the effective operators generated by coarse graining.",
        ],
        "what_changes": [
            "Couplings, field normalizations, effective degrees of freedom, and operator coefficients depend on scale.",
            "Microscopic Hamiltonians can differ while their long-distance flows enter the same universality class.",
            "A relevant perturbation can drive the system away from one fixed point toward another phase or scale regime.",
        ],
        "missing_experiments": [
            "Measurements at several scales determine whether running couplings follow one beta function.",
            "Microscopically different realizations test whether critical exponents and scaling functions coincide.",
            "Corrections to scaling distinguish approach to a fixed point from an exact scale-invariant law.",
        ],
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
        morph.update(update_public_lists())
        morph.update({key: value for key, value in override.items() if key != "grammar"})
        morph["grammar"] = override["grammar"]
        grammar = morph["grammar"]
        morph["mathematical_skeleton_is_source_backed"] = False
        morph["mathematical_skeleton_is_topic_native"] = True
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
    parser.add_argument(
        "--only-overrides",
        action="store_true",
        help="Rewrite only pages with an explicit topic-native model.",
    )
    parser.add_argument(
        "--render-only",
        action="store_true",
        help="Regenerate Markdown from existing JSON without changing page data.",
    )
    args = parser.parse_args()
    count = 0
    for path in sorted(args.pages_dir.glob("*.json")):
        if args.render_only:
            write_text(path.with_suffix(".md"), render_markdown(load_json(path)))
            count += 1
            continue
        if args.only_overrides and path.stem not in TOPIC_PUBLIC_OVERRIDES:
            continue
        if rewrite_page(path):
            count += 1
    print(
        json.dumps(
            {
                "pages_dir": str(args.pages_dir),
                "rendered" if args.render_only else "rewritten": count,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
