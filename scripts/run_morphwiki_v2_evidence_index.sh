#!/usr/bin/env bash
set -euo pipefail
ROOT="${MORPHWIKI_ROOT:-discoveries/morphwiki_quantum}"
PYTHON_BIN="${PYTHON_BIN:-}"
if [[ -z "$PYTHON_BIN" ]]; then
  if command -v python >/dev/null 2>&1; then PYTHON_BIN=python; else PYTHON_BIN=python3; fi
fi
if [[ -n "${MORPHWIKI_V2_ROOT:-}" ]]; then V2_ROOT="$MORPHWIKI_V2_ROOT"; elif [[ -d "../tm" ]]; then V2_ROOT="../tm"; elif [[ -d "../goidanich/tm" ]]; then V2_ROOT="../goidanich/tm"; else V2_ROOT="$ROOT/v2_language"; fi
OUT_JSON="${MORPHWIKI_V2_EVIDENCE_INDEX_JSON:-$ROOT/v2_quantum_evidence_index.json}"
OUT_MD="${MORPHWIKI_V2_EVIDENCE_INDEX_MD:-$ROOT/v2_quantum_evidence_index.md}"
AUDIT_JSON="${MORPHWIKI_V2_EVIDENCE_INDEX_AUDIT_JSON:-$ROOT/v2_quantum_evidence_index_audit.json}"
AUDIT_MD="${MORPHWIKI_V2_EVIDENCE_INDEX_AUDIT_MD:-$ROOT/v2_quantum_evidence_index_audit.md}"
TREE_JSON="${MORPHWIKI_TREE_JSON:-$ROOT/quantum_mechanism_tree.json}"
if [[ ! -d "$V2_ROOT" ]]; then echo "[MorphWiki] V2 root not found: $V2_ROOT" >&2; exit 2; fi
echo "[MorphWiki] building V2 quantum evidence index from $V2_ROOT"
if (($#)); then
  "$PYTHON_BIN" -B scripts/build_morphwiki_v2_quantum_evidence_index.py --root "$ROOT" --v2-root "$V2_ROOT" --out-json "$OUT_JSON" --out-md "$OUT_MD" "$@"
else
  "$PYTHON_BIN" -B scripts/build_morphwiki_v2_quantum_evidence_index.py --root "$ROOT" --v2-root "$V2_ROOT" --out-json "$OUT_JSON" --out-md "$OUT_MD"
fi
echo "[MorphWiki] auditing V2 quantum evidence index"
"$PYTHON_BIN" -B scripts/audit_morphwiki_v2_quantum_evidence_index.py --index "$OUT_JSON" --tree "$TREE_JSON" --out-json "$AUDIT_JSON" --out-md "$AUDIT_MD"
echo "[MorphWiki] evidence index: $OUT_JSON"
