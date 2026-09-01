# Quantum state

## Evidence Status
A quantum state can be read as a quantum construction: the potential, domain, initial condition, or boundary condition fixes the admissible state space; the Hamiltonian, whose exponential gives unitary time evolution defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## Formal Role
In quantum-mechanical terms, a quantum state is described by a wave function or density operator defined on the Hilbert space allowed by the system's domain. The physical question is represented by the Hamiltonian, whose exponential gives unitary time evolution; the experimental or mathematical setting is the potential, domain, initial condition, or boundary condition. The observable content is obtained from the eigenvalues and eigenfunctions of the relevant observable. In the local terminology of this topic, the same construction appears through Quantum state or wave function, observable operator or matrix, and eigenstate or spectrum. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through uncertainty relation or incompatible observables.

## Formal Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (detector, preparation, or preparation context) determine which states are admissible.
- State terms (Quantum state, wave function, or superposition) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (observable operator, matrix, or Hamiltonian) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (eigenstate, spectrum, or eigenvalue) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (uncertainty relation, incompatible observables, or commutator) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** Quantum state; wave function; superposition
- **operator:** observable operator; matrix
- **spectrum:** eigenstate; spectrum; eigenvalue
- **boundary:** detector; preparation
- **incompatibility:** uncertainty relation; incompatible observables
- **protocol:** unitary evolution; projection or measurement update; path integral weighting

## Representation-Stable Content
- the rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation
- the operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels
- the dependence of admissible readout on measurement context or boundary condition
- the non-commuting compatibility structure, which survives changes of representation

## Representation-Dependent Content
- the name of the carrier: particle, wave, field, qubit, or excitation
- where time dependence is represented: on the state, on the operator, or in a path weight
- the coordinate system, basis, or geometric picture used to display the same relation
- the physical implementation of detector, boundary, preparation, or readout

## Validation Checks
- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.
