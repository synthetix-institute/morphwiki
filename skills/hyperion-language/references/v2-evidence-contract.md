# V2 Evidence Contract And Legacy Coordinate Reference

Read the relevant section when inspecting symbolic-compiler, variational or
legacy atlas artifacts. The parent `SKILL.md` defines schema selection and the
current nested constructor. Here `A` denotes the atlas regime, not the newer
constructor's realization clause. Historical artifact names are not a required
reading list for every question.

## Core Rule

Read Hyperion as an evidence language over measured equation/logical-morphism
coordinates. Do not treat machine tokens as human theory names.

The source truth is schema-dependent. In legacy atlas runs, the full `366D`
fingerprint is the source coordinate evidence. In V2 operator/substrate product
runs, the source evidence is the strict equation-morphism row plus
`operator_core`, `substrate_core`, `control`, typed graph edges, and source-card
links. `GGAE` means Geometric Graph Autoencoder. The current symbolic compiler
clusters standardized active evidence matrices; GGAE latents are a separate
learned representation audit and do not yet define the Ω/Ξ alphabet. Variance
axes, UMAP/PCA maps, and Wikipedia prose are downstream views.

## V2 Hierarchical Language Contract

When artifacts use `operator_substrate_v2`, do not collapse the system back
into one mixed geometry and do not read the language as one flat list of
apparatus labels. V2 uses a hierarchy:

```text
modelled state coordinates:
  Ω = operator-side coordinate; apparatus kernel only after the non-circular factor gate
  Ξ = admissible substrate / carrier / selector-context state

attached completion fibers:
  C = closure / admissibility obligation
  R = readout / current / observable obligation
  P = protocol / order / construction obligation

transport and variation layers:
  Λ = typed cross-row road family
  T = directed source-local transition
  Γ = bridge / transfer family
  J = finite first-variation diagnostic; current candidate only after a conservation gate

derived layers:
  A  = derived apparatus regime
  A* = optional non-overwriting refinement of a broad A parent
  Π  = repeated transition motif
  cells = sparse periodic-table / index layer
```

### Non-circular factor gate

Before calling `Omega` a reusable apparatus factor, inspect the state contract
stored in the operator alphabet or symbolic-language rollup:

```text
state_contract.omega_feature_scope == apparatus_only
```

The historical V2 `operator_core` matrix contains four source ranges:
operator apparatus (`0:32`), closure (`32:56`), readout (`56:80`) and protocol
(`80:96`). A codebook fitted to the whole active `operator_core` is an
operator-side composite, not an independent apparatus factor. It cannot by
itself establish the hierarchy `Omega x Xi` with a separately attached
`C/R/P` fiber. For such artifacts, call the token `operator-side state` and
mark the factor claim provisional.

Promotion of the non-circular hierarchy requires
`PREFIX_omega_scope_audit.json` to pass all four gates: paper-held-out
predictive non-inferiority, retained completion-fiber information, apparatus
fidelity and no increase in completion leakage. This ablation compares
apparatus-only and composite source codebooks against the same destination
state.

Use three nested identity levels. Do not call all three simply "identity":

```text
operator-kernel identity: K = Omega
realized mechanism type: M = (Omega, Xi)
completed contract:       I = (M; C, R, P)
```

`K` can persist while the substrate changes. `M` persists only when both
operator and substrate codewords persist. `I` persists only when the attached
completion mask also persists. This distinction is required when discussing
mechanism transfer or conservation.

The minimal V2 reading of a retained morphism is:

```text
morphism := Ω operator evidence realized on Ξ substrate evidence,
            with C/R/P completion obligations
```

The compact V2 sentence form is:

```text
K_i=Ω_i
M_i=(Ω_i, Ξ_i)
I_i=(M_i; C_i, R_i, P_i)
I_i --Λ/T/Γ--> I_j :: A(I_i,I_j) :: δ_G I :: J_candidate
```

where:

```text
K = reusable operator-kernel codeword
M = realized operator-on-substrate type
I = completed symbolic contract with attached C/R/P evidence
Λ = undirected or typed cross-row road family
T = directed source-local derivation transition
Γ = transfer bridge where one factor remains recognizable while the other changes
A = derived regime code over Ω, Ξ, route evidence and edge participation
δ_G I = first variation of the discrete typed action under generator G
J_candidate = current candidate only when first-variation diagnostics pass
```

