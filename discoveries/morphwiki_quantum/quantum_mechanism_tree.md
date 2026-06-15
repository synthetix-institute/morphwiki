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
- state evolution: mean 0.232, pages above 0.10 = 146
- normalization and admissibility: mean 0.165, pages above 0.10 = 136
- observables and spectra: mean 0.327, pages above 0.10 = 146
- preparation and boundary context: mean 0.094, pages above 0.10 = 54
- incompatible questions: mean 0.086, pages above 0.10 = 59
- controlled update protocol: mean 0.075, pages above 0.10 = 32

Interpretation: the stable evidence signal is observables-and-spectra, but the mechanism tree is not the same object as the evidence ranking.  The tree orders quantum theory by construction role; the route scores explain why each role is supported.

## Tree
### Hilbert-space context: admissible carrier and basis
A quantum calculation first fixes the Hilbert space, operator domain, basis, preparation context, representation, gauge, or boundary condition. This is not the measured answer; it is the legal carrier on which states, transformations, observables, and probabilities can be defined.

Why it belongs here: This branch is the first step because quantum mechanics is not defined on raw objects. It begins by specifying the space, basis, representation, or admissibility condition in which states and questions make sense.

Representative pages:
- Mathematical formulation of quantum mechanics - evidence route: observables and spectra (0.40); assignment score 1.41
- Hilbert space - evidence route: observables and spectra (0.42); assignment score 1.40
- Transformation theory (quantum mechanics) - evidence route: observables and spectra (0.43); assignment score 1.14
- Quantum differential calculus - evidence route: observables and spectra (0.38); assignment score 0.88
- Quantum complexity theory - evidence route: preparation and boundary context (0.25); assignment score 0.75
- Quantum cellular automaton - evidence route: preparation and boundary context (0.28); assignment score 0.71
- Relativistic quantum mechanics - evidence route: state evolution (0.27); assignment score 0.71

### State carrier inside Hilbert space
A state is the probability-bearing element of the selected Hilbert space or its density-operator state space. Wave functions, density matrices, superpositions, and coherent states are different representations of this predictive carrier.

Why it belongs here: The state branch should be introduced before particles.  It is the predictive carrier; particles, waves, fields, and qubits are later realizations of that carrier.

Representative pages:
- Density matrix - evidence route: observables and spectra (0.43); assignment score 1.54
- Quantum superposition - evidence route: observables and spectra (0.41); assignment score 1.53
- Quantum decoherence - evidence route: observables and spectra (0.37); assignment score 1.52
- Superposition principle - evidence route: observables and spectra (0.31); assignment score 1.51
- Coherence (physics) - evidence route: observables and spectra (0.37); assignment score 1.50
- Wave function - evidence route: state evolution (0.26); assignment score 1.48
- Quantum state - evidence route: state evolution (0.27); assignment score 1.46
- Two-state quantum system - evidence route: observables and spectra (0.43); assignment score 1.44
- 16 more pages in this branch

### Generator: lawful change before readout
Hamiltonians, unitary maps, equations of motion, and path weights describe the lawful transport of the state before a question is resolved.

Why it belongs here: Time evolution is a transport problem over states.  The Hamiltonian and path integral are two views of the same generator role rather than unrelated formalisms.

Representative pages:
- Unitary operator - evidence route: observables and spectra (0.44); assignment score 1.50
- Perturbation theory - evidence route: observables and spectra (0.39); assignment score 1.50
- Quantum dynamics - evidence route: observables and spectra (0.39); assignment score 1.50
- Path integral formulation - evidence route: observables and spectra (0.34); assignment score 1.49
- Hamiltonian mechanics - evidence route: observables and spectra (0.41); assignment score 1.49
- Path integral - evidence route: observables and spectra (0.24); assignment score 1.48
- Hamiltonian (quantum mechanics) - evidence route: state evolution (0.26); assignment score 1.47
- Perturbation theory (quantum mechanics) - evidence route: observables and spectra (0.26); assignment score 1.46
- 14 more pages in this branch

