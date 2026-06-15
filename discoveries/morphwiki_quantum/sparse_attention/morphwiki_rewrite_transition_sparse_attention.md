# MorphWiki Rewrite Transition Sparse Attention

This run treats the rewrite itself as the transition: Wikipedia/topic view -> mechanism-tree view. It asks what becomes visible only after quantum pages are reorganized by constructor role.

## Summary

- `page_count`: `147`
- `constructed_pages`: `145`
- `evidence_placements`: `2`
- `mean_operation_gain`: `22.0487`
- `mean_object_shift`: `3.899`

### Mean Route Profile

- state evolution / transport: `0.2321`
- normalization / admissibility: `0.1646`
- operator-to-spectrum readout: `0.3272`
- context / boundary realization: `0.0943`
- compatibility / non-commutation: `0.0861`
- protocol / engineered sequence: `0.0753`

## What Can Be Done With This Structure

### Teach quantum theory as a derivation tree.

The reader sees the required assembly order: context, state, generator, observable spectrum, probability readout, compatibility limit, and realization. This avoids presenting interpretations, particles, and protocols as equal primitives.

**Required evidence.** Topic pages must have either constructed equations or route/fiber placements with clear branch assignment.

### Build constructor targets for the decoder.

The 145 constructed pages are seed targets. The 2 evidence placements become a supervised specialization set: each needs a topic-native state, operator/map, spectrum/readout, compatibility condition, and realization.

**Required evidence.** Clean equation witnesses and constructor-target rows extracted from Hyperion fingerprints.

### Find transfer candidates across fields.

A page can be transferred only if the role survives. This lets FieldBridge search for analogues of a mechanism rather than semantic analogues of words.

**Required evidence.** Route/fiber profiles plus field-specific receptors and falsification tests.

### Use anomalies as research prompts.

Multi-role pages such as EPR, measurement problem, quantum gravity, and quantum biology are not clean branches. They mark places where compatibility, boundary, protocol, and transport signals collide.

**Required evidence.** Dedicated reruns with targeted topic sets and arXiv witness audits.

### Separate interpretation from machinery.

Interpretive pages can be retained as readout/probability annotations without allowing them to rewrite the Hamiltonian/operator/spectral core.

**Required evidence.** Explicit distinction between formal equations and semantic claims about state/probability/update.

## New Information Produced By The Rewrite

### 1. The rewrite converts a noun-indexed encyclopedia into a derivation graph.

The new object is not a better summary of each topic; it is an ordering relation: which topic plays context, state, generator, observable, readout, compatibility, boundary, field, protocol, or annotation.

Evidence:
- `page_count`: `147`
- `branch_counts`: `{'generators': 22, 'measurement': 10, 'states': 24, 'annotations': 16, 'boundaries': 12, 'incompatibility': 6, 'fields': 22, 'context': 7, 'protocols': 18, 'observables': 10}`
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
- `particle_like_pages`: Wave–particle duality; Quantum field theory; Particle in a box; Photon; Fock space; Electron microscope; Boson; Fermion; Electron; History of quantum field theory
- `field_branch_count`: `22`

### 4. Interpretations mostly act on readout semantics rather than replacing the formal constructor.

QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.

Evidence:
- `interpretation_like_pages`: Introduction to quantum mechanics; Quantum Theory: Concepts and Methods; Erwin Schrödinger; Old quantum theory; David Hilbert; QBism; Quantum mind; History of quantum mechanics; Modern Quantum Mechanics; Interpretations of quantum mechanics; Quantum mysticism; Introduction to Quantum Mechanics (book)
- `annotation_count`: `16`

### 5. Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.

Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.

Evidence:
- `boundary_count`: `12`
- `boundary_pages`: Scattering; Quantum metamaterial; Potential well; Particle in a box; Macroscopic quantum phenomena; Quantum tunnelling; Quantum harmonic oscillator; Quantum optics; Quantum imaging; Wave interference; Spectral line; S-matrix

### 6. Protocol pages are an engineering layer over the constructor, not the root of the theory.

Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.

Evidence:
- `protocol_count`: `18`
- `protocol_pages`: Quantum computing; Quantum finite automaton; Quantum programming; Quantum neural network; Quantum circuit; Quantum image processing; Quantum key distribution; Quantum channel; Quantum logic gate; Quantum bus; Quantum error correction; Quantum information science
- `protocol_route_mean`: `0.0753`

