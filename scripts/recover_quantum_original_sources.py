#!/usr/bin/env python3
"""Recover original arXiv displays without inventing V2 row/card alignment.

Downloads are opt-in. Cached HTML is private build material; the public export
contains equation locations, mathematical expressions and hashes, not article
prose. A selected original display remains distinct from a verified V2 card.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

from bs4 import BeautifulSoup

try:
    from quantum_source_evidence import canonical_arxiv_id, equation_issues
except ModuleNotFoundError:
    from scripts.quantum_source_evidence import canonical_arxiv_id, equation_issues


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def displays(html: bytes) -> list[dict]:
    soup = BeautifulSoup(html, "html.parser")
    result = []
    for element in soup.select(".ltx_equation, .ltx_equationgroup"):
        if element.find_parent(class_="ltx_equationgroup"):
            continue
        location = element.get("id")
        math = [m.get("alttext", "").strip() for m in element.select("math[alttext]")]
        if not location or not math:
            continue
        equation = r" \\ ".join(dict.fromkeys(math))
        syntax_issues = equation_issues(equation)
        if len(math) > 1 and any(equation_issues(part) for part in math):
            syntax_issues.append("fragmented_math_cells")
        section = element.find_parent(["section", "article"])
        heading = section.find(re.compile(r"^h[1-6]$")) if section else None
        previous = element.find_previous(class_="ltx_para")
        following = element.find_next(class_="ltx_para")
        context = "\n".join(p.get_text(" ", strip=True) for p in [previous, following] if p)
        result.append({"display_id": location, "equation_latex": equation,
                       "equation_sha256": digest(equation.encode()),
                       "section": heading.get_text(" ", strip=True) if heading else "",
                       "context": context, "context_sha256": digest(context.encode()),
                       "syntax_issues": syntax_issues})
    return result


def recover(plan: dict, cache: Path, *, fetch: bool, index: dict) -> dict:
    documents, failures, records = {}, [], []
    for item in plan["papers"]:
        paper = canonical_arxiv_id(item["paper_id"])
        if not paper or paper != item["paper_id"]:
            raise ValueError("Plan requires canonical arXiv identifiers")
        path = cache / (paper.replace("/", "_") + ".html")
        url = "https://arxiv.org/html/" + paper
        try:
            if not path.exists():
                if not fetch:
                    raise FileNotFoundError(f"Missing cached HTML: {paper}")
                import requests
                response = requests.get(url, timeout=60, headers={"User-Agent": "MorphWiki/source-recovery (research; one request per 3 seconds)"})
                response.raise_for_status()
                if "html" not in response.headers.get("Content-Type", ""):
                    raise ValueError("arXiv did not return HTML")
                cache.mkdir(parents=True, exist_ok=True)
                path.write_bytes(response.content)
                time.sleep(3)
            data = path.read_bytes()
            source_displays = displays(data)
            if not source_displays:
                raise ValueError("No locatable LaTeX displays in HTML")
            soup = BeautifulSoup(data, "html.parser")
            documents[paper] = {"url": url, "sha256": digest(data),
                                "title": soup.title.get_text(" ", strip=True) if soup.title else "",
                                "display_count": len(source_displays)}
            # Full context stays in the local cache for inspection, not the published index.
            path.with_suffix(".displays.json").write_text(json.dumps(source_displays, indent=2) + "\n")
            for selection in item.get("selections", []):
                found = [d for d in source_displays if d["display_id"] == selection["display_id"]]
                if len(found) != 1:
                    failures.append({"paper_id": paper, "selection": selection, "reason": "display_not_unique_or_missing"})
                    continue
                d = found[0]
                required = selection.get("required_latex", [])
                if not required or any(term not in d["equation_latex"] for term in required) or d["syntax_issues"]:
                    failures.append({"paper_id": paper, "selection": selection, "reason": "equation_contract_failed", "syntax_issues": d["syntax_issues"]})
                    continue
                slug = selection["topic"]
                legacy = (index.get("pages", {}).get(slug) or {}).get("source_examples", [])
                old_cards = sorted({c for e in legacy if any(re.sub(r"v\d+$", "", canonical_arxiv_id(p)) == re.sub(r"v\d+$", "", paper) for p in e.get("paper_ids", [])) for c in e.get("card_ids", [])})
                records.append({"topic": slug, "paper_id": paper, "url": url + "#" + d["display_id"],
                    "display_id": d["display_id"], "equation_latex": d["equation_latex"],
                    "equation_sha256": d["equation_sha256"], "document_sha256": digest(data),
                    "context_sha256": d["context_sha256"], "section": d["section"],
                    "relation": selection["relation"], "scope": selection["scope"],
                    "selection": "editorially selected original display; exact locator and expression checked",
                    "candidate_v2_card_ids": old_cards,
                    "v2_card_alignment": "not_established", "source_origin": "original_arxiv_html"})
        except Exception as exc:
            failures.append({"paper_id": paper, "reason": str(exc)})
        print(json.dumps({"paper": paper, "cached": path.exists(), "records": len(records)}), flush=True)
    return {"report_type": "original_quantum_source_recovery", "generated_at": datetime.now(timezone.utc).isoformat(),
            "documents": documents, "records": records, "failures": failures,
            "topic_count": len({r["topic"] for r in records}),
            "claim_scope": "Original displays and their mathematical context were selected for the explanation. No V2 row-to-display alignment or chapter-wide proof is inferred."}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--plan", required=True)
    p.add_argument("--cache", default="build/arxiv_originals")
    p.add_argument("--v2-index", default="discoveries/morphwiki_quantum/v2_quantum_evidence_index.json")
    p.add_argument("--out", default="discoveries/morphwiki_quantum/original_source_relations.json")
    p.add_argument("--fetch", action="store_true")
    args = p.parse_args()
    index = json.loads(Path(args.v2_index).read_text())
    report = recover(json.loads(Path(args.plan).read_text()), Path(args.cache), fetch=args.fetch, index=index)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"out": args.out, "topics": report["topic_count"], "failures": len(report["failures"])}))
    if report["failures"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
