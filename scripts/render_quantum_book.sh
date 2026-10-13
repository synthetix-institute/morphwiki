#!/usr/bin/env bash
set -euo pipefail

# Render the quantum book from cached material only: no source download, extraction or topic reassignment.
cd "$(dirname "${BASH_SOURCE[0]}")/.."
PYTHON_BIN="${PYTHON_BIN:-python3}"
ROOT="${MORPHWIKI_ROOT:-discoveries/morphwiki_quantum}"
OUT="${MORPHWIKI_OUT_DIR:-$ROOT/book}"
PAGES="${MORPHWIKI_PAGES_OUT_DIR:-$ROOT/derivation_pages}"

"$PYTHON_BIN" -B scripts/build_morphwiki_quantum_book.py \
  --root "$ROOT" --out-dir "$OUT" --pages-out-dir "$PAGES"
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir="$OUT" "$OUT/quantum_mechanism_tree_book.tex"

"$PYTHON_BIN" -B scripts/audit_quantum_book_content_preservation.py \
  --root "$ROOT" --contract "$ROOT/book/quantum_book_content_contract.json" \
  --tex "$OUT/quantum_mechanism_tree_book.tex" --pdf "$OUT/quantum_mechanism_tree_book.pdf" \
  --out-json "$OUT/quantum_book_content_preservation_audit.json" \
  --out-md "$OUT/quantum_book_content_preservation_audit.md"
"$PYTHON_BIN" -B scripts/audit_quantum_book_integrity.py \
  --root "$ROOT" --tex "$OUT/quantum_mechanism_tree_book.tex"
