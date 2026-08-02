# MorphWiki Field-Wiki Contract

A MorphWiki field wiki is a source-grounded reconstruction of a scientific field
around mechanisms and their transformations. Familiar topics remain searchable,
but the field map is built from operational clauses rather than historical order.

## Four Synchronized Views

### Topic View

Preserves the names used in papers, textbooks, reviews, and public references.
It answers: what will a reader search for?

### Mechanism View

Represents the topic as

```text
(Omega, Xi) -> M -> I_op=(M; C, R, P) -> I_real=(I_op; A)
```

It answers: what operation acts on what carrier, under which conditions, through
which observable map and protocol, in which physical realization?

### Transformation View

Connects two identities by stating the clause that changes and the relation that
is retained:

```text
source identity -> controlled constructor edit -> target identity -> consequence
```

It answers: what can be completed, reattached, composed, deformed, observed, or
revised?

### Evidence View

Retains source passages, equations, citations, historical names, implementation
details, and empirical results. It answers: where does each clause come from and
how can it be checked?

## Required Page Content

A public mechanism page contains:

1. familiar title and source description;
2. operation `Omega`;
3. carrier `Xi`;
4. closure `C`;
5. observable or prediction map `R`;
6. protocol `P`;
7. realization `A`;
8. representative equations;
9. transformations to neighboring identities;
10. the relation retained by each transformation;
11. a derived observable consequence or a precise unresolved clause;
12. source links and equation witnesses.

Not every source states every clause in one equation. A page may assemble a
mechanism from neighboring equations in the same source, provided the assembly
and its dependencies remain visible.

## Field-Level Organization

The upper-level contract is shared across fields. The contents of its clauses
are field-specific and must be recovered from the corpus. A quantum carrier may
be a Hilbert or Fock space; a materials carrier may be an interface, lattice, or
microstructure; a biological carrier may be a population, regulatory state, or
spatial tissue domain. The notation is common, but the admissibility conditions
and executable protocols are not interchangeable.

The field index groups topics by the clause they specify and the transformations
they support. It does not require a single linear constructor spine.

## Cross-Field Construction

A cross-field link must state:

```text
retained operation or relation
source carrier and target carrier
new closure requirements
new observable map and protocol
physical realization
consequence that can fail
```

Shared terminology, nearby embeddings, and similar equation shapes can nominate
a comparison. They cannot establish the transfer.

## Reproduction Contract

The repository must preserve the input manifest, source identifiers, extracted
equations, constructor assignments, generated pages, transformation records,
book source, and build checks. The public exposition may omit internal
diagnostics, but the reproducibility artifacts remain available.
