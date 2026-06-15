# MorphWiki: Knowledge Without Nouns

**A GitHub repository where physics compiles.**

MorphWiki is an operator-native rewrite system for scientific knowledge. It takes
historical prose, such as Wikipedia physics pages, and rewrites it as typed
mechanism constructors: state, carrier, operator, spectrum, boundary, readout,
compatibility, protocol, and commutator.

The first public build produces a quantum-theory book:

```text
Quantum Theory
As A Mechanism Tree
```

The point is not to summarize quantum mechanics. The point is to reorganize it:
not by nouns such as `electron`, `photon`, `wavefunction`, or `measurement`, but
by the operations that make those concepts predictive.

## Why This Exists

Most scientific search tools compare words. MorphWiki compares operational
roles.

Wikipedia says what a concept is called. MorphWiki asks what the concept does in
a construction:

```text
context
  -> admissible state space
  -> generator or evolution law
  -> observable spectrum
  -> probability readout
  -> compatibility constraint
  -> boundary or protocol realization
```

That sequence is a computable object. A young researcher can inspect it, edit
it, rerun it, and ask whether a topic is a stable constructor, an overloaded
junction, an unresolved placement, or a missing equation.

## What You Can Do With It

- Build a mechanism-first PDF book for quantum theory.
- Convert topic pages into a typed constructor tree.
- Link topics to public Hyperion equation witnesses and arXiv sources.
- Run sparse-attention analysis over the rewritten corpus.
- Detect overloaded concepts, weakly constructed pages, and missing mechanisms.
- Use the code as a template for another field: statistical mechanics, active
  matter, biological intelligence, materials, patents, or AI safety.

## Quick Start

The core pipeline uses only the Python standard library. A LaTeX engine is
optional and is needed only to compile the generated `.tex` into PDF.

```bash
git clone https://github.com/synthetix-institute/morphwiki.git
cd morphwiki

bash scripts/run_quantum_book.sh
```

Outputs are written to:

```text
discoveries/morphwiki_quantum/book/
```

The important files are:

```text
quantum_mechanism_tree_book.tex   # generated LaTeX book
quantum_mechanism_tree_book.pdf   # generated when xelatex/lualatex is present
```

For a step-by-step guide, see [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md).

## Repository Map

```text
scripts/export_morphwiki_topic_index.py
    Fetch or read cached Wikipedia pages, score mechanism roles, attach
    Hyperion witnesses, and write per-topic JSON/Markdown.

scripts/build_morphwiki_quantum_tree.py
    Place topic pages into the mechanism tree.

scripts/analyze_morphwiki_rewrite_transition.py
    Run sparse-attention analysis over the rewrite and report hidden rules,
    overloaded pages, anomalies, and unresolved placements.

scripts/build_morphwiki_quantum_book.py
    Compile the topic pages, tree, and analysis into a LaTeX book.

scripts/run_quantum_book.sh
    Run the local quantum-book pipeline.

discoveries/fieldbridge_static_index/hyperion_static_index.json
    Compact public Hyperion witness index with route/fiber profiles, apparatus
    labels, arXiv links, and sanitized equation-witness snippets.

discoveries/morphwiki_quantum/
    Cached/generated quantum pages, sparse-attention outputs, mechanism tree,
    and current TeX/PDF book outputs.
```

## Rebuild Topic Pages

The repo includes cached data, so the book can be rebuilt offline. To refetch
Wikipedia and rebuild topic pages, run:

```bash
python -B scripts/export_morphwiki_topic_index.py \
  --topic-preset quantum \
  --expand-wikipedia-links \
  --max-expanded-topics 160 \
  --hyperion-index discoveries/fieldbridge_static_index/hyperion_static_index.json \
  --out-dir discoveries/morphwiki_quantum
```

Optional OpenRouter variables:

```text
OPENROUTER_API_KEY=
HYPERION_MODEL=
MORPHWIKI_MODEL=
```

The deterministic pipeline works without an LLM. If an LLM is enabled, it should
only rewrite prose from the same structured payload; it should not invent
evidence.

## Scientific Boundary

MorphWiki is not a replacement for a textbook and not a claim that physics is
reducible to a short word list. It tests a narrower claim: when scientific pages
are represented by operational roles and equation-witness profiles, many named
topics collapse into a smaller constructor sequence. The useful output is the
map of what is stable, what is overloaded, and what still lacks explicit
equation-level construction.

## For Contributors

Start with [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md), then read
[docs/METHOD.md](docs/METHOD.md). A good contribution adds one of three things:

1. A cleaner mechanism placement for a topic.
2. A better equation witness or arXiv link.
3. A new field preset that can be rebuilt reproducibly.

Broader Hyperion and FieldBridge work is maintained by Synthetix Institute:
https://synthetix.institute
