# Quantum teleportation

## Evidence Status
A quantum teleportation can be read as a quantum construction: the chosen basis, pulse sequence, or measurement axis fixes the admissible state space; a Hamiltonian or unitary matrix rotating that state between preparation and measurement defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## The Standard Story
Quantum teleportation is a technique for transferring quantum information from a sender at one location to a receiver some distance away. While teleportation is commonly portrayed in science fiction as a means to transfer physical objects from one location to the next, quantum teleportation only transfers quantum information.

## Mechanism Reading
In quantum-mechanical terms, a quantum teleportation is described by a two-dimensional Hilbert space, usually written as a qubit state or a density matrix. The physical question is represented by a Hamiltonian or unitary matrix rotating that state between preparation and measurement; the experimental or mathematical setting is the chosen basis, pulse sequence, or measurement axis. The observable content is obtained from projectors onto the two eigenstates of the measured observable. In the local terminology of this topic, the same construction appears through quantum state or superposition, Hamiltonian or observable operator, and eigenvalue or energy level. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or uncertainty relation.

## Operational Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (basis, preparation context, or measurement basis) determine which states are admissible.
- State terms (quantum state, superposition, or wave function) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (Hamiltonian, observable operator, or generator) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (eigenvalue, energy level, or measurement outcome) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (commutator, uncertainty relation, or non-commuting observables) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** quantum state; superposition
- **operator:** Hamiltonian; observable operator; generator
- **spectrum:** eigenvalue; energy level; measurement outcome
- **boundary:** basis
- **incompatibility:** commutator; uncertainty relation; non-commuting observables
- **protocol:** projection update

## Evidence Profile
- Routes: operator and spectrum: 0.38, state evolution / transport: 0.17, update protocol: 0.11, closure / conservation: 0.11, boundary or preparation: 0.08, non-commuting transformations: 0.06
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
- [1604.05385](https://arxiv.org/abs/1604.05385) — score 0.536
- [0912.2823](https://arxiv.org/abs/0912.2823) — score 0.497
- [2308.15676](https://arxiv.org/abs/2308.15676) — score 0.486
- [1612.00682](https://arxiv.org/abs/1612.00682) — score 0.484
- [quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159) — score 0.474
- [0809.5271](https://arxiv.org/abs/0809.5271) — score 0.473
- [2105.11733](https://arxiv.org/abs/2105.11733) — score 0.472
- [2108.07838](https://arxiv.org/abs/2108.07838) — score 0.470
- [1506.05598](https://arxiv.org/abs/1506.05598) — score 0.469
- [0805.4565](https://arxiv.org/abs/0805.4565) — score 0.466

---
Wikipedia scaffold: [Quantum teleportation](https://en.wikipedia.org/wiki/Quantum_teleportation) (CC BY-SA). Synthesis from Wikipedia scaffold + 32 Hyperion equation witnesses. Not a claim of physical reduction.
