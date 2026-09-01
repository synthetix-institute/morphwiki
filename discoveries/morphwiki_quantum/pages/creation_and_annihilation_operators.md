# Creation and annihilation operators

## Central Claim
Creation and annihilation operators are the algebraic moves that change mode occupation; they are the mechanism by which fixed-particle quantum mechanics becomes field or many-body quantum theory.

## Formal Role
This page is about the operation that moves a state between occupation sectors. A creation operator adds one quantum to a mode, an annihilation operator removes one, and their commutation or anticommutation relation selects bosonic or fermionic statistics. The number operator then supplies the spectral readout of occupation. The central mechanism is therefore sector-changing algebra, not a generic Hamiltonian question.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The mode basis defines the occupation sectors.
- Creation and annihilation operators add or remove one quantum in a mode.
- Commutation or anticommutation selects the particle statistics.
- Number operators are constructed from creation-annihilation pairs.
- The occupation spectrum is the readout.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
a_i^{\dagger}|\ldots,n_i,\ldots\rangle=\sqrt{n_i+1}|\ldots,n_i+1,\ldots\rangle
a_i|\ldots,n_i,\ldots\rangle=\sqrt{n_i}|\ldots,n_i-1,\ldots\rangle
N_i=a_i^{\dagger}a_i
```

## Mechanism Roles
- **state:** occupation-number state; Fock state; mode state
- **operator:** creation operator; annihilation operator; number operator
- **spectrum:** occupation number; mode population
- **boundary:** mode basis; statistics sector
- **incompatibility:** commutation relation; anticommutation relation
- **protocol:** add one quantum; remove one quantum; normal ordering

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
