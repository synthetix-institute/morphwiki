# Quantum decoherence

**Derivation step:** State carrier inside Hilbert space

## Topic Context

Quantum decoherence is the loss of quantum coherence. It involves generally a loss of information of a system to its environment. Quantum decoherence has been studied to understand how quantum systems convert to systems that can be explained by classical mechanics. Beginning out of attempts to extend the understanding of quantum mechanics, the theory has developed in several directions and experimental studies have confirmed some of the key issues. Quantum computing relies on quantum coherence and is one of the primary practical applications of the concept.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_decoherence)

## Role In The Derivation

Quantum decoherence supplies the carrier of prediction: the object that is propagated, transformed, restricted, or read out.

## Why This Step Is Needed

Quantum decoherence specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

## Mechanism

The topic concerns quantum state transport under environmental coupling, coherence loss, biological or macroscopic boundary conditions, or effective dynamics outside an ideal closed system.

## How It Enters The Theory

**Place in the construction.** Quantum decoherence contributes an open-system transport and coherence role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** A density operator, reduced state, coherence variable, bath-coupled state, or effective mesoscopic carrier. Hamiltonian plus environmental coupling, Lindbladian, memory kernel, stochastic map, or effective transport operator.

**Admissibility and prediction.** Positivity, trace preservation, timescale separation, bath assumptions, and control over classical noise determine whether the model is legal. Coherence, population transfer, relaxation rate, transport efficiency, noise spectrum, or macroscopic response.

## Representative Relation

```math
\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k\left(L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}\right),\quad C(t)=\operatorname{Tr}(\rho(t)O)
```

## How To Read The Relation

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

## What Remains Stable

The topic concerns quantum state transport under environmental coupling, coherence loss, biological or macroscopic boundary conditions, or effective dynamics outside an ideal closed system. Quantum decoherence carries the predictive information before a measurement question is asked. The same physical preparation may be represented as a vector, wave function, density matrix, or reduced state. Normalization and positivity are the admissibility checks that make the state usable for probability assignment.

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
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
