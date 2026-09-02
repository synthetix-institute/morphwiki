#!/usr/bin/env python3
"""Fail closed when a quantum-book rebuild drops substantive topic content."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping


def load_json(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise TypeError(f"Expected an object in {path}")
    return data


def tree_pages(tree: Mapping[str, Any]) -> Dict[str, str]:
    pages: Dict[str, str] = {}
    for branch_id, branch in (tree.get("branches") or {}).items():
        for row in branch.get("pages") or []:
            slug = str(row.get("slug") or "").strip()
            if slug:
                pages[slug] = str(branch_id)
    return dict(sorted(pages.items()))


def pdf_page_count(path: Path) -> int:
    if not path.exists():
        return 0
    output = subprocess.check_output(["pdfinfo", str(path)], text=True, errors="replace")
    match = re.search(r"^Pages:\s+(\d+)\s*$", output, flags=re.MULTILINE)
    return int(match.group(1)) if match else 0


def latex_label(value: str) -> str:
    text = re.sub(r"[^a-z0-9:.-]+", "-", value.lower())
    return re.sub(r"-+", "-", text).strip("-") or "item"


def labels_with_prefix(tex: str, prefix: str) -> List[str]:
    """Return the labels in one LaTeX namespace."""
    return re.findall(rf"\\label\{{{re.escape(prefix)}:([^}}]+)\}}", tex)


def retention(current: int, baseline: int) -> float:
    if baseline <= 0:
        return 1.0
    return float(current) / float(baseline)


def audit(args: argparse.Namespace) -> Dict[str, Any]:
    root = Path(args.root)
    tree = load_json(root / "quantum_mechanism_tree.json")
    contract = load_json(Path(args.contract))
    tex_path = Path(args.tex)
    pdf_path = Path(args.pdf)
    derivation_dir = root / "derivation_pages"
    topic_page_dir = root / "pages"
    derivation_manifest_path = derivation_dir / "manifest.json"

    expected_pages = tree_pages(tree)
    expected_slugs = list(expected_pages)
    equation_required_slugs = [
        slug for slug, branch_id in expected_pages.items() if branch_id != "annotations"
    ]
    tex = tex_path.read_text(encoding="utf-8", errors="replace")
    expected_labels = {latex_label(slug): slug for slug in expected_slugs}
    expected_label_set = set(expected_labels)
    map_labels = labels_with_prefix(tex, "page")
    topic_labels = labels_with_prefix(tex, "topic")
    map_label_set = set(map_labels)
    topic_label_set = set(topic_labels)
    missing_map_labels = [
        expected_labels[label] for label in sorted(expected_label_set - map_label_set)
    ]
    missing_topic_labels = [
        expected_labels[label] for label in sorted(expected_label_set - topic_label_set)
    ]
    unexpected_topic_labels = sorted(topic_label_set - expected_label_set)
    duplicate_topic_labels = sorted(
        label for label in topic_label_set if topic_labels.count(label) != 1
    )
    missing_pages: List[str] = []
    missing_equations: List[str] = []
    total_words = 0
    equation_blocks = 0
    source_equation_pages = 0
    for slug in expected_slugs:
        path = derivation_dir / f"{slug}.md"
        if not path.exists():
            missing_pages.append(slug)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        total_words += len(text.split())
        blocks = len(re.findall(r"```math", text))
        equation_blocks += blocks
        if blocks == 0 and slug in equation_required_slugs:
            missing_equations.append(slug)
        if "## Source Equations" in text:
            source_equation_pages += 1

    derivation_manifest = (
        load_json(derivation_manifest_path) if derivation_manifest_path.exists() else {}
    )
    derivation_rows = derivation_manifest.get("pages") or []
    topic_specific_count = int(derivation_manifest.get("topic_specific_count", 0))
    branch_level_count = int(derivation_manifest.get("branch_level_count", 0))
    derivation_slugs = {
        str(row.get("slug") or "").strip()
        for row in derivation_rows
        if str(row.get("slug") or "").strip()
    }
    manifest_missing_slugs = sorted(set(expected_slugs) - derivation_slugs)
    manifest_extra_slugs = sorted(derivation_slugs - set(expected_slugs))

    tree_rows = [
        row
        for branch in (tree.get("branches") or {}).values()
        for row in (branch.get("pages") or [])
    ]
    grounded_topics = sum(
        bool((row.get("v2_evidence") or {}).get("available")) for row in tree_rows
    )
    identifier_linked_topics = sum(
        (row.get("v2_evidence") or {}).get("status") == "v2_identifier_linked"
        for row in tree_rows
    )
    minimum_grounded = int(contract.get("minimum_source_grounded_topics", 0))
    public_topic_pages = list(topic_page_dir.glob("*.md"))
    wikipedia_scaffold_pages = [
        path.name
        for path in public_topic_pages
        if "Wikipedia" in path.read_text(encoding="utf-8", errors="replace")
        or "wikipedia.org" in path.read_text(encoding="utf-8", errors="replace")
    ]
    unverified_arxiv_topic_pages = [
        path.name
        for path in public_topic_pages
        if "arxiv.org" in path.read_text(encoding="utf-8", errors="replace")
    ]

    pdf_pages = pdf_page_count(pdf_path)
    word_retention = retention(total_words, int(contract.get("baseline_topic_words", 0)))
    equation_retention = retention(
        equation_blocks, int(contract.get("baseline_equation_blocks", 0))
    )
    page_retention = retention(pdf_pages, int(contract.get("baseline_pdf_pages", 0)))
    checks = {
        "topic_count": len(expected_slugs) >= int(contract["minimum_topic_count"]),
        "all_topics_mapped_in_tex": not missing_map_labels,
        "all_topics_have_dedicated_sections": (
            not missing_topic_labels
            and not unexpected_topic_labels
            and not duplicate_topic_labels
            and len(topic_labels) == len(expected_slugs)
        ),
        "all_derivation_pages_present": not missing_pages,
        "derivation_manifest_matches_tree": (
            not manifest_missing_slugs and not manifest_extra_slugs
        ),
        "topic_specific_depth": topic_specific_count
        >= int(contract.get("minimum_topic_specific_count", 0)),
        "all_physics_topics_have_equations": not missing_equations,
        "topic_words": total_words >= int(contract["minimum_topic_words"]),
        "topic_word_retention": word_retention
        >= float(contract.get("minimum_topic_word_retention", 0.0)),
        "equation_blocks": equation_blocks >= int(contract["minimum_equation_blocks"]),
        "equation_block_retention": equation_retention
        >= float(contract.get("minimum_equation_block_retention", 0.0)),
        "pdf_pages": pdf_pages >= int(contract["minimum_pdf_pages"]),
        "pdf_page_retention": page_retention
        >= float(contract.get("minimum_pdf_page_retention", 0.0)),
        "source_equations_only_when_grounded": source_equation_pages == grounded_topics,
        "source_grounding": grounded_topics >= minimum_grounded,
        "source_summary_consistent": (
            "Each topic page retains its source links and equation witnesses" not in tex
            and (
                grounded_topics > 0
                or "The present source-card export confirms none" in tex
            )
        ),
        "no_wikipedia_scaffold": (
            "Wikipedia" not in tex
            and "wikipedia.org" not in tex
            and not wikipedia_scaffold_pages
        ),
        "no_unverified_topic_page_links": not unverified_arxiv_topic_pages,
        "no_internal_pipeline_language": not re.search(
            r"\b(?:Hyperion|V2|sparse[- ]attention|evidence placement|audit queue)\b",
            tex,
            flags=re.IGNORECASE,
        ),
    }
    readiness = "usable" if all(checks.values()) else "blocked"
    report = {
        "schema_version": 1,
        "report_type": "quantum_book_content_preservation_audit",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "readiness": readiness,
        "contract": str(args.contract),
        "metrics": {
            "topic_count": len(expected_slugs),
            "mapped_topic_count": len(map_label_set & expected_label_set),
            "dedicated_topic_section_count": len(topic_label_set & expected_label_set),
            "equation_required_topic_count": len(equation_required_slugs),
            "annotation_count": len(expected_slugs) - len(equation_required_slugs),
            "topic_specific_count": topic_specific_count,
            "branch_level_count": branch_level_count,
            "topic_words": total_words,
            "topic_word_retention": word_retention,
            "equation_blocks": equation_blocks,
            "equation_block_retention": equation_retention,
            "pdf_pages": pdf_pages,
            "pdf_page_retention": page_retention,
            "source_grounded_topics": grounded_topics,
            "identifier_linked_topics": identifier_linked_topics,
            "source_equation_pages": source_equation_pages,
        },
        "checks": checks,
        "missing_map_labels": missing_map_labels,
        "missing_topic_sections": missing_topic_labels,
        "unexpected_topic_sections": unexpected_topic_labels,
        "duplicate_topic_sections": duplicate_topic_labels,
        "missing_derivation_pages": missing_pages,
        "manifest_missing_topics": manifest_missing_slugs,
        "manifest_extra_topics": manifest_extra_slugs,
        "missing_equation_blocks": missing_equations,
        "wikipedia_scaffold_pages": wikipedia_scaffold_pages,
        "unverified_arxiv_topic_pages": unverified_arxiv_topic_pages,
        "claim_scope": "Build-integrity audit. It requires equation-bearing content for physical topics while keeping historical and interpretive entries free of invented equations; it does not validate the physics of individual pages.",
    }
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Quantum Book Content Preservation Audit",
        "",
        f"- Readiness: `{readiness}`",
        f"- Topics in the mechanism map: `{len(expected_slugs)}`",
        f"- Dedicated topic sections: `{len(topic_label_set & expected_label_set)}`",
        f"- Topic words: `{total_words}`",
        f"- Topic-specific physical treatments: `{topic_specific_count}`",
        f"- Branch-level topic maps: `{branch_level_count}`",
        f"- Topic-word retention: `{word_retention:.3f}`",
        f"- Equation blocks: `{equation_blocks}`",
        f"- PDF pages: `{pdf_pages}`",
        f"- PDF-page retention: `{page_retention:.3f}`",
        f"- Source-grounded topics: `{grounded_topics}`",
        f"- Identifier-linked candidates: `{identifier_linked_topics}`",
        "",
        "## Checks",
        "",
    ]
    lines.extend(f"- `{key}`: **{'passed' if value else 'failed'}**" for key, value in checks.items())
    Path(args.out_md).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": args.out_json, "markdown": args.out_md, "readiness": readiness}, indent=2))
    if readiness != "usable":
        raise SystemExit(1)
    return report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="discoveries/morphwiki_quantum")
    parser.add_argument("--contract", default="discoveries/morphwiki_quantum/book/quantum_book_content_contract.json")
    parser.add_argument("--tex", default="discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex")
    parser.add_argument("--pdf", default="discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.pdf")
    parser.add_argument("--out-json", default="discoveries/morphwiki_quantum/book/quantum_book_content_preservation_audit.json")
    parser.add_argument("--out-md", default="discoveries/morphwiki_quantum/book/quantum_book_content_preservation_audit.md")
    return parser


if __name__ == "__main__":
    audit(build_parser().parse_args())
