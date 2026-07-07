# MorphWiki Rewrite Transition Sparse Attention

This run treats the rewrite itself as the transition: Wikipedia/topic view -> mechanism-tree view. It asks what becomes visible only after quantum pages are reorganized by constructor role.

## Summary

- `page_count`: `147`
- `constructed_pages`: `145`
- `evidence_placements`: `2`
- `mean_operation_gain`: `22.0967`
- `mean_object_shift`: `3.6544`

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
- `branch_counts`: `{'generators': 22, 'states': 24, 'measurement': 10, 'annotations': 16, 'incompatibility': 6, 'boundaries': 12, 'fields': 21, 'protocols': 18, 'unresolved': 1, 'context': 7, 'observables': 10}`
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
- `particle_like_pages`: Wave–particle duality; Quantum field theory; Electron microscope; Particle in a box; Photon; Fock space; History of quantum field theory; Boson; Fermion; Electron
- `field_branch_count`: `21`

### 4. Interpretations mostly act on readout semantics rather than replacing the formal constructor.

QBism, relational quantum mechanics, collapse language, and popular frames can be kept without letting them become false roots of the derivation tree.

Evidence:
- `interpretation_like_pages`: Introduction to quantum mechanics; Quantum Theory: Concepts and Methods; Erwin Schrödinger; Quantum mind; Old quantum theory; QBism; History of quantum mechanics; David Hilbert; Interpretations of quantum mechanics; Quantum mysticism; Modern Quantum Mechanics; Introduction to Quantum Mechanics (book)
- `annotation_count`: `16`

### 5. Boundary pages are realization gates: they change allowed spectra without changing the core prediction problem.

Tunnelling, particle-in-a-box, scattering, cavities, and spectral lines become one family: boundary-shaped spectra.

Evidence:
- `boundary_count`: `12`
- `boundary_pages`: Scattering; Potential well; Macroscopic quantum phenomena; Quantum tunnelling; Quantum metamaterial; Particle in a box; Quantum harmonic oscillator; Quantum optics; Quantum imaging; Wave interference; Spectral line; S-matrix

### 6. Protocol pages are an engineering layer over the constructor, not the root of the theory.

Quantum computing is reorganized as controlled composition of states, operators, readouts, and error constraints rather than a separate ontology of qubits.

Evidence:
- `protocol_count`: `18`
- `protocol_pages`: Quantum computing; Quantum finite automaton; Quantum neural network; Quantum programming; Quantum image processing; Quantum key distribution; Quantum circuit; Quantum logic gate; Quantum information science; Quantum error correction; Quantum network; Quantum teleportation
- `protocol_route_mean`: `0.0753`

### 7. Anomalies identify where several constructor roles collide.

Anomalies are not errors in the tree. They are research handles: EPR, measurement problem, quantum gravity, quantum biology, and related pages require several roles at once.

Evidence:
- `top_anomalies`: {'title': "Schrödinger's cat", 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.8924, 'explanation': "Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.", 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}; {'title': 'Einstein–Podolsky–Rosen paradox', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.8433, 'explanation': 'EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails.', 'routes': {'boundary_weak_form_route': 0.1426, 'commutator_incompatibility_route': 0.1438, 'constraint_closure_route': 0.2059, 'discrete_protocol_route': 0.1094, 'spectral_operator_route': 0.1414, 'transport_flow_route': 0.2673}}; {'title': 'Quantum biology', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.7914, 'explanation': 'Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control.', 'routes': {'boundary_weak_form_route': 0.1532, 'commutator_incompatibility_route': 0.1317, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.0802, 'spectral_operator_route': 0.1574, 'transport_flow_route': 0.2761}}; {'title': 'Introduction to quantum mechanics', 'labels': ['weak spectral anchor', 'compatibility/closure junction', 'protocol is unusually explicit', 'multi-role hub', 'branch-ambiguous'], 'score': 2.7614, 'explanation': 'An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims.', 'routes': {'boundary_weak_form_route': 0.0712, 'commutator_incompatibility_route': 0.1637, 'constraint_closure_route': 0.1928, 'discrete_protocol_route': 0.108, 'spectral_operator_route': 0.2882, 'transport_flow_route': 0.2575}}; {'title': 'Measurement problem', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5725, 'explanation': 'The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning.', 'routes': {'boundary_weak_form_route': 0.2021, 'commutator_incompatibility_route': 0.0581, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1478, 'spectral_operator_route': 0.1374, 'transport_flow_route': 0.2689}}; {'title': 'Quantum gravity', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5455, 'explanation': 'Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.', 'routes': {'boundary_weak_form_route': 0.1683, 'commutator_incompatibility_route': 0.0505, 'constraint_closure_route': 0.2009, 'discrete_protocol_route': 0.1554, 'spectral_operator_route': 0.2006, 'transport_flow_route': 0.2689}}; {'title': 'Scattering', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5443, 'explanation': 'Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.', 'routes': {'boundary_weak_form_route': 0.161, 'commutator_incompatibility_route': 0.061, 'constraint_closure_route': 0.2083, 'discrete_protocol_route': 0.1568, 'spectral_operator_route': 0.204, 'transport_flow_route': 0.2673}}; {'title': 'Wave–particle duality', 'labels': ['weak spectral anchor', 'boundary-driven dynamics', 'protocol is unusually explicit', 'multi-role hub'], 'score': 2.5424, 'explanation': 'Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel.', 'routes': {'boundary_weak_form_route': 0.1643, 'commutator_incompatibility_route': 0.0565, 'constraint_closure_route': 0.1862, 'discrete_protocol_route': 0.154, 'spectral_operator_route': 0.2249, 'transport_flow_route': 0.2689}}

