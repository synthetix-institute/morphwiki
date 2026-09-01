# Fock space

## Central Claim
Fock space is the occupation-number version of quantum state space: it replaces a fixed-particle Hilbert space with a direct sum over sectors containing zero, one, two, or more identical quanta.

## Formal Role
Fock space changes the carrier of the theory. A single-particle Hilbert space is lifted to a many-sector space, and the exchange rule selects bosonic or fermionic sectors. Creation and annihilation operators then become the native operations: they move the state between particle-number sectors, while the number operator provides the spectral readout of occupation. The important mechanism is therefore not a generic state-to-spectrum template, but the conversion from fixed-particle description to occupation-number dynamics.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The one-particle Hilbert space H is the seed carrier.
- The full carrier is a direct sum of n-particle sectors, symmetrized for bosons or antisymmetrized for fermions.
- Creation and annihilation operators move states between occupation sectors.
- The number operator or mode observables provide the spectral readout.
- The commutation or anticommutation rule encodes the particle statistics.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
\mathcal F_{\pm}(\mathcal H)=\bigoplus_{n=0}^{\infty}\mathcal S_{\pm}\mathcal H^{\otimes n}
[a_i,a_j^\dagger]_{\mp}=\delta_{ij},\quad [a_i,a_j]_{\mp}=0
N=\sum_i a_i^\dagger a_i
```

## Mechanism Roles
- **state:** occupation-number state; Fock vector; n-particle sector
- **operator:** creation operator; annihilation operator; number operator
- **spectrum:** occupation number; mode population; particle-number sector
- **boundary:** bosonic symmetrization; fermionic antisymmetrization
- **incompatibility:** commutation relation; anticommutation relation
- **protocol:** sector-changing operation; mode expansion

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
