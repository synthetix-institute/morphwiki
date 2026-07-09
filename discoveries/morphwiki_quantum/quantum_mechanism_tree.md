# Quantum Theory As A Mechanism Tree

## Root
Given a context-selected Hilbert space, an admissible state, and a permitted observable, quantum theory determines which numerical outcomes can occur, assigns probabilities to those outcomes, and marks which questions cannot be made simultaneously sharp.

This reorders the topic away from historical names and toward the construction that recurs across the pages:

```text
SELECTOR -> CARRIER -> MAP -> QUESTION -> READOUT
    |          |        |         |          |
    |          |        |         |          +-- probabilities
    |          |        |         +------------- spectrum / effects
    |          |        +----------------------- generator or channel
    |          +-------------------------------- state or density operator
    +------------------------------------------- Hilbert space and operator domain

COMPATIBILITY constrains which questions can be jointly sharp.
REALIZATION adds boundaries, fields, detectors, protocols, and scaling limits.
```

## DAG Then Constructor

The DAG gives the assembly order: context and admissibility precede state transport; state transport precedes spectral readout; readout and compatibility precede boundary, field, detector, or protocol realization. The constructor fills this ordered scaffold with the carrier, operator, map, question, readout, closure condition, and realization needed for a predictive mechanism.

## Re-Derivation Path
1. **Selector.** A context selects the Hilbert space and operator domain. Euclidean space may label a representation, but Hilbert space is the admissible carrier.
2. **Carrier.** The state, density operator, field state, or register state carries predictive information on that selected space.
3. **Map.** A Hamiltonian, unitary, channel, constraint, or action transports the carrier before readout.
4. **Question.** An observable, effect family, or spectral measure defines the possible answer channels.
5. **Readout.** The Born or trace rule turns the state and answer channels into probabilities.
6. **Compatibility and realization.** Commutators, contextuality, uncertainty, boundaries, fields, detectors, and protocols constrain or embody the five-step constructor.

```math
B \longmapsto (\mathcal H_B,\mathcal D_B)
\rho_B\in\mathcal S(\mathcal H_B),\quad \rho_B\ge0,\quad \operatorname{Tr}\rho_B=1
\rho_t = U_t \rho_B U_t^\dagger
O = \sum_i \lambda_i P_i
p_i = \operatorname{Tr}(P_i \rho_t)
[O_1,O_2] \ne 0
```

## Sparse Attention Summary
- state evolution: mean 0.232, pages above 0.10 = 145
- normalization and admissibility: mean 0.165, pages above 0.10 = 136
- observables and spectra: mean 0.328, pages above 0.10 = 145
- preparation and boundary context: mean 0.095, pages above 0.10 = 54
- incompatible questions: mean 0.086, pages above 0.10 = 59
- controlled update protocol: mean 0.076, pages above 0.10 = 32

Interpretation: the stable evidence signal is observables-and-spectra. The mechanism tree orders quantum theory by construction role; the route scores explain why each role is supported.

## Tree
### Hilbert-space context: admissible carrier and basis
A quantum calculation first fixes the Hilbert space, operator domain, basis, preparation context, representation, gauge, or boundary condition. This is not the measured answer; it is the legal carrier on which states, transformations, observables, and probabilities can be defined.

Why it belongs here: This branch is the first step because quantum mechanics is not defined on raw objects. It begins by specifying the space, basis, representation, or admissibility condition in which states and questions make sense.

Representative pages:
- Mathematical formulation of quantum mechanics
- Hilbert space
- Transformation theory (quantum mechanics)
- Quantum differential calculus
- Quantum complexity theory
- Quantum cellular automaton
- Relativistic quantum mechanics

### State carrier inside Hilbert space
A state is the probability-bearing element of the selected Hilbert space or its density-operator state space. Wave functions, density matrices, superpositions, and coherent states are different representations of this predictive carrier.

Why it belongs here: The state branch should be introduced before particles.  It is the predictive carrier; particles, waves, fields, and qubits are later realizations of that carrier.

Representative pages:
- Density matrix
- Quantum superposition
- Quantum decoherence
- Superposition principle
- Coherence (physics)
- Wave function
- Quantum state
- Two-state quantum system
- 16 more pages in this branch

### Generator: lawful change before readout
Hamiltonians, unitary maps, equations of motion, and path weights describe the lawful transport of the state before a question is resolved.