### Spectral question: what can be asked
An observable is a permitted question whose operator form determines the possible numerical answers.

Why it belongs here: The central unit is not a microscopic entity but a legal question.  Spectra make the possible answers visible.

Representative pages:
- Angular momentum operator - evidence route: observables and spectra (0.38); assignment score 1.48
- Observable - evidence route: observables and spectra (0.40); assignment score 1.47
- Self-adjoint operator - evidence route: observables and spectra (0.43); assignment score 1.47
- Spectral theory - evidence route: observables and spectra (0.44); assignment score 1.41
- Pauli matrices - evidence route: observables and spectra (0.42); assignment score 1.35
- Operator theory - evidence route: observables and spectra (0.43); assignment score 1.34
- Operator (physics) - evidence route: observables and spectra (0.37); assignment score 1.30
- Eigenvalues and eigenvectors - evidence route: observables and spectra (0.38); assignment score 1.48
- 2 more pages in this branch

### Readout rule: how answers become probabilities
Measurement connects a state and an observable to recorded frequencies.  Projection, POVMs, Born weights, and collapse language are alternative ways of presenting this state-to-spectrum readout step.

Why it belongs here: Measurement is best placed after observables and spectra: it is the rule that turns spectral resolution into recorded probability, not the mystical starting point of the theory.

Representative pages:
- POVM - evidence route: observables and spectra (0.41); assignment score 1.47
- Wave function collapse - evidence route: observables and spectra (0.35); assignment score 1.45
- Born rule - evidence route: observables and spectra (0.39); assignment score 1.45
- Measurement in quantum mechanics - evidence route: observables and spectra (0.40); assignment score 1.39
- Quantum jump - evidence route: observables and spectra (0.43); assignment score 1.32
- Measurement problem - evidence route: state evolution (0.27); assignment score 1.28
- Quantum eraser experiment - evidence route: observables and spectra (0.32); assignment score 1.23
- Projection-valued measure - evidence route: observables and spectra (0.41); assignment score 1.19
- 2 more pages in this branch

### Compatibility limit: what cannot be jointly sharp
The non-classical part of the theory appears when two otherwise legal questions do not compose into one common sharp question.  Commutators, uncertainty relations, contextuality, Bell tests, and entanglement live here.

Why it belongs here: The non-classical core appears as failure of joint sharpness.  Entanglement, Bell phenomena, and uncertainty are different faces of this compatibility structure.

Representative pages:
- Bell's theorem - evidence route: observables and spectra (0.30); assignment score 1.42
- Quantum entanglement - evidence route: state evolution (0.27); assignment score 1.38
- Commutator - evidence route: observables and spectra (0.41); assignment score 1.33
- Uncertainty principle - evidence route: observables and spectra (0.40); assignment score 1.32
- Einstein–Podolsky–Rosen paradox - evidence route: state evolution (0.27); assignment score 1.13
- Quantum nonlocality - evidence route: observables and spectra (0.30); assignment score 1.10

### Boundary realization: how effects appear
Many named quantum effects are boundary realizations of the same construction.  A potential, barrier, box, cavity, detector, or medium changes the allowed spectral channels without changing the basic prediction problem.

Why it belongs here: Named effects such as tunnelling and particle-in-a-box are boundary realizations.  They are not separate conceptual primitives.

Representative pages:
- Potential well - evidence route: observables and spectra (0.42); assignment score 1.44
- Particle in a box - evidence route: observables and spectra (0.42); assignment score 1.42
- Scattering - evidence route: state evolution (0.27); assignment score 1.39
- Wave interference - evidence route: observables and spectra (0.36); assignment score 1.37
- Quantum optics - evidence route: observables and spectra (0.34); assignment score 1.37
- Spectral line - evidence route: observables and spectra (0.27); assignment score 0.92
- S-matrix - evidence route: observables and spectra (0.39); assignment score 1.44
- Quantum tunnelling - evidence route: observables and spectra (0.42); assignment score 1.42
- 4 more pages in this branch

