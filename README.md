# MorphWiki: Scientific Fields By Mechanism

MorphWiki rebuilds a scientific field around the mechanisms that make its
theories predictive. Familiar names remain searchable, and their sources remain
attached, but they no longer determine the structure of the field.

![MorphWiki mechanism-construction workflow](docs/assets/morphwiki-operator-native-physics.svg)

The shared representation is

```text
(Omega, Xi) -> M -> I_op=(M; C, R, P) -> I_real=(I_op; A)
```

- `Omega` is the operation: generator, observable, channel, projection, symmetry
  action, or composition.
- `Xi` is its carrier: state space, domain, substrate, factorization, or algebra.
- `C`, `R`, and `P` are closure, observable map, and protocol.
- `A` is the realization: named objects, parameters, units, boundaries, geometry,
  apparatus, and experimental conditions.

The clauses are addressable but not freely interchangeable. A proposed change
must state what relation is retained, why the new clauses are compatible, and
which consequence can reject the construction.

## Quantum Theory: As A Mechanism Tree

The first complete build is a mechanism-first quantum theory book. It keeps the
full topic archive while reorganizing the exposition into five parts:

```text
carrier and states
operations
completion
realizations and extensions
provenance and interpretations
```

The opening chapters derive the quantum operational identity, show standard
mechanism-preserving transformations, and turn six constructor verbs into a
procedure for discovery:

```text
complete    add a missing closure, observable map, or protocol
reattach    replace an operation or carrier under stated compatibility maps
compose     join supported transformations in a new order
deform      vary a boundary, parameter, scale, or representation
observe     construct a discriminating observable or measurement
revise      replace the clause identified by a failed consequence
```

Current book:
[Quantum Theory: As A Mechanism Tree](discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.pdf)

## Why A Mechanism Wiki

Conventional encyclopedias are organized around objects, discoveries, people,
and established field boundaries. That organization is useful for finding a
name. It is less useful for answering four constructive questions:

1. What operation produces the claimed consequence?
2. On what carrier is that operation defined?
3. Which closure, observable map, and protocol make the mechanism predictive?
4. Which parts can change while a specified prediction remains invariant?

MorphWiki answers those questions without discarding provenance. Topic names and
historical vocabulary enter through the realization and evidence layers. The
operational graph supplies a second, mechanism-first view of the same field.

## Quick Start

The deterministic build uses the Python standard library. XeLaTeX or LuaLaTeX
is required only for the PDF.

```bash
git clone https://github.com/synthetix-institute/morphwiki.git
cd morphwiki
bash scripts/run_quantum_book.sh
```

Outputs are written to:

```text
discoveries/morphwiki_quantum/book/
```

Sparse-attention and build diagnostics remain separate repository artifacts.
They inform the field structure and candidate connections but are not chapters
in the PDF.

## Build A Field Wiki From Papers

MorphWiki can start from a folder containing text-layer PDFs, TeX, Markdown, or
plain-text papers. The FieldBridge-backed workflow retains source passages and
equations while producing synchronized topic, mechanism, transformation, and
evidence views.

See [Build A Mechanism-First Field Wiki From PDFs](docs/PDF_CORPUS_WORKFLOW.md)
and [Getting Started](docs/GETTING_STARTED.md).

## Repository Map

```text
scripts/morphwiki_constructor.py
    Shared constructor clauses, discovery verbs, and book grouping.

scripts/export_morphwiki_topic_index.py
    Build source-grounded topic records and equation-witness links.

scripts/build_morphwiki_quantum_tree.py
    Place quantum topics in the operational identity and write the public map.

scripts/analyze_quantum_constructor_rewiring.py
    Derive worked mechanism-preserving transformations across quantum topics.

scripts/build_morphwiki_quantum_book.py
    Generate the complete LaTeX book and optional method appendices.

scripts/run_quantum_book.sh
    Rebuild the tree, transformation cases, book, PDF, and preservation report.

discoveries/morphwiki_quantum/
    Topic records, equation witnesses, mechanism map, derivation pages, and book.
```

## Adapt The Constructor To Another Field

A new field uses the same upper-level identity but supplies its own operations,
carriers, closure conditions, observables, protocols, and realizations. The field
structure must be inferred from its equations and source-local transformations,
not produced by renaming quantum terms.

```text
1. Ingest the field corpus and retain source identity.
2. Extract candidate operation, carrier, completion, and realization clauses.
3. Group topics by the clauses they specify.
4. Recover transformations and state what each one preserves.
5. Write topic pages as realized operational identities.
6. Generate discovery questions by controlled clause edits.
7. Derive and test the consequences of the proposed constructions.
```

The formal contract is in
[FIELD_WIKI_CONTRACT.md](docs/FIELD_WIKI_CONTRACT.md). The worked tutorial starts
at [Building A Mechanism-First Field Wiki](docs/tutorial/index.md).

## Contribution Standard

A useful contribution does at least one of the following:

1. supplies a topic-native equation and identifies its constructor clauses;
2. states a mechanism-preserving transformation and its retained relation;
3. adds a physically executable realization and a discriminating consequence;
4. builds another field from a reproducible source corpus.

Broader Hyperion and FieldBridge work is maintained by the
[Synthetix Institute](https://synthetix.institute).