Why it belongs here: Time evolution is a transport problem over states.  The Hamiltonian and path integral are two views of the same generator role rather than unrelated formalisms.

Representative pages:
- Unitary operator
- Perturbation theory
- Quantum dynamics
- Path integral formulation
- Hamiltonian mechanics
- Path integral
- Hamiltonian (quantum mechanics)
- Perturbation theory (quantum mechanics)
- 14 more pages in this branch

### Spectral question: what can be asked
An observable is a permitted question whose operator form determines the possible numerical answers.

Why it belongs here: The central unit is a legal question posed to a state. Spectra make the possible answers visible.

Representative pages:
- Angular momentum operator
- Observable
- Self-adjoint operator
- Spectral theory
- Pauli matrices
- Operator theory
- Operator (physics)
- Eigenvalues and eigenvectors
- 2 more pages in this branch

### Readout rule: how answers become probabilities
Measurement connects a state and an observable to recorded frequencies.  Projection, POVMs, Born weights, and collapse language are alternative ways of presenting this state-to-spectrum readout step.

Why it belongs here: Measurement is best placed after observables and spectra: it is the rule that turns spectral resolution into recorded probability, not the mystical starting point of the theory.

Representative pages:
- POVM
- Wave function collapse
- Born rule
- Measurement in quantum mechanics
- Quantum jump
- Measurement problem
- Quantum eraser experiment
- Projection-valued measure
- 2 more pages in this branch

### Compatibility limit: what cannot be jointly sharp
The non-classical part of the theory appears when two otherwise legal questions do not compose into one common sharp question.  Commutators, uncertainty relations, contextuality, Bell tests, and entanglement live here.

Why it belongs here: The non-classical core appears as failure of joint sharpness.  Entanglement, Bell phenomena, and uncertainty are different faces of this compatibility structure.

Representative pages:
- Bell's theorem
- Quantum entanglement
- Commutator
- Uncertainty principle
- Einstein–Podolsky–Rosen paradox
- Quantum nonlocality

### Boundary realization: how effects appear
Many named quantum effects are boundary realizations of the same construction.  A potential, barrier, box, cavity, detector, or medium changes the allowed spectral channels without changing the basic prediction problem.

Why it belongs here: Named effects such as tunnelling and particle-in-a-box are boundary realizations of the state-operator-readout construction.

Representative pages:
- Potential well
- Particle in a box
- Scattering
- Wave interference
- Quantum optics
- Spectral line
- S-matrix
- Quantum tunnelling
- 4 more pages in this branch

### Many-mode extension: fields, particles, and scaling
Quantum field theory, gauge theory, renormalization, photons, fermions, and related topics extend the same state-operator-spectrum logic to variable particle number, local fields, and scale-dependent descriptions.

Why it belongs here: Field theory and gauge theory extend the same construction to many modes, local generators, and scale-dependent descriptions.

Representative pages:
- Fermi–Dirac statistics
- Dirac equation
- Quantum electrodynamics
- Renormalization
- Gauge theory
- Photon
- Quantum field theory
- Fermion
- 13 more pages in this branch

### Protocol layer: engineered transformations
Quantum computing, channels, circuits, algorithms, networks, sensors, and error correction turn the same formal machinery into controlled sequences of operations.

Why it belongs here: Quantum information is the engineering layer: the same state-operator-readout machinery becomes a controlled sequence of transformations.

Representative pages:
- Quantum information science
- Quantum network
- Quantum algorithm
- Quantum error correction
- Quantum channel
- Quantum logic gate
- Quantum neural network
- Quantum circuit
- 10 more pages in this branch

### Annotations: history, interpretations, and popular frames
Some pages help readers navigate the subject but do not form steps in the mechanism. They are kept as annotations so books, historical figures, interpretations, and popular frames do not distort the constructive tree.

Why it belongs here: These pages remain useful for orientation and are placed downstream of the construction steps. This prevents biographies, books, and interpretations from becoming false roots of the mechanism.

Representative pages:
- Introduction to quantum mechanics
- Old quantum theory
- 14 more pages in this branch
- 14 historical, interpretive, or popular pages are treated as annotations downstream of the conceptual roots

## A New Reading Of Quantum Mechanics

