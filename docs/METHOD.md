# Method

MorphWiki separates two graphs that are usually merged in scientific prose.

## 1. Provenance Graph

The provenance graph records where a statement came from:

```text
Wikipedia topic scaffold
arXiv source link
Hyperion equation witness
generated page
generated book section
```

This graph is about evidence and attribution. It does not decide what a concept
means.

## 2. Operational Graph

The operational graph records what a statement does in a construction:

```text
carrier
operator
spectrum
readout
boundary
compatibility
protocol
commutator
```

This graph is about mechanism. A topic such as `photon` is not placed because it
is a familiar noun. It is placed by the role it plays: field mode, excitation,
readout channel, scattering carrier, or boundary-dependent spectrum.

## 3. Constructor Spine

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

This is not claimed as a new axiom system. It is a compact index over the topic
set. Its value is diagnostic: it shows which pages are stable leaves, which are
junctions, which are annotations, and which are unresolved because they lack
explicit equation-level construction evidence.

## 4. Evidence Use

The public witness index contains route and fiber profiles exported from
Hyperion. The scripts use these profiles to rank nearby equation witnesses and
avoid pure semantic similarity.

A high-ranking witness is not treated as proof that the Wikipedia topic is
explained by that equation. It is an evidence pointer: a similar operational
pattern exists in the arXiv-derived morphism index.

## 5. Sparse-Attention Analysis

The sparse-attention script reads the generated pages and tree, then identifies:

- dominant constructor roles;
- repeated hidden rules;
- pages whose roles are overloaded;
- unresolved placements where the tree can place the topic but cannot yet construct it;
- transition rules introduced by rewriting the original topic index into the mechanism tree.

This is why the book distinguishes between placement and construction. A page can
be easy to place and still hard to construct if it lacks a clear carrier,
operator, readout, or compatibility equation.

## 6. Placement Versus Construction

MorphWiki uses three levels of claim strength.

```text
placement
    The topic has a plausible role in the constructor tree.

construction
    The topic has enough equation-level structure to state the mechanism.

validation
    The mechanism has source evidence, controls, and a falsifier.
```

Many current pages are placements. That is expected for a public first release.
The research task is to turn more placements into constructions by adding
equations, witnesses, and sharper role definitions.

## 7. Why This Is Useful

The method makes hidden weakness visible. A normal encyclopedia can describe a
topic fluently even when its operational role is unclear. MorphWiki should expose
that gap.

For example, a page is weak if it says `measurement` but does not state the
readout map, or says `state` but does not state the carrier space, or says
`incompatibility` but does not identify the non-commuting operations.

That is the intended discipline: no mechanism without roles; no role without
evidence.
