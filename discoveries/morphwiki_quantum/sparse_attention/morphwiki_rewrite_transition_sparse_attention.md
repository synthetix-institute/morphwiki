# Quantum Rewrite Transition Analysis

This run treats the rewrite itself as the transition from article ordering to derivation ordering. It asks what becomes visible after quantum pages are sorted by formal role.

## Summary

- `page_count`: `146`
- `constructed_pages`: `42`
- `evidence_placements`: `104`
- `mean_operation_gain`: `18.2505`
- `mean_object_shift`: `3.0861`

### Mean Route Profile

- state evolution / transport: `0.2318`
- normalization / admissibility: `0.1651`
- operator-to-spectrum readout: `0.3284`
- context / boundary realization: `0.0947`
- compatibility / non-commutation: `0.0865`
- protocol / engineered sequence: `0.0756`

## Consequences For The Quantum Presentation

### Derivation order

The domain or Hilbert space precedes the state; the state precedes the generator or measurement map; the spectrum and probability rule precede interpretation. This order keeps particles, protocols, and interpretations downstream of the formal construction they use.

**Required evidence.** A page needs local equations or a clear route placement showing which formal role is being used.

### Pages that need explicit equations

The 42 topic-specific pages already supply local equation skeletons. The 104 core-derived pages mark topics where the book can state the expected quantum ingredients, but still needs a page-native state, operator or map, spectrum or readout, compatibility condition, and realization.

**Required evidence.** Clean equation witnesses and page-local role rows linked to the source text.

### Role-based topic comparison

Two topics can be compared when they preserve the same state-operator-readout pattern, even if their historical names differ. A valid comparison should keep track of the Hilbert space or domain, operator class, spectrum, probability rule, and compatibility condition.

**Required evidence.** Route profiles, equation witnesses, and a check that the compared topics share the relevant formal roles.

### Mixed-role topics

Pages such as EPR, the measurement problem, quantum gravity, and quantum biology combine compatibility, boundary, protocol, and transport roles. They require decomposition into separate formal questions before they can be presented as derivations.

**Required evidence.** Targeted source-equation checks for each role claimed on the page.

### Interpretation layer

Interpretive pages change the status assigned to state vectors, probabilities, updates, observers, or recorded outcomes. They do not by themselves replace the Hamiltonian, operator algebra, spectral decomposition, or Born-rule assignment.

**Required evidence.** Explicit separation between formal equations and claims about state, probability, update, or ontology.

## New Information Produced By The Rewrite

### 1. The rewrite converts a noun-indexed encyclopedia into a derivation graph.

The new object is not a better summary of each topic; it is an ordering relation: which topic plays context, state, generator, observable, readout, compatibility, boundary, field, protocol, or annotation.

Evidence:
- `page_count`: `146`
- `branch_counts`: `{'states': 16, 'measurement': 16, 'boundaries': 10, 'fields': 25, 'protocols': 25, 'annotations': 17, 'observables': 11, 'generators': 16, 'context': 7, 'incompatibility': 3}`
- `constructed_pages`: `42`
- `evidence_placements`: `104`

### 2. The dominant stable role is operator-to-spectrum readout, not object naming.

The rewrite makes explicit that many named quantum topics become different ways of asking a legal spectral question of a state.

Evidence:
- `spectral_operator_mean`: `0.3284`
- `transport_mean`: `0.2318`
- `closure_mean`: `0.1651`

### 3. Particles become stable role-realizations inside field/mode/readout machinery.

The particle pages are not discarded; they are relocated as field/mode/statistics/readout constructions. This is a more precise statement than 'particles are not fundamental'.

Evidence:
- `particle_like_pages`: Quantum field theory; Wave–particle duality; Particle in a box; Electron microscope; History of quantum field theory; Fock space; Photon; Electron; Boson; Fermion
- `field_branch_count`: `25`

### 4. Interpretations mostly act on state, probability, and update semantics.

QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.

Evidence:
- `interpretation_like_pages`: Quantum Theory: Concepts and Methods; Quantum mind; Erwin Schrödinger; QBism; Quantum mysticism; Applications of quantum mechanics; History of quantum mechanics; Interpretations of quantum mechanics; David Hilbert; Modern Quantum Mechanics; Introduction to quantum mechanics; Werner Heisenberg
- `annotation_count`: `17`

