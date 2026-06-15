# Quantum simulator

## Evidence Status
A quantum simulator can be read as a quantum construction: the chosen basis, pulse sequence, or measurement axis fixes the admissible state space; a Hamiltonian or unitary matrix rotating that state between preparation and measurement defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## The Standard Story
Quantum simulators permit the study of a quantum system in a programmable fashion. In this instance, simulators are special purpose devices designed to provide insight about specific physics problems.

## Mechanism Reading
In quantum-mechanical terms, a quantum simulator is described by a two-dimensional Hilbert space, usually written as a qubit state or a density matrix. The physical question is represented by a Hamiltonian or unitary matrix rotating that state between preparation and measurement; the experimental or mathematical setting is the chosen basis, pulse sequence, or measurement axis. The observable content is obtained from projectors onto the two eigenstates of the measured observable. In the local terminology of this topic, the same construction appears through superposition or wave function, Hamiltonian or unitary operator, and eigenvalue or energy level. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or uncertainty relation.

## Operational Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (preparation condition, measurement setup, or potential or domain condition) determine which states are admissible.
- State terms (superposition, wave function, or quantum state) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (Hamiltonian, unitary operator, or observable operator) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (eigenvalue, energy level, or measurement outcome) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (commutator, uncertainty relation, or non-commuting observables) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** superposition
- **operator:** Hamiltonian; unitary operator
- **spectrum:** eigenvalue; energy level; measurement outcome
- **boundary:** preparation condition; measurement setup; potential or domain condition
- **incompatibility:** commutator; uncertainty relation; non-commuting observables
- **protocol:** unitary evolution; projection or measurement update; path integral weighting

## Evidence Profile
- Routes: operator and spectrum: 0.30, state evolution / transport: 0.28, closure / conservation: 0.19, boundary or preparation: 0.12, update protocol: 0.11, non-commuting transformations: 0.05
- Fibers: field-specific vocabulary: 0.59, probability / information: 0.41, symbolic structure: 0.33, spectral profile: 0.33, geometric realization: 0.33

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
- [0912.2823](https://arxiv.org/abs/0912.2823) — score 0.526
- [1604.05385](https://arxiv.org/abs/1604.05385) — score 0.526
- [quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159) — score 0.506
- [1708.03640](https://arxiv.org/abs/1708.03640) — score 0.504
- [1801.03283](https://arxiv.org/abs/1801.03283) — score 0.503
- [1506.05598](https://arxiv.org/abs/1506.05598) — score 0.501
- [1612.00682](https://arxiv.org/abs/1612.00682) — score 0.501
- [0908.0752](https://arxiv.org/abs/0908.0752) — score 0.498
- [1706.03846](https://arxiv.org/abs/1706.03846) — score 0.489
- [1604.06537](https://arxiv.org/abs/1604.06537) — score 0.488

---
Wikipedia scaffold: [Quantum simulator](https://en.wikipedia.org/wiki/Quantum_simulator) (CC BY-SA). Synthesis from Wikipedia scaffold + 32 Hyperion equation witnesses. Not a claim of physical reduction.