Use the three-object form when explaining the architecture:

```text
state grammar:         K = Ω, M = (Ω, Ξ), S = (M; F), F = (C, R, P)
transport grammar:     E = (Λ, T, Γ), with J as a variation diagnostic on E
construction order:    D = monotone role-completion subgraph
observed source order: Q = source-local equation sequence graph
derived summaries:     A = state-regime index, Π = repeated transition motif
```

Do not merge `E`, `D`, and `Q`. Operational similarity, constructor order and
observed equation order are different mathematical objects.

## Compression And Constructor Contract

Keep these maps separate:

```text
typed extraction:
  source equation -> typed evidence state

symbolic compression:
  typed state/edge -> bounded factor-and-relation index

constructor extension:
  indexed state + missing roles + source context -> candidate equations/tests
```

Symbolic compression is many-to-one. It is not lossless equation coding.
Constructor extension is set-valued and is not the inverse of compression. A
candidate extension must restore assumptions, constants, boundaries and
context, then pass re-featurization, dimensional, closure, residual and
provenance checks.

Do not call six route families the terminal grammar. They are overlapping
interpretive axes. The grammar is the factor-and-relation system Ω/Ξ with
C/R/P obligations and Λ/T/Γ/J movement; A and Π are derived indices.

Do not call the language a compact predictive grammar from codebook counts or
full assignment alone. Those artifacts establish a compact symbolic index.
Predictive grammar requires held-out next-state or edge description-length
gain over frequency and factorized baselines. Inspect
`PREFIX_predictive_grammar_audit.json`; its pass is bounded to symbolic
source-local transitions and does not validate exact equations.

Do not infer the logical dependency graph from token counts. Inspect
`PREFIX_sparse_grammar_dependencies.json`. This audit holds out complete
papers, tests every subset of source `Omega`, `Xi` and `C/R/P`, and selects the
smallest parent set whose code length is non-inferior to the best tested set.
It fits separate graphs for completion-increasing, lateral and projection
transitions. A retained dependency is a predictive relation in written
equation sequences. It is not physical causality or neural attention.

Before claiming that a mechanism is preserved, inspect
`PREFIX_transition_invariance_audit.json`. Keep its tests separate:

```text
same Omega, changed Xi     = candidate operator-kernel transfer
same Omega and same Xi     = realized mechanism-type persistence
same Omega/Xi and same F   = completed-contract persistence
opposite T centroids       = algebraic inverse-axis candidate only
```

An opposite T pair is not physical time reversal. A stable codeword is not a
gauge invariant. Neither result is a Noether theorem without a source action,
an explicit group action or infinitesimal generator, boundary conditions and
an on-shell conservation test.

The current Ω/Ξ codebooks are fitted to typed active evidence, while the GGAE
learns separate operator and substrate bottlenecks. Confirm the Omega feature
scope before interpreting its semantics. Before describing the bottleneck as
the language-defining quotient, inspect
`PREFIX_bottleneck_codebook_ablation.json`: latent partitions must be stable,
improve the typed-edge contract, and then pass source-grounded token and
held-out predictive audits.

Use these V2 symbol roles:

```text
Ω     = modelled operator-apparatus coordinate; reusable transformation evidence
Ξ     = modelled substrate/carrier coordinate; admissible realization evidence
A     = derived apparatus regime; not a primitive factor
A*    = refined derived regime; non-overwriting split of a broad A parent
Λ     = typed road relation in product evidence space
T     = directed transition verb promoted by source-local sequence evidence
Γ     = bridge/transfer relation, including operator-transfer and substrate-transfer families
J     = variational current candidate from first-variation diagnostics
Π     = repeated transition motif; not a replacement for Λ or T
V     = variance-axis diagnostic per view or product view
```

Do not promote a third primitive factor merely because `A` is useful. A is
computed from the primitive factors and graph context:

```text
A := derive(Ω, Ξ, route_6, edge_participation)
```

The six V2 route families are:

```text
transport_flow
constraint_closure
spectral_operator
boundary_weak_form
commutator_incompatibility
discrete_protocol
```

These six route families are mechanism axes. They are different from the four
morphism-chain action verbs `preserve`, `project`, `convert`, and `add`.
They are also different from the nested V2 state contract
`K=Omega`, `M=(Omega, Xi)`, `I=(M; C, R, P)`. Routes describe which evidence
axis is active while states move or are compared; they are not state
coordinates or terminal grammar symbols.

