# Quantum decoherence

## Central Claim
Quantum decoherence is the loss of observable phase coherence in a subsystem when information about alternative amplitudes becomes encoded in environmental correlations.

## Formal Role
The combined system and environment may evolve unitarily while the reduced system loses interference. Interaction correlates different system alternatives with distinguishable environmental states; tracing over the environment then suppresses off-diagonal terms in the selected pointer basis. Decoherence does not by itself select one outcome, and it is not identical to memory. Markovian decoherence is possible when the reduced state still determines its future. Memory begins when discarded correlations return and two preparations with the same reduced state acquire different later statistics.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- A joint system-environment state and interaction are specified.
- Unitary evolution creates correlations between system alternatives and environmental states.
- Partial tracing gives the reduced density operator available to the observer.
- Interference visibility or off-diagonal coherence provides the readout.
- A divisibility or history test distinguishes Markovian decoherence from memory.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
\rho_S(t)=\operatorname{Tr}_E[U_{SE}(t)\rho_{SE}(0)U_{SE}^{\dagger}(t)]
\frac{|0\rangle|E_0\rangle+|1\rangle|E_1\rangle}{\sqrt2},\quad \rho_{01}\propto\langle E_1|E_0\rangle
\dot\rho_S=-\frac{i}{\hbar}[H_S,\rho_S]+\sum_k\gamma_k\mathcal D[L_k]\rho_S
V_{t+s}=V_tV_s\quad\text{only in the time-homogeneous Markov limit}
```

## Mechanism Roles
- **state:** joint system-environment state; reduced density operator; pointer basis
- **operator:** interaction Hamiltonian; partial trace; reduced dynamical map
- **spectrum:** coherence; interference visibility; purity
- **boundary:** initial environmental state; system-environment partition
- **incompatibility:** returning correlations; failure of divisible reduced dynamics
- **protocol:** prepare; couple; trace environment; measure interference

## Representation-Stable Content
- The joint state retains the phase information transferred from the subsystem into system-environment correlations.
- The reduced interference visibility is fixed by the overlap of the corresponding environmental states.
- Equivalent dilations give the same reduced channel and the same system observables.

## Representation-Dependent Content
- The preferred basis, decay rate, and recoherence depend on the interaction, environmental spectrum, and initial correlations.
- Changing the system-environment partition changes which correlations are hidden.
- A Markov approximation removes returning correlations; retaining them introduces auxiliary coordinates or a memory kernel.

## Validation Checks
- Interference visibility is compared with a control in which the environment cannot distinguish the alternatives.
- Two preparations with the same reduced state test whether hidden correlations alter later observables.
- Reversing or decoupling the interaction tests whether the lost coherence remains recoverable in the joint state.
