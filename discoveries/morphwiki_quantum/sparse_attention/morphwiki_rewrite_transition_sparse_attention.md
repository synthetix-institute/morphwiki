# Quantum Rewrite Transition Analysis

This run treats the rewrite itself as the transition from article ordering to derivation ordering. It asks what becomes visible after quantum pages are sorted by formal role.

## Summary

- `page_count`: `147`
- `constructed_pages`: `145`
- `evidence_placements`: `2`
- `mean_operation_gain`: `21.9066`
- `mean_object_shift`: `3.6921`

### Mean Route Profile

- state evolution / transport: `0.2321`
- normalization / admissibility: `0.1646`
- operator-to-spectrum readout: `0.3272`
- context / boundary realization: `0.0943`
- compatibility / non-commutation: `0.0861`
- protocol / engineered sequence: `0.0753`

## Consequences For The Quantum Presentation

### Derivation order

The domain or Hilbert space precedes the state; the state precedes the generator or measurement map; the spectrum and probability rule precede interpretation. This order keeps particles, protocols, and interpretations downstream of the formal construction they use.

**Required evidence.** A page needs local equations or a clear route placement showing which formal role is being used.

### Pages that need explicit equations

The 145 topic-specific pages already supply local equation skeletons. The 2 core-derived pages mark topics where the book can state the expected quantum ingredients, but still needs a page-native state, operator or map, spectrum or readout, compatibility condition, and realization.

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
- `page_count`: `147`
- `branch_counts`: `{'generators': 22, 'states': 24, 'measurement': 10, 'annotations': 16, 'incompatibility': 6, 'boundaries': 12, 'fields': 21, 'protocols': 18, 'unresolved': 1, 'observables': 10, 'context': 7}`
- `constructed_pages`: `145`
- `evidence_placements`: `2`

### 2. The dominant stable role is operator-to-spectrum readout, not object naming.

The rewrite makes explicit that many named quantum topics become different ways of asking a legal spectral question of a state.

Evidence:
- `spectral_operator_mean`: `0.3272`
- `transport_mean`: `0.2321`
- `closure_mean`: `0.1646`

### 3. Particles become stable role-realizations inside field/mode/readout machinery.

The particle pages are not discarded; they are relocated as field/mode/statistics/readout constructions. This is a more precise statement than 'particles are not fundamental'.

Evidence:
- `particle_like_pages`: Wave–particle duality; Quantum field theory; Electron microscope; Particle in a box; Photon; Fock space; History of quantum field theory; Boson; Electron; Fermion
- `field_branch_count`: `21`

### 4. Interpretations mostly act on state, probability, and update semantics.

QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.

Evidence:
- `interpretation_like_pages`: Introduction to quantum mechanics; Quantum Theory: Concepts and Methods; Erwin Schrödinger; Quantum mind; Old quantum theory; QBism; History of quantum mechanics; David Hilbert; Interpretations of quantum mechanics; Quantum mysticism; Modern Quantum Mechanics; Relational quantum mechanics
- `annotation_count`: `16`

### 5. Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.

Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.

Evidence:
- `boundary_count`: `12`
- `boundary_pages`: Scattering; Potential well; Quantum tunnelling; Macroscopic quantum phenomena; Quantum metamaterial; Particle in a box; Quantum harmonic oscillator; Quantum optics; Quantum imaging; Wave interference; Spectral line; S-matrix

### 6. Protocol pages compose state preparation, maps, and readouts.

Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.

Evidence:
- `protocol_count`: `18`
- `protocol_pages`: Quantum computing; Quantum finite automaton; Quantum neural network; Quantum programming; Quantum image processing; Quantum key distribution; Quantum circuit; Quantum logic gate; Quantum information science; Quantum error correction; Quantum network; Quantum teleportation
- `protocol_route_mean`: `0.0753`

### 7. Anomalies identify where several formal roles coincide.

EPR, the measurement problem, quantum gravity, quantum biology, and related pages combine several formal questions in one topic: state preparation, compatibility, boundary or environmental coupling, protocol order, and readout.

