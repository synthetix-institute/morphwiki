#!/usr/bin/env python3
"""Recheck an existing export without inventing or re-extracting source evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

try:
    from quantum_source_evidence import canonical_arxiv_id, evidence_issues
except ModuleNotFoundError:
    from scripts.quantum_source_evidence import canonical_arxiv_id, evidence_issues


def revalidate(report: dict) -> dict:
    reasons = Counter()
    grounded = linked = 0
    for page in report.get("pages", {}).values():
        examples = []
        by_card = {}
        for source in page.get("source_examples", []):
            example = dict(source)
            example["paper_ids"] = sorted({canonical_arxiv_id(p) for p in example.get("paper_ids", [])} - {""})
            key = (tuple(example.get("paper_ids", [])), tuple(example.get("card_ids", [])), example.get("equation_preview"))
            if key in by_card:
                old = by_card[key]
                old["row_ids"] = sorted(set(old.get("row_ids", [])) | set(example.get("row_ids", [])))
                continue
            by_card[key] = example
            examples.append(example)
        for example in examples:
            example["screening_issues"] = evidence_issues(example)
            example["source_grounded"] = not example["screening_issues"]
            reasons.update(example["screening_issues"])
        page["source_examples"] = examples
        accepted = sum(e["source_grounded"] for e in examples)
        page["topic_relevant_source_examples"] = accepted
        if accepted:
            page["status"] = "v2_source_grounded"
            grounded += 1
        elif examples or page.get("matched_v2_row_ids"):
            page["status"] = "v2_identifier_linked"
        if page["status"] in {"v2_source_grounded", "v2_identifier_linked"}:
            linked += 1
    total = len(report.get("pages", {}))
    report.setdefault("coverage", {}).update({
        "pages_with_v2_source_grounding": grounded,
        "pages_with_v2_identifier_links": linked,
        "page_v2_grounding_rate": grounded / total if total else 0,
        "page_v2_identifier_link_rate": linked / total if total else 0,
    })
    report["evidence_revalidation"] = {
        "policy": "complete relation, exact card/row link, local context and relation-specific terms; no chapter-wide correctness inference",
        "screening_issue_counts": dict(reasons),
        "rejected_candidates_retained": True,
    }
    report["claim_scope"] = (
        "Source-grounded denotes a screened recovered relation, not validation of a chapter. "
        "Topic-only mentions and damaged equations remain retrieval candidates."
    )
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", default="discoveries/morphwiki_quantum/v2_quantum_evidence_index.json")
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--out-md")
    args = parser.parse_args()
    data = Path(args.index).read_bytes()
    report = revalidate(json.loads(data))
    report["evidence_revalidation"]["input_sha256"] = hashlib.sha256(data).hexdigest()
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if args.out_md:
        try:
            from build_morphwiki_v2_quantum_evidence_index import render_md
        except ModuleNotFoundError:
            from scripts.build_morphwiki_v2_quantum_evidence_index import render_md
        Path(args.out_md).write_text(render_md(report), encoding="utf-8")
    print(json.dumps({"output": args.out_json, "coverage": report["coverage"], "screening": report["evidence_revalidation"]}, indent=2))


if __name__ == "__main__":
    main()
