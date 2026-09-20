# Fermion

## Central Claim
Fermionic exchange makes the many-body wave function antisymmetric in the complete one-particle coordinates, including spin. It forbids double occupation of one mode and produces a same-spin exchange hole; opposite-spin particles may occupy the same spatial orbital.

## Formal Role
Exchanging identical fermions reverses the sign of the wave function when both spatial and spin coordinates are exchanged. Exterior Fock space and canonical anticommutation express this restriction when particle number varies. In a homogeneous ideal gas at zero temperature, occupied momentum modes fill a Fermi sphere and produce degeneracy pressure without repulsive interactions. Pairing creates collective even-parity degrees of freedom while the constituent particles retain fermionic antisymmetry. Mappings to spins or hard-core bosons require the corresponding transformation of operators and correlation functions.

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
z_i=(\mathbf x_i,\sigma_i),\quad \Psi(\ldots,z_i,\ldots,z_j,\ldots)=-\Psi(\ldots,z_j,\ldots,z_i,\ldots)
\mathcal F_{-}(\mathcal H)=\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H
\{a_i,a_j^{\dagger}\}=\delta_{ij},\quad \{a_i,a_j\}=0
n_i=a_i^{\dagger}a_i,\quad n_i^2=n_i,\quad \operatorname{spec}(n_i)=\{0,1\}
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
