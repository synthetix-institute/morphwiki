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


BUILD_V2_EVIDENCE_INDEX="${MORPHWIKI_BUILD_V2_EVIDENCE_INDEX:-auto}"
if [[ -n "${MORPHWIKI_V2_ROOT:-}" ]]; then
  V2_ROOT="$MORPHWIKI_V2_ROOT"
elif [[ -d "../tm" ]]; then
  V2_ROOT="../tm"
elif [[ -d "../goidanich/tm" ]]; then
  V2_ROOT="../goidanich/tm"
else
  V2_ROOT=""
fi
if [[ "$BUILD_V2_EVIDENCE_INDEX" != "0" && "$BUILD_V2_EVIDENCE_INDEX" != "false" && -n "$V2_ROOT" && -d "$V2_ROOT" ]]; then
  export MORPHWIKI_V2_EVIDENCE_INDEX_JSON="${MORPHWIKI_V2_EVIDENCE_INDEX_JSON:-$ROOT/v2_quantum_evidence_index.json}"
  echo "[MorphWiki] building V2 evidence index from $V2_ROOT"
  evidence_args=()
  if [[ -n "${MORPHWIKI_V2_SOURCE_CARD_ALIGNMENT_JSONL:-}" ]]; then
    evidence_args+=(--source-card-alignment-jsonl "$MORPHWIKI_V2_SOURCE_CARD_ALIGNMENT_JSONL")
  fi
  if [[ -n "${MORPHWIKI_V2_SOURCE_CARDS_JSONL:-}" ]]; then
    evidence_args+=(--source-cards-jsonl "$MORPHWIKI_V2_SOURCE_CARDS_JSONL")
  fi
  "$PYTHON_BIN" -B scripts/build_morphwiki_v2_quantum_evidence_index.py \
    --root "$ROOT" \
    --v2-root "$V2_ROOT" \
    --out-json "$MORPHWIKI_V2_EVIDENCE_INDEX_JSON" \
    --out-md "${MORPHWIKI_V2_EVIDENCE_INDEX_MD:-$ROOT/v2_quantum_evidence_index.md}" \
    "${evidence_args[@]}"
  "$PYTHON_BIN" -B scripts/audit_morphwiki_v2_quantum_evidence_index.py \
    --index "$MORPHWIKI_V2_EVIDENCE_INDEX_JSON" \
    --tree "$ROOT/quantum_mechanism_tree.json" \
    --out-json "${MORPHWIKI_V2_EVIDENCE_INDEX_AUDIT_JSON:-$ROOT/v2_quantum_evidence_index_audit.json}" \
    --out-md "${MORPHWIKI_V2_EVIDENCE_INDEX_AUDIT_MD:-$ROOT/v2_quantum_evidence_index_audit.md}"
fi

if [[ -n "$V2_ROOT" && -d "$V2_ROOT" ]]; then
  V2_DAG_JSON="${MORPHWIKI_V2_DAG_JSON:-$(find "$V2_ROOT" -maxdepth 1 -type f -name '*v2_dag.json' -print -quit)}"
  V2_GRAMMAR_JSON="${MORPHWIKI_V2_GRAMMAR_RULES_JSON:-$(find "$V2_ROOT" -maxdepth 1 -type f -name '*grammar_rule_learner.json' -print -quit)}"
  V2_SOURCE_CONSTRUCTOR="${MORPHWIKI_V2_SOURCE_CONSTRUCTOR:-$(find "$V2_ROOT" -maxdepth 1 -type f \( -name '*source_constructor_graph.json' -o -name '*source_constructor_graph.md' \) -print -quit)}"
  if [[ -n "$V2_DAG_JSON" && -n "$V2_GRAMMAR_JSON" && -n "$V2_SOURCE_CONSTRUCTOR" ]]; then
    echo "[MorphWiki] deriving constructor dependencies"
    "$PYTHON_BIN" -B scripts/analyze_quantum_constructor_dependencies.py \
      --dag-json "$V2_DAG_JSON" \
      --grammar-json "$V2_GRAMMAR_JSON" \
      --source-constructor "$V2_SOURCE_CONSTRUCTOR" \
      --out-json "$ROOT/quantum_constructor_dependencies.json" \
      --out-md "$ROOT/quantum_constructor_dependencies.md"
  fi
fi

echo "[MorphWiki] refreshing explicit topic-native page models"
"$PYTHON_BIN" -B scripts/rewrite_morphwiki_quantum_public_language.py \
  --pages-dir "$ROOT/pages" \
  --only-overrides
"$PYTHON_BIN" -B scripts/rewrite_morphwiki_quantum_public_language.py \
  --pages-dir "$ROOT/pages" \
  --render-only

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
if [[ -n "${MORPHWIKI_V2_EVIDENCE_INDEX_JSON:-}" ]]; then
  tree_args+=(--v2-evidence-index-json "$MORPHWIKI_V2_EVIDENCE_INDEX_JSON")
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

echo "[MorphWiki] deriving testable cross-topic rewiring candidates"
"$PYTHON_BIN" -B scripts/analyze_quantum_constructor_rewiring.py \
  --root "$ROOT" \
  --out-json "$ROOT/quantum_constructor_rewiring.json" \
  --out-md "$ROOT/quantum_constructor_rewiring.md"

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

echo "[MorphWiki] auditing content preservation"
"$PYTHON_BIN" -B scripts/audit_quantum_book_content_preservation.py \
  --root "$ROOT" \
  --contract "$OUT_DIR/quantum_book_content_contract.json" \
  --tex "$TEX" \
  --pdf "$PDF" \
  --out-json "$OUT_DIR/quantum_book_content_preservation_audit.json" \
  --out-md "$OUT_DIR/quantum_book_content_preservation_audit.md"

echo "[MorphWiki] done: $PDF"
