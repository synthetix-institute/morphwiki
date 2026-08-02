# Heisenberg picture

**Derivation step:** Generator: lawful change before measurement

## Topic Context

In physics, the Heisenberg picture or Heisenberg representation is a formulation of quantum mechanics in which observables incorporate a dependency on time, but the states are time-independent. It stands in contrast to the Schrödinger picture in which observables are constant and the states evolve in time.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Heisenberg_picture)

## Role In The Derivation

Heisenberg picture belongs to the lawful-change step: it specifies how the state changes before a question is asked.

## Why This Step Is Needed

Heisenberg picture separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

This step specifies the Hamiltonian, action, channel, or other transformation that changes the state.

## How It Enters The Theory

**Place in the construction.** Heisenberg picture contributes a generator or transformation role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wave function, field state, or register on a specified domain. A Hamiltonian, action, Liouvillian, channel generator, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary conditions determine whether the evolution is legal. Time-dependent probabilities, transition amplitudes, response functions, conserved quantities, or spectra implied by the dynamics.

## Representative Relation

```math
i\hbar\,\partial_t\rho=[H,\rho],\quad U(t)=e^{-iHt/\hbar},\quad \rho(t)=U(t)\rho(0)U^\dagger(t)
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

Heisenberg picture specifies lawful change before measurement. The generator determines the propagator or path weight that carries the state between preparation and measurement. Conserved quantities and symmetries are read from the generator and its commutation relations.

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
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
