# Build an isolated copy of the quantum book

A tutorial build should leave the current book and its source records available
for comparison. The book generator writes both LaTeX and individual topic
pages, so changing only its PDF directory is insufficient. Use a separate
source copy and set both output destinations.

## Make a separate build

The following copy deliberately fails if the destination already exists.
Choose a new directory for another attempt rather than overlaying a previous
comparison.

```bash
python3 - <<'PY'
import shutil

shutil.copytree(
    'discoveries/morphwiki_quantum', 'build/tutorial_quantum_source',
    ignore=shutil.ignore_patterns('*.jsonl', '*.npy', '*.npz',
                                 'book', 'derivation_pages', 'wiki_cache'))
PY

python3 -B scripts/revalidate_quantum_evidence_index.py \
  --index build/tutorial_quantum_source/v2_quantum_evidence_index.json \
  --out-json build/tutorial_quantum_source/v2_quantum_evidence_index.json \
  --out-md build/tutorial_quantum_source/v2_quantum_evidence_index.md

python3 -B scripts/build_morphwiki_quantum_tree.py \
  --root build/tutorial_quantum_source

mkdir -p build/tutorial_quantum_book
python3 -B scripts/build_morphwiki_quantum_book.py \
  --root build/tutorial_quantum_source \
  --out-dir build/tutorial_quantum_book \
  --pages-out-dir build/tutorial_quantum_pages \
  > build/tutorial_quantum_book/build_report.json
```

The outputs are a TeX manuscript under `build/tutorial_quantum_book/` and
explanatory pages under `build/tutorial_quantum_pages/`. Their source is the
copied cached input tree. The detailed builder report
is saved to `build/tutorial_quantum_book/build_report.json` rather than printed
as hundreds of page records. The copy keeps the cached
page records and JSON summaries, while omitting raw alignment streams,
matrices and previous rendered files. This run renders cached evidence; the
full source-grounding build is described below. Revalidation retains rejected
candidates and their reasons in the copied index.
The copy also retains `original_source_relations.json`. Those independently
inspected arXiv displays supply original-paper links with their own alignment
status. [The recovery tutorial](12_original_sources.md)
explains how to reproduce them from the articles.

With a TeX installation that provides `latexmk` and `pdflatex`:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build/tutorial_quantum_book \
  build/tutorial_quantum_book/quantum_mechanism_tree_book.tex
```

The production wrapper also supports direct `pdflatex`, `xelatex` and
`lualatex` fallbacks. No TeX engine is needed for the separate
[calculation companion](10_submission_companion.md).

## Check content and sources separately

Compare the developed topic sections and equations with the original. Count
name-only index entries separately from full explanations.
Inspect the generated `manifest.json` in the topic-page directory and the
book's source-coverage account.

The [content checker](../../scripts/audit_quantum_book_content_preservation.py)
and [source checker](../../scripts/audit_morphwiki_v2_quantum_evidence_index.py)
answer different questions. The content checker tracks developed treatments;
the source checker tracks equation witnesses. Derivations and executable
checks establish the mathematical claims in those treatments.

The rewrite-analysis script
[analyze_morphwiki_rewrite_transition.py](../../scripts/analyze_morphwiki_rewrite_transition.py)
helps locate weak or overloaded pages. Its scores prioritize inspection of
the physical derivations.

## When to use the full V2.1 build

On a machine with the source cards and alignment artifacts, the production job is:

```bash
KNOWLEDGE_PARSER_DISCOVERIES=/path/to/KnowledgeParser/discoveries \
  bash scripts/run_quantum_book_v21_full.sh
```

This is a full rebuild in the repository's configured output locations, unlike
the isolated tutorial commands. Use it when intentionally updating the book's
source grounding. Keep its book, evidence index and reports together when
copying the result from a cluster.

[Next: another field](06_new_field.md) · [Tutorial](index.md)
