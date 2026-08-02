# Quantum dynamics

**Derivation step:** Generator: lawful change before measurement

## Topic Context

In physics, quantum dynamics is the quantum version of classical dynamics. Quantum dynamics deals with the motions, and energy and momentum exchanges of systems whose behavior is governed by the laws of quantum mechanics. Quantum dynamics is relevant for burgeoning fields, such as quantum computing and atomic optics.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_dynamics)

## Role In The Derivation

Quantum dynamics belongs to the lawful-change step: it specifies how the state changes before a question is asked.

## Why This Step Is Needed

Quantum dynamics separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

The topic supplies or modifies the generator of state evolution before measurement. It should be read as a transport step before measurement.

## How It Enters The Theory

**Place in the construction.** Quantum dynamics contributes a lawful state-transport role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wavefunction, field state, or register on a specified domain. Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Representative Relation

```math
i\hbar\partial_t\rho=[H,\rho],\quad U(t)=e^{-iHt/\hbar},\quad H\psi=E\psi
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

The topic supplies or modifies the generator of state evolution before measurement. It should be read as a transport step before measurement. Quantum dynamics specifies lawful change before measurement. The generator determines the propagator or path weight that carries the state between preparation and measurement. Conserved quantities and symmetries are read from the generator and its commutation relations.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. Time dependence can be assigned to states, operators, propagators, or path amplitudes. Perturbative, Hamiltonian, Lagrangian, and path-integral presentations can represent the same evolution. Approximation schemes change the calculational route without changing the target transition amplitude.

## Connection To The Next Step

A generator predicts a new state but not yet an experimental number. The next step selects an observable, whose spectrum and expectation values expose consequences of the dynamics.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Lawful closed-system evolution preserves norm or trace; open-system evolution must preserve positivity and trace under the stated approximation.
- The short-time and classical limits identify whether the generator has the correct physical regime.

## Evidence Links

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
