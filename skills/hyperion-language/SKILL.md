---
name: hyperion-language
description: Interpret Hyperion equation states, mechanism transfers and constructor outputs using the schema of the selected run. Use for Hyperion language questions and source-grounded explanations.
---

# Hyperion Language

Explain the operation, what it acts on, the conditions under which it works,
and the consequence that can be calculated or measured. Machine tokens index
these objects; they do not replace equations or establish physical laws.

## Choose The Contract

Read the selected run's manifest, schema, feature scope and source references.
An implementation or a later document does not retroactively upgrade an older
run. Use the user's selected run rather than a hard-coded "latest" folder.

| Artifact family | Interpretation |
| --- | --- |
| Legacy 366D atlas | Fingerprint bands and A00/A09-style regimes; historical coordinate evidence |
| V2 operator/substrate compiler | Typed equation rows, factor codebooks, completion evidence and typed edges |
| V2.1 / nested constructor | Operational clauses, joint destination proposals, explicit nulls, interfaces and physical realizations |

V2.1 run versions and `ConstructorV12` implementation versions are different
identifiers. Record both when present. Mixed V1/V2 claims require row-level
alignment and the equations behind the matched rows, not matching labels.

## Operational State

```text
K = Omega                     operator-side identity
M = (Omega, Xi)                operation on a carrier
I_op = ((Omega, Xi); C, R, P)   completed operational contract

Omega   operation, generator or equational rule
Xi      carrier, state space, medium or representation sector
C       imposed admissibility, closure, normalization or boundary conditions
R       observable map and derived invariants or conserved quantities
P       preparation, intervention, coarse-graining or measurement order
```

A conserved quantity derived from the dynamics belongs to `R`; an imposed
constraint belongs to `C`. A boundary condition is not automatically a
conservation law. Use the source equation to resolve ambiguous assignments.

Keep two uses of `A` separate: `A_regime` is a derived atlas class;
`A_realization` in the nested constructor supplies material names, variables,
units, parameters and implementation details. Preserve exported keys, but
qualify their meanings in explanations. Likewise, `P` is the protocol clause;
an explicit probability density must be defined separately.

The historical V2 `operator_core` combines apparatus and C/R/P features. Call
its codeword an operator-side composite unless the recorded scope is
`apparatus_only` and the corresponding factor tests support separation.
Compression is many-to-one. Decoding proposes realizations; it is not an exact
inverse. A GGAE latent or a UMAP location alone does not define a mechanism.

## Relations And Construction

`Lambda` denotes typed roads, `T` source-local directed transitions, and
`Gamma` candidate transfers. `J` is a variation diagnostic until a specified
action, generator and conservation calculation justify a stronger name.
Corpus action is a representation-space cost unless its physical action is
actually supplied. GW similarity can nominate a comparison, not prove it.

The nested constructor predicts edits and a joint destination `(Omega, Xi)`.
Factor rankings are marginals of that joint prediction, not independent
proofs of compatibility. Explicit null means an absent clause under the run's
extraction contract; a missing file or unknown value must not be recoded as null.

The six construction operations are completion, reattachment, deformation,
composition, observation and revision. These are not the six legacy feature
routes or the four atomic retain/attach/detach/replace edits.

For source operation `Omega_A`, target operation `Omega_B`, state map `alpha`
and output map `beta`, a typed linear interface tests

```text
Delta(alpha, beta) = Omega_B alpha - beta Omega_A.
```

For nonlinear flows use the pushforward condition
`d(alpha)_x f(x,e) = g(alpha(x), alpha_E(e))`, with domains and units supplied.
Do not subtract expressions in incompatible spaces.

- Vanishing defect supports transfer of the tested operation and consequence.
- A nonzero operator-valued defect with a closing equation can supply an
  additional operator. A changed operational clause can extend the mechanism.
- A mismatch without closure leaves this attempted transfer unresolved or
  rejected. A change confined to realization is not a new mechanism class.

These are outcomes of construction, not extra construction verbs. Numerical
tolerance must be reported; a small sampled residual is not an exact theorem.
Keep corpus support, compatibility residuals and observable consequences
separate. A weighted sum must not hide a failed physical condition.

## Use Evidence Proportionately

For an explanation, read the relevant source equations and result fields and
answer the physical question. For a proposal, specify the preserved operation,
changed carrier or clause, interface, realization and discriminating test.
For a validation claim, inspect the tests required by that claim. Do not
require every atlas audit or launch simulations for a read-only question.

An empty product cell or blank map region is not a prediction. Missing-role
enrichment needs matched held-out evidence; a negative result stays negative.
A dimensionless match nominates a comparison, not a universality class.
Stable fitted exponents do not alone establish a renormalization fixed point.

Memory requires a specified preparation, release dynamics, readout and time
window. Neither spatial frustration nor a nonzero operation commutator alone
establishes retained memory. Distinguish surface curvature, connection
holonomy, incompatibility and persistence under relaxation. Use measured
release and control comparisons; do not promote the legacy A09 label into a
universal memory kernel.

## Focused References

- [V2 evidence contract](references/v2-evidence-contract.md): compiler feature
  scopes, atlas symbols, legacy 366D bands, variational and predictive audits.
- [Constructor contract](references/constructor-contract.md): current
  interfaces, structured non-transfer, physical tests and implementation paths.
- [Explanatory examples](EXPLANATORY_TEXTS.md): read when writing or repairing
  public scientific prose, not for a routine file or schema question.

The canonical bundle is maintained in `KnowledgeParser/skills/hyperion-language`.
`scripts/sync_hyperion_language_skill.py` checks or updates the morphwiki copy.
Do not maintain independent symbol definitions in companion skills.
