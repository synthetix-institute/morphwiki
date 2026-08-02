# Quantum biology

**Derivation step:** Generator: lawful change before measurement

## Topic Context

Quantum biology is the study of applications of quantum mechanics and theoretical chemistry to aspects of biology that cannot be accurately described by the classical laws of physics. An understanding of fundamental quantum interactions is important because they determine the properties of the next level of organization in biological systems.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_biology)

## Role In The Derivation

Quantum biology belongs to the lawful-change step: it specifies how the state changes before a question is asked.

## Why This Step Is Needed

Quantum biology separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

The topic concerns quantum state transport under environmental coupling, coherence loss, biological or macroscopic boundary conditions, or effective dynamics outside an ideal closed system.

## How It Enters The Theory

**Place in the construction.** Quantum biology contributes an open-system transport and coherence role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A density operator, reduced state, coherence variable, bath-coupled state, or effective mesoscopic carrier. Hamiltonian plus environmental coupling, Lindbladian, memory kernel, stochastic map, or effective transport operator.

**Admissibility and prediction.** Positivity, trace preservation, timescale separation, bath assumptions, and control over classical noise determine whether the model is legal. Coherence, population transfer, relaxation rate, transport efficiency, noise spectrum, or macroscopic response.

## Representative Relation

```math
\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k\left(L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}\right),\quad C(t)=\operatorname{Tr}(\rho(t)O)
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

The topic concerns quantum state transport under environmental coupling, coherence loss, biological or macroscopic boundary conditions, or effective dynamics outside an ideal closed system. Quantum biology specifies lawful change before measurement. The generator determines the propagator or path weight that carries the state between preparation and measurement. Conserved quantities and symmetries are read from the generator and its commutation relations.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. Time dependence can be assigned to states, operators, propagators, or path amplitudes. Perturbative, Hamiltonian, Lagrangian, and path-integral presentations can represent the same evolution. Approximation schemes change the calculational route without changing the target transition amplitude.

## Connection To The Next Step

A generator predicts a new state but not yet an experimental number. The next step selects an observable, whose spectrum and expectation values expose consequences of the dynamics.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Lawful closed-system evolution preserves norm or trace; open-system evolution must preserve positivity and trace under the stated approximation.
- The short-time and classical limits identify whether the generator has the correct physical regime.

## Evidence Links

- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:2006.13679](https://arxiv.org/abs/2006.13679)
