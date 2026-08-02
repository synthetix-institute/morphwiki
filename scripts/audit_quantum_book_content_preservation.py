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


def audit(args: argparse.Namespace) -> Dict[str, Any]:
    root = Path(args.root)
    tree = load_json(root / "quantum_mechanism_tree.json")
    contract = load_json(Path(args.contract))
    tex_path = Path(args.tex)
    pdf_path = Path(args.pdf)
    derivation_dir = root / "derivation_pages"

    expected_pages = tree_pages(tree)
    expected_slugs = list(expected_pages)
    equation_required_slugs = [
        slug for slug, branch_id in expected_pages.items() if branch_id != "annotations"
    ]
    tex = tex_path.read_text(encoding="utf-8", errors="replace")
    missing_labels = [slug for slug in expected_slugs if f"\\label{{page:{latex_label(slug)}}}" not in tex]
    missing_pages: List[str] = []
    missing_equations: List[str] = []
    total_words = 0
    equation_blocks = 0
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

    pdf_pages = pdf_page_count(pdf_path)
    checks = {
        "topic_count": len(expected_slugs) >= int(contract["minimum_topic_count"]),
        "all_topics_in_tex": not missing_labels,
        "all_derivation_pages_present": not missing_pages,
        "all_physics_topics_have_equations": not missing_equations,
        "topic_words": total_words >= int(contract["minimum_topic_words"]),
        "equation_blocks": equation_blocks >= int(contract["minimum_equation_blocks"]),
        "pdf_pages": pdf_pages >= int(contract["minimum_pdf_pages"]),
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
            "equation_required_topic_count": len(equation_required_slugs),
            "annotation_count": len(expected_slugs) - len(equation_required_slugs),
            "topic_words": total_words,
            "equation_blocks": equation_blocks,
            "pdf_pages": pdf_pages,
        },
        "checks": checks,
        "missing_tex_labels": missing_labels,
        "missing_derivation_pages": missing_pages,
        "missing_equation_blocks": missing_equations,
        "claim_scope": "Build-integrity audit. It requires equation-bearing content for physical topics while keeping historical and interpretive entries free of invented equations; it does not validate the physics of individual pages.",
    }
    Path(args.out_json).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = [
        "# Quantum Book Content Preservation Audit",
        "",
        f"- Readiness: `{readiness}`",
        f"- Topics: `{len(expected_slugs)}`",
        f"- Topic words: `{total_words}`",
        f"- Equation blocks: `{equation_blocks}`",
        f"- PDF pages: `{pdf_pages}`",
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
