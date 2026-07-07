#!/usr/bin/env bash
set -euo pipefail

ROOT="${MORPHWIKI_ROOT:-discoveries/morphwiki_quantum}"
OUT_DIR="${MORPHWIKI_OUT_DIR:-$ROOT/book}"
PYTHON_BIN="${PYTHON_BIN:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python >/dev/null 2>&1; then
    PYTHON_BIN=python
  else
    PYTHON_BIN=python3
  fi
fi

echo "[MorphWiki] building mechanism tree"
tree_args=()
if [[ -n "${MORPHWIKI_V2_LANGUAGE_JSON:-}" ]]; then
  tree_args+=(--v2-language-json "$MORPHWIKI_V2_LANGUAGE_JSON")
fi
if [[ -n "${MORPHWIKI_V2_GRAMMAR_RULES_JSON:-}" ]]; then
  tree_args+=(--v2-grammar-rules-json "$MORPHWIKI_V2_GRAMMAR_RULES_JSON")
fi
if [[ -n "${MORPHWIKI_V2_SOURCE_LANGUAGE_EXAMPLES_JSON:-}" ]]; then
  tree_args+=(--v2-source-examples-json "$MORPHWIKI_V2_SOURCE_LANGUAGE_EXAMPLES_JSON")
fi
if ((${#tree_args[@]})); then
  "$PYTHON_BIN" -B scripts/build_morphwiki_quantum_tree.py \
    --root "$ROOT" \
    "${tree_args[@]}"
else
  "$PYTHON_BIN" -B scripts/build_morphwiki_quantum_tree.py \
    --root "$ROOT"
fi

echo "[MorphWiki] running sparse-attention rewrite analysis"
"$PYTHON_BIN" -B scripts/analyze_morphwiki_rewrite_transition.py \
  --root "$ROOT"

echo "[MorphWiki] building LaTeX book"
"$PYTHON_BIN" -B scripts/build_morphwiki_quantum_book.py \
  --root "$ROOT" \
  --out-dir "$OUT_DIR"

TEX="$OUT_DIR/quantum_mechanism_tree_book.tex"
PDF="$OUT_DIR/quantum_mechanism_tree_book.pdf"

if command -v latexmk >/dev/null 2>&1 && command -v xelatex >/dev/null 2>&1; then
  echo "[MorphWiki] compiling PDF with latexmk/xelatex"
  latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir="$OUT_DIR" "$TEX"
elif command -v xelatex >/dev/null 2>&1; then
  echo "[MorphWiki] compiling PDF with xelatex"
  xelatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT_DIR" "$TEX"
  xelatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT_DIR" "$TEX"
elif command -v lualatex >/dev/null 2>&1; then
  echo "[MorphWiki] compiling PDF with lualatex"
  lualatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT_DIR" "$TEX"
  lualatex -interaction=nonstopmode -halt-on-error -output-directory "$OUT_DIR" "$TEX"
elif command -v pdflatex >/dev/null 2>&1; then
  echo "[MorphWiki] pdflatex found, but this book uses fontspec and requires xelatex or lualatex; TeX written to $TEX"
  exit 0
else
  echo "[MorphWiki] no LaTeX engine found; TeX written to $TEX"
  exit 0
fi

echo "[MorphWiki] done: $PDF"
