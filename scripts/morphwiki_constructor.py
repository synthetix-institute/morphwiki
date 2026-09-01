#!/usr/bin/env python3
"""Shared public contract for the MorphWiki mechanism constructor."""

from __future__ import annotations


CONSTRUCTOR_CHAIN_LATEX = (
    r"(\Omega,\Xi)\longrightarrow M\longrightarrow "
    r"I_{\mathrm{op}}=(M;C,R,P)\longrightarrow "
    r"I_{\mathrm{real}}=(I_{\mathrm{op}};A)"
)

CONSTRUCTOR_CHAIN_TEXT = (
    "(Omega, Xi) -> M -> I_op=(M; C, R, P) -> "
    "I_real=(I_op; A)"
)

CONSTRUCTOR_CLAUSES = (
    (
        "Omega",
        "operation",
        "The transformation apparatus: generator, observable, channel, "
        "symmetry action, projection, or composed map.",
    ),
    (
        "Xi",
        "physical state space",
        "The admissible configurations on which the operation is defined, "
        "together with the required domain, tensor factorization, or field algebra.",
    ),
    (
        "C",
        "closure",
        "The conditions that make the construction admissible: normalization, "
        "positivity, domain, gauge, constitutive, or compatibility constraints.",
    ),
    (
        "R",
        "observable map",
        "The map from the construction to a prediction: spectral measure, "
        "POVM, correlator, current, detector outcome, or error statistic.",
    ),
    (
        "P",
        "protocol",
        "The ordered preparation, intervention, evolution, control, or "
        "measurement sequence required to execute the mechanism.",
    ),
    (
        "A",
        "realization",
        "The named physical embodiment: material or field content, initial and "
        "boundary data, parameter ranges, units, geometry, drives, devices, and trajectories.",
    ),
)

DISCOVERY_VERBS = (
    (
        "Complete",
        "add a missing closure, observable map, or protocol clause to a partial mechanism",
    ),
    (
        "Reattach",
        "retain an operation and replace its carrier, or retain a carrier and replace its operation",
    ),
    (
        "Compose",
        "join supported transformations into a mechanism not written as one source equation",
    ),
    (
        "Deform",
        "vary a parameter, boundary, scale, or representation while tracking a stated invariant",
    ),
    (
        "Observe",
        "construct the observable or intervention that exposes a predicted consequence",
    ),
    (
        "Revise",
        "use a failed consequence to identify and replace the clause responsible for the failure",
    ),
)

QUANTUM_BRANCH_PARTS = (
    ("State Spaces And Dynamical Laws", ("context", "states", "generators")),
    ("Observables, Compatibility, And Probability", ("observables", "incompatibility", "measurement")),
    ("Controlled And Spatial Realizations", ("protocols", "boundaries")),
    ("Fields, Constraints, And Scale", ("fields",)),
    ("Historical And Interpretive Annotations", ("annotations",)),
)


ROLE_PROMOTION_PRINCIPLE = (
    "A quantity remains realization data while it selects parameters within a fixed state space, "
    "operator domain, closure, observable, and protocol. It changes physical role when it alters "
    "one of those objects. The promoted quantity must then be represented in the corresponding "
    "clause of the mechanism."
)

PREDICTIVE_CLOSURE_PRINCIPLE = (
    "At a chosen resolution, a physical theory is closed when its declared state fixes future "
    "observable probabilities and its allowed transformations compose consistently. If either "
    "condition fails, the smallest missing field, state coordinate, operator, closure condition, "
    "observable, or protocol must enter the theory."
)

PREDICTIVE_CLOSURE_LATEX = (
    r"q(h_1)=q(h_2)\Longrightarrow "
    r"p(y,t\mid h_1)=p(y,t\mid h_2),\qquad "
    r"T_{\gamma_1}=T_{\gamma_2}\ "
    r"\text{for physically equivalent paths}"
)

ROLE_PROMOTION_CRITERION_LATEX = (
    r"\begin{aligned}"
    r"a\in A\quad &\text{while}\quad "
    r"(\Xi,\Omega,C,R,P)_a=(\Xi,\Omega,C,R,P),\\"
    r"a\longrightarrow X\in\{\Xi,\Omega,C,R,P\}\quad "
    r"&\text{when the physical object }X\text{ changes}."
    r"\end{aligned}"
)


