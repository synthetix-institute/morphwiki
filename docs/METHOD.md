# Method: Mechanism-First Rewriting

MorphWiki separates two graphs that are usually merged in scientific prose.

1. **The provenance graph** stores where evidence came from: Wikipedia topic scaffolds, arXiv witness links, and Hyperion-exported equation witnesses.

2. **The operational graph** stores what a statement does: carrier, operator, spectrum, readout, boundary, compatibility, and protocol roles.

The quantum book is built from the second graph.  A topic such as `photon` is therefore not placed because it is a familiar object name.  It is placed by the role it plays in a construction: field mode, excitation, readout channel, scattering carrier, or boundary-dependent spectrum.

## Constructor Spine

The current quantum spine is:

```text
context
-> admissible Hilbert-space carrier
-> state
-> generator/evolution
-> observable spectrum
-> Born/probability readout
-> compatibility constraint
-> boundary or protocol realization
-> many-mode extension
```

This is not claimed as a new axiom system.  It is a compact index over the topic set.  Its value is diagnostic: it shows which pages are stable leaves, which are junctions, which are annotations, and which are unresolved because they lack explicit equation-level construction evidence.

## Evidence Use

The public witness index contains route and fiber profiles exported from Hyperion.  The scripts use these profiles to rank nearby equation witnesses and avoid pure semantic similarity.  A high-ranking witness is not treated as a proof that the Wikipedia topic is explained by that equation.  It is an evidence pointer indicating that a similar operational pattern exists in the arXiv-derived morphism index.

## Sparse-Attention Analysis

The sparse-attention script reads the generated pages and tree, then identifies:

- dominant constructor roles;
- repeated hidden rules;
- pages whose roles are overloaded;
- unresolved placements where the tree can place the topic but cannot yet construct it;
- transition rules introduced by rewriting the original topic index into the mechanism tree.

This is why the book distinguishes between placement and construction.  A page can be easy to place and still hard to construct if it lacks a clear carrier, operator, readout, or compatibility equation.

