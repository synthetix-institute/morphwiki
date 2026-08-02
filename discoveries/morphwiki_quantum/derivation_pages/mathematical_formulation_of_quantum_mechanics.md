# Mathematical formulation of quantum mechanics

**Derivation step:** Formal context: carrier, domain, and representation

## Topic Context

The mathematical formulations of quantum mechanics are those mathematical formalisms that permit a rigorous description of quantum mechanics. This mathematical formalism uses mainly a part of functional analysis, especially Hilbert spaces, which are a kind of linear space. Such are distinguished from mathematical formalisms for physics theories developed prior to the early 1900s by the use of abstract mathematical structures, such as infinite-dimensional Hilbert spaces, and operators on these spaces. In brief, values of physical observables such as energy and momentum were no longer considered as values of functions on phase space, but as eigenvalues; more precisely as spectral values of linear operators in Hilbert space.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Mathematical_formulation_of_quantum_mechanics)

## Role In The Derivation

Mathematical formulation of quantum mechanics belongs at the first step of the constructor: it fixes the Hilbert space, operator domain, basis, representation, or preparation context before any probability statement is meaningful.

## Why This Step Is Needed

This page is the entrance to the construction because quantum theory separates three objects that classical prose often mixes: a state encoding preparation, an operator encoding a physical question, and a probability rule connecting the two. The formalism is useful precisely because each object can change representation without changing the prediction.

## Mechanism

This step fixes the state space, representation, basis, or operator domain in which the later equations are defined.

## How It Enters The Theory

**Place in the construction.** Mathematical formulation of quantum mechanics contributes a representation and domain role to the quantum construction. This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.

**State and operation.** A Hilbert, Fock, or function space together with the operator domains and representation used in the calculation. A unitary or isometric change of basis, Fourier transform, coordinate map, or representation equivalence.

**Admissibility and prediction.** Inner products, domains, normalization, and completeness relations must be preserved by a purely representational change. Transition amplitudes, expectation values, spectra, and probabilities that remain invariant under an admissible representation change.

## Representative Relation

```math
V:\mathcal H\to\mathcal H',\quad V^\dagger V=I,\quad \rho'=V\rho V^\dagger,\quad O'=VOV^\dagger
```

## How To Read The Relation

A state vector or density operator carries preparation information; an observable supplies possible values; their pairing gives probabilities and expectation values. When a unitary map changes basis, the state and observable transform together. Their matrices change, but every probability remains the same.

## Worked Example

A spin-one-half preparation can be written in the vertical basis or the horizontal basis. The two column vectors look different, and the spin operator has different matrix entries, yet a consistently transformed calculation predicts the same detector counts.

## What Remains Stable

Mathematical formulation of quantum mechanics supplies the admissible arena in which quantum states and operators are defined. Changing basis or representation should not change physical probabilities when the transformation is unitary. Normalization, domain conditions, and inner products remain part of the same formal container.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The chosen basis, coordinate representation, or preparation convention can change. The same calculation may be written with vectors, wave functions, density operators, or operator algebras. Physical realization enters later through boundary conditions, detectors, or fields.

## Connection To The Next Step

The Hilbert-space page now specifies the arena in which states, operators, inner products, and unitary transformations are defined.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Unitary changes of basis preserve Born probabilities; if probabilities change, the page has changed the physical context rather than only the representation.
- The operator domain and normalization conditions determine which questions are legal on the selected Hilbert space.

## Evidence Links

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
