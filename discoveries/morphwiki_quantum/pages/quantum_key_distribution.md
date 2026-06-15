# Quantum key distribution

## Evidence Status
A quantum key distribution can be read as a quantum construction: the chosen basis, pulse sequence, or measurement axis fixes the admissible state space; a Hamiltonian or unitary matrix rotating that state between preparation and measurement defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## The Standard Story
Quantum key distribution (QKD) is a secure communication method that implements a cryptographic protocol based on the laws of quantum mechanics, specifically quantum entanglement, the measurement-disturbance principle, and the no-cloning theorem. The goal of QKD is to enable two parties to produce a shared random secret key known only to them, which then can be used to encrypt and decrypt messages.

## Mechanism Reading
In quantum-mechanical terms, a quantum key distribution is described by a two-dimensional Hilbert space, usually written as a qubit state or a density matrix. The physical question is represented by a Hamiltonian or unitary matrix rotating that state between preparation and measurement; the experimental or mathematical setting is the chosen basis, pulse sequence, or measurement axis. The observable content is obtained from projectors onto the two eigenstates of the measured observable. In the local terminology of this topic, the same construction appears through quantum state or wave function, Hamiltonian or observable operator, and Mode or eigenstate. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or uncertainty relation.

## Operational Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (basis, preparation context, or measurement basis) determine which states are admissible.
- State terms (quantum state, wave function, or density operator) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (Hamiltonian, observable operator, or generator) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (Mode, eigenstate, or eigenvalue) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (commutator, uncertainty relation, or non-commuting observables) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** quantum state
- **operator:** Hamiltonian; observable operator; generator
- **spectrum:** Mode; eigenstate
- **boundary:** basis
- **incompatibility:** commutator; uncertainty relation; non-commuting observables
- **protocol:** unitary evolution; projection or measurement update; path integral weighting

## Evidence Profile
- Routes: operator and spectrum: 0.41, state evolution / transport: 0.18, closure / conservation: 0.16, update protocol: 0.07, boundary or preparation: 0.04, non-commuting transformations: 0.04
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
- [1604.05385](https://arxiv.org/abs/1604.05385) — score 0.583
- [1612.00682](https://arxiv.org/abs/1612.00682) — score 0.573
- [quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159) — score 0.566
- [1801.03283](https://arxiv.org/abs/1801.03283) — score 0.563
- [1506.05598](https://arxiv.org/abs/1506.05598) — score 0.560
- [2308.15676](https://arxiv.org/abs/2308.15676) — score 0.556
- [1604.06537](https://arxiv.org/abs/1604.06537) — score 0.548
- [1708.03640](https://arxiv.org/abs/1708.03640) — score 0.547
- [2105.11733](https://arxiv.org/abs/2105.11733) — score 0.544
- [0809.5271](https://arxiv.org/abs/0809.5271) — score 0.542

---
Wikipedia scaffold: [Quantum key distribution](https://en.wikipedia.org/wiki/Quantum_key_distribution) (CC BY-SA). Synthesis from Wikipedia scaffold + 32 Hyperion equation witnesses. Not a claim of physical reduction.
