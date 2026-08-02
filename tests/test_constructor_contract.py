import json
from pathlib import Path

from scripts.build_morphwiki_quantum_book import (
    BRANCH_ORDER,
    render_book,
    render_derivation_page,
)
from scripts.build_morphwiki_quantum_tree import render_markdown
from scripts.morphwiki_constructor import (
    CONSTRUCTOR_CHAIN_LATEX,
    CONSTRUCTOR_CLAUSES,
    DISCOVERY_VERBS,
)


ROOT = Path("discoveries/morphwiki_quantum")


def test_shared_constructor_has_nested_identity_and_six_verbs():
    symbols = [row[0] for row in CONSTRUCTOR_CLAUSES]
    verbs = [row[0] for row in DISCOVERY_VERBS]

    assert symbols == ["Omega", "Xi", "C", "R", "P", "A"]
    assert verbs == ["Complete", "Reattach", "Compose", "Deform", "Observe", "Revise"]
    assert r"I_{\mathrm{op}}=(M;C,R,P)" in CONSTRUCTOR_CHAIN_LATEX
    assert r"\mathcal I_{\mathrm{real}}=(I_{\mathrm{op}};A)" in CONSTRUCTOR_CHAIN_LATEX


def test_public_tree_leads_with_construction_not_diagnostics():
    report = {
        "root": {"definition": "A quantum operational identity."},
        "branches": {
            branch_id: {
                "title": branch_id.title(),
                "definition": f"Definition of {branch_id}.",
                "pages": [],
            }
            for branch_id in BRANCH_ORDER
        },
        "discovery_leads": ["Derive a new consequence."],
    }

    text = render_markdown(report)

    assert text.startswith("# Quantum Theory By Construction")
    assert "## Six Constructor Verbs" in text
    assert "## A Discovery Procedure" in text
    assert "Sparse Attention Summary" not in text
    assert "Anomalies And Discovery Leads" not in text
    assert "readout" not in text.lower()


def test_default_book_uses_physical_constructor_and_hides_internal_audits(monkeypatch):
    monkeypatch.delenv("MORPHWIKI_EXPOSE_INTERNAL_METHOD", raising=False)

    tex = render_book(ROOT, max_pages_per_branch=0)

    assert "Quantum Theory" in tex
    assert "As A Mechanism Tree" in tex
    assert "How to Read Quantum Theory by Construction" in tex
    assert "The Quantum Operational Identity" in tex
    assert "Mechanism-Preserving Transformations In Quantum Theory" in tex
    assert "Designing Quantum Mechanisms" in tex
    assert r"\mathcal E_P\ \text{completely positive and trace preserving}" in tex
    assert r"E_y\ge0" in tex
    assert "Sparse Attention Summary" not in tex
    assert "Mechanism Validation Layers" not in tex
    assert "Anomalies And Leads" not in tex
    assert "readout" not in tex.lower()
    assert "unresolved constructor role" not in tex.lower()


def test_public_pdf_folder_page_uses_theoretical_physics_vocabulary():
    from scripts.build_morphwiki_field_from_pdfs import render_mechanism_page

    markdown, _ = render_mechanism_page(
        record={
            "title": "Spectral example",
            "measurements": ["energy spectrum"],
            "variables": ["state_or_carrier: Hilbert space"],
        },
        field_label="Quantum theory",
        active_substrates=[],
    )

    assert "### R: observable or prediction" in markdown
    assert "energy spectrum" in markdown
    assert "readout" not in markdown.lower()


def test_quantum_topic_pages_explain_the_construction_in_connected_prose():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    branch = tree["branches"]["context"]
    row = next(
        page
        for page in branch["pages"]
        if page["slug"] == "mathematical_formulation_of_quantum_mechanics"
    )

    markdown = render_derivation_page(ROOT, row, "context", branch)

    assert "## Why This Step Is Needed" in markdown
    assert "## How To Read The Relation" in markdown
    assert "## Worked Example" in markdown
    assert "## Connection To The Next Step" in markdown
    assert "a state encoding preparation" in markdown
    assert "- **Role:**" not in markdown
    assert "readout" not in markdown.lower()


def test_quantum_statistics_are_admissibility_rules_not_time_generators():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    branch = tree["branches"]["fields"]
    row = next(page for page in branch["pages"] if page["slug"] == "fermi_dirac_statistics")

    markdown = render_derivation_page(ROOT, row, "fields", branch)

    assert "antisymmetric-state constructor" in markdown
    assert "Fermi-Dirac statistics is an admissibility rule, not a generator" in markdown
    assert r"\{a_i,a_j^\dagger\}=\delta_{ij}" in markdown
    assert "supplies or modifies the generator of state evolution" not in markdown
