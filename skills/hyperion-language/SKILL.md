---
name: hyperion-language
description: Use when an LLM must understand or write with the Hyperion symbolic language: 366D fingerprints, Ω/Α/Ξ/Λ/Τ/J/V roles, GW/Ricci/GGAE (Geometric Graph Autoencoder)/Noether flows, apparatus regimes, transition evidence, Wikipedia-style article generation, equation construction, or claim validation. Enforces syntax-band separation, evidence ordering, and fail-closed scientific interpretation.
---

# Hyperion Language

Companion file: `EXPLANATORY_TEXTS.md`.

Article-synthesis prompts must load this skill and the companion explanatory
texts. This file defines the language; the companion file shows bad/good human
prose patterns so the LLM describes recovered equations instead of describing
Hyperion instructions.

## Core Rule

Read Hyperion as an evidence language over measured equation/logical-morphism
coordinates. Do not treat machine tokens as human theory names.

The source truth is the full `366D` fingerprint. `GGAE` means Geometric Graph
Autoencoder; GGAE latents, variance axes, UMAP/PCA maps, and Wikipedia prose
are downstream views.

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

## Symbol Roles

Use the symbols this way:

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
- A `Τ` transition operator is a learned edge verb over observed displacements `v = x_target - x_source` in 366D fingerprint space. It is not automatically a physical time-evolution operator, Hamiltonian, implication arrow, functor, gauge transform, or GW analogy.
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

When interpreting a run, inspect artifacts in this order:

```text
article_language_contract.json / .md
research_atlas.json
apparatus_regimes.json
geometric_operator_alphabet.json
directed_transition_pairs.json
transition_operator_language.json
morphism_path_grammar.json
edge_language_report.json
level5_noether_validation.json
noether_cross_fiber_transfer.json
boundary_condition_report.json / physical_constraint_report.json
cross_field_analogies.json / gw_analogy_candidates.json
method_bridge_pipeline/validated_method_bridges.json
high_dimensional_bridge_analysis/high_dimensional_bridge_analysis.json
novel_bridge_proposals/novel_bridge_proposals.json
lagrangian_landscape/lagrangian_landscape_report.json
j_violation_targets.json
morphism_periodic_table.json
mathematical_meaning_report.json / .md
wikipedia_hierarchy.json
```

Treat `wikipedia_hierarchy.json` as readable prose, not source identity.

## Article Evidence Order

For Wikipedia-style article synthesis, use this order:

```text
1. Representative equations / source statements
2. Α apparatus regime
3. Route affordances
4. Fiber profile
5. Ω/Λ/J diagnostics
6. Boundary/constraint physical-gate evidence
7. Directed transitions / Τ verbs
8. GW bridges
9. Ricci/GGAE topology
10. Voids and missing validation
```

Do not start articles with machine coordinates. Machine tokens belong in bounded
evidence tables unless the user explicitly asks for raw diagnostics.

## Equation Construction

Construct equations from `Α`, not from raw `Ω` alone:

```text
Α := Ω motif :: route family :: fiber carrier :: Λ family
```

Examples:

```text
Α spectral-operator apparatus
  try eigenvalue, kernel, propagator, spectral expansion, or operator-response forms

Α transport/closure apparatus
  try continuity, flow, compatibility, projection, constraint, or weak/integral forms

Α geometry-free spectral-structure apparatus
  avoid spatial PDE claims by default
  try algebraic/operator constraints, commutators, compatibility, or matrix forms
```

A09 kernel language:

```text
A09 = discovered pure theory-kernel regime in the current atlas
Omega26 = rare operator-frequency compression marker inside the A09 core
A06 = embodiment-frontier / transport-closure gate
A08-like regimes = geometry-bearing receptors for re-embodiment
central low-action valley = known theory machinery stabilized by the corpus
red/void region near A06 = equation-construction frontier
```

Use this reading when the evidence matches the measured A09 signature:

```text
geometry = 0
spectral + structure ~= 1
constraint_closure + spectral_operator dominate
validated bridges containing A09 = 0/75
A09 voids enriched toward A08 receptors
```

Do not treat A09 as a smooth method bridge. Treat it as a compressed
instruction source:

```text
strip geometry
preserve operator role, spectral structure, closure, boundary debt, observable
route the stripped kernel through A06-like transport/flow/boundary/compatibility closure
re-embody in a receptor apparatus by adding geometry, boundary, or weak form
test by residual improvement and controls
```

Use the Lagrangian atlas reading when the learned signed-action field supports
it:

```text
A09 strips theories into operator/structure closure.
A06 is where stripped kernels must become transport, flow, boundary,
compatibility, and geometric closure.
The central blue valley is known low-action theory machinery already stabilized
by the corpus.
The red/void region near A06 is where new equations are needed.
```

This is a construction pathway, not just a map caption:

```text
embodied source theory
-> A09 disembodiment kernel
-> A06 embodiment frontier
-> central low-action machinery or geometry-bearing receptor
-> residual-tested candidate equation
```

Every generated equation is only a hypothesis until it is parsed, re-featurized
into 366D, checked against the target apparatus, and validated mathematically.

## Claim Ladder

Promote claims only through this ladder:

```text
coordinate target
candidate equation/logical morphism
refeaturization into 366D
Α/Ω/Λ assignment
GW/J/Τ/Ricci/GGAE checks
representative-equation and domain validation
human mathematical name
```

Evidence tiers:

```text
Tier 0: coordinate or geometry pattern only
Tier 1: stable Ω/Ξ/Α/Λ/Π pattern
Tier 2: GW bridge, void target, bridge-taxonomy label, or directed Τ candidate with controls
Tier 3: representative equations support the form and re-featurize near target
Tier 4: J/Noether, GW, Ricci/GGAE, and transition checks agree on held-out evidence
Tier 5: external scientific or theorem-level validation
```

## Fail-Closed Rules

Use these exact boundaries:

- No representative equations means no theory name.
- No promoted `Τ` means no transition or process claim.
- GW-only evidence means analogy or transport candidate, not a bridge law.
- A hardened method bridge is still a method-transfer suggestion until equation
  residuals, assumptions, dimensions, and boundary conditions pass.
- `L_theta`/Lagrangian scores are representation-space path diagnostics; check
  `action_source` before treating them as direct learned-action evidence.
- `J` current evidence means internal invariant diagnostic, not physical conservation law.
- `Α` regime means candidate apparatus, not final domain.
- Sparse territory means unobserved coordinate combinations in this corpus, not impossible laws of nature.
- J-violating targets are adversarial coordinate probes, not decoded equations.
- Human labels are display paraphrases, not ontology source truth.

## Output Pattern

For interpretation:

```text
Finding:
Evidence:
Α apparatus / route:
GW/T/J/Ricci status:
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
Α apparatus evidence:
Equivalent forms to test:
Assumptions and boundary conditions:
Expected 366D movement:
GW/J/Τ/Ricci checks:
Falsification route:
```
