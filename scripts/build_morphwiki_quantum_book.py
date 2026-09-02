#!/usr/bin/env python3
"""Build a PDF-ready LaTeX book from the MorphWiki quantum tree."""

from __future__ import annotations

import argparse
import json
import os
import re
import unicodedata
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence

try:
    from morphwiki_constructor import (
        CONSTRUCTOR_CHAIN_LATEX,
        CONSTRUCTOR_CLAUSES,
        COMPATIBILITY_BRANCH_LATEX,
        COMPATIBILITY_RESIDUAL_LATEX,
        DISCOVERY_CONTRACT_LATEX,
        DISCOVERY_PATH_LATEX,
        DISCOVERY_VERBS,
        PHYSICAL_STATE_LATEX,
        PREDICTIVE_CLOSURE_LATEX,
        PREDICTIVE_CLOSURE_PRINCIPLE,
        QUANTUM_BRANCH_PARTS,
        QUANTUM_ROLE_PROMOTIONS,
        ROLE_PROMOTION_CRITERION_LATEX,
        ROLE_PROMOTION_PRINCIPLE,
        public_theory_language,
    )
except ModuleNotFoundError:  # Imported as scripts.build_morphwiki_quantum_book.
    from scripts.morphwiki_constructor import (
        CONSTRUCTOR_CHAIN_LATEX,
        CONSTRUCTOR_CLAUSES,
        COMPATIBILITY_BRANCH_LATEX,
        COMPATIBILITY_RESIDUAL_LATEX,
        DISCOVERY_CONTRACT_LATEX,
        DISCOVERY_PATH_LATEX,
        DISCOVERY_VERBS,
        PHYSICAL_STATE_LATEX,
        PREDICTIVE_CLOSURE_LATEX,
        PREDICTIVE_CLOSURE_PRINCIPLE,
        QUANTUM_BRANCH_PARTS,
        QUANTUM_ROLE_PROMOTIONS,
        ROLE_PROMOTION_CRITERION_LATEX,
        ROLE_PROMOTION_PRINCIPLE,
        public_theory_language,
    )

try:
    from morphwiki_derivation_depth import (
        DERIVATION_DEPTH_SECTIONS,
        classify_derivation_basis,
    )
except ModuleNotFoundError:
    from scripts.morphwiki_derivation_depth import (
        DERIVATION_DEPTH_SECTIONS,
        classify_derivation_basis,
    )


BRANCH_ORDER = [
    "context",
    "states",
    "generators",
    "observables",
    "incompatibility",
    "measurement",
    "protocols",
    "boundaries",
    "fields",
    "annotations",
]

ANOMALY_LABEL_EXPLANATIONS = {
    "weak spectral anchor": (
        "another construction step fixes the admissible question before eigenvalues become meaningful"
    ),
    "boundary-driven dynamics": (
        "preparation, apparatus, context, representation, or boundary conditions are part of the mechanism rather than surrounding detail"
    ),
    "compatibility/closure junction": (
        "the page joins the rules that make a quantum state legal with the rules that restrict jointly resolvable questions"
    ),
    "protocol is unusually explicit": (
        "the order of operations matters; the topic cannot be reduced to a static state, operator, and spectrum"
    ),
    "multi-role hub": (
        "several construction steps meet in one topic, so the page is a junction rather than a clean branch leaf"
    ),
    "branch-ambiguous": (
        "the topic joins two physical roles that cannot be represented by one branch alone"
    ),
}


ANOMALY_PUBLIC_NAMES = {
    "weak spectral anchor": "pre-spectral admissibility",
    "boundary-driven dynamics": "context participates in the law",
    "compatibility/closure junction": "admissibility meets incompatibility",
    "protocol is unusually explicit": "operation order matters",
    "multi-role hub": "several mechanisms meet",
    "branch-ambiguous": "branch interface",
}


def topic_family(slug: str, title: str) -> str:
    """Coarse quantum family used to avoid generic page prose.

    These families are not final classifications.  They provide topic-native
    language for pages that only have route/fiber placement evidence in the
    public export.
    """
    text = f"{slug} {title}".lower()
    if any(term in text for term in ("microscope", "microscopy", "imaging", "metrology", "detector", "sensor", "amplifier")):
        return "instrument_readout"
    if any(term in text for term in ("photon", "electron", "fermion", "boson", "particle", "fock", "field theory", "standard model")):
        return "particle_field"
    if any(term in text for term in ("quantum biology", "coherence", "decoherence", "macroscopic quantum", "fluctuation")):
        return "open_system"
    if any(term in text for term in ("tunnelling", "tunneling", "box", "well", "scattering", "s-matrix", "spectral line", "optics", "cavity", "metamaterial")):
        return "boundary_spectrum"
    if any(term in text for term in ("born", "measurement", "collapse", "povm", "projection", "detector", "qbism", "interpretation", "relational")):
        return "readout"
    if any(term in text for term in ("commutator", "uncertainty", "bell", "epr", "nonlocality", "entanglement", "eraser", "duality")):
        return "compatibility"
    if any(term in text for term in ("circuit", "algorithm", "channel", "logic gate", "network", "cryptography", "error correction", "computing", "programming", "sensor")):
        return "protocol"
    if any(term in text for term in ("gravity", "geometry", "spacetime", "cosmology", "spin foam", "spin network", "ads", "holograph", "string")):
        return "geometry_boundary"
    if any(term in text for term in ("hamiltonian", "schr", "dirac", "klein", "path integral", "unitary", "dynamics", "evolution")):
        return "generator"
    if any(term in text for term in ("hilbert", "state", "wave function", "density matrix", "superposition", "coherence", "qubit")):
        return "state_carrier"
    return "general_quantum"


FAMILY_NATIVE_LANGUAGE: Dict[str, Dict[str, str]] = {
    "particle_field": {
        "role": "many-mode field or particle-realization role",
        "known": "The mechanism is the field/mode version of the constructor: a state space is decomposed into modes or sectors, operators create, annihilate, or constrain those modes, and readouts are occupation, charge, spin, momentum, energy, or scattering response.",
        "missing": "A completed page must name the sector or field algebra, the statistics or gauge constraint, and the observable readout that fixes the particle identity.",
        "equation": r"\mathcal F_{\pm}(\mathcal H),\quad a_k^\dagger,a_k,\quad N_k=a_k^\dagger a_k,\quad \sigma(H)\ \text{or scattering data}",
    },
    "boundary_spectrum": {
        "role": "boundary-shaped spectrum role",
        "known": "The topic changes the admissible domain or boundary condition and thereby changes the allowed spectrum, transmission amplitude, resonance, or scattering channel.",
        "missing": "A completed page must specify the operator domain, boundary condition, potential, interface, or asymptotic channel and show how the spectrum or amplitude changes.",
        "equation": r"H_B\psi=E\psi,\quad \psi\in\mathcal D(H_B),\quad S:\psi_{\rm in}\mapsto\psi_{\rm out}",
    },
    "readout": {
        "role": "probability/readout role",
        "known": "The topic modifies how a state is connected to recorded outcomes. The stable machinery is the spectral measure or POVM together with the probability rule.",
        "missing": "A completed page must distinguish the formal readout map from interpretation: state update, subjective probability, detector record, and ensemble frequency must not be conflated.",
        "equation": r"\Pr(\Delta)=\operatorname{Tr}(\rho E(\Delta)),\quad \rho\mapsto \frac{M_y\rho M_y^\dagger}{\operatorname{Tr}(M_y\rho M_y^\dagger)}",
    },
    "instrument_readout": {
        "role": "instrument-mediated readout role",
        "known": "The mechanism is an apparatus-coupled readout: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate.",
        "missing": "A completed page must name the probe state, interaction Hamiltonian or transfer map, detector observable, reconstruction rule, and control separating sample signal from apparatus artifact.",
        "equation": r"\rho_{\rm probe}\mapsto \mathcal E_{\rm sample}(\rho_{\rm probe}),\quad p(y)=\operatorname{Tr}(M_y\mathcal E_{\rm sample}(\rho_{\rm probe})),\quad \hat s=R(\{y_i\})",
    },
    "compatibility": {
        "role": "compatibility or joint-readout role",
        "known": "The topic tests whether separately legal questions can be resolved together. The mechanism is a restriction on joint spectra, correlations, or admissible hidden-variable assignments.",
        "missing": "A completed page must name the observables, subsystem split, commutator or Bell-type constraint, and the experimental or mathematical inequality that would fail classically.",
        "equation": r"[A,B]\ne0,\quad \Delta A\,\Delta B\ge \frac12|\langle[A,B]\rangle|,\quad S_{\rm Bell}\le 2",
    },
    "protocol": {
        "role": "engineered operation-sequence role",
        "known": "The mechanism is a controlled composition of allowed maps: a sequence that prepares, transforms, protects, transmits, or reads a quantum state.",
        "missing": "A completed page must specify the channel or circuit, the admissibility condition on the maps, the measured output, and the classical or shuffled-protocol control.",
        "equation": r"\rho_{\rm out}=\mathcal E_n\circ\cdots\circ\mathcal E_1(\rho_{\rm in}),\quad \mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger",
    },
    "geometry_boundary": {
        "role": "geometry or holographic realization role",
        "known": "Geometry supplies the realization, boundary, gauge, or dual description in which the operator construction becomes physically legible.",
        "missing": "A completed page must state which operator content is invariant across the geometric representation and which boundary or metric data change the readout.",
        "equation": r"\mathcal A_{\rm bulk}\leftrightarrow \mathcal A_{\partial},\quad Z_{\rm bulk}[\phi|_{\partial}=J]=\left\langle e^{\int J\mathcal O}\right\rangle_{\partial}",
    },
    "generator": {
        "role": "lawful state-transport role",
        "known": "The Hamiltonian, Liouvillian, action, or channel determines the change of state that precedes measurement.",
        "missing": "A completed page must name the state carrier, generator, domain, conserved quantity or symmetry, and the readout that tests the generated motion.",
        "equation": r"i\hbar\partial_t\rho=[H,\rho],\quad U(t)=e^{-iHt/\hbar},\quad H\psi=E\psi",
    },
    "state_carrier": {
        "role": "state-carrier role",
        "known": "The topic contributes the mathematical carrier of prediction: vector, wavefunction, density operator, register, coherent state, or field state.",
        "missing": "A completed page must specify the admissible state space, normalization or positivity condition, representation, and observable that reads the carrier.",
        "equation": r"\ket{\psi}\in\mathcal H,\quad \rho\ge0,\quad \operatorname{Tr}\rho=1,\quad p_i=\operatorname{Tr}(\rho P_i)",
    },
    "general_quantum": {
        "role": "formal quantum role",
        "known": "The topic enters through a state space, admissible transformations, and observable consequences.",
        "missing": "A complete treatment states the carrier, operator or map, admissibility condition, observable, and a consequence that distinguishes the mechanism from alternatives.",
        "equation": r"C\mapsto(\mathcal H_C,\mathcal D_C),\quad \rho\mapsto U\rho U^\dagger,\quad A=\int\lambda\,dE_A(\lambda)",
    },
    "open_system": {
        "role": "open-system transport and coherence role",
        "known": "The topic concerns quantum state transport under environmental coupling, coherence loss, biological or macroscopic boundary conditions, or effective dynamics outside an ideal closed system.",
        "missing": "A completed page must name the relevant state carrier, Hamiltonian or Lindbladian generator, environmental coupling, coherence/readout observable, and the control that separates quantum transport from classical noise.",
        "equation": r"\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k\left(L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}\right),\quad C(t)=\operatorname{Tr}(\rho(t)O)",
    },
}


FAMILY_MECHANISM_FRAMES: Dict[str, Dict[str, str]] = {
    "particle_field": {
        "carrier": "Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data.",
        "operator": "Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector.",
        "admissibility": "Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal.",
        "readout": "Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.",
        "test": "The field description must preserve the relevant observables under changes of representation and reduce to the expected particle or quasiparticle limit when that limit exists.",
    },
    "boundary_spectrum": {
        "carrier": "A Hilbert space with a selected domain, potential, interface, asymptotic channel, cavity, well, or boundary condition.",
        "operator": "A Hamiltonian, wave operator, transfer operator, or scattering map whose domain is changed by the boundary.",
        "admissibility": "Boundary conditions and matching conditions determine allowed states, resonances, transmission amplitudes, and spectra.",
        "readout": "Eigenvalues, resonances, tunnelling probabilities, phase shifts, reflection/transmission amplitudes, or scattering data.",
        "test": "Changing the boundary should change the spectrum or amplitude in the predicted way, while the free or asymptotic limit is recovered when the boundary is removed.",
    },
    "readout": {
        "carrier": "A state vector or density operator together with the measurement context in which outcome channels are defined.",
        "operator": "A projection-valued measure, POVM, update map, or instrument map connecting state to record.",
        "admissibility": "Outcome probabilities must be positive, normalized, and tied to a specified readout map rather than to informal observer language.",
        "readout": "Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.",
        "test": "The interpretation is constrained by whether it changes the probability rule, the update rule, the detector model, or only the language used for them.",
    },
    "instrument_readout": {
        "carrier": "A probe state, sample state, field mode, detector state, or estimation register.",
        "operator": "An interaction Hamiltonian, transfer map, measurement channel, reconstruction map, or estimator.",
        "admissibility": "The instrument must separate sample signal from preparation, detector response, calibration, noise, and reconstruction artifacts.",
        "readout": "Counts, images, spectra, phase shifts, trajectories, intensity maps, correlation data, or parameter estimates.",
        "test": "The claimed mechanism is credible only when the same readout survives control experiments, calibration changes, and reconstruction checks.",
    },
    "compatibility": {
        "carrier": "One state space or a multipartite state space on which several questions can be asked.",
        "operator": "Two or more observables, contexts, correlation operators, or hidden-variable assignments being compared.",
        "admissibility": "Commutators, uncertainty bounds, contextuality constraints, or Bell-type inequalities decide which joint assignments are possible.",
        "readout": "Joint spectra, correlations, inequality violations, uncertainty products, or incompatible outcome statistics.",
        "test": "The non-classical content appears only if the incompatible questions cannot be replaced by one common sharp classical assignment.",
    },
    "protocol": {
        "carrier": "An input state, register, channel state, error syndrome, key, or controlled experimental configuration.",
        "operator": "An ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps.",
        "admissibility": "Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective.",
        "readout": "Output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.",
        "test": "Changing operation order, inserting classical controls, or replacing a quantum channel should identify which step carries the effect.",
    },
    "geometry_boundary": {
        "carrier": "A spacetime, boundary algebra, gauge orbit, spin network, bulk/boundary pair, or geometric representation of a quantum state space.",
        "operator": "Hamiltonian, action, constraint, boundary operator, correlation map, or dictionary between two representations.",
        "admissibility": "Gauge, boundary, metric, covariance, and constraint conditions decide which geometric descriptions represent the same physical content.",
        "readout": "Boundary correlators, spectra, entropies, scattering data, geometric invariants, or reconstructed bulk quantities.",
        "test": "A geometric reformulation is physical only to the extent that it preserves observables or correlation functions across the representation change.",
    },
    "generator": {
        "carrier": "A state vector, density operator, wavefunction, field state, or register on a specified domain.",
        "operator": "Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.",
        "admissibility": "Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal.",
        "readout": "Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.",
        "test": "The generator must predict the observed evolution while preserving the relevant normalization, positivity, symmetry, or conservation constraint.",
    },
    "state_carrier": {
        "carrier": "The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register.",
        "operator": "Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.",
        "admissibility": "Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states.",
        "readout": "Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.",
        "test": "Equivalent representations must preserve probabilities and expectation values when the change is only representational.",
    },
    "general_quantum": {
        "carrier": "A context-selected state space or effective carrier for prediction.",
        "operator": "The relevant Hamiltonian, observable, channel, constraint, or update map.",
        "admissibility": "Domain, normalization, positivity, compatibility, boundary, or gauge requirements state what is legal.",
        "readout": "The outcome probabilities, spectra, correlations, amplitudes, or records used to test the mechanism.",
        "test": "A complete account must specify state carrier, operator or map, admissibility condition, readout, and at least one possible falsifier.",
    },
    "open_system": {
        "carrier": "A density operator, reduced state, coherence variable, bath-coupled state, or effective mesoscopic carrier.",
        "operator": "Hamiltonian plus environmental coupling, Lindbladian, memory kernel, stochastic map, or effective transport operator.",
        "admissibility": "Positivity, trace preservation, timescale separation, bath assumptions, and control over classical noise determine whether the model is legal.",
        "readout": "Coherence, population transfer, relaxation rate, transport efficiency, noise spectrum, or macroscopic response.",
        "test": "The quantum contribution must survive controls against classical noise, preparation artifacts, and coarse-graining choices.",
    },
}


BRANCH_FRAME_FOCUS: Dict[str, str] = {
    "context": "This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.",
    "states": "This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.",
    "generators": "This page is read first as a lawful-transport move: it identifies what changes the state before measurement.",
    "observables": "This page is read first as a question-selection move: it identifies the observable and its possible values.",
    "measurement": "This page is read first as a measurement move: it connects the state and observable to outcome probabilities.",
    "incompatibility": "This page is read first as a compatibility move: it asks which otherwise legal questions cannot share one sharp answer set.",
    "boundaries": "This page is read first as a realization move: it changes the domain, boundary, geometry, or interface in which the operator acts.",
    "fields": "This page is read first as a many-mode or field-realization move: it extends the state and operator construction beyond a single-particle carrier.",
    "protocols": "This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.",
    "annotations": "This page is read first as an interpretive or historical move: it clarifies which formal layer is being discussed.",
}

BRANCH_PUBLIC_ROLE: Dict[str, str] = {
    "context": "representation and domain role",
    "states": "state or sector role",
    "generators": "generator or transformation role",
    "observables": "observable and spectral role",
    "measurement": "probability and measurement role",
    "incompatibility": "compatibility and correlation role",
    "boundaries": "boundary and spectral role",
    "fields": "many-body or field-theoretic role",
    "protocols": "engineered transformation role",
    "annotations": "historical or interpretive role",
}

BRANCH_PUBLIC_DESCRIPTION: Dict[str, str] = {
    "context": "The state space, representation, basis, and operator domain determine which vectors are physical and which operators are defined.",
    "states": "The state vector or density operator carries the preparation information from which probabilities are calculated.",
    "generators": "The Hamiltonian, action, Liouvillian, or channel determines how an admissible state changes.",
    "observables": "An observable represents a physical quantity; its spectrum gives the possible sharp values and the state fixes their probabilities.",
    "measurement": "A measurement couples a prepared state to recorded outcomes and, when conditioning is retained, to the resulting state change.",
    "incompatibility": "Commutators and correlation constraints determine which observables can share a sharp assignment.",
    "boundaries": "Boundary conditions, interfaces, and asymptotic channels enter the operator domain and alter the allowed solutions and spectra.",
    "fields": "Field and many-body theories enlarge the state space to variable occupation, local fields, gauge sectors, and collective modes.",
    "protocols": "Circuits, controls, and sensing sequences are ordered compositions of physical transformations and measurements.",
    "annotations": "Historical and interpretive accounts concern the meaning of the formal relations without adding a dynamical law.",
}


BRANCH_EXPLANATIONS: Dict[str, Dict[str, str]] = {
    "context": {
        "why": (
            "{title} is needed because a quantum equation has no fixed meaning until its state space, "
            "inner product, representation, and operator domains have been specified. These choices decide "
            "which states are admissible and which apparent changes are only changes of coordinates."
        ),
        "reading": (
            "A unitary or isometric change of representation carries the state and operator together. Amplitudes, expectation values, and spectra agree. "
            "If they do not, the physical model has changed rather than merely its notation."
        ),
        "connection": (
            "A quantum state belongs to this state space, and every Hamiltonian and observable must act on its stated domain. "
            "These domain relations determine whether the resulting amplitudes and probabilities are defined."
        ),
    },
    "states": {
        "why": (
            "{title} specifies the object from which quantum probabilities are calculated. A Hamiltonian or an "
            "observable does not make a prediction by itself; it must act on a normalized state vector, density "
            "operator, or statistical sector that records the preparation."
        ),
        "reading": (
            "Normalization guarantees that the probabilities sum to one, while positivity prevents negative "
            "probabilities. Pure vectors and density operators are not competing theories: the density-operator "
            "form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out."
        ),
        "connection": (
            "The Hamiltonian or channel evolves the prepared state. An observable and measurement map then convert that evolved state into outcome probabilities."
        ),
    },
    "generators": {
        "why": (
            "{title} separates quantum kinematics from dynamics. The state space lists what can exist, whereas a "
            "Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale."
        ),
        "reading": (
            "The evolution law transports a state without redefining it. Closed-system evolution is unitary; effective open-system evolution must preserve trace and "
            "positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes."
        ),
        "connection": (
            "The evolved state becomes experimentally meaningful through an observable whose spectrum and expectation values expose the consequences of the dynamics."
        ),
    },
    "observables": {
        "why": (
            "{title} states which physical question is being asked. The same state supports many incompatible questions, "
            "so a prediction requires an operator, spectral measure, or effect family in addition to the state itself."
        ),
        "reading": (
            "The operator's spectrum lists possible sharp values, while the state determines their weights. Matrix entries "
            "depend on basis, but the spectrum, expectation values, and probability distribution are unchanged by an "
            "equivalent representation. Domain and self-adjointness conditions are part of the physical definition."
        ),
        "connection": (
            "An observable defines possible outcomes. The measurement chapter adds the probability rule and, when needed, "
            "the physical interaction that records one of those outcomes."
        ),
    },
    "measurement": {
        "why": (
            "{title} connects the formal state and observable to experimental frequencies. It distinguishes the probability "
            "assigned to an outcome from the conditional state change that may follow a recorded event."
        ),
        "reading": (
            "Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized "
            "probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum "
            "instrument, whose maps describe both the outcome probability and the corresponding post-measurement state."
        ),
        "connection": (
            "Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty "
            "relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment."
        ),
    },
    "incompatibility": {
        "why": (
            "{title} is needed because individually valid observables need not admit a common set of definite values. Quantum "
            "theory therefore requires a separate compatibility analysis rather than treating every collection of questions as classical."
        ),
        "reading": (
            "A nonzero commutator obstructs a common eigenbasis for the corresponding sharp observables. Uncertainty, contextuality, "
            "and Bell inequalities express related obstructions under different assumptions. The assumptions must be stated because "
            "the mathematical conclusion changes when the measurement context or factorization changes."
        ),
        "connection": (
            "Compatibility limits are then carried into concrete realizations. Boundaries, interfaces, and tensor factorizations decide "
            "which observables and correlations can actually be prepared and compared."
        ),
    },
    "boundaries": {
        "why": (
            "{title} makes the operator domain physical. The same differential expression can have different spectra, resonances, "
            "and scattering channels when its boundary conditions, potential, or asymptotic states are changed."
        ),
        "reading": (
            "The eigenvalue or scattering equation must be read together with its domain and matching conditions. Confinement selects "
            "discrete modes; open channels produce transmission, reflection, and resonances. Removing the boundary should recover the "
            "appropriate free or infinite-domain limit."
        ),
        "connection": (
            "Boundary-shaped single-particle mechanisms extend naturally to many modes and fields. The field-theory chapter replaces a "
            "fixed particle number with occupation sectors, local fields, and symmetry constraints."
        ),
    },
    "fields": {
        "why": (
            "{title} places quantum dynamics in a relativistic, many-body, field, gauge, geometric, or scale-dependent setting. "
            "The state space and operator domain must therefore be specified for that setting rather than inferred from a single-particle model."
        ),
        "reading": (
            "Different topics in this branch use different carriers: spinor wave functions, Fock spaces, many-body states, gauge sectors, "
            "geometric states, or effective low-energy sectors. Their physical content is fixed by the associated field equation or Hamiltonian, "
            "its constraints and domain, and the amplitudes, spectra, charges, or correlation functions it predicts."
        ),
        "connection": (
            "Field and many-body mechanisms become experimentally useful when assembled into an ordered intervention. The protocol chapter "
            "shows how preparation, controlled evolution, measurement, and correction compose into one executable map."
        ),
    },
    "protocols": {
        "why": (
            "{title} specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available "
            "gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle."
        ),
        "reading": (
            "The ordered composition carries a prepared input to a final state. Every intermediate map must preserve its stated physical conditions, "
            "and conditional operations are tied to explicit measurement outcomes. Performance is quantified "
            "through fidelity, error rate, capacity, precision, or success probability."
        ),
        "connection": (
            "This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the "
            "operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole."
        ),
    },
}


TOPIC_EXPLANATION_OVERRIDES: Dict[str, Dict[str, str]] = {
    "mathematical_formulation_of_quantum_mechanics": {
        "why": (
            "This page is the entrance to the construction because quantum theory separates three objects that classical prose often mixes: "
            "a state encoding preparation, an operator encoding a physical question, and a probability rule connecting the two. The formalism "
            "is useful precisely because each object can change representation without changing the prediction."
        ),
        "reading": (
            "A state vector or density operator carries preparation information; an observable supplies possible values; their pairing gives "
            "probabilities and expectation values. When a unitary map changes basis, the state and observable transform together. Their matrices "
            "change, but every probability remains the same."
        ),
        "example": (
            "A spin-one-half preparation can be written in the vertical basis or the horizontal basis. The two column vectors look different, "
            "and the spin operator has different matrix entries, yet a consistently transformed calculation predicts the same detector counts."
        ),
        "connection": (
            "The Hilbert-space page now specifies the arena in which states, operators, inner products, and unitary transformations are defined."
        ),
    },
    "hilbert_space": {
        "why": (
            "Hilbert space is not merely a container for wave functions. Its inner product defines amplitudes and orthogonality, while the domains "
            "of unbounded operators decide whether expressions for position, momentum, and energy are mathematically and physically admissible."
        ),
        "reading": (
            "The linear structure permits superposition, the inner product converts pairs of states into amplitudes, and completeness guarantees "
            "that convergent sequences of approximations remain inside the space. Operator domains must be carried with the operators; the same "
            "differential formula on another domain can describe a different physical system."
        ),
        "example": (
            "A qubit lives in a two-dimensional complex space, whereas a particle on a line is described in a space of square-integrable functions. "
            "Both obey the same Hilbert-space logic, but their operators, spectra, and boundary conditions are different."
        ),
        "connection": (
            "After the arena is fixed, a quantum state selects one preparation or statistical ensemble within it."
        ),
    },
    "quantum_state": {
        "why": (
            "A quantum state is the minimal object that assigns probabilities to every admissible measurement in a fixed context. It is therefore "
            "defined by its predictive role, not by a preferred wave-function notation."
        ),
        "reading": (
            "A pure state is represented by a ray rather than by a unique vector, because an overall phase changes no probability. More general "
            "preparations are density operators. In either form, the state must be normalized and must yield non-negative probabilities."
        ),
        "example": (
            "Two laboratories may prepare the same polarization statistics by different procedures. If every allowed measurement has the same "
            "probability distribution, quantum theory assigns the same density operator to both preparations."
        ),
        "connection": (
            "The wave-function and density-matrix pages develop the two principal representations of this predictive object."
        ),
    },
    "wave_function": {
        "why": (
            "The wave function is a representation of a state in a chosen continuous basis. Treating it as the state itself can obscure that a "
            "Fourier transform changes its shape while preserving all predictions."
        ),
        "reading": (
            "Its complex value is a probability amplitude. The squared magnitude gives a position density only in the position representation; "
            "phase differences remain essential because they control interference and momentum content. Normalization fixes the total probability."
        ),
        "example": (
            "A localized wave packet and its momentum-space Fourier transform emphasize different features of one preparation. Their forms differ, "
            "but either representation reproduces the same expectation values when the observables are transformed consistently."
        ),
        "connection": (
            "Density operators extend this description to mixtures, subsystems, and open-system dynamics."
        ),
    },
    "density_matrix": {
        "why": (
            "The density matrix is required whenever the preparation is statistical, part of an entangled system is ignored, or environmental "
            "coupling makes a state-vector description of the subsystem incomplete."
        ),
        "reading": (
            "Diagonal elements in a selected basis give populations and off-diagonal elements carry coherence in that basis. Positivity and unit "
            "trace make the Born probabilities legal. Partial tracing produces the state of a subsystem without assigning a pure vector to it."
        ),
        "example": (
            "Either randomly preparing two spin directions or discarding one member of an entangled pair can produce a mixed state. The density "
            "matrix records the observable statistics, even though the physical origins of the mixture differ."
        ),
        "connection": (
            "With the state representation established, unitary and non-unitary maps specify how it changes."
        ),
    },
    "quantum_decoherence": {
        "why": (
            "Interference is lost when alternative system amplitudes become correlated with environmental states that can, even in principle, distinguish them. The missing coherence has then moved into correlations of the larger state rather than being erased by the subsystem equation alone."
        ),
        "reading": (
            "Unitary system-environment evolution can suppress the off-diagonal elements of the reduced density matrix after the environment is traced out. The overlap of the corresponding environmental states fixes the remaining visibility. Decoherence can be Markovian; memory requires the stronger condition that hidden correlations later alter evolution from the same reduced state."
        ),
        "example": (
            "In a two-path interferometer, scattering one distinguishable environmental state from each path lowers the fringe visibility in proportion to their overlap. Erasing the distinguishing record can restore interference in suitable conditional measurements."
        ),
        "connection": (
            "The distinction between lost visibility and returning correlations leads directly to quantum channels, non-Markovian dynamics, and the composition test for memory."
        ),
    },
    "unitary_operator": {
        "why": (
            "Unitary operators express reversible quantum change and changes of representation with one mathematical condition: preservation of "
            "the inner product. That condition preserves normalization, orthogonality, and transition probabilities."
        ),
        "reading": (
            "Applying a unitary map to a state rotates it within Hilbert space without losing information. Conjugating an observable by the same map "
            "gives the equivalent description in the transformed representation. Continuous unitary evolution is generated by a self-adjoint operator."
        ),
        "example": (
            "A spin rotation changes the amplitudes assigned to vertical and horizontal outcomes, but a second inverse rotation restores the original "
            "state exactly. Decoherence cannot be represented by such a unitary map on the subsystem alone."
        ),
        "connection": (
            "The Hamiltonian page identifies the generator that produces unitary time evolution."
        ),
    },
    "hamiltonian_quantum_mechanics": {
        "why": (
            "The Hamiltonian specifies both the energy observable and, for a closed system, the generator of time translation. These roles coincide "
            "but should not be confused: one concerns possible energy values, the other the path followed by every prepared state."
        ),
        "reading": (
            "Exponentiating a self-adjoint Hamiltonian produces the unitary propagator. Its eigenvectors acquire phases at rates set by their energies; "
            "relative phases then produce interference and motion. Time dependence or external driving requires a time-ordered propagator."
        ),
        "example": (
            "For a particle in a static potential, kinetic and potential terms determine both stationary energy levels and the evolution of a wave "
            "packet assembled from those levels."
        ),
        "connection": (
            "The Schrodinger equation gives the differential form of this evolution, while path integrals and the Heisenberg picture reorganize the same predictions."
        ),
    },
    "schr_dinger_equation": {
        "why": (
            "The Schrodinger equation turns a Hamiltonian into a local rule for the time dependence of a state. It is the point at which the chosen "
            "state space, boundary conditions, and interaction model become a calculable prediction."
        ),
        "reading": (
            "The time derivative of the state is fixed by the Hamiltonian acting on that state. For a self-adjoint Hamiltonian, the equation preserves "
            "norm. Stationary solutions separate time dependence from the spatial eigenvalue problem, but a general preparation is their superposition."
        ),
        "example": (
            "A wave packet in a potential well spreads and interferes according to the same equation whose stationary solutions define the well's energy levels."
        ),
        "connection": (
            "Observables determine which consequences of the evolved state are compared with experiment."
        ),
    },
    "observable": {
        "why": (
            "An observable converts a broad physical question such as position, energy, or spin into an operator with a defined domain and spectrum. "
            "Without that operator, the state alone does not specify which distribution is being predicted."
        ),
        "reading": (
            "The spectral measure decomposes the observable into possible outcome sectors. Pairing those sectors with the state gives probabilities, "
            "and weighting them by their spectral values gives expectation values. Degenerate eigenspaces correspond to outcomes that do not resolve every state component."
        ),
        "example": (
            "A spin state has different probability distributions for measurements along different axes. The preparation is unchanged; the observable selects the question."
        ),
        "connection": (
            "The Born rule supplies the probability assigned to each spectral sector, and measurement theory describes its physical registration."
        ),
    },
    "born_rule": {
        "why": (
            "The Born rule is the bridge from complex amplitudes to experimentally testable probabilities. It is an additional postulate: linear state "
            "evolution alone does not say how often a detector outcome should occur."
        ),
        "reading": (
            "For a sharp measurement, the probability of an outcome is the state weight in the corresponding eigenspace. The density-operator form "
            "extends the same rule to mixtures and generalized measurements. Completeness of the outcome operators makes the probabilities sum to one."
        ),
        "example": (
            "A spin prepared equally between two vertical outcomes gives one-half for each vertical detector channel, even though each individual run records only one result."
        ),
        "connection": (
            "Measurement theory adds detector coupling and conditional state change without altering this probability assignment."
        ),
    },
    "measurement_in_quantum_mechanics": {
        "why": (
            "Measurement theory must describe both an outcome distribution and the physical operation that produces a record. Keeping these roles separate "
            "prevents an interpretive account of state change from being mistaken for the probability law itself."
        ),
        "reading": (
            "A POVM gives outcome probabilities, whereas a quantum instrument gives the corresponding conditional transformations. Projective measurement "
            "is an ideal sharp limit. Real detectors are calibrated by showing that their effects are positive, complete, and consistent with observed frequencies."
        ),
        "example": (
            "A photon counter may report click or no click with non-unit efficiency. A two-effect POVM models those probabilities; the associated instrument "
            "is needed only when the state after the event matters."
        ),
        "connection": (
            "The incompatibility chapter asks which families of such measurements can be jointly realized or assigned simultaneous sharp values."
        ),
    },
    "commutator": {
        "why": (
            "The commutator measures whether the order of two transformations matters. For observables it also tests whether a common eigenbasis, and hence a "
            "joint sharp description, can exist."
        ),
        "reading": (
            "A zero commutator is a compatibility condition under the stated domains; a nonzero commutator identifies an algebraic obstruction. The value can "
            "also generate symmetry transformations, so the same operation links compatibility, dynamics, and conservation."
        ),
        "example": (
            "Position followed by momentum is not the same operation as momentum followed by position. Their canonical commutator fixes the lower bound in the corresponding uncertainty relation."
        ),
        "connection": (
            "The uncertainty-principle page converts this algebraic obstruction into a state-dependent bound on simultaneous dispersion."
        ),
    },
    "uncertainty_principle": {
        "why": (
            "The uncertainty principle states a quantitative consequence of incompatibility. It is not a claim about poor apparatus: it constrains the spreads "
            "of outcome distributions for every state in the relevant operator domains."
        ),
        "reading": (
            "The lower bound depends on the expectation value of the commutator and can be strengthened by covariance terms. A small spread in one observable "
            "therefore requires a compensating spread in its incompatible partner for the same prepared state."
        ),
        "example": (
            "Narrowing a particle's position wave packet broadens its momentum distribution because the two amplitudes are Fourier transforms, not because the momentum detector disturbs a pre-existing sharp value."
        ),
        "connection": (
            "Multipartite correlations generalize incompatibility beyond pairs of observables and lead to entanglement and Bell tests."
        ),
    },
    "quantum_entanglement": {
        "why": (
            "Entanglement is required when the state of a composite system cannot be assembled from independent states of its parts. It changes which "
            "correlations are possible and makes subsystem states mixed even when the total state is pure."
        ),
        "reading": (
            "The tensor-product structure defines the proposed subsystems. A state is entangled when it is not separable across that factorization. Partial "
            "traces describe each part, while joint observables expose correlations that no product state can reproduce."
        ),
        "example": (
            "In a Bell pair, each spin alone is maximally mixed, yet measurements on the pair are strongly correlated. The information resides in the relation between subsystems rather than in either local state."
        ),
        "connection": (
            "Bell's theorem and contextuality determine which entangled correlations are incompatible with classical joint assignments."
        ),
    },
    "particle_in_a_box": {
        "why": (
            "The particle in a box shows in the simplest form that a boundary condition is part of the Hamiltonian's physical definition. Confinement turns a "
            "continuous free-particle spectrum into discrete allowed energies."
        ),
        "reading": (
            "The wave function satisfies the same differential equation inside the box as a free particle, but vanishing boundary values select standing waves. "
            "Only wavelengths fitting the interval are admissible, and their curvature fixes the quantized energies."
        ),
        "example": (
            "Doubling the box length reduces every level spacing by a factor of four. This follows from the boundary-selected wavelength and provides a direct check of the construction."
        ),
        "connection": (
            "Replacing an impenetrable wall by a finite barrier leads to tunnelling, resonances, and scattering channels."
        ),
    },
    "quantum_tunnelling": {
        "why": (
            "Quantum tunnelling tests the consequence of wave evolution across a classically forbidden region. The effect depends jointly on the generator, "
            "barrier geometry, matching conditions, and incident state."
        ),
        "reading": (
            "Inside the barrier the stationary wave function is evanescent rather than oscillatory. Continuity and flux conditions connect it to incoming and "
            "outgoing waves, producing a nonzero transmission amplitude that falls approximately exponentially with barrier width in the semiclassical regime."
        ),
        "example": (
            "Changing the barrier width while holding its height and the incident energy fixed isolates the predicted exponential dependence and separates tunnelling from an over-barrier contribution."
        ),
        "connection": (
            "Scattering theory generalizes the same matching construction to many incoming, outgoing, and resonant channels."
        ),
    },
    "fermion": {
        "why": (
            "A many-particle Hilbert space does not specify how identical particles are exchanged. Choosing the antisymmetric representation removes coincidence states and changes the spectrum, pressure, correlations, and admissible collective phases before a particular interaction Hamiltonian is chosen."
        ),
        "reading": (
            "The minus sign acquired under exchange makes every Slater determinant vanish when two columns coincide. In occupation language the same restriction is encoded by anticommutation and by eigenvalues zero or one of each mode-number operator. These are equivalent descriptions of one state-space constraint."
        ),
        "example": (
            "A zero-temperature ideal Fermi gas fills all momentum modes up to the Fermi momentum. Compressing the gas therefore forces particles into higher-momentum states and raises its pressure even when the interaction potential is set to zero."
        ),
        "connection": (
            "Fermi--Dirac statistics adds thermal occupation to this exchange-constrained state space. Pairing, bosonization and Jordan--Wigner transformations then test which consequences of fermionic algebra survive on a different carrier."
        ),
    },
    "fermi_dirac_statistics": {
        "why": (
            "Fermi-Dirac statistics is needed because identical fermions do not occupy many-particle states independently. Antisymmetry under particle exchange, "
            "and the exclusion principle that follows from it, changes the allowed occupation patterns before any Hamiltonian dynamics is considered."
        ),
        "reading": (
            "Single-particle energy levels provide the available modes, while each mode can be occupied at most once per internal state. The Fermi-Dirac distribution "
            "gives the mean occupation at thermal equilibrium. At zero temperature it fills modes up to the Fermi energy."
        ),
        "example": (
            "The degeneracy pressure of an electron gas follows from filling successively higher momentum states even without a repulsive force between the electrons. "
            "The effect is a consequence of antisymmetric state construction."
        ),
        "connection": (
            "Bose-Einstein statistics changes the exchange rule from antisymmetric to symmetric and therefore permits unlimited occupation of one mode."
        ),
    },
    "bose_einstein_statistics": {
        "why": (
            "Bose-Einstein statistics is needed because identical bosons occupy symmetric many-particle states. Multiple particles may share one mode, which produces "
            "collective occupation effects absent from distinguishable particles and fermions."
        ),
        "reading": (
            "The Bose-Einstein distribution gives the mean occupation of each energy mode at thermal equilibrium. The chemical potential and density determine whether "
            "a macroscopic population accumulates in the lowest mode, as in Bose-Einstein condensation."
        ),
        "example": (
            "Cooling a dilute bosonic gas below its critical temperature transfers a macroscopic fraction of the atoms into one quantum mode. The condensate is not "
            "caused by an attractive binding force; it follows from the symmetric occupation rule and thermodynamic constraints."
        ),
        "connection": (
            "Fock space provides one common language for bosonic and fermionic occupations, while field operators create and remove individual mode excitations."
        ),
    },
    "quantum_field_theory": {
        "why": (
            "Quantum field theory is needed when relativity, locality, and particle creation must be described together. Fields become the primary operator-valued objects, while particles appear as excitations of their modes."
        ),
        "reading": (
            "The state lives in a many-particle or field space, local operators create correlations, and the action or Hamiltonian generates their evolution. "
            "Perturbative amplitudes are expansions of these operator relations, not independent pictorial rules."
        ),
        "example": (
            "A photon is represented as an excitation of the electromagnetic field. Processes that change photon number are natural in Fock space but cannot be represented in a fixed one-particle Hilbert space."
        ),
        "connection": (
            "Gauge theory identifies redundant field descriptions, and renormalization connects parameters measured at different scales."
        ),
    },
    "gauge_theory": {
        "why": (
            "Gauge theory separates physical states from multiple mathematical descriptions related by local transformations. The redundancy is useful because "
            "it makes locality and interaction structure explicit, but constraints are required to remove unphysical degrees of freedom."
        ),
        "reading": (
            "Gauge-related field configurations represent the same physical state. Observable quantities must therefore be gauge invariant, or transform covariantly "
            "within a construction whose final predictions are invariant. Gauge fixing chooses one representative without changing the physical equivalence class."
        ),
        "example": (
            "Changing the electromagnetic scalar and vector potentials by a gauge transformation changes their formulas but leaves electric and magnetic fields, phase-consistent amplitudes, and measured forces unchanged."
        ),
        "connection": (
            "Renormalization adds a second kind of transformation: changing the scale at which the same theory is parametrized."
        ),
    },
    "renormalization": {
        "why": (
            "Renormalization explains how a theory preserves predictions while its effective parameters and degrees of freedom change with scale. It is therefore "
            "a transformation between descriptions, not merely a device for removing infinities."
        ),
        "reading": (
            "A change of scale moves the couplings along a flow. Predictions remain fixed when explicit scale dependence and coupling dependence compensate. Fixed "
            "points and relevant directions then organize universality across microscopically different systems."
        ),
        "example": (
            "Different lattice models can approach the same critical exponents because coarse-graining removes microscopic details while preserving the long-distance transformation structure."
        ),
        "connection": (
            "Effective field theory uses this scale organization to decide which operators must be retained for a specified accuracy."
        ),
    },
    "quantum_channel": {
        "why": (
            "A quantum channel is the general transformation available to a state when an environment, uncontrolled degree of freedom, or measurement outcome is not retained. "
            "It extends unitary dynamics without abandoning positivity or probability conservation."
        ),
        "reading": (
            "Complete positivity guarantees that the map remains physical when the input is entangled with an untouched system, and trace preservation guarantees total probability. "
            "A Kraus representation displays one realization, but different Kraus sets can describe the same channel."
        ),
        "example": (
            "Loss of phase coherence can be represented by a dephasing channel. Its action suppresses off-diagonal density-matrix elements while leaving the corresponding populations unchanged."
        ),
        "connection": (
            "Quantum error correction asks whether information can be encoded so that a specified family of channels is detectable and reversible on the code space."
        ),
    },
    "quantum_error_correction": {
        "why": (
            "Quantum error correction protects a subspace against a family of noise operations without learning the encoded amplitudes. It is a mechanism design problem involving encoding, error syndromes, conditional correction, and a final logical observable."
        ),
        "reading": (
            "The error-correction conditions require different errors either to act identically on the code space or to move it into distinguishable syndrome sectors. A recovery map then restores the logical state while preserving superpositions."
        ),
        "example": (
            "A repetition-style code can diagnose one class of flips by comparing parity checks. The syndrome identifies the error location without measuring the unknown logical amplitudes themselves."
        ),
        "connection": (
            "Fault-tolerant protocols extend this logic by constraining how errors propagate through an entire sequence of gates and measurements."
        ),
    },
}

