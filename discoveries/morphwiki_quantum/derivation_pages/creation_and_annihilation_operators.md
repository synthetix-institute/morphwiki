# Creation and annihilation operators

**Physical domain:** Dynamics and transformations

## Mechanism

Creation and annihilation operators are sector-changing operators: they add or remove one quantum from a mode and make many-body or field descriptions executable.

Creation and annihilation operators separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

The page is about the algebraic move that changes occupation number. Creation raises the population of a mode, annihilation lowers it, and the commutation or anticommutation rule determines the statistics. The number operator gives the spectral prediction.

## Physical Construction

The state carrier is a state vector, density operator, wave function, field state, or register on a specified domain. The governing operation is a Hamiltonian, action, Liouvillian, channel generator, or differential operator that transports the state. Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary conditions determine whether the evolution is legal. The calculated observables are Time-dependent probabilities, transition amplitudes, response functions, conserved quantities, or spectra implied by the dynamics.

## Topic Equations

Topic-specific constructor: the equations express raising, lowering, and occupation-number observable.

```math
a_i^\dagger\ket{\ldots,n_i,\ldots}=\sqrt{n_i+1}\ket{\ldots,n_i+1,\ldots}
a_i\ket{\ldots,n_i,\ldots}=\sqrt{n_i}\ket{\ldots,n_i-1,\ldots}
N_i=a_i^\dagger a_i
```

## Physical Meaning

The evolution law transports a state without redefining it. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

The evolved state becomes experimentally meaningful through an observable whose spectrum and expectation values expose the consequences of the dynamics.

## Invariance And Realization

The relation between prepared states, observables, and spectral probability measures. The use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations. The dependence of the observable on basis, domain, potential, preparation, or measurement context. The commutator structure that limits which observables can be jointly diagonalized.

The physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation. The representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields. Where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight. The implementation of preparation, boundary condition, detector, or outcome channel.

## Discriminating Consequences

A transfer target provides a state space, a transformation law, and a spectral or categorical observable, with one compatibility relation experimentally unresolved. A useful validation varies the basis, domain, or measurement context and measures whether the allowed observable changes while the underlying transformation law remains identifiable. A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.

## Source Equations

- [arXiv:math-ph/0509009](https://arxiv.org/abs/math-ph/0509009)
- [arXiv:math-ph0509009](https://arxiv.org/abs/math-ph0509009)
- [arXiv:gr-qc/0104053](https://arxiv.org/abs/gr-qc/0104053)
- [arXiv:gr-qc0104053](https://arxiv.org/abs/gr-qc0104053)
