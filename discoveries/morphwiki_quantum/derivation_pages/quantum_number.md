# Quantum number

**Derivation step:** State carrier inside Hilbert space

## Topic Context

In quantum physics and chemistry, quantum numbers are quantities that characterize the possible states of the system. To fully specify the state of the electron in a hydrogen atom, four quantum numbers are needed. The traditional set of quantum numbers includes the principal, azimuthal, magnetic, and spin quantum numbers. To describe other systems, different quantum numbers are required. For subatomic particles, one needs to introduce new quantum numbers, such as the flavour of quarks, which have no classical correspondence.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_number)

## Role In The Derivation

Quantum number supplies the carrier of prediction: the object that is propagated, transformed, restricted, or read out.

## Why This Step Is Needed

Quantum number specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

## Mechanism

This step identifies the state, sector, or statistical operator that carries the theory's predictions.

## How It Enters The Theory

**Place in the construction.** Quantum number contributes a state or sector role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** A state vector, wave function, density operator, field state, register state, or superselection sector. The transformations and observables defined on that state space.

**Admissibility and prediction.** Normalization, positivity, inner-product, tensor-factorization, and superselection conditions define the allowed states. Born probabilities, expectation values, reduced states, or correlation functions determined by the state.

## Representative Relation

```math
\ket\psi\in\mathcal H,\quad \rho\ge0,\quad \operatorname{Tr}\rho=1,\quad p_i=\operatorname{Tr}(\rho P_i)
```

## How To Read The Relation

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

## What Remains Stable

Quantum number carries the predictive information before a measurement question is asked. The same physical preparation may be represented as a vector, wave function, density matrix, or reduced state. Normalization and positivity are the admissibility checks that make the state usable for probability assignment.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The state representation can change between position, momentum, spin, occupation, or density-operator forms. Pure-state and mixed-state descriptions may differ while describing the same formal preparation. Subsystem descriptions change when degrees of freedom are traced out or ignored.

## Connection To The Next Step

With the state identified, the next question is how it changes. The generator chapter supplies that lawful transformation; the observable and measurement chapters then turn the transformed state into a prediction.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- A usable state gives normalized probabilities for every complete observable attached to the selected Hilbert space.
- Vector, wave-function, density-matrix, and reduced-state forms can describe the same preparation when connected by the appropriate representation map.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