### Many-mode extension: fields, particles, and scaling
Quantum field theory, gauge theory, renormalization, photons, fermions, and related topics extend the same state-operator-spectrum logic to variable particle number, local fields, and scale-dependent descriptions.

Why it belongs here: Field theory and gauge theory extend the same construction to many modes, local generators, and scale-dependent descriptions.

Representative pages:
- Fermi–Dirac statistics - evidence route: state evolution (0.26); assignment score 1.50
- Dirac equation - evidence route: observables and spectra (0.30); assignment score 1.50
- Quantum electrodynamics - evidence route: observables and spectra (0.26); assignment score 1.50
- Renormalization - evidence route: observables and spectra (0.38); assignment score 1.50
- Gauge theory - evidence route: observables and spectra (0.39); assignment score 1.49
- Photon - evidence route: observables and spectra (0.40); assignment score 1.48
- Quantum field theory - evidence route: observables and spectra (0.27); assignment score 1.47
- Fermion - evidence route: state evolution (0.28); assignment score 1.42
- 14 more pages in this branch

### Protocol layer: engineered transformations
Quantum computing, channels, circuits, algorithms, networks, sensors, and error correction turn the same formal machinery into controlled sequences of operations.

Why it belongs here: Quantum information is the engineering layer: the same state-operator-readout machinery becomes a controlled sequence of transformations.

Representative pages:
- Quantum information science - evidence route: observables and spectra (0.35); assignment score 1.42
- Quantum network - evidence route: observables and spectra (0.32); assignment score 1.42
- Quantum algorithm - evidence route: observables and spectra (0.32); assignment score 1.42
- Quantum error correction - evidence route: observables and spectra (0.39); assignment score 1.41
- Quantum channel - evidence route: observables and spectra (0.40); assignment score 1.40
- Quantum logic gate - evidence route: observables and spectra (0.43); assignment score 1.39
- Quantum neural network - evidence route: observables and spectra (0.42); assignment score 1.39
- Quantum circuit - evidence route: observables and spectra (0.41); assignment score 1.39
- 10 more pages in this branch

### Annotations: history, interpretations, and popular frames
Some pages help readers navigate the subject but do not form steps in the mechanism. They are kept as annotations so books, historical figures, interpretations, and popular frames do not distort the constructive tree.

Why it belongs here: These pages remain useful for orientation, but they are deliberately not treated as construction steps. This prevents biographies, books, and interpretations from becoming false roots of the mechanism.

Representative pages:
- Introduction to quantum mechanics - evidence route: observables and spectra (0.29); assignment score 0.72
- Old quantum theory - evidence route: observables and spectra (0.34); assignment score 0.91
- 14 more pages in this branch
- 14 historical, interpretive, or popular pages are treated as annotations, not as conceptual roots

## A New Reading Of Quantum Mechanics

Quantum mechanics can be introduced through a direct constructor order: first define the Hilbert space, operator domain, and basis; then define a state as a predictive carrier; then define lawful change; then define legal questions as operators; then show that each question exposes a spectrum of possible answers; then add the probability rule; only then introduce particles, waves, detectors, barriers, fields, and computers as realizations of this construction.

In this reading, the measurement problem is not the root of the subject.  It is a junction where the readout protocol, context dependence, and incompatible questions meet.  Likewise, tunnelling is not a paradox about a particle crossing a wall; it is a boundary-shaped spectral channel with non-zero amplitude in a region that the classical energy description would exclude.

## Anomalies And Discovery Leads

These labels describe the role of a page in the mechanism tree, not the physical object named by the page. For example, a page can be structurally anomalous because context, protocol, or compatibility carries the explanation before spectra are read out.

