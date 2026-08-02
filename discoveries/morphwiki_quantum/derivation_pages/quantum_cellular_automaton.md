# Quantum cellular automaton

**Derivation step:** Formal context: carrier, domain, and representation

## Topic Context

A quantum cellular automaton (QCA) is an abstract model of quantum computation, devised in analogy to conventional models of cellular automata introduced by John von Neumann.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_cellular_automaton)

## Role In The Derivation

Quantum cellular automaton belongs at the first step of the constructor: it fixes the Hilbert space, operator domain, basis, representation, or preparation context before any probability statement is meaningful.

## Why This Step Is Needed

Quantum cellular automaton is needed because a quantum equation has no fixed meaning until its state space, inner product, representation, and operator domains have been specified. These choices decide which states are admissible and which apparent changes are only changes of coordinates.

## Mechanism

This step fixes the state space, representation, basis, or operator domain in which the later equations are defined.

## How It Enters The Theory

**Place in the construction.** Quantum cellular automaton contributes a representation and domain role to the quantum construction. This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.

**State and operation.** A Hilbert, Fock, or function space together with the operator domains and representation used in the calculation. A unitary or isometric change of basis, Fourier transform, coordinate map, or representation equivalence.

**Admissibility and prediction.** Inner products, domains, normalization, and completeness relations must be preserved by a purely representational change. Transition amplitudes, expectation values, spectra, and probabilities that remain invariant under an admissible representation change.

## Representative Relation

```math
V:\mathcal H\to\mathcal H',\quad V^\dagger V=I,\quad \rho'=V\rho V^\dagger,\quad O'=VOV^\dagger
```

## How To Read The Relation

Read the relation as a comparison between descriptions of the same state and operator. Under a unitary or isometric change of representation, amplitudes, expectation values, and spectra agree. If they do not, the physical model has changed rather than merely its notation.

## What Remains Stable

Quantum cellular automaton supplies the admissible arena in which quantum states and operators are defined. Changing basis or representation should not change physical probabilities when the transformation is unitary. Normalization, domain conditions, and inner products remain part of the same formal container.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The chosen basis, coordinate representation, or preparation convention can change. The same calculation may be written with vectors, wave functions, density operators, or operator algebras. Physical realization enters later through boundary conditions, detectors, or fields.

## Connection To The Next Step

Once the mathematical arena is fixed, the construction can specify a state within it. Later steps add a generator, an observable, and a measurement model, each constrained by the same domain.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Unitary changes of basis preserve Born probabilities; if probabilities change, the page has changed the physical context rather than only the representation.
- The operator domain and normalization conditions determine which questions are legal on the selected Hilbert space.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1109.3239](https://arxiv.org/abs/1109.3239)
- [arXiv:gr-qc0411110](https://arxiv.org/abs/gr-qc/0411110)
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
- [arXiv:astro-ph0604157](https://arxiv.org/abs/astro-ph/0604157)
- [arXiv:hep-lat9608080](https://arxiv.org/abs/hep-lat/9608080)