### 5. Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.

Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.

Evidence:
- `boundary_count`: `10`
- `boundary_pages`: Scattering; Particle in a box; Quantum tunnelling; Quantum metamaterial; Potential well; Quantum harmonic oscillator; Quantum optics; Wave interference; Spectral line; S-matrix

### 6. Protocol pages compose state preparation, maps, and readouts.

Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.

Evidence:
- `protocol_count`: `25`
- `protocol_pages`: Quantum simulator; Quantum cellular automaton; Quantum computing; Quantum circuit; Quantum finite automaton; Quantum programming; Quantum channel; Quantum neural network; Quantum machine learning; Quantum complexity theory; Quantum metrology; Quantum engineering
- `protocol_route_mean`: `0.0756`

### 7. Anomalies identify where several formal roles coincide.

EPR, the measurement problem, quantum gravity, quantum biology, and related pages combine several formal questions in one topic: state preparation, compatibility, boundary or environmental coupling, protocol order, and readout.

Evidence:
- `top_anomalies`: {'title': 'Einstein–Podolsky–Rosen paradox', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 3.1933, 'explanation': 'EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails.', 'routes': {'boundary_weak_form_route': 0.1426, 'commutator_incompatibility_route': 0.1438, 'constraint_closure_route': 0.2059, 'discrete_protocol_route': 0.1094, 'spectral_operator_route': 0.1414, 'transport_flow_route': 0.2673}}; {'title': 'Quantum biology', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 3.1414, 'explanation': 'Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.', 'routes': {'boundary_weak_form_route': 0.1532, 'commutator_incompatibility_route': 0.1317, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.0802, 'spectral_operator_route': 0.1574, 'transport_flow_route': 0.2761}}; {'title': 'Measurement problem', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.9225, 'explanation': 'The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning.', 'routes': {'boundary_weak_form_route': 0.2021, 'commutator_incompatibility_route': 0.0581, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1478, 'spectral_operator_route': 0.1374, 'transport_flow_route': 0.2689}}; {'title': 'Quantum gravity', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8955, 'explanation': 'Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.', 'routes': {'boundary_weak_form_route': 0.1683, 'commutator_incompatibility_route': 0.0505, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1554, 'spectral_operator_route': 0.2006, 'transport_flow_route': 0.2689}}; {'title': 'Scattering', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8943, 'explanation': 'Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.', 'routes': {'boundary_weak_form_route': 0.161, 'commutator_incompatibility_route': 0.061, 'constraint_closure_route': 0.2083, 'discrete_protocol_route': 0.1568, 'spectral_operator_route': 0.204, 'transport_flow_route': 0.2673}}; {'title': "Schrödinger's cat", 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.", 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Wave–particle duality', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': 'Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Quantum state', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': 'Quantum state is the carrier rather than the final prediction. It precedes admissibility, evolution, observable choice, and probability readout. The unresolved distinction is whether the carrier is a vector, density operator, field state, or register, and which transformations preserve it.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}

## Sparse Transition Hotspots

- **Quantum biology** (states): attention `0.53743`, operation gain `19.8768`, top roles state=0.30, context=0.18, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.
- **Measurement problem** (measurement): attention `0.522305`, operation gain `20.4493`, top roles measurement=0.32, state=0.17, context=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning.
- **Einstein–Podolsky–Rosen paradox** (measurement): attention `0.509067`, operation gain `22.3157`, top roles measurement=0.33, state=0.24, observable=0.14; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails.
- **Schrödinger's cat** (states): attention `0.500347`, operation gain `22.6986`, top roles state=0.27, context=0.18, measurement=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.
- **Scattering** (boundaries): attention `0.493152`, operation gain `22.1729`, top roles boundary=0.25, context=0.21, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.
- **Macroscopic quantum phenomena** (states): attention `0.493108`, operation gain `19.6078`, top roles state=0.30, context=0.18, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: This state page mixes state evolution, preparation and boundary context, and normalization and admissibility. The relevant fields are the state carrier, representation, evolution, admissibility, and later readout.
- **Quantum gravity** (fields): attention `0.493038`, operation gain `18.3113`, top roles context=0.22, state=0.19, observable=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.
- **Bell's theorem** (measurement): attention `0.485195`, operation gain `18.6111`, top roles measurement=0.21, context=0.19, state=0.18; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This measurement page mixes observables and spectra, state evolution, and normalization and admissibility. Separate the state before readout, the detector or measurement map, the recorded outcome, and the update or conditioning rule.
- **Quantum simulator** (protocols): attention `0.483002`, operation gain `15.7216`, top roles context=0.21, state=0.20, observable=0.18; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: A quantum simulator is an engineered realization of another Hamiltonian or channel. It is both an observable system and a protocol for representing a target system. The formal fields are the simulated target, physical carrier, encoding map, and validation observable.
- **Delayed-choice quantum eraser** (measurement): attention `0.482107`, operation gain `21.3033`, top roles measurement=0.29, state=0.23, observable=0.15; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.
- **Quantum Theory: Concepts and Methods** (annotations): attention `0.477394`, operation gain `25.3233`, top roles measurement=0.28, context=0.17, state=0.17
- **Quantum nonlocality** (measurement): attention `0.469639`, operation gain `21.349`, top roles measurement=0.30, state=0.21, context=0.15; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This measurement page mixes observables and spectra, state evolution, and controlled update protocol. Separate the state before readout, the detector or measurement map, the recorded outcome, and the update or conditioning rule.
- **Quantum field theory** (fields): attention `0.465803`, operation gain `17.4234`, top roles context=0.21, observable=0.19, state=0.15; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub, branch-ambiguous
  - Interpretation: This field-level page mixes observables and spectra, state evolution, and normalization and admissibility. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable.
- **Wave function** (states): attention `0.460403`, operation gain `16.4841`, top roles state=0.26, context=0.21, measurement=0.21; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. The formal decomposition separates representation, admissibility, evolution, and Born readout.
- **Wave–particle duality** (measurement): attention `0.456285`, operation gain `19.334`, top roles measurement=0.21, state=0.18, context=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel.
- **Quantum logic** (observables): attention `0.452456`, operation gain `22.6081`, top roles observable=0.28, context=0.20, measurement=0.19
- **Spin (physics)** (states): attention `0.44803`, operation gain `19.909`, top roles state=0.31, context=0.19, observable=0.17; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This state page mixes observables and spectra, state evolution, and normalization and admissibility. The relevant fields are the state carrier, representation, evolution, admissibility, and later readout.
- **Quantum electrodynamics** (fields): attention `0.44628`, operation gain `19.9115`, top roles context=0.22, state=0.20, observable=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub, branch-ambiguous
  - Interpretation: Quantum electrodynamics is a field-interaction construction. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. The relevant formal objects are field operators, gauge constraints, interaction terms, and observable amplitudes.
- **Quantum cellular automaton** (protocols): attention `0.445527`, operation gain `16.8662`, top roles state=0.23, context=0.19, measurement=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: A quantum cellular automaton is a locality-preserving update rule. The lattice, neighborhood rule, unitarity or channel condition, and update protocol define the mechanism together.
- **Fermi–Dirac statistics** (fields): attention `0.445198`, operation gain `14.8543`, top roles state=0.21, context=0.18, fields=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. The formal content is anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space.

## Branch-Level Transition

- **Fields, constraints, and scale**: `25` pages, `13` constructed, mean operation gain `15.195`.
- **Control sequences and quantum channels**: `25` pages, `3` constructed, mean operation gain `16.4046`.
- **Annotations: history, interpretations, and popular frames**: `17` pages, `0` constructed, mean operation gain `23.2335`.
- **Quantum states and subsystem structure**: `16` pages, `5` constructed, mean operation gain `16.9323`.
- **Measurement, instruments, and probabilities**: `16` pages, `6` constructed, mean operation gain `19.4596`.
- **Dynamics and transformations**: `16` pages, `6` constructed, mean operation gain `19.4076`.
- **Observables and spectra**: `11` pages, `2` constructed, mean operation gain `19.1545`.
- **Boundaries and operator domains**: `10` pages, `2` constructed, mean operation gain `21.0928`.
- **State space, domain, and representation**: `7` pages, `3` constructed, mean operation gain `17.812`.
- **Noncommuting observables**: `3` pages, `2` constructed, mean operation gain `13.5013`.

## Structural Conclusion

The transition map separates pages with local equation support from pages that still require local equations. It also identifies mixed-role pages and role-preserving comparisons across topics. The new information is structural: the topic encyclopedia becomes an ordered set of formal questions and unresolved derivations.
