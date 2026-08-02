#!/usr/bin/env python3
"""Shared public contract for the MorphWiki mechanism constructor."""

from __future__ import annotations


CONSTRUCTOR_CHAIN_LATEX = (
    r"(\Omega,\Xi)\longrightarrow M\longrightarrow "
    r"I_{\mathrm{op}}=(M;C,R,P)\longrightarrow "
    r"\mathcal I_{\mathrm{real}}=(I_{\mathrm{op}};A)"
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
        "carrier",
        "The structure on which the operation is defined: Hilbert or Fock "
        "space, state class, operator domain, tensor factorization, or field algebra.",
    ),
    (
        "C",
        "closure",
        "The conditions that make the construction admissible: normalization, "
        "positivity, domain, gauge, compatibility, or conservation constraints.",
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
        "The named physical embodiment: objects, parameters, units, geometry, "
        "boundaries, devices, and experimental conditions.",
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
    ("Carrier And States", ("context", "states")),
    ("Operations", ("generators", "observables")),
    ("Completion", ("incompatibility", "measurement", "protocols")),
    ("Realizations And Extensions", ("boundaries", "fields")),
    ("Provenance And Interpretations", ("annotations",)),
)

DISCOVERY_CONTRACT_LATEX = (
    r"(I_{\mathrm{op}},p;Q_{\mathrm{keep}},B_{\mathrm{edit}})"
    r"\longmapsto(\widehat I_{\mathrm{op}},\widehat A,\widehat y)"
)

DISCOVERY_PATH_LATEX = (
    r"(I,p)\xrightarrow{\mathrm{retain}\ Q,\,\mathrm{edit}\ B}"
    r"\widehat I_{\mathrm{op}}\xrightarrow{\mathrm{complete}}"
    r"\widehat I_{\mathrm{real}}\xrightarrow{\mathrm{derive}}"
    r"\widehat y\xrightarrow{\mathrm{test}}"
    r"\{\mathrm{accept},\mathrm{revise}\}"
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
