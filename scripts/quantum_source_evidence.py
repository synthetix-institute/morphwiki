"""Conservative checks on recovered equation evidence, not a proof verifier.

Retrieval aliases are not public identifiers. A topic mention locates a candidate;
it does not establish the physical relation explained by a chapter.
"""
from __future__ import annotations

import re
from typing import Any, Mapping


def canonical_arxiv_id(value: Any) -> str:
    text = str(value or "").strip()
    text = re.sub(r"^https?://arxiv\.org/(?:abs|pdf)/", "", text, flags=re.I)
    text = re.sub(r"^arxiv:\s*", "", text, flags=re.I)
    text = re.sub(r"\.pdf$", "", text, flags=re.I)
    if re.fullmatch(r"\d{4}\.\d{4,5}(?:v\d+)?", text):
        return text
    old = re.fullmatch(r"([A-Za-z][A-Za-z.-]*?)/?(\d{7})(v\d+)?", text)
    if old:
        return f"{old[1]}/{old[2]}{old[3] or ''}"
    return ""


def equation_issues(value: Any) -> list[str]:
    """Reject truncated displays; passing is necessary, not semantic validation."""
    equation = str(value or "").strip()
    if not equation:
        return ["missing_equation"]
    issues = []
    depth = 0
    for match in re.finditer(r"(?<!\\)[{}]", equation):
        depth += 1 if match[0] == "{" else -1
        if depth < 0:
            break
    if depth:
        issues.append("unbalanced_braces")
    # Alignment separators and display-ending punctuation do not supply an operand.
    flat = re.sub(r"\\(?:label|tag)\{[^}]*\}", "", equation)
    flat = re.sub(r"\\[,;! ]|\\\\|&", "", flat).strip().rstrip(".,;").strip()
    relations = re.split(r"=|\\(?:leq?(?:slant)?|geq?(?:slant)?|neq?|equiv|in|sim|propto|mapsto)\b", flat)
    if len(relations) < 2:
        issues.append("missing_relation")
    elif not all(re.search(r"[A-Za-z0-9]", part) for part in relations):
        issues.append("missing_relation_operand")
    if re.search(r"[=+*/^_-]\s*$", flat):
        issues.append("truncated_expression")
    return issues


def evidence_issues(example: Mapping[str, Any]) -> list[str]:
    issues = equation_issues(example.get("equation_preview"))
    if not example.get("row_ids") or not example.get("card_ids"):
        issues.append("missing_exact_alignment")
    if not any(canonical_arxiv_id(p) for p in example.get("paper_ids", [])):
        issues.append("missing_public_paper_identifier")
    if not example.get("local_context"):
        issues.append("missing_source_context")
    if example.get("topic_relevance") != "local_context_match":
        issues.append("topic_not_located")
    if (example.get("relation_relevance") != "relation_context_match"
            or not example.get("relation_terms_matched")):
        issues.append("relation_not_established")
    return issues


def accepted_source_example(example: Mapping[str, Any]) -> bool:
    return not evidence_issues(example)