Evidence:
- `top_anomalies`: {'title': "Schrödinger's cat", 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.", 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Einstein–Podolsky–Rosen paradox', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.8433, 'explanation': 'EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails.', 'routes': {'boundary_weak_form_route': 0.1426, 'commutator_incompatibility_route': 0.1438, 'constraint_closure_route': 0.2059, 'discrete_protocol_route': 0.1094, 'spectral_operator_route': 0.1414, 'transport_flow_route': 0.2673}}; {'title': 'Quantum biology', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.7914, 'explanation': 'Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.', 'routes': {'boundary_weak_form_route': 0.1532, 'commutator_incompatibility_route': 0.1317, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.0802, 'spectral_operator_route': 0.1574, 'transport_flow_route': 0.2761}}; {'title': 'Introduction to quantum mechanics', 'labels': ['weak spectral anchor', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.7614, 'explanation': 'An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Its technical content separates into individual branches before supporting specific derivations.', 'routes': {'boundary_weak_form_route': 0.0712, 'commutator_incompatibility_route': 0.1637, 'constraint_closure_route': 0.1928, 'discrete_protocol_route': 0.108, 'spectral_operator_route': 0.2882, 'transport_flow_route': 0.2575}}; {'title': 'Measurement problem', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5725, 'explanation': 'The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning.', 'routes': {'boundary_weak_form_route': 0.2021, 'commutator_incompatibility_route': 0.0581, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1478, 'spectral_operator_route': 0.1374, 'transport_flow_route': 0.2689}}; {'title': 'Quantum gravity', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5455, 'explanation': 'Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.', 'routes': {'boundary_weak_form_route': 0.1683, 'commutator_incompatibility_route': 0.0505, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1554, 'spectral_operator_route': 0.2006, 'transport_flow_route': 0.2689}}; {'title': 'Scattering', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5443, 'explanation': 'Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.', 'routes': {'boundary_weak_form_route': 0.161, 'commutator_incompatibility_route': 0.061, 'constraint_closure_route': 0.2083, 'discrete_protocol_route': 0.1568, 'spectral_operator_route': 0.204, 'transport_flow_route': 0.2673}}; {'title': 'Wave–particle duality', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5424, 'explanation': 'Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}

## Sparse Transition Hotspots

- **Quantum logic** (generators): attention `0.60207`, operation gain `26.0703`, top roles measurement=0.26, context=0.19, state=0.16; anomaly: compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This page sits between Generator: lawful change before readout and Annotations: history, interpretations, and popular frames. The ambiguity is useful: it marks a place where two formal roles meet and require separate treatment before the page supports a derivation.
- **Quantum biology** (generators): attention `0.558879`, operation gain `23.1188`, top roles context=0.19, observable=0.19, measurement=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. The formal fields are the state carrier, environmental coupling, coherence or transport observable, and classical control.
- **Schrödinger's cat** (states): attention `0.557218`, operation gain `26.0753`, top roles measurement=0.26, context=0.19, state=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.
- **Measurement problem** (measurement): attention `0.547564`, operation gain `26.699`, top roles measurement=0.31, context=0.18, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. The formal decomposition is pre-measurement evolution, apparatus or environment coupling, POVM or projection readout, and post-record conditioning.
- **Delayed-choice quantum eraser** (measurement): attention `0.54272`, operation gain `26.4579`, top roles measurement=0.26, context=0.18, state=0.17; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.
- **Introduction to quantum mechanics** (annotations): attention `0.54122`, operation gain `21.0158`, top roles measurement=0.21, context=0.21, state=0.19; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Its technical content separates into individual branches before supporting specific derivations.
- **Einstein–Podolsky–Rosen paradox** (incompatibility): attention `0.533816`, operation gain `24.236`, top roles measurement=0.26, context=0.18, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. The formal starting point is the joint state and local observables; the question is which correlation constraint fails.
- **Quantum nonlocality** (incompatibility): attention `0.524501`, operation gain `26.1315`, top roles measurement=0.27, context=0.18, state=0.16; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This incompatibility page mixes observables and spectra, state evolution, and controlled update protocol. State which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure.
- **Wave–particle duality** (states): attention `0.516754`, operation gain `24.069`, top roles context=0.19, observable=0.19, measurement=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Its compact form is context selection plus readout channel.
- **Scattering** (boundaries): attention `0.507467`, operation gain `23.2611`, top roles context=0.19, observable=0.17, measurement=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. The relevant objects are the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.
- **Quantum gravity** (fields): attention `0.50639`, operation gain `23.1227`, top roles observable=0.20, context=0.19, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing formal objects are a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.
- **Quantum simulator** (states): attention `0.495582`, operation gain `20.3307`, top roles context=0.20, measurement=0.20, state=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: A quantum simulator is an engineered realization of another Hamiltonian or channel. It is both an observable system and a protocol for representing a target system. The formal fields are the simulated target, physical carrier, encoding map, and validation observable.
- **Fermi–Dirac statistics** (fields): attention `0.4955`, operation gain `22.3848`, top roles context=0.20, measurement=0.19, state=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. The formal content is anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space.
- **Quantum Theory: Concepts and Methods** (annotations): attention `0.47547`, operation gain `25.1035`, top roles measurement=0.28, context=0.18, state=0.16
- **Spin (physics)** (states): attention `0.475368`, operation gain `21.9928`, top roles context=0.21, measurement=0.20, state=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This state page mixes observables and spectra, state evolution, and normalization and admissibility. The relevant fields are the state carrier, representation, evolution, admissibility, and later readout.
- **Quantum computing** (protocols): attention `0.471254`, operation gain `21.3442`, top roles context=0.20, measurement=0.20, state=0.18; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This protocol page mixes observables and spectra, state evolution, and controlled update protocol. Its formal content is an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters.
- **Quantum electrodynamics** (fields): attention `0.470158`, operation gain `21.6022`, top roles measurement=0.22, context=0.20, observable=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: Quantum electrodynamics is a field-interaction construction. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. The relevant formal objects are field operators, gauge constraints, interaction terms, and observable amplitudes.
- **Wave function** (states): attention `0.470084`, operation gain `20.6938`, top roles state=0.27, measurement=0.22, context=0.20; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. The formal decomposition separates representation, admissibility, evolution, and Born readout.
- **Quantum cosmology** (unresolved): attention `0.46302`, operation gain `30.7692`, top roles state=0.25, observable=0.23, measurement=0.16
- **Quantum field theory** (fields): attention `0.457392`, operation gain `20.2775`, top roles context=0.20, measurement=0.17, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: This field-level page mixes observables and spectra, state evolution, and normalization and admissibility. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable.

## Branch-Level Transition

- **State carrier inside Hilbert space**: `24` pages, `24` constructed, mean operation gain `21.1184`.
- **Generator: lawful change before readout**: `22` pages, `22` constructed, mean operation gain `22.4482`.
- **Many-mode extension: fields, particles, and scaling**: `21` pages, `21` constructed, mean operation gain `21.4452`.
- **Protocol layer: engineered transformations**: `18` pages, `18` constructed, mean operation gain `20.7947`.
- **Annotations: history, interpretations, and popular frames**: `16` pages, `16` constructed, mean operation gain `23.1262`.
- **Boundary realization: how effects appear**: `12` pages, `12` constructed, mean operation gain `22.3313`.
- **Readout rule: how answers become probabilities**: `10` pages, `10` constructed, mean operation gain `22.7315`.
- **Spectral question: what can be asked**: `10` pages, `9` constructed, mean operation gain `21.342`.
- **Hilbert-space context: admissible carrier and basis**: `7` pages, `7` constructed, mean operation gain `22.5403`.
- **Compatibility limit: what cannot be jointly sharp**: `6` pages, `6` constructed, mean operation gain `21.2721`.
- **Unresolved**: `1` pages, `0` constructed, mean operation gain `30.7692`.

## Structural Conclusion

The transition map separates pages with local equation support from pages that still require local equations. It also identifies mixed-role pages and role-preserving comparisons across topics. The new information is structural: the topic encyclopedia becomes an ordered set of formal questions and unresolved derivations.
