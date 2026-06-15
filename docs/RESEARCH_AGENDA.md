# Research Agenda

MorphWiki is a small public test of a larger claim: scientific knowledge can be
organized by transformations rather than by nouns.

## Core Research Question

Can a scientific field be rewritten as a typed constructor system?

For quantum theory, the proposed constructor sequence is:

```text
context
-> admissible state space
-> generator/evolution
-> observable spectrum
-> probability readout
-> compatibility constraint
-> boundary/protocol realization
```

This is useful only if it does real work. It should make the field easier to
audit, compare, extend, or mechanize.

## What Would Count As Progress

### 1. Better topic placement

Weak placement means a topic can be named but not mechanistically located.
Progress means the page now has a clear role:

```text
carrier
operator
spectrum
readout
boundary
compatibility
protocol
```

### 2. Better construction

Weak construction means the page has prose but no equation-level spine. Progress
means the page names:

```text
state space
operator or generator
domain or boundary condition
readout rule
compatibility constraint
```

### 3. Better anomaly explanations

Bad anomaly labels are generic. Good anomaly labels say what fails:

```text
the spectrum is present but no operator is named
the protocol is doing the work of a missing dynamics
the boundary changes the admissible state space
the same page mixes state, readout, and interpretation
```

### 4. Better cross-field tests

The long-term goal is to compare mechanisms across fields. A useful analogy is
not a shared word. It is a shared role contract:

```text
same operator/readout/closure role
different substrate or realization
compatible boundary/protocol conditions
```

## Good First Projects

1. Improve the Hilbert-space chapter so it explains why Hilbert space is the
   selector/carrier layer for quantum theory.
2. Split overloaded topics such as measurement, interpretation, and quantum
   information into smaller constructor roles.
3. Add explicit equations to pages that currently have only placement evidence.
4. Add a second field preset and compare its constructor tree with quantum
   theory.
5. Build a small web viewer for the mechanism tree.

## What Not To Do

Do not turn MorphWiki into an LLM summary generator. The goal is not smoother
prose. The goal is a stricter representation of scientific mechanisms.

Do not hide unresolved pages. They are often the most useful output: they show
where a field has names without enough explicit construction evidence.

