# Quantum geometry

## Central Claim
Quantum geometry treats geometric quantities as quantum observables: geometry is not only a background stage, but a state-dependent structure with possible spectral readouts.

## Formal Role
Quantum geometry is not the same mechanism as Fock space. Its carrier is a quantum state of geometry, often represented by graph or spin-network data. The operator-to-spectrum step asks for eigenvalues of geometric observables such as area or volume. The mechanism therefore sits at the geometry/boundary frontier: a geometric quantity is promoted to an operator, and the readout is a spectrum of admissible geometric values.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The graph, spin-network, or quantum-gravity state space is the carrier.
- Geometric data are represented as quantum labels or states rather than as a fixed smooth background.
- Area, volume, or metric-related quantities become operators.
- The spectra of those geometric operators provide readouts.
- The invariant content is the part of the geometric readout that survives changes of graph, gauge, or boundary description.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
\mathcal H_{\Gamma}=L^2(SU(2)^E/SU(2)^V),\quad |\Gamma,j_e,\iota_v\rangle
\hat A(S)|\Gamma,j,\iota\rangle=8\pi\gamma\ell_P^2\sum_{e\cap S}\sqrt{j_e(j_e+1)}|\Gamma,j,\iota\rangle
\hat G|g_i\rangle=g_i|g_i\rangle
```

## Mechanism Roles
- **state:** spin-network state; quantum geometry state; graph-labelled state
- **operator:** area operator; volume operator; geometric observable
- **spectrum:** area spectrum; volume spectrum; geometry eigenvalue
- **boundary:** graph boundary; spin-network graph; Planck-scale domain
- **incompatibility:** non-commuting observables; constraint algebra
- **protocol:** geometric measurement; coarse graining; spin-foam transition

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
