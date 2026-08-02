# Quantum Rewrite Transition Analysis

This run treats the rewrite itself as the transition from article ordering to derivation ordering. It asks what becomes visible after quantum pages are sorted by formal role.

## Summary

- `page_count`: `146`
- `constructed_pages`: `39`
- `evidence_placements`: `107`
- `mean_operation_gain`: `17.3198`
- `mean_object_shift`: `2.9514`

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

The 39 topic-specific pages already supply local equation skeletons. The 107 core-derived pages mark topics where the book can state the expected quantum ingredients, but still needs a page-native state, operator or map, spectrum or readout, compatibility condition, and realization.

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
- `branch_counts`: `{'measurement': 9, 'states': 14, 'generators': 21, 'fields': 25, 'boundaries': 12, 'annotations': 17, 'incompatibility': 7, 'context': 8, 'protocols': 23, 'observables': 10}`
- `constructed_pages`: `39`
- `evidence_placements`: `107`

### 2. The dominant stable role is operator-to-spectrum readout, not object naming.

The rewrite makes explicit that many named quantum topics become different ways of asking a legal spectral question of a state.

Evidence:
- `spectral_operator_mean`: `0.3284`
- `transport_mean`: `0.2318`
- `closure_mean`: `0.1651`

### 3. Particles become stable role-realizations inside field/mode/readout machinery.

The particle pages are not discarded; they are relocated as field/mode/statistics/readout constructions. This is a more precise statement than 'particles are not fundamental'.

Evidence:
- `particle_like_pages`: Electron; Particle in a box; Photon; Wave–particle duality; Fock space; Quantum field theory; Fermion; Boson; Electron microscope; History of quantum field theory
- `field_branch_count`: `25`

### 4. Interpretations mostly act on state, probability, and update semantics.

QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.

Evidence:
- `interpretation_like_pages`: Introduction to quantum mechanics; Quantum Theory: Concepts and Methods; David Hilbert; Quantum mysticism; History of quantum mechanics; Applications of quantum mechanics; Quantum mind; Erwin Schrödinger; Werner Heisenberg; Modern Quantum Mechanics; Interpretations of quantum mechanics; QBism
- `annotation_count`: `17`

### 5. Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.

Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.

Evidence:
- `boundary_count`: `12`
- `boundary_pages`: Macroscopic quantum phenomena; Scattering; Quantum tunnelling; Potential well; Particle in a box; Quantum metamaterial; Quantum harmonic oscillator; Quantum optics; S-matrix; Wave interference; Spectral line; Quantum imaging

### 6. Protocol pages compose state preparation, maps, and readouts.

Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.

Evidence:
- `protocol_count`: `23`
- `protocol_pages`: Quantum computing; Quantum circuit; Quantum channel; Quantum finite automaton; Quantum programming; Quantum machine learning; Quantum neural network; Quantum image processing; Quantum complexity theory; Quantum engineering; Quantum metrology; Quantum logic gate
- `protocol_route_mean`: `0.0756`

### 7. Anomalies identify where several formal roles coincide.

EPR, the measurement problem, quantum gravity, quantum biology, and related pages combine several formal questions in one topic: state preparation, compatibility, boundary or environmental coupling, protocol order, and readout.