Human explanation rule:

```text
Ω says what transformation apparatus remains recognizable.
Ξ says what kind of substrate can carry it.
C/R/P say which closure, readout/current, and protocol obligations complete the mechanism.
A says which recurring derived operator-on-substrate regime the full product occupies.
Λ/T/Γ say how rows are related.
J says whether a learned generator is stable under the typed action.
Π says which short construction motifs repeat.
```

The reason the language has this structure is empirical and architectural: the
V2 audits separate operator and substrate neighborhoods, while relation layers
are edge objects rather than node factors. A single flat A vocabulary hides this
factorization and produces overbroad basins.

This does not prove that the world contains exactly two fundamental factor
spaces. The bounded corpus result is conditional: operator classes can recur
across substrate classes, substrate classes can support several operator
classes, and C/R/P evidence determines whether a pairing is completed. This
may reflect physical modularity, mathematical writing, or both. External
formal and experimental tests are required to distinguish those explanations.

The strongest admissible generalization is **factorized persistence**:
scientific writing repeatedly separates a reusable transformation apparatus
from the carrier on which it is realized, and records closure, observability
and execution as additional obligations. Whether this regularity originates
in physical law, mathematical representation, human exposition, or all three
cannot be decided from the archive alone.

Human-readable signature names are centroid summaries, not source truth. A
`clean_endpoint_rate` measures extraction sanitation only. Before using a name
as a mechanism class, inspect `mechanism_role_support_rate`,
`classified_route_rate`, `complete_constructor_rate`, and
`interpretation_status` in `PREFIX_source_language_examples.json`. Retain the
numeric token and call the name provisional when the status is
`feature_signature_only` or `insufficient_source_support`.

Use the grammar-rule learner to test changes to this hierarchy. The learner
compares candidate structures such as:

```text
current_two_factor:
  primitive = operator_core, substrate_core

identity_with_completion_fiber:
  primitive = Ω operator_apparatus, Ξ substrate_core
  attached = C/R/P completion_core

three_factor_completion:
  primitive = Ω operator_apparatus, Ξ substrate_core, Χ completion_core

identity_multi_fiber:
  primitive = Ω operator_apparatus, Ξ substrate_core
  attached = C closure, R readout, P protocol
```

The grammar-rule learner is a structural screen. The sparse grammar-dependency
audit supplies held-out model selection. Promote C/R/P to a third primitive
space only when independent neighborhood evidence and complete-paper
predictive gain both require that factor. Otherwise read C/R/P as attached
completion obligations of the mechanism contract.

Product Lagrangian and Product Noether are not generic road labels and not
similarity thresholds. In V2 production artifacts they must be read as a
discrete variational calculation:

```text
state:
I_i = (Ω_i, Ξ_i; C_i, R_i, P_i)

discrete action:
I = sum_{i->j} L_ij
L_ij = sum_b w_b ||I_b(j) - I_b(i)||^2

infinitesimal generator:
G_F(i) = mean_{i->k in F}(I_k - I_i)

first variation:
delta_G I = sum_{i->j,b} 2 w_b (I_b(j)-I_b(i)) · (G_b(j)-G_b(i))
```

A discrete Noether-current claim is admissible only when the artifact reports
small relative first variation and small node-divergence residual for a named
generator. The current production audit reports finite edge-family variation;
unless a divergence residual is also present, call `J` an action-preserving
edge-family candidate, not a conserved current. High latent similarity alone
is not a Noether current. The default V2 action gives zero action weight to
equation-shape/control channels, so syntax cannot create a mechanism current
unless a run explicitly changes that weight.

A V2 void is a missing product obligation, not merely an empty atlas cell:

```text
operator void      = substrate exists but compatible operator/current is missing
substrate void     = operator exists but legal substrate/carrier/context is missing
coupling void      = operator and substrate exist separately but no low-action coupling joins them
transition void    = product road exists but no promoted Τ transition supports it
readout/closure void = operator/substrate pair exists but admissibility, closure, readout, or current is missing
protocol void        = operator/substrate pair exists but protocol/order evidence is missing
completion void      = operator/substrate pair exists but at least one C/R/P obligation is missing
control artifact void = apparent gap is driven by equation shape or syntax controls
```

