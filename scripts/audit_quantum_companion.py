#!/usr/bin/env python3
"""Check the expository edition without treating an index as developed physics."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

try:
    from audit_quantum_book_content_preservation import pdf_page_count, noncanonical_arxiv_links
    from build_morphwiki_quantum_book import (
        edition_inventory, latex_escape, latex_label, load_json, load_original_sources,
        page_display_name, page_path, top_evidence,
    )
except ModuleNotFoundError:
    from scripts.audit_quantum_book_content_preservation import pdf_page_count, noncanonical_arxiv_links
    from scripts.build_morphwiki_quantum_book import (
        edition_inventory, latex_escape, latex_label, load_json, load_original_sources,
        page_display_name, page_path, top_evidence,
    )


def topic_bodies(tex: str) -> dict[str, str]:
    """Only a labelled section is a treatment; reference-index labels never count."""
    return {
        match[1]: match[2].strip()
        for match in re.finditer(
            r"\\section\{[^\n]+\}\s*\\label\{topic:([^}]+)\}(.*?)"
            r"(?=\\clearpage|\\chapter\{|\\part\{|\\backmatter|\Z)", tex, re.S
        )
    }


def displayed_equations(tex: str) -> list[str]:
    """Count rendered display environments, excluding definitions in the preamble."""
    body = tex.split(r"\begin{document}", 1)[-1]
    pattern = re.compile(
        r"\\begin\{(centeredalign|equation\*?|align\*?|gather\*?|displaymath)\}"
        r"(.*?)\\end\{\1\}|\\\[(.*?)\\\]", re.S
    )
    return [match.group(2) if match.group(1) else match.group(3)
            for match in pattern.finditer(body)]


def assess(root: Path, tex: str, full_tex: str, pdf: Path, expected_treatments: int = 62) -> dict:
    tree = load_json(root / "quantum_mechanism_tree.json")
    inventory = edition_inventory(root, tree)
    expected = {latex_label(slug) for slug, row in inventory.items() if row["kind"] == "treatment"}
    sections, full_sections = topic_bodies(tex), topic_bodies(full_tex)
    section_labels = re.findall(r"\\section\{[^\n]+\}\s*\\label\{topic:([^}]+)\}", tex)
    index = re.findall(r"\\label\{index:([^}]+)\}", tex)
    omitted = sorted(expected - sections.keys())
    changed = sorted(label for label in expected if label in sections and sections[label] != full_sections.get(label))
    equations = displayed_equations(tex)
    missing_equations = sorted(label for label in expected & sections.keys()
        if not re.search(r"\\begin\{(?:centeredalign|equation\*?)\}|\\\[", sections[label]))
    originals = load_original_sources(root)
    missing_sources = []
    original_by_topic = {}
    for record in originals["records"]:
        original_by_topic.setdefault(record["topic"], []).append(record["url"])
    for branch in tree["branches"].values():
        for row in branch.get("pages", []):
            slug = row["slug"]
            if inventory[slug]["kind"] != "treatment":
                continue
            body = sections.get(latex_label(slug), "")
            page = load_json(page_path(root, slug))
            recovered = [witness["arxiv_url"] for witness in top_evidence(page, row)]
            original = original_by_topic.get(slug, [])
            for url in recovered + original:
                if url not in body:
                    missing_sources.append(url)
            if recovered and r"\subsection*{Equation Sources}" not in body:
                missing_sources.append(f"{slug}: Equation Sources")
            if original and r"\subsection*{Relations In The Original Papers}" not in body:
                missing_sources.append(f"{slug}: Relations In The Original Papers")
    title_page = tex.split(r"\end{titlepage}", 1)[0]
    connections = load_json(root / "quantum_constructor_rewiring.json").get("connections", [])
    connection_sections = [
        rf"\section{{{latex_escape(page_display_name(str(connection.get('title') or 'Constructor connection')))}}}"
        for connection in connections
    ]
    checks = {
        "all_62_topic_specific_treatments_preserved": len(expected) == expected_treatments and set(sections) == expected,
        "each_treatment_appears_once": Counter(section_labels) == Counter(expected),
        "retained_treatment_bodies_match_full_edition": not changed,
        "every_treatment_has_equations": not missing_equations,
        "source_links_remain_at_the_relevant_treatment": not missing_sources,
        "all_topics_indexed_once": Counter(index) == Counter(latex_label(s) for s in inventory),
        "index_not_counted_as_treatments": not any(label.startswith("index:") for label in sections),
        "no_representative_relation_templates": "Representative Relation" not in tex and "a topic-specific Hamiltonian or field equation is required" not in tex,
        "first_page_explains_scope": "Scope and authorship" in title_page and "authors' organization" in title_page,
        "cross_topic_connections_retained": bool(connections) and all(tex.count(section) == 1 for section in connection_sections),
        "no_process_labels_in_topic_prose": not re.search(
            r"Authored exposition of established theory|independently inspected original-paper display\(s\)|"
            r"No equation in this treatment is attributed|Standard constructor skeleton", tex),
        "canonical_arxiv_links": not noncanonical_arxiv_links(tex),
        "no_slug_or_fragment_artifacts": not re.search(r"Schr Dinger|Schrodinger|The governing operation is|The state carrier is A complex", tex),
        "pdf_exists": pdf.is_file() and pdf_page_count(pdf) > 0,
    }
    counts = Counter(row["kind"] for row in inventory.values())
    return {
        "report_type": "quantum_expository_companion_integrity",
        "build_integrity": "pass" if all(checks.values()) else "fail",
        "publication_role": "separate expository companion; not discovery evidence",
        "scientific_review_status": "incomplete; selected equations have executable checks, not chapter-wide certification",
        "checks": checks,
        "metrics": {"indexed_topics": len(index), "developed_treatments": len(sections),
                    "overview_entries": counts["overview"], "aliases": counts["alias"], "annotations": counts["annotation"],
                    "display_blocks": len(equations), "distinct_display_blocks": len(set(re.sub(r"\s+", "", e) for e in equations)),
                    "pdf_pages": pdf_page_count(pdf)},
        "missing_treatments": omitted, "changed_treatments": changed,
        "missing_equations": missing_equations,
        "missing_original_sources": missing_sources,
        "tex_sha256": hashlib.sha256(tex.encode()).hexdigest(),
        "preserved_body_sha256": {label: hashlib.sha256(body.encode()).hexdigest() for label, body in sections.items()},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("discoveries/morphwiki_quantum"))
    parser.add_argument("--full-tex", type=Path, default=Path("discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex"))
    parser.add_argument("--companion-dir", type=Path, default=Path("discoveries/morphwiki_quantum/book/companion"))
    args = parser.parse_args()
    tex = args.companion_dir / "quantum_mechanism_tree_book.tex"
    report = assess(args.root, tex.read_text(), args.full_tex.read_text(), tex.with_suffix(".pdf"))
    (args.companion_dir / "companion_integrity.json").write_text(json.dumps(report, indent=2) + "\n")
    lines = ["# Expository companion", "", f"Build integrity: {report['build_integrity']}",
             f"Role: {report['publication_role']}", f"Scientific review: {report['scientific_review_status']}", "", "## Contents"]
    lines.extend(f"- {key}: {value}" for key, value in report["metrics"].items())
    lines.extend(["", "## Preservation and provenance"])
    lines.extend(f"- {key}: {'pass' if value else 'FAIL'}" for key, value in report["checks"].items())
    (args.companion_dir / "companion_integrity.md").write_text("\n".join(lines) + "\n")
    print(json.dumps({"build_integrity": report["build_integrity"], "metrics": report["metrics"]}, indent=2))
    if report["build_integrity"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
