#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KP_DISCOVERIES="${KNOWLEDGE_PARSER_DISCOVERIES:-$REPO_ROOT/../KnowledgeParser/discoveries}"
ALIGNMENT="${MORPHWIKI_V2_SOURCE_CARD_ALIGNMENT_JSONL:-$KP_DISCOVERIES/operator_substrate_v2_full_v21_source_card_alignment.jsonl}"
CARDS="${MORPHWIKI_V2_SOURCE_CARDS_JSONL:-$KP_DISCOVERIES/source_equation_cards_full_v21.jsonl}"

for path in "$KP_DISCOVERIES" "$ALIGNMENT" "$CARDS"; do
  if [[ ! -e "$path" ]]; then
    echo "Required V2.1 artifact is missing: $path" >&2
    exit 2
  fi
done

export MORPHWIKI_BUILD_V2_EVIDENCE_INDEX="${MORPHWIKI_BUILD_V2_EVIDENCE_INDEX:-1}"
export MORPHWIKI_V2_ROOT="$KP_DISCOVERIES"
export MORPHWIKI_V2_SOURCE_CARD_ALIGNMENT_JSONL="$ALIGNMENT"
export MORPHWIKI_V2_SOURCE_CARDS_JSONL="$CARDS"
export MORPHWIKI_V2_EVIDENCE_INDEX_JSON="${MORPHWIKI_V2_EVIDENCE_INDEX_JSON:-$REPO_ROOT/discoveries/morphwiki_quantum/v2_quantum_evidence_index.json}"

cd "$REPO_ROOT"
exec bash scripts/run_quantum_book.sh