Use only a role-aware void artifact with `void_schema_version >= 2` when
interpreting `readout_closure_void`, `protocol_void` or `completion_void`.
Earlier `readout_closure_void` exports used neighbourhood isolation rather
than the readout and closure feature blocks and therefore cannot support a
missing-role claim.

A typed void is a diagnostic queue, not yet a prediction. It becomes a
predictive queue only when `PREFIX_void_predictivity.json` shows a positive
matched effect on held-out complete papers with a confidence interval above
zero. The matching stratum must include at least the source `Omega`, `Xi` and
current completion mask. Otherwise report the void as an unresolved absence.

Blank area in UMAP/PCA is not a void statistic. `raw_projection` is a sampled
row-level audit; `leaf_cloud` is a display of the symbolic quotient. Report
sparsity from explicit role-completion or symbolic-cell occupancy. Likewise, a
curved kNN display road does not prove that a path avoids a void. That claim
requires path-versus-chord clearance against a defined void region.

In V2 outputs, the old 366D atlas is a historical/control comparison unless
the artifact explicitly fuses legacy 366D with V2 evidence.

## 366D Coordinate Contract

Use this band layout exactly:

```text
0:64     bigrams       hashed adjacent-token surface syntax
64:128   fivegrams     longer token surface syntax
128:256  spectral      operator-frequency / PSD apparatus
256:296  structure     structural/form layout metadata
296:363  geometry      trigram-cube shape/inertia morphology
363:366  entropy       compression/persistence summaries
```

Never collapse `0:256` into syntax. The n-gram syntax group is only:

```text
bigrams + fivegrams = 0:128
```

The `surface_syntax_triad` is:

```text
bigrams + fivegrams + spectral = 0:256
```

It is a triad of distinct evidence channels, not one homogeneous syntax band.

The `spectral` band is a fingerprint channel, not a content claim. It means
operator-frequency / PSD-like morphology in the 366D representation. Do not
rename a high `spectral` score as Fourier analysis, spectral theory, eigenmode
physics, wave mechanics, or frequency-domain mathematics unless representative
equations or equation witnesses explicitly instantiate that content.

Use this boundary:

```text
spectral band only
  -> operator-frequency morphology / spectral-operator route hypothesis

spectral band + representative equations with Fourier/eigen/mode/spectrum form
  -> possible spectral-type mathematics, still requiring validation
```

Sequential/flow evidence is edge-level evidence, usually `edge_type=5`. It is
not a 366D node band.

## Legacy 366D Symbol Roles

Use this section only for legacy 366D artifacts. For V2
`operator_substrate_v2` artifacts, use the hierarchical language contract
above. Do not import these legacy meanings into V2 atlas, DAG, GGAE, or decoder
interpretation.

In legacy 366D artifacts, use the symbols this way:

```text
Ω = coordinate radical / low-level apparatus atom
Α = apparatus-regime noun over Ω, route, fiber, and Λ evidence
Ξ = state/chart/territory evidence
Λ = local transformation family
Τ = Tau/TNN directed transition operator, only when promoted by directed edge evidence
J = private invariant/conservation-candidate diagnostic
V = variance-axis diagnostic only
Π = learned derivation/protocol primitive when present
```

Important boundaries:

- `Ω` is not a final noun or established operator name.
- `Α` is the preferred language for constructing candidate equation forms.
- `Ξ` is not a theory name.
- `Λ` is not gauge/rotation/duality/scale unless representative equations validate that name.
- `Τ` is not available unless `transition_operator_language.json` or `edge_language_report.json` promotes it.
- In legacy 366D, a `Τ` transition operator is a learned edge verb over observed displacements `v = x_target - x_source` in 366D fingerprint space. In V2, `T` is a source-local directed transition over typed operator/substrate evidence. Neither is automatically a physical time-evolution operator, Hamiltonian, implication arrow, functor, gauge transform, or GW analogy.
- Static node labels such as `J00`, `J01`, or `J_flat` are private diagnostics; they are not source-level conserved currents.
- `V` axes are SVD/covariance diagnostics, not operators and not replacements for 366D fibers.

## Flow And Geometry Roles

Keep the flow languages separate:

