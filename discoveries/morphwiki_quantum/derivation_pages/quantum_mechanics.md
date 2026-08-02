# Quantum mechanics

**Derivation step:** Generator: lawful change before measurement

## Topic Context

Quantum mechanics is the fundamental physical theory that describes the behavior of matter and of light; its unusual characteristics typically occur at and below the scale of atoms. It is the foundation of all quantum physics, which includes quantum chemistry, quantum biology, quantum field theory, quantum technology, and quantum information science.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_mechanics)

## Role In The Derivation

Quantum mechanics is the baseline constructor: states live in Hilbert space, physical questions are represented by operators, and probabilities are assigned to spectral projectors.

## Why This Step Is Needed

Quantum mechanics separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

The page supplies the general quantum assembly. A preparation gives a state vector or density operator. A self-adjoint observable or measurement operator family gives the possible outcome channels. The Born or trace rule assigns probabilities, while Hamiltonian evolution transports the state between preparation and observable.

## How It Enters The Theory

**Place in the construction.** Quantum mechanics contributes a generator or transformation role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A state vector, density operator, wave function, field state, or register on a specified domain. A Hamiltonian, action, Liouvillian, channel generator, or differential operator that transports the state.

**Admissibility and prediction.** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary conditions determine whether the evolution is legal. Time-dependent probabilities, transition amplitudes, response functions, conserved quantities, or spectra implied by the dynamics.

## Topic Equations

Topic-specific constructor: the equations express state admissibility, spectral prediction, unitary evolution, and incompatibility.

```math
\rho\ge 0,\qquad \operatorname{Tr}\rho=1
A=\sum_a aP_a,\qquad p(a)=\operatorname{Tr}(\rho P_a)
\rho(t)=U(t)\rho(0)U(t)^\dagger,\qquad U(t)=e^{-iHt/\hbar}
[A,B]\ne0\quad\Rightarrow\quad \text{no generic common sharp eigenbasis}
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

A generator predicts a new state but not yet an experimental number. The next step selects an observable, whose spectrum and expectation values expose consequences of the dynamics.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
