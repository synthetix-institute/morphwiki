# Quantum Theory Through Physical Roles

Quantum theories differ in what they treat as physical. Geometry may be fixed background or a quantum degree of freedom. An environment may be discarded or retained as memory. A detector may record an outcome or participate in the dynamics that produces it. The map is organized by these changes of physical role.

## Predictive Closure

At a chosen resolution, a physical theory is closed when its declared state fixes future observable probabilities and its allowed transformations compose consistently. If either condition fails, the smallest missing field, state coordinate, operator, closure condition, observable, or protocol must enter the theory.

```math
q(h_1)=q(h_2)\Longrightarrow p(y,t\mid h_1)=p(y,t\mid h_2),\qquad T_{\gamma_1}=T_{\gamma_2}\ \text{for physically equivalent paths}
```

The first relation requires the declared state to contain every coordinate needed for later probabilities. The second requires equivalent sequences of transformations to agree. Hidden environmental correlations violate the first relation; curvature, frustration, and other path-dependent effects violate the second. A complete theory restores closure by adding the smallest missing physical object.

## A Quantum Mechanism

```text
(Omega, Xi) -> M -> I_op=(M; C, R, P) -> I_real=(I_op; A)
```

A physical state `q` belongs to `Xi`, the space of admissible states. The operation `Omega` moves that state, constrains it, or asks a measurable question of it. Their pair `M=(Omega,Xi)` is the mechanism core. Closure `C` fixes domains and admissibility. The map `R` gives probabilities or observables, and `P` gives the order of preparation, control, and measurement. The realization `A` fixes the fields, material, geometry, parameters, and apparatus.

The clauses are physically coupled. A Hamiltonian requires a domain. A measurement requires an admissible state and a positive probability rule. A control sequence must preserve the constraints of every intermediate state. Removing any one of these relations leaves the prediction undefined or ambiguous.

```math
\Xi_Q=(\mathcal H,\mathcal D,\mathcal S),\qquad \Omega_Q=\{G,O,\mathcal E,\ldots\}
I_{\mathrm{op},Q}=((\Omega_Q,\Xi_Q);C_Q,R_Q,P_Q)
\rho_0\xrightarrow[P_Q,C_Q]{G}\rho_t,\qquad p(y)=\operatorname{Tr}(E_y\rho_t)
```

Here the density operator `rho` is the state. The Hilbert space, state class, and domain belong to `Xi_Q`; generators, observables, and channels belong to `Omega_Q`. The Born rule then converts the evolved state and the measurement operators into outcome probabilities.

## Role Promotion

A quantity remains realization data while it selects parameters within a fixed state space, operator domain, closure, observable, and protocol. It changes physical role when it alters one of those objects. The promoted quantity must then be represented in the corresponding clause of the mechanism.

```math
\begin{aligned}a\in A\quad &\text{while}\quad (\Xi,\Omega,C,R,P)_a=(\Xi,\Omega,C,R,P),\\a\longrightarrow X\in\{\Xi,\Omega,C,R,P\}\quad &\text{when the physical object }X\text{ changes}.\end{aligned}
```

The resulting promotions connect the major frontiers of quantum theory:

- **A background becomes a quantum field** (`A -> Xi, Omega`). A prescribed background potential or geometry becomes a fluctuating degree of freedom with its own state and equation of motion. The enlarged theory contains quanta, correlations, and back-reaction that a fixed background cannot carry.
- **Geometry becomes part of the quantum state** (`A -> Xi, Omega`). Distances, areas, connections, or causal relations cease to label a fixed arena and enter the quantum state and dynamics. Geometric observables acquire spectra and fluctuations, while matter and geometry must evolve consistently.
- **An environment becomes a retained degree of freedom** (`A -> Xi, Omega, C`). Environmental correlations that influence later motion are retained as state variables or represented by a memory kernel. The future reduced state can depend on earlier interactions rather than on its present coordinates alone.
- **An apparatus becomes part of the quantum dynamics** (`A -> Xi, Omega, R`). A detector or amplifier is represented as an interacting quantum subsystem and an outcome-resolved channel. Back-action, conditional state change, and detector noise become calculable parts of the outcome probabilities.
- **A boundary becomes a closure condition** (`A -> C, Omega`). A wall, interface, or asymptotic condition selects the operator domain or self-adjoint extension. The allowed spectrum, scattering channels, and edge states change with the domain of the operator.
- **A constraint defines the physical state space** (`C -> Xi`). Gauge conditions, exchange symmetry, or superselection rules remove vectors that do not represent physical states. The surviving Hilbert-space sectors determine particle statistics, charges, and admissible observables.
- **A subsystem split becomes part of the state space** (`A -> Xi, C`). A chosen partition into subsystems fixes the tensor-product or algebraic decomposition used to define locality. Entanglement and Bell correlations become properties of the joint state relative to that decomposition.
- **An ordered protocol becomes a dynamical map** (`P -> Omega`). A sequence of controls, measurements, and conditional operations is composed into a channel or effective generator. Changing the order changes the implemented unitary, channel, or feedback law even when the same elementary operations are used.
- **Scale becomes part of the law** (`A -> Omega, C`). The observation scale changes effective couplings or operators rather than merely changing numerical resolution. Renormalization flow connects different effective laws and exposes fixed points, relevant operators, and universality classes.

## Transformations And Missing Physics

