# Quantum information

## Evidence Status
A quantum information can be read as a quantum construction: the chosen basis, pulse sequence, or measurement axis fixes the admissible state space; a Hamiltonian or unitary matrix rotating that state between preparation and measurement defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## The Standard Story
Quantum information is the information of the state of a quantum system. It is the basic entity of study in quantum information science, and can be manipulated using quantum information processing techniques.

## Mechanism Reading
In quantum-mechanical terms, a quantum information is described by a two-dimensional Hilbert space, usually written as a qubit state or a density matrix. The physical question is represented by a Hamiltonian or unitary matrix rotating that state between preparation and measurement; the experimental or mathematical setting is the chosen basis, pulse sequence, or measurement axis. The observable content is obtained from projectors onto the two eigenstates of the measured observable. In the local terminology of this topic, the same construction appears through quantum state or density matrix, observable operator or matrix, and eigenstate or eigenvalue. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through uncertainty relation or non-commuting observables.

## Operational Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (preparation, basis, or preparation context) determine which states are admissible.
- State terms (quantum state, density matrix, or wave function) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (observable operator, matrix, or unitary operator) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (eigenstate, eigenvalue, or measurement outcome) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (uncertainty relation, non-commuting observables, or commutator) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** quantum state; density matrix
- **operator:** observable operator; matrix; unitary operator
- **spectrum:** eigenstate; eigenvalue
- **boundary:** preparation; basis
- **incompatibility:** uncertainty relation; non-commuting observables
- **protocol:** unitary evolution; projection or measurement update; path integral weighting

## Evidence Profile
- Routes: operator and spectrum: 0.38, state evolution / transport: 0.26, closure / conservation: 0.21, non-commuting transformations: 0.13, update protocol: 0.07, boundary or preparation: 0.07
- Fibers: field-specific vocabulary: 0.59, probability / information: 0.41, spectral profile: 0.34, symbolic structure: 0.34, geometric realization: 0.32

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

## Validation Boundary
- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links
- [1604.06537](https://arxiv.org/abs/1604.06537) — score 0.521
- [0912.2823](https://arxiv.org/abs/0912.2823) — score 0.501
- [1604.05385](https://arxiv.org/abs/1604.05385) — score 0.500
- [1612.00682](https://arxiv.org/abs/1612.00682) — score 0.493
- [1801.03283](https://arxiv.org/abs/1801.03283) — score 0.492
- [quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159) — score 0.490
- [1506.05598](https://arxiv.org/abs/1506.05598) — score 0.486
- [1708.03640](https://arxiv.org/abs/1708.03640) — score 0.480
- [0908.0752](https://arxiv.org/abs/0908.0752) — score 0.473
- [1706.03846](https://arxiv.org/abs/1706.03846) — score 0.451

---
Wikipedia scaffold: [Quantum information](https://en.wikipedia.org/wiki/Quantum_information) (CC BY-SA). Synthesis from Wikipedia scaffold + 32 Hyperion equation witnesses. Not a claim of physical reduction.
