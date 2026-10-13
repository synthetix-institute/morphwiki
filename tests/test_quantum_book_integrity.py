import re
from pathlib import Path

import pytest

from scripts.build_morphwiki_quantum_book import (
    edition_inventory, load_json, page_display_name, page_entry, render_book,
    physical_construction_prose,
)
from scripts.audit_quantum_book_integrity import topic_bodies, assess, displayed_equations

ROOT = Path("discoveries/morphwiki_quantum")


@pytest.fixture(scope="module")
def book():
    return render_book(ROOT)


def test_book_prints_every_treatment_and_no_template_pages(book):
    inventory = edition_inventory(ROOT, load_json(ROOT / "quantum_mechanism_tree.json"))
    assert sum(row["kind"] == "treatment" for row in inventory.values()) == 125
    assert sum(row["kind"] == "overview" for row in inventory.values()) == 0
    labels = re.findall(r"\\section\{[^\n]+\}\s*\\label\{topic:([^}]+)\}", book)
    assert len(labels) == len(inventory) == 146
    assert "\\label{index:" not in book
    assert "Representative Relation" not in book
    assert "a topic-specific Hamiltonian or field equation is required" not in book
    assert "Expository companion" not in book and "Full reference edition" not in book


def test_scope_and_source_attribution_without_process_labels(book):
    title = book.split(r"\end{titlepage}")[0]
    assert "Scope and authorship" in title
    assert "authors' organization" in title
    assert "Authored exposition of established theory" not in book
    assert "Authored connection; equations supplied in the exposition" not in book
    assert "Schr Dinger" not in book and "Schrodinger" not in book
    assert "The governing operation is" not in book
    assert "Relations In The Original Papers" in book
    assert "Equation Sources" in book
    assert "Standard constructor skeleton" not in book
    assert "No evolution law depending only on \\(x_0\\) can reproduce both initial slopes." in book


def test_aliases_do_not_hide_existing_physical_treatments():
    tree = load_json(ROOT / "quantum_mechanism_tree.json")
    for branch_id, branch in tree["branches"].items():
        for row in branch["pages"]:
            if row["slug"] in {"hamiltonian_quantum_mechanics", "path_integral_formulation"}:
                tex = page_entry(ROOT, row, 1, branch_id, branch)
                assert r"\begin{centeredalign}" in tex
                assert "is an alternative name" not in tex


def test_missing_or_altered_treatments_fail_the_audit(book, tmp_path):
    broken = book.replace(r"\label{topic:quantum-state}", r"\label{other:quantum-state}")
    report = assess(ROOT, broken, tmp_path / "missing.pdf")
    assert not report["checks"]["all_topic_specific_treatments_preserved"]
    assert "quantum-state" in report["missing_treatments"]
    body = topic_bodies(book)["quantum-state"]
    report = assess(ROOT, book.replace(body, "A treatment without equations."), tmp_path / "missing.pdf")
    assert not report["checks"]["every_treatment_has_equations"]


def test_copyediting_retains_names_and_fixes_sentence_fragments():
    assert page_display_name("Schr Dinger Picture") == "Schrödinger Picture"
    assert page_display_name("Schrodinger picture") == "Schrödinger picture"
    text = physical_construction_prose("Uncertainty principle", "incompatibility", {"slug": "uncertainty_principle"}, {})
    assert "involves two or more" in text
    assert "is Two" not in text


def test_all_display_forms_count_without_preamble_definitions():
    tex = (r"\newcommand{\example}{\[ignored\]}\begin{document}"
           r"\[a=b\]\begin{equation}c=d\end{equation}"
           r"\begin{centeredalign}e=f\end{centeredalign}")
    assert displayed_equations(tex) == ["a=b", "c=d", "e=f"]


def test_duplicate_treatment_labels_fail(book, tmp_path):
    duplicate = book + r"\section{Duplicate}\label{topic:quantum-state}text\clearpage"
    report = assess(ROOT, duplicate, tmp_path / "missing.pdf")
    assert not report["checks"]["each_treatment_appears_once"]