## Sparse Transition Hotspots

- **Quantum logic** (generators): attention `0.603036`, operation gain `26.1438`, top roles measurement=0.26, context=0.19, state=0.16; anomaly: compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: This page sits between Generator: lawful change before readout and Annotations: history, interpretations, and popular frames. The ambiguity is useful: it marks a place where two constructor roles meet and should be separated before the page is used as a derivation.
- **Quantum biology** (generators): attention `0.564918`, operation gain `23.67`, top roles context=0.19, observable=0.18, measurement=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum biology is an open-system transfer problem. The environment is part of the boundary that may preserve, destroy, or select coherence. A constructor must name the state carrier, the environmental coupling, the coherence or transport observable, and the classical control.
- **Schrödinger's cat** (states): attention `0.564708`, operation gain `26.7094`, top roles measurement=0.25, state=0.19, context=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: Schrödinger's cat is a macroscopic readout protocol. It couples microscopic unitary evolution to a macroscopic boundary and forces three steps apart: coherent transport, decoherence or apparatus coupling, and the rule by which one record is selected or conditioned.
- **Measurement problem** (measurement): attention `0.555044`, operation gain `27.3312`, top roles measurement=0.30, context=0.18, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: The measurement problem is a readout junction. It sits where unitary state transport, detector context, probability assignment, and state update meet. Decompose it into pre-measurement evolution, apparatus/environment coupling, POVM or projection readout, and post-record conditioning.
- **Delayed-choice quantum eraser** (measurement): attention `0.543928`, operation gain `26.5273`, top roles measurement=0.26, context=0.17, state=0.17; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The delayed-choice eraser is a protocol-order stress test. Its mechanism is the arrangement of which-path information, later measurement choice, and conditional correlation readout. The relevant statistics are defined only after the full measurement protocol is specified.
- **Introduction to quantum mechanics** (annotations): attention `0.542382`, operation gain `21.1053`, top roles measurement=0.21, context=0.21, state=0.19; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub, branch-ambiguous
  - Interpretation: An introductory page is a compressed map. It mixes states, operators, spectra, measurement, examples, and interpretations because it is written pedagogically. Decompose it into mechanism branches before using it for technical claims.
- **Einstein–Podolsky–Rosen paradox** (incompatibility): attention `0.541265`, operation gain `24.8691`, top roles measurement=0.26, context=0.18, state=0.17; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: EPR is a compatibility test. The mechanism is a bipartite state, separated measurement contexts, and a correlation readout that cannot be reduced to pre-existing local values. Start from the joint state and local observables, then ask which correlation constraint fails.
- **Quantum nonlocality** (incompatibility): attention `0.525728`, operation gain `26.2032`, top roles measurement=0.27, context=0.18, state=0.16; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This incompatibility page mixes observables and spectra, state evolution, and controlled update protocol. State which otherwise legal questions fail to share a single sharp representation, and what experiment or inequality exposes that failure.
- **Wave–particle duality** (states): attention `0.523242`, operation gain `24.6161`, top roles context=0.18, observable=0.18, measurement=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Wave-particle duality is a representation/readout switch. The same carrier is interrogated through incompatible experimental contexts, so the observed pattern changes from interference-like to count-like. Write it as context selection plus readout channel.
- **Scattering** (boundaries): attention `0.513957`, operation gain `23.8095`, top roles context=0.19, observable=0.17, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Scattering is a boundary-to-spectrum mechanism. The central map is from asymptotic in-states to out-states. Specify the interaction region, asymptotic channels, S-matrix or cross-section readout, and conservation constraints.
- **Quantum gravity** (fields): attention `0.51297`, operation gain `23.6794`, top roles observable=0.19, context=0.19, state=0.16; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Quantum gravity is a field/boundary junction. It asks whether geometry becomes part of the quantum state carrier or remains a realization layer for an operator theory. The missing constructor is a state of geometry, a constraint or evolution operator, a boundary or semiclassical readout, and a test of which geometric quantities survive quantization.
- **Fermi–Dirac statistics** (fields): attention `0.501914`, operation gain `22.9277`, top roles context=0.20, state=0.19, measurement=0.19; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Fermi-Dirac statistics is an admissibility rule for many-particle states. The mechanism is antisymmetry and occupation restriction. Expose anticommutation, exclusion, occupation numbers, and the thermodynamic readout derived from that constrained state space.
- **Quantum simulator** (states): attention `0.496801`, operation gain `20.4263`, top roles context=0.20, measurement=0.20, state=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: A quantum simulator is an engineered realization of another Hamiltonian or channel. It is both an observable system and a protocol for representing a target system. Name the simulated target, physical carrier, encoding map, and validation observable.
- **Wave function** (states): attention `0.47859`, operation gain `21.427`, top roles state=0.27, measurement=0.21, context=0.20; anomaly: weak spectral anchor, compatibility/closure junction, protocol is unusually explicit, multi-role hub
  - Interpretation: The wave function is a representation of the state carrier. It stores amplitude, phase, normalization, basis choice, and probability potential in one object. Separate representation, admissibility, evolution, and Born readout.