### 7. Anomalies identify where several constructor roles collide.

Anomalies are not errors in the tree. They are research handles: EPR, measurement problem, quantum gravity, quantum biology, and related pages require several roles at once.

Evidence:
- `top_anomalies`: {'title': "Schrödinger's cat", 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.", 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Einstein–Podolsky–Rosen paradox', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.8433, 'explanation': 'EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails.', 'routes': {'boundary_weak_form_route': 0.1426, 'commutator_incompatibility_route': 0.1438, 'constraint_closure_route': 0.2059, 'discrete_protocol_route': 0.1094, 'spectral_operator_route': 0.1414, 'transport_flow_route': 0.2673}}; {'title': 'Quantum biology', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.7914, 'explanation': 'Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control.', 'routes': {'boundary_weak_form_route': 0.1532, 'commutator_incompatibility_route': 0.1317, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.0802, 'spectral_operator_route': 0.1574, 'transport_flow_route': 0.2761}}; {'title': 'Introduction to quantum mechanics', 'labels': ['weak spectral anchor', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.7614, 'explanation': 'An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims.', 'routes': {'boundary_weak_form_route': 0.0712, 'commutator_incompatibility_route': 0.1637, 'constraint_closure_route': 0.1928, 'discrete_protocol_route': 0.108, 'spectral_operator_route': 0.2882, 'transport_flow_route': 0.2575}}; {'title': 'Measurement problem', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5725, 'explanation': 'The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning.', 'routes': {'boundary_weak_form_route': 0.2021, 'commutator_incompatibility_route': 0.0581, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1478, 'spectral_operator_route': 0.1374, 'transport_flow_route': 0.2689}}; {'title': 'Quantum gravity', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5455, 'explanation': 'Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.', 'routes': {'boundary_weak_form_route': 0.1683, 'commutator_incompatibility_route': 0.0505, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1554, 'spectral_operator_route': 0.2006, 'transport_flow_route': 0.2689}}; {'title': 'Scattering', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5443, 'explanation': 'Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.', 'routes': {'boundary_weak_form_route': 0.161, 'commutator_incompatibility_route': 0.061, 'constraint_closure_route': 0.2083, 'discrete_protocol_route': 0.1568, 'spectral_operator_route': 0.204, 'transport_flow_route': 0.2673}}; {'title': 'Wave–particle duality', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5424, 'explanation': 'Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}

## Sparse Transition Hotspots

- **Quantum logic** (generators): attention `0.613832`, operation gain `24.2629`, top roles measurement=0.23, context=0.20, state=0.17; anomaly: compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This page sits between Generator: lawful change before readout and Annotations: history, interpretations, and popular frames. The ambiguity is useful: it marks a place where two constructor roles meet and should be separated before the page is used as a derivation.
- **Measurement problem** (measurement): attention `0.600635`, operation gain `27.6074`, top roles measurement=0.30, context=0.19, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning.
- **Quantum biology** (generators): attention `0.594145`, operation gain `22.9029`, top roles context=0.20, state=0.18, measurement=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control.
- **Schrödinger's cat** (states): attention `0.593268`, operation gain `25.7177`, top roles state=0.22, measurement=0.22, context=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.
- **Introduction to quantum mechanics** (annotations): attention `0.580124`, operation gain `21.3514`, top roles context=0.22, measurement=0.22, state=0.19; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims.
- **Delayed-choice quantum eraser** (measurement): attention `0.578219`, operation gain `26.0098`, top roles measurement=0.25, context=0.19, state=0.18; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.
- **Scattering** (boundaries): attention `0.56782`, operation gain `25.1659`, top roles context=0.20, observable=0.16, state=0.15; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.
- **Einstein–Podolsky–Rosen paradox** (incompatibility): attention `0.551351`, operation gain `22.6438`, top roles measurement=0.23, context=0.20, state=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails.
- **Quantum simulator** (states): attention `0.540834`, operation gain `20.9924`, top roles state=0.23, context=0.20, measurement=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: A quantum simulator is an engineered realization of another Hamiltonian or channel. It is both an observable system and a protocol for representing a target system. Name the simulated target, physical carrier, encoding map, and validation observable.
- **Wave–particle duality** (states): attention `0.538443`, operation gain `22.8249`, top roles context=0.19, state=0.19, observable=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel.
- **Fermi–Dirac statistics** (fields): attention `0.537482`, operation gain `22.9482`, top roles context=0.22, measurement=0.18, state=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. Expose anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space.
- **Quantum nonlocality** (incompatibility): attention `0.535175`, operation gain `23.7654`, top roles measurement=0.24, context=0.21, state=0.15; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This incompatibility page mixes observables and spectra, state evolution, and controlled update protocol. State which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure.
- **Quantum gravity** (fields): attention `0.533536`, operation gain `22.4252`, top roles context=0.22, observable=0.18, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.
- **Wave function** (states): attention `0.52176`, operation gain `22.2294`, top roles measurement=0.22, context=0.22, state=0.22; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. Separate representation, admissibility, evolution, and Born readout.
- **Quantum field theory** (fields): attention `0.52001`, operation gain `22.7273`, top roles context=0.21, measurement=0.19, observable=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: This field-level page mixes observables and spectra, state evolution, and normalization and admissibility. Treat it as a many-mode or geometric realization problem: identify the state sector or field algebra, then the constraints and readout that make the field content observable.
- **Quantum entanglement** (incompatibility): attention `0.519704`, operation gain `21.4293`, top roles measurement=0.22, context=0.20, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. Separate the joint state, subsystem observables, and correlation test.
- **Bell's theorem** (incompatibility): attention `0.512008`, operation gain `21.816`, top roles context=0.22, measurement=0.20, state=0.17; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This incompatibility page mixes observables and spectra, state evolution, and normalization and admissibility. State which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure.
- **Spin (physics)** (states): attention `0.511046`, operation gain `22.107`, top roles state=0.23, context=0.21, measurement=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This state page mixes observables and spectra, state evolution, and normalization and admissibility. Specify the state carrier, then distinguish representation, evolution, admissibility, and later readout.
- **Quantum electrodynamics** (fields): attention `0.51018`, operation gain `22.107`, top roles context=0.21, measurement=0.20, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: Quantum electrodynamics is a field-interaction constructor. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. Derive it through field operators, gauge constraints, interaction terms, and observable amplitudes.
- **Relativistic quantum mechanics** (context): attention `0.506371`, operation gain `21.5299`, top roles context=0.27, measurement=0.19, state=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, multi-role hub, branch-ambiguous
  - Interpretation: Relativistic quantum mechanics is a compatibility junction between quantum state evolution and spacetime symmetry. It must preserve relativistic covariance, define the correct state carrier, and explain how spin, energy, and causality constraints enter the operator algebra.

## Branch-Level Transition

- **State carrier inside Hilbert space**: `24` pages, `24` constructed, mean operation gain `21.3747`.
- **Generator: lawful change before readout**: `22` pages, `22` constructed, mean operation gain `21.8136`.
- **Many-mode extension: fields, particles, and scaling**: `22` pages, `21` constructed, mean operation gain `22.0176`.
- **Protocol layer: engineered transformations**: `18` pages, `18` constructed, mean operation gain `21.1423`.
- **Annotations: history, interpretations, and popular frames**: `16` pages, `16` constructed, mean operation gain `22.7054`.
- **Boundary realization: how effects appear**: `12` pages, `12` constructed, mean operation gain `23.5914`.
- **Readout rule: how answers become probabilities**: `10` pages, `10` constructed, mean operation gain `23.3299`.
- **Spectral question: what can be asked**: `10` pages, `9` constructed, mean operation gain `20.8714`.
- **Hilbert-space context: admissible carrier and basis**: `7` pages, `7` constructed, mean operation gain `23.2121`.
- **Compatibility limit: what cannot be jointly sharp**: `6` pages, `6` constructed, mean operation gain `22.0729`.

## Practical Conclusion

The useful object is the transition map, not the prose rewrite alone. It tells us which named topics are already constructible, which are only placed by evidence, which pages are multi-role junctions, and which parts of quantum theory are transferable as mechanisms. The new information is therefore structural: a topic encyclopedia becomes a queue of constructor roles and unresolved derivations.
