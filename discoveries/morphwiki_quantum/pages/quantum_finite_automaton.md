# Quantum finite automaton

## Evidence Status
A quantum finite automaton can be read as a quantum construction: the potential, domain, initial condition, or boundary condition fixes the admissible state space; the Hamiltonian, whose exponential gives unitary time evolution defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## The Standard Story
In quantum computing, quantum finite automata (QFA) or quantum state machines are a quantum analog of probabilistic automata or a Markov decision process. They provide a mathematical abstraction of real-world quantum computers.

## Mechanism Reading
In quantum-mechanical terms, a quantum finite automaton is described by a wave function or density operator defined on the Hilbert space allowed by the system's domain. The physical question is represented by the Hamiltonian, whose exponential gives unitary time evolution; the experimental or mathematical setting is the potential, domain, initial condition, or boundary condition. The observable content is obtained from the eigenvalues and eigenfunctions of the relevant observable. In the local terminology of this topic, the same construction appears through quantum state or state vector, matrix or unitary operator, and eigenvalue or energy level. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or uncertainty relation.

## Operational Contribution
- The standard article organizes concepts by topic names and historical formalisms; this page reorganizes them by the quantum construction that relates preparation, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution, rather than as a topic-specific vocabulary item.
- It turns analogy into a testable criterion: another system must supply a state space, admissible transformations, a readout basis, and a compatibility relation.

## Mechanism Form
- Preparation or domain terms (preparation condition, measurement setup, or potential or domain condition) determine which states are admissible.
- State terms (quantum state, state vector, or wave function) name the predictive carrier: vector, wave function, density operator, field state, or register state.
- Operator terms (matrix, unitary operator, or Hamiltonian) name the observable, Hamiltonian, unitary, or constraint acting on the carrier.
- Spectral terms (eigenvalue, energy level, or measurement outcome) name the outcome labels and projectors that define readout channels.
- The probability rule maps states and projectors to recorded probabilities through the Born rule, trace rule, or projection-valued measure.
- Compatibility terms (commutator, uncertainty relation, or non-commuting observables) mark cases where observables do not admit one common sharp readout basis.

## Mechanism Roles
- **state:** quantum state; state vector
- **operator:** matrix; unitary operator
- **spectrum:** eigenvalue; energy level; measurement outcome
- **boundary:** preparation condition; measurement setup; potential or domain condition
- **incompatibility:** commutator; uncertainty relation; non-commuting observables
- **protocol:** unitary evolution; projection or measurement update; path integral weighting

## Evidence Profile
- Routes: state evolution / transport: 0.28, closure / conservation: 0.24, operator and spectrum: 0.19, update protocol: 0.16, boundary or preparation: 0.06, non-commuting transformations: 0.05
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
- [1604.05385](https://arxiv.org/abs/1604.05385) — score 0.446
- [1706.03846](https://arxiv.org/abs/1706.03846) — score 0.442
- [1708.03640](https://arxiv.org/abs/1708.03640) — score 0.420
- [0908.0752](https://arxiv.org/abs/0908.0752) — score 0.410
- [1801.03283](https://arxiv.org/abs/1801.03283) — score 0.408
- [0806.4515](https://arxiv.org/abs/0806.4515) — score 0.402
- [1302.5510](https://arxiv.org/abs/1302.5510) — score 0.400
- [quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159) — score 0.398
- [1506.05598](https://arxiv.org/abs/1506.05598) — score 0.396
- [1604.06537](https://arxiv.org/abs/1604.06537) — score 0.393

---
Wikipedia scaffold: [Quantum finite automaton](https://en.wikipedia.org/wiki/Quantum_finite_automaton) (CC BY-SA). Synthesis from Wikipedia scaffold + 32 Hyperion equation witnesses. Not a claim of physical reduction.