A transformation relates two mechanisms while naming the amplitude, expectation value, operator algebra, current, or probability law that should remain unchanged:

```math
I_i=((\Omega_i,\Xi_i);C_i,R_i,P_i) \xrightarrow{T} I_j=((\Omega_j,\Xi_j);C_j,R_j,P_j),
\qquad \Delta_{\alpha,\beta}=\Omega_j\alpha-\beta\Omega_i.
```

When `Delta` vanishes, the retained mechanism has another realization. When it closes as a reproducible operator and changes an independent observable, the missing term becomes a candidate field, interaction, boundary contribution, or internal coordinate. Predictive closure therefore connects transfer and theory extension in one calculation.

## The Quantum Map

### State space, domain, and representation
The Hilbert or Fock space, operator domain, basis, gauge sector, and subsystem decomposition determine which states and operations exist. Changing this structure can change the theory before any Hamiltonian parameter is varied.

Representative topics: Transformation theory (quantum mechanics); Mathematical formulation of quantum mechanics; Hilbert space; Quantum differential calculus; Quantum mechanics; Old quantum theory; Fourier transform.

### Quantum states and subsystem structure
A state is the probability-bearing element of the selected Hilbert space or its density-operator state space. Wave functions, density matrices, superpositions, and coherent states are different representations of this predictive carrier.

Representative topics: Density matrix; Quantum superposition; Quantum decoherence; Coherence (physics); Superposition principle; Wave function; Quantum state; Two-state quantum system.

### Dynamics and transformations
Hamiltonians, unitary maps, equations of motion, and path weights describe the lawful transport of the state before a question is resolved.

Representative topics: Unitary operator; Perturbation theory; Quantum dynamics; Path integral formulation; Hamiltonian mechanics; Path integral; Hamiltonian (quantum mechanics); Perturbation theory (quantum mechanics).

### Observables and spectra
An observable is a permitted question whose operator form determines the possible numerical answers.

Representative topics: Spectral theory; Pauli matrices; Angular momentum operator; Observable; Self-adjoint operator; Operator theory; Operator (physics); Eigenvalues and eigenvectors.

### Noncommuting observables
Two observables need not possess a common sharp spectral resolution. Their commutator and uncertainty relations quantify this algebraic incompatibility. Entanglement belongs instead to the structure of composite states, while Bell experiments join that state structure to local measurements.

Representative topics: Commutator; Uncertainty principle; Canonical commutation relation.

### Measurement, instruments, and probabilities
Measurement connects a state and an observable to recorded frequencies.  Projection, POVMs, Born weights, and collapse language are alternative ways of presenting this state-to-spectrum probability assignment.

Representative topics: POVM; Measurement in quantum mechanics; Quantum jump; Wave function collapse; Born rule; Measurement problem; Quantum eraser experiment; Projection-valued measure.

### Control sequences and quantum channels
Quantum computing, channels, circuits, algorithms, networks, sensors, and error correction turn the same formal machinery into controlled sequences of operations.

Representative topics: Quantum computing; Quantum information science; Quantum network; Quantum algorithm; Quantum error correction; Quantum channel; Quantum logic gate; Quantum neural network.

### Boundaries and operator domains
Walls, interfaces, asymptotic conditions, and media become part of the mechanism when they select the operator domain. The resulting self-adjoint extension fixes spectra, scattering channels, tunnelling amplitudes, and edge states.

Representative topics: Potential well; Scattering; Particle in a box; Quantum optics; Wave interference; Spectral line; Quantum tunnelling; S-matrix.

### Fields, constraints, and scale
Quantum field theory promotes fields to operator-valued degrees of freedom. Gauge constraints select the physical Hilbert space, particle statistics select admissible sectors, and renormalization makes the effective law depend on scale.

Representative topics: Gauge theory; Photon; Renormalization; Quantum field theory; Fermi–Dirac statistics; Dirac equation; Quantum electrodynamics; Boson.

### Annotations: history, interpretations, and popular frames
Some pages help readers navigate the subject but do not form steps in the mechanism. They are kept as annotations so books, historical figures, interpretations, and popular frames do not distort the constructive tree.

Representative topics: Introduction to Quantum Mechanics (book); Quantum mind; Erwin Schrödinger; History of quantum mechanics; Introduction to quantum mechanics; History of quantum field theory; David Hilbert; Quantum Computing: A Gentle Introduction.

## Constructing A Theory

- **Complete.** Add a missing closure, observable map, or protocol clause to a partial mechanism.
- **Reattach.** Retain an operation and replace its carrier, or retain a carrier and replace its operation.
- **Compose.** Join supported transformations into a mechanism not written as one source equation.
- **Deform.** Vary a parameter, boundary, scale, or representation while tracking a stated invariant.
- **Observe.** Construct the observable or intervention that exposes a predicted consequence.
- **Revise.** Use a failed consequence to identify and replace the clause responsible for the failure.

A detached law `(Omega,0)` and a target state space `(0,Xi')` define a concrete theoretical problem. The law becomes physical on the new state space only after its domain, closure, observable, and realization have been derived. The same calculation either produces a new embodiment or identifies the term needed to restore predictive closure.

## Sources

A paper is cited on a topic page only when one of its equations supports the displayed physical relation. Candidate identifiers without a matching equation remain absent from the public text. This build records the unresolved topics in the reproduction report.
