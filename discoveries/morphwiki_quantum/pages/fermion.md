# Fermion

## Central Claim
Fermionic exchange constrains the global many-body state: antisymmetry removes coincidence states and thereby produces exclusion, exchange holes, Fermi surfaces, and degeneracy pressure before a repulsive interaction is introduced.

## Formal Role
The fermion construction is an exchange constraint on state space, not a particle label. The wave function changes sign under exchange and vanishes when identical one-particle states coincide. Exterior Fock space and canonical anticommutation preserve that nodal restriction when particle number changes. At finite density, distinct modes fill to a Fermi surface and generate degeneracy pressure without pairwise repulsion. Pairing can move the state into an even-parity collective sector, while mappings to spins or hard-core bosons preserve selected spectra only by changing locality or correlation observables.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The many-particle state lives in an antisymmetric sector.
- Creation and annihilation operators anticommute.
- Mode occupation is restricted to zero or one.
- Number, energy, momentum, spin, or charge provide field-dependent readouts.
- Exchange of identical particles changes the sign of the state.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
\Psi(\ldots,x_i,\ldots,x_j,\ldots)=-\Psi(\ldots,x_j,\ldots,x_i,\ldots)
\mathcal F_{-}(\mathcal H)=\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H
\{a_i,a_j^{\dagger}\}=\delta_{ij},\quad \{a_i,a_j\}=0
n_i=a_i^{\dagger}a_i\in\{0,1\}
```

## Mechanism Roles
- **state:** antisymmetric many-body state; fermionic Fock state; occupied mode
- **operator:** fermionic creation operator; fermionic annihilation operator; number operator
- **spectrum:** occupation number; energy; momentum; spin
- **boundary:** exchange symmetry sector; mode basis
- **incompatibility:** anticommutation; Pauli exclusion
- **protocol:** mode filling; fermionic quantization

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
