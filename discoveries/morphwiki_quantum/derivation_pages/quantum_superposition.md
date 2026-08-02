# Quantum superposition

**Derivation step:** State carrier inside Hilbert space

## Topic Context

Quantum superposition is a fundamental principle of quantum mechanics that states that linear combinations of solutions to the Schrödinger equation are also solutions of the Schrödinger equation. This follows from the fact that the Schrödinger equation is a linear differential equation in time and position. More precisely, the state of a system is given by a linear combination of all the eigenfunctions of the Schrödinger equation governing that system.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_superposition)

## Role In The Derivation

Quantum superposition supplies the carrier of prediction: the object that is propagated, transformed, restricted, or read out.

## Why This Step Is Needed

Quantum superposition specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

## Mechanism

The topic contributes the mathematical carrier of prediction: vector, wavefunction, density operator, register, coherent state, or field state.

## How It Enters The Theory

**Place in the construction.** Quantum superposition contributes a state-carrier role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.

**Admissibility and prediction.** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Representative Relation

```math
\ket{\psi}\in\mathcal H,\quad \rho\ge0,\quad \operatorname{Tr}\rho=1,\quad p_i=\operatorname{Tr}(\rho P_i)
```

## How To Read The Relation

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

## What Remains Stable

The topic contributes the mathematical carrier of prediction: vector, wavefunction, density operator, register, coherent state, or field state. Quantum superposition carries the predictive information before a measurement question is asked. The same physical preparation may be represented as a vector, wave function, density matrix, or reduced state. Normalization and positivity are the admissibility checks that make the state usable for probability assignment.

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
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
