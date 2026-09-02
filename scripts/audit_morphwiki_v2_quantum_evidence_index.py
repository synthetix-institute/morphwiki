#!/usr/bin/env python3
"""Verify that the quantum evidence index is source-grounded and tree-complete."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping


DEFAULT_CORE_TOPICS = (
    "fermion",
    "gauge_theory",
    "quantum_decoherence",
    "commutator",
    "quantum_entanglement",
    "renormalization",
)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


def tree_slugs(tree: Mapping[str, Any]) -> set[str]:
    return {
        str(page["slug"])
        for branch in (tree.get("branches") or {}).values()
        for page in (branch.get("pages") or [])
        if page.get("slug")
    }


def has_relation_grounding(page: Mapping[str, Any]) -> bool:
    return any(
        example.get("topic_relevance") == "local_context_match"
        and example.get("relation_relevance") == "relation_context_match"
        and example.get("row_ids")
        and example.get("card_ids")
        for example in (page.get("source_examples") or [])
    )


def build(args: argparse.Namespace) -> dict[str, Any]:
    index = load_json(Path(args.index))
    pages = index.get("pages") or {}
    tree = load_json(Path(args.tree))
    expected = tree_slugs(tree)
    indexed = set(pages)
    missing = sorted(expected - indexed)
    extra = sorted(indexed - expected)
    statuses = Counter(str(page.get("status")) for page in pages.values())
    tokens: Counter[str] = Counter()
    roles: Counter[str] = Counter()
    routes: Counter[str] = Counter()
    for page in pages.values():
        tokens.update(page.get("tokens") or {})
        roles.update(page.get("constructor_roles") or {})
        routes.update(page.get("routes") or {})

    grounded_slugs = sorted(
        slug for slug, page in pages.items()
        if page.get("status") == "v2_source_grounded"
    )
    required_core = tuple(
        slug.strip() for slug in args.required_core_topics.split(",") if slug.strip()
    )
    core_missing = sorted(
        slug for slug in required_core
        if slug not in pages or not has_relation_grounding(pages[slug])
    )
    source_first = index.get("source_first_scan") or {}
    checks = {
        "tree_and_index_have_identical_topics": not missing and not extra,
        "source_first_scan_completed": int(source_first.get("cards_seen") or 0) > 0,
        "minimum_grounded_topics": len(grounded_slugs) >= args.minimum_grounded,
        "core_relations_are_grounded": not core_missing,
    }
    readiness = "usable" if pages and all(checks.values()) else "blocked"
    ungrounded = sorted(indexed - set(grounded_slugs))
    return {
        "schema_version": 2,
        "report_type": "morphwiki_quantum_v2_evidence_index_audit",
        "readiness": readiness,
        "index": args.index,
        "tree": args.tree,
        "coverage": index.get("coverage") or {},
        "checks": checks,
        "status_counts": dict(statuses),
        "tree_pages_missing_from_index": missing,
        "index_pages_absent_from_tree": extra,
        "source_grounded_topics": grounded_slugs,
        "source_grounded_topic_count": len(grounded_slugs),
        "required_core_topics": list(required_core),
        "core_topics_without_relation_grounding": core_missing,
        "pages_without_v2_source_grounding_count": len(ungrounded),
        "pages_without_v2_source_grounding_examples": ungrounded[:40],
        "top_tokens": tokens.most_common(30),
        "top_constructor_roles": roles.most_common(20),
        "top_routes": routes.most_common(20),
        "source_first_scan": source_first,
        "source_first_alignment": index.get("source_first_alignment") or {},
        "claim_scope": (
            "A grounded page contains a topic-bearing source equation joined through "
            "its exact equation-card identifier to a V2 mechanism row. Core pages also "
            "require a relation-specific term in the local derivation."
        ),
    }


def render_markdown(report: Mapping[str, Any]) -> str:
    coverage = report.get("coverage") or {}
    lines = [
        "# MorphWiki Quantum V2 Evidence Index Audit",
        "",
        f"- Readiness: `{report.get('readiness')}`",
        f"- Topics in index: `{coverage.get('pages_total', 0)}`",
        f"- Source-grounded topics: `{report.get('source_grounded_topic_count', 0)}`",
        "",
        "## Checks",
        "",
    ]
    lines.extend(
        f"- `{name}`: **{'passed' if passed else 'failed'}**"
        for name, passed in (report.get("checks") or {}).items()
    )
    if report.get("core_topics_without_relation_grounding"):
        lines.extend(["", "## Core Relations Still Missing"])
        lines.extend(
            f"- `{slug}`"
            for slug in report["core_topics_without_relation_grounding"]
        )
    if report.get("tree_pages_missing_from_index"):
        lines.extend(["", "## Tree Pages Missing From Index"])
        lines.extend(f"- `{slug}`" for slug in report["tree_pages_missing_from_index"])
    if report.get("index_pages_absent_from_tree"):
        lines.extend(["", "## Index Pages Absent From Tree"])
        lines.extend(f"- `{slug}`" for slug in report["index_pages_absent_from_tree"])
    lines.extend(["", "## Scope", str(report.get("claim_scope") or ""), ""])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--index",
        default="discoveries/morphwiki_quantum/v2_quantum_evidence_index.json",
    )
    parser.add_argument(
        "--tree", default="discoveries/morphwiki_quantum/quantum_mechanism_tree.json"
    )
    parser.add_argument(
        "--out-json",
        default="discoveries/morphwiki_quantum/v2_quantum_evidence_index_audit.json",
    )
    parser.add_argument(
        "--out-md",
        default="discoveries/morphwiki_quantum/v2_quantum_evidence_index_audit.md",
    )
    parser.add_argument("--minimum-grounded", type=int, default=6)
    parser.add_argument(
        "--required-core-topics", default=",".join(DEFAULT_CORE_TOPICS)
    )
    args = parser.parse_args()
    report = build(args)
    dump_json(Path(args.out_json), report)
    destination = Path(args.out_md)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(render_markdown(report), encoding="utf-8")
    print(
        json.dumps(
            {
                "json": args.out_json,
                "markdown": args.out_md,
                "readiness": report["readiness"],
            },
            indent=2,
        )
    )
    if report["readiness"] != "usable":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
