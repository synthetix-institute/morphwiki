# Outputs

MorphWiki produces several layers of output. They should not be mixed.

## 1. Topic Pages

Location:

```text
discoveries/morphwiki_quantum/pages/
```

Purpose:

```text
Rewrite each source topic as a mechanism-bearing page.
```

Use these pages for human inspection. They are not the final analysis.

## 2. Mechanism Tree

Location:

```text
discoveries/morphwiki_quantum/mechanism_tree.json
```

Purpose:

```text
Place topics into a constructor sequence.
```

The current quantum sequence is:

```text
context
-> admissible state space
-> generator/evolution
-> observable spectrum
-> probability readout
-> compatibility constraint
-> boundary/protocol realization
```

This tree is the main object. It says how the field becomes navigable when it is
organized by operations rather than names.

## 3. Sparse-Attention Analysis

Location:

```text
discoveries/morphwiki_quantum/rewrite_transition_sparse_attention.json
discoveries/morphwiki_quantum/rewrite_transition_sparse_attention.md
```

Purpose:

```text
Analyze what changed when the topic set was rewritten as a mechanism tree.
```

The analysis should identify:

```text
dominant roles
hidden rules
overloaded pages
weak placements
unresolved construction targets
```

## 4. Book

Location:

```text
discoveries/morphwiki_quantum/book/
```

Purpose:

```text
Human-readable synthesis.
```

The `.tex` file is always generated. The `.pdf` file is generated only when a
compatible LaTeX engine exists locally.

## 5. Hyperion Witness Index

Location:

```text
discoveries/fieldbridge_static_index/hyperion_static_index.json
```

Purpose:

```text
Attach public equation-witness evidence to topic placements.
```

The witness index is not a proof that a topic is solved. It is an evidence
pointer: a nearby equation pattern exists in the exported Hyperion morphism
index.

## Reading The Outputs Correctly

Use this distinction:

```text
placement = the topic has a plausible role in the tree
construction = the topic has enough equation evidence to write the mechanism
validation = the mechanism has source evidence and falsifying checks
```

A page can be placed without being constructed. That is not a bug. It is a useful
diagnostic: the system has found where more equations or better evidence are
needed.

