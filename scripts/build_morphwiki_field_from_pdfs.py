#!/usr/bin/env python3
"""Build a first-pass MorphWiki field wiki from a folder of scientific papers.

FieldBridge owns document extraction and operational evidence scoring. This
script turns its adapter, source anchors, and extraction report into synchronized
topic, mechanism, and construction views without inventing missing clauses.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence


ROLE_ORDER = (
    "state_or_carrier",
    "operator_apparatus",
    "update_or_transport",
    "admissibility_logic",
    "readout_rule",
    "protocol_execution",
    "falsifier",
)

ROLE_TO_IDENTITY = {
    "state_or_carrier": "Xi: carrier or state space",
    "operator_apparatus": "Omega: transformation apparatus",
    "update_or_transport": "Omega: directed operation",
    "admissibility_logic": "C: closure and admissibility",
    "readout_rule": "R: observable or prediction",
    "protocol_execution": "P: preparation and execution",
    "falsifier": "Validation: clause-breaking control",
}


def slugify(value: str, fallback: str = "field") -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    return text or fallback


def clean_text(value: Any, limit: int = 700) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def fieldbridge_builder():
    try:
        from fieldbridge.pdf_sparse_builder import build_pdf_field_pack
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "The PDF workflow requires FieldBridge. Clone fieldbridge beside "
            "morphwiki and run `python3 -m pip install -e '../fieldbridge[pdf]'`."
        ) from exc
    return build_pdf_field_pack


def active_scores(
    values: Mapping[str, Any],
    *,
    threshold: float,
    limit: int = 8,
) -> List[Dict[str, Any]]:
    rows = [
        {"id": key, "score": float(value)}
        for key, value in values.items()
        if float(value) >= threshold
    ]
    return sorted(rows, key=lambda row: row["score"], reverse=True)[:limit]


def role_evidence(record: Mapping[str, Any]) -> Dict[str, List[str]]:
    roles: Dict[str, List[str]] = defaultdict(list)
    for value in record.get("variables") or []:
        head, separator, body = str(value).partition(": ")
        if separator and head in ROLE_ORDER and body:
            roles[head].append(body)
    roles["readout_rule"].extend(str(value) for value in record.get("measurements") or [])
    roles["falsifier"].extend(str(value) for value in record.get("controls") or [])
    return dict(roles)


def record_status(roles: Mapping[str, Sequence[str]]) -> str:
    required = {
        "state_or_carrier",
        "operator_apparatus",
        "admissibility_logic",
        "readout_rule",
        "protocol_execution",
    }
    return (
        "candidate_construction"
        if required.issubset({role for role, rows in roles.items() if rows})
        else "incomplete_candidate"
    )


def bullet_rows(values: Iterable[str], unresolved: str) -> List[str]:
    rows = [f"- {clean_text(value, 360)}" for value in values if str(value).strip()]
    return rows or [f"- Unresolved: {unresolved}"]


def render_mechanism_page(
    *,
    record: Mapping[str, Any],
    field_label: str,
    active_substrates: Sequence[Mapping[str, Any]],
) -> tuple[str, Dict[str, Any]]:
    roles = role_evidence(record)
    status = record_status(roles)
    title = str(record.get("title") or "Mechanism anchor")
    sources = [str(value) for value in record.get("references") or []]
    routes = active_scores(record.get("routes") or {}, threshold=0.18)
    fibers = active_scores(record.get("fibers") or {}, threshold=0.18)
    equations = [clean_text(value, 420) for value in record.get("equations") or []]

    lines = [
        f"# {title}",
        "",
        f"- Field: `{field_label}`",
        f"- Construction status: `{status}`",
        f"- Source: {', '.join(f'`{value}`' for value in sources) or '`unresolved`'}",
        "",
        "## Topic View",
        "",
        clean_text(record.get("summary"), 900) or "No source summary was extracted.",
        "",
        "## Mechanism View",
        "",
        "```text",
        "M = (Omega, Xi)",
        "I_op = (M; C, R, P)",
        "I_real = (I_op; A)",
        "```",
        "",
        "### Omega: transformation apparatus",
        "",
        *bullet_rows(
            [*roles.get("operator_apparatus", []), *roles.get("update_or_transport", [])],
            "no source passage identified the operation",
        ),
        "",
        "### Xi: carrier or state space",
        "",
        *bullet_rows(
            roles.get("state_or_carrier", []),
            "no source passage identified the carrier",
        ),
        "",
        "Candidate substrate classes:",
        *bullet_rows(
            [
                f"{row['id']} ({float(row['score']):.3f})"
                for row in active_substrates
            ],
            "no substrate class crossed the corpus threshold",
        ),
        "",
        "### C: closure and admissibility",
        "",
        *bullet_rows(
            roles.get("admissibility_logic", []),
            "closure or admissibility was not explicit",
        ),
        "",
        "### R: observable or prediction",
        "",
        *bullet_rows(
            roles.get("readout_rule", []),
            "no source-grounded observable or prediction was extracted",
        ),
        "",
        "### P: protocol",
        "",
        *bullet_rows(
            roles.get("protocol_execution", []),
            "preparation or execution order was not explicit",
        ),
        "",
        "### A: realization",
        "",
        *bullet_rows(sources, "source realization was not retained"),
        "",
        "## Representative Equations",
        "",
        *([f"- `{value}`" for value in equations] or ["- No equation was extracted from this anchor."]),
        "",
        "## Operational Index",
        "",
        "Active routes:",
        *bullet_rows(
            [f"{row['id']} ({float(row['score']):.3f})" for row in routes],
            "no route crossed the display threshold",
        ),
        "",
        "Active fibers:",
        *bullet_rows(
            [f"{row['id']} ({float(row['score']):.3f})" for row in fibers],
            "no fiber crossed the display threshold",
        ),
        "",
        "## Falsification",
        "",
        *bullet_rows(
            roles.get("falsifier", []),
            "the source anchor did not state a clause-breaking control",
        ),
        "",
        "## Evidence Boundary",
        "",
        "This page is a source-indexed construction candidate. Missing clauses remain "
        "unresolved; the page does not promote them from nearby papers or generic templates.",
    ]

    payload = {
        "title": title,
        "status": status,
        "sources": sources,
        "roles": roles,
        "routes": routes,
        "fibers": fibers,
        "equations": equations,
    }
    return "\n".join(lines), payload


def render_index(
    *,
    label: str,
    adapter: Mapping[str, Any],
    evidence: Mapping[str, Any],
    pages: Sequence[Mapping[str, Any]],
) -> str:
    corpus = adapter.get("corpus") or {}
    role_profile = adapter.get("constructor_role_profile") or {}
    failures = (evidence.get("source_artifacts") or {}).get("extraction_failures") or []
    lines = [
        f"# {label}: Mechanism-First Field Wiki",
        "",
        "This first-pass wiki was built from a local paper folder. FieldBridge "
        "extracts source passages and operational evidence; MorphWiki organizes "
        "them as topic, mechanism, and construction views.",
        "",
        "## Corpus",
        "",
        f"- Readable documents: `{corpus.get('documents', 0)}`",
        f"- Extracted chunks: `{corpus.get('chunks', 0)}`",
        f"- Mechanism pages: `{len(pages)}`",
        f"- Unreadable documents: `{len(failures)}`",
        "",
        "## Candidate Construction Spine",
        "",
    ]
    for role in ROLE_ORDER:
        lines.append(
            f"- `{ROLE_TO_IDENTITY[role]}`: evidence score "
            f"`{float(role_profile.get(role, 0.0)):.3f}`"
        )
    lines.extend(
        [
            "",
            "The order above is the shared MorphWiki dependency contract. The "
            "scores state which clauses are evidenced by this corpus; they do not "
            "establish a field-specific causal order.",
            "",
            "## Mechanism Pages",
            "",
        ]
    )
    for page in pages:
        lines.append(
            f"- [{page['title']}](pages/{page['filename']}) "
            f"(`{page['status']}`)"
        )
    if failures:
        lines.extend(["", "## Extraction Failures", ""])
        for failure in failures:
            lines.append(
                f"- `{failure.get('path', '')}`: {clean_text(failure.get('error'), 240)}"
            )
    lines.extend(
        [
            "",
            "## Next Audit",
            "",
            "Review source passages, merge duplicate anchors, name the field-specific "
            "constructor spine, and retain unresolved clauses until equation or "
            "experimental evidence is added.",
        ]
    )
    return "\n".join(lines)


def build_field_wiki(
    *,
    pdf_dir: Path,
    field_id: str,
    label: str,
    description: str,
    out_dir: Path,
    max_docs: int,
    max_chunks_per_doc: int,
    max_chars: int,
    max_anchors: int,
    max_pages: int,
    extensions: Sequence[str],
) -> Dict[str, Any]:
    field_id = slugify(field_id)
    builder = fieldbridge_builder()
    fieldbridge_dir = out_dir / "fieldbridge"
    summary = builder(
        pdf_dir=pdf_dir,
        field_id=field_id,
        label=label,
        description=description,
        out_dir=fieldbridge_dir,
        max_docs=max_docs,
        max_chunks_per_doc=max_chunks_per_doc,
        max_chars=max_chars,
        max_anchors=max_anchors,
        extensions=extensions,
    )
    adapter = load_json(fieldbridge_dir / "field_adapters" / f"{field_id}.json")
    evidence = load_json(
        fieldbridge_dir / "field_pack_evidence" / f"{field_id}.json"
    )
    records = load_json(fieldbridge_dir / "index" / "core_examples.json")[:max_pages]
    active_substrates = active_scores(
        adapter.get("substrate_profile") or {},
        threshold=0.025,
        limit=6,
    )

    pages: List[Dict[str, Any]] = []
    used_names: Dict[str, int] = defaultdict(int)
    for index, record in enumerate(records):
        stem = slugify(str(record.get("title") or f"mechanism_{index:04d}"))
        suffix = used_names[stem]
        used_names[stem] += 1
        filename = f"{stem}.md" if suffix == 0 else f"{stem}_{suffix:02d}.md"
        markdown, payload = render_mechanism_page(
            record=record,
            field_label=label,
            active_substrates=active_substrates,
        )
        write_text(out_dir / "pages" / filename, markdown)
        pages.append({"filename": filename, **payload})

    index_markdown = render_index(
        label=label,
        adapter=adapter,
        evidence=evidence,
        pages=pages,
    )
    write_text(out_dir / "index.md", index_markdown)
    wiki = {
        "schema_version": 1,
        "artifact_type": "morphwiki_pdf_field_wiki",
        "field_id": field_id,
        "label": label,
        "description": description,
        "source_folder": str(pdf_dir),
        "fieldbridge_summary": summary,
        "constructor_role_profile": adapter.get("constructor_role_profile") or {},
        "substrate_profile": adapter.get("substrate_profile") or {},
        "active_routes": adapter.get("active_routes") or [],
        "pages": pages,
        "artifacts": {
            "index": "index.md",
            "pages": "pages/",
            "fieldbridge": "fieldbridge/",
        },
        "claim_scope": (
            "Source-grounded first-pass field wiki. It organizes extracted evidence "
            "but does not infer missing clauses or validate a scientific mechanism."
        ),
    }
    write_json(out_dir / "field_wiki.json", wiki)
    return {
        "out_dir": str(out_dir),
        "field_id": field_id,
        "documents": summary["documents"],
        "documents_failed": summary["documents_failed"],
        "pages": len(pages),
        "index": str(out_dir / "index.md"),
        "field_wiki": str(out_dir / "field_wiki.json"),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build a source-grounded MorphWiki field wiki from PDFs/texts."
    )
    parser.add_argument("pdf_dir", help="Folder containing PDF, text, TeX, or Markdown documents.")
    parser.add_argument("--field-id", required=True)
    parser.add_argument("--label", default="")
    parser.add_argument("--description", default="")
    parser.add_argument("--out-dir", default="")
    parser.add_argument("--max-docs", type=int, default=200)
    parser.add_argument("--max-chunks-per-doc", type=int, default=40)
    parser.add_argument("--max-chars", type=int, default=2600)
    parser.add_argument("--max-anchors", type=int, default=80)
    parser.add_argument("--max-pages", type=int, default=80)
    parser.add_argument("--extensions", default=".pdf,.txt,.tex,.md")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    field_id = slugify(args.field_id)
    label = args.label or field_id.replace("_", " ").title()
    out_dir = (
        Path(args.out_dir)
        if args.out_dir
        else Path("discoveries") / f"morphwiki_{field_id}"
    )
    extensions = tuple(
        value.strip().lower()
        for value in args.extensions.split(",")
        if value.strip()
    )
    report = build_field_wiki(
        pdf_dir=Path(args.pdf_dir),
        field_id=field_id,
        label=label,
        description=args.description,
        out_dir=out_dir,
        max_docs=args.max_docs,
        max_chunks_per_doc=args.max_chunks_per_doc,
        max_chars=args.max_chars,
        max_anchors=args.max_anchors,
        max_pages=args.max_pages,
        extensions=extensions,
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