- **Spin (physics)** (states): attention `0.476684`, operation gain `22.0785`, top roles context=0.21, measurement=0.20, state=0.19; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This state page mixes observables and spectra, state evolution, and normalization and admissibility. Specify the state carrier, then distinguish representation, evolution, admissibility, and later readout.
- **Quantum Theory: Concepts and Methods** (annotations): attention `0.476453`, operation gain `25.1799`, top roles measurement=0.28, context=0.18, state=0.16
- **Quantum computing** (protocols): attention `0.472616`, operation gain `21.435`, top roles context=0.20, measurement=0.20, state=0.18; anomaly: weak spectral anchor, protocol is unusually explicit, multi-role hub
  - Interpretation: This protocol page mixes observables and spectra, state evolution, and controlled update protocol. Write it as an ordered sequence of allowed maps with a defined input state, output readout, and control showing why the order matters.
- **Quantum electrodynamics** (fields): attention `0.471496`, operation gain `21.6905`, top roles measurement=0.22, context=0.20, observable=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, compatibility/closure junction, multi-role hub
  - Interpretation: Quantum electrodynamics is a field-interaction constructor. It combines gauge admissibility, charged matter states, photon modes, perturbative transport, and scattering/readout. Derive it through field operators, gauge constraints, interaction terms, and observable amplitudes.
- **Quantum cosmology** (unresolved): attention `0.46888`, operation gain `31.25`, top roles state=0.25, observable=0.23, measurement=0.16
- **Quantum entanglement** (incompatibility): attention `0.459632`, operation gain `18.9988`, top roles measurement=0.22, state=0.19, context=0.18; anomaly: weak spectral anchor, boundary-driven dynamics, protocol is unusually explicit, multi-role hub
  - Interpretation: Entanglement is a tensor-factorization and correlation constraint. The state is not reducible to independently readable subsystem states, while the readout is still local and spectral. Separate the joint state, subsystem observables, and correlation test.

## Branch-Level Transition

- **State carrier inside Hilbert space**: `24` pages, `24` constructed, mean operation gain `21.3549`.
- **Generator: lawful change before readout**: `22` pages, `22` constructed, mean operation gain `22.5968`.
- **Many-mode extension: fields, particles, and scaling**: `21` pages, `21` constructed, mean operation gain `21.6581`.
- **Protocol layer: engineered transformations**: `18` pages, `18` constructed, mean operation gain `20.9146`.
- **Annotations: history, interpretations, and popular frames**: `16` pages, `16` constructed, mean operation gain `23.3205`.
- **Boundary realization: how effects appear**: `12` pages, `12` constructed, mean operation gain `22.5672`.
- **Readout rule: how answers become probabilities**: `10` pages, `10` constructed, mean operation gain `22.8728`.
- **Spectral question: what can be asked**: `10` pages, `9` constructed, mean operation gain `21.414`.
- **Hilbert-space context: admissible carrier and basis**: `7` pages, `7` constructed, mean operation gain `22.8302`.
- **Compatibility limit: what cannot be jointly sharp**: `6` pages, `6` constructed, mean operation gain `21.5705`.
- **Unresolved**: `1` pages, `0` constructed, mean operation gain `31.25`.

## Practical Conclusion

The useful object is the transition map, not the prose rewrite alone. It tells us which named topics are already constructible, which are only placed by evidence, which pages are multi-role junctions, and which parts of quantum theory are transferable as mechanisms. The new information is therefore structural: a topic encyclopedia becomes a queue of constructor roles and unresolved derivations.
