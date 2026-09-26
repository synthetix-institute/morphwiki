import re
from pathlib import Path

import pytest

from scripts.build_morphwiki_quantum_book import (
    edition_inventory, load_json, page_display_name, page_entry, render_book,
    physical_construction_prose,
)
from scripts.audit_quantum_companion import topic_bodies, assess, displayed_equations

ROOT = Path("discoveries/morphwiki_quantum")


@pytest.fixture(scope="module")
def editions():
    return render_book(ROOT), render_book(ROOT, edition="companion")


def test_companion_preserves_treatments_not_template_pages(editions):
    full, companion = editions
    inventory = edition_inventory(ROOT, load_json(ROOT / "quantum_mechanism_tree.json"))
    assert sum(row["kind"] == "treatment" for row in inventory.values()) == 62
    assert sum(row["kind"] == "overview" for row in inventory.values()) == 63
    assert len(re.findall(r"\\label\{index:", companion)) == 146
    full_bodies, bodies = topic_bodies(full), topic_bodies(companion)
    assert len(bodies) == 62
    assert all(body == full_bodies[slug] for slug, body in bodies.items())
    assert "Representative Relation" not in companion
    assert "a topic-specific Hamiltonian or field equation is required" not in companion


def test_scope_and_source_attribution_without_process_labels(editions):
    for tex in editions:
        title = tex.split(r"\end{titlepage}")[0]
        assert "Scope and authorship" in title
        assert "authors' organization" in title
        assert "Authored exposition of established theory" not in tex
        assert "Authored connection; equations supplied in the exposition" not in tex
        assert "Schr Dinger" not in tex and "Schrodinger" not in tex
        assert "The governing operation is" not in tex
    assert "Relations In The Original Papers" in editions[1]
    assert "Equation Sources" in editions[1]
    assert "Standard constructor skeleton" not in editions[1]
    assert "No evolution law depending only on \\(x_0\\) can reproduce both initial slopes." in editions[1]


def test_aliases_do_not_hide_existing_physical_treatments():
    tree = load_json(ROOT / "quantum_mechanism_tree.json")
    for branch_id, branch in tree["branches"].items():
        for row in branch["pages"]:
            if row["slug"] in {"hamiltonian_quantum_mechanics", "path_integral_formulation"}:
                tex = page_entry(ROOT, row, 1, branch_id, branch)
                assert "Topic Equations" in tex
                assert "is an alternative name" not in tex


def test_inventory_is_not_allowed_to_masquerade_as_sections(editions, tmp_path):
    full, companion = editions
    broken = companion.replace(r"\label{topic:quantum-state}", r"\label{index:quantum-state}")
    report = assess(ROOT, broken, full, tmp_path / "missing.pdf")
    assert not report["checks"]["all_62_topic_specific_treatments_preserved"]
    assert "quantum-state" in report["missing_treatments"]
    corrupted = companion.replace(r"|\mathbf r|\leq1", r"|\mathbf r|\leq2")
    report = assess(ROOT, corrupted, full, tmp_path / "missing.pdf")
    assert not report["checks"]["retained_treatment_bodies_match_full_edition"]


def test_copyediting_retains_names_and_fixes_sentence_fragments():
    assert page_display_name("Schr Dinger Picture") == "Schrödinger Picture"
    assert page_display_name("Schrodinger picture") == "Schrödinger picture"
    text = physical_construction_prose("Uncertainty principle", "incompatibility", {"slug": "uncertainty_principle"}, {})
    assert "involves two or more" in text
    assert "is Two" not in text


def test_companion_cannot_silently_drop_treatments():
    with pytest.raises(ValueError, match="cannot be truncated"):
        render_book(ROOT, max_pages_per_branch=1, edition="companion")


def test_all_display_forms_count_without_preamble_definitions():
    tex = (r"\newcommand{\example}{\[ignored\]}\begin{document}"
           r"\[a=b\]\begin{equation}c=d\end{equation}"
           r"\begin{centeredalign}e=f\end{centeredalign}")
    assert displayed_equations(tex) == ["a=b", "c=d", "e=f"]


def test_duplicate_treatment_labels_fail(editions, tmp_path):
    full, companion = editions
    duplicate = companion + r"\section{Duplicate}\label{topic:quantum-state}text\clearpage"
    report = assess(ROOT, duplicate, full, tmp_path / "missing.pdf")
    assert not report["checks"]["each_treatment_appears_once"]
