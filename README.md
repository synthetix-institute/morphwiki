# MorphWiki: Knowledge Without Nouns

MorphWiki is a public, reproducible companion to the Hyperion project.  It tests a specific claim: a scientific subject can be reorganized by the operations that make its statements predictive, rather than by the historical nouns used to name the subject.

The first release builds a mechanism-first book for quantum theory.  It starts from Wikipedia topic scaffolds and a compact exported Hyperion witness index, places each topic into an operational tree, and compiles a PDF called **Quantum Theory: As A Mechanism Tree**.

## Core Idea

Conventional encyclopedias organize knowledge by names: electron, wavefunction, Hilbert space, measurement, photon, string theory.  MorphWiki instead asks what each topic does in a construction:

```text
context -> admissible state space -> generator/evolution
        -> observable spectrum -> probability readout
        -> compatibility constraint -> boundary/protocol realization
```

The result is not a replacement for a textbook.  It is a different index over the same scientific material.  The central unit is a mechanism role: carrier, operator, spectrum, readout, boundary, compatibility, or protocol.

## What This Repo Contains

- `scripts/export_morphwiki_topic_index.py`  
  Fetches or reads cached Wikipedia pages, scores route/fiber profiles, links pages to Hyperion equation witnesses, and writes per-topic MorphWiki JSON/Markdown pages.

- `scripts/build_morphwiki_quantum_tree.py`  
  Converts topic pages into a mechanism tree for quantum theory.

- `scripts/analyze_morphwiki_rewrite_transition.py`  
  Runs sparse-attention analysis over the rewrite to identify dominant roles, hidden rules, anomalies, and unresolved placements.

- `scripts/build_morphwiki_quantum_book.py`  
  Builds the LaTeX source for the book and writes derivation pages.

- `discoveries/fieldbridge_static_index/hyperion_static_index.json`  
  Compact public witness index exported from Hyperion.  It contains route/fiber profiles, apparatus labels, arXiv links, and sanitized equation-witness snippets.

- `discoveries/morphwiki_quantum/`  
  Cached/generated quantum pages, sparse-attention outputs, mechanism tree, and current PDF/TeX book outputs.

## Quick Start

Generate the tree and LaTeX book from the included cached data:

```bash
python -B scripts/build_morphwiki_quantum_tree.py \
  --root discoveries/morphwiki_quantum

python -B scripts/analyze_morphwiki_rewrite_transition.py \
  --root discoveries/morphwiki_quantum

python -B scripts/build_morphwiki_quantum_book.py \
  --root discoveries/morphwiki_quantum \
  --out-dir discoveries/morphwiki_quantum/book
```

Or run the full local pipeline:

```bash
bash scripts/run_quantum_book.sh
```

The generated TeX appears at:

```text
discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex
```

If a LaTeX engine is available, the script also builds:

```text
discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.pdf
```

## Rebuilding Topic Pages

The repo includes cached Wikipedia topic data, so the book can be rebuilt without network access.  To refetch/rebuild topic pages, run:

```bash
python -B scripts/export_morphwiki_topic_index.py \
  --topic-preset quantum \
  --expand-wikipedia-links \
  --max-expanded-topics 160 \
  --hyperion-index discoveries/fieldbridge_static_index/hyperion_static_index.json \
  --out-dir discoveries/morphwiki_quantum
```

Optional OpenRouter support is available through:

```text
OPENROUTER_API_KEY=
HYPERION_MODEL=
MORPHWIKI_MODEL=
```

The deterministic generator works without an LLM.  LLM calls, when enabled, are used only to improve prose fields from the same mechanism/evidence payload.

## Scientific Boundary

MorphWiki does not claim that Wikipedia articles or quantum theory are reducible to a small list of words.  The claim is narrower and testable: when pages are represented by operational roles and witness profiles, many named topics collapse into a smaller constructor sequence.  The book therefore exposes where this compression is strong, where it fails, and which pages need explicit equations or better evidence.

## Project Link

This repository is designed to be public-facing.  The broader Hyperion atlas and FieldBridge work are maintained by Synthetix Institute: https://synthetix.institute

