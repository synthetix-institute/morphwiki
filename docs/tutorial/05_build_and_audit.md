# Rebuild without replacing the current book

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

python3 -B scripts/build_morphwiki_quantum_book.py \
  --root build/tutorial_quantum_source \
  --out-dir build/tutorial_quantum_book \
  --pages-out-dir build/tutorial_quantum_pages
```

The outputs are a TeX manuscript under `build/tutorial_quantum_book/` and
explanatory pages under `build/tutorial_quantum_pages/`. Their source is the
copied input tree, not a newly downloaded corpus. The copy keeps the cached
page records and JSON summaries, while omitting raw alignment streams,
matrices and previous rendered files. This is a rendering exercise from
cached evidence, not a new source-grounding run.
Revalidation retains rejected candidates in the copied index; it does not
invent replacements for incomplete or irrelevant source equations.
The copy also retains `original_source_relations.json`. Those independently
inspected arXiv displays supply separate original-paper links, without changing
the corpus-alignment status. [The recovery tutorial](12_original_sources.md)
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

Compare topic sections and equations with the original, not only PDF page
count. A list of topic names is not a replacement for their explanations.
Inspect the generated `manifest.json` in the topic-page directory and the
book's source-coverage account.

The [content checker](../../scripts/audit_quantum_book_content_preservation.py)
and [source checker](../../scripts/audit_morphwiki_v2_quantum_evidence_index.py)
answer different questions. A readable, complete PDF can still lack confirmed
equation witnesses. A well-sourced page can still omit the explanation linking
its equations. Mathematical correctness requires an additional derivation
or executable check.

The rewrite-analysis script
[analyze_morphwiki_rewrite_transition.py](../../scripts/analyze_morphwiki_rewrite_transition.py)
helps locate weak or overloaded pages. Its scores prioritize inspection; they
do not establish that a physical explanation is correct.

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