```text
GW transport
  Gromov-Wasserstein-style relational coupling between two morphism clouds
  asks whether internal distances/relations in one region can be transported to another
  may produce a similarity-transport diagnostic over matched 366D displacements
  not a transition verb, not temporal flow, not causality, and not a physical flow by itself

Directed pairs / CFG
  observed document-order, rewrite, or symbolic-path edge evidence
  can support Τ verbs after promotion

Noether J currents
  private invariant diagnostics over directed representation transitions
  not physical conservation laws until equations and domain validation support them

Ricci/GGAE
  GGAE = Geometric Graph Autoencoder
  Ollivier-Ricci-like graph curvature in the learned Poincare/GGAE latent
  diagnoses phase separation, necks, curvature, bottlenecks, and coherent patches
  lives in GGAE/hyperbolic graph geometry, not raw 366D coordinate space
  not physical geometry or a physical phase transition by default

Boundary/constraint evidence
  extracted from retained equation witnesses into boundary_condition_report.json
  and physical_constraint_report.json
  physical-world gate for interpretation: domains, initial data, boundary values,
  closure, gauge, normalization, compatibility, conservation, and inequalities
  not proof of a physical law without parser, dimension, source-context, and held-out checks
```

## Artifact Order

For a V2 operator/substrate run, select artifacts from this catalogue according
to the claim being checked. Read the run manifest and representative source
rows first. Missing evidence limits the corresponding claim; it does not
prevent explanation of available evidence. Do not regenerate artifacts merely
to answer a reading request.

```text
article_language_contract.json / .md
PREFIX_manuscript_contract_audit.json / .md
PREFIX_hierarchical_language.json / .md
PREFIX_symbolic_language.json / .md
PREFIX_symbolic_full_assignment.json / .md
PREFIX_omega_scope_audit.json / .md
PREFIX_completion_flow.json / .md
PREFIX_source_language_examples.json / .md
PREFIX_grammar_rule_learner.json / .md
PREFIX_bottleneck_codebook_ablation.json / .md
PREFIX_predictive_grammar_audit.json / .md
PREFIX_grammar_dynamics.json / .md
PREFIX_role_voids.json / .md
PREFIX_void_predictivity.json / .md
PREFIX_promoted_token_purity.json / .md
PREFIX_independent_factorization.json / .md
PREFIX_prospective_constructor_audit.json / .md
PREFIX_geometric_operator_alphabet.json
PREFIX_morphism_state_alphabet.json
PREFIX_apparatus_regimes.json
PREFIX_apparatus_regimes_refined.json
PREFIX_lambda_families.json
PREFIX_transition_operator_language.json
PREFIX_gamma_bridge_alphabet.json
PREFIX_noether_orbit_alphabet.json
PREFIX_derivation_fragments.json
PREFIX_v2_dag.json / .md
PREFIX_source_constructor_graph.json / .md
PREFIX_variational_operator_substrate.json / .md
PREFIX_typed_graph.json
PREFIX_territory_atlas.json / .npz
PREFIX_lagrangian_roads_plot.json
```

For legacy 366D runs, the older atlas artifacts such as `research_atlas.json`,
`apparatus_regimes.json`, `mathematical_meaning_report.json`, and
`wikipedia_hierarchy.json` remain control references. Do not use them as V2
source identity unless an explicit legacy--V2 alignment audit is present.

Treat `wikipedia_hierarchy.json` as readable prose, not source identity.

## Article Evidence Order

For Wikipedia-style article synthesis, use this order:

```text
1. Representative equations / source statements
2. Constructor frame and source-card context
3. Ω operator factor and Ξ substrate factor
4. Derived A/A* regime, with route_6 profile
5. Λ roads, T directed transitions, Γ bridges
6. J first-variation status and variational-action evidence
7. Π repeated motifs and constructor DAG layer
8. Boundary/constraint physical-gate evidence
9. GGAE/atlas topology as representation evidence
10. Held-out void predictivity, residuals, and missing validation
```

Do not start articles with machine coordinates. Machine tokens belong in bounded
evidence tables unless the user explicitly asks for raw diagnostics.

## Equation Construction

Construct equations from the hierarchy, not from a flat `A` label or raw `Ω`
alone:

```text
candidate mechanism frame :=
  Ω operator factor
  + Ξ substrate factor
  + closure/readout/protocol obligations
  + route_6 profile
  + Λ/T/Γ relation evidence
  + source-card context
```

If the Omega scope is composite, replace `Omega operator factor` with
`operator-side state` and do not use stripping/reattachment language until the
non-circular factor gate passes.