QUANTUM_ROLE_PROMOTIONS = (
    {
        "id": "background_to_field",
        "label": "A background becomes a quantum field",
        "source_role": "A",
        "target_roles": ("Xi", "Omega"),
        "physical_change": (
            "A prescribed background potential or geometry becomes a fluctuating degree of freedom "
            "with its own state and equation of motion."
        ),
        "consequence": (
            "The enlarged theory contains quanta, correlations, and back-reaction that a fixed background cannot carry."
        ),
    },
    {
        "id": "geometry_to_state",
        "label": "Geometry becomes part of the quantum state",
        "source_role": "A",
        "target_roles": ("Xi", "Omega"),
        "physical_change": (
            "Distances, areas, connections, or causal relations cease to label a fixed arena and enter the quantum state and dynamics."
        ),
        "consequence": (
            "Geometric observables acquire spectra and fluctuations, while matter and geometry must evolve consistently."
        ),
    },
    {
        "id": "environment_to_state",
        "label": "An environment becomes a retained degree of freedom",
        "source_role": "A",
        "target_roles": ("Xi", "Omega", "C"),
        "physical_change": (
            "Environmental correlations that influence later motion are retained as state variables or represented by a memory kernel."
        ),
        "consequence": (
            "The future reduced state can depend on earlier interactions rather than on its present coordinates alone."
        ),
    },
    {
        "id": "apparatus_to_channel",
        "label": "An apparatus becomes part of the quantum dynamics",
        "source_role": "A",
        "target_roles": ("Xi", "Omega", "R"),
        "physical_change": (
            "A detector or amplifier is represented as an interacting quantum subsystem and an outcome-resolved channel."
        ),
        "consequence": (
            "Back-action, conditional state change, and detector noise become calculable parts of the outcome probabilities."
        ),
    },
    {
        "id": "boundary_to_closure",
        "label": "A boundary becomes a closure condition",
        "source_role": "A",
        "target_roles": ("C", "Omega"),
        "physical_change": (
            "A wall, interface, or asymptotic condition selects the operator domain or self-adjoint extension."
        ),
        "consequence": (
            "The allowed spectrum, scattering channels, and edge states change with the domain of the operator."
        ),
    },
    {
        "id": "constraint_to_state_space",
        "label": "A constraint defines the physical state space",
        "source_role": "C",
        "target_roles": ("Xi",),
        "physical_change": (
            "Gauge conditions, exchange symmetry, or superselection rules remove vectors that do not represent physical states."
        ),
        "consequence": (
            "The surviving Hilbert-space sectors determine particle statistics, charges, and admissible observables."
        ),
    },
    {
        "id": "factorization_to_state_space",
        "label": "A subsystem split becomes part of the state space",
        "source_role": "A",
        "target_roles": ("Xi", "C"),
        "physical_change": (
            "A chosen partition into subsystems fixes the tensor-product or algebraic decomposition used to define locality."
        ),
        "consequence": (
            "Entanglement and Bell correlations become properties of the joint state relative to that decomposition."
        ),
    },
    {
        "id": "protocol_to_dynamics",
        "label": "An ordered protocol becomes a dynamical map",
        "source_role": "P",
        "target_roles": ("Omega",),
        "physical_change": (
            "A sequence of controls, measurements, and conditional operations is composed into a channel or effective generator."
        ),
        "consequence": (
            "Changing the order changes the implemented unitary, channel, or feedback law even when the same elementary operations are used."
        ),
    },
    {
        "id": "scale_to_dynamics",
        "label": "Scale becomes part of the law",
        "source_role": "A",
        "target_roles": ("Omega", "C"),
        "physical_change": (
            "The observation scale changes effective couplings or operators rather than merely changing numerical resolution."
        ),
        "consequence": (
            "Renormalization flow connects different effective laws and exposes fixed points, relevant operators, and universality classes."
        ),
    },
)


QUANTUM_PROMOTION_TOPIC_MAP = {
    "background_to_field": (
        "quantum_field_theory", "quantum_electrodynamics", "quantum_chromodynamics",
        "gauge_theory", "photon", "electron", "standard_model",
    ),
    "geometry_to_state": (
        "quantum_gravity", "loop_quantum_gravity", "quantum_geometry", "quantum_spacetime",
        "spin_network", "spin_foam", "string_theory", "ads_cft_correspondence",
    ),
    "environment_to_state": (
        "quantum_decoherence", "quantum_stochastic_calculus", "quantum_biology",
        "macroscopic_quantum_phenomena", "measurement_problem",
    ),
    "apparatus_to_channel": (
        "measurement_in_quantum_mechanics", "measurement_problem", "povm",
        "projection_valued_measure", "wave_function_collapse", "quantum_jump",
        "electron_microscope", "quantum_amplifier", "quantum_sensor", "quantum_imaging",
    ),
    "boundary_to_closure": (
        "potential_well", "particle_in_a_box", "quantum_tunnelling", "scattering",
        "s_matrix", "quantum_optics", "spectral_line", "quantum_metamaterial",
        "quantum_harmonic_oscillator",
    ),
    "constraint_to_state_space": (
        "gauge_theory", "fermi_dirac_statistics", "bose_einstein_statistics", "fermion",
        "boson", "fock_space", "standard_model",
    ),
    "factorization_to_state_space": (
        "quantum_entanglement", "bell_s_theorem", "einstein_podolsky_rosen_paradox",
        "quantum_nonlocality", "quantum_information", "quantum_information_science",
    ),
    "protocol_to_dynamics": (
        "quantum_channel", "quantum_circuit", "quantum_logic_gate", "quantum_algorithm",
        "quantum_computing", "quantum_error_correction", "quantum_network",
        "quantum_teleportation", "quantum_key_distribution", "quantum_metrology",
        "quantum_simulator", "quantum_finite_automaton", "quantum_cellular_automaton",
    ),
    "scale_to_dynamics": (
        "renormalization", "quantum_field_theory", "quantum_chromodynamics",
        "quantum_statistical_mechanics", "ads_cft_correspondence",
    ),
}