BRANCH_MECHANISM_FRAMES: Dict[str, Dict[str, str]] = {
    "context": {
        "carrier": "A Hilbert, Fock, or function space together with the operator domains and representation used in the calculation.",
        "operator": "A unitary or isometric change of basis, Fourier transform, coordinate map, or representation equivalence.",
        "admissibility": "Inner products, domains, normalization, and completeness relations must be preserved by a purely representational change.",
        "readout": "Transition amplitudes, expectation values, spectra, and probabilities that remain invariant under an admissible representation change.",
        "test": "Calculate the same amplitude, expectation value, or spectrum in both representations and verify equality within the stated domain.",
    },
    "states": {
        "carrier": "A state vector, wave function, density operator, field state, register state, or superselection sector.",
        "operator": "The transformations and observables defined on that state space.",
        "admissibility": "Normalization, positivity, inner-product, tensor-factorization, and superselection conditions define the allowed states.",
        "readout": "Born probabilities, expectation values, reduced states, or correlation functions determined by the state.",
        "test": "Equivalent state representations must give the same probabilities and expectation values for corresponding observables.",
    },
    "generators": {
        "carrier": "A state vector, density operator, wave function, field state, or register on a specified domain.",
        "operator": "A Hamiltonian, action, Liouvillian, channel generator, or differential operator that transports the state.",
        "admissibility": "Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary conditions determine whether the evolution is legal.",
        "readout": "Time-dependent probabilities, transition amplitudes, response functions, conserved quantities, or spectra implied by the dynamics.",
        "test": "The generated evolution must preserve the stated normalization, positivity, symmetry, or conservation condition and recover the appropriate limiting dynamics.",
    },
    "observables": {
        "carrier": "An admissible quantum state space on which the physical quantity is represented.",
        "operator": "A self-adjoint operator, operator-valued measure, or algebra element representing the physical question.",
        "admissibility": "Domain, self-adjointness, gauge invariance, and spectral conditions determine whether the quantity is a physical observable.",
        "readout": "Eigenvalues, spectral measures, expectation values, moments, and response functions associated with the observable.",
        "test": "The operator must yield real, normalized predictions and transform consistently under changes of representation or symmetry.",
    },
    "measurement": {
        "carrier": "A prepared state together with the measurement context and any apparatus degrees of freedom retained in the model.",
        "operator": "A projection-valued measure, POVM, quantum instrument, or detector interaction.",
        "admissibility": "Outcome probabilities are positive and normalized; conditional state changes must define completely positive maps.",
        "readout": "Outcome probabilities, detector records, ensemble frequencies, and conditional post-measurement states.",
        "test": "The probability and update rules must reproduce calibration data and remain distinct from interpretive claims that do not change predictions.",
    },
    "incompatibility": {
        "carrier": "One state space or a multipartite state space on which several observables or contexts are defined.",
        "operator": "Commutators, correlation operators, joint measurements, or hidden-variable assignments under comparison.",
        "admissibility": "Uncertainty relations, contextuality constraints, and Bell-type inequalities restrict possible joint assignments.",
        "readout": "Joint spectra, uncertainty products, correlation functions, and inequality violations.",
        "test": "Show that no single sharp assignment reproduces the observed or calculated statistics under the stated compatibility assumptions.",
    },
    "boundaries": {
        "carrier": "A state space equipped with a domain, potential, interface, cavity, or asymptotic channel.",
        "operator": "A Hamiltonian, wave operator, transfer operator, or scattering map whose domain depends on the boundary data.",
        "admissibility": "Boundary and matching conditions determine the allowed modes, resonances, and conserved fluxes.",
        "readout": "Energy levels, resonances, transmission and reflection amplitudes, phase shifts, or scattering cross-sections.",
        "test": "Vary the boundary and verify the predicted spectral or scattering change while recovering the free or asymptotic limit when it is removed.",
    },
    "fields": {
        "carrier": "A Fock space, field configuration space, gauge sector, many-body Hilbert space, or effective low-energy sector.",
        "operator": "Field, creation, annihilation, charge, Hamiltonian, constraint, or renormalization operators.",
        "admissibility": "Statistics, locality, gauge symmetry, domain conditions, and renormalization prescriptions determine the physical sector.",
        "readout": "Correlation functions, particle spectra, charges, scattering amplitudes, effective couplings, or geometric observables.",
        "test": "The construction must preserve the relevant symmetries and recover the expected particle, quasiparticle, classical, or low-energy limit where it exists.",
    },
    "protocols": {
        "carrier": "An input state, register, encoded subspace, channel state, key, syndrome, or controlled experimental configuration.",
        "operator": "An ordered sequence of gates, channels, measurements, encodings, corrections, or feedback maps.",
        "admissibility": "Each step must belong to the claimed map class and the composition must preserve normalization and positivity.",
        "readout": "Output state, fidelity, error rate, key rate, channel capacity, algorithmic success probability, or sensor estimate.",
        "test": "Change the operation order or replace a quantum step with a matched control to identify which transformation carries the effect.",
    },
}

BRANCH_ROLE_EQUATIONS: Dict[str, str] = {
    "context": r"V:\mathcal H\to\mathcal H',\quad V^\dagger V=I,\quad \rho'=V\rho V^\dagger,\quad O'=VOV^\dagger",
    "states": r"\ket\psi\in\mathcal H,\quad \rho\ge0,\quad \operatorname{Tr}\rho=1,\quad p_i=\operatorname{Tr}(\rho P_i)",
    "generators": r"i\hbar\,\partial_t\rho=[H,\rho],\quad U(t)=e^{-iHt/\hbar},\quad \rho(t)=U(t)\rho(0)U^\dagger(t)",
    "observables": r"O=\int_{\sigma(O)}\lambda\,dE_O(\lambda),\quad \langle O\rangle_\rho=\operatorname{Tr}(\rho O)",
    "measurement": r"p(y)=\operatorname{Tr}(\rho E_y),\quad E_y\ge0,\quad \sum_yE_y=I",
    "incompatibility": r"[A,B]\ne0,\quad \Delta A\,\Delta B\ge\frac12|\langle[A,B]\rangle|",
    "boundaries": r"H_B\psi=E\psi,\quad \psi\in\mathcal D(H_B),\quad S:\mathcal H_{\rm in}\to\mathcal H_{\rm out}",
    "fields": r"\mathcal F_\pm(\mathcal H),\quad a_k^\dagger,a_k,\quad N_k=a_k^\dagger a_k,\quad \langle\Phi(x_1)\cdots\Phi(x_n)\rangle",
    "protocols": r"\rho_{\rm out}=\mathcal E_n\circ\cdots\circ\mathcal E_1(\rho_{\rm in}),\quad \mathcal E(\rho)=\sum_aK_a\rho K_a^\dagger",
}


def first_sentence(value: Any, limit: int = 420) -> str:
    text = clean_text(value, limit)
    if not text:
        return ""
    match = re.search(r"(.+?[.!?])(?:\s|$)", text)
    return match.group(1).strip() if match else text


def topic_context_text(page: Mapping[str, Any], limit: int = 900) -> str:
    """Exclude the historical Wikipedia scaffold from the public theory book."""
    return ""


def topic_source_url(page: Mapping[str, Any]) -> str:
    return ""


def terms_text(values: Any, fallback: str = "not specified in the page artifact") -> str:
    if isinstance(values, str):
        terms = [values]
    else:
        terms = [str(item) for item in (values or []) if str(item).strip()]
    if not terms:
        return fallback
    if len(terms) == 1:
        return terms[0]
    if len(terms) == 2:
        return f"{terms[0]} and {terms[1]}"
    return ", ".join(terms[:-1]) + f", or {terms[-1]}"


def page_native_constructor_available(mw: Mapping[str, Any]) -> bool:
    return bool(
        mw.get("mathematical_skeleton_is_source_backed")
        or mw.get("mathematical_skeleton_is_topic_native")
    )


def page_native_mechanism_frame_rows(
    title: str,
    branch_id: str,
    row: Mapping[str, Any],
    mw: Mapping[str, Any],
) -> Optional[List[tuple[str, str]]]:
    if not page_native_constructor_available(mw):
        return None
    grammar = mw.get("grammar") or {}
    missing = [public_book_text(item) for item in (mw.get("missing_experiments") or []) if clean_text(item)]
    claim_boundary = public_book_text(mw.get("claim_boundary"))
    display = page_display_name(title)
    role = "topic-native constructor role"
    family_key = topic_family(str(row.get("slug") or ""), title)
    if family_key != "general_quantum":
        role = FAMILY_NATIVE_LANGUAGE[family_key]["role"]
    carrier_terms = terms_text(grammar.get("state"))
    boundary_terms = terms_text(grammar.get("boundary"))
    operator_terms = terms_text(grammar.get("operator"))
    protocol_terms = terms_text(grammar.get("protocol"))
    spectrum_terms = terms_text(grammar.get("spectrum"))
    compatibility_terms = terms_text(grammar.get("incompatibility"))
    check = missing[0] if missing else claim_boundary
    if not check:
        check = "The page assignment remains a constructor hypothesis until checked against source equations and controls."
    return [
        ("Role", f"{display} contributes {indefinite_article(role)} {role} to the quantum construction."),
        ("Placement", BRANCH_FRAME_FOCUS.get(branch_id, BRANCH_FRAME_FOCUS["annotations"])),
        ("Carrier or domain", f"State terms: {carrier_terms}. Context/domain terms: {boundary_terms}."),
        ("Operator or map", f"Operator terms: {operator_terms}. Protocol or update terms: {protocol_terms}."),
        ("Admissibility", f"Compatibility or closure terms: {compatibility_terms}. These determine which questions, states, or updates are legal."),
        ("Observable or prediction", f"Observable terms: {spectrum_terms}. These name the outcome labels, projectors, amplitudes, or records used for testing."),
        ("Check", check),
    ]


def mechanism_frame_for_page(slug: str, title: str, branch_id: str) -> Dict[str, str]:
    override = TOPIC_FRAME_OVERRIDES.get(slug)
    if override:
        return override
    family_key = topic_family(slug, title)
    if family_key != "general_quantum":
        return FAMILY_MECHANISM_FRAMES[family_key]
    return BRANCH_MECHANISM_FRAMES.get(branch_id, FAMILY_MECHANISM_FRAMES["general_quantum"])


def role_equation_for_page(slug: str, title: str, branch_id: str) -> str:
    family_key = topic_family(slug, title)
    if family_key != "general_quantum":
        return FAMILY_NATIVE_LANGUAGE[family_key]["equation"]
    return BRANCH_ROLE_EQUATIONS.get(branch_id, FAMILY_NATIVE_LANGUAGE["general_quantum"]["equation"])


def quantum_mechanism_frame_rows(
    title: str,
    branch_id: str,
    row: Mapping[str, Any],
    mw: Optional[Mapping[str, Any]] = None,
) -> List[tuple[str, str]]:
    """Return a public quantum-language mechanism frame for a page.

    This is the public translation of the internal mechanism grammar.  It uses
    ordinary quantum vocabulary only; codebook names and internal coordinate
    symbols are intentionally not emitted into the book.
    """
    slug = str(row.get("slug") or "")
    if slug not in TOPIC_CONSTRUCTOR_OVERRIDES and page_native_constructor_available(mw or {}):
        native = page_native_mechanism_frame_rows(title, branch_id, row, mw or {})
        if native:
            return native
    family_key = topic_family(slug, title)
    family = FAMILY_NATIVE_LANGUAGE[family_key]
    role = (
        BRANCH_PUBLIC_ROLE.get(branch_id, "formal role")
        if family_key == "general_quantum"
        else family["role"]
    )
    frame = mechanism_frame_for_page(slug, title, branch_id)
    role = frame.get("role", role)
    return [
        ("Role", f"{page_display_name(title)} contributes {indefinite_article(role)} {role} to the quantum construction."),
        ("Placement", BRANCH_FRAME_FOCUS.get(branch_id, BRANCH_FRAME_FOCUS["annotations"])),
        ("Carrier or domain", frame["carrier"]),
        ("Operator or map", frame["operator"]),
        ("Admissibility", frame["admissibility"]),
        ("Observable or prediction", frame["readout"]),
        ("Check", frame["test"]),
    ]


def physical_construction_prose(
    title: str,
    branch_id: str,
    row: Mapping[str, Any],
    mw: Mapping[str, Any],
) -> str:
    """State the four physical elements of a topic as connected prose."""
    frame = dict(quantum_mechanism_frame_rows(title, branch_id, row, mw))

    def fragment(value: str) -> str:
        text = clean_text(value, 1200).rstrip(" .")
        for prefix in ("A ", "An ", "The "):
            if text.startswith(prefix):
                return prefix.lower() + text[len(prefix) :]
        return text

    admissibility = clean_text(frame.get("Admissibility", ""), 1200).rstrip(" .")
    return " ".join(
        [
            f"The state carrier is {fragment(frame.get('Carrier or domain', ''))}.",
            f"The governing operation is {fragment(frame.get('Operator or map', ''))}.",
            admissibility + ".",
            f"The calculated observables are {fragment(frame.get('Observable or prediction', ''))}.",
        ]
    )


def topic_explanation_for_page(slug: str, title: str, branch_id: str) -> Dict[str, str]:
    """Return connected prose that explains a topic's necessity and use.

    Topic-specific explanations take precedence. Branch prose supplies a
    physically meaningful fallback for the remaining pages, so the public book
    does not collapse into a repeated field schema.
    """
    branch = BRANCH_EXPLANATIONS.get(branch_id, BRANCH_EXPLANATIONS["context"])
    override = TOPIC_EXPLANATION_OVERRIDES.get(slug, {})
    display = page_display_name(title)
    result: Dict[str, str] = {}
    for key in ("why", "reading", "example", "connection"):
        text = override.get(key) or branch.get(key) or ""
        result[key] = clean_text(text.format(title=display), 1800)
    return result


def prose_from_items(values: Sequence[str], maximum: int = 4) -> str:
    """Join short evidence statements into readable prose without changing claims."""
    sentences: List[str] = []
    for value in list(values)[:maximum]:
        sentence = clean_text(value, 520).strip()
        if not sentence:
            continue
        for index, character in enumerate(sentence):
            if character.isalpha():
                sentence = sentence[:index] + character.upper() + sentence[index + 1 :]
                break
        if sentence[-1] not in ".!?":
            sentence += "."
        sentences.append(sentence)
    return " ".join(sentences)


def consequence_prose_from_items(values: Sequence[str], maximum: int = 3) -> str:
    """Render discriminating consequences as statements rather than instructions."""
    replacements = (
        ("Verify whether ", "The discriminating question is whether "),
        ("Verify that ", "The defining relation requires that "),
        ("Verify ", "The defining relation is "),
        ("Check whether ", "The discriminating question is whether "),
        ("Check that ", "The defining relation requires that "),
        ("Check ", "The relevant comparison is "),
        ("Confirm whether ", "The discriminating question is whether "),
        ("Confirm that ", "The observable consequence requires that "),
        ("Compare ", "A comparison of "),
        ("Recover ", "The theory recovers "),
        ("Measure ", "The measured consequence is "),
        ("Test whether ", "The discriminating question is whether "),
        ("Specify ", "The physical description contains "),
    )
    statements: List[str] = []
    for value in list(values)[:maximum]:
        sentence = clean_text(value, 520).strip()
        if not sentence:
            continue
        for prefix, replacement in replacements:
            if sentence.startswith(prefix):
                sentence = replacement + sentence[len(prefix) :]
                break
        if sentence[-1] not in ".!?":
            sentence += "."
        statements.append(sentence)
    return " ".join(statements)


def equivalence_condition_text(value: str) -> str:
    """Turn a validation prompt into the physical condition for equivalence."""
    sentence = clean_text(value, 900).strip()
    exact = {
        "Check domain and self-adjointness once, then verify separately that the generated dynamics is unitary and that the spectral measure reproduces energy statistics.": (
            "Equivalence requires a common operator domain and self-adjointness; the generated dynamics must be unitary and the spectral measure must reproduce the same energy statistics."
        ),
        "Specify domains, measure, boundary conditions, and regularization; the formulations are connected only where they yield the same amplitudes or correlators.": (
            "Equivalence requires compatible domains, measures, boundary conditions, and regularization; the formulations coincide only where they yield the same amplitudes or correlators."
        ),
        "State the subsystem algebra or tensor factorization explicitly; entanglement and locality claims are not invariant under arbitrary refactorization.": (
            "Equivalence requires a fixed subsystem algebra or tensor factorization because entanglement and locality are not invariant under arbitrary refactorization."
        ),
        "Verify that candidate effects descend to the constrained or quotient state space; gauge-dependent quantities cannot be promoted directly to physical records.": (
            "Physical effects must descend to the constrained or quotient state space; gauge-dependent quantities do not define physical records."
        ),
        "A claimed connection must identify the operator domain and conserved flux; similar-looking wave equations with different domains need not have comparable spectra.": (
            "Equivalence requires the same operator domain and conserved flux; identical differential expressions on different domains can have different spectra."
        ),
        "Check complete positivity, normalization, and recovery fidelity with a reference system; state-update rules alone are insufficient.": (
            "Equivalence requires complete positivity, normalization, and recovery fidelity with a reference system; a state-update rule alone is insufficient."
        ),
        "Validate more than state overlap: compare a generating set of observables or correlators and report the approximation regime and error bounds.": (
            "Equivalence requires agreement of a generating set of observables or correlators within a stated approximation regime and error bound; state overlap alone is insufficient."
        ),
    }
    if sentence in exact:
        return exact[sentence]
    replacements = (
        ("Check that ", "Equivalence requires that "),
        ("Verify that ", "Equivalence requires that "),
        ("Check ", "Equivalence requires "),
        ("Specify ", "Equivalence requires specified "),
        ("State ", "Equivalence requires an explicit statement of "),
        ("Validate more than ", "Equivalence requires more than "),
        ("A claimed connection must ", "Equivalence requires the relation to "),
    )
    for prefix, replacement in replacements:
        if sentence.startswith(prefix):
            sentence = replacement + sentence[len(prefix) :]
            break
    if sentence and sentence[-1] not in ".!?":
        sentence += "."
    return sentence


def rewiring_description_text(value: str) -> str:
    """Express a stored transformation prompt as a declarative physical relation."""
    sentence = clean_text(value, 900).strip()
    exact = {
        "read the same operator through its exponential for transport and through its spectral measure as an energy observable": (
            "The exponential of the Hamiltonian generates time evolution, whereas its spectral measure defines energy probabilities."
        ),
        "move time dependence between states and operators, or replace the propagator by an action-weighted integral": (
            "Time dependence may be carried by states or operators, and the same propagator may be represented by an action-weighted path integral."
        ),
        "change the tensor-product or algebraic subsystem decomposition and track which observables remain local": (
            "Changing the tensor-product or algebraic decomposition changes which observables are local and which states are entangled."
        ),
        "attach gauge or diffeomorphism closure before assigning outcome effects to physical observables": (
            "Gauge or diffeomorphism constraints select the physical state space before outcome operators acquire observable meaning."
        ),
        "change domain, boundary conditions, or asymptotic channels and follow the induced spectrum or transmission map": (
            "The operator domain, boundary conditions, and asymptotic channels determine the spectrum and transmission amplitudes."
        ),
        "retain or discard the classical outcome of a quantum instrument, then condition a recovery channel on that outcome": (
            "A quantum instrument produces both an outcome probability and a conditional state; error correction uses the recorded outcome to select a recovery channel."
        ),
        "encode one carrier in another and require the encoding to intertwine the relevant dynamics and observables": (
            "An encoding represents one state space in another only when it intertwines the relevant dynamics and observables."
        ),
    }
    if sentence in exact:
        return exact[sentence]
    if sentence and sentence[-1] not in ".!?":
        sentence += "."
    return sentence


def quantum_mechanism_frame_block(title: str, branch_id: str, row: Mapping[str, Any], mw: Optional[Mapping[str, Any]] = None) -> str:
    frame = dict(quantum_mechanism_frame_rows(title, branch_id, row, mw))
    lines = [
        r"\subsection*{How It Enters The Theory}",
        rf"\textbf{{Place in the construction.}} {latex_escape(frame.get('Role', ''))} "
        + latex_escape(frame.get("Placement", "")),
        r"\par\smallskip",
        rf"\textbf{{State and operation.}} {latex_escape(frame.get('Carrier or domain', ''))} "
        + latex_escape(frame.get("Operator or map", "")),
        r"\par\smallskip",
        rf"\textbf{{Admissibility and prediction.}} {latex_escape(frame.get('Admissibility', ''))} "
        + latex_escape(frame.get("Observable or prediction", "")),
    ]
    return "\n".join(lines)


def markdown_mechanism_frame(title: str, branch_id: str, row: Mapping[str, Any], mw: Optional[Mapping[str, Any]] = None) -> str:
    frame = dict(quantum_mechanism_frame_rows(title, branch_id, row, mw))
    lines = [
        "## How It Enters The Theory",
        "",
        f"**Place in the construction.** {frame.get('Role', '')} {frame.get('Placement', '')}",
        "",
        f"**State and operation.** {frame.get('Carrier or domain', '')} {frame.get('Operator or map', '')}",
        "",
        f"**Admissibility and prediction.** {frame.get('Admissibility', '')} {frame.get('Observable or prediction', '')}",
        "",
    ]
    return "\n".join(lines)


def latex_escape(value: Any) -> str:
    text = str(value or "")
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    greek = {
        "Α": r"\(A\)",
        "Ω": r"\(\Omega\)",
        "Ξ": r"\(\Xi\)",
        "ρ": r"\(\rho\)",
        "θ": r"\(\theta\)",
        "ψ": r"\(\psi\)",
        "Ψ": r"\(\Psi\)",
        "φ": r"\(\phi\)",
        "Φ": r"\(\Phi\)",
        "λ": r"\(\lambda\)",
        "Λ": r"\(\Lambda\)",
        "π": r"\(\pi\)",
        "Δ": r"\(\Delta\)",
        "⊕": r"\(\oplus\)",
    }
    pieces: List[str] = []
    for ch in text:
        if ch in greek:
            pieces.append(greek[ch])
        else:
            pieces.append(replacements.get(ch, ch))
    return "".join(pieces)


def latex_url(value: Any) -> str:
    text = str(value or "")
    return text.replace("\\", "/").replace("%", "\\%")