Quantum mechanics can be introduced through a direct constructor order: first define the Hilbert space, operator domain, and basis; then define a state as a predictive carrier; then define lawful change; then define legal questions as operators; then show that each question exposes a spectrum of possible answers; then add the probability rule; only then introduce particles, waves, detectors, barriers, fields, and computers as realizations of this construction.

In this reading, the measurement problem is a junction where the readout protocol, context dependence, and incompatible questions meet.  Tunnelling is a boundary-shaped spectral channel with non-zero amplitude in a region that the classical energy description would exclude.

## Anomalies And Discovery Leads

These labels describe the role of a page in the mechanism tree, not the physical object named by the page. For example, a page can be structurally anomalous because context, protocol, or compatibility carries the explanation before spectra are read out.

Label guide:
- **weak spectral anchor**: another construction step carries the topic before spectra become meaningful.
- **boundary-driven dynamics**: the experimental context, boundary, apparatus, or representation is part of the mechanism rather than background description.
- **compatibility/closure junction**: the page joins the rules that make a state legal with the rules that limit which questions can be resolved together.
- **protocol is unusually explicit**: the order of operations is itself mechanistic; changing the sequence changes what can be inferred or observed.
- **multi-role hub**: several construction steps meet in one topic, so the page is a junction rather than a clean leaf in the tree.
- **branch-ambiguous**: the topic belongs at an interface between two explanatory roles and should be read as a bridge before branch assignment.

- **Schrödinger's cat**. Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, and branch-ambiguous. Branch: State carrier inside Hilbert space; secondary: Annotations: history, interpretations, and popular frames.
- **Einstein–Podolsky–Rosen paradox**. EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails. Flags: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, and multi-role hub. Branch: Compatibility limit: what cannot be jointly sharp; secondary: Annotations: history, interpretations, and popular frames.
- **Quantum biology**. Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control. Flags: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, and multi-role hub. Branch: Generator: lawful change before readout; secondary: Hilbert-space context: admissible carrier and basis.
- **Introduction to quantum mechanics**. An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Its technical content separates into individual branches before supporting specific derivations. Flags: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, and branch-ambiguous. Branch: Annotations: history, interpretations, and popular frames; secondary: State carrier inside Hilbert space.
- **Measurement problem**. The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Readout rule: how answers become probabilities; secondary: Generator: lawful change before readout.
- **Quantum gravity**. Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Many-mode extension: fields, particles, and scaling; secondary: Generator: lawful change before readout.
- **Scattering**. Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Boundary realization: how effects appear; secondary: Generator: lawful change before readout.
- **Quantum state**. Quantum state is the carrier rather than the final prediction. It precedes admissibility, evolution, observable choice, and probability readout. The unresolved distinction is whether the carrier is a vector, density operator, field state, or register, and which transformations preserve it. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: State carrier inside Hilbert space; secondary: Generator: lawful change before readout.
- **Wave–particle duality**. Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: State carrier inside Hilbert space; secondary: Compatibility limit: what cannot be jointly sharp.
- **Quantum entanglement**. Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. The required distinction is between joint state, subsystem observables, and correlation test. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Compatibility limit: what cannot be jointly sharp; secondary: State carrier inside Hilbert space.
- **Fermi–Dirac statistics**. Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. The formal content is anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Many-mode extension: fields, particles, and scaling; secondary: Hilbert-space context: admissible carrier and basis.
- **Hamiltonian (quantum mechanics)**. The Hamiltonian has two roles: it generates time evolution and, as an observable, supplies an energy spectrum. The formal split is domain/self-adjointness, unitary transport, conserved energy, and spectral readout. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Generator: lawful change before readout; secondary: Spectral question: what can be asked.

Possible leads:
- Search for systems where a state-like carrier and a legal-question operator exist, but the incompatibility relation has not been tested.  Those systems are candidates for quantum-like contextual behavior without importing quantum ontology.
- Treat tunnelling, particle-in-a-box, cavity optics, and spectral lines as one family of boundary-shaped spectra.  This suggests looking for overlooked boundary controls in systems currently described only by bulk evolution.
- Quantum computing should be read as an engineering layer over the state-operator-readout constructor. New protocols should be searched by composing lawful quantum questions and controlled maps.
- Pages that are branch-ambiguous are useful: they often mark junctions where two constructions meet, such as field theory joining transport, incompatibility, and boundary context.
- Historical, interpretive, and object-name pages should be demoted to annotations.  The conceptual spine is context, state, generator, spectral question, probability, compatibility, realization.
