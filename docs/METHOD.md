# Method

MorphWiki represents a scientific field with two synchronized graphs. The
operational graph records what a construction does. The provenance graph records
where each clause, equation, and interpretation came from.

## Operational Identity

The common hierarchy is

```text
(Omega, Xi) -> M -> I_op=(M; C, R, P) -> I_real=(I_op; A)
```

`Omega` is an operation and `Xi` is the carrier on which it is defined. Their
pair is the mechanism core `M`. Closure `C`, observable map `R`, and protocol `P`
complete the operational identity. The realization `A` supplies the named
objects, parameters, units, geometry, boundaries, devices, and experimental
conditions of a concrete model.

The hierarchy does not impose one temporal order. It distinguishes levels of
specification. Within a paper, a derivation may add a clause, project a complete
relation onto one consequence, or rewrite the same mechanism in another
representation.

## Quantum Specialization

For quantum theory, a broad operational form is

```math
\Xi_Q=(\mathcal H,\mathcal D,\mathcal S),\qquad
\Omega_Q\supset\{\mathcal E_P,\{E_y\}_y\},
```

```math
\rho_P=\mathcal E_P(\rho_0),\qquad
p(y\mid P)=\operatorname{Tr}(E_y\rho_P).
```

The carrier includes the Hilbert or Fock space, admissible states, domains, and
factorizations used by the problem. The operation includes generators,
observables, channels, symmetry actions, and compositions. Closure imposes
normalization, positivity, domain, self-adjointness, gauge, conservation, or
compatibility conditions. The observable map and protocol connect the formal mechanism to
an observable consequence and an executable order of operations.

For a closed system with a time-independent self-adjoint Hamiltonian,
`E_P(rho)=U(t) rho U(t)^dagger` with `U(t)=exp(-iHt/hbar)`. The channel form is
kept in the upper-level constructor because it also covers open systems,
measurements, feedback, and quantum information protocols.

## Transformations

MorphWiki links two scientific representations only after specifying the
retained relation:

```math
I_i=((\Omega_i,\Xi_i);C_i,R_i,P_i)
\xrightarrow{T}
I_j=((\Omega_j,\Xi_j);C_j,R_j,P_j).
```

The index change may describe physical evolution, reformulation, completion,
carrier replacement, projection, composition, deformation, or revision. The
retained relation may be an amplitude, expectation value, algebra, conserved
flux, probability law, correlator family, or controlled approximation. Equation
shape and vocabulary do not establish the link.

## Constructor Operations

The public constructor uses six verbs:

1. `complete`: add a missing closure, observable map, or protocol;
2. `reattach`: replace the operation or carrier under explicit compatibility maps;
3. `compose`: join supported transformations;
4. `deform`: vary a boundary, parameter, scale, or representation while tracking an invariant;
5. `observe`: build the observable or measurement that exposes a consequence;
6. `revise`: use a failed consequence to replace the responsible clause.

The discovery contract is

```math
(I_{\mathrm{op}},p;Q_{\mathrm{keep}},B_{\mathrm{edit}})
\longmapsto
(\widehat I_{\mathrm{op}},\widehat A,\widehat y).
```

`Q_keep` states what must survive. `B_edit` states which clauses may change.
The output includes a new operational identity, a physical realization, and a
derived consequence. This record makes the proposal reproducible and identifies
the clause to revise if the consequence fails.

## Provenance And Evidence

Every public page retains:

```text
topic and historical vocabulary
source document and passage
equation witness
constructor clauses
transformation and retained relation
realization and predicted consequence
```

Provenance does not determine operational identity, but it remains necessary for
attribution, priority, interpretation, and checking the source assumptions.

## From Corpus To Book

1. Export topic records and their source equations.
2. assign each record to the constructor clause it primarily specifies;
3. recover source-local and cross-topic transformations;
4. generate the mechanism map and transformation cases;
5. write all retained topics as specializations of the shared identity;
6. compile the book and verify that no topic or equation-bearing derivation page was lost.

Sparse-attention summaries, placement reports, and build diagnostics are retained
as reproducibility artifacts. They are not chapters in the default public book.

## Physical Standard

A constructor proposal must satisfy the mathematical conditions of its field.
In quantum theory these include the relevant domain and self-adjointness
conditions, positivity and normalization, complete positivity for channels,
gauge or constraint closure, dimensional consistency, and a defined observable or probability law.
An empirical proposal must also specify apparatus, parameter regime, controls,
and a consequence that differs from plausible alternatives.
