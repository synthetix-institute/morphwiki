# Hyperion Language Explanatory Texts For Article Synthesis

Use this file together with `SKILL.md`. `SKILL.md` defines the internal
evidence language; this file shows how to turn that language into neutral
scientific prose. The examples are schematic style guides. Do not copy their
sentences verbatim into generated articles; every page lead must be specific to
that page's representative equations, variables, operators, and constraints.

## Core Writing Rule

The article subject is the reconstructed mathematical or physical topic.
Internal tokens explain the evidence path to the generator; they are not the
topic and must not appear in public article prose.

```text
bad:
  A spectral-operator apparatus region in the morphism corpus where
  operator-frequency evidence dominates.

good when content is present:
  Conserved-density transport is described by a gradient-like operator acting
  under an explicit closure constraint.

good when content is missing:
  The available source material is insufficient to reconstruct a mathematical
  field. A field-level interpretation should therefore be withheld until
  content-bearing equations are available.
```

## Two-Space Translation Rule

Every article must keep two spaces separate:

```text
Hyperion representation space:
  learned coordinates of equations, morphisms, TeX statements, bands,
  routes, transitions, and corpus relations

source mathematical / physical space:
  variables, domains, operators, constraints, boundary conditions, units,
  assumptions, and physical systems visible in retained source evidence
```

Do not turn an internal band into a real physical object. A high internal
geometry score is not automatically physical geometry. A high internal spectral
score is not automatically spectral theory. A stable internal current role is
not automatically a physical Noether law.

```text
bad:
  This field collects mathematical structures where geometric and spectral
  constraints organize real fields.

bad:
  The system is a geometric-spectral field because the cluster has high
  geometry and spectral bands.

good when equations show content:
  The retained equations combine an operator response with an explicit domain
  or boundary condition. The physical reading comes from the witnessed operator
  and boundary terms, not from the discovery metadata.

good when equations do not show content:
  The retained witnesses do not contain enough equation content to decide
  whether a spectral method or physical domain is actually involved. Those
  interpretations should be withheld.
```

Translation must be evidence-gated:

```text
spectral band only
  -> machine spectral-band evidence

spectral band + witnessed eigen/Fourier/mode/operator equation
  -> possible spectral/operator mathematical form

geometry band only
  -> machine geometry-band evidence

geometry band + witnessed domain, boundary, metric, curvature, coordinate,
or shape variable
  -> possible physical or mathematical geometry
```

## What The LLM Must Understand

Hyperion language is an audit language:

```text
Ξ tells where the field sits.
Ω tells which coordinate radicals are active.
Α tells the apparatus or equation-construction regime.
Λ tells the local transformation family.
Τ tells a directed transition only when promoted by edge evidence.
J tells current/conservation evidence only after Noether validation.
V tells variance-axis diagnostics only.
GW tells relational similarity transport, not causality or physical flow.
Ricci/GGAE tells graph topology, not spacetime geometry by default.
```

Human text should translate this into:

```text
what equation form appears,
what operation transforms it,
what constraint closes it,
what symmetry or current may be preserved,
what evidence is missing.
```

## Description Paragraph Patterns

When representative equations exist:

```text
The Description should start with the reconstructed topic:
  "This topic concerns ..."
  "The equations describe ..."
  "The mathematical structure is organized around ..."
```

When equations are absent:

```text
The Description should start with the absence:
  "The available source material is insufficient ..."
  "The available equations do not preserve enough source mathematics ..."

Then explain what can still be said:
  "Only a limited evidence note can be written ..."
```

Never start with:

```text
F###
Ξ...
Ω...
Α...
Λ...
J...
Τ...
366D
morphism apparatus
operator-frequency region
spectral-operator apparatus region
corpus-level structure
```

## Internal Evidence Rule

Internal evidence may be used to decide what to write, but public articles
should not expose machine tokens or provenance. If an audit table is needed, it
belongs in a separate audit artifact, not in the Wikipedia-style article.

```text
bad:
  Machine Evidence: Α02, Ω01, Λ10, J_flat.

good:
  The equation family suggests a transport or closure formulation, but the
  source material does not yet justify a conservation-law interpretation.
```

## Bridge Explanation Pattern

For bridges, use method-transfer language:

```text
good:
  The bridge suggests trying a weak-form or transport formulation on the
  target equations, because source and target share route and fiber evidence.
  This is a method-transfer hypothesis until the transformed target equation
  passes residual and boundary-condition checks.

bad:
  The two fields are the same physics.
  GW proves a geodesic flow.
  The bridge reveals a universal law.
```

## Symmetry And Conservation Pattern

Use strict language:

```text
internal current diagnostic strong:
  "The equation family shows a repeatable invariant-like structure across the
  available transformations. The scientific interpretation is that a conserved
  quantity, balance law, or symmetry may exist, but it must be derived from the
  equations and checked against the stated domain and boundary conditions."

internal current diagnostic weak:
  "No conserved quantity follows from the available equations alone. A proposed
  invariant would require an explicit continuity equation, variational
  symmetry, boundary-compatible balance law, or residual test."
```

Physical conservation requires:

```text
representative equation,
identified variables,
dimension/unit compatibility,
boundary/domain assumptions,
residual test,
held-out recurrence.
```

## Applications And Predictions Pattern

Only write evidence-scoped applications:

```text
good:
  "A useful next test is to express the target equations in continuity form
  and measure whether the residual decreases under the proposed closure."

bad:
  "This predicts a new physical force."
  "This solves quantum gravity."
  "This is a universal theory of nature."
```

## Final Check Before Returning JSON

Before returning the article JSON, verify:

```text
summary starts with content or missing-content statement
Description starts with content or missing-content statement
public article does not mention Hyperion, morphisms, 366D, GGAE, internal bands,
or machine evidence
no invented equations
no invented established-theory relation
no physical prediction without boundary/constraint/residual evidence
structural_category is compact and never INDETERMINATE
```