Evidence:
- `top_anomalies`: {'title': 'Einstein–Podolsky–Rosen paradox', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 3.1933, 'explanation': 'EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails.', 'routes': {'boundary_weak_form_route': 0.1426, 'commutator_incompatibility_route': 0.1438, 'constraint_closure_route': 0.2059, 'discrete_protocol_route': 0.1094, 'spectral_operator_route': 0.1414, 'transport_flow_route': 0.2673}}; {'title': 'Quantum gravity', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8955, 'explanation': 'Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.', 'routes': {'boundary_weak_form_route': 0.1683, 'commutator_incompatibility_route': 0.0505, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1554, 'spectral_operator_route': 0.2006, 'transport_flow_route': 0.2689}}; {'title': "Schrödinger's cat", 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.", 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Wave–particle duality', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': 'Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Quantum state', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': 'Quantum state is the carrier rather than the final prediction. It precedes admissibility, evolution, observable choice, and probability readout. The unresolved distinction is whether the carrier is a vector, density operator, field state, or register, and which transformations preserve it.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Quantum biology', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.7914, 'explanation': 'Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.', 'routes': {'boundary_weak_form_route': 0.1532, 'commutator_incompatibility_route': 0.1317, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.0802, 'spectral_operator_route': 0.1574, 'transport_flow_route': 0.2761}}; {'title': 'Delayed-choice quantum eraser', 'labels': ['weak spectral anchor', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.7627, 'explanation': 'The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.', 'routes': {'boundary_weak_form_route': 0.1331, 'commutator_incompatibility_route': 0.1562, 'constraint_closure_route': 0.1796, 'discrete_protocol_route': 0.1081, 'spectral_operator_route': 0.2934, 'transport_flow_route': 0.2313}}; {'title': 'Introduction to quantum mechanics', 'labels': ['weak spectral anchor', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.7614, 'explanation': 'An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Its technical content separates into individual branches before supporting specific derivations.', 'routes': {'boundary_weak_form_route': 0.0712, 'commutator_incompatibility_route': 0.1637, 'constraint_closure_route': 0.1928, 'discrete_protocol_route': 0.108, 'spectral_operator_route': 0.2882, 'transport_flow_route': 0.2575}}

## Sparse Transition Hotspots

- **Measurement problem** (measurement): attention `0.556991`, operation gain `20.2546`, top roles measurement=0.30, context=0.17, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning.
- **Schrödinger's cat** (states): attention `0.539395`, operation gain `21.3582`, top roles state=0.27, context=0.19, measurement=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.
- **Quantum biology** (generators): attention `0.535596`, operation gain `18.2403`, top roles state=0.24, context=0.17, generator=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.
- **Quantum gravity** (fields): attention `0.532199`, operation gain `17.7165`, top roles context=0.21, observable=0.20, state=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.
- **Macroscopic quantum phenomena** (boundaries): attention `0.530902`, operation gain `19.9591`, top roles state=0.20, context=0.19, observable=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: This boundary page mixes state evolution, preparation and boundary context, and normalization and admissibility. Read it as a change in domain, interface, potential, or asymptotic channel that changes the allowed readout.
- **Scattering** (boundaries): attention `0.522722`, operation gain `21.3632`, top roles boundary=0.27, context=0.21, observable=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.
- **Introduction to quantum mechanics** (annotations): attention `0.504684`, operation gain `16.5746`, top roles context=0.21, measurement=0.21, state=0.19; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Its technical content separates into individual branches before supporting specific derivations.
- **Delayed-choice quantum eraser** (measurement): attention `0.499866`, operation gain `18.8457`, top roles measurement=0.26, state=0.22, observable=0.18; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.
- **Fermi–Dirac statistics** (fields): attention `0.499461`, operation gain `20.02`, top roles state=0.21, context=0.19, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. The formal content is anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space.
- **Quantum spacetime** (fields): attention `0.497559`, operation gain `17.9474`, top roles context=0.22, state=0.19, observable=0.19; anomaly: weak spectral anchor, compatibility/closure junction, multi-role hub, branch-ambiguous
  - Interpretation: This field-level page mixes incompatible questions, state evolution, and normalization and admissibility. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable.
- **Quantum geometry** (fields): attention `0.493532`, operation gain `19.1327`, top roles observable=0.25, context=0.19, state=0.16
- **Wave function** (states): attention `0.491968`, operation gain `16.7585`, top roles state=0.29, context=0.19, measurement=0.19; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. The formal decomposition separates representation, admissibility, evolution, and Born readout.
- **Quantum electrodynamics** (fields): attention `0.489447`, operation gain `20.3459`, top roles state=0.20, context=0.19, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: Quantum electrodynamics is a field-interaction construction. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. The relevant formal objects are field operators, gauge constraints, interaction terms, and observable amplitudes.
- **Quantum Theory: Concepts and Methods** (annotations): attention `0.486368`, operation gain `21.6998`, top roles measurement=0.27, context=0.17, state=0.17
- **Electron** (fields): attention `0.478715`, operation gain `16.4103`, top roles context=0.21, observable=0.17, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: This field-level page mixes observables and spectra, preparation and boundary context, and state evolution. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable.
- **Quantum tunnelling** (boundaries): attention `0.473367`, operation gain `20.1571`, top roles context=0.21, boundary=0.21, observable=0.19
- **Quantum entanglement** (incompatibility): attention `0.469585`, operation gain `14.8571`, top roles context=0.19, state=0.19, measurement=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. The required distinction is between joint state, subsystem observables, and correlation test.
- **Quantum logic** (generators): attention `0.462093`, operation gain `20.2864`, top roles state=0.22, measurement=0.19, context=0.17
- **Schrödinger picture** (generators): attention `0.461449`, operation gain `18.2772`, top roles generator=0.21, state=0.19, context=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: This page sits between Generator: lawful change before measurement and Formal context: carrier, domain, and representation. The ambiguity is useful: it marks a place where two formal roles meet and require separate treatment before the page supports a derivation.
- **Heisenberg group** (generators): attention `0.461143`, operation gain `20.4258`, top roles state=0.21, context=0.18, generator=0.18

## Branch-Level Transition

- **Many-mode extension: fields, particles, and scaling**: `25` pages, `11` constructed, mean operation gain `17.6192`.
- **Protocol layer: engineered transformations**: `23` pages, `2` constructed, mean operation gain `15.1551`.
- **Generator: lawful change before measurement**: `21` pages, `7` constructed, mean operation gain `18.4622`.
- **Annotations: history, interpretations, and popular frames**: `17` pages, `0` constructed, mean operation gain `18.9022`.
- **State carrier inside Hilbert space**: `14` pages, `4` constructed, mean operation gain `17.2124`.
- **Boundary realization: how effects appear**: `12` pages, `2` constructed, mean operation gain `19.968`.
- **Spectral question: what can be asked**: `10` pages, `2` constructed, mean operation gain `15.8494`.
- **Measurement rule: how observables become probabilities**: `9` pages, `5` constructed, mean operation gain `17.116`.
- **Formal context: carrier, domain, and representation**: `8` pages, `2` constructed, mean operation gain `16.1354`.
- **Compatibility limit: what cannot be jointly sharp**: `7` pages, `4` constructed, mean operation gain `15.4839`.

## Structural Conclusion

The transition map separates pages with local equation support from pages that still require local equations. It also identifies mixed-role pages and role-preserving comparisons across topics. The new information is structural: the topic encyclopedia becomes an ordered set of formal questions and unresolved derivations.