def latex_label(value: Any) -> str:
    text = str(value or "item").lower()
    text = re.sub(r"[^a-z0-9:.-]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "item"


def clean_text(value: Any, limit: Optional[int] = None) -> str:
    raw = "".join(ch for ch in str(value or "") if unicodedata.category(ch) != "Cf")
    text = re.sub(r"\s+", " ", raw).strip()
    if limit and len(text) > limit:
        return text[:limit].rsplit(" ", 1)[0].rstrip()
    return public_theory_language(text)


def public_book_text(value: Any, limit: Optional[int] = None) -> str:
    """Sanitize imported analysis text for the public quantum book.

    The build may consume internal analysis artifacts.  This function keeps the
    generated book in ordinary quantum/evidence language.
    """
    text = clean_text(value, limit)
    replacements = {
        "this matches Hyperion geometry ablations and Noether stability": "this matches the current source-equation stability checks",
        "Hyperion geometry ablations and Noether stability": "source-equation stability checks",
        "A09-like kernel/geometry void": "geometry-free operator-kernel gap",
        "A09-like geometry-free kernels": "geometry-free operator kernels",
        "A09-like": "geometry-free",
        "Hyperion": "source-equation",
        "MorphWiki": "source-equation",
        "apparatus-route-fiber": "construction-role",
        "shared quantum constructor": "page-native constructor",
        "366D page-coordinate export": "page-coordinate export",
        "366D": "high-dimensional",
        "but they need explicit topic reruns and typed equations": "They require explicit topic reruns and typed equations",
        "Operationally, ": "",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def is_generic_native_constructor_text(value: str) -> bool:
    """Detect imported constructor text that is too broad for a topic page."""
    lowered = clean_text(value).lower()
    if not lowered:
        return True
    if "read through the compact quantum constructor" in lowered and len(lowered.split()) < 28:
        return True
    if "available language supplies" in lowered and "mechanism should be completed" in lowered:
        return True
    markers = [
        "can be read as a quantum construction",
        "in quantum-mechanical terms",
        "two-dimensional hilbert space",
        "chosen basis, pulse sequence, or measurement axis",
        "spectral projectors with the born rule determine",
        "read through the compact quantum constructor",
        "mechanism should be completed by naming",
        "state terms such as",
        "operator terms such as",
        "spectral terms such as",
        "constructor role",
        "placed by route/fiber evidence",
        "public morphwiki export",
        "complete mechanism names",
    ]
    hits = sum(1 for marker in markers if marker in lowered)
    return hits >= 1


def clean_math_skeleton(value: Any) -> List[str]:
    text = str(value or "").strip()
    if not text:
        return []
    text = text.replace("\x08ig", r"\big")
    text = text.replace(r"\mathrm", r"\operatorname")
    math_replacements = {
        "\u2003": r"\quad ",
        "ρ": r"\rho",
        "λ": r"\lambda",
        "Σ": r"\sum",
        "ℋ": r"\mathcal{H}",
        "∈": r"\in",
        "†": r"^\dagger",
        "≠": r"\neq",
        "⇒": r"\implies",
        "↦": r"\mapsto",
        "₀": r"_0",
        "₁": r"_1",
        "₂": r"_2",
        "ₜ": r"_t",
        "ᵢ": r"_i",
    }
    for old, new in math_replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"(?<![\\A-Za-z])Tr\(", r"\\operatorname{Tr}(", text)
    text = re.sub(r"\\quad\s*\(([^\\{}]+?)\)", r"\\quad \\text{(\1)}", text)
    text = re.sub(r"\\implies\s+([A-Za-z][A-Za-z ]+?)\s+\\quad", r"\\implies \\text{\1} \\quad", text)
    text = text.replace(r"\newline", "\n")
    text = text.replace(r"\[", "").replace(r"\]", "")
    text = re.sub(r"(?<=[)}\]])\\n(?=\s*(?:[A-Z]|\[|\\[A-Za-z]))", "\n", text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    cleaned: List[str] = []
    for line in lines:
        line = re.sub(r"\\\\\s*$", "", line).strip()
        line = line.rstrip(",.;")
        line = line.replace("  ", " ")
        if line and line not in {r"\\", r"\\"}:
            cleaned.append(line)
    return cleaned


def math_skeleton_block(value: Any) -> str:
    lines = clean_math_skeleton(value)
    if not lines:
        return ""
    body = "\\\\\n".join(lines)
    return "\n".join([r"\subsection*{Topic Equations}", r"\begin{centeredalign}", body, r"\end{centeredalign}"])


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_optional_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def page_path(root: Path, slug: str) -> Path:
    return root / "pages" / f"{slug}.json"


def page_title(page: Mapping[str, Any]) -> str:
    return str(page.get("wikipedia", {}).get("title") or page.get("_slug") or "Untitled")


def route_label(top_route: str) -> str:
    return re.sub(r"\s*\([0-9.]+\)$", "", str(top_route or ""))


def lagrangian_road_label(row: Mapping[str, Any]) -> str:
    signal = row.get("lagrangian") or {}
    if signal.get("global_only"):
        return "global atlas prior; page-level action unavailable in this export"
    label = signal.get("road_label") or signal.get("path_class") or "not projected"
    score = signal.get("road_score")
    action = signal.get("action")
    pieces = [str(label)]
    if score is not None:
        try:
            pieces.append(f"road score {float(score):.2f}")
        except (TypeError, ValueError):
            pass
    if action is not None:
        try:
            pieces.append(f"action {float(action):.3f}")
        except (TypeError, ValueError):
            pass
    return "; ".join(pieces)


def top_evidence(
    page: Mapping[str, Any],
    row: Mapping[str, Any] | None = None,
    limit: int = 5,
) -> List[Mapping[str, Any]]:
    """Return only source witnesses confirmed by the transferred V2 index.

    Legacy route matches are useful for retrieval, but they are not page-level
    equation provenance.  The V2 evidence index records the papers and source
    cards that survived source-card alignment.  Restricting public links to
    that overlap prevents a topic model from acquiring unrelated citations.
    """
    v2 = ((row or {}).get("v2_evidence") or {}) if isinstance(row, Mapping) else {}
    if not v2.get("available"):
        return []

    source_examples = [
        example
        for example in (v2.get("source_examples") or [])
        if example.get("source_grounded") is True
    ]
    if not source_examples:
        return []
    confirmed_ids = {
        str(paper_id)
        for example in source_examples
        for paper_id in (example.get("paper_ids") or [])
        if str(paper_id)
    }
    legacy = list(page.get("hyperion", {}).get("equation_witnesses") or [])
    matched = [row for row in legacy if str(row.get("paper_id") or "") in confirmed_ids]

    if len(matched) < limit:
        represented = {str(item.get("paper_id") or "") for item in matched}
        for example in source_examples:
            preview = clean_source_equation(example.get("equation_preview"))
            for paper_id in example.get("paper_ids") or []:
                paper_id = str(paper_id)
                if not paper_id or paper_id in represented:
                    continue
                matched.append(
                    {
                        "paper_id": paper_id,
                        "arxiv_url": f"https://arxiv.org/abs/{paper_id}",
                        "equation_excerpt": preview,
                        "record_id": (example.get("card_ids") or ["source card"])[0],
                        "source_grounded": True,
                    }
                )
                represented.add(paper_id)
                if len(matched) >= limit:
                    break
            if len(matched) >= limit:
                break
    return matched[:limit]


def clean_source_equation(value: Any, limit: int = 520) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    text = text.replace("__HYPERION_SEQ_09A2__", " ")
    text = text.replace("__HYPERION_EQ_SEP__", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rsplit(" ", 1)[0].rstrip()
    return text


def source_equations_block(evidence: Sequence[Mapping[str, Any]], limit: int = 5) -> str:
    rows = []
    for witness in evidence[:limit]:
        equation = clean_source_equation(witness.get("equation_excerpt") or witness.get("equation"))
        if not equation:
            continue
        arxiv = witness.get("paper_id") or ""
        url = witness.get("arxiv_url") or (f"https://arxiv.org/abs/{arxiv}" if arxiv else "")
        score = float(witness.get("score") or 0.0)
        quality = float(witness.get("witness_quality") or 0.0)
        label = f"arXiv:{arxiv}" if arxiv else str(witness.get("record_id") or "source witness")
        link = rf"\href{{{latex_url(url)}}}{{{latex_escape(label)}}}" if url else latex_escape(label)
        rows.extend(
            [
                rf"\item \textbf{{{link}}} (match score {score:.3f}; parser quality {quality:.2f}).",
                r"\begin{quote}\footnotesize\ttfamily " + latex_escape(equation) + r"\end{quote}",
            ]
        )
    if not rows:
        return "\n".join(
            [
                r"\subsection*{Source Equation Witnesses}",
                latex_escape("No clean source-backed equation excerpt is available for this page in the public export."),
            ]
        )
    return "\n".join(
        [
            r"\subsection*{Source Equation Witnesses}",
            latex_escape(
                "The formulas below are parser excerpts from ranked source-equation witnesses, not generated textbook equations."
            ),
            r"\begin{itemize}",
            *rows,
            r"\end{itemize}",
        ]
    )


def list_items(items: Sequence[Any], limit: int = 3) -> str:
    values = [clean_text(item, 260) for item in items if clean_text(item)]
    if not values:
        return r"\emph{Not specified in the public artifact.}"
    lines = []
    for item in values[:limit]:
        lines.append(r"\item " + latex_escape(item))
    return "\n".join(lines)


ROUTE_PUBLIC = {
    "transport_flow_route": "state evolution",
    "constraint_closure_route": "normalization or admissibility",
    "spectral_operator_route": "operator-to-spectrum readout",
    "boundary_weak_form_route": "preparation, basis, or boundary context",
    "commutator_incompatibility_route": "non-commuting compatibility limits",
    "discrete_protocol_route": "controlled update protocol",
}

FIBER_PUBLIC = {
    "structure": "formula structure",
    "spectral": "spectral profile",
    "geometry": "geometric realization",
    "syntax": "local notation",
    "entropy": "information profile",
}

BRANCH_CONSTRUCTOR = {
    "context": {
        "claim": "{title} belongs at the first step of the constructor: it fixes the Hilbert space, operator domain, basis, representation, or preparation context before any probability statement is meaningful.",
        "reading": "The constructor starts by declaring the legal state carrier and the conditions under which states are admissible. In this role, {title} specifies the mathematical setting in which states, operators, spectra, and readout probabilities can be written without ambiguity.",
        "equations": [
            r"B \longmapsto (\mathcal H_B,\mathcal D_B)",
            r"\rho_B \in \mathcal S(\mathcal H_B),\qquad \rho_B\ge 0,\quad \operatorname{Tr}\rho_B=1",
        ],
    },
    "states": {
        "claim": "{title} supplies the carrier of prediction: the object that is propagated, transformed, restricted, or read out.",
        "reading": "At this step the constructor names the predictive carrier, not the final physical story. The carrier may be a state vector, wave function, density operator, field state, or register state. What matters is that later operations can act on it and that probabilities can be computed from it.",
        "equations": [
            r"\ket{\psi}\in\mathcal H,\qquad \rho=\ket{\psi}\bra{\psi}\ \text{or}\ \rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a}",
            r"\rho\ge 0,\qquad \operatorname{Tr}\rho=1",
        ],
    },
    "generators": {
        "claim": "{title} belongs to the lawful-change step: it specifies how the state changes before a question is asked.",
        "reading": "The generator is the part of the construction that makes the state move while preserving the admissibility conditions. In ordinary quantum mechanics this is usually a Hamiltonian or unitary map; in path-integral language it is an action weight over histories.",
        "equations": [
            r"i\hbar\,\partial_t\ket{\psi_t}=H\ket{\psi_t}",
            r"U_t=\exp(-iHt/\hbar),\qquad \rho_t=U_t\rho_0U_t^\dagger",
        ],
    },
    "observables": {
        "claim": "{title} belongs to the question step: it turns a physical question into an operator with admissible answers.",
        "reading": "The constructor separates the state from the question asked of it. A measurable question is represented by an operator; the allowed answers are exposed by its spectral resolution. This is why the operator/spectrum signal is the spine of the quantum tree.",
        "equations": [
            r"O=\sum_i \lambda_i P_i",
            r"P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=I",
        ],
    },
    "measurement": {
        "claim": "{title} belongs to the readout step: it connects a prepared state and an operator spectrum to probabilities or state updates.",
        "reading": "The constructor reads probabilities from the pair consisting of a state and a spectral question. Interpretive pages in this branch assign meaning to probability, state, or update while preserving the formal readout rule.",
        "equations": [
            r"p(i\mid \rho,O)=\operatorname{Tr}(P_i\rho)",
            r"\rho\mapsto \rho_i=\frac{P_i\rho P_i}{\operatorname{Tr}(P_i\rho)}\quad \text{when a projective update is assumed}",
        ],
    },
    "incompatibility": {
        "claim": "{title} belongs to the compatibility step: it marks when two valid questions cannot be jointly sharpened in one basis.",
        "reading": "In this role the constructor describes an algebraic obstruction. If two operators fail to commute, the same state cannot generally supply one common sharp spectral decomposition for both.",
        "equations": [
            r"[A,B]\ne 0",
            r"\Delta_\rho A\,\Delta_\rho B\ge \frac12\left|\operatorname{Tr}(\rho[A,B])\right|",
        ],
    },
    "boundaries": {
        "claim": "{title} belongs to realization: it shows how the abstract state-operator construction becomes legal on a domain, interface, potential, detector geometry, or scattering boundary.",
        "reading": "Boundary realization is where the same operator logic receives a physical presentation. The state space and generator are restricted by a domain, potential, asymptotic condition, interface, or detector arrangement. This is where geometry enters as the realization layer around the invariant operator role.",
        "equations": [
            r"H_B=-\frac{\hbar^2}{2m}\Delta_B+V_B",
            r"\mathcal D(H_B)=\{\psi\in\mathcal H_B:\ C_B\psi=0\}",
        ],
    },
    "fields": {
        "claim": "{title} belongs to the many-mode extension: the same state, generator, observable, and compatibility logic is lifted from one system to fields, particles, scaling limits, or gauge constraints.",
        "reading": "The field layer extends the same constructor to variable numbers of modes and symmetry constraints. Creation and annihilation operators, correlation functions, gauge conditions, and renormalization flows are higher-capacity versions of the same assembly.",
        "equations": [
            r"[a_k,a_l^\dagger]=\delta_{kl}",
            r"\Phi(x)=\sum_k\left(a_k u_k(x)+a_k^\dagger u_k^*(x)\right)",
            r"\frac{dg}{d\log \mu}=\beta(g)",
        ],
    },
    "protocols": {
        "claim": "{title} belongs to the protocol layer: it packages the quantum constructor into engineered sequences of admissible transformations and readouts.",
        "reading": "Protocols are built after the state, operation, and readout rules exist. A circuit, channel, sensor, network, or algorithm is a controlled composition of maps whose output is checked by a final measurement.",
        "equations": [
            r"\rho\mapsto \mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger,\qquad \sum_aK_a^\dagger K_a=I",
            r"p(y)=\operatorname{Tr}(M_y\,\mathcal E(\rho_{\mathrm{in}}))",
        ],
    },
    "annotations": {
        "claim": "{title} is an annotation layer attached to the formal constructor.",
        "reading": "This page changes how the formalism is narrated, interpreted, taught, or historically situated. The underlying assembly remains the same: a context admits states, operators expose spectra, and probability rules connect states to outcomes.",
        "equations": [
            r"\rho,\ O,\ \{P_i\},\ p_i=\operatorname{Tr}(P_i\rho)\quad \text{remain the formal layer}",
            r"\operatorname{meaning}(\rho),\ \operatorname{meaning}(p_i),\ \operatorname{meaning}(\text{update})\quad \text{are reinterpreted}",
        ],
    },
}


TOPIC_CONSTRUCTOR_OVERRIDES = {
    "old_quantum_theory": {
        "claim": (
            "{title} is the semiclassical quantization precursor to modern quantum mechanics: "
            "classical periodic motion is retained, while only selected actions and transition frequencies are admitted."
        ),
        "reading": (
            "Old quantum theory predates the Hilbert-space formalism. Its carrier is classical phase space, "
            "its motion follows Hamiltonian trajectories, and its quantum restriction is imposed on periodic action integrals. "
            "The resulting discrete energies and transition frequencies anticipated quantum spectra but did not provide a general "
            "theory of states, observables, or noncommuting transformations."
        ),
        "equations": [
            r"J_k=\oint p_k\,dq_k=n_k h",
            r"E_m-E_n=h\nu_{mn}",
            r"\frac{\partial E}{\partial J_k}=\nu_k^{\mathrm{cl}}\quad\text{in the correspondence regime}",
        ],
        "equation_note": (
            "Semiclassical constructor: Hamiltonian orbits are restricted by action quantization, and energy differences determine spectral frequencies."
        ),
    },
    "quantum_mechanics": {
        "claim": (
            "{title} is the baseline constructor: states live in Hilbert space, physical questions are represented by operators, and probabilities are assigned to spectral projectors."
        ),
        "reading": (
            "The page supplies the general quantum assembly. A preparation gives a state vector or density operator. "
            "A self-adjoint observable or measurement operator family gives the possible readout channels. "
            "The Born or trace rule assigns probabilities, while Hamiltonian evolution transports the state between preparation and readout."
        ),
        "equations": [
            r"\rho\ge 0,\qquad \operatorname{Tr}\rho=1",
            r"A=\sum_a aP_a,\qquad p(a)=\operatorname{Tr}(\rho P_a)",
            r"\rho(t)=U(t)\rho(0)U(t)^\dagger,\qquad U(t)=e^{-iHt/\hbar}",
            r"[A,B]\ne0\quad\Rightarrow\quad \text{no generic common sharp eigenbasis}",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express state admissibility, spectral readout, unitary evolution, and incompatibility."
        ),
    },
    "photon": {
        "claim": (
            "{title} is a field-mode constructor: a one-quantum excitation of the electromagnetic field, constrained by massless dispersion and transverse polarization."
        ),
        "reading": (
            "The native photon mechanism is field quantization. The electromagnetic field is decomposed into modes, "
            "creation and annihilation operators act on those modes, and a one-photon state is created from the vacuum. "
            "The relevant readouts are occupation number, energy, momentum, polarization, and detector clicks; the constraints are dispersion and gauge-compatible transversality."
        ),
        "equations": [
            r"E=\hbar\omega,\qquad \mathbf p=\hbar\mathbf k,\qquad \omega=c|\mathbf k|",
            r"\ket{1_{\mathbf k,\lambda}}=a_{\mathbf k,\lambda}^{\dagger}\ket{0}",
            r"\hat N_{\mathbf k,\lambda}=a_{\mathbf k,\lambda}^{\dagger}a_{\mathbf k,\lambda}",
            r"\mathbf k\cdot\boldsymbol\epsilon_{\mathbf k,\lambda}=0",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express massless dispersion, one-mode occupation, number readout, and transverse polarization."
        ),
    },
    "electron": {
        "claim": (
            "{title} is a charged spinor constructor: its identity is fixed by mass, charge, spin-1/2 representation, fermionic statistics, and electromagnetic coupling."
        ),
        "reading": (
            "The electron is not a generic object label in this tree. Its native mechanism combines a spinor state, "
            "a Schrödinger/Pauli/Dirac generator depending on regime, conserved charge, and fermionic anticommutation. "
            "The readouts are charge, spin, momentum, energy, and scattering response."
        ),
        "equations": [
            r"(i\hbar\gamma^{\mu}D_{\mu}-mc)\psi=0",
            r"D_{\mu}=\partial_{\mu}+\frac{ie}{\hbar c}A_{\mu}",
            r"\{\psi_{\alpha}(x),\psi_{\beta}^{\dagger}(y)\}=\delta_{\alpha\beta}\delta(x-y)",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express relativistic spinor transport, electromagnetic coupling, and fermionic field statistics."
        ),
    },
    "fermion": {
        "claim": (
            "{title} is an exchange-antisymmetry construction: exchanging two identical fermions reverses the many-body amplitude, so coincident one-particle states are removed from the admissible state space."
        ),
        "reading": (
            "The defining object is the antisymmetric many-body sector, not a particle name. Its nodal set contains every coincidence configuration, and the canonical anticommutation relations preserve that restriction while particles are added or removed. "
            "Filling distinct one-particle modes then produces an exchange hole, a Fermi surface and degeneracy pressure even in the absence of a repulsive potential."
        ),
        "equations": [
            r"\Psi(\ldots,x_i,\ldots,x_j,\ldots)=-\Psi(\ldots,x_j,\ldots,x_i,\ldots),\qquad \Psi(\ldots,x,\ldots,x,\ldots)=0",
            r"\mathcal F_{-}(\mathcal H)=\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H",
            r"\{a_i,a_j^\dagger\}=\delta_{ij},\qquad \{a_i,a_j\}=0",
            r"n_i=a_i^\dagger a_i\in\{0,1\}",
        ],
        "equation_note": (
            "The exchange sign fixes the admissible state space; exterior Fock space and anticommutation extend it to variable particle number."
        ),
        "forced_consequences": [
            "Antisymmetry forces the wave function to vanish when two identical fermions occupy the same one-particle state. The resulting exchange hole is present before a dynamical interaction is specified.",
            "At finite density, distinct momentum states fill up to the Fermi surface. The associated kinetic energy and degeneracy pressure arise from state counting rather than from pairwise repulsion.",
            "Pairing changes the exchange sector: a bound state of two fermions has even fermion parity and can acquire bosonic collective behaviour, as in superconductors and superfluid helium-3.",
        ],
        "transfer_relations": [
            "In one dimension, hard-core bosons and free fermions can share the same density spectrum. The map changes exchange phases and off-diagonal correlations, so equality of energies does not imply identity of all observables.",
            "A Jordan--Wigner map carries local fermionic occupation into spins by adding a parity string. The exchange algebra survives, but locality is transferred into an ordered, generally nonlocal operator.",
            "In two dimensions, exchanges are classified by braids rather than only by permutations. Anyonic statistics therefore extends, rather than merely interpolates between, the boson and fermion constructions.",
        ],
        "scope_conditions": [
            "The relativistic spin--statistics theorem additionally requires locality, positive energy and the relativistic field framework. Antisymmetric lattice or effective quasiparticle models do not by themselves establish that theorem.",
            "Fermi surfaces and degeneracy pressure require a many-mode spectrum and a specified density or particle-number constraint; they do not follow from the word fermion alone.",
        ],
    },
    "boson": {
        "claim": (
            "{title} is an exchange-symmetry constructor: identical bosons live in symmetric sectors and can share the same mode."
        ),
        "reading": (
            "The mechanism is symmetric exchange. Commuting creation and annihilation operators allow arbitrary nonnegative occupation of a mode, "
            "which supports field modes, coherent states, condensates, and photon-like readouts."
        ),
        "equations": [
            r"\mathcal F_{+}(\mathcal H)=\bigoplus_{n=0}^{\infty}\operatorname{Sym}^n\mathcal H",
            r"[a_i,a_j^\dagger]=\delta_{ij},\qquad [a_i,a_j]=0",
            r"n_i=a_i^\dagger a_i\in\{0,1,2,\ldots\}",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express symmetric sectors, commutation, and unrestricted mode occupation."
        ),
    },
    "creation_and_annihilation_operators": {
        "claim": (
            "{title} are sector-changing operators: they add or remove one quantum from a mode and make many-body or field descriptions executable."
        ),
        "reading": (
            "The page is about the algebraic move that changes occupation number. Creation raises the population of a mode, annihilation lowers it, "
            "and the commutation or anticommutation rule determines the statistics. The number operator gives the spectral readout."
        ),
        "equations": [
            r"a_i^\dagger\ket{\ldots,n_i,\ldots}=\sqrt{n_i+1}\ket{\ldots,n_i+1,\ldots}",
            r"a_i\ket{\ldots,n_i,\ldots}=\sqrt{n_i}\ket{\ldots,n_i-1,\ldots}",
            r"N_i=a_i^\dagger a_i",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express raising, lowering, and occupation-number readout."
        ),
    },
    "fock_space": {
        "claim": (
            "{title} is the occupation-number state space: "
            "the construction that replaces a fixed-particle Hilbert space by a direct sum over particle number."
        ),
        "reading": (
            "Fock space changes the carrier of the quantum state. Instead of describing one system in one Hilbert space, "
            "it builds sectors with zero, one, two, and more identical quanta, then imposes the bosonic or fermionic exchange rule. "
            "Creation and annihilation operators are the native coordinates of this page because they move the state between occupation sectors."
        ),
        "equations": [
            r"\mathcal F_{\pm}(\mathcal H)=\bigoplus_{n=0}^{\infty} \mathcal S_{\pm}\mathcal H^{\otimes n}",
            r"[a_i,a_j^\dagger]_{\mp}=\delta_{ij},\qquad [a_i,a_j]_{\mp}=0",
            r"N=\sum_i a_i^\dagger a_i,\qquad N\ket{n_1,n_2,\ldots}=\left(\sum_i n_i\right)\ket{n_1,n_2,\ldots}",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express variable particle number, exchange symmetry, and occupation-number readout."
        ),
    },
    "quantum_geometry": {
        "claim": (
            "{title} is a geometry-realization page: geometric quantities are promoted to quantum observables rather than assumed as a smooth background."
        ),
        "reading": (
            "Quantum geometry uses a quantum state of geometry, often represented by graph or spin-network data. "
            "The operator-to-spectrum step asks for eigenvalues of geometric observables such as area or volume. This places the page near the geometry/boundary interface rather than inside a generic many-mode field layer."
        ),
        "equations": [
            r"\mathcal H_{\Gamma}=L^2\!\left(SU(2)^E/SU(2)^V\right),\qquad \ket{\Gamma,j_e,\iota_v}",
            r"\hat A(S)\ket{\Gamma,j,\iota}=8\pi\gamma\ell_P^2\sum_{e\cap S}\sqrt{j_e(j_e+1)}\,\ket{\Gamma,j,\iota}",
            r"\text{geometry readout}:\quad \hat G\,\ket{g_i}=g_i\ket{g_i}",
        ],
        "equation_note": (
            "Topic-specific constructor: the equations express graph-based geometry states and spectral readout of geometric observables."
        ),
    },
}

TOPIC_CONSTRUCTOR_OVERRIDES.update(
    {
        "hilbert_space": {
            "claim": "{title} is the admissible state carrier of quantum theory: it supplies the space in which states, operators, bases, spectra, and probabilities become legally defined.",
            "reading": "Hilbert space is not physical space and not a geometric background in this book. It is the legal carrier of quantum identity. A state is a vector or density operator on it; the inner product gives amplitudes and norms; observables are self-adjoint operators on it; spectral projectors define possible answers; and unitary evolution preserves norm and probability. Hilbert space is therefore central because it binds state, probability, operator spectrum, and identity preservation into one formal carrier.",
            "equations": [
                r"\ket{\psi}\in\mathcal H,\qquad \langle\psi|\psi\rangle=1",
                r"\rho\in\mathcal S(\mathcal H),\qquad \rho\ge0,\quad \operatorname{Tr}\rho=1",
                r"A=A^\dagger,\qquad A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)",
                r"\Pr(\Delta\mid \rho,A)=\operatorname{Tr}\!\left(\rho E_A(\Delta)\right)",
                r"\rho_t=U(t)\rho U(t)^\dagger,\qquad U^\dagger U=I",
            ],
            "equation_note": "Standard constructor skeleton: normalized states, density states, spectral resolution, Born readout, and unitary identity preservation.",
        },
        "wave_function": {
            "claim": "{title} is a basis-dependent representative of a pure-state ray; it is not identical to the abstract state or to physical configuration space.",
            "reading": "For a configuration space Q with measure mu, the position wave function is the generalized-basis representative psi(x)=<x|psi> of a ray [psi] in L2(Q,mu). Vectors that differ by a nonzero global phase represent the same pure state. Its modulus squared is a probability density only relative to the stated position measure; spin and particle statistics enlarge or constrain the carrier.",
            "equations": [
                r"\mathcal H=L^2(Q,d\mu),\qquad \psi(x)=\langle x|\psi\rangle",
                r"\int_Q |\psi(x)|^2\,d\mu(x)=1,\qquad \ket\psi\sim e^{i\alpha}\ket\psi",
                r"\Pr(X\in\Delta\mid\psi)=\langle\psi|E_X(\Delta)|\psi\rangle=\int_\Delta|\psi(x)|^2\,d\mu(x)",
                r"\mathcal H_{\mathrm{spin}\,s}=L^2(Q,d\mu)\otimes\mathbb C^{2s+1}",
            ],
            "equation_note": "Topic-specific constructor: abstract state ray, position representation, measure-dependent Born probability, and internal spin carrier.",
        },
        "density_matrix": {
            "claim": "{title} is the mixed-state constructor: it keeps probabilistic preparation, entanglement with unobserved degrees of freedom, and partial information in the same state formalism.",
            "reading": "Density matrices generalize pure states without changing the state-to-spectrum readout rule. They are the correct carrier when the preparation is statistical, when a subsystem is traced out, or when decoherence is being described.",
            "equations": [
                r"\rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a},\qquad p_a\ge0,\quad \sum_a p_a=1",
                r"\rho\ge0,\qquad \operatorname{Tr}\rho=1",
                r"p(i)=\operatorname{Tr}(\rho P_i)",
                r"\rho_A=\operatorname{Tr}_B(\rho_{AB})",
            ],
            "equation_note": "Standard constructor skeleton: mixed state, trace rule, and subsystem reduction.",
        },
        "qubit": {
            "claim": r"{title} is the two-dimensional state-carrier constructor used when the admissible state space is \(\mathbb C^2\).",
            "reading": "A qubit is the minimal quantum state space with a basis, amplitudes, unitary control, and measurement readout. Bloch-vector language is a representation of the same two-dimensional carrier.",
            "equations": [
                r"\ket{\psi}=\alpha\ket{0}+\beta\ket{1},\qquad |\alpha|^2+|\beta|^2=1",
                r"\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),\qquad |\mathbf r|\le1",
                r"p(0)=|\langle0|\psi\rangle|^2,\qquad p(1)=|\langle1|\psi\rangle|^2",
            ],
            "equation_note": "Standard constructor skeleton: two-state carrier, Bloch representation, and basis readout.",
        },
        "schr_dinger_equation": {
            "claim": "{title} is the state-transport constructor: the Hamiltonian generates lawful change of the state before readout.",
            "reading": "The Schrödinger equation is not a measurement rule. It is the generator step of the quantum constructor. It evolves the predictive carrier while preserving normalization when the Hamiltonian is self-adjoint.",
            "equations": [
                r"i\hbar\,\partial_t\ket{\psi(t)}=H\ket{\psi(t)}",
                r"\ket{\psi(t)}=U(t)\ket{\psi(0)},\qquad U(t)=e^{-iHt/\hbar}",
                r"\frac{d}{dt}\langle\psi(t)|\psi(t)\rangle=0\quad (H=H^\dagger)",
            ],
            "equation_note": "Standard constructor skeleton: Hamiltonian transport and norm preservation.",
        },
        "hamiltonian_quantum_mechanics": {
            "claim": "{title} is the generator observable: it both transports states and supplies the energy spectrum.",
            "reading": "The Hamiltonian has a dual role. Dynamically, it generates unitary time evolution. Spectrally, its eigenvalues are admissible energy readouts. This dual role is one reason the operator/spectrum branch is central.",
            "equations": [
                r"H\ket{E_n}=E_n\ket{E_n}",
                r"U(t)=e^{-iHt/\hbar}",
                r"\rho(t)=U(t)\rho(0)U(t)^\dagger",
            ],
            "equation_note": "Standard constructor skeleton: energy spectrum and unitary generation.",
        },
        "unitary_operator": {
            "claim": "{title} is the reversible-map constructor: it changes the state while preserving inner products and probabilities.",
            "reading": "Unitary maps are the admissible reversible transformations of closed-system quantum theory. They preserve normalization and carry projective geometry of the state space through time or controlled operations.",
            "equations": [
                r"U^\dagger U=UU^\dagger=I",
                r"\ket{\psi'}=U\ket{\psi}",
                r"\langle\psi'|\phi'\rangle=\langle\psi|\phi\rangle",
            ],
            "equation_note": "Standard constructor skeleton: reversible state transformation and inner-product preservation.",
        },
        "path_integral": {
            "claim": "{title} is an alternate generator constructor: transition amplitudes are obtained by summing phase weights over histories.",
            "reading": "The path integral does not replace the operator constructor. It repackages the generator step as a weighted sum over histories between boundary conditions. It is especially useful when action, symmetry, and field degrees of freedom are more natural than state-vector evolution.",
            "equations": [
                r"K(x_f,t_f;x_i,t_i)=\int_{x_i}^{x_f}\mathcal D x(t)\,\exp\!\left(\frac{i}{\hbar}S[x]\right)",
                r"\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i",
            ],
            "equation_note": "Standard constructor skeleton: boundary-to-boundary transition amplitude through action weights.",
        },
        "path_integral_formulation": {
            "claim": "{title} is the formulation in which the generator is represented by action-weighted histories.",
            "reading": "This page belongs with lawful change because it changes how the transport step is calculated. The observable predictions remain probabilities after amplitudes are composed and squared or traced.",
            "equations": [
                r"\langle q_f,t_f|q_i,t_i\rangle=\int\mathcal Dq\,e^{iS[q]/\hbar}",
                r"Z[J]=\int\mathcal D\phi\,\exp\!\left(\frac{i}{\hbar}(S[\phi]+\int J\phi)\right)",
            ],
            "equation_note": "Standard constructor skeleton: transition amplitudes and generating functional.",
        },
        "observable": {
            "claim": "{title} is the legal-question constructor: it turns a physical question into an operator with spectral outcome channels.",
            "reading": "An observable is the mathematical form of a question that can be asked of a state. Its spectral decomposition defines the possible answers.",
            "equations": [
                r"A=A^\dagger",
                r"A=\sum_i a_iP_i",
                r"p(a_i)=\operatorname{Tr}(\rho P_i)",
            ],
            "equation_note": "Standard constructor skeleton: self-adjoint question, spectral projectors, and Born probabilities.",
        },
        "self_adjoint_operator": {
            "claim": "{title} is the admissible-observable condition: it gives real spectra and well-defined spectral measures.",
            "reading": "Self-adjointness is not a technical decoration. It is the condition that makes an operator a legitimate spectral question in ordinary quantum mechanics.",
            "equations": [
                r"A=A^\dagger",
                r"A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)",
                r"\Pr(\Delta)=\operatorname{Tr}(\rho E_A(\Delta))",
            ],
            "equation_note": "Standard constructor skeleton: spectral theorem form of a legitimate observable.",
        },
        "projection_valued_measure": {
            "claim": "{title} is the sharp-readout constructor: mutually exclusive outcome projectors partition the identity.",
            "reading": "A projection-valued measure encodes an ideal sharp measurement. It defines outcome channels that are orthogonal and exhaustive.",
            "equations": [
                r"P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=I",
                r"p(i)=\operatorname{Tr}(\rho P_i)",
                r"\rho\mapsto \frac{P_i\rho P_i}{\operatorname{Tr}(\rho P_i)}",
            ],
            "equation_note": "Standard constructor skeleton: sharp outcome channels, probability, and projective update.",
        },
        "povm": {
            "claim": "{title} is the generalized-readout constructor: outcome effects need not be orthogonal projectors.",
            "reading": "POVMs separate the probability readout from the idealized projection assumption. They are the natural mechanism for noisy, coarse-grained, indirect, or open-system measurements.",
            "equations": [
                r"E_i\ge0,\qquad \sum_iE_i=I",
                r"p(i)=\operatorname{Tr}(\rho E_i)",
                r"E_i=\sum_\alpha K_{i\alpha}^\dagger K_{i\alpha}",
            ],
            "equation_note": "Standard constructor skeleton: positive effects and generalized Born rule.",
        },
        "born_rule": {
            "claim": "{title} is the probability-readout constructor: it maps a state and a spectral channel to an observed probability.",
            "reading": "The Born rule is the point where the constructor becomes predictive. It does not name an object; it connects state preparation and a legal question to frequencies over outcome channels.",
            "equations": [
                r"p(i|\rho,\{P_i\})=\operatorname{Tr}(\rho P_i)",
                r"\Pr(X\in\Delta|\psi)=\int_\Delta|\psi(x)|^2\,d\mu(x)",
                r"\sum_i p(i)=1",
            ],
            "equation_note": "Standard constructor skeleton: probability assignment for projective and position readouts.",
        },
        "measurement_in_quantum_mechanics": {
            "claim": "{title} is the complete readout junction: it combines a state, a measurement model, probabilities, and sometimes an update rule.",
            "reading": "Measurement is not the root of quantum theory in this book. It is the junction where a prepared state and an observable or POVM are converted into probabilities and recorded outcomes.",
            "equations": [
                r"p(i)=\operatorname{Tr}(\rho E_i)",
                r"\rho\mapsto \rho_i=\frac{K_i\rho K_i^\dagger}{\operatorname{Tr}(K_i\rho K_i^\dagger)}",
                r"E_i=K_i^\dagger K_i",
            ],
            "equation_note": "Standard constructor skeleton: generalized measurement probability and conditional update.",
        },
        "commutator": {
            "claim": "{title} measures the physical consequence of exchanging two operations: it governs joint measurability, generated motion, and the leading difference between reversed protocols.",
            "reading": "For two operators on a common domain, [A,B]=AB-BA compares the two possible orders. For observables, a nonzero commutator obstructs a common sharp spectral resolution and enters uncertainty bounds. For a Hamiltonian H, [H,A] gives the dynamical change of A. For short control pulses, [A,B] is the first term that distinguishes the two reversed sequences. One algebraic object therefore connects compatibility, dynamics, and order-sensitive response.",
            "equations": [
                r"[A,B]=AB-BA",
                r"\frac{dA}{dt}=\frac{i}{\hbar}[H,A]+\left(\frac{\partial A}{\partial t}\right)",
                r"\Delta A\,\Delta B\geq\frac12\left|\langle[A,B]\rangle\right|",
                r"e^{\epsilon A}e^{\epsilon B}e^{-\epsilon A}e^{-\epsilon B}=I+\epsilon^2[A,B]+O(\epsilon^3)",
            ],
            "equation_note": "Order exchange, Heisenberg evolution, uncertainty, and the leading closed-sequence response are four consequences of the same commutator.",
            "forced_consequences": [
                "A nonzero commutator prevents a generic common sharp eigenbasis and imposes state-dependent uncertainty bounds.",
                "The commutator with the Hamiltonian determines whether an observable is conserved and how it changes in time.",
                "Reversing two short operations produces a difference proportional to their commutator at leading nontrivial order.",
            ],
            "scope_conditions": [
                "For unbounded operators, the common domain belongs to the physical statement; a formal commutator without a domain need not define an observable relation.",
                "A nonzero commutator is not by itself a new interaction. It becomes physical through a state and an observable consequence.",
            ],
        },
        "uncertainty_principle": {
            "claim": "{title} is a compatibility-limit theorem: non-commuting observables impose lower bounds on joint sharpness.",
            "reading": "Uncertainty is not detector imperfection. It is a structural consequence of state variance and non-commuting observables.",
            "equations": [
                r"\Delta_\rho A\,\Delta_\rho B\ge \frac12\left|\operatorname{Tr}(\rho[A,B])\right|",
                r"\Delta x\,\Delta p\ge\frac{\hbar}{2}",
            ],
            "equation_note": "Standard constructor skeleton: variance bound from commutator structure.",
        },
        "quantum_entanglement": {
            "claim": "{title} is a property of a composite state that cannot be written as a classical mixture of product states across a chosen subsystem decomposition; for a pure state, this reduces to failure to factor.",
            "reading": "The tensor-product decomposition specifies what counts as subsystem A and subsystem B. A pure state is entangled when its Schmidt rank exceeds one. Each subsystem can then be mixed even though the joint state is pure, because partial tracing discards the correlations that purify it. Local basis changes preserve the Schmidt coefficients, while a different physical factorization can change whether the same vector is called entangled. Bell measurements test whether the resulting correlations admit a local hidden-variable model.",
            "equations": [
                r"\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B",
                r"\ket{\Psi}_{AB}=\sum_k\sqrt{\lambda_k}\ket{k_A}\ket{k_B},\qquad \sum_k\lambda_k=1",
                r"\rho_A=\operatorname{Tr}_B\ket{\Psi}\bra{\Psi},\qquad S_A=-\operatorname{Tr}(\rho_A\log\rho_A)",
                r"|S_{\mathrm{CHSH}}|\leq2,\qquad |S_{\mathrm{CHSH}}|_{\mathrm{QM}}\leq2\sqrt2",
            ],
            "equation_note": "Subsystem factorization, Schmidt spectrum, reduced-state entropy, and Bell correlations separate the state relation from its local readout.",
            "forced_consequences": [
                "A pure bipartite state with more than one nonzero Schmidt coefficient gives mixed reduced states and correlations unavailable to product preparations.",
                "Local unitary changes of basis preserve the Schmidt coefficients and the pure-state entanglement entropy.",
                "Suitable local measurements can violate a Bell inequality even though each subsystem alone carries no corresponding pure state.",
            ],
            "scope_conditions": [
                "Entanglement is defined relative to a physical subsystem algebra or tensor-product factorization.",
                "For mixed states, nonfactorization of one decomposition is insufficient; separability requires testing all convex product decompositions.",
            ],
        },
        "quantum_decoherence": {
            "claim": "{title} is the loss of observable phase coherence in a subsystem when information about alternative amplitudes becomes encoded in environmental correlations.",
            "reading": "The joint system and environment may evolve unitarily while the reduced system loses interference. Interaction correlates different system alternatives with distinguishable environmental states; tracing over the environment then suppresses off-diagonal terms in the selected pointer basis. Decoherence does not select one outcome, and it is not identical to memory. Markovian decoherence is possible when the reduced state still determines its future. Memory begins when discarded correlations return and two preparations with the same reduced state acquire different later statistics.",
            "equations": [
                r"\rho_S(t)=\operatorname{Tr}_E[U_{SE}(t)\rho_{SE}(0)U_{SE}^{\dagger}(t)]",
                r"\frac{\ket0\ket{E_0}+\ket1\ket{E_1}}{\sqrt2},\qquad (\rho_S)_{01}\propto\langle E_1|E_0\rangle",
                r"\dot\rho_S=-\frac{i}{\hbar}[H_S,\rho_S]+\sum_k\gamma_k\mathcal D[L_k]\rho_S",
                r"V_{t+s}=V_tV_s\quad\text{only in the time-homogeneous Markov limit}",
            ],
            "equation_note": "Joint unitary evolution, environmental distinguishability, reduced decoherence, and the semigroup test distinguish loss of interference from dynamical memory.",
            "forced_consequences": [
                "Interference visibility falls with the overlap of the environmental states correlated with the interfering alternatives.",
                "The phase information can remain in the joint state even when it is absent from all reduced-system observables.",
                "When hidden correlations later alter the reduced dynamics, an auxiliary state coordinate or a memory kernel is required for predictive closure.",
            ],
            "scope_conditions": [
                "The preferred basis and decoherence rate depend on the interaction, environmental spectrum, and initial system-environment state.",
                "Suppression of off-diagonal terms does not by itself derive a unique recorded outcome.",
            ],
        },
        "bell_s_theorem": {
            "claim": "{title} is a compatibility/locality stress test: quantum correlations violate bounds satisfied by local hidden-variable assignments.",
            "reading": "Bell's theorem is not a page about a mysterious object. It is a falsifier for a classical joint-assignment model of measurement outcomes.",
            "equations": [
                r"|E(a,b)+E(a,b')+E(a',b)-E(a',b')|\le 2",
                r"\text{quantum prediction can reach }2\sqrt2",
            ],
            "equation_note": "Standard constructor skeleton: CHSH inequality and quantum violation bound.",
        },
        "particle_in_a_box": {
            "claim": "{title} is a boundary-spectrum constructor: a spatial domain and boundary condition discretize the allowed energy spectrum.",
            "reading": "The page shows how a boundary condition changes the domain of the Hamiltonian and therefore the allowed spectra.",
            "equations": [
                r"\psi(0)=\psi(L)=0",
                r"\psi_n(x)=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}",
                r"E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}",
            ],
            "equation_note": "Standard constructor skeleton: boundary condition and discrete spectrum.",
        },
        "quantum_tunnelling": {
            "claim": "{title} is a boundary-realization constructor: a state has nonzero transmission through a classically forbidden region.",
            "reading": "Tunnelling shows that the realization layer matters. A potential barrier changes the admissible wave solutions and produces transmission even where classical kinetic energy would be negative.",
            "equations": [
                r"T\sim \exp\!\left(-2\int_{x_1}^{x_2}\sqrt{\frac{2m(V(x)-E)}{\hbar^2}}\,dx\right)",
                r"-\frac{\hbar^2}{2m}\psi''(x)+V(x)\psi(x)=E\psi(x)",
            ],
            "equation_note": "Standard constructor skeleton: barrier-domain Schrödinger equation and WKB transmission.",
        },
        "fermi_dirac_statistics": {
            "claim": "{title} is an antisymmetric-state constructor: exchange statistics restricts which many-fermion occupation patterns are admissible.",
            "reading": "Fermi-Dirac statistics is an admissibility rule, not a generator of time evolution. Anticommutation and antisymmetry imply single occupation of each one-particle mode, while the thermal distribution states the mean occupation of those modes.",
            "equations": [
                r"\{a_i,a_j^\dagger\}=\delta_{ij},\qquad n_i\in\{0,1\}",
                r"\bar n_i=\frac{1}{e^{\beta(\varepsilon_i-\mu)}+1}",
            ],
            "equation_note": "Topic-specific construction: antisymmetric mode algebra, exclusion, and equilibrium occupation.",
        },
        "bose_einstein_statistics": {
            "claim": "{title} is a symmetric-state constructor: exchange statistics permits collective occupation of one quantum mode.",
            "reading": "Bose-Einstein statistics is an admissibility rule for symmetric many-particle states. Commutation permits unrestricted mode occupation, while the thermal distribution determines the mean population and the conditions for macroscopic ground-state occupation.",
            "equations": [
                r"[a_i,a_j^\dagger]=\delta_{ij},\qquad n_i\in\{0,1,2,\ldots\}",
                r"\bar n_i=\frac{1}{e^{\beta(\varepsilon_i-\mu)}-1}",
            ],
            "equation_note": "Topic-specific construction: symmetric mode algebra, unrestricted occupation, and equilibrium population.",
        },
        "quantum_field_theory": {
            "claim": "{title} is the many-mode local-field extension of the quantum constructor.",
            "reading": "Quantum field theory lifts the state-operator-spectrum construction to fields, local operators, creation and annihilation modes, and scattering amplitudes. Particles become stable excitation/readout roles of fields.",
            "equations": [
                r"\Phi(x)=\sum_k\left(a_k u_k(x)+a_k^\dagger u_k^*(x)\right)",
                r"[a_k,a_l^\dagger]_{\mp}=\delta_{kl}",
                r"\langle 0|T\{\Phi(x)\Phi(y)\}|0\rangle",
            ],
            "equation_note": "Standard constructor skeleton: field expansion, mode algebra, and correlation readout.",
        },
        "gauge_theory": {
            "claim": "{title} defines how internal states are compared at different spacetime points: a connection relates neighboring frames, and curvature records the path dependence that no single gauge choice can remove.",
            "reading": "A local gauge transformation changes the field coordinates used at each point without changing the physical state. Ordinary derivatives compare fields in different local frames and therefore cease to transform covariantly. The gauge connection repairs that comparison. Its commutator gives the field strength, while Wilson loops measure the accumulated transport around a closed path. Gauss constraints select physical states and charges. The connection is representation dependent; curvature, loop observables, and gauge-invariant amplitudes carry the physical content.",
            "equations": [
                r"D_\mu=\partial_\mu+igA_\mu",
                r"[D_\mu,D_\nu]=igF_{\mu\nu}",
                r"W(\gamma)=\operatorname{Tr}\,\mathcal P\exp\!\left(ig\oint_\gamma A_\mu dx^\mu\right)",
                r"G^a\ket{\Psi_{\mathrm{phys}}}=0",
            ],
            "equation_note": "The connection defines local comparison, curvature measures its infinitesimal path dependence, and the constraint selects physical states.",
            "forced_consequences": [
                "Gauge-related potentials give identical gauge-invariant amplitudes, charges, field strengths, and loop observables.",
                "A nontrivial Wilson loop can retain global transport information that is absent from any one local gauge representative.",
                "The Gauss constraint removes redundant state vectors and fixes the physical charge sector.",
            ],
            "scope_conditions": [
                "The gauge group, representation, matter content, dimension, and boundary conditions distinguish different physical theories.",
                "A gauge-dependent potential becomes observable only through a gauge-invariant relation such as field strength, phase difference, charge, or loop holonomy.",
            ],
        },
        "renormalization": {
            "claim": "{title} relates physical descriptions at different resolutions by changing couplings and operator weights while preserving long-distance predictions.",
            "reading": "Coarse graining removes short-distance variables and generates every operator allowed by the remaining symmetries. Their coefficients flow with scale. Relevant directions grow, irrelevant directions decay, and fixed points organize scale-invariant behaviour. Microscopically different systems can therefore share critical exponents and scaling functions when their flows approach the same fixed point. Universality is the invariance class of this scale transformation, not a visual similarity between equations.",
            "equations": [
                r"\mu\frac{dg_i}{d\mu}=\beta_i(\{g\})",
                r"\left(\mu\partial_\mu+\beta_i\partial_{g_i}+n\gamma\right)G^{(n)}=0",
                r"\beta_i(g_*)=0,\qquad \delta g_i(b)=b^{y_i}\delta g_i",
                r"\mathcal L_{\mathrm{eff}}(\mu)=\sum_i c_i(\mu)\mathcal O_i",
            ],
            "equation_note": "Beta functions, scale-independent observables, fixed points, and scaling directions define the transport of a theory across resolution.",
            "forced_consequences": [
                "Observable predictions are independent of the arbitrary renormalization scale when explicit scale dependence and coupling flow compensate.",
                "Systems approaching the same fixed point with the same relevant directions share critical exponents and scaling functions.",
                "Relevant perturbations drive the flow away from a fixed point and select the accessible phases or crossover regimes.",
            ],
            "scope_conditions": [
                "Universality requires matching dimensionality, symmetries, conserved quantities, interaction range, and relevant directions; a shared dimensionless group alone is insufficient.",
                "An effective theory is tied to a scale and accuracy, because omitted operators return through controlled corrections.",
            ],
        },
        "quantum_channel": {
            "claim": "{title} is the open-system protocol constructor: it maps input states to output states while preserving complete positivity and trace.",
            "reading": "A channel is the mechanism for noisy transformations, measurements with forgotten outcomes, and subsystem evolution.",
            "equations": [
                r"\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger",
                r"\sum_aK_a^\dagger K_a=I",
                r"p(y)=\operatorname{Tr}(M_y\mathcal E(\rho))",
            ],
            "equation_note": "Standard constructor skeleton: completely positive trace-preserving map and readout.",
        },
        "quantum_circuit": {
            "claim": "{title} is the engineered-composition constructor: a finite sequence of admissible maps prepares, transforms, and measures a register.",
            "reading": "A circuit is the protocol layer of the same state-operator-readout machinery. Gates are controlled unitary or channel maps; measurement converts final states into output probabilities.",
            "equations": [
                r"\rho_{\mathrm{out}}=U_m\cdots U_2U_1\,\rho_{\mathrm{in}}\,U_1^\dagger U_2^\dagger\cdots U_m^\dagger",
                r"p(y)=\operatorname{Tr}(M_y\rho_{\mathrm{out}})",
            ],
            "equation_note": "Standard constructor skeleton: composed gates and final measurement.",
        },
        "ads_cft_correspondence": {
            "claim": "{title} is a geometry-translation constructor: bulk gravitational data and boundary field data are treated as dual presentations of one operator structure.",
            "reading": "AdS/CFT belongs at the interface where geometry becomes a representation of the quantum construction rather than the invariant root. The practical content is a dictionary between bulk fields and boundary operators.",
            "equations": [
                r"Z_{\mathrm{grav}}[\phi_0]\simeq Z_{\mathrm{CFT}}[J=\phi_0]",
                r"\left\langle \exp\!\int J\mathcal O\right\rangle_{\mathrm{CFT}}=Z_{\mathrm{bulk}}[\phi|_{\partial}=J]",
            ],
            "equation_note": "Standard constructor skeleton: boundary-source/bulk-field dictionary.",
        },
        "measurement_problem": {
            "claim": "{title} is the junction between unitary system--apparatus coupling, probability readout, and conditional state update; these are distinct maps and need not be identified.",
            "reading": "A measurement model first couples the system to an apparatus or environment. A POVM or instrument then assigns outcome probabilities, and a conditional map specifies the post-record state. The foundational problem concerns the relation between these operations and a definite record, not the absence of a probability formula.",
            "equations": [
                r"\rho_{SA}'=U_{SA}(\rho_S\otimes\rho_A)U_{SA}^{\dagger}",
                r"p(i)=\operatorname{Tr}[\mathcal I_i(\rho_S)]=\operatorname{Tr}(\rho_SE_i)",
                r"\rho_{S|i}=\frac{\mathcal I_i(\rho_S)}{p(i)},\qquad \rho_S'=\sum_i\mathcal I_i(\rho_S)",
            ],
            "equation_note": "Topic-specific constructor: premeasurement coupling, outcome probability, conditional update, and unconditioned evolution are separated.",
        },
        "quantum_gravity": {
            "claim": "{title} asks whether geometry is a background realization, a constrained quantum carrier, or an emergent readout of a deeper quantum state.",
            "reading": "The constructor cannot treat quantum gravity as an ordinary wave function on a fixed domain. A candidate theory must specify the state space of geometric and matter degrees of freedom, the constraint or evolution operators, the gauge-invariant or relational observables, and the limit in which classical spacetime is recovered.",
            "equations": [
                r"\Psi\in\mathcal H_{\mathrm{geom}\otimes\mathrm{matter}},\qquad \widehat{\mathcal C}_a\Psi=0",
                r"[\widehat O_{\mathrm{phys}},\widehat{\mathcal C}_a]\Psi=0",
                r"\langle\Psi|\widehat g_{\mu\nu}|\Psi\rangle\longrightarrow g^{\mathrm{cl}}_{\mu\nu}\quad\text{in a controlled semiclassical regime}",
            ],
            "equation_note": "Schematic constructor shared by constrained approaches: quantum carrier, constraints, physical observables, and semiclassical recovery must all be specified.",
        },
        "quantum_simulator": {
            "claim": "{title} is a target--carrier--validation construction: a controllable physical system encodes another model, and selected observables test whether the encoded dynamics is faithful.",
            "reading": "The simulator Hamiltonian is not by itself the target theory. The claim also needs an encoding between target and device states, a correspondence between their generators or channels, and validation observables with an error budget over the stated time and parameter range.",
            "equations": [
                r"V:\mathcal H_{\mathrm{target}}\hookrightarrow\mathcal H_{\mathrm{device}}",
                r"\left\|U_{\mathrm{device}}(t)V-VU_{\mathrm{target}}(t)\right\|\le\varepsilon(t)",
                r"\left|\langle O\rangle_{\mathrm{target}}-\langle VO V^{\dagger}\rangle_{\mathrm{device}}\right|\le\delta_O",
            ],
            "equation_note": "Topic-specific constructor: encoding, dynamical correspondence, and observable validation are separate obligations.",
        },
    }
)


TOPIC_FRAME_OVERRIDES: Dict[str, Dict[str, str]] = {
    "fermi_dirac_statistics": {
        "role": "fermionic state-admissibility role",
        "carrier": "A fermionic Fock space assembled from antisymmetric many-particle sectors or occupation-number modes.",
        "operator": "Creation, annihilation, and number operators obeying canonical anticommutation relations.",
        "admissibility": "Exchange antisymmetry restricts each one-particle mode to occupation zero or one for each internal state.",
        "readout": "Mode occupations, Fermi energy, particle density, pressure, heat capacity, and other equilibrium response functions.",
        "test": "The statistics must reproduce exclusion-controlled occupation and the appropriate classical dilute limit at low fugacity.",
    },
    "bose_einstein_statistics": {
        "role": "bosonic state-admissibility role",
        "carrier": "A bosonic Fock space assembled from symmetric many-particle sectors or occupation-number modes.",
        "operator": "Creation, annihilation, and number operators obeying canonical commutation relations.",
        "admissibility": "Exchange symmetry permits any non-negative integer occupation of a one-particle mode.",
        "readout": "Mode occupations, condensate fraction, particle density, pressure, heat capacity, and coherence observables.",
        "test": "The statistics must recover Bose enhancement, the classical dilute limit, and condensation only where density of states and thermodynamic constraints permit it.",
    },
    "old_quantum_theory": {
        "role": "semiclassical quantization role",
        "carrier": "Classical phase space, especially periodic or multiply periodic Hamiltonian trajectories described by action variables.",
        "operator": "Hamiltonian flow together with Bohr--Sommerfeld action quantization; no general Hilbert-space operator calculus is assumed.",
        "admissibility": "Only trajectories satisfying quantized action conditions are retained, with correspondence to classical frequencies required at large quantum number.",
        "readout": "Discrete energies, transition frequencies, and the spectral regularities inferred from them.",
        "test": "Recover the observed level or line spectrum in the regime where the semiclassical orbit construction is valid, and identify where it fails for nonintegrable or many-electron systems.",
    },
    "hilbert_space": {
        "carrier": "A complex Hilbert space, or a density-operator state space built on it.",
        "operator": "Self-adjoint observables, unitary maps, spectral projectors, and domain-restricted generators defined on the carrier.",
        "admissibility": "Inner-product structure, normalization, positivity for density states, and operator-domain conditions make states and observables legal.",
        "readout": "Born probabilities, spectral projectors, expectation values, and preserved norms.",
        "test": "Changing basis or representation should preserve probabilities and expectation values when the change is unitary.",
    },
    "commutator": {
        "carrier": "A common state space on which two transformations, observables, or questions are both defined.",
        "operator": "The ordered products AB and BA, compared through the obstruction [A,B]=AB-BA.",
        "admissibility": "A nonzero commutator marks an order-dependence or compatibility limit; a zero commutator permits a common sharp refinement only when the remaining spectral conditions hold.",
        "readout": "Compatibility tests, uncertainty bounds, common eigenspaces, or canonical commutation relations.",
        "test": "The mechanism is supported only when changing operator order changes the algebraic or statistical prediction.",
    },
    "quantum_entanglement": {
        "carrier": "A composite Hilbert space with a physically specified subsystem algebra or tensor-product factorization.",
        "operator": "Schmidt decomposition, partial trace, local observables, and joint correlation operators.",
        "admissibility": "The joint density operator is positive and normalized; separability is defined relative to the chosen subsystem structure.",
        "readout": "Reduced-state spectra, entanglement entropy, correlation witnesses, and Bell parameters.",
        "test": "Product and separable controls cannot reproduce a validated entanglement witness or Bell violation under the same local measurements.",
    },
    "quantum_decoherence": {
        "carrier": "A joint system-environment state together with the reduced density operator accessible to the observer.",
        "operator": "System-environment unitary evolution followed by partial trace, or the corresponding reduced dynamical map.",
        "admissibility": "The joint state remains normalized and positive; a Markovian reduction additionally requires future maps to be fixed by the present reduced state.",
        "readout": "Off-diagonal coherence, interference visibility, purity, and history-dependent response.",
        "test": "Environmental distinguishability suppresses interference, while equal reduced states with different later responses identify retained hidden correlations rather than decoherence alone.",
    },
    "gauge_theory": {
        "carrier": "Matter and gauge fields modulo local gauge equivalence, restricted to the physical constraint sector.",
        "operator": "A covariant derivative and connection whose commutator gives the field strength.",
        "admissibility": "Gauss constraints, gauge covariance, operator domains, and boundary conditions select the physical states and charges.",
        "readout": "Field strengths, Wilson loops, conserved charges, scattering amplitudes, and other gauge-invariant quantities.",
        "test": "Gauge-related representatives give identical physical observables, while a nontrivial loop observable records curvature or global holonomy.",
    },
    "renormalization": {
        "carrier": "Effective fields and degrees of freedom defined at a stated resolution or cutoff.",
        "operator": "A coarse-graining transformation and beta functions acting on the coefficients of an effective operator expansion.",
        "admissibility": "Symmetry, dimensionality, locality assumptions, relevant directions, and renormalization conditions determine the allowed flow.",
        "readout": "Running couplings, correlation functions, scaling dimensions, critical exponents, and corrections to scaling.",
        "test": "Observables remain independent of the arbitrary renormalization scale, and distinct microscopic systems share scaling data only when their flows approach the same fixed point.",
    },
    "quantum_channel": {
        "carrier": "Input and output density operators, possibly on different Hilbert spaces or subsystem carriers.",
        "operator": "A completely positive trace-preserving map, often represented by Kraus operators or by a Stinespring dilation.",
        "admissibility": "Complete positivity and trace preservation are the legal conditions; non-trace-preserving maps require an explicitly conditioned outcome.",
        "readout": "Output state, final POVM probabilities, fidelity, capacity, error rate, or recovered subsystem statistics.",
        "test": "The channel claim requires a map that stays positive under extension by an untouched reference system and preserves total probability.",
    },
    "measurement_problem": {
        "carrier": "A joint system--apparatus state, possibly enlarged by environmental degrees of freedom.",
        "operator": "A premeasurement interaction followed by a measurement instrument whose components label possible records.",
        "admissibility": "The instrument maps are completely positive and their sum is trace preserving; the outcome effects sum to the identity.",
        "readout": "Outcome probabilities and conditional post-record states must be stated separately.",
        "test": "A proposed resolution must identify where a definite record enters and how its prediction differs from the unconditioned state evolution.",
    },
    "quantum_gravity": {
        "carrier": "A state space for geometric and matter degrees of freedom, or a deeper carrier from which geometry is reconstructed.",
        "operator": "Constraint, evolution, or amplitude operators that do not presuppose an unexamined fixed spacetime background.",
        "admissibility": "Gauge and diffeomorphism constraints determine the physical state space and which operators are observable.",
        "readout": "Relational observables, boundary amplitudes, geometric spectra, or semiclassical spacetime data.",
        "test": "The construction must recover controlled classical geometry and reproduce established low-energy quantum field predictions in its domain of validity.",
    },
    "quantum_simulator": {
        "carrier": "A controllable device state space together with an explicit encoding of the target state space.",
        "operator": "Device Hamiltonians, channels, or gate sequences intended to reproduce target dynamics under the encoding.",
        "admissibility": "Control errors, leakage, finite size, noise, and approximation order define the regime in which the correspondence is claimed.",
        "readout": "Encoded target observables compared with independently predicted or calibrated device measurements.",
        "test": "Validation requires observables and error bounds beyond agreement with the programmed control Hamiltonian.",
    },
}


TOPIC_SUPPORT_OVERRIDES: Dict[str, tuple[List[str], List[str], List[str]]] = {
    "commutator": (
        [
            "The commutator transforms covariantly under a simultaneous unitary change of representation.",
            "Joint spectral compatibility is unchanged by a consistent representation change.",
            "The leading order-sensitive response survives when different physical controls realize the same operator algebra.",
        ],
        [
            "The matrix entries, basis, carrier, and physical implementation of the two operations may change.",
            "Domains can change the meaning of formal commutation relations for unbounded operators.",
            "The observable consequence depends on the prepared state and on how the operator difference is read out.",
        ],
        [
            "Reversing two calibrated operations isolates the response generated by their commutator.",
            "A commuting control pair removes the order-sensitive contribution without changing the individual operations.",
            "Agreement requires the same operator domain and measured observable, not merely similar notation.",
        ],
    ),
    "quantum_entanglement": (
        [
            "Schmidt coefficients and pure-state entanglement entropy are invariant under local unitary changes of basis.",
            "The reduced-state spectra preserve the amount of bipartite pure-state entanglement.",
            "Correlations remain joint properties even when neither subsystem has a pure local state.",
        ],
        [
            "The subsystem factorization and accessible observable algebra determine which correlations count as entanglement.",
            "Noise, loss, and coarse graining can convert pure-state entanglement into mixed-state correlations.",
            "Photons, spins, atoms, modes, and encoded qubits can realize the same Schmidt structure.",
        ],
        [
            "Local measurements reconstruct a correlation witness or Bell parameter that product preparations cannot reproduce.",
            "Independent local-unitary rotations leave the inferred Schmidt spectrum unchanged.",
            "A separable-state control fixes the correlation background of the apparatus.",
        ],
    ),
    "quantum_decoherence": (
        [
            "The joint state retains phase information transferred from the subsystem into system-environment correlations.",
            "Reduced interference visibility is fixed by the overlap of environmental states correlated with the alternatives.",
            "Equivalent system-environment dilations give the same reduced channel and system observables.",
        ],
        [
            "The preferred basis, decay rate, and recoherence depend on the interaction, environmental spectrum, and initial correlations.",
            "Changing the system-environment partition changes which correlations are hidden.",
            "A Markov approximation removes returning correlations; retaining them introduces auxiliary coordinates or a memory kernel.",
        ],
        [
            "Interference visibility is compared with a control in which the environment cannot distinguish the alternatives.",
            "Two preparations with the same reduced state determine whether hidden correlations alter later observables.",
            "Reversing or decoupling the interaction determines whether coherence remains recoverable in the joint state.",
        ],
    ),
    "gauge_theory": (
        [
            "Gauge-equivalent potentials give the same gauge-invariant amplitudes, field strengths, charges, and loop observables.",
            "Curvature records the infinitesimal holonomy of the connection and cannot be removed by a local gauge choice.",
            "The physical state belongs to the constraint sector rather than to an arbitrary field-coordinate representation.",
        ],
        [
            "The gauge potential, local basis, gauge-fixing condition, and coordinate description may change.",
            "The gauge group, representation, matter content, dimension, and boundary conditions specify different physical theories.",
            "Topological sectors and boundary charges can survive even where the local field strength vanishes.",
        ],
        [
            "A closed-loop phase or Wilson observable distinguishes nontrivial holonomy from a removable local gauge choice.",
            "Gauge-related descriptions give identical probabilities for the same physical preparation and readout.",
            "An additional field or interaction changes a gauge-invariant observable rather than only the gauge potential.",
        ],
    ),
    "renormalization": (
        [
            "Observable predictions remain independent of the arbitrary renormalization scale when couplings and fields flow consistently.",
            "Critical exponents and scaling functions are shared by systems approaching the same fixed point with the same relevant directions.",
            "Symmetry and dimensionality constrain the effective operators generated by coarse graining.",
        ],
        [
            "Couplings, field normalizations, effective degrees of freedom, and operator coefficients depend on scale.",
            "Microscopic Hamiltonians can differ while their long-distance flows enter the same universality class.",
            "A relevant perturbation can drive the system away from one fixed point toward another phase or crossover regime.",
        ],
        [
            "Measurements at several scales determine whether running couplings follow one beta function.",
            "Microscopically different realizations determine whether critical exponents and scaling functions coincide.",
            "Corrections to scaling distinguish approach to a fixed point from an exact scale-invariant law.",
        ],
    ),
    "fermion": (
        [
            "Exchange antisymmetry, exterior-product state space, canonical anticommutation and zero-or-one mode occupation are equivalent forms of the fermionic restriction.",
            "The coincidence node and exchange hole survive changes between first-quantized wave functions, Slater determinants and second-quantized fields.",
            "Fermion parity remains meaningful when particle number changes, including in paired and superconducting states.",
        ],
        [
            "Mass, charge, dispersion, dimensionality, interaction law and gauge representation belong to the physical realization and are not fixed by exchange statistics.",
            "A change of carrier can turn local fermion operators into nonlocal strings, as in the Jordan--Wigner transformation.",
            "Two-dimensional braid statistics and composite-particle structure alter the exchange construction beyond the elementary boson--fermion dichotomy.",
        ],
        [
            "Verify antisymmetry or canonical anticommutation and the resulting zero-or-one occupation spectrum.",
            "At fixed one-particle spectrum, compare with distinguishable-particle and sign-erased controls to isolate exchange.",
            "For a claimed transfer, compare correlations and locality as well as energies; spectral agreement alone is insufficient.",
        ],
    ),
    "fermi_dirac_statistics": (
        [
            "Exchange antisymmetry and canonical anticommutation define the fermionic many-particle sectors.",
            "Each one-particle mode has occupation zero or one for each internal state.",
            "The Fermi-Dirac function gives the equilibrium mean occupation once energy, temperature, and chemical potential are specified.",
        ],
        [
            "The dispersion relation, dimensionality, degeneracy, density of states, and interaction approximation depend on the physical system.",
            "Electrons, atoms, nucleons, and fermionic quasiparticles realize the same exchange rule with different Hamiltonians and observables.",
            "Finite temperature smooths the occupation edge that is sharp at the Fermi energy in the ideal zero-temperature limit.",
        ],
        [
            "Recover occupations restricted to zero or one and the ideal zero-temperature Fermi sea.",
            "Recover the Maxwell-Boltzmann distribution in the dilute low-fugacity limit.",
            "Integrate the mode occupations against the density of states and verify the specified particle number.",
        ],
    ),
    "bose_einstein_statistics": (
        [
            "Exchange symmetry and canonical commutation define the bosonic many-particle sectors.",
            "Each one-particle mode admits any non-negative integer occupation.",
            "The Bose-Einstein function gives the equilibrium mean occupation once energy, temperature, and chemical potential are specified.",
        ],
        [
            "The dispersion relation, dimensionality, density of states, conserved particle number, and interaction approximation depend on the physical system.",
            "Photons, cold atoms, phonons, and bosonic quasiparticles realize the same exchange rule with different chemical-potential constraints.",
            "Macroscopic occupation of the lowest mode occurs only when the density of states and thermodynamic limit support condensation.",
        ],
        [
            "Recover unrestricted mode occupation and Bose enhancement relative to distinguishable particles.",
            "Recover the Maxwell-Boltzmann distribution in the dilute low-fugacity limit.",
            "Verify particle-number or energy constraints and test whether the inferred condensate fraction follows the correct dimensional dependence.",
        ],
    ),
    "old_quantum_theory": (
        [
            "Hamiltonian trajectories and their action variables provide the classical carrier of the construction.",
            "Action quantization selects a discrete subset of otherwise continuous classical motions.",
            "Energy differences determine transition frequencies, with correspondence to classical orbital frequencies at large quantum number.",
        ],
        [
            "The orbit family, potential, number of action variables, and applicable quantization condition depend on the physical system.",
            "Modern semiclassical theory adds phase and turning-point corrections absent from the earliest quantization rules.",
            "The construction ceases to be adequate for generic nonintegrable motion, many-electron spectra, and intrinsically noncommuting questions.",
        ],
        [
            "Recover the hydrogenic level and line spectrum in the regime where action quantization applies.",
            "Compare the semiclassical prediction with the corresponding Schrödinger spectrum and identify its controlled limit.",
            "Treat failures outside that limit as evidence for the modern state-and-operator formalism, rather than as adjustable orbit parameters.",
        ],
    ),
}


def page_display_name(title: str) -> str:
    clean = clean_text(title)
    special = {
        "qbism": "QBism",
        "qed": "QED",
        "qcd": "QCD",
        "ads/cft correspondence": "AdS/CFT correspondence",
    }
    return special.get(clean.lower(), clean)


def indefinite_article(phrase: str) -> str:
    text = str(phrase or "").strip().lower()
    if not text:
        return "a"
    if text[0] in "aeiou":
        return "an"
    return "a"


def ranked_keys(profile: Mapping[str, Any], labels: Mapping[str, str], limit: int = 3, threshold: float = 0.05) -> List[str]:
    rows = [
        (key, float(value or 0.0))
        for key, value in profile.items()
        if float(value or 0.0) >= threshold
    ]
    rows.sort(key=lambda item: item[1], reverse=True)
    return [labels.get(key, key) for key, _ in rows[:limit]]


def normalize_private_formula(value: Any) -> str:
    text = str(value or "")
    text = text.replace("Α", "A").replace("Ω", "O").replace("Ξ", "Xi").replace("Λ", "L")
    text = text.replace("⊕", "+")
    return re.sub(r"\s+", " ", text).strip()


def constructor_template(branch_id: str, row: Mapping[str, Any]) -> Mapping[str, Any]:
    slug = str(row.get("slug") or "")
    return TOPIC_CONSTRUCTOR_OVERRIDES.get(slug) or BRANCH_CONSTRUCTOR.get(branch_id, BRANCH_CONSTRUCTOR["annotations"])


def latex_derivation_depth_sections(template: Mapping[str, Any]) -> str:
    """Render optional consequences and transformations for any field wiki."""
    lines: List[str] = []
    for key, title in DERIVATION_DEPTH_SECTIONS:
        items = [clean_text(item, 700) for item in (template.get(key) or []) if clean_text(item)]
        if not items:
            continue
        lines.extend([rf"\subsection*{{{title}}}", latex_escape(prose_from_items(items, len(items)))])
    return "\n".join(lines)


def markdown_derivation_depth_sections(template: Mapping[str, Any]) -> str:
    """Markdown counterpart of :func:`latex_derivation_depth_sections`."""
    lines: List[str] = []
    for key, title in DERIVATION_DEPTH_SECTIONS:
        items = [clean_text(item, 700) for item in (template.get(key) or []) if clean_text(item)]
        if not items:
            continue
        lines.extend([f"## {title}", "", prose_from_items(items, len(items)), ""])
    return "\n".join(lines)


def center_equation_rows(tex: str) -> str:
    """Center every row in public multiline displays instead of right-aligning it."""
    pattern = re.compile(
        r"(\\begin\{centeredalign\})(.*?)(\\end\{centeredalign\})",
        flags=re.DOTALL,
    )

    def rewrite(match: re.Match[str]) -> str:
        body = re.sub(r"(?<!\\)&", "", match.group(2))
        return match.group(1) + body + match.group(3)

    return pattern.sub(rewrite, tex)


def derivation_basis(page: Mapping[str, Any], row: Mapping[str, Any], branch_id: str) -> str:
    """Classify evidential depth independently of topical specificity."""
    slug = str(row.get("slug") or "")
    v2 = row.get("v2_evidence") or {}
    source_grounded = bool(v2.get("available"))
    identifier_linked = v2.get("status") == "v2_identifier_linked"
    topic_model = has_topic_constructor(page, slug)
    return classify_derivation_basis(
        topic_model=topic_model,
        source_grounded=source_grounded,
        identifier_linked=identifier_linked,
        annotation=bool(branch_id == "annotations" or row.get("is_annotation")),
    )


def has_topic_constructor(page: Mapping[str, Any], slug: str) -> bool:
    """Return whether the page has topic-specific construction evidence.

    All pages can now be expanded as specializations of the compact quantum
    constructor.  This predicate is kept only to distinguish topic-specific or
    source-backed pages from pages that are expanded by the shared constructor
    spine.
    """
    mw = page.get("morphwiki") or {}
    if slug in TOPIC_CONSTRUCTOR_OVERRIDES:
        return True
    if mw.get("mathematical_skeleton_is_source_backed") or mw.get("mathematical_skeleton_is_topic_native"):
        return True
    return False


def page_mechanism_status(page: Mapping[str, Any], slug: str) -> str:
    if has_topic_constructor(page, slug):
        return "topic-specific mechanism"
    return "branch-level construction"


def page_constructor_status(root: Path, row: Mapping[str, Any]) -> str:
    page = load_json(page_path(root, str(row["slug"])))
    return page_mechanism_status(page, str(row.get("slug") or ""))


def split_constructed_pages(root: Path, pages: Sequence[Mapping[str, Any]]) -> tuple[List[Mapping[str, Any]], List[Mapping[str, Any]]]:
    constructed: List[Mapping[str, Any]] = []
    placements: List[Mapping[str, Any]] = []
    for row in pages:
        if page_constructor_status(root, row) == "constructed":
            constructed.append(row)
        else:
            placements.append(row)
    return constructed, placements


def top_constructor_index(evidence: Sequence[Mapping[str, Any]], hyperion: Mapping[str, Any]) -> Dict[str, str]:
    first = evidence[0] if evidence else {}
    invariant = str(first.get("invariant") or "")
    xi = re.search(r"(Ξ\d+)", invariant)
    family = re.search(r"(Λ\d+)", invariant)
    current = re.search(r"(J_[A-Za-z0-9_]+)", invariant)
    active_apparatus = hyperion.get("active_apparatus") or []
    apparatus = first.get("apparatus_regime") or (active_apparatus[0] if active_apparatus else "")
    omega = first.get("omega_tokens") or ""
    return {
        "xi": normalize_private_formula(xi.group(1) if xi else "Xi?"),
        "apparatus": normalize_private_formula(apparatus or "A?"),
        "omega": normalize_private_formula(omega or "O?"),
        "family": normalize_private_formula(family.group(1) if family else "L?"),
        "current": current.group(1) if current else "J_flat",
    }


def constructor_text(
    title: str,
    branch_id: str,
    row: Mapping[str, Any],
    hyperion: Mapping[str, Any],
    mw: Optional[Mapping[str, Any]] = None,
) -> Dict[str, str]:
    template = constructor_template(branch_id, row)
    slug = str(row.get("slug") or "")
    display = page_display_name(title)
    route_terms = ranked_keys(hyperion.get("route_profile") or {}, ROUTE_PUBLIC, 3)
    fiber_terms = ranked_keys(hyperion.get("fiber_profile") or {}, FIBER_PUBLIC, 3)
    route_sentence = ", ".join(route_terms) if route_terms else "no dominant public route"
    fiber_sentence = ", ".join(fiber_terms) if fiber_terms else "no dominant public fiber"
    mw = mw or {}
    native_source_backed = bool(
        mw.get("mathematical_skeleton_is_source_backed")
        or mw.get("mathematical_skeleton_is_topic_native")
    )
    native_reading = public_book_text(mw.get("mechanism_view")) if native_source_backed else ""
    native_claim = public_book_text(mw.get("takeaway")) if native_source_backed else ""
    generic_native = is_generic_native_constructor_text(native_reading) or is_generic_native_constructor_text(native_claim)
    source_specific = native_source_backed
    weak_claim = (
        not native_claim
        or "placed by route/fiber evidence" in native_claim.lower()
        or "complete mechanism names" in native_claim.lower()
        or "read through the compact quantum constructor" in native_claim.lower()
    )
    if slug in TOPIC_CONSTRUCTOR_OVERRIDES:
        claim = template["claim"].format(title=display)
        reading = template["reading"].format(title=display)
    elif native_reading and not generic_native:
        if weak_claim:
            native_claim = first_sentence(native_reading, 520)
        claim = native_claim or first_sentence(native_reading, 520)
        reading = native_reading
    elif source_specific:
        family_key = topic_family(slug, title)
        family = FAMILY_NATIVE_LANGUAGE[family_key]
        role = (
            BRANCH_PUBLIC_ROLE.get(branch_id, "formal role")
            if family_key == "general_quantum"
            else family["role"]
        )
        frame_rows = quantum_mechanism_frame_rows(title, branch_id, row, mw)
        frame = {key: value for key, value in frame_rows}
        claim = (
            f"{display} contributes {indefinite_article(role)} {role} to the quantum construction."
        )
        reading = (
            f"Its carrier or domain is {frame.get('Carrier or domain', 'not specified')}. "
            f"The relevant operator or map is {frame.get('Operator or map', 'not specified')}. "
            f"Its admissibility condition is {frame.get('Admissibility', 'not specified')}. "
            f"The resulting observable or prediction is {frame.get('Observable or prediction', 'not specified')}."
        )
    else:
        family_key = topic_family(slug, title)
        family = FAMILY_NATIVE_LANGUAGE[family_key]
        branch_role = BRANCH_CONSTRUCTOR.get(branch_id, BRANCH_CONSTRUCTOR["annotations"])
        branch_claim = branch_role["claim"].format(title=display)
        frame = mechanism_frame_for_page(slug, title, branch_id)
        claim = branch_claim
        known = (
            BRANCH_PUBLIC_DESCRIPTION.get(branch_id, family["known"])
            if family_key == "general_quantum"
            else family["known"]
        )
        reading = known
    if branch_id == "annotations" or row.get("is_annotation"):
        reading += (
            " Its constructive use is to identify which formal layer is being interpreted: state assignment, probability, update, observable, or ontology."
        )
    return {"claim": claim, "reading": reading}


def constructor_block(
    title: str,
    branch_id: str,
    row: Mapping[str, Any],
    hyperion: Mapping[str, Any],
    evidence: Sequence[Mapping[str, Any]],
    mw: Optional[Mapping[str, Any]] = None,
) -> str:
    template = constructor_template(branch_id, row)
    slug = str(row.get("slug") or "")
    mw = mw or {}
    if slug in TOPIC_CONSTRUCTOR_OVERRIDES:
        if not template.get("equation_note"):
            return ""
        lines = [
            r"\subsection*{Topic Equations}",
            latex_escape(
                str(
                    template.get("equation_note")
                    or (
                        "Role-level skeleton: a branch-level mechanism equation for checking the page's source evidence; source notation may differ."
                    )
                )
            ),
            r"\begin{centeredalign}",
        ]
        equations = list(template["equations"])
        for idx, equation in enumerate(equations):
            suffix = r"\\" if idx < len(equations) - 1 else ""
            lines.append(equation + suffix)
        lines.append(r"\end{centeredalign}")
        return "\n".join(lines)
    conversion = [public_book_text(item) for item in (mw.get("conversion_form") or []) if clean_text(item)]
    if conversion:
        return "\n".join(
            [r"\subsection*{Defining Relations}", latex_escape(prose_from_items(conversion, 6))]
        )
    else:
        lines = [
            r"\subsection*{Representative Relation}",
            latex_escape(
                "The equation identifies the state, operation, and observable relation associated with this physical role."
            ),
            r"\begin{centeredalign}",
            role_equation_for_page(slug, title, branch_id),
            r"\end{centeredalign}",
        ]
        return "\n".join(lines)


def constructed_support_for_branch(title: str, branch_id: str) -> tuple[List[str], List[str], List[str]]:
    """Human-readable support bullets for constructed pages.

    These are deliberately branch-specific and state what the page contributes
    to the quantum constructor in ordinary quantum language.
    """
    rules: Dict[str, tuple[List[str], List[str], List[str]]] = {
        "context": (
            [
                f"{title} supplies the admissible arena in which quantum states and operators are defined.",
                "Changing basis or representation should not change physical probabilities when the transformation is unitary.",
                "Normalization, domain conditions, and inner products remain part of the same formal container.",
            ],
            [
                "The chosen basis, coordinate representation, or preparation convention can change.",
                "The same calculation may be written with vectors, wave functions, density operators, or operator algebras.",
                "Physical realization enters later through boundary conditions, detectors, or fields.",
            ],
            [
                "Unitary changes of basis preserve Born probabilities; if probabilities change, the page has changed the physical context rather than only the representation.",
                "The operator domain and normalization conditions determine which questions are legal on the selected Hilbert space.",
                "Basis names are bookkeeping; inner products, spectra, and probabilities are the physical content that must survive the rewrite.",
            ],
        ),
        "states": (
            [
                f"{title} carries the predictive information before a measurement question is asked.",
                "The same physical preparation may be represented as a vector, wave function, density matrix, or reduced state.",
                "Normalization and positivity are the admissibility checks that make the state usable for probability readout.",
            ],
            [
                "The state representation can change between position, momentum, spin, occupation, or density-operator forms.",
                "Pure-state and mixed-state descriptions may differ while describing the same formal preparation.",
                "Subsystem descriptions change when degrees of freedom are traced out or ignored.",
            ],
            [
                "A usable state gives normalized probabilities for every complete readout attached to the selected Hilbert space.",
                "Vector, wave-function, density-matrix, and reduced-state forms can describe the same preparation when connected by the appropriate representation map.",
                "Physical state changes preserve positivity and trace, or norm in the pure closed-system limit.",
            ],
        ),
        "generators": (
            [
                f"{title} specifies lawful change before readout.",
                "The generator determines the propagator or path weight that carries the state between preparation and measurement.",
                "Conserved quantities and symmetries are read from the generator and its commutation relations.",
            ],
            [
                "Time dependence can be assigned to states, operators, propagators, or path amplitudes.",
                "Perturbative, Hamiltonian, Lagrangian, and path-integral presentations can represent the same evolution.",
                "Approximation schemes change the calculational route without changing the target transition amplitude.",
            ],
            [
                "Lawful closed-system evolution preserves norm or trace; open-system evolution must preserve positivity and trace under the stated approximation.",
                "The short-time and classical limits identify whether the generator has the correct physical regime.",
                "Hamiltonian, propagator, and path-integral forms are equivalent only when they yield the same transition amplitudes or correlation functions.",
            ],
        ),
        "observables": (
            [
                f"{title} defines the legal question being asked of the state.",
                "The measurable answers are encoded by the operator spectrum, projectors, or spectral measure.",
                "The operator role is preserved across equivalent bases even when matrix entries change.",
            ],
            [
                "The same observable may be represented by matrices, differential operators, projectors, or algebraic elements.",
                "Degeneracy, basis choice, and domain conditions can change how the spectrum is displayed.",
                "Detector implementation changes the physical realization, not the operator role itself.",
            ],
            [
                "Self-adjointness, or the appropriate POVM positivity condition, is what makes the question a legal readout.",
                "A complete spectral resolution supplies all outcome channels for the question being asked.",
                "Equivalent representations preserve expectation values and probability distributions.",
            ],
        ),
        "measurement": (
            [
                f"{title} connects the state and the spectral question to observed probabilities.",
                "The invariant step is the map from state plus measurement operators to a normalized probability distribution.",
                "Projection-valued and POVM readouts preserve the same role: outcome channels weighted by the state.",
            ],
            [
                "The detector model, basis, and update convention can change.",
                "State-vector, density-matrix, projective, and generalized-measurement forms may present the readout differently.",
                "Interpretive language about collapse or information update can vary without changing the probability rule.",
            ],
            [
                "Outcome probabilities are non-negative and normalized because the readout acts on a valid state with a complete effect family.",
                "Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors.",
                "The probability assignment is distinct from any optional post-measurement update convention.",
            ],
        ),
        "incompatibility": (
            [
                f"{title} identifies when otherwise legal quantum questions cannot be made jointly sharp.",
                "The stable object is the obstruction: non-commutation, non-factorization, contextuality, or failure of a joint assignment.",
                "The page belongs to the compatibility layer because it limits which spectra can be read together.",
            ],
            [
                "The obstruction may be written as a commutator, inequality, correlation bound, uncertainty relation, or contextuality test.",
                "Different experiments realize the same compatibility limit with different observables and detectors.",
                "The language of paradox can change while the formal obstruction remains.",
            ],
            [
                "A common eigenbasis or joint probability model exists only when the relevant compatibility conditions are satisfied.",
                "Commutators, uncertainty bounds, Bell inequalities, and contextuality tests are different forms of the same joint-readout obstruction.",
                "Classical joint-assignment failure is meaningful only under the explicitly stated locality, realism, or measurement-independence assumptions.",
            ],
        ),
        "boundaries": (
            [
                f"{title} shows how a context, domain, potential, or boundary changes the allowed quantum channels.",
                "The invariant role is boundary-shaped spectral selection: the operator is the same kind of object, but its domain changes.",
                "Transmission, confinement, scattering, and mode selection are read as consequences of admissible boundary conditions.",
            ],
            [
                "The potential, geometry, asymptotic condition, or detector arrangement can change.",
                "The same boundary role may appear as a box, barrier, cavity, interface, or scattering region.",
                "Changing the boundary can change the spectrum without changing the general quantum constructor.",
            ],
            [
                "The boundary changes the operator domain, and therefore the allowed modes, transmission amplitudes, or scattering channels.",
                "The same operator can have different spectra when the admissible domain changes.",
                "Removing the boundary recovers the appropriate free, infinite-domain, or asymptotic limit.",
            ],
        ),
        "fields": (
            [
                f"{title} extends the state-operator-spectrum constructor to many modes, fields, particles, gauge structure, or scale.",
                "Particle identity is treated as a stable excitation or representation role rather than as the starting object.",
                "Creation/annihilation, field operators, gauge constraints, and scale flow preserve operator structure across realizations.",
            ],
            [
                "The carrier can be a field state, occupation-number state, gauge orbit, spin network, or effective theory.",
                "The same formal role may be displayed through particles, modes, amplitudes, correlation functions, or boundary dictionaries.",
                "Scale and geometry can change the realization while preserving operator or spectral content.",
            ],
            [
                "Commutation, anticommutation, gauge, and occupation rules define which many-mode states are admissible.",
                "The field or many-mode construction must reduce to the appropriate single-particle, quasiparticle, or low-energy limit when those limits exist.",
                "Dual presentations are credible only when observables, spectra, or correlation functions are preserved across the translation.",
            ],
        ),
        "protocols": (
            [
                f"{title} turns the quantum constructor into an ordered operation sequence.",
                "The stable role is compositional: admissible maps transform an input state into an output state before readout.",
                "Unitary gates, channels, measurements, correction steps, and algorithms are protocolized versions of the same state-map-readout logic.",
            ],
            [
                "The implementation can be a circuit, channel, network, sensor, automaton, or cryptographic protocol.",
                "Noise, measurement timing, and correction rules change the realized map.",
                "Different hardware can implement the same abstract sequence of completely positive or unitary operations.",
            ],
            [
                "Each operation in the sequence is constrained by the map class it claims: unitary, completely positive, trace preserving, measurement, correction, or conditional update.",
                "The composed protocol is defined by its output state and readout probabilities, not only by the names of the gates.",
                "Changing operation order or replacing a quantum channel with a classical control identifies which part of the protocol carries the effect.",
            ],
        ),
        "annotations": (
            [
                f"{title} is retained as interpretive or historical context rather than as a constructor step.",
                "Its stable role is to clarify which formal layer is being discussed: state, probability, update, readout, or ontology.",
                "It is most useful when attached to the operator, spectrum, and probability machinery it interprets.",
            ],
            [
                "The wording of interpretation, pedagogy, or historical emphasis can change.",
                "The same formal equations can support different explanatory narratives.",
                "Popular terminology can obscure which constructor role is actually being modified.",
            ],
            [
                "The useful question is which formal layer the interpretation changes: state, probability, update, ontology, or readout.",
                "When the same equations and probabilities remain intact, the page belongs to the interpretive boundary of the formal constructor.",
                "A new physical law requires additional equations or empirical constraints beyond interpretive vocabulary.",
            ],
        ),
    }
    return rules.get(branch_id, rules["annotations"])


def support_lists_for_page(
    page: Mapping[str, Any],
    row: Mapping[str, Any],
    branch_id: str,
    constructed: bool,
) -> tuple[List[str], List[str], List[str]]:
    """Return support/variation/test bullets with a strict construction boundary."""
    mw = page.get("morphwiki") or {}
    slug = str(row.get("slug") or "")
    if slug in TOPIC_SUPPORT_OVERRIDES:
        return TOPIC_SUPPORT_OVERRIDES[slug]
    if not constructed:
        stable, variable, falsifiers = constructed_support_for_branch(page_display_name(page_title(page)), branch_id)
        family_key = topic_family(slug, page_title(page))
        family = FAMILY_NATIVE_LANGUAGE[family_key]
        stable = (
            [family["known"], *stable[:3]]
            if family_key != "general_quantum"
            else stable[:4]
        )
        variable = [
            "The local title, representation, and physical realization may change while the constructor role is preserved.",
            *variable[:3],
        ]
        falsifiers = [
            "The topic is physically defined by its state carrier, operator or map, observable consequence, and compatibility condition.",
            *falsifiers[:2],
        ]
        return (stable[:4], variable[:4], falsifiers[:3])

    survives = [public_book_text(item, 240) for item in (mw.get("what_survives") or []) if clean_text(item)]
    changes = [public_book_text(item, 240) for item in (mw.get("what_changes") or []) if clean_text(item)]
    tests = [public_book_text(item, 260) for item in (mw.get("missing_experiments") or []) if clean_text(item)]
    unresolved_markers = (
        "future constructor",
        "does not yet",
        "only the measured",
        "upgrade",
        "attach a topic-native",
        "promote the page",
        "shuffled topic assignment",
    )
    unresolved_survives = any(marker in " ".join(survives).lower() for marker in unresolved_markers)
    unresolved_changes = any(marker in " ".join(changes).lower() for marker in unresolved_markers)
    unresolved_tests = any(marker in " ".join(tests).lower() for marker in unresolved_markers)

    if survives and not unresolved_survives:
        stable = survives[:4]
    else:
        stable, _, _ = constructed_support_for_branch(page_display_name(page_title(page)), branch_id)

    if changes and not unresolved_changes:
        variable = changes[:4]
    else:
        _, variable, _ = constructed_support_for_branch(page_display_name(page_title(page)), branch_id)

    if tests and not unresolved_tests:
        falsifiers = tests[:3]
    else:
        template = constructor_template(branch_id, row)
        equation_note = clean_text(template.get("equation_note"))
        if slug in TOPIC_CONSTRUCTOR_OVERRIDES or equation_note:
            _, _, falsifiers = constructed_support_for_branch(page_display_name(page_title(page)), branch_id)
        else:
            falsifiers = [
                "The constructor is meaningful only if it fits this branch better than an alternative branch placement.",
                "The same formal role should survive a change of representation when the change is only notational.",
                "A source-backed equation upgrades the branch placement into a completed mechanism.",
            ]
    return stable, variable, falsifiers


def human_hidden_rule_basis(rule: Mapping[str, Any]) -> str:
    """Render a sparse-attention basis without exposing internal field names."""
    basis = str(rule.get("attention_basis") or "")
    evidence = rule.get("evidence") or {}
    if basis == "route_active_counts_gt_0_10 and route_means":
        return "The role appears broadly across the export rather than only inside one topic family."
    if basis == "branch-conditioned route mean minus global route mean":
        return "This branch carries the role more strongly than the corpus background."
    if basis == "normalized route entropy":
        return "These pages activate several constructor roles at once, so they behave as junctions rather than clean leaves."
    if basis == "constructed-vs-route-placement text and page status":
        return "The current export separates pages with topic-specific equations from pages expanded by the shared constructor spine."
    if basis == "annotation branch route profile":
        return "Interpretive and historical pages retain formal route signals, but their role is explanatory framing rather than equation construction."
    if basis == "repeated title-token family route profile":
        token = evidence.get("token")
        if token:
            return f"The repeated topic family around '{token}' shares a route profile strongly enough to form a local mechanism family."
        return "A repeated title family shares a route profile strongly enough to form a local mechanism family."
    if basis == "finding text plus boundary/field/context branch profile":
        return "This rule links the quantum tree to an independent source-equation finding and checks whether the relevant branches carry the same kind of signal."
    return "The rule is induced from a repeated sparse-attention pattern in the current export."


def human_hidden_rule_statement(rule: Mapping[str, Any]) -> str:
    """Render the rule itself as a scientific interpretation rather than a metric string."""
    name = str(rule.get("name") or "")
    evidence = rule.get("evidence") or {}
    route = str(evidence.get("route") or "").replace("_route", "").replace("_", " ")
    branch = str(evidence.get("branch") or "").replace("_", " ")
    if "broad spine role" in name and route:
        return (
            f"{route} behaves as a spine role in the current quantum rewrite. It should be introduced as part of the "
            "general constructor before specialist topics are derived from it."
        )
    if " is enriched for " in name and branch and route:
        return (
            f"The {branch} branch is a construction-role region where {route} becomes the "
            "dominant way the topic is made predictive."
        )
    if "High-entropy pages" in name:
        return (
            "Some pages cannot be explained by one constructor role. They are junction pages where state, transformation, "
            "readout, boundary, or compatibility must be separated before the page can become a derivation."
        )
    if "Route placement is easier" in name:
        return (
            "The rewrite can often locate a topic in the mechanism tree before it can construct the topic. This is useful: "
            "it marks where source equations are still needed."
        )
    if "annotation" in name.lower() or "interpretation" in name.lower():
        return (
            "Interpretive and historical pages retain formal signals, but they should orient the reader rather than define "
            "the constructive root of the theory."
        )
    statement = clean_text(rule.get("rule"))
    statement = re.sub(r"\b\d+(?:\.\d+)?\b", "", statement)
    statement = re.sub(r"\s+", " ", statement).strip(" .;")
    return statement or "This rule marks a repeated sparse-attention pattern in the current export."


def hidden_rule_public_blocks(rule: Mapping[str, Any]) -> List[tuple[str, str]]:
    """Render sparse-attention rules as quantum-mechanics claims.

    The JSON rule fields are useful for auditing, but many of them are written
    in metric language. The book states the scientific reading directly and
    omits internal diagnostic boundaries from public prose.
    """
    rid = str(rule.get("id") or "")
    evidence = rule.get("evidence") or {}
    branch = str(evidence.get("branch") or "")
    route = str(evidence.get("route") or "")
    token = str(evidence.get("title_token") or evidence.get("token") or "")

    by_id: Dict[str, List[tuple[str, str]]] = {
        "R01": [
            (
                "Reading",
                "The stable readout of a quantum construction is usually spectral.  A state becomes experimentally or mathematically predictive when an allowed operator question exposes eigenvalues, projectors, or a spectral measure.",
            ),
            (
                "Use",
                "Introduce observables, self-adjointness, spectral projectors, and the Born rule as the common readout interface before presenting particles, fields, or protocols as separate subjects.",
            ),
            (
                "Boundary",
                "The claim is role-specific: spectra are the most reusable readout layer in this export, while other roles supply state, evolution, context, and compatibility.",
            ),
        ],
        "R02": [
            (
                "Reading",
                "Quantum topics repeatedly require a lawful carrier of change: a state vector, density operator, field mode, or channel is propagated before it is read.",
            ),
            (
                "Use",
                "Derive state evolution as the map between preparation and later readout, using unitary, semigroup, or channel language depending on whether the system is closed, open, or operational.",
            ),
            (
                "Boundary",
                "Transport becomes meaningful after the admissible state space and the observable question have been specified.",
            ),
        ],
        "R03": [
            (
                "Reading",
                "Closure and admissibility form the legal spine of the theory: states must be normalizable or positive, maps must preserve the allowed state set, and operators must have a domain on which the question is well-defined.",
            ),
            (
                "Use",
                "Every derivation should state what makes the state, operator, map, or probability assignment legal before it discusses physical interpretation.",
            ),
            (
                "Boundary",
                "Admissibility is the formal condition that prevents the same symbols from representing an illegal quantum construction.",
            ),
        ],
        "R04": [
            (
                "Reading",
                "Incompatibility is selective.  It becomes central when two questions, bases, or transformations cannot be made sharp at the same time.",
            ),
            (
                "Use",
                "Use commutators, non-common eigenbases, Bell-type constraints, or contextuality tests only where the page is actually about jointly unavailable readouts.",
            ),
            (
                "Boundary",
                "Use non-commutation where jointly unavailable readouts are the active mechanism; many topics are dominated by state evolution, spectra, or admissibility instead.",
            ),
        ],
        "R05": [
            (
                "Reading",
                "Context is sometimes part of the law.  Preparation, boundary conditions, detector arrangement, basis choice, or representation can change which state and operator are admissible.",
            ),
            (
                "Use",
                "When context is active, write the context before the state: specify the Hilbert space, domain, boundary, apparatus, or channel that makes the later spectral question meaningful.",
            ),
            (
                "Boundary",
                "The mathematical question is defined only after its carrier and boundary conditions are fixed.",
            ),
        ],
        "R06": [
            (
                "Reading",
                "Protocols are a sparse but real layer.  They become central when an ordered sequence of operations, measurements, controls, or updates determines what can be inferred.",
            ),
            (
                "Use",
                "Place quantum algorithms, circuits, finite automata, Bell tests, and delayed-choice experiments in this layer: their content depends on operation order, not only on a static Hamiltonian.",
            ),
            (
                "Boundary",
                "A protocol realizes the state, operator, readout, and compatibility machinery in an ordered experiment or computation.",
            ),
        ],
        "R07": [
            (
                "Reading",
                "The observables branch is correctly centered on spectral questions.  Its pages ask which physical quantities can be represented by operators and which outcome channels those operators permit.",
            ),
            (
                "Use",
                "Read this branch through self-adjoint operators, spectral decompositions, projectors, expectation values, and the distinction between compatible and incompatible observables.",
            ),
            (
                "Boundary",
                "A quantity becomes a quantum observable when its operator domain and spectral readout are specified.",
            ),
        ],
        "R08": [
            (
                "Reading",
                "The incompatibility branch is unexpectedly protocol-like.  Bell tests, erasers, nonlocality arguments, and related pages depend on which questions are asked in which order and under which measurement arrangement.",
            ),
            (
                "Use",
                "Present these topics as experimental or logical sequences that expose incompatible readouts, rather than as isolated paradoxes.",
            ),
            (
                "Boundary",
                "The protocol does not replace the formal incompatibility; it is the way the incompatibility becomes observable.",
            ),
        ],
        "R09": [
            (
                "Reading",
                "Interpretation and history pages cluster around compatibility and readout problems.  They usually debate what the state, probability, or update means after the formal machinery has already produced a constrained readout.",
            ),
            (
                "Use",
                "Attach interpretations to the mechanism they reinterpret: state assignment, measurement update, probability, nonlocal correlations, or incompatible observables.",
            ),
            (
                "Boundary",
                "Interpretations should not be roots of the mechanism tree unless they supply a different formal constructor.",
            ),
        ],
        "R10": [
            (
                "Reading",
                "The context branch is where a spectral question becomes legally posed.  Hilbert space, basis, representation, operator domain, and preparation context are not background labels; they define the admissible state space on which operators can have spectra.",
            ),
            (
                "Use",
                "For pages such as Hilbert space or mathematical formulation, write the carrier first: choose the space, domain, inner product, and allowed states before asking for eigenvalues or probabilities.",
            ),
            (
                "Boundary",
                "The quantum question is well formed after the admissible carrier of the question has been supplied.",
            ),
        ],
        "R11": [
            (
                "Reading",
                "Engineered quantum protocols still depend on spectral structure.  Circuits, automata, sensors, and algorithms arrange allowed transformations so that a final readout exposes the desired spectral or probability information.",
            ),
            (
                "Use",
                "Describe protocols as controlled sequences of unitary maps, channels, measurements, and conditional updates, then identify what spectral or probability readout the sequence is designed to reveal.",
            ),
            (
                "Boundary",
                "The engineering layer packages the same constructor formally.",
            ),
        ],
        "R12": [
            (
                "Reading",
                "Some pages are junctions rather than leaves.  EPR, wave function, delayed-choice eraser, entanglement, quantum biology, and similar topics join state, evolution, readout, boundary, protocol, and compatibility in one place.",
            ),
            (
                "Reading consequence",
                "Such pages should be read as junctions of several formal roles: state carrier, transformation, readout, context, and compatibility condition. Their position marks where a single topic name covers more than one construction step.",
            ),
            (
                "Boundary",
                "A junction signals that the page should be decomposed before it is used as an explanatory root.",
            ),
        ],
        "R13": [
            (
                "Reading",
                "Role assignment is easier than full local derivation.  Sparse attention can often locate the constructor role of a page before the export contains a topic-specific equation skeleton.",
            ),
            (
                "Use",
                "Treat core-derived pages as specialization targets: specify their state/operator/readout roles, then decide whether they need a topic-specific equation or can remain a specialization of the compact constructor.",
            ),
            (
                "Boundary",
                "A constructor role assignment is evidence of formal similarity; a topic-specific derivation still requires local equations and controls.",
            ),
        ],
        "R14": [
            (
                "Reading",
                "Annotation pages still contain formal signal.  Historical and interpretive texts often preserve the same state, operator, probability, and compatibility vocabulary as technical pages.",
            ),
            (
                "Use",
                "Use these pages to explain why a mechanism mattered or how it was interpreted, but attach them downstream of the formal constructor they discuss.",
            ),
            (
                "Boundary",
                "A strong annotation signal is an orientation cue; independent equation evidence remains the source for derivation.",
            ),
        ],
        "R15": [
            (
                "Reading",
                "The word operator is not one mechanism.  Unitary operators transport states, self-adjoint operators define observable spectra, and angular-momentum operators carry symmetry and incompatibility structure.",
            ),
            (
                "Use",
                "Split operator pages by role rather than by title: generator of evolution, observable question, symmetry generator, algebraic constraint, or protocol component.",
            ),
            (
                "Boundary",
                "A shared word is an index term; physical equivalence requires matching role structure.",
            ),
        ],
        "R16": [
            (
                "Reading",
                "The Schrödinger family separates into distinct constructor roles.  The equation is a generator of state evolution, the picture is a representation choice, the cat is a protocol/readout junction, and the biography is an annotation.",
            ),
            (
                "Use",
                "Separate the Schrödinger equation, Schrödinger picture, Schrödinger's cat, and historical material by the role each performs in the constructor.",
            ),
            (
                "Boundary",
                "The shared name is resolved by the role each page performs.",
            ),
        ],
        "R17": [
            (
                "Reading",
                "Physics-labeled pages split into field realizations, scaling regimes, annotation pages, and constructor junctions depending on how state, operator, boundary, and readout appear.",
            ),
            (
                "Use",
                "Ask what each physics-labeled page does: does it define a carrier, a generator, a spectrum, a compatibility limit, or a realization domain?",
            ),
            (
                "Boundary",
                "Mechanism placement follows state, operator, boundary, and readout roles rather than discipline labels.",
            ),
        ],
        "R18": [
            (
                "Reading",
                "Equation-named pages separate by state carrier, symmetry constraints, admissible domains, and relativistic or field-theoretic realization.",
            ),
            (
                "Use",
                "Derive each equation by stating its state space, generator, conserved or constrained quantities, and readout role instead of grouping all equations as a single topic type.",
            ),
            (
                "Boundary",
                "The word equation identifies a presentation form; the mechanism is determined by the role performed by the page.",
            ),
        ],
        "R19": [
            (
                "Reading",
                "The Heisenberg family separates representation, uncertainty, historical annotation, and operator dynamics. Its unity comes from the recurring role of non-commuting observables and time-dependent operators.",
            ),
            (
                "Use",
                "Place Heisenberg-picture pages with generators and representations; place uncertainty and matrix mechanics pages with compatibility and observable algebra.",
            ),
            (
                "Boundary",
                "A named tradition should not collapse distinct constructor roles.",
            ),
        ],
        "R20": [
            (
                "Reading",
                "Introductory pages are compressed junctions.  They mix state, generator, observable, probability, interpretation, and examples because they are written pedagogically rather than mechanistically.",
            ),
            (
                "Use",
                "Use introductions as maps, then redistribute their content into the mechanism tree before treating any paragraph as a derivation.",
            ),
            (
                "Boundary",
                "Pedagogical order and construction order answer different questions.",
            ),
        ],
        "R21": [
            (
                "Reading",
                "Network-labeled pages split into physical networks, computational networks, and graph-like state structures.  The title word hides different roles of connectivity, protocol, and state space.",
            ),
            (
                "Use",
                "Ask whether the network is a physical realization, a computational protocol, an entanglement structure, or an abstract graph used to define admissible transformations.",
            ),
            (
                "Boundary",
                "Connectivity language must be paired with carrier, operator, and readout evidence to infer a common mechanism.",
            ),
        ],
        "R22": [
            (
                "Reading",
                "Geometry enters mainly through realization-heavy branches.  In this export, geometric language most often specifies boundary, field, context, or reconstruction layers rather than replacing the operator-spectral core.",
            ),
            (
                "Use",
                "Introduce geometry when the theory needs a domain, boundary, metric, representation, field realization, or reconstruction map.  Keep the operator and admissibility structure visible underneath.",
            ),
            (
                "Boundary",
                "Physical geometry supplies embodiment and boundary conditions; in the current artifacts it is less portable than the operator/readout machinery.",
            ),
        ],
    }
    if rid in by_id:
        return by_id[rid]

    if "broad spine role" in str(rule.get("name") or ""):
        return [
            (
                "Reading",
                f"{route.replace('_route', '').replace('_', ' ')} behaves as a reusable constructor role across the quantum export.",
            ),
            (
                "Use",
                "Introduce it as part of the core derivation rather than as a specialist topic.",
            ),
            (
                "Boundary",
                "The rule is an artifact-level sparse-attention claim until checked against source equations.",
            ),
        ]
    if branch:
        return [
            (
                "Reading",
                f"The {branch.replace('_', ' ')} branch carries a distinctive constructor role in the current export.",
            ),
            (
                "Use",
                "Read the branch by the formal role its pages perform, not by the conventional topic label.",
            ),
            (
                "Boundary",
                "A branch-level rule gives a first mechanism reading; page-level equations supply the finer test.",
            ),
        ]
    if token:
        return [
            (
                "Reading",
                f"The repeated title family around {token!r} is a linguistic cluster, but the mechanism tree separates its pages by role.",
            ),
            (
                "Use",
                "Split the pages by state, generator, observable, readout, boundary, or protocol function.",
            ),
            (
                "Boundary",
                "A shared title token is an index term; role structure supplies the equivalence test.",
            ),
        ]
    return [
        (
            "Reading",
            human_hidden_rule_statement(rule),
        ),
        (
            "Boundary",
            "The rule is an artifact-level sparse-attention claim that becomes stronger when checked against source equations.",
        ),
    ]


def hidden_rule_public_title(rule: Mapping[str, Any]) -> str:
    """Human-facing title for a sparse-attention rule."""
    rid = str(rule.get("id") or "")
    titles = {
        "R01": "Operator-to-spectrum as the readout spine",
        "R02": "State transport as the carrier of change",
        "R03": "Admissibility as the legal spine",
        "R04": "Incompatibility as a selective limit",
        "R05": "Context as the active boundary of the question",
        "R06": "Protocol as ordered implementation",
        "R07": "Observables are spectral questions",
        "R08": "Incompatibility becomes visible through protocols",
        "R09": "Interpretations attach to readout conflicts",
        "R10": "Context makes spectra well-defined",
        "R11": "Engineered protocols package spectral questions",
        "R12": "Junction pages require decomposition",
        "R13": "Placement precedes derivation",
        "R14": "Annotation pages preserve formal signal",
        "R15": "Operator pages split by role",
        "R16": "Schrödinger pages split by role",
        "R17": "Physics labels hide different roles",
        "R18": "Equation pages split by mechanism",
        "R19": "Heisenberg pages split by role",
        "R20": "Introductions are compressed maps",
        "R21": "Network pages split by role",
        "R22": "Geometry enters as realization",
    }
    if rid in titles:
        return titles[rid]
    name = clean_text(rule.get("name"))
    name = re.sub(r"Repeated title token '([^']+)' decomposes into route roles", r"\1 pages split by role", name)
    return name or "Sparse-attention rule"


def anomaly_public_summary(labels: Sequence[Any]) -> str:
    names = [ANOMALY_PUBLIC_NAMES.get(str(label), str(label).replace("-", " ")) for label in labels if label]
    if not names:
        return "structural junction"
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return ", ".join(names[:-1]) + f", and {names[-1]}"


def anomaly_public_explanation(item: Mapping[str, Any]) -> str:
    slug = str(item.get("slug") or "").lower()
    branch = str(item.get("branch") or "")
    secondary = str(item.get("secondary") or "")
    routes = item.get("routes") or {}
    top_routes = ranked_keys(routes, ROUTE_PUBLIC, limit=3, threshold=0.0)
    route_text = ", ".join(top_routes) if top_routes else "several constructor roles"
    specific = {
        "einstein_podolsky_rosen_paradox": (
            "EPR is a compatibility test, not a page about a peculiar object. Its mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and the allowed local observables; the question is which correlation constraints fail."
        ),
        "quantum_biology": (
            "Quantum biology is an open-system transfer problem. The anomaly is that the biological environment is not background noise only; it is part of the boundary that may preserve, destroy, or select coherence. The unresolved formal fields are the state carrier, environmental coupling, coherence or transport observable, and the classical control that would remove the quantum contribution."
        ),
        "measurement_problem": (
            "The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and the rule used to condition the state after the record."
        ),
        "quantum_gravity": (
            "Quantum gravity is a field/boundary junction. It asks whether geometry itself becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are explicit: a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test showing which geometric quantities survive quantization."
        ),
        "scattering": (
            "Scattering is a boundary-to-spectrum mechanism. The relevant object is the map from asymptotic in-states to out-states, together with the interaction region, boundary or asymptotic channels, S-matrix or cross-section readout, and conservation constraints."
        ),
        "quantum_state": (
            "Quantum state is the carrier, not the final prediction. It is anomalous because it precedes several downstream roles: admissibility, evolution, observable choice, and probability readout. The unresolved distinction is whether the carrier is a vector, density operator, field state, or register, and which transformations preserve its legality."
        ),
        "schr_dinger_s_cat": (
            "Schrödinger's cat is a macroscopic readout protocol, not a spectrum-first topic. It couples microscopic unitary evolution to a macroscopic boundary and forces the reader to separate three steps: coherent state transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned."
        ),
        "wave_particle_duality": (
            "Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel."
        ),
        "quantum_entanglement": (
            "Entanglement is a tensor-factorization and correlation constraint. The anomaly is that the state is not reducible to independently readable subsystem states, while the readout is still local and spectral. The required distinction is between joint state, subsystem observables, and correlation test."
        ),
        "fermi_dirac_statistics": (
            "Fermi-Dirac statistics is an admissibility rule for many-particle states. The central mechanism is antisymmetry and occupation restriction, not an ordinary eigenvalue list. The formal content is anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space."
        ),
        "hamiltonian_quantum_mechanics": (
            "The Hamiltonian has two roles at once: it generates time evolution and, when treated as an observable, supplies an energy spectrum. That double role explains the anomaly. A clean page must separate domain/self-adjointness, unitary transport, conserved energy, and spectral readout."
        ),
        "wave_function": (
            "The wave function is a representation of the state carrier, not a material wave by itself. Its anomaly is that it stores amplitude, phase, normalization, basis choice, and probability potential in one object. The formal decomposition separates representation, admissibility, evolution, and Born readout."
        ),
        "delayed_choice_quantum_eraser": (
            "The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The anomaly is not retrocausality by default; it is that the relevant statistics are defined only after the full measurement protocol is specified."
        ),
        "introduction_to_quantum_mechanics": (
            "An introductory page is anomalous because pedagogy compresses the whole formal sequence into one narrative. It mixes states, operators, spectra, measurement, examples, and interpretations. Its technical content separates into the individual branches before supporting specific derivations."
        ),
        "quantum_simulator": (
            "A quantum simulator is an engineered realization of another Hamiltonian or channel. The anomaly is that the page is both an observable system and a protocol for representing a different system. The formal fields are the simulated target, physical carrier, encoding map, and validation observable."
        ),
        "quantum_cellular_automaton": (
            "A quantum cellular automaton is a locality-preserving update rule. It sits between Hilbert-space context and generator dynamics because the lattice, neighborhood rule, unitarity or channel condition, and update protocol all define the mechanism together."
        ),
        "relativistic_quantum_mechanics": (
            "Relativistic quantum mechanics is a compatibility junction between quantum state evolution and spacetime symmetry. Its construction preserves relativistic covariance, defines the correct state carrier, and explains how spin, energy, and causality constraints enter the operator algebra."
        ),
        "quantum_electrodynamics": (
            "Quantum electrodynamics is a field-interaction construction. Its anomaly comes from combining gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. The relevant formal objects are field operators, gauge constraints, interaction terms, and observable amplitudes."
        ),
    }
    if slug in specific:
        return specific[slug]

    labels = item.get("labels") or item.get("anomaly_labels") or []
    label_set = {str(label) for label in labels}
    if branch == "fields":
        return (
            f"This field-level page mixes {route_text}. It is a many-mode or geometric realization problem: state sector or field algebra, constraints, and observable readout determine the field content."
        )
    if branch == "boundaries":
        return (
            f"This boundary page mixes {route_text}. Its formal effect is a change in domain, interface, potential, or asymptotic channel that changes the allowed readout."
        )
    if branch == "measurement":
        return (
            f"This measurement page mixes {route_text}. Its formal components are the state before readout, the detector or measurement map, the recorded outcome, and the update or conditioning rule."
        )
    if branch == "incompatibility":
        return (
            f"This incompatibility page mixes {route_text}. It identifies which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure."
        )
    if branch == "states":
        return (
            f"This state page mixes {route_text}. It requires the state carrier, representation, evolution, admissibility, and later readout as separate fields."
        )
    if branch == "protocols":
        return (
            f"This protocol page mixes {route_text}. Its formal content is an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters."
        )
    if "branch-ambiguous" in label_set and secondary:
        return (
            f"This page sits between {branch} and {secondary}. The ambiguity marks a place where two formal roles meet and require separate treatment before the page supports a derivation."
        )
    return (
        f"This page activates {route_text}. It is a formal junction until a topic-native derivation identifies its state carrier, transformation, readout, and compatibility condition."
    )


def validation_layers_chapter(root: Path) -> str:
    discoveries = root.parent
    noether = load_optional_json(discoveries / "self_cognition_lab" / "noether_tau_gw_self_cognition.json")
    lagrangian = load_optional_json(discoveries / "lagrangian_landscape" / "lagrangian_landscape_report.json")
    atlas_lagrangian = load_optional_json(discoveries / "operational_geometry" / "atlas_void_lagrangian_report.json")

    currents = ((noether.get("currents") or {}).get("level5_validation") or {})
    per_fiber = currents.get("per_fiber") or {}
    count_ledger = ((noether.get("currents") or {}).get("count_ledger") or {})
    funnel = noether.get("gw_tau_noether_bridge_funnel") or {}
    learned = lagrangian.get("learned_lagrangian") or {}
    diagnostics = lagrangian.get("diagnostics") or {}
    landscape = lagrangian.get("landscape_properties") or {}
    atlas_summary = atlas_lagrangian.get("summary") or {}
    occupancy = atlas_summary.get("occupancy") or {}
    territory_counts = atlas_summary.get("territory_counts") or {}
    path_counts = (
        atlas_summary.get("path_class_counts")
        or diagnostics.get("path_class_counts_all")
        or landscape.get("path_class_counts")
        or {}
    )

    structure_std = (per_fiber.get("structure") or {}).get("mean_relative_std")
    spectral_std = (per_fiber.get("spectral") or {}).get("mean_relative_std")
    geometry_std = (per_fiber.get("geometry") or {}).get("mean_relative_std")
    strict_currents = count_ledger.get("strict_promoted_noether_like_currents", currents.get("strict_promoted", learned.get("n_promoted", "?")))
    near_currents = count_ledger.get("near_currents", currents.get("near_only", learned.get("n_near_promoted", "?")))
    gw_candidates = funnel.get("gw_candidate_count", "?")
    hardened = funnel.get("hardened_gw_bridge_count", "?")
    validated = funnel.get("validated_method_bridge_count", diagnostics.get("validated_bridge_count", "?"))
    occupied = occupancy.get("occupied_cells", "?")
    total = occupancy.get("total_cells", "?")
    empty_percent = occupancy.get("empty_percent")

    lines: List[str] = [
        r"\chapter{Mechanism Validation Layers}",
        r"\begin{claimbox}",
        latex_escape(
            "The mechanism tree is evaluated by three independent evidence layers: "
            "role-current stability asks what survives a rewrite, Gromov-Wasserstein (GW) neighborhoods measure relational bridge candidates, "
            "and the learned Lagrangian asks whether a proposed move is an easy continuation, "
            "a strained bridge, or a void-boundary design target."
        ),
        r"\end{claimbox}",
        r"\section{Role-Current Layer: What Stays Stable}",
    ]
    lines.append(
        latex_escape(
            "The role-current layer measures stability of formal roles under rewrite and translation. "
            "When a theory is rewritten, translated, or moved through the corpus, the test asks which part of the formal apparatus keeps its role. "
            "For a mechanism tree, this is the identity test: two formulations belong together when the same role contract survives the move."
        )
    )
    lines.append(r"\begin{itemize}")
    lines.append(
        r"\item "
        + latex_escape(
            f"The run promoted {strict_currents} strict currents and {near_currents} near currents. These mark role-preserving directions in the learned representation."
        )
    )
    if structure_std is not None:
        lines.append(
            r"\item "
            + latex_escape(
                f"Structure is the cleanest invariant: formula architecture is conserved in all six probes, with mean relative variation {float(structure_std):.3f}."
            )
        )
    if spectral_std is not None:
        lines.append(
            r"\item "
            + latex_escape(
                f"Spectral/operator content is partly conserved, with mean relative variation {float(spectral_std):.3f}; this supports placing spectral questions at the spine of the quantum mechanism."
            )
        )
    if geometry_std is not None:
        lines.append(
            r"\item "
            + latex_escape(
                f"Geometry is not conserved in these probes, with mean relative variation {float(geometry_std):.3f}; this supports treating barriers, boxes, gauges, and fields as realization layers rather than the invariant root."
            )
        )
    lines.append(r"\end{itemize}")

    lines.extend([r"\section{Structural Bridge Layer: Candidate Translations}"])
    lines.append(
        latex_escape(
            "The Gromov-Wasserstein layer compares relational neighborhoods. It contributes a structural bridge score: "
            "two formulations are stronger bridge candidates when their local neighborhoods preserve comparable relations among roles. "
            "In the current constructor, this layer is combined with typed transfer edges, bridge-family candidates, source-local transitions, and source-equation validation."
        )
    )
    lines.append(r"\begin{itemize}")
    lines.append(
        r"\item "
        + latex_escape(
            f"The run scanned {gw_candidates} Gromov-Wasserstein candidates, hardened {hardened} bridge records, and retained {validated} artifact-validated method bridges."
        )
    )
    gate_counts = funnel.get("gate_counts") or {}
    transition_passed = (gate_counts.get("transition_gate") or {}).get("passed")
    directed_passed = (gate_counts.get("directed_gate") or {}).get("passed")
    equation_passed = (gate_counts.get("equation_gate") or {}).get("passed")
    if transition_passed is not None:
        lines.append(
            r"\item "
            + latex_escape(
                f"The narrowest gate is observed transition: {transition_passed} candidates pass the transition-observation gate, while {directed_passed} pass directedness and {equation_passed} pass representative-equation availability."
            )
        )
    lines.append(
        r"\item "
        + latex_escape(
            "GW nominates relationally compatible bridge candidates; typed transfer edges, directed source transitions, source equations, and residual checks rank them for use."
        )
    )
    lines.append(r"\end{itemize}")

    lines.extend([r"\section{Lagrangian Layer: Which Moves Are Easy Or Strained}"])
    lines.append(
        latex_escape(
            "The learned Lagrangian is the navigation layer of the atlas. It is a representation-space action surrogate over source-equation fingerprints, separate from the physical action of a quantum system. "
            "Given a construction-role state, it asks which next states are cheap continuations, which require a strained bridge, and which absences sit on a meaningful void front. "
            "In this sense it finds roads through the formal grammar: low-action corridors where a formal role can be continued, translated, or tested. "
            "In the current quantum tree this layer supplies the global road-map constraint. A full page-coordinate export will allow direct page-level action scoring."
        )
    )
    lines.append(r"\begin{itemize}")
    if occupied != "?":
        empty_phrase = f"{float(empty_percent):.1f}%" if isinstance(empty_percent, (int, float)) else "most"
        lines.append(
            r"\item "
            + latex_escape(
                f"The atlas occupies {occupied} of {total} cells; {empty_phrase} of the discrete grammar is empty in this run. This is a sparsity result, not a no-go theorem. A blank cell only means that the corpus has not supplied aligned apparatus, route, fiber, boundary, and transition evidence for that combination."
            )
        )
        lines.append(
            r"\item "
            + latex_escape(
                "Most empty cells are inert search space. The Lagrangian is useful because it does not treat all emptiness equally: an empty cell becomes testable only when it lies next to a low-action road, a validated bridge, or a void boundary with compatible surrounding evidence."
            )
        )
    if path_counts:
        labels = {
            "canonical_transfer_path": "low-action transfer paths",
            "canonical_multiband_transfer_path": "multi-band transfer paths",
            "local_formal_rewrite_or_near_duplicate": "local rewrites or near duplicates",
            "review_required": "high-tension review paths",
            "void_boundary_candidate": "void-boundary design targets",
        }
        road_parts = []
        for key in (
            "canonical_transfer_path",
            "canonical_multiband_transfer_path",
            "local_formal_rewrite_or_near_duplicate",
            "review_required",
            "void_boundary_candidate",
        ):
            if key in path_counts:
                road_parts.append(f"{path_counts[key]} {labels[key]}")
        if road_parts:
            lines.append(
                r"\item "
                + latex_escape(
                    "In this run the road map contains " + ", ".join(road_parts) + ". Low-action paths are stable continuations; multi-band paths are translation corridors; high-tension paths require review; void-boundary targets are candidates for new equations or missing closure conditions."
                )
            )
    if territory_counts:
        lines.append(
            r"\item "
            + latex_escape(
                "The territory map separates local formal regions, low-action transfer valleys, multi-band saddles, rough boundaries, strict void boundaries, and void-boundary design targets. This is why the Lagrangian is stronger than an occupancy statistic: it adds direction, resistance, and priority."
            )
        )
    lines.append(
        r"\item "
        + latex_escape(
            "For the quantum tree, the Lagrangian is therefore a construction constraint rather than a leaf selector. It tells how open construction steps should be interpreted in the atlas, but the present export cannot yet say that a particular Wikipedia page lies on a particular low-action road. That requires full fingerprints or witness transition vectors for the page."
        )
    )
    lines.append(r"\end{itemize}")

    lines.extend([r"\section{How These Layers Change The Quantum Tree}"])
    lines.append(
        latex_escape(
            "A quantum concept is not placed by name alone. It is placed by the role it plays in the mechanism, checked against source equation witnesses, "
            "and interpreted through stability and transfer layers. If a page preserves structure and spectral role, it belongs near the spine. If it changes the admissible domain, it belongs in boundary realization. "
            "If it introduces many modes or scale flow, it belongs in the field/scaling extension. If it describes a sequence of controlled operations, it belongs in the protocol layer."
        )
    )
    lines.append(
        latex_escape(
            "This is the human-readable reason for the tree: it unfolds quantum theory as a construction, then asks which parts survive when notation, representation, geometry, or field changes."
        )
    )
    return "\n".join(lines)


def sparse_attention_results_chapter(root: Path) -> str:
    report = load_optional_json(root / "sparse_attention" / "morphwiki_quantum_sparse_attention.json")
    if not report:
        return ""
    summary = report.get("summary") or {}
    simplified = report.get("simplified_constructor") or {}
    route_means = summary.get("route_means") or {}
    route_counts = summary.get("route_active_counts_gt_0_10") or {}
    hidden_rules = report.get("hidden_rules") or []
    lens_readings = report.get("lens_readings") or []
    lens_by_id = {row.get("lens_id"): row for row in lens_readings}

    route_names = {
        "transport_flow_route": "state evolution",
        "constraint_closure_route": "admissibility and closure",
        "spectral_operator_route": "observable spectra",
        "boundary_weak_form_route": "preparation and boundary context",
        "commutator_incompatibility_route": "incompatible questions",
        "discrete_protocol_route": "controlled update protocol",
    }

    lines: List[str] = [
        r"\chapter{Sparse-Attention Result}",
        r"\begin{claimbox}",
        latex_escape(
            simplified.get("one_sentence")
            or "Sparse attention collapses the quantum tree into a state, operator, spectrum, probability, compatibility, and boundary constructor."
        ),
        r"\end{claimbox}",
    ]
    collapse = simplified.get("what_collapses")
    if collapse:
        lines.append(latex_escape(collapse))

    constructor = simplified.get("minimal_constructor") or []
    if constructor:
        lines.extend(
            [
                r"\section{Minimal Constructor}",
                latex_escape(
                    "The sparse-attention run returns the same constructor as a role sequence. Rendered in standard quantum notation, the sequence is:"
                ),
                r"\begin{centeredalign}",
                r"B &\longmapsto (\mathcal H_B,\mathcal D_B)\\",
                r"\rho_B(t) &= U_B(t)\rho_B(0)U_B(t)^\dagger\\",
                r"O_B &= \sum_i \lambda_i P_i\qquad\text{or, more generally,}\qquad O_B=\int_{\sigma(O_B)}\lambda\,dE_{O_B}(\lambda)\\",
                r"p_i &= \operatorname{Tr}\!\left(P_i\rho_B(t)\right),\qquad \Pr(\Delta)=\operatorname{Tr}\!\left(\rho_B(t)E_{O_B}(\Delta)\right)\\",
                r"[O_1,O_2]\ne 0 &\quad\Rightarrow\quad \text{no generic common sharp readout}\\",
                r"\mathcal R &:\ \text{boundary, field, detector, circuit, or scaling realization.}",
                r"\end{centeredalign}",
                r"\begin{itemize}",
                r"\item \(B\) denotes the context: preparation, basis, boundary, domain, gauge, or detector arrangement.",
                r"\item \((\mathcal H_B,\mathcal D_B)\) is the admissible state space and operator domain selected by that context.",
                r"\item \(\rho_B(t)\) is the propagated state carrier.",
                r"\item \(O_B\), \(P_i\), and \(E_{O_B}\) express the observable question and its spectral readout channels.",
                r"\item The probabilities \(p_i\) or \(\Pr(\Delta)\) are Born-rule readouts of the state against those channels.",
                r"\item Non-commuting observables define compatibility limits; realization layers specify how the same role is embodied.",
                r"\end{itemize}",
            ]
        )

    lines.extend(
        [
            r"\section{Route Statistics}",
            r"\begin{longtable}{p{0.42\textwidth}rr}",
            r"\toprule",
            r"Role & Mean signal & Pages \(>0.10\) \\",
            r"\midrule",
        ]
    )
    for key, name in route_names.items():
        lines.append(rf"{latex_escape(name)} & {float(route_means.get(key, 0.0)):.3f} & {int(route_counts.get(key, 0))} \\")
    lines.extend([r"\bottomrule", r"\end{longtable}"])
    lines.append(
        latex_escape(
            "The strongest recurrent signal is observable spectra. In the current export it is active above threshold on nearly every page, while protocol/update is much sparser. This is the quantitative reason the tree begins with state, generator, observable, spectrum, and readout before it introduces algorithms, experiments, or interpretations."
        )
    )

    regularity_ids = ["R01", "R02", "R03", "R04", "R05", "R06", "R12", "R22"]
    rules_by_id = {str(rule.get("id")): rule for rule in hidden_rules}
    regularities = [rules_by_id[rid] for rid in regularity_ids if rid in rules_by_id]
    lines.extend([r"\section{Constructor Regularities}"])
    lines.append(
        latex_escape(
            "The regularities below are the strongest reusable patterns in the sparse-attention export. "
            "They are public reading rules for the quantum book, not internal diagnostics or a fixed ontology. "
            "Title-token rules and other lexical artifacts are omitted here because they are useful for auditing but too weak for the main exposition."
        )
    )
    for rule in regularities:
        lines.append(rf"\subsection{{{latex_escape(hidden_rule_public_title(rule))}}}")
        for label, text in hidden_rule_public_blocks(rule):
            if label == "Boundary":
                continue
            if label == "Use":
                label = "Reading consequence"
            if label:
                lines.append(rf"\paragraph{{{latex_escape(label)}.}} {latex_escape(text)}")
            else:
                lines.append(latex_escape(text))

    lines.extend([r"\section{Topic-Specific Readings}", r"\begin{itemize}"])
    for lens_id, label in [
        ("particle", "Particle"),
        ("black_hole", "Black-hole direction"),
        ("string_theory", "String-theory direction"),
        ("measurement", "Measurement and interpretations"),
        ("geometry", "Geometry"),
        ("voids", "Void leads"),
    ]:
        row = lens_by_id.get(lens_id) or {}
        claim = row.get("claim")
        unusual = row.get("unusual_observation")
        pages = ", ".join(row.get("top_pages") or [])
        body = public_book_text(" ".join(part for part in [claim, unusual, f"Relevant pages: {pages}." if pages else ""] if part))
        if body:
            lines.append(rf"\item \textbf{{{latex_escape(label)}}}: {latex_escape(body)}")
    lines.append(r"\end{itemize}")
    lines.append(
        latex_escape(
            "These statements are role hypotheses produced by deterministic sparse attention over the quantum page archive and existing source-equation findings. They are not final physics claims. The next test is to rerun the same analysis on explicit black-hole, horizon, Hawking-radiation, entropy, holography, and information-loss topics with typed equation witnesses."
        )
    )
    return "\n".join(lines)


def _legacy_compact_operator_formulation_chapter() -> str:
    """Human-readable compact formulation used as the book spine."""
    lines: List[str] = [
        r"\chapter{Compact Operator Formulation}",
        r"\begin{claimbox}",
        latex_escape(
            "The compact form of nonrelativistic quantum theory is a typed carrier-operator identity with closure and readout attached where a prediction requires them."
        ),
        r"\end{claimbox}",
        latex_escape(
            "This chapter is the formal spine of the book. It does not impose one temporal sequence on every derivation. Each later page is placed by asking which part of the typed identity it specifies, which completion condition it adds, and which realization it changes."
        ),
        r"\section{The Minimal Constructor}",
        r"\begin{centeredalign}",
        r"C &\longmapsto (\mathcal H_C,\mathcal D_C)\\",
        r"\rho &\in \mathcal S(\mathcal H_C),\qquad \rho\ge 0,\quad \operatorname{Tr}\rho=1\\",
        r"\rho_t &= U_C(t)\rho U_C(t)^\dagger,\qquad U_C(t)=\exp(-iH_Ct/\hbar)\\",
        r"A_C &= \int_{\sigma(A_C)} \lambda\,dE_{A_C}(\lambda)\\",
        r"\Pr(\Delta\mid C,\rho,A) &= \operatorname{Tr}\!\left(\rho_t\,E_{A_C}(\Delta)\right)\\",
        r"[A_C,B_C]\ne 0 &\quad\Rightarrow\quad \text{no generic common sharp spectral refinement.}",
        r"\end{centeredalign}",
        r"\section{Interpretation Of The Symbols}",
        r"\begin{itemize}",
        r"\item \(C\) is the context: preparation, basis, boundary condition, gauge choice, detector arrangement, domain, or representation.",
        r"\item \(\mathcal H_C\) is the admissible state space selected by that context.",
        r"\item \(\mathcal D_C\) is the domain or admissibility condition for the generator and observables.",
        r"\item \(\rho\) is the predictive state carrier. It may be a state vector, density operator, field state, or register state.",
        r"\item \(H_C\) is the generator of lawful change before readout.",
        r"\item \(A_C\) is the question being asked. Its spectral measure \(E_{A_C}\) supplies the outcome channels.",
        r"\item \(\Pr(\Delta\mid C,\rho,A)\) is the Born probability of an outcome set \(\Delta\).",
        r"\item A non-zero commutator marks a compatibility limit: two legal questions may not share one sharp readout basis.",
        r"\end{itemize}",
        r"\section{Identity, Completion, And Realization}",
        latex_escape(
            "The carrier and operator apparatus are jointly typed: an operator has a domain on a carrier, while the carrier determines which operators and states are admissible. Closure, readout, and protocol are attached completion modes. A boundary, field representation, detector, or circuit is a realization of this structure rather than a later universal stage."
        ),
        r"\begin{centeredalign}",
        r"\mathcal I_Q &= \bigl((\mathcal H_C,\mathcal D_C),\,\mathcal O_C\bigr) && \text{typed identity}\\",
        r"\mathcal F_Q &= \bigl(\mathcal K_C,\,\mathcal E_C,\,\mathcal P_C\bigr) && \text{closure, readout, protocol}\\",
        r"\mathcal R_Q &: \mathcal I_Q\oplus\mathcal F_Q \longrightarrow \text{boundary, field, device, or encoding}. &&",
        r"\end{centeredalign}",
        latex_escape(
            "A calculation can add a missing role, project a complete relation onto one consequence, or rewrite the same role in another representation. These are derivation moves on the constructor, not new physical postulates."
        ),
        r"\section{Why This Is More Compact}",
        latex_escape(
            "The usual presentation introduces particles, waves, measurement, operators, interpretations, and fields as separate conceptual blocks. The compact constructor shows that many of these are changes of role rather than separate roots. A particle is a stable state/readout role. A barrier is a context that changes the operator domain. A field is a many-mode extension of the state space. A quantum circuit is a protocolized composition of maps. An interpretation changes the meaning of state, probability, or update, but usually leaves the constructor intact."
        ),
    ]
    return "\n".join(lines)


def constructor_dependency_chapter(root: Path) -> str:
    """Render the V2 DAG and source-constructor result without exposing internal tokens."""
    report = load_optional_json(root / "quantum_constructor_dependencies.json")
    if not report:
        return ""

    dag = report.get("v2_completion_dag") or {}
    grammar = report.get("grammar_factorization") or {}
    source = report.get("source_constructor") or {}
    source_edges = source.get("source_local_edges") or {}
    status = source.get("constructor_status") or {}
    mdl = grammar.get("candidate_mdl_scores") or {}
    directed_fraction = float(dag.get("directed_fraction") or 0.0)
    coupled_lateral = float(dag.get("coupled_operator_substrate_lateral_fraction") or 0.0)
    complete_fraction = float((source.get("constructor_status_fractions") or {}).get("complete_constructor_frame") or 0.0)
    balance = float(source.get("completion_projection_balance") or 0.0)

    lines: List[str] = [
        r"\chapter{Dependencies Exposed By The Constructor}",
        r"\begin{claimbox}",
        latex_escape(
            "The corpus supports a typed carrier-operator identity, an attached completion fibre, and a reversible derivation calculus. The completion DAG records a partial order of formal specification; the source constructor records how equations are actually developed inside papers."
        ),
        r"\end{claimbox}",
        r"\section{How The Structure Was Obtained}",
        latex_escape(
            f"The analysis combines {int(dag.get('rows') or 0):,} retained equation morphisms with a source-local graph of {int(source.get('nodes') or 0):,} equations from {int(source.get('source_groups') or 0):,} paper groups. The factorization was selected on {int(grammar.get('rows_sampled') or 0):,} sampled rows and then checked against the full assignment."
        ),
        r"\begin{enumerate}",
        r"\item Each equation record was separated into carrier or context evidence, operator-apparatus evidence, and completion evidence for closure, readout, or ordered protocol.",
        r"\item Candidate grammars were compared by a description-length objective. The selected model retains carrier and operator as primitive factors and attaches completion as a fibre.",
        r"\item Mechanism edges were oriented only when the destination contained more constructor roles. This orientation defines completion rank, not physical time.",
        r"\item Equations adjacent in the same source were classified as role completion, role projection, or lateral rewrite. These edges restore the local order omitted by the corpus-wide DAG.",
        r"\end{enumerate}",
        r"\begin{longtable}{p{0.47\linewidth}r p{0.30\linewidth}}",
        r"\toprule",
        r"Measured quantity & Value & Consequence \\",
        r"\midrule",
        r"\endhead",
        rf"Selected grammar description score & {float(mdl.get('identity_with_completion_fiber') or 0.0):.3f} & carrier--operator identity with attached completion \\",
        rf"Three-factor alternative score & {float(mdl.get('three_factor_completion') or 0.0):.3f} & completion is not promoted to a third primitive space \\",
        rf"Mechanism edges increasing completion rank & {directed_fraction * 100:.1f}\% & the DAG is a partial order, not the whole graph \\",
        rf"Coupled carrier--operator edges remaining lateral & {coupled_lateral * 100:.2f}\% & similarity usually preserves rank \\",
        rf"Complete source constructor frames & {complete_fraction * 100:.1f}\% & mechanisms are distributed across neighboring equations \\",
        rf"Completion--projection balance & {balance:.3f} & source derivation is approximately bidirectional \\",
        r"\bottomrule",
        r"\end{longtable}",
        r"\section{Static Identity And Derivation Dynamics}",
        latex_escape(
            "Two structures must therefore be kept separate. The static identity says which operator apparatus is defined on which carrier and domain. The derivation dynamics says how a paper adds assumptions or readout, projects a relation onto a consequence, or changes representation without changing completion rank."
        ),
        r"\begin{centeredalign}",
        r"\text{identity:}\quad &\mathcal I=((\mathcal H,\mathcal D),\mathcal O),\\",
        r"\text{completion:}\quad &\mathcal F=(\mathcal K,\mathcal E,\mathcal P),\\",
        r"\text{derivation moves:}\quad &x\xrightarrow{+\,\mathrm{role}}y,\qquad x\xrightarrow{\mathrm{projection}}y,\qquad x\overset{\mathrm{rewrite}}{\longleftrightarrow}y.",
        r"\end{centeredalign}",
        latex_escape(
            f"The source graph contains {int(source_edges.get('source_sequence_role_completion') or 0):,} completion moves, {int(source_edges.get('source_sequence_role_projection') or 0):,} projections, and {int(source_edges.get('source_sequence_lateral') or 0):,} lateral rewrites. The near balance between the first two classes explains why a derivation cannot be represented faithfully as a one-way funnel."
        ),
        r"\section{Dependencies Made Explicit}",
        r"\begin{description}",
        r"\item[Hamiltonian.] Generator and observable are distinct roles of the same operator. Time evolution and energy readout share domain conditions but are not the same operation.",
        r"\item[Measurement.] Probability readout and post-measurement state update are separate maps. Treating them as one step hides the measurement junction.",
        r"\item[Wave function.] A wave function is a coordinate representation of a state. Basis change alters the function while preserving the carrier-level state and its probabilities.",
        r"\item[Entanglement.] The factorization of the carrier determines which observables count as local. Subsystem structure therefore enters the definition of the readout, not only the state.",
        r"\item[Gauge theory.] Representational redundancy must be quotiented or constrained before a physical readout is assigned. Closure is part of admissibility rather than a later correction.",
        r"\item[Quantum gravity.] Geometry may be a realization domain or part of the quantum carrier. The two cases require different operator domains and different notions of observable.",
        r"\item[Path integrals.] Integral and differential descriptions are alternative realizations of generator dynamics. Their equivalence depends on measure, boundary, and regularization data.",
        r"\item[Quantum simulation.] Physical carrier, encoded target, and validation observable are three distinct roles. Agreement of a programmed Hamiltonian alone does not complete the simulation claim.",
        r"\end{description}",
        r"\section{How This Chapter Organizes The Book}",
        latex_escape(
            "The branch chapters remain complete. They are grouped by the role each topic contributes to the typed identity, its completion, or its realization. Every topic page is retained; the constructor supplies cross-references between pages that share a formal dependency but use different physical vocabulary."
        ),
    ]
    return "\n".join(lines)


def _legacy_constructor_rewiring_chapter(root: Path) -> str:
    """Render testable cross-topic connections proposed by the constructor."""
    report = load_optional_json(root / "quantum_constructor_rewiring.json")
    connections = report.get("connections") if report else None
    if not isinstance(connections, list) or not connections:
        return ""

    lines: List[str] = [
        r"\chapter{Rewiring Quantum Concepts}",
        r"\begin{claimbox}",
        latex_escape(
            "A useful connection between two topics must specify the mathematical object that is retained, the part of the construction that is changed, and an independent calculation that can fail. Similar terminology or nearby evidence profiles are not sufficient."
        ),
        r"\end{claimbox}",
        r"\section{Four Legal Moves}",
        r"\begin{description}",
        r"\item[Representation change.] Move between descriptions while preserving amplitudes, expectation values, or correlators on their common domain.",
        r"\item[Carrier refactorization.] Change the subsystem, algebra, boundary, or encoding structure; locality and entanglement must then be recomputed.",
        r"\item[Completion attachment.] Add a constraint, readout, or protocol to an otherwise incomplete carrier--operator pair.",
        r"\item[Dual-role split.] Separate two operations performed by one mathematical object, such as generation of motion and spectral readout by a Hamiltonian.",
        r"\end{description}",
        latex_escape(
            "These moves do not assert that the connected theories are physically equivalent. They identify a controlled question: which predictions survive when one part of a quantum construction is replaced?"
        ),
        latex_escape(
            "The comparisons below were nominated by overlap among the equation-derived route profiles of the connected pages. That corpus signal is used only for selection; the displayed invariant and failure test determine whether a proposed connection survives mathematical scrutiny."
        ),
    ]

    for connection in connections:
        title = str(connection.get("title") or "Constructor connection")
        topic_names = []
        for value in connection.get("topics") or []:
            name = str(value).replace("_", " ").strip().title()
            name = name.replace("Ads/Cft", "AdS/CFT").replace("Schr Dinger", "Schrodinger")
            topic_names.append(name)
        topics = ", ".join(topic_names)
        invariant = str(connection.get("invariant") or "")
        rewiring = str(connection.get("rewiring") or "")
        test = str(connection.get("test") or "")
        equations = [str(x) for x in (connection.get("equations") or []) if str(x).strip()]
        if rewiring:
            rewiring = rewiring[0].upper() + rewiring[1:]

        lines.extend([
            rf"\section{{{latex_escape(title)}}}",
            rf"\textbf{{Connected topics:}} {latex_escape(topics)}\par",
            latex_escape(rewiring),
            rf"\textbf{{Retained object or prediction:}} {latex_escape(invariant)}\par",
        ])
        if equations:
            lines.append(r"\begin{centeredalign}")
            for index, equation in enumerate(equations):
                suffix = r"\\" if index + 1 < len(equations) else ""
                lines.append(equation + suffix)
            lines.append(r"\end{centeredalign}")
        lines.extend([
            rf"\textbf{{Failure test:}} {latex_escape(test)}\par",
        ])

    lines.extend([
        r"\section{What The Rewiring Adds}",
        latex_escape(
            "The resulting organization is neither a chronology nor a vocabulary tree. It exposes dependencies that are scattered across conventional chapters: domains connect dynamics to spectroscopy; factorization connects entanglement to locality; constraints connect gauge redundancy to observable construction; and instruments connect measurement to channels and error correction. Each connection can be used to design a calculation, but none bypasses its domain, normalization, or approximation conditions."
        ),
    ])
    return "\n".join(lines)


def page_entry(root: Path, row: Mapping[str, Any], index: int, branch_id: str, branch: Mapping[str, Any]) -> str:
    page = load_json(page_path(root, str(row["slug"])))
    mw = page.get("morphwiki", {})
    hyperion = page.get("hyperion", {})
    evidence = top_evidence(page, row, 5)
    title = page_title(page)
    topic_context = topic_context_text(page)
    topic_url = topic_source_url(page)
    topic_label = rf"\label{{topic:{latex_label(str(row.get('slug') or ''))}}}"
    if row.get("is_alias"):
        canonical_slug = str(row.get("canonical_slug") or "").strip()
        canonical_title = canonical_slug.replace("_", " ").strip().title() or "the canonical topic"
        target = latex_label(canonical_slug)
        return "\n".join(
            [
                r"\clearpage",
                rf"\section{{{latex_escape(title)}}}",
                topic_label,
                latex_escape(f"{title} is an alternative name for {canonical_title}."),
                rf"The physical derivation is given in \hyperref[topic:{target}]{{{latex_escape(canonical_title)}}}.",
            ]
        )
    if branch_id == "annotations" or row.get("is_annotation"):
        lines = [
            r"\clearpage",
            rf"\section{{{latex_escape(title)}}}",
            topic_label,
            r"\par\smallskip\noindent\textit{Historical or interpretive annotation.}",
        ]
        if topic_context:
            lines.extend([r"\subsection*{Topic Context}", latex_escape(topic_context)])
            if topic_url:
                lines.append(
                    rf"\par\smallskip\noindent\href{{{latex_url(topic_url)}}}"
                    r"{Topic scaffold: Wikipedia, CC BY-SA; adapted.}"
                )
        lines.extend([
            r"\subsection*{Historical Role}",
            latex_escape(
                f"{title} records the history, pedagogy, or interpretation of quantum theory. "
                "It does not define an additional state space, equation of motion, observable, or probability law."
            ),
            r"\subsection*{Relation To The Formal Theory}",
            latex_escape(
                "The source discusses states, operators, probability rules, or protocols whose mathematical consequences are developed in the physical chapters. "
                "Its interpretation changes the theory only when it changes an equation, admissibility condition, probability law, or experimental prediction."
            ),
        ])
        if evidence:
            lines.extend([r"\subsection*{Source Pointers}", r"\begin{itemize}"])
            for witness in evidence:
                arxiv = witness.get("paper_id") or ""
                url = witness.get("arxiv_url") or (f"https://arxiv.org/abs/{arxiv}" if arxiv else "")
                label = f"arXiv:{arxiv}" if arxiv else str(witness.get("record_id") or "source witness")
                if url:
                    lines.append(rf"\item \href{{{latex_url(url)}}}{{{latex_escape(label)}}}")
                else:
                    lines.append(rf"\item {latex_escape(label)}")
            lines.append(r"\end{itemize}")
        return public_theory_language("\n".join(lines))
    constructed = has_topic_constructor(page, str(row.get("slug") or ""))
    constructor = constructor_text(title, branch_id, row, hyperion, mw)
    claim = constructor["claim"]
    mechanism = constructor["reading"]
    slug = str(row.get("slug") or "")
    template = constructor_template(branch_id, row)
    explanation = topic_explanation_for_page(slug, title, branch_id)
    survives, changes, tests = support_lists_for_page(page, row, branch_id, constructed)
    route_profile = hyperion.get("route_profile") or {}
    route_summary = ", ".join(
        f"{key.replace('_route', '').replace('_', ' ')}={float(value or 0):.2f}"
        for key, value in sorted(route_profile.items(), key=lambda item: float(item[1] or 0), reverse=True)[:3]
    )
    lines = [r"\clearpage"]
    lines.append(rf"\section{{{latex_escape(title)}}}")
    lines.append(topic_label)
    if branch_id == "annotations" or row.get("is_annotation"):
        lines.append(r"\par\smallskip\noindent\textit{This page is treated as historical, interpretive, or popular context rather than as a conceptual root.}")
    lines.append("")
    if topic_context:
        lines.append(r"\subsection*{Topic Context}")
        lines.append(latex_escape(topic_context))
        if topic_url:
            lines.append(
                rf"\par\smallskip\noindent\href{{{latex_url(topic_url)}}}"
                r"{Topic scaffold: Wikipedia, CC BY-SA; adapted.}"
            )
        lines.append("")
    lines.append(r"\subsection*{Mechanism}")
    lines.append(latex_escape(clean_text(claim, 850)))
    lines.append("")
    lines.append(latex_escape(explanation["why"]))
    lines.append("")
    lines.append(latex_escape(clean_text(mechanism, 1200)))
    lines.append("")
    lines.append(r"\subsection*{Physical Construction}")
    lines.append(latex_escape(physical_construction_prose(title, branch_id, row, mw)))
    lines.append("")
    topic_equations = (
        math_skeleton_block(mw.get("mathematical_skeleton"))
        if constructed and slug not in TOPIC_CONSTRUCTOR_OVERRIDES
        else ""
    )
    if topic_equations:
        lines.append(topic_equations)
        lines.append("")
    else:
        block = constructor_block(title, branch_id, row, hyperion, evidence, mw)
        if block:
            lines.append(block)
            lines.append("")
    lines.append(r"\subsection*{Physical Meaning}")
    lines.append(latex_escape(explanation["reading"]))
    lines.append("")
    if explanation["example"]:
        lines.append(latex_escape(explanation["example"]))
        lines.append("")
    if explanation["connection"]:
        lines.append(latex_escape(explanation["connection"]))
        lines.append("")
    depth_sections = latex_derivation_depth_sections(template)
    if depth_sections:
        lines.append(depth_sections)
        lines.append("")
    lines.append(r"\subsection*{Invariance And Realization}")
    lines.append(latex_escape(prose_from_items(survives, 4)))
    lines.append("")
    lines.append(latex_escape(prose_from_items(changes, 4)))
    lines.append("")
    lines.append(r"\subsection*{Discriminating Consequences}")
    lines.append(latex_escape(consequence_prose_from_items(tests, 3)))
    lines.append("")
    if evidence:
        lines.append(r"\subsection*{Source Pointers}")
        lines.append(r"\begin{itemize}")
        for witness in evidence:
            arxiv = witness.get("paper_id") or ""
            url = witness.get("arxiv_url") or (f"https://arxiv.org/abs/{arxiv}" if arxiv else "")
            label = f"arXiv:{arxiv}" if arxiv else str(witness.get("record_id") or "source witness")
            if url:
                lines.append(rf"\item \href{{{latex_url(url)}}}{{{latex_escape(label)}}}")
            else:
                lines.append(rf"\item {latex_escape(label)}")
        lines.append(r"\end{itemize}")
    return public_theory_language("\n".join(lines))


def markdown_equations(value: Any) -> str:
    equations = clean_math_skeleton(value)
    if not equations:
        return ""
    body = "\n".join(equations)
    return "\n".join(["## Topic Equations", "", "```math", body, "```", ""])


def evidence_status_text(row: Mapping[str, Any]) -> str:
    v2 = row.get("v2_evidence") or {}
    status = str(v2.get("status") or "")
    if status == "v2_identifier_linked":
        return (
            "Candidate paper and equation-card identifiers were found, but no source equation "
            "has passed topic-level alignment; no citation is assigned."
        )
    if status == "legacy_witness_only":
        return "No V2-aligned source-equation candidate is available for this topic."
    if status == "no_v2_index":
        return "No V2 source-evidence index was available for this build."
    if status == "page_not_in_v2_index":
        return "This topic is absent from the current V2 source-evidence index."
    return "No source equation has passed topic-level alignment for this topic."


def markdown_evidence(
    evidence: Sequence[Mapping[str, Any]],
    row: Mapping[str, Any],
) -> str:
    if not evidence:
        return ""
    lines = []
    for witness in evidence[:6]:
        arxiv = witness.get("paper_id") or ""
        url = witness.get("arxiv_url") or (f"https://arxiv.org/abs/{arxiv}" if arxiv else "")
        label = f"arXiv:{arxiv}" if arxiv else str(witness.get("record_id") or "source witness")
        linked = f"[{label}]({url})" if url else label
        lines.append(f"- {linked}")
    return "\n".join(lines) + "\n"


def render_derivation_page(root: Path, row: Mapping[str, Any], branch_id: str, branch: Mapping[str, Any]) -> str:
    page = load_json(page_path(root, str(row["slug"])))
    mw = page.get("morphwiki") or {}
    hyperion = page.get("hyperion") or {}
    title = page_title(page)
    topic_context = topic_context_text(page)
    topic_url = topic_source_url(page)
    evidence = top_evidence(page, row, 6)
    if branch_id == "annotations" or row.get("is_annotation"):
        lines = [
            f"# {title}",
            "",
            "*Historical or interpretive annotation.*",
            "",
        ]
        if topic_context:
            lines.extend(["## Topic Context", "", topic_context, ""])
            if topic_url:
                lines.extend([f"[Topic scaffold: Wikipedia, CC BY-SA; adapted.]({topic_url})", ""])
        lines.extend([
            "## Historical Role",
            "",
            f"{title} records the history, pedagogy, or interpretation of quantum theory. "
            "It does not define an additional state space, equation of motion, observable, or probability law.",
            "",
            "## Relation To The Formal Theory",
            "",
            "The source discusses states, operators, probability rules, or protocols whose mathematical consequences are developed in the physical chapters. "
            "Its interpretation changes the theory only when it changes an equation, admissibility condition, probability law, or experimental prediction.",
            "",
        ])
        if evidence:
            lines.extend(["## Source Equations", "", markdown_evidence(evidence, row)])
        return public_theory_language("\n".join(lines).rstrip() + "\n")
    constructed = has_topic_constructor(page, str(row.get("slug") or ""))
    constructor = constructor_text(title, branch_id, row, hyperion, mw)
    slug = str(row.get("slug") or "")
    template = constructor_template(branch_id, row)
    explanation = topic_explanation_for_page(slug, title, branch_id)
    lines = [
        f"# {title}",
        "",
        f"**Physical domain:** {branch.get('title')}",
        "",
    ]
    if topic_context:
        lines.extend(["## Topic Context", "", topic_context, ""])
        if topic_url:
            lines.extend([f"[Topic scaffold: Wikipedia, CC BY-SA; adapted.]({topic_url})", ""])
    lines.extend(
        [
            "## Mechanism",
            "",
            clean_text(constructor["claim"], 1200),
            "",
            explanation["why"],
            "",
            clean_text(constructor["reading"], 1800),
            "",
            "## Physical Construction",
            "",
            physical_construction_prose(title, branch_id, row, mw),
            "",
        ]
    )
    eq = (
        markdown_equations(mw.get("mathematical_skeleton"))
        if constructed and slug not in TOPIC_CONSTRUCTOR_OVERRIDES
        else ""
    )
    if eq:
        lines.append(eq)
    else:
        conversion = (
            [public_book_text(item) for item in (mw.get("conversion_form") or []) if clean_text(item)]
            if constructed
            else []
        )
        if slug in TOPIC_CONSTRUCTOR_OVERRIDES:
            equations = template.get("equations") or []
            if equations:
                lines.extend(
                    [
                        "## Topic Equations",
                        "",
                        str(template.get("equation_note") or "Topic-specific constructor skeleton."),
                        "",
                        "```math",
                        "\n".join(equations),
                        "```",
                        "",
                    ]
                )
        elif conversion:
            lines.extend(["## Defining Relations", "", prose_from_items(conversion, 6), ""])
        else:
            equations = template.get("equations") or []
            if slug not in TOPIC_CONSTRUCTOR_OVERRIDES:
                equations = [role_equation_for_page(slug, title, branch_id)]
            if equations:
                heading = "Topic Equations" if constructed else "Representative Relation"
                lines.extend(["## " + heading, "", "```math", "\n".join(equations), "```", ""])
    lines.extend(["## Physical Meaning", "", explanation["reading"], ""])
    if explanation["example"]:
        lines.extend([explanation["example"], ""])
    if explanation["connection"]:
        lines.extend([explanation["connection"], ""])
    depth_sections = markdown_derivation_depth_sections(template)
    if depth_sections:
        lines.append(depth_sections)
    survives, changes, tests = support_lists_for_page(page, row, branch_id, constructed)
    if survives or changes:
        lines.extend(["## Invariance And Realization", ""])
    if survives:
        lines.extend([prose_from_items(survives, 4), ""])
    if changes:
        lines.extend([prose_from_items(changes, 4), ""])
    if tests:
        lines.extend(["## Discriminating Consequences", "", consequence_prose_from_items(tests, 3), ""])
    if evidence:
        lines.extend(["## Source Equations", "", markdown_evidence(evidence, row)])
    return public_theory_language("\n".join(lines).rstrip() + "\n")


def write_derivation_pages(root: Path, out_dir: Path, tree: Mapping[str, Any]) -> Dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: List[Dict[str, Any]] = []
    for branch_id in BRANCH_ORDER:
        branch = tree["branches"][branch_id]
        for row in branch.get("pages") or []:
            page = load_json(page_path(root, str(row["slug"])))
            constructed = has_topic_constructor(page, str(row.get("slug") or ""))
            basis = derivation_basis(page, row, branch_id)
            path = out_dir / f"{row['slug']}.md"
            path.write_text(render_derivation_page(root, row, branch_id, branch), encoding="utf-8")
            rows.append(
                {
                    "slug": row.get("slug"),
                    "title": row.get("title"),
                    "branch": branch_id,
                    "status": (
                        "annotation"
                        if branch_id == "annotations" or row.get("is_annotation")
                        else "topic_specific" if constructed else "branch_level"
                    ),
                    "derivation_basis": basis,
                    "source_grounded": basis.startswith("source_grounded"),
                    "identifier_linked": basis.startswith("identifier_linked"),
                    "path": str(path),
                }
            )
    manifest = {
        "report_type": "quantum_derivation_pages_manifest",
        "row_count": len(rows),
        "topic_specific_count": sum(1 for row in rows if row["status"] == "topic_specific"),
        "branch_level_count": sum(1 for row in rows if row["status"] == "branch_level"),
        "core_derived_count": sum(1 for row in rows if row["status"] == "branch_level"),
        "annotation_count": sum(1 for row in rows if row["status"] == "annotation"),
        "source_grounded_count": sum(1 for row in rows if row["source_grounded"]),
        "identifier_linked_count": sum(1 for row in rows if row["identifier_linked"]),
        "derivation_basis_counts": dict(Counter(row["derivation_basis"] for row in rows)),
        "pages": rows,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return manifest


def branch_table(branch: Mapping[str, Any]) -> str:
    rows = list(branch.get("pages", []))
    lines = [
        r"\begin{longtable}{p{0.92\linewidth}}",
        r"\toprule",
        r"Page \\",
        r"\midrule",
        r"\endhead",
    ]
    for row in rows:
        title = row.get("title")
        anchor = rf"\phantomsection\label{{page:{latex_label(str(row.get('slug') or ''))}}}"
        if row.get("is_alias"):
            canonical = str(row.get("canonical_slug") or "").replace("_", " ").title()
            suffix = rf" \emph{{(see {latex_escape(canonical)})}}"
        elif branch.get("id") == "annotations" or row.get("is_annotation"):
            suffix = r" \emph{(annotation)}"
        else:
            suffix = ""
        lines.append(rf"{anchor}{latex_escape(title)}{suffix} \\")
    lines.extend([r"\bottomrule", r"\end{longtable}"])
    return "\n".join(lines)


def render_transition_sparse_attention_section() -> str:
    """Render the source-equation rewrite transition sparse-attention results."""
    report = load_optional_json(
        Path("discoveries/morphwiki_quantum/sparse_attention/morphwiki_rewrite_transition_sparse_attention.json")
    )
    if not report:
        return ""

    summary = report.get("summary") or {}
    rules = report.get("rules") or []
    hotspots = report.get("top_transition_pages") or []
    uses = report.get("uses") or []
    route_means = summary.get("route_means") or {}

    constructed = int(summary.get("constructed_pages", 0))
    placements = int(summary.get("evidence_placements", 0))
    page_count = int(summary.get("page_count", constructed + placements))

    lines: List[str] = [
        r"\section*{Transition Sparse-Attention Result}",
        r"\addcontentsline{toc}{section}{Transition Sparse-Attention Result}",
    ]
    lines.append(
        latex_escape(
            "A second sparse-attention pass compared the article ordering with the rewritten derivation ordering. "
            "The comparison asks which formal roles become visible when the same quantum topics are sorted by Hilbert-space "
            "context, state, generator, spectrum, probability rule, compatibility condition, and physical realization rather "
            "than by article title."
        )
    )
    lines.append(
        latex_escape(
            f"The transition run covered {page_count} pages. Of these, {constructed} currently have topic-specific equation skeletons "
            f"or explicit page overrides, while {placements} are expanded from the common quantum formalism. "
            "The distinction is evidential, not structural: both page types are read through the same context-state-generator-spectrum-readout sequence."
        )
    )
    lines.append(
        latex_escape(
            "The transition signal is asymmetric: the rewrite adds formal roles more strongly than it adds object names. "
            "It exposes state, operator, readout, compatibility, boundary, and protocol roles that are implicit "
            "in the article ordering."
        )
    )
    lines.extend(
        [
            r"\begin{longtable}{p{0.44\linewidth}p{0.20\linewidth}p{0.20\linewidth}}",
            r"\toprule",
            r"Route role & Mean signal & Interpretation \\",
            r"\midrule",
            r"\endhead",
        ]
    )
    for key in [
        "spectral_operator_route",
        "transport_flow_route",
        "constraint_closure_route",
        "boundary_weak_form_route",
        "commutator_incompatibility_route",
        "discrete_protocol_route",
    ]:
        lines.append(
            rf"{latex_escape(ROUTE_PUBLIC.get(key, key))} & {float(route_means.get(key, 0.0)):.4f} & "
            rf"{latex_escape('formal role preserved in the rewrite')} \\"
        )
    lines.extend([r"\bottomrule", r"\end{longtable}"])

    if rules:
        lines.extend(
            [
                r"\subsection*{New Structural Information}",
                r"\begin{enumerate}",
            ]
        )
        for rule in rules:
            lines.append(
                rf"\item \textbf{{{latex_escape(rule.get('rule'))}}} "
                rf"{latex_escape(rule.get('new_information'))}"
            )
        lines.append(r"\end{enumerate}")

    if hotspots:
        lines.extend(
            [
                r"\subsection*{Highest-Attention Transition Pages}",
                r"\begin{itemize}",
            ]
        )
        for row in hotspots[:8]:
            roles = ", ".join(str(name) for name, _score in (row.get("top_post_roles") or [])[:3])
            if not roles:
                roles = "multiple formal roles"
            explanation = anomaly_public_explanation(row)
            lines.append(
                rf"\item \textbf{{{latex_escape(row.get('title'))}}} "
                rf"({latex_escape(row.get('branch'))}, {latex_escape(row.get('status'))}): "
                rf"dominant roles after rewriting are {latex_escape(roles)}. "
                rf"Formal reading: {latex_escape(explanation)}"
            )
        lines.append(r"\end{itemize}")

    if uses:
        lines.extend(
            [
                r"\subsection*{Consequences For The Quantum Presentation}",
            ]
        )
        for row in uses[:5]:
            why = str(row.get("why_useful") or "")
            why = why.replace("evidence placements", "core-derived pages")
            why = why.replace("evidence placement", "core-derived page")
            why = why.replace("constructed pages", "topic-specific pages")
            why = why.replace("constructed page", "topic-specific page")
            why = why.replace("supervised queue", "supervised specialization set")
            lines.append(latex_escape(why))

    lines.append(
        latex_escape(
            "The resulting presentation is a derivation tree rather than a topic list. Topic-specific pages show local equations. "
            "Core-derived pages state which quantum ingredients must be supplied before the page supports a full derivation."
        )
    )
    return public_theory_language("\n\n".join(lines))


def render_preamble(tree: Mapping[str, Any]) -> str:
    stats = tree.get("sparse_attention", {})
    count_routes = stats.get("count_gt_0_1", {})
    mean_routes = stats.get("mean_routes", {})
    branches = tree.get("branches", {})
    branch_counts = {
        branch_id: len((branches.get(branch_id) or {}).get("pages") or [])
        for branch_id in BRANCH_ORDER
    }
    anomalies = tree.get("anomalies") or []
    top_anomalies = anomalies[:8]
    lines: List[str] = []
    lines.extend(
        [
            r"\chapter*{Preamble: Findings From The Rewrite}",
            r"\addcontentsline{toc}{chapter}{Preamble: Findings From The Rewrite}",
            r"\section*{Core Insight}",
            r"\addcontentsline{toc}{section}{Core Insight}",
        ]
    )
    lines.append(
        latex_escape(
            "The rewrite reveals a compact dependency structure beneath the usual quantum topic list. The new DAG and source constructor distinguish the identity of a mechanism from the local moves used to derive it:"
        )
    )
    lines.extend(
        [
            r"\begin{claimbox}",
            r"\noindent\textbf{Constructor structure:} carrier/context \(\leftrightarrow\) operator apparatus; closure, readout, and protocol attach as completion modes; boundaries, fields, and devices supply realizations. Source derivations move by completion, projection, and lateral rewrite.",
            r"\end{claimbox}",
        ]
    )
    lines.append(
        latex_escape(
            "Here, context means the preparation, basis, boundary, gauge, domain, detector, or representation in which a question "
            "is posed. It selects the Hilbert space and operator domain allowed by that context, together with normalization, "
            "positivity, boundary, gauge, or domain constraints. This carrier is central: it defines which states are legal, "
            "how amplitudes and norms are compared, which operators may act, and how spectral projectors can be read probabilistically. "
            "The generator is the Hamiltonian, unitary map, "
            "channel, or action that carries the state before readout. The observable spectrum is the allowed answer set of the "
            "question being asked. The probability readout is the Born or trace-rule assignment to those answers. The compatibility "
            "constraint records which otherwise valid questions cannot be resolved together, for example through a non-zero "
            "commutator, uncertainty relation, contextuality test, conservation law, or admissibility condition. Boundary and "
            "protocol realization specify how the same construction is embodied as a potential well, scattering boundary, cavity, "
            "field mode, detector, circuit, or measurement sequence."
        )
    )
    lines.extend(
        [
            r"\section*{Main Finding And Why It Matters}",
            r"\addcontentsline{toc}{section}{Main Finding And Why It Matters}",
        ]
    )
    lines.append(
        latex_escape(
            "The rewrite reorganizes the quantum corpus by the sequence needed to make a prediction: select a domain or Hilbert space, "
            "assign a state, specify a generator or measurement map, resolve the relevant spectrum, assign probabilities, and check "
            "compatibility and realization conditions. Named topics then enter as positions in that sequence. Particles, waves, measurement, "
            "tunnelling, entanglement, collapse, fields, and interpretations are not treated as equal roots; each supplies a state, map, "
            "readout, compatibility limit, boundary condition, protocol, or annotation."
        )
    )
    lines.append(
        latex_escape(
            "This gives a test for comparing pages. A page is technically specified when it states what state is carried, what operator "
            "or map acts, what spectrum or readout is produced, what compatibility constraint applies, and what changes when the physical "
            "realization changes. Two topics can therefore differ in vocabulary while preserving the same state-operator-readout structure."
        )
    )
    lines.append(
        latex_escape(
            "This organization also changes how quantum models can be compared. The comparison is no longer based on topic names alone; "
            "it asks whether the Hilbert space or domain, operator class, spectral readout, and compatibility condition remain well defined "
            "after a change of representation or realization. Mixed-role pages then become specific decomposition problems rather than isolated puzzles."
        )
    )
    lag_prior = tree.get("lagrangian_construction_prior") or {}
    if lag_prior.get("available"):
        class_counts = lag_prior.get("path_class_counts") or {}
        class_text = ", ".join(f"{str(key).replace('_', ' ')}: {value}" for key, value in sorted(class_counts.items()))
        lines.extend(
            [
                r"\section*{How The Tree Was Constructed}",
                r"\addcontentsline{toc}{section}{How The Tree Was Constructed}",
            ]
        )
        lines.append(
            latex_escape(
                "The tree uses a DAG-then-constructor procedure. The DAG supplies the ordered assembly of roles, so context, carrier, generator, readout, compatibility, and realization are not treated as interchangeable topic labels. "
                "The constructor fills that order with page-local equations or branch-level role equations. Page branches are assigned from topic-native lexical anchors and equation evidence. "
                "The Lagrangian supplies the global construction prior: it identifies low-action roads, high-tension paths, and void-boundary targets in the evidence atlas, which sets the interpretation of open construction steps."
            )
        )
        if lag_prior.get("page_projection_available") and class_text:
            lines.append(
                latex_escape(
                    "In the current quantum tree, the page-level Lagrangian projections are: " + class_text + ". "
                    "These classes are construction priorities; physical law status requires source equations and validation."
                )
            )
        else:
            lines.append(
                latex_escape(
                    "The current quantum archive contains witness links. A later export with "
                    "full page-coordinate vectors and page-specific transition velocities will support direct page-level action scoring. "
                    "For this version, the Lagrangian supplies the road-map logic for construction priority."
                )
            )
    transition_section = render_transition_sparse_attention_section()
    if transition_section:
        lines.append(transition_section)
    lines.extend(
        [
            r"\section*{Main Findings}",
            r"\addcontentsline{toc}{section}{Main Findings}",
            r"\begin{enumerate}",
        ]
    )
    findings = [
        (
            "A compact order is enough to reconstruct most pages.",
            "The recurring order is Hilbert space or domain, state, generator, observable, spectral resolution, probability rule, and compatibility condition. The book uses this order to present the standard formalism before moving to particles, fields, protocols, and interpretations.",
        ),
        (
            "Observables and spectra carry the largest recurrent signal.",
            f"{int(count_routes.get('spectral_operator_route', 0))} of 147 pages exceed the operator/spectrum threshold, "
            f"with mean signal {float(mean_routes.get('spectral_operator_route', 0.0)):.3f}. This is why self-adjoint operators, projectors, eigenvalues, and spectral measures appear early in the reconstruction.",
        ),
        (
            "State evolution is widespread but requires a later question.",
            f"{int(count_routes.get('transport_flow_route', 0))} pages carry state-evolution or transport signal. In the quantum reading, a Hamiltonian, unitary map, semigroup, channel, or path integral evolves a state before an observable defines the recorded distribution.",
        ),
        (
            "Domains and boundary conditions specify admissible realizations.",
            f"{int(count_routes.get('boundary_weak_form_route', 0))} pages emphasize preparation, boundary, or domain context. Tunnelling, cavities, scattering, and particle-in-a-box are grouped as cases where the domain or potential changes the allowed spectrum or transition amplitude.",
        ),
        (
            "Incompatibility marks failure of joint spectral resolution.",
            f"{int(count_routes.get('commutator_incompatibility_route', 0))} pages carry explicit incompatibility signal. Entanglement, Bell phenomena, commutators, and uncertainty enter through observables that cannot be assigned one common sharp classical readout under the stated assumptions.",
        ),
        (
            "Protocols are ordered implementations of the same formal steps.",
            f"Only {int(count_routes.get('discrete_protocol_route', 0))} pages exceed the protocol threshold. Quantum computing and information pages are therefore placed after the state, map, measurement, and compatibility layers that their circuits or channels compose.",
        ),
        (
            "Topic names map onto formal roles.",
            ", ".join(f"{(branches.get(branch_id) or {}).get('title', branch_id)}: {count}" for branch_id, count in branch_counts.items())
            + ". This gives a formal table of contents for the book: the branch of a page is determined by the role its equations or witnesses emphasize.",
        ),
        (
            "Particles enter through representations, statistics, and readout-stable excitations.",
            "Particle pages resolve into field modes, spectra, occupation rules, statistics, and detector-stable excitations. Particle identity is treated as a role inside the state-operator-readout formalism, not as the first organizing variable of the book.",
        ),
        (
            "String theory and AdS/CFT are field/geometry correspondence cases.",
            "String theory is placed with many-mode spectral constructions. AdS/CFT is placed closer to geometry because boundary data, correlators, and reconstruction maps carry more of its formal content in the current evidence profile.",
        ),
        (
            "Black-hole topics require a dedicated source set.",
            "The sparse-attention analysis places black-hole physics near boundary, information, and closure questions. A reliable black-hole chapter needs a targeted run over horizons, Hawking radiation, entropy, holography, and information-loss source equations.",
        ),
        (
            "Interpretations modify state, probability, update, or observer language.",
            "Interpretive pages are retained as annotations on the formal machinery. They are not used to replace the Hamiltonian, operator algebra, spectral decomposition, or Born-rule probability assignment.",
        ),
        (
            "Geometry supplies domains, boundary data, and reconstruction maps.",
            "Geometry enters when the carrier space, metric, boundary, gauge representation, or reconstruction map determines which operators and readouts are admissible. In the current evidence profile, operator and spectral roles are more portable than geometric presentation.",
        ),
    ]
    for head, body in findings:
        lines.append(rf"\item \textbf{{{latex_escape(head)}}} {latex_escape(body)}")
    lines.extend([r"\end{enumerate}", r"\section*{What Changed Relative To Wikipedia}", r"\addcontentsline{toc}{section}{What Changed Relative To Wikipedia}"])
    lines.append(
        latex_escape(
            "A conventional encyclopedia organizes quantum theory by names and historical articles. The source-equation rewrite "
            "organizes the same material by the operations needed to construct a prediction. The page named "
            "measurement no longer becomes the origin of the theory; it becomes the readout junction. The page named "
            "particle becomes a realization. The page named tunnelling becomes a boundary spectral channel. The page named "
            "quantum field theory becomes a scaling and many-mode extension. The tree therefore gives a new order of "
            "explanation rather than a new interpretation of consciousness, observation, or ontology."
        )
    )
    lines.extend(
        [
            r"\section*{Unusual Findings And Anomalies}",
            r"\addcontentsline{toc}{section}{Unusual Findings And Anomalies}",
        ]
    )
    lines.append(
        latex_escape(
            "The most useful anomalies are not errors. They are pages that sit between branches or violate the dominant "
            "operator/spectrum pattern. These pages mark conceptual junctions where a theory-builder should look for "
            "missing assumptions, hidden boundary conditions, or possible transfers to other fields."
        )
    )
    lines.append(
        latex_escape(
            "The anomaly labels describe a page's role in the mechanism tree, not the literal physical object named by the page. "
            "For example, a page can be structurally anomalous because context, protocol, or compatibility carries the explanation before spectra are read out."
        )
    )
    lines.append(r"\begin{itemize}")
    for label, explanation in ANOMALY_LABEL_EXPLANATIONS.items():
        public_name = ANOMALY_PUBLIC_NAMES.get(label, label)
        lines.append(rf"\item \textbf{{{latex_escape(public_name)}}}: {latex_escape(explanation)}.")
    lines.append(r"\end{itemize}")
    lines.append(r"\begin{itemize}")
    for item in top_anomalies:
        branch = (branches.get(item.get("branch")) or {}).get("title", item.get("branch"))
        secondary = (branches.get(item.get("secondary")) or {}).get("title", item.get("secondary"))
        explanation = anomaly_public_explanation(item)
        lines.append(
            rf"\item \textbf{{{latex_escape(item.get('title'))}}}. "
            rf"Primary reading: {latex_escape(branch)}; neighboring reading: {latex_escape(secondary)}. "
            rf"{latex_escape(explanation)}"
        )
    lines.append(r"\end{itemize}")
    anomaly_implications = {
        "weak spectral anchor": (
            "the eigenvalue problem is downstream of another role that first defines the admissible question"
        ),
        "boundary-driven dynamics": (
            "preparation, apparatus, domain, detector, or boundary conditions participate in the observed law"
        ),
        "compatibility/closure junction": (
            "admissibility conditions and jointly resolvable questions meet in the same topic"
        ),
        "protocol is unusually explicit": (
            "the order of preparation, transformation, and readout is part of the mechanism"
        ),
        "multi-role hub": (
            "one topic name covers several formal roles, so the page is a junction rather than a single branch leaf"
        ),
        "branch-ambiguous": (
            "the topic lies at an interface between explanatory roles and should be read as a bridge"
        ),
    }
    label_counts: Counter[str] = Counter()
    for item in anomalies:
        label_counts.update(item.get("labels") or [])
    lines.extend(
        [
            r"\section*{Interpretation Of The Anomalies}",
            r"\addcontentsline{toc}{section}{Interpretation Of The Anomalies}",
        ]
    )
    if label_counts:
        lines.append(
            latex_escape(
                "The sparse-attention interpretation is aggregated from role labels assigned by the mechanism pass. "
                "It summarizes recurring junction types in the mechanism tree rather than presenting a list of physical anomalies."
            )
        )
        lines.append(r"\begin{itemize}")
        for label, _count in label_counts.most_common():
            explanation = ANOMALY_LABEL_EXPLANATIONS.get(label, "the page has an unresolved constructor role")
            implication = anomaly_implications.get(label, "the assignment should be read with source-equation and route evidence")
            public_name = ANOMALY_PUBLIC_NAMES.get(label, label)
            lines.append(
                rf"\item \textbf{{{latex_escape(public_name)}}}. "
                rf"{latex_escape(explanation)}. Mechanism implication: {latex_escape(implication)}."
            )
        lines.append(r"\end{itemize}")
    lines.extend(
        [
            r"\section*{Constructor-Detected Research Leads}",
            r"\addcontentsline{toc}{section}{Constructor-Detected Research Leads}",
        ]
    )
    lines.append(
        latex_escape(
            "The useful anomalies in this book are constructor junctions: places where a topic requires several formal roles at once. "
            "Some are established foundational problems; others are under-formulated mechanism questions that can guide derivation and experiment."
        )
    )
    constructor_leads = [
        (
            "Measurement as a four-map junction",
            "The established measurement problem becomes formally sharper when split into pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record state conditioning. The useful signal is the missing local map between probability readout and state update.",
        ),
        (
            "Geometry as a possible state carrier",
            "Quantum gravity is a field/geometry interface problem. The constructor reading isolates the specific unresolved choice: whether geometry remains a substrate on which operators act, or becomes part of the quantum state carrier itself. The corresponding test is which geometric quantities survive as admissible observables after quantization.",
        ),
        (
            "Boundary-selected spectra across different phenomena",
            "Scattering, tunnelling, cavities, particle-in-a-box systems, spectral lines, and optical boundary problems share a boundary-to-spectrum construction. The research lead is to treat them as one transferable mechanism family rather than as separate examples tied to different physical nouns.",
        ),
        (
            "Environment as an active selector in quantum biology",
            "In quantum biology, the useful constructor signal is that the environment can be part of the mechanism: it may preserve, destroy, or select coherence. A useful derivation must name the carrier, coupling, coherence or transport observable, and classical control.",
        ),
        (
            "Hamiltonian dual role",
            "The Hamiltonian is both a generator of time evolution and an observable with an energy spectrum. This is standard formalism. The constructor lead is to keep those roles distinct when deriving mechanisms that use energy conservation, spectral measurement, and unitary transport in the same page.",
        ),
        (
            "Quantum simulation as a target-carrier-validation triangle",
            "A simulator is an engineered realization of another Hamiltonian, channel, or field theory. The anomaly is practical: the physical carrier, encoded target, and validation observable are distinct roles. A simulator claim is incomplete until all three are specified.",
        ),
    ]
    lines.append(r"\begin{itemize}")
    for title, body in constructor_leads:
        lines.append(rf"\item \textbf{{{latex_escape(title)}}}. {latex_escape(body)}")
    lines.append(r"\end{itemize}")

    lines.extend(
        [
            r"\section*{Relation To Lagrangian, Transfer, And Stability Layers}",
            r"\addcontentsline{toc}{section}{Relation To Lagrangian, Transfer, And Stability Layers}",
        ]
    )
    lines.append(
        latex_escape(
            "The later validation chapter explains how the global evidence layers check this tree. Stability tests ask "
            "which part of a formalism remains the same after a rewrite. Typed transfer and bridge-family layers ask which constructor roles can move between contexts. "
            "The Lagrangian navigation layer asks whether a proposed move through the atlas is a low-resistance continuation, a strained bridge, or a void-boundary target. "
            "In ordinary quantum language: the invariant is mostly operator/structural role, while geometry, boundary, and representation are where the role becomes embodied."
        )
    )
    lines.extend(
        [
            r"\section*{Practical Consequence}",
            r"\addcontentsline{toc}{section}{Practical Consequence}",
        ]
    )
    lines.append(
        latex_escape(
            "A reader, teacher, or AI constructor should not start from named quantum objects. The constructive order is: "
            "define the admissible context, define the predictive carrier, define lawful change, define the legal question, "
            "resolve its spectrum, assign probabilities, test incompatibility, then dress the construction in the relevant physical realization. That is the main structural result "
            "of the rewrite."
        )
    )
    return "\n\n".join(lines)


def render_v2_language_chapter(tree: Mapping[str, Any]) -> str:
    """Render the optional mechanism-grammar layer when artifacts are supplied."""

    v2 = tree.get("hyperion_v2_language") or {}
    if not v2.get("available"):
        return ""
    counts = v2.get("language_counts") or {}
    compact = v2.get("logical_compactness") or {}
    grounding = v2.get("source_grounding") or {}
    lines: List[str] = [
        r"\chapter{Auxiliary Mechanism Grammar Layer}",
        r"\begin{claimbox}",
        r"\noindent\textbf{Mechanism identity signature:} \(I=(\Omega,\Xi;C,R,P)\). "
        r"\(\Omega\) is the operator-apparatus coordinate, \(\Xi\) is the substrate/carrier coordinate, and "
        r"\(C,R,P\) are attached completion fibers for closure, readout/current, and protocol/order.",
        r"\end{claimbox}",
        latex_escape(
            "This optional build note records how the transferred mechanism grammar changes the quantum-book interpretation. "
            "The grammar separates the reusable operator apparatus from the admissible substrate, "
            "then attaches the obligations needed for a mechanism to become constructible: closure, readout/current, and protocol/order."
        ),
        latex_escape(
            "The important correction is that the six route families are not identity coordinates. They are edge or road modes by which identities move or are compared. "
            "The identity object has two primitive coordinates and three attached completion fibers."
        ),
        r"\section{How Quantum Theory Maps To The Grammar}",
        r"\begin{longtable}{p{0.20\linewidth}p{0.68\linewidth}}",
        r"\toprule",
        r"Grammar role & Quantum reading \\",
        r"\midrule",
        r"\endhead",
        r"\(\Omega\) & Operator apparatus: Hamiltonian, unitary map, channel, observable algebra, creation/annihilation operator, commutator or generator. \\",
        r"\(\Xi\) & Admissible substrate/carrier: Hilbert space, Fock space, density-operator state space, operator domain, gauge sector, boundary domain or detector context. \\",
        r"\(C\) & Closure/admissibility: normalization, positivity, self-adjointness, gauge constraint, boundary condition, trace preservation or complete positivity. \\",
        r"\(R\) & Readout/current: Born rule, spectral projector, POVM effect, detector record, occupation number, scattering amplitude or conserved-current checkpoint. \\",
        r"\(P\) & Protocol/order: preparation--evolution--measurement order, circuit sequence, channel composition, perturbative expansion or source-local derivation step. \\",
        r"\(\Lambda,T,\Gamma,J,\Pi\) & Typed roads, directed transitions, transfer bridges, first-variation current candidates and repeated construction motifs. \\",
        r"\bottomrule",
        r"\end{longtable}",
        r"\section{Counts And Compactness}",
    ]
    lines.append(
        latex_escape(
            f"Artifact readiness: {v2.get('readiness') or 'not reported'}. "
            f"Selected grammar: {v2.get('selected_grammar') or 'not supplied'}."
        )
    )
    lines.extend(
        [
            r"\begin{longtable}{p{0.38\linewidth}p{0.20\linewidth}p{0.32\linewidth}}",
            r"\toprule",
            r"Layer & Count & Interpretation \\",
            r"\midrule",
            r"\endhead",
            rf"Primitive factor tokens & {int(compact.get('primitive_factor_token_count') or 0)} & \(\Omega+\Xi\), not a flat apparatus vocabulary \\",
            rf"Identity components & {int(compact.get('identity_component_count') or 5)} & two coordinates plus three attached completion fibers \\",
            rf"Relation tokens & {int(compact.get('relation_token_count') or 0)} & \(\Lambda,T,\Gamma,J\) relation or variation layers \\",
            rf"Derived regime tokens & {int(compact.get('derived_regime_token_count') or 0)} & \(A\) or \(A^\ast\), derived from product context \\",
            rf"Motif tokens & {int(compact.get('motif_token_count') or 0)} & repeated transition fragments \(\Pi\) \\",
            r"\bottomrule",
            r"\end{longtable}",
            r"\section{Evidence Boundary}",
        ]
    )
    claims = [str(x) for x in (v2.get("claims_supported") or []) if str(x).strip()]
    if claims:
        lines.append(r"\begin{itemize}")
        for claim in claims[:6]:
            lines.append(r"\item " + latex_escape(claim))
        lines.append(r"\end{itemize}")
    source_files = v2.get("source_files") or {}
    if source_files:
        lines.append(
            latex_escape(
                "The auxiliary grammar layer was loaded from transferred mechanism artifacts. These paths are evidence pointers inside the build, not book claims: "
                + "; ".join(f"{key}={value}" for key, value in source_files.items() if value)
            )
        )
    if grounding:
        lines.append(r"\section{Source Grounding Rates}")
        lines.append(r"\begin{longtable}{p{0.22\linewidth}p{0.18\linewidth}p{0.18\linewidth}p{0.22\linewidth}}")
        lines.append(r"\toprule")
        lines.append(r"Token kind & Grounded & Checked & Rate \\")
        lines.append(r"\midrule")
        lines.append(r"\endhead")
        for kind, row in grounding.items():
            try:
                rate = float(row.get("grounding_rate") or 0.0)
            except Exception:
                rate = 0.0
            lines.append(
                rf"{latex_escape(kind)} & {int(row.get('grounded') or 0)} & {int(row.get('checked') or 0)} & {rate:.4f} \\"
            )
        lines.append(r"\bottomrule")
        lines.append(r"\end{longtable}")
    lines.append(
        latex_escape(
            v2.get("claim_boundary")
            or "The auxiliary language is a representation-level mechanism grammar. Physical claims still require source equations and validation."
        )
    )
    return "\n\n".join(lines)


def _legacy_render_mechanism_guide(tree: Mapping[str, Any]) -> str:
    """Opening guide: define the mechanism tree and how to use it."""
    stats = tree.get("sparse_attention", {})
    count_routes = stats.get("count_gt_0_1", {})
    mean_routes = stats.get("mean_routes", {})
    branches = tree.get("branches", {})
    constructed = 35
    placements = 112
    try:
        manifest = load_optional_json(Path("discoveries/morphwiki_quantum/derivation_pages/manifest.json"))
        constructed = int(manifest.get("topic_specific_count", manifest.get("constructed_count", constructed)))
        placements = int(manifest.get("core_derived_count", manifest.get("evidence_placement_count", placements)))
    except Exception:
        pass

    lines: List[str] = [
        r"\chapter*{How To Use The Mechanism Tree}",
        r"\addcontentsline{toc}{chapter}{How To Use The Mechanism Tree}",
        r"\section*{What The Tree Is}",
        r"\addcontentsline{toc}{section}{What The Tree Is}",
        latex_escape(
            "This book is a derivation map for quantum topics. Each named topic is treated as a contribution to one "
            "prediction-making mechanism. The base object is a carrier or context jointly typed with an operator apparatus. "
            "Closure, readout, and ordered protocol attach when the topic requires them. Boundaries, fields, detectors, and encodings "
            "specify realizations. The page title is therefore not the root of the explanation; the root is the dependency that the page supplies."
        ),
        r"\begin{claimbox}",
        r"\noindent Mechanism-first reading: identify the operation a named topic performs in the quantum construction.",
        r"\par\smallskip\noindent\textbf{Constructor structure:} typed carrier--operator identity \(\oplus\) closure/readout/protocol completion \(\rightarrow\) physical realization. Derivations may add roles, project consequences, or rewrite laterally.",
        r"\end{claimbox}",
        r"\section*{Completion DAG And Source Constructor}",
        r"\addcontentsline{toc}{section}{Completion DAG And Source Constructor}",
        latex_escape(
            "The mechanism tree uses two graph layers. The completion DAG points from records with fewer constructor roles to records with more roles. "
            "It is a partial order of formal specification, not physical time and not a compulsory order of exposition. The source constructor follows adjacent equations inside papers and records completion, projection, and lateral rewrite."
        ),
        latex_escape(
            "This distinction matters because a complete theory is rarely written in one equation. The DAG measures how much of the role contract is explicit. "
            "The source constructor shows how authors distribute that contract across neighboring equations, often expanding a relation and then projecting it onto a term, limit, observable, or consequence."
        ),
        r"\begin{centeredalign}",
        r"\mathrm{identity}:&\quad \mathcal I_Q=((\mathcal H_C,\mathcal D_C),\mathcal O_C)\\",
        r"\mathrm{completion}:&\quad \mathcal F_Q=(\mathcal K_C,\mathcal E_C,\mathcal P_C)\\",
        r"\mathrm{source\ moves}:&\quad +\mathrm{role},\quad \mathrm{projection},\quad \mathrm{lateral\ rewrite}.",
        r"\end{centeredalign}",
        latex_escape(
            "Standard quantum mechanics already contains Hilbert spaces, operators, spectra, Born probabilities, and commutators. The corpus result concerns their organization: carrier and operator form the reusable typed identity, completion is attached locally, and source derivations move in both directions through completion rank."
        ),
        r"\section*{Why Hilbert Space Is Central}",
        r"\addcontentsline{toc}{section}{Why Hilbert Space Is Central}",
        "Hilbert space supplies the carrier on which states, operator domains, inner products, spectra, and probability measures are defined. A position or configuration space instead labels one possible representation of that carrier. The two spaces coincide neither conceptually nor generally.",
        r"For a spinless particle on a configuration space \(Q\) with measure \(\mu\), a pure state is a ray \([\psi]\) in \(\mathcal H=L^2(Q,d\mu)\). The function \(\psi(x)=\langle x|\psi\rangle\) is a representative of that ray in the generalized position basis; \(x\in Q\) labels a configuration, not the representation itself. Functions equal almost everywhere define the same vector, and vectors related by a global phase define the same pure state. For \(Q=\mathbb R^3\) with Lebesgue measure this becomes \(L^2(\mathbb R^3,d^3x)\), but spin gives \(L^2(Q,d\mu)\otimes\mathbb C^{2s+1}\), identical particles require symmetric or antisymmetric subspaces, and mixed states are density operators rather than rays.",
        r"\begin{centeredalign}",
        r"[\psi]\in\mathbb P(\mathcal H),\quad \ket\psi\sim e^{i\alpha}\ket\psi &\qquad \text{pure state ray}\\",
        r"\psi(x)=\langle x|\psi\rangle,\quad \Pr(X\in\Delta)=\int_\Delta|\psi(x)|^2d\mu(x) &\qquad \text{position representation}\\",
        r"\rho\ge0,\quad \operatorname{Tr}\rho=1,\quad \Pr_A(\Delta)=\operatorname{Tr}(\rho E_A(\Delta)) &\qquad \text{general state and readout}\\",
        r"A=A^\dagger,\quad A=\int_{\sigma(A)}\lambda\,dE_A(\lambda) &\qquad \text{operator-to-spectrum conversion}\\",
        r"\rho_t=U(t)\rho U(t)^\dagger,\quad U^\dagger U=I &\qquad \text{identity-preserving evolution.}",
        r"\end{centeredalign}",
        r"The carrier \((\mathcal H_C,\mathcal D_C)\) and its operator apparatus must be typed together. States inhabit the carrier, generators act on specified domains, observables supply spectral measures, and Born probabilities refer to those measures. A choice of carrier constrains the legal questions but does not select an outcome.",
        r"\section*{The Compact Representation}",
        r"\addcontentsline{toc}{section}{The Compact Representation}",
        latex_escape(
            "The compact representation is the minimal formal record needed to say what a quantum mechanism is doing. "
            "It is a compressed version of standard quantum mechanics:"
        ),
        r"\begin{claimbox}",
        r"\noindent\textbf{Compact tree:} carrier/context \(\leftrightarrow\) operator apparatus, with closure, readout, and protocol attached as required.",
        r"\par\smallskip\noindent Realization changes boundaries, fields, detectors, encodings, and scaling limits without forcing a new universal construction order.",
        r"\end{claimbox}",
        r"\begin{itemize}",
        r"\item \textbf{Context} means the experimental or mathematical setting in which a quantum question is posed: preparation, basis, boundary, gauge, detector, domain, or representation.",
        r"\item \textbf{Hilbert-space carrier and domain} means the Hilbert space, operator domain, and constraints selected by that context. Examples include normalization, positivity of a density operator, boundary conditions, gauge constraints, and domain conditions for an unbounded operator.",
        r"\item \textbf{Generator/evolution} means the Hamiltonian, unitary map, quantum channel, action, or other lawful map that transports the state before readout.",
        r"\item \textbf{Observable spectrum} means the allowed answer set of a measurable question, represented by a self-adjoint operator, projection-valued measure, POVM, or channel readout.",
        r"\item \textbf{Probability readout} means the Born or trace rule that turns the state and spectral channels into probabilities for observed outcomes.",
        r"\item \textbf{Compatibility constraint} means a restriction on which questions can be jointly resolved, usually expressed by commutators, uncertainty relations, contextuality tests, conservation laws, or admissibility checks.",
        r"\item \textbf{Boundary/protocol realization} means the physical or engineered implementation: a potential well, scattering boundary, cavity, field mode, detector, circuit, channel, or measurement protocol.",
        r"\end{itemize}",
        r"\begin{centeredalign}",
        r"\mathfrak M_Q &= (C,\mathcal H_C,\mathcal D_C,\rho,H_C,A_C,E_{A_C},\Pr,\mathcal K,\mathcal R)\\",
        r"C &:\ \text{context, preparation, basis, boundary, gauge, or detector arrangement}\\",
        r"\mathcal H_C,\mathcal D_C &:\ \text{admissible state space and operator domain}\\",
        r"\rho_t &= U_C(t)\rho U_C(t)^\dagger,\qquad U_C(t)=\exp(-iH_Ct/\hbar)\\",
        r"A_C &= \int_{\sigma(A_C)} \lambda\,dE_{A_C}(\lambda)\\",
        r"\Pr(\Delta\mid C,\rho,A) &= \operatorname{Tr}\!\left(\rho_t E_{A_C}(\Delta)\right)\\",
        r"\mathcal K &: \text{compatibility tests such as commutators, constraints, and admissibility checks}\\",
        r"\mathcal R &: \text{realization layer: boundary, field mode, detector, circuit, or scaling limit.}",
        r"\end{centeredalign}",
        latex_escape(
            "This representation explains the tree. Context selects the Hilbert-space carrier and operator domain. The wave function and density matrix are states on that carrier. "
            "The Hamiltonian and unitary operator contribute the generator. Observables and projection-valued measures contribute the spectral question. "
            "The Born rule contributes the probability readout. Commutators, uncertainty, Bell-type pages, and EPR-type pages contribute compatibility tests. "
            "Tunnelling, particle-in-a-box, scattering, fields, gauge theory, circuits, and channels contribute realization or protocol layers."
        ),
        r"\section*{Recipe For Reading A Page}",
        r"\addcontentsline{toc}{section}{Recipe For Reading A Page}",
        r"\begin{enumerate}",
        r"\item \textbf{Locate the page in the tree.} The branch tells which dependency of \(\mathfrak M_Q\) the page mainly specifies.",
        r"\item \textbf{Fill the compact tuple.} Identify \(C\), \(\mathcal H_C\), \(\rho\), \(H_C\) or the relevant map, \(A_C\), the spectral measure or readout, and any compatibility condition.",
        r"\item \textbf{Read the topic page in full.} Every retained topic remains in the book. Native equations and source links show how its local construction differs from the shared branch structure.",
        r"\item \textbf{Read anomalies as diagnostics.} An anomaly is a junction where the topic uses several roles at once; the diagnosis is decomposition, not rejection.",
        r"\item \textbf{Use transfer carefully.} A mechanism can be transferred only when the state carrier, operator role, readout, and compatibility test survive the move; field-specific nouns may change.",
        r"\end{enumerate}",
        r"\section*{What Was Found In This Run}",
        r"\addcontentsline{toc}{section}{What Was Found In This Run}",
    ]
    spectral_count = int(count_routes.get("spectral_operator_route", 0))
    transport_count = int(count_routes.get("transport_flow_route", 0))
    boundary_count = int(count_routes.get("boundary_weak_form_route", 0))
    incompat_count = int(count_routes.get("commutator_incompatibility_route", 0))
    protocol_count = int(count_routes.get("discrete_protocol_route", 0))
    total_pages = sum(len((branches.get(branch_id) or {}).get("pages") or []) for branch_id in BRANCH_ORDER)
    lines.append(
        latex_escape(
            f"The current export contains {total_pages} quantum pages. Of these, {constructed} have topic-specific equation skeletons or explicit constructor overrides, "
            f"and {placements} are expanded from the compact constructor as core-derived mechanisms. The sparse-attention profile is strongly operator/spectral: "
            f"{spectral_count} pages exceed the operator/spectrum threshold, with mean signal {float(mean_routes.get('spectral_operator_route', 0.0)):.3f}. "
            f"State evolution is also broad ({transport_count} pages), while boundary/context ({boundary_count}), incompatibility ({incompat_count}), and explicit protocol ({protocol_count}) are more selective. "
            "The practical result is a compact reading of quantum theory as operator-to-spectrum conversion under context and compatibility constraints."
        )
    )
    lines.append(
        latex_escape(
            "This is the main structural finding of the rewrite. Quantum theory can be introduced as a constructor in which "
            "particles, waves, fields, detectors, boundaries, circuits, and interpretations are roles attached to a smaller "
            "state-operator-readout spine. The portable unit is the legal transformation from context and state to spectral readout."
        )
    )
    lines.extend([r"\section*{Branch Map}", r"\addcontentsline{toc}{section}{Branch Map}", r"\begin{longtable}{p{0.26\linewidth}p{0.50\linewidth}r}", r"\toprule", r"Role & Use in the derivation & Pages \\", r"\midrule", r"\endhead"])
    for branch_id in BRANCH_ORDER:
        branch = branches.get(branch_id) or {}
        lines.append(
            rf"{latex_escape(branch.get('title', branch_id))} & {latex_escape(branch.get('definition', ''))} & {len(branch.get('pages') or [])} \\"
        )
    lines.extend([r"\bottomrule", r"\end{longtable}"])
    return "\n".join(lines)


def render_mechanism_guide(tree: Mapping[str, Any]) -> str:
    """Open the book with the physical principle that connects its topics."""
    branches = tree.get("branches") or {}
    total_pages = sum(len((branches.get(branch_id) or {}).get("pages") or []) for branch_id in BRANCH_ORDER)
    lines: List[str] = [
        r"\chapter*{When External Conditions Become Quantum Physics}",
        r"\addcontentsline{toc}{chapter}{When External Conditions Become Quantum Physics}",
        latex_escape(
            "Quantum theory changes when a quantity once treated as fixed becomes part of the physical state or its dynamics. "
            "A prescribed electromagnetic potential becomes a quantum field. A classical measuring device becomes an interacting quantum subsystem. "
            "A passive environment becomes a source of memory when its correlations influence later motion. Quantum gravity asks the same question of geometry itself."
        ),
        latex_escape(
            "In each case, the variables retained by the theory must determine future observable probabilities, and equivalent physical transformations must compose to the same result. "
            "We call this condition predictive closure."
        ),
        r"\begin{claimbox}",
        latex_escape(PREDICTIVE_CLOSURE_PRINCIPLE),
        rf"\[{PREDICTIVE_CLOSURE_LATEX}\]",
        r"\end{claimbox}",
        latex_escape(
            "The first relation compares two histories that produce the same declared state. Their later probabilities must agree. "
            "If they do not, the state has discarded a physically active correlation; an internal coordinate or memory kernel restores the missing dependence. "
            "The second relation compares two physically equivalent paths. Their transformations must agree when applied to the same state. "
            "A non-neutral loop records curvature, frustration, or another obstruction to global composition."
        ),
        latex_escape(
            "Predictive closure also determines the boundary between a mechanism and its realization. A parameter remains external while it selects a member of a fixed theory. "
            "It enters the mechanism when it changes the state space, operator domain, dynamical map, admissibility condition, observable, or operation order."
        ),
        rf"\[{ROLE_PROMOTION_CRITERION_LATEX}\]",
        latex_escape(
            "A wall illustrates the distinction. Its position can parameterize one boundary-value problem, while its boundary condition selects the domain of the Hamiltonian. "
            "The first quantity belongs to a realization. The second fixes the spectrum and therefore belongs to the closure of the mechanism."
        ),
        rf"\[{CONSTRUCTOR_CHAIN_LATEX}\]",
        rf"\[{PHYSICAL_STATE_LATEX}\]",
        r"A physical state \(q\) contains the information required to determine later observables at the chosen resolution. "
        r"The admissible states form \(\Xi\), and \(\Omega\) acts on them as a generator, channel, projection, constraint, or observable. "
        r"Their pair \(M=(\Omega,\Xi)\) fixes which operation acts on which physical degrees of freedom. "
        r"Closure \(C\) fixes domains and admissibility, \(R\) maps states to observable predictions, and \(P\) fixes the order of preparation, control, and measurement. "
        r"The realization \(A\) supplies the fields, material, parameters, geometry, initial data, and apparatus of a particular experiment.",
        latex_escape(
            "Each clause prevents a specific ambiguity. Without the state space, the operator has no domain. Without closure, its solutions or probabilities need not be admissible. "
            "Without an observable, the formal evolution has no predicted measurement. Without a protocol, noncommuting operations have no defined order."
        ),
        latex_escape(
            "For a quantum state, this identity reduces to a state space, an evolution map, and a positive measurement law."
        ),
        r"\begin{centeredalign}",
        r"\Xi_Q &= (\mathcal H,\mathcal D,\mathcal S),\qquad \rho_0\in\mathcal S(\mathcal H),\\",
        r"\rho_P &= \mathcal E_P(\rho_0),\qquad \mathcal E_P\ \text{completely positive and trace preserving},\\",
        r"p(y\mid P) &= \operatorname{Tr}(E_y\rho_P),\qquad E_y\ge0,\quad \sum_yE_y=I.",
        r"\end{centeredalign}",
        latex_escape(
            "The Hilbert space, state class, and operator domain define the admissible states. The channel describes their evolution under protocol P. "
            "The positive operators E_y define the possible outcomes, and the trace rule assigns their probabilities. "
            "Unitary dynamics, open-system evolution, measurement, and feedback differ in which physical structures enter these three lines."
        ),
        latex_escape(
            f"These relations order the following {total_pages} topics by the physical role each one fixes or changes. "
            "Entanglement belongs to composite state structure. Commutators belong to observable algebra. Bell experiments join the two through local measurements. "
            "Gauge constraints select physical states, while renormalization changes the effective law with scale. "
            "This ordering exposes transitions between theories that conventional subject headings place in separate fields."
        ),
    ]
    return "\n".join(lines)


def compact_operator_formulation_chapter() -> str:
    """State the nested language and its quantum specialization."""
    lines: List[str] = [
        r"\chapter{The Physical Identity Of A Quantum Mechanism}",
        r"\begin{claimbox}",
        latex_escape(
            "Quantum predictions join an admissible state space to an operation, the conditions under which that operation is defined, and an observable consequence. "
            "The same equation can play different roles when its domain, state, or measurement changes."
        ),
        r"\end{claimbox}",
        r"\section{Nested Construction}",
        rf"\[{CONSTRUCTOR_CHAIN_LATEX}\]",
        r"A physical state \(q\) belongs to \(\Xi\). The operation \(\Omega\) acts on \(q\), while \(M=(\Omega,\Xi)\) identifies the law together "
        r"with the state space on which it is meaningful. Closure, an observable map, and protocol give the operational identity. "
        r"The realization layer fixes the material or field content, scales, parameter values, initial and boundary data, geometry, drives, "
        r"and apparatus needed for a particular calculation or experiment.",
        r"\section{State Space And Operation Must Agree}",
        r"\begin{centeredalign}",
        r"\Xi_Q &= (\mathcal H,\mathcal D,\mathcal S,\mathcal A_{\rm obs}),\\",
        r"q&=\rho\in\mathcal S(\mathcal H),\\",
        r"\Omega_Q &= \{G,\mathcal E,\{E_y\},\mathcal U,\ldots\},\\",
        r"M_Q &= (\Omega_Q,\Xi_Q).",
        r"\end{centeredalign}",
        r"The state space \(\Xi_Q\) contains the Hilbert or Fock space, admissible density operators, operator domains, and, when needed, a subsystem "
        r"or observable algebra. The operation \(\Omega_Q\) contains generators, channels, observables, symmetry actions, projections, or their compositions. "
        r"Neither factor can be interpreted without the other: the state space fixes what operations are defined, and the operation selects which structure "
        r"of the state enters a prediction.",
        r"\section{Completion And Realization}",
        r"Normalization, positivity, self-adjointness, domains, and gauge constraints form the closure \(C_Q\). "
        r"Spectral measures, positive operator-valued measures, correlators, currents, and detector outcomes form the observable map \(R_Q\). "
        r"Preparation, evolution, control, and measurement order form the protocol \(P_Q\). The realization \(A_Q\) then fixes the particles, fields, material, geometry, parameter values, drives, and apparatus.",
        r"\begin{centeredalign}",
        r"I_{\mathrm{op},Q} &= ((\Omega_Q,\Xi_Q);C_Q,R_Q,P_Q),\\",
        r"I_{\mathrm{real},Q} &= (I_{\mathrm{op},Q};A_Q),\\",
        r"I_{\mathrm{real},Q} &\longmapsto p(y),\ \langle O\rangle,\ S(\omega),\ J,\ \text{or another stated consequence}.",
        r"\end{centeredalign}",
        latex_escape(
            "Changing the state space can destroy self-adjointness, locality, or normalization. Changing the protocol can change the channel itself. "
            "The closure and observable must therefore be derived again whenever one of these physical roles changes."
        ),
        r"\section{Transformations And Compatibility}",
        r"\begin{centeredalign}",
        r"I_i=((\Omega_i,\Xi_i);C_i,R_i,P_i)\xrightarrow{\tau}I_j=((\Omega_j,\Xi_j);C_j,R_j,P_j).",
        r"\end{centeredalign}",
        r"The transformation \(\tau\) relates two descriptions or realizations. It may change representation, complete a partial model, project onto a reduced "
        r"description, transfer a law to another state space, compose operations, or take a controlled limit. Its physical content is the relation retained "
        r"between the two constructions: an amplitude, expectation value, operator algebra, balance law, probability distribution, or approximation with a stated error.",
        r"The retained relation is tested by maps that carry states and outputs between the two descriptions.",
        r"\begin{centeredalign}",
        r"\alpha &: \Xi_A\longrightarrow\Xi_B,\\",
        r"\beta &: \Omega_A(\Xi_A)\longrightarrow\Omega_B(\Xi_B),\\",
        r"\Delta_{\alpha,\beta}&=\Omega_B\alpha-\beta\Omega_A.",
        r"\end{centeredalign}",
        r"The map \(\alpha\) carries physical states from the source description to the target, while \(\beta\) carries the corresponding outputs. "
        r"Exact compatibility means that acting first and then mapping gives the same result as mapping first and acting in the target. "
        r"The residual \(\Delta_{\alpha,\beta}\) records the part of the source dynamics that the proposed target description cannot represent.",
        rf"\[{COMPATIBILITY_BRANCH_LATEX}\]",
        r"A vanishing residual, together with agreement of the stated observables, identifies another realization of the same mechanism. "
        r"A residual with no stable form rejects the proposed transfer. When \(\Delta_{\alpha,\beta}\) recurs, obeys its own closure relation, and changes "
        r"a measurable consequence, it becomes a candidate correction operator, interaction, boundary term, or hidden state variable.",
    ]
    return "\n".join(lines)


def quantum_structure_chapter() -> str:
    """Relate quantum frontiers through changes of physical role."""
    lines: List[str] = [
        r"\chapter{When External Structure Becomes Dynamical}",
        r"\begin{claimbox}",
        latex_escape(
            "A background field, geometry, environment, boundary, constraint, or control sequence changes the theory when it alters the state space, dynamics, operator domain, observable, or operation order."
        ),
        r"\end{claimbox}",
        r"\section{Backgrounds, Geometry, And Environment}",
        latex_escape(
            "A background field supplies prescribed coefficients to a Hamiltonian. Quantizing that field enlarges the Hilbert space and gives the field its own conjugate variables, fluctuations, and quanta. "
            "Quantum electrodynamics makes this change for the electromagnetic field. Quantum gravity asks whether distances and causal relations must likewise participate in the quantum state."
        ),
        latex_escape(
            "The same change occurs in reduced dynamics. Tracing over an environment produces closed Markovian dynamics only when discarded correlations do not influence the future. "
            "When they return, the reduced state is incomplete. Retaining environmental coordinates or a memory kernel restores predictive closure. "
            "Decoherence, non-Markovian dynamics, and measurement back-action therefore differ by which environmental correlations remain physically active."
        ),
        r"\section{Domains, Constraints, And Controlled Dynamics}",
        latex_escape(
            "A boundary condition enters the physical law when it defines the operator domain. The same differential expression can then possess different self-adjoint extensions and different spectra. "
            "Confinement, tunnelling, scattering, and topological edge modes follow from this dependence on the domain."
        ),
        latex_escape(
            "Constraints alter the state space rather than the operator domain. Gauge redundancy and exchange symmetry begin as restrictions on allowed descriptions. Imposing them selects the physical Hilbert-space sectors. "
            "Gauss constraints remove gauge-equivalent vectors, while Bose or Fermi symmetry fixes the admissible many-particle states. "
            "Charges, particle statistics, and observable algebras follow from the surviving sectors."
        ),
        latex_escape(
            "A sequence of gates, measurements, and conditional controls becomes a single physical map after composition. Its order can change the resulting unitary or channel. "
            "In quantum computing, feedback, error correction, and Floquet control, the experimental sequence is therefore part of the dynamics implemented during the experiment."
        ),
        r"\section{One Principle Across The Frontiers}",
        latex_escape(
            "Each enlargement repairs the same failure. A smaller theory omitted information required for future probabilities or for consistent composition. "
            "The minimal enlargement identifies the missing physical object: a field, an environmental coordinate, an operator domain, a constrained state sector, or a composed channel. "
            "Quantum theories can therefore be compared by the physical role of their variables rather than by the historical field in which those variables were introduced."
        ),
    ]
    return "\n".join(lines)


def global_composition_chapter() -> str:
    """Connect quantum curvature, frustration, and memory through composition."""
    lines: List[str] = [
        r"\chapter{Global Composition: Curvature, Frustration, And Memory}",
        r"\begin{claimbox}",
        latex_escape(
            "Local quantum relations define one global physical state only when their ordered composition is independent of the path used to connect the descriptions. "
            "Curvature, frustration, and memory arise when this composition retains information that is absent from the endpoint variables."
        ),
        r"\end{claimbox}",
        r"\section{From Local Transformations To A Global State}",
        r"Let \(T_{ij}\) carry a state, basis, or constraint from one local description to the next. A path is an ordered composition of these maps. "
        r"It can describe transport through parameter space, constraints around an interaction loop, or a sequence of interventions followed by relaxation. "
        r"For a closed path \(\gamma\), the composite map is",
        r"\begin{equation*}",
        r"\mathfrak H_\gamma=T_{0n}T_{n,n-1}\cdots T_{21}T_{10}.",
        r"\end{equation*}",
        r"For changes of description, \(\mathfrak H_\gamma=I\) means that the local identifications fit one path-independent global description. "
        r"A physical protocol need not return the state when its external controls close a loop. The corresponding completeness test compares histories "
        r"that end at the same retained state. If their later observables differ, the retained endpoint variables have omitted physically active path information.",
        r"\section{Curvature Records Transport Around A Loop}",
        latex_escape(
            "A quantum state transported around a loop can return with a phase or an internal rotation. In gauge theory the path-ordered exponential of the connection gives the loop operator; "
            "for a small loop its departure from the identity is set by the field strength. Berry curvature gives the corresponding relation in parameter space."
        ),
        r"\begin{centeredalign}",
        r"W(\gamma)&=\operatorname{Tr}\,\mathcal P\exp\!\left(i\oint_\gamma A_\mu\,dx^\mu\right),\\",
        r"\mathfrak H_\gamma&=I+iF_{\mu\nu}S^{\mu\nu}+O(S^2).",
        r"\end{centeredalign}",
        latex_escape(
            "The connection specifies how neighboring descriptions are compared; the curvature measures the infinitesimal failure of those comparisons to be path independent. "
            "The loop, rather than any one local coordinate choice, carries the observable geometric information."
        ),
        r"\section{Frustration Records Incompatible Local Preferences}",
        latex_escape(
            "In a frustrated quantum magnet, each bond can impose a well-defined local preference while no spin configuration satisfies every bond around a loop. "
            "For an Ising loop, a negative product of bond signs is the simplest obstruction:"
        ),
        r"\begin{equation*}",
        r"\prod_{\langle ij\rangle\in\gamma}\operatorname{sign}J_{ij}=-1.",
        r"\end{equation*}",
        latex_escape(
            "The mismatch survives every local reassignment of spin signs and is therefore a property of the loop. In quantum magnets the same logic is carried by loop operators, flux sectors, or non-commuting bond terms. "
            "The loop flux or frustration sector becomes an additional physical label that local bond variables alone cannot determine."
        ),
        r"\section{Memory Records Hidden Paths Through State Space}",
        r"A reduced quantum state is complete only if equal present states give equal future observable statistics. Let \(h_1\) and \(h_2\) be two histories "
        r"that produce the same retained state \(q\). The state is incomplete when hidden system--environment correlations make a later observable distinguish the histories:",
        r"\begin{centeredalign}",
        r"q(h_1)=q(h_2),\qquad R\Phi_t(h_1)&\ne R\Phi_t(h_2),\\",
        r"V_{t+s}&\ne V_tV_s.",
        r"\end{centeredalign}",
        latex_escape(
            "The second relation is the failure of the reduced propagator to compose as a Markov semigroup. A memory kernel keeps the missing history explicit; an auxiliary mode or correlation coordinate enlarges the state and can restore a local evolution law. "
            "For order memory, two write operations followed by the same relaxation are distinguishable precisely when their ordered products leave different retained states."
        ),
        r"\begin{equation*}",
        r"R\mathcal R_tW_BW_A(q_0)\ne R\mathcal R_tW_AW_B(q_0).",
        r"\end{equation*}",
        r"\section{The Shared Physical Content}",
        r"Gauge curvature, frustrated loops, and reduced-state memory attach different physical meanings to \(\mathfrak H_\gamma\). Their common content is failure "
        r"of global composition: locally valid relations do not assemble into a path-independent state. The obstruction identifies what the smaller description has omitted. "
        r"A connection and field strength complete local gauge comparisons; a flux or defect sector completes an incompatible interaction network; a memory kernel "
        r"or hidden coordinate completes reduced dynamics. In each case the enlarged state distinguishes paths that the original endpoint variables identified as the same.",
    ]
    return "\n".join(lines)


def constructor_rewiring_chapter(root: Path) -> str:
    """Render source-grounded equivalences between quantum descriptions."""
    report = load_optional_json(root / "quantum_constructor_rewiring.json")
    connections = report.get("connections") if report else None
    if not isinstance(connections, list) or not connections:
        return ""

    lines: List[str] = [
        r"\chapter{Equivalence Across Quantum Descriptions}",
        r"\begin{claimbox}",
        latex_escape(
            "Two quantum descriptions represent the same physical mechanism when a map between their states preserves the dynamics and the stated observable consequences."
        ),
        r"\end{claimbox}",
        latex_escape(
            "Quantum theory uses several forms of this equivalence. A change of representation carries states and observables together. "
            "A change of carrier embeds the same operator algebra in another Hilbert space. A reduced description projects onto fewer degrees of freedom, "
            "and a measurement or boundary condition completes the relation by fixing its observable content. In each case the equivalence is decided by the quantity that remains unchanged."
        ),
    ]

    for connection in connections:
        title = str(connection.get("title") or "Constructor connection")
        topics = ", ".join(str(value).replace("_", " ").title() for value in connection.get("topics") or [])
        invariant = str(connection.get("invariant") or "")
        rewiring = str(connection.get("rewiring") or "")
        test = str(connection.get("test") or "")
        equations = [str(x) for x in (connection.get("equations") or []) if str(x).strip()]
        lines.extend(
            [
                rf"\section{{{latex_escape(title)}}}",
                latex_escape(f"This relation connects {topics}."),
                latex_escape(rewiring_description_text(rewiring)),
                latex_escape(f"The retained physical relation is {invariant}" + ("." if invariant and not invariant.endswith(".") else "")),
            ]
        )
        if equations:
            lines.append(r"\begin{centeredalign}")
            for index, equation in enumerate(equations):
                lines.append(equation + (r"\\" if index + 1 < len(equations) else ""))
            lines.append(r"\end{centeredalign}")
        if test:
            lines.append(latex_escape(equivalence_condition_text(test)))
    return "\n".join(lines)


def quantum_discovery_chapter() -> str:
    """Explain how transfer and obstruction extend a physical theory."""
    lines: List[str] = [
        r"\chapter{Theory Extension By Transfer And Obstruction}",
        r"\begin{claimbox}",
        latex_escape(
            "A physical relation can survive in another state space, or its failure can identify the term missing from the target theory. Exact compatibility and structured incompatibility are therefore two outcomes of the same transformation."
        ),
        r"\end{claimbox}",
        r"\section{Incomplete Mechanisms}",
        latex_escape(
            "A law can be stated before the physical degrees of freedom on which it acts are known. Conversely, a state space can be specified before its governing operation is fixed. These one-sided descriptions occur at the boundary between an abstract theory and a physical realization."
        ),
        r"\begin{centeredalign}",
        r"(\Omega,0_{\Xi})+(0_{\Omega},\Xi')&\longrightarrow(\Omega,\Xi')\\",
        r"&\longrightarrow(\Omega,\Xi';\widehat C,\widehat R,\widehat P)\\",
        r"&\longrightarrow I_{\mathrm{real}}'.",
        r"\end{centeredalign}",
        latex_escape(
            "The combined theory exists only if the operation has a domain on the target state space. Its closure must admit physical states, and its observable must produce normalized probabilities. These requirements determine the additional terms introduced by the new realization."
        ),
        r"\section{Exact Transfer}",
        rf"\[{COMPATIBILITY_RESIDUAL_LATEX}\]",
        latex_escape(
            "The maps alpha and beta carry source states and outputs into the target description. A vanishing residual means that evolution followed by translation gives the same state as translation followed by target evolution. Agreement of the corresponding observables then establishes another physical realization of the retained mechanism."
        ),
        latex_escape(
            "Schrodinger, Heisenberg, and path-integral descriptions provide standard examples. Their variables and intermediate objects differ, while amplitudes and expectation values agree on the common domain. Quantum simulation uses the same structure when an encoded target algebra reproduces selected correlators in another physical device."
        ),
        r"\section{Structured Failure}",
        latex_escape(
            "A nonzero residual separates two physical possibilities. An irregular residual reflects an incompatible comparison. A residual that recurs across states or scales and obeys a closure relation has acquired the form of a physical operator."
        ),
        r"\begin{equation*}",
        r"\Delta\longmapsto\Omega',\ \Xi',\ C',\ R',\ P',\ \text{or }A'.",
        r"\end{equation*}",
        latex_escape(
            "Promotion into Omega introduces a correction law or interaction. Promotion into Xi adds a hidden degree of freedom or state sector. Promotion into C changes the admissible domain. Promotion into P makes operation order part of the dynamics. The enlarged theory is fixed by the smallest promotion that restores predictive closure."
        ),
        r"\section{Observable Consequences}",
        latex_escape(
            "The promoted term becomes physical when it changes an observable that was not used to define it. Removing the obstructing coupling must remove that consequence. Curvature, memory, edge flux, and effective interactions are familiar outcomes of this logic: each retains information that the smaller state or transformation law had discarded."
        ),
    ]
    return "\n".join(lines)


def _legacy_render_book(root: Path, max_pages_per_branch: Optional[int] = None) -> str:
    tree = load_json(root / "quantum_mechanism_tree.json")
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: List[str] = []
    lines.extend(
        [
            r"\documentclass[11pt,oneside]{book}",
            r"\usepackage[a4paper,margin=1in]{geometry}",
            r"\usepackage{fontspec}",
            r"\usepackage{amsmath,amssymb}",
            r"\usepackage{booktabs,longtable,array}",
            r"\usepackage{xcolor}",
            r"\usepackage{titlesec}",
            r"\usepackage[most]{tcolorbox}",
            r"\usepackage{hyperref}",
            r"\hypersetup{colorlinks=true,linkcolor=blue!55!black,urlcolor=blue!55!black,citecolor=blue!55!black}",
            r"\pagestyle{plain}",
            r"\emergencystretch=3em",
            r"\definecolor{quantumgreen}{HTML}{5B7F2A}",
            r"\definecolor{softgray}{HTML}{F5F6F2}",
            r"\definecolor{ink}{HTML}{1C1E1A}",
            r"\titleformat{\chapter}[display]{\normalfont\huge\bfseries\color{ink}}{\chaptertitlename\ \thechapter}{14pt}{\Huge}",
            r"\newtcolorbox{claimbox}{colback=softgray,colframe=quantumgreen!65!black,arc=2pt,boxrule=0.7pt,left=8pt,right=8pt,top=6pt,bottom=6pt}",
            r"\newenvironment{centeredalign}{\[\begin{gathered}}{\end{gathered}\]}",
            r"\newcommand{\ket}[1]{\lvert #1\rangle}",
            r"\newcommand{\bra}[1]{\langle #1\rvert}",
            r"\begin{document}",
            r"\frontmatter",
            r"\begin{titlepage}",
            r"\centering",
            r"\vspace*{1.5cm}",
        r"{\Huge\bfseries Quantum Theory\par}",
        r"\vspace{0.12cm}",
        r"{\Huge\bfseries Through Physical Roles\par}",
            r"\vspace{1.2cm}",
            r"{\large Synthetix Institute\par}",
            rf"{{\large Generated {latex_escape(generated)}\par}}",
            r"\vfill",
            r"\begin{claimbox}",
            r"\noindent This book reorganizes quantum theory away from historical article names and toward the recurring construction detected across the quantum page archive: context-selected Hilbert space, state carrier, generator, spectral question, probability/readout, compatibility limits, boundary realization, many-mode extension, and protocols.",
            r"\end{claimbox}",
            r"\end{titlepage}",
            r"\tableofcontents",
        ]
    )
    lines.append(render_mechanism_guide(tree))
    lines.extend(
        [
            render_preamble(tree),
            r"\mainmatter",
            r"\part{The Mechanism Tree}",
            r"\chapter{Root Construction}",
            r"\begin{claimbox}",
            latex_escape(tree["root"]["definition"]),
            r"\end{claimbox}",
            r"\section{Re-Derivation Path}",
            r"\begin{enumerate}",
            r"\item \textbf{Type the identity.} Specify the Hilbert-space carrier, operator domain, state class, and operator apparatus together. Neither carrier nor operator is complete without the other.",
            r"\item \textbf{Attach completion.} Add normalization, symmetry, compatibility, spectral readout, probability assignment, or an ordered protocol where the problem requires it.",
            r"\item \textbf{Choose a realization.} State how boundaries, fields, scaling limits, detectors, gauges, or encodings embody the typed identity.",
            r"\item \textbf{Follow the derivation moves.} Track when a source equation adds a role, projects a relation onto a consequence, or rewrites the same role in another representation.",
            r"\end{enumerate}",
            "\n".join(
                [
                    r"\begin{centeredalign}",
                    r"B &\longmapsto \rho_B\\",
                    r"\rho_t &= U_t \rho_B U_t^\dagger\\",
                    r"O &= \sum_i \lambda_i P_i\\",
                    r"p_i &= \operatorname{Tr}(P_i \rho_t)\\",
                    r"[O_1,O_2] &\ne 0.",
                    r"\end{centeredalign}",
                ]
            ),
            r"\chapter{Sparse Attention Summary}",
        ]
    )
    stats = tree.get("sparse_attention", {})
    mean_routes = stats.get("mean_routes", {})
    count_routes = stats.get("count_gt_0_1", {})
    lines.extend(
        [
            r"\begin{longtable}{p{0.50\linewidth}p{0.18\linewidth}p{0.20\linewidth}}",
            r"\toprule",
            r"Operation & Mean signal & Pages above 0.10 \\",
            r"\midrule",
            r"\endhead",
        ]
    )
    route_names = {
        "transport_flow_route": "State evolution",
        "constraint_closure_route": "Normalization and admissibility",
        "spectral_operator_route": "Observables and spectra",
        "boundary_weak_form_route": "Preparation and boundary context",
        "commutator_incompatibility_route": "Incompatible questions",
        "discrete_protocol_route": "Controlled update protocol",
    }
    for key, name in route_names.items():
        lines.append(rf"{latex_escape(name)} & {float(mean_routes.get(key, 0.0)):.3f} & {int(count_routes.get(key, 0))} \\")
    lines.extend([r"\bottomrule", r"\end{longtable}"])
    lines.append(
        latex_escape(
            "The dominant recurrent signal is observables and spectra. Evolution, context, incompatibility, "
            "closure, and protocol are branch-forming operations. This is why the book begins with admissible context, "
            "state carrier, generator, and legal question rather than with particles or measurement folklore."
        )
    )
    lines.append(compact_operator_formulation_chapter())
    dependency_chapter = constructor_dependency_chapter(root)
    if dependency_chapter:
        lines.append(dependency_chapter)
    rewiring_chapter = constructor_rewiring_chapter(root)
    if rewiring_chapter:
        lines.append(rewiring_chapter)
    if os.environ.get("MORPHWIKI_EXPOSE_INTERNAL_METHOD", "").strip() == "1":
        v2_chapter = render_v2_language_chapter(tree)
        if v2_chapter:
            lines.append(v2_chapter)
    lines.append(validation_layers_chapter(root))
    sparse_chapter = sparse_attention_results_chapter(root)
    if sparse_chapter:
        lines.append(sparse_chapter)
    lines.extend([r"\chapter{Anomalies And Leads}", r"\section{Structural Anomalies}"])
    lines.append(
        latex_escape(
            "The labels below describe why a page is structurally interesting in the mechanism tree. They do not describe the literal object named by the page."
        )
    )
    lines.append(r"\begin{itemize}")
    for label, explanation in ANOMALY_LABEL_EXPLANATIONS.items():
        public_name = ANOMALY_PUBLIC_NAMES.get(label, label)
        lines.append(rf"\item \textbf{{{latex_escape(public_name)}}}: {latex_escape(explanation)}.")
    lines.append(r"\end{itemize}")
    lines.append(r"\begin{itemize}")
    for item in tree.get("anomalies", [])[:18]:
        explanation = anomaly_public_explanation(item)
        lines.append(rf"\item \textbf{{{latex_escape(item.get('title'))}}}. {latex_escape(explanation)}")
    lines.append(r"\end{itemize}")
    lines.extend([r"\section{Research Leads}", r"\begin{itemize}"])
    for lead in tree.get("discovery_leads", []):
        lines.append(r"\item " + latex_escape(lead))
    lines.extend([r"\end{itemize}", r"\part{Branch Chapters}"])

    for branch_id in BRANCH_ORDER:
        branch = tree["branches"][branch_id]
        lines.append(rf"\chapter{{{latex_escape(branch['title'])}}}")
        lines.append(r"\begin{claimbox}")
        lines.append(latex_escape(branch["definition"]))
        lines.append(r"\end{claimbox}")
        lines.append(r"\section{Why This Branch Exists}")
        lines.append(latex_escape(branch["insight"]))
        lines.append(r"\section{Page Map}")
        lines.append(branch_table(branch))
        pages_all = list(branch.get("pages") or [])
        lines.append(r"\section{Mechanism Pages}")
        lines.append(
            latex_escape(
                "Each page below is read as a specialization of the compact quantum constructor. Topic-specific pages use explicit equations or overrides; core-derived pages use the branch-level equation form associated with their mechanism role."
            )
        )
        pages = pages_all
        if max_pages_per_branch is not None:
            pages = pages[:max_pages_per_branch]
        if not pages:
            lines.append(latex_escape("No pages were assigned to this mechanism role in the current export."))
        else:
            for idx, row in enumerate(pages, 1):
                lines.append(page_entry(root, row, idx, branch_id, branch))

    lines.extend(
        [
            r"\backmatter",
            r"\chapter{Source Boundary}",
            latex_escape(
                "The generated page archive and tree record the source equations used for this synthesis. "
                "ArXiv links are evidence pointers, not claims that any individual paper proves the whole branch."
            ),
            r"\end{document}",
        ]
    )
    return center_equation_rows(public_theory_language("\n\n".join(lines)))


def render_book(root: Path, max_pages_per_branch: Optional[int] = None) -> str:
    """Render the public discovery-oriented book and optional method appendices."""
    tree = load_json(root / "quantum_mechanism_tree.json")
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: List[str] = [
        r"\documentclass[11pt,oneside]{book}",
        r"\usepackage[a4paper,margin=1in]{geometry}",
        r"\usepackage{fontspec}",
        r"\usepackage{amsmath,amssymb}",
        r"\usepackage{booktabs,longtable,array}",
        r"\usepackage{xcolor}",
        r"\usepackage{titlesec}",
        r"\usepackage[most]{tcolorbox}",
        r"\usepackage{hyperref}",
        r"\hypersetup{colorlinks=true,linkcolor=blue!55!black,urlcolor=blue!55!black,citecolor=blue!55!black}",
        r"\pagestyle{plain}",
        r"\emergencystretch=3em",
        r"\definecolor{quantumgreen}{HTML}{3F6F5A}",
        r"\definecolor{softgray}{HTML}{F5F6F2}",
        r"\definecolor{ink}{HTML}{1C1E1A}",
        r"\titleformat{\chapter}[display]{\normalfont\huge\bfseries\color{ink}\raggedright}{\chaptertitlename\ \thechapter}{14pt}{\Huge}",
        r"\newtcolorbox{claimbox}{colback=softgray,colframe=quantumgreen!70!black,arc=2pt,boxrule=0.7pt,left=8pt,right=8pt,top=6pt,bottom=6pt}",
        r"\newenvironment{centeredalign}{\[\begin{gathered}}{\end{gathered}\]}",
        r"\newcommand{\ket}[1]{\lvert #1\rangle}",
        r"\newcommand{\bra}[1]{\langle #1\rvert}",
        r"\begin{document}",
        r"\frontmatter",
        r"\begin{titlepage}",
        r"\centering",
        r"\vspace*{1.7cm}",
        r"{\Huge\bfseries Quantum Theory\par}",
        r"\vspace{0.12cm}",
        r"{\Huge\bfseries Through Physical Roles\par}",
        r"\vspace{1.2cm}",
        r"{\large Synthetix Institute\par}",
        rf"{{\large Generated {latex_escape(generated)}\par}}",
        r"\vfill",
        r"\begin{claimbox}",
        r"\noindent Quantum theories differ in what they treat as state, dynamics, constraint, measurement, protocol, or external realization. Predictive closure connects these choices and identifies the physical structure missing from an incomplete description.",
        r"\end{claimbox}",
        r"\end{titlepage}",
        r"\tableofcontents",
        render_mechanism_guide(tree),
        r"\mainmatter",
        r"\part{Predictive Closure And Physical Role}",
        compact_operator_formulation_chapter(),
        quantum_structure_chapter(),
        global_composition_chapter(),
    ]

    rewiring = constructor_rewiring_chapter(root)
    if rewiring:
        lines.append(rewiring)
    lines.append(quantum_discovery_chapter())

    for part_title, branch_ids in QUANTUM_BRANCH_PARTS:
        lines.append(rf"\part{{{latex_escape(part_title)}}}")
        for branch_id in branch_ids:
            branch = tree["branches"][branch_id]
            lines.append(rf"\chapter{{{latex_escape(branch['title'])}}}")
            lines.append(r"\begin{claimbox}")
            lines.append(latex_escape(branch["definition"]))
            lines.append(r"\end{claimbox}")
            lines.append(latex_escape(branch["insight"]))
            lines.append(r"\section{Topics}")
            lines.append(branch_table(branch))
            pages = list(branch.get("pages") or [])
            if max_pages_per_branch is not None:
                pages = pages[:max_pages_per_branch]
            if not pages:
                lines.append(latex_escape("No topic currently occupies this physical role."))
            else:
                for index, row in enumerate(pages, 1):
                    lines.append(page_entry(root, row, index, branch_id, branch))

    evidence_rows = [
        row
        for branch in (tree.get("branches") or {}).values()
        for row in (branch.get("pages") or [])
    ]
    grounded = sum(bool((row.get("v2_evidence") or {}).get("available")) for row in evidence_rows)
    identifier_linked = sum(
        (row.get("v2_evidence") or {}).get("status") == "v2_identifier_linked"
        for row in evidence_rows
    )
    without_candidate = sum(
        (row.get("v2_evidence") or {}).get("status") == "legacy_witness_only"
        for row in evidence_rows
    )
    if grounded:
        source_statement = (
            f"Source citations are included only for topic-level equation witnesses confirmed by source-card alignment. "
            f"This edition contains {grounded} topics with confirmed witnesses; {identifier_linked} topics have "
            f"identifier-linked candidates awaiting equation-level confirmation, and {without_candidate} have no aligned candidate."
        )
    else:
        source_statement = (
            "Source citations are included only for topic-level equation witnesses confirmed by source-card alignment. "
            f"The present source-card export confirms none: {identifier_linked} topics have identifier-linked candidates "
            f"awaiting equation-level confirmation, and {without_candidate} have no aligned candidate."
        )
    source_statement += (
        " The repository contains the generated tree, topic records, derivation pages, build scripts, "
        "and preservation report needed to reproduce this edition."
    )

    lines.extend(
        [
            r"\backmatter",
            r"\chapter{Sources And Reproduction}",
            latex_escape(source_statement),
            r"\end{document}",
        ]
    )
    return center_equation_rows(public_theory_language("\n\n".join(lines)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="discoveries/morphwiki_quantum")
    parser.add_argument("--out-dir", default="discoveries/morphwiki_quantum/book")
    parser.add_argument("--pages-out-dir", default="discoveries/morphwiki_quantum/derivation_pages")
    parser.add_argument("--max-pages-per-branch", type=int, default=None)
    args = parser.parse_args()

    root = Path(args.root)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tex = render_book(root, args.max_pages_per_branch)
    tex_path = out_dir / "quantum_mechanism_tree_book.tex"
    tex_path.write_text(tex, encoding="utf-8")
    tree = load_json(root / "quantum_mechanism_tree.json")
    pages_manifest = write_derivation_pages(root, Path(args.pages_out_dir), tree)
    print(json.dumps({"tex": str(tex_path), "derivation_pages": pages_manifest}, indent=2))


if __name__ == "__main__":
    main()