Label guide:
- **weak spectral anchor**: another construction step carries the topic before spectra become meaningful.
- **boundary-driven dynamics**: the experimental context, boundary, apparatus, or representation is part of the mechanism rather than background description.
- **compatibility/closure junction**: the page joins the rules that make a state legal with the rules that limit which questions can be resolved together.
- **protocol is unusually explicit**: the order of operations is itself mechanistic; changing the sequence changes what can be inferred or observed.
- **multi-role hub**: several construction steps meet in one topic, so the page is a junction rather than a clean leaf in the tree.
- **branch-ambiguous**: the topic belongs at an interface between two explanatory roles and should be read as a bridge, not assigned to one branch too early.

- **Schrödinger's cat**. Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, and branch-ambiguous. Branch: State carrier inside Hilbert space; secondary: Annotations: history, interpretations, and popular frames.
- **Einstein–Podolsky–Rosen paradox**. EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails. Flags: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, and multi-role hub. Branch: Compatibility limit: what cannot be jointly sharp; secondary: Annotations: history, interpretations, and popular frames.
- **Quantum biology**. Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control. Flags: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, and multi-role hub. Branch: Generator: lawful change before readout; secondary: Hilbert-space context: admissible carrier and basis.
- **Introduction to quantum mechanics**. An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims. Flags: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, and branch-ambiguous. Branch: Annotations: history, interpretations, and popular frames; secondary: State carrier inside Hilbert space.
- **Measurement problem**. The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Readout rule: how answers become probabilities; secondary: Generator: lawful change before readout.
- **Quantum gravity**. Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Many-mode extension: fields, particles, and scaling; secondary: Generator: lawful change before readout.
- **Scattering**. Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Boundary realization: how effects appear; secondary: Generator: lawful change before readout.
- **Quantum state**. Quantum state is the carrier rather than the final prediction. It precedes admissibility, evolution, observable choice, and probability readout. State whether the carrier is a vector, density operator, field state, or register, and which transformations preserve it. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: State carrier inside Hilbert space; secondary: Generator: lawful change before readout.
- **Wave–particle duality**. Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: State carrier inside Hilbert space; secondary: Compatibility limit: what cannot be jointly sharp.
- **Quantum entanglement**. Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. Separate the joint state, subsystem observables, and correlation test. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Compatibility limit: what cannot be jointly sharp; secondary: State carrier inside Hilbert space.
- **Fermi–Dirac statistics**. Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. Expose anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Many-mode extension: fields, particles, and scaling; secondary: Hilbert-space context: admissible carrier and basis.
- **Hamiltonian (quantum mechanics)**. The Hamiltonian has two roles: it generates time evolution and, as an observable, supplies an energy spectrum. Separate domain/self-adjointness, unitary transport, conserved energy, and spectral readout. Flags: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, and multi-role hub. Branch: Generator: lawful change before readout; secondary: Spectral question: what can be asked.

Possible leads:
- Search for systems where a state-like carrier and a legal-question operator exist, but the incompatibility relation has not been tested.  Those systems are candidates for quantum-like contextual behavior without importing quantum ontology.
- Treat tunnelling, particle-in-a-box, cavity optics, and spectral lines as one family of boundary-shaped spectra.  This suggests looking for overlooked boundary controls in systems currently described only by bulk evolution.
- Quantum computing should be read as an engineering layer over the state-operator-readout constructor, not as a separate foundation. New protocols should be searched by composing lawful quantum questions and controlled maps, not by naming new qubit objects.
- Pages that are branch-ambiguous are useful: they often mark junctions where two constructions meet, such as field theory joining transport, incompatibility, and boundary context.
- Historical, interpretive, and object-name pages should be demoted to annotations.  The conceptual spine is context, state, generator, spectral question, probability, compatibility, realization.

## Boundary
This tree is a mechanism-indexed synthesis from MorphWiki pages and Hyperion witness profiles.  It supports reading, hypothesis generation, and constructor-target selection; formal derivation and experimental validation promote a proposed mechanism into a physical claim.
