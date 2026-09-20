"""Validate published original-display records without treating them as V2 cards."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

try:
    from quantum_source_evidence import canonical_arxiv_id, equation_issues
except ModuleNotFoundError:
    from scripts.quantum_source_evidence import canonical_arxiv_id, equation_issues


def validate_report(report: dict) -> list[str]:
    errors = []
    if report.get("failures"):
        errors.append("source recovery contains failed selections")
    seen = set()
    for record in report.get("records", []):
        topic, paper, location = (record.get(k, "") for k in ("topic", "paper_id", "display_id"))
        key = (topic, paper, location)
        if key in seen:
            errors.append(f"duplicate original display: {key}")
        seen.add(key)
        expected_url = f"https://arxiv.org/html/{paper}#{location}"
        equation = record.get("equation_latex", "")
        if not topic or not location or not paper or canonical_arxiv_id(paper) != paper:
            errors.append(f"invalid original display identity: {key}")
        if record.get("url") != expected_url:
            errors.append(f"original display URL mismatch: {key}")
        if equation_issues(equation):
            errors.append(f"incomplete original display: {key}")
        if hashlib.sha256(equation.encode()).hexdigest() != record.get("equation_sha256"):
            errors.append(f"original equation hash mismatch: {key}")
        document = report.get("documents", {}).get(paper, {})
        if document.get("sha256") != record.get("document_sha256"):
            errors.append(f"document identity mismatch: {key}")
        for field in ("context_sha256", "document_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", record.get(field, "")):
                errors.append(f"missing {field}: {key}")
        if not record.get("relation") or not record.get("scope"):
            errors.append(f"missing mathematical relevance or assumptions: {key}")
        if (record.get("source_origin") != "original_arxiv_html"
                or record.get("v2_card_alignment") != "not_established"):
            errors.append(f"unsupported source-card alignment: {key}")
    if report.get("topic_count") != len({r.get("topic") for r in report.get("records", [])}):
        errors.append("original source topic count mismatch")
    return errors


def load_original_sources(root: Path) -> dict:
    path = root / "original_source_relations.json"
    if not path.exists():
        return {"records": [], "documents": {}, "topic_count": 0}
    report = json.loads(path.read_text())
    errors = validate_report(report)
    if errors:
        raise ValueError("; ".join(errors))
    return report