Examples:

```text
Ω spectral/operator + Ξ inner-product-like substrate + closure/readout evidence
  try eigenvalue, kernel, propagator, spectral expansion, or operator-response forms

Ω transport/closure + Ξ coordinate or probability substrate + protocol evidence
  try continuity, flow, compatibility, projection, constraint, or weak/integral forms

Ω algebraic/commutator + Ξ non-coordinate substrate
  avoid spatial PDE claims unless source cards or substrate evidence support them
  try algebraic/operator constraints, commutators, compatibility, or matrix forms
```

Legacy A09/A06 language is not active V2 language. Use it only when the
artifact explicitly aligns legacy 366D regimes to V2 rows:

```text
legacy A09/A06 terms require:
  legacy atlas artifact
  V2 row alignment
  source equation witnesses
  statement of which V2 Ω/Ξ/A/Λ/T/Γ/J tokens replace the legacy label
```

The V2 construction pathway is:

```text
source-card equation
-> constructor frame
-> Ω/Ξ factor assignment
-> A/A* derived regime
-> Λ/T/Γ relation evidence
-> decoder proposal or equation template
-> re-featurization, residual tests, and source-level validation
```

Every generated equation is only a hypothesis until it is parsed, re-featurized
into V2, checked against the target constructor frame, and validated
mathematically.

## Claim Ladder

Promote claims only through this ladder:

```text
source equation or source-card witness
constructor frame
Ω/Ξ primitive factor assignment
A/A* derived regime assignment
Λ/T/Γ relation evidence
J variational audit when relevant
decoder or residual test
domain validation and human mathematical name
```

Evidence tiers:

```text
Tier 0: feature or display pattern only
Tier 1: stable Ω/Ξ assignment with source-card or row evidence
Tier 2: derived A/A* regime plus Λ/T/Γ relation support
Tier 3: representative equations support the form and re-featurize near target
Tier 4: J/Noether-like, GGAE, decoder/residual, and transition checks agree on held-out evidence
Tier 5: external scientific or theorem-level validation
```

## Fail-Closed Rules

Apply these boundaries to claims about the learned atlas. Source equations can
independently establish dynamics or a known theory without a promoted atlas
token. Missing atlas support does not negate that source-level result.

- No representative equations means no theory name.
- No promoted `Τ` means no transition or process claim.
- `Γ` or GW-only evidence means analogy or transfer candidate, not a bridge law.
- A hardened method bridge is still a method-transfer suggestion until equation
  residuals, assumptions, dimensions, and boundary conditions pass.
- `L_theta`/Lagrangian scores are representation-space path diagnostics; check
  `action_source` before treating them as direct learned-action evidence.
- `J` current evidence means internal invariant diagnostic, not physical conservation law.
- `A`/`Α` regime means derived candidate apparatus, not a primitive factor and not a final domain.
- `Ω` without `Ξ` is not a realized mechanism; `Ξ` without `Ω` is not a mechanism identity.
- Sparse territory means unobserved coordinate combinations in this corpus, not impossible laws of nature.
- A role void is not a discovery recipe until it predicts held-out role
  acquisition and a source-grounded candidate passes rejection tests.
- A completion DAG is directional by construction. Claim an empirical order
  among C/R/P only when `PREFIX_completion_flow.json` reproduces that order on
  held-out complete papers.
- Near-equal forward and reverse aggregate code lengths do not establish an
  inverse for each transition class. Call the conversion sector
  near-reversible only at the measured aggregate resolution.
- J-violating targets are adversarial coordinate probes, not decoded equations.
- Human labels are display paraphrases, not ontology source truth.

## Output Pattern

For an internal diagnostic, select relevant fields from this pattern rather
than requiring every heading in every answer:

```text
Finding:
Evidence:
Ω/Ξ/A apparatus and route:
Λ/T/Γ/J/GGAE status:
What it may mean:
What it does not prove:
Falsification route:
Next computation:
```

For article synthesis:

```text
Content present:
Representative equations:
Apparatus reading:
Transitions and bridges:
Noether/symmetry status:
Relation to known theories:
Validation gaps:
```

For equation hypotheses:

```text
Candidate equation/template:
Ω/Ξ/A evidence:
Equivalent forms to test:
Assumptions and boundary conditions:
Expected V2 movement:
Λ/T/Γ/J/GGAE checks:
Falsification route:
```
