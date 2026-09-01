# Electron

## Central Claim
An electron is a stable charged spin-1/2 excitation whose operational identity is fixed by charge, mass, spin, fermionic statistics, and its coupling to electromagnetic fields.

## Formal Role
The electron page has a native constructor that combines a spinor state, a relativistic generator, a conserved charge, and fermionic anticommutation. In nonrelativistic settings this appears as a Schrödinger or Pauli state under electromagnetic coupling; in relativistic field theory it appears as a Dirac field excitation. The readouts are charge, mass-energy, spin, momentum, and scattering or detector events.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The spinor or field state carries electron quantum numbers.
- The Schrödinger, Pauli, or Dirac generator defines the regime-specific evolution.
- Charge conservation and fermionic exchange statistics define admissibility.
- Electromagnetic potentials couple through minimal coupling.
- Energy, momentum, spin, charge, and scattering response are readout channels.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
(i\hbar\gamma^{\mu}D_{\mu}-mc)\psi=0
D_{\mu}=\partial_{\mu}+\frac{ie}{\hbar c}A_{\mu}
\{\psi_{\alpha}(x),\psi_{\beta}^{\dagger}(y)\}=\delta_{\alpha\beta}\delta(x-y)
```

## Mechanism Roles
- **state:** spinor state; Dirac field excitation; electron wave packet
- **operator:** Dirac operator; Pauli Hamiltonian; charge operator
- **spectrum:** energy; momentum; spin projection; charge
- **boundary:** electromagnetic potential; scattering boundary; confining potential
- **incompatibility:** fermionic anticommutation; spin measurement basis
- **protocol:** scattering; spectroscopy; charge detection

## Representation-Stable Content
- the relation between prepared states, observables, and spectral probability measures
- the use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations
- the dependence of the readout on basis, domain, potential, preparation, or measurement context
- the commutator structure that limits which observables can be jointly diagonalized

## Representation-Dependent Content
- the physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation
- the representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields
- where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight
- the implementation of preparation, boundary condition, detector, or readout channel

## Validation Checks
- A transfer target provides a state space, a transformation law, and a spectral or categorical readout, with one compatibility relation experimentally unresolved.
- A useful validation varies the basis, domain, or measurement context and measures whether the allowed readout changes while the underlying transformation law remains identifiable.
- A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.