CANONICAL_TOPIC_ALIASES = {
    "perturbation_theory_quantum_mechanics": "perturbation_theory",
    "path_integral_formulation": "path_integral",
    "hamiltonian_quantum_mechanics": "hamiltonian_mechanics",
    "superposition_principle": "quantum_superposition",
    "operator_physics": "operator_theory",
    "quantum_information_science": "quantum_information",
}


def quantum_role_promotions_for_slug(slug: str) -> tuple[dict, ...]:
    """Return the physical role changes associated with a quantum topic."""
    promotions = {row["id"]: row for row in QUANTUM_ROLE_PROMOTIONS}
    return tuple(
        promotions[promotion_id]
        for promotion_id, slugs in QUANTUM_PROMOTION_TOPIC_MAP.items()
        if slug in slugs
    )

DISCOVERY_PROBLEM_LATEX = (
    r"(I_{\mathrm{op}},p;Q_{\mathrm{keep}},B_{\mathrm{edit}})"
    r"\longmapsto(\widehat I_{\mathrm{op}},\widehat A,\widehat y)"
)

# Backwards-compatible import name for downstream scripts.  Public text calls
# this a construction problem rather than a contract.
DISCOVERY_CONTRACT_LATEX = DISCOVERY_PROBLEM_LATEX

PHYSICAL_STATE_LATEX = (
    r"q\in\Xi,\qquad \dot q=\Omega[q;C,P],\qquad y=R(q)"
)

COMPATIBILITY_RESIDUAL_LATEX = (
    r"\Delta_{\alpha,\beta}=\Omega_B\alpha-\beta\Omega_A"
)

COMPATIBILITY_BRANCH_LATEX = (
    r"\begin{cases}"
    r"\mathrm{transfer},&\Delta_{\alpha,\beta}=0,\\"
    r"\mathrm{reject},&\Delta_{\alpha,\beta}\ne0\ \text{without stable closure},\\"
    r"\mathrm{promote}(\Delta),&\Delta_{\alpha,\beta}\ne0\ \text{and closes}"
    r"\end{cases}"
)

DISCOVERY_PATH_LATEX = (
    r"(I,p)\xrightarrow{\mathrm{retain}\ Q,\,\mathrm{edit}\ B}"
    r"\widehat I_{\mathrm{op}}\xrightarrow{\mathrm{complete}}"
    r"\widehat I_{\mathrm{real}}\xrightarrow{\mathrm{compatibility}}"
    r"\{\mathrm{transfer},\mathrm{reject},\mathrm{promote}\ \Delta\}"
)


def public_theory_language(value: object) -> str:
    """Translate internal corpus terminology into theoretical-physics prose.

    The internal language retains the historical name of the R fibre. Public
    books and tutorials describe the same clause as an observable, measurement
    map, probability law, or prediction map, according to context.
    """
    text = str(value or "")
    replacements = (
        ("operator-to-spectrum readout", "operator-to-spectrum relation"),
        ("state-to-spectrum readout", "state-to-spectrum probability assignment"),
        ("probability readout", "probability assignment"),
        ("spectral readout", "spectral prediction"),
        ("physical readout", "physical observable"),
        ("experimental readout", "experimental observable"),
        ("readout probabilities", "outcome probabilities"),
        ("readout probability", "outcome probability"),
        ("readout channels", "outcome channels"),
        ("readout channel", "outcome channel"),
        ("readout map", "measurement map"),
        ("readout rule", "probability rule"),
        ("readout step", "measurement step"),
        ("readout role", "observable role"),
        ("readout junction", "measurement junction"),
        ("before readout", "before measurement"),
        ("Readout probabilities", "Outcome probabilities"),
        ("Readout probability", "Outcome probability"),
        ("Readout channels", "Outcome channels"),
        ("Readout channel", "Outcome channel"),
        ("Readout map", "Measurement map"),
        ("Readout rule", "Probability rule"),
        ("Readout step", "Measurement step"),
        ("Readout role", "Observable role"),
        ("Readout junction", "Measurement junction"),
        ("Readouts", "Observables"),
        ("readouts", "observables"),
        ("Readout", "Observable"),
        ("readout", "observable"),
    )
    for old, new in replacements:
        text = text.replace(old, new)
    return text
