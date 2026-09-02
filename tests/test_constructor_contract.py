import json
from pathlib import Path

from scripts.audit_quantum_book_content_preservation import labels_with_prefix
from scripts.build_morphwiki_quantum_book import (
    BRANCH_ORDER,
    derivation_basis,
    latex_label,
    render_book,
    render_derivation_page,
    top_evidence,
)
from scripts.build_morphwiki_quantum_tree import (
    explicit_branch,
    render_markdown,
    v2_page_evidence_summary,
)
from scripts.build_morphwiki_v2_quantum_evidence_index import detect, enrich_with_source_cards
from scripts.morphwiki_constructor import (
    COMPATIBILITY_RESIDUAL_LATEX,
    CONSTRUCTOR_CHAIN_LATEX,
    CONSTRUCTOR_CLAUSES,
    DISCOVERY_VERBS,
    PHYSICAL_STATE_LATEX,
    PREDICTIVE_CLOSURE_LATEX,
    QUANTUM_ROLE_PROMOTIONS,
    ROLE_PROMOTION_CRITERION_LATEX,
    quantum_role_promotions_for_slug,
)


ROOT = Path("discoveries/morphwiki_quantum")


def test_shared_constructor_has_nested_identity_and_six_verbs():
    symbols = [row[0] for row in CONSTRUCTOR_CLAUSES]
    verbs = [row[0] for row in DISCOVERY_VERBS]

    assert symbols == ["Omega", "Xi", "C", "R", "P", "A"]
    assert verbs == ["Complete", "Reattach", "Compose", "Deform", "Observe", "Revise"]
    assert r"I_{\mathrm{op}}=(M;C,R,P)" in CONSTRUCTOR_CHAIN_LATEX
    assert r"I_{\mathrm{real}}=(I_{\mathrm{op}};A)" in CONSTRUCTOR_CHAIN_LATEX
    assert r"q\in\Xi" in PHYSICAL_STATE_LATEX
    assert r"\Omega_B\alpha-\beta\Omega_A" in COMPATIBILITY_RESIDUAL_LATEX


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

    assert text.startswith("# Quantum Theory Through Physical Roles")
    assert "## Predictive Closure" in text
    assert "## Role Promotion" in text
    assert "## Constructing A Theory" in text
    assert "Sparse Attention Summary" not in text
    assert "Anomalies And Discovery Leads" not in text
    assert "readout" not in text.lower()


def test_default_book_uses_physical_constructor_and_hides_internal_audits(monkeypatch):
    monkeypatch.delenv("MORPHWIKI_EXPOSE_INTERNAL_METHOD", raising=False)

    tex = render_book(ROOT, max_pages_per_branch=0)

    assert "Quantum Theory" in tex
    assert "Through Physical Roles" in tex
    assert "When External Conditions Become Quantum Physics" in tex
    assert "The Physical Identity Of A Quantum Mechanism" in tex
    assert "When External Structure Becomes Dynamical" in tex
    assert "Global Composition: Curvature, Frustration, And Memory" in tex
    assert "Equivalence Across Quantum Descriptions" in tex
    assert "Theory Extension By Transfer And Obstruction" in tex
    assert r"\usepackage[T1]{fontenc}" in tex
    assert r"\usepackage[utf8]{inputenc}" in tex
    assert "fontspec" not in tex
    assert "Structured Failure" in tex
    assert "Incomplete Mechanisms" in tex
    assert "Constructor Contract" not in tex
    assert r"\mathcal E_P\ \text{completely positive and trace preserving}" in tex
    assert r"E_y\ge0" in tex
    assert "Sparse Attention Summary" not in tex
    assert "Mechanism Validation Layers" not in tex
    assert "Anomalies And Leads" not in tex
    assert "readout" not in tex.lower()
    assert "unresolved constructor role" not in tex.lower()
    assert "Wikipedia" not in tex
    assert "wikipedia.org" not in tex


def test_public_equation_rows_are_centered_independently():
    tex = render_book(ROOT, max_pages_per_branch=0)

    assert r"\newenvironment{centeredalign}{\[\begin{gathered}}{\end{gathered}\]}" in tex
    for block in tex.split(r"\begin{centeredalign}")[1:]:
        body = block.split(r"\end{centeredalign}", 1)[0]
        assert "&" not in body.replace(r"\&", "")


def test_default_book_expands_every_mapped_topic_once():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    slugs = [
        str(row["slug"])
        for branch in tree["branches"].values()
        for row in branch.get("pages", [])
    ]
    tex = render_book(ROOT)

    assert len(slugs) == 146
    for slug in slugs:
        assert tex.count(rf"\label{{topic:{latex_label(slug)}}}") == 1


def test_topic_map_labels_cannot_masquerade_as_topic_sections():
    tex = r"\section{Topics}\label{page:dirac-equation}"

    assert labels_with_prefix(tex, "page") == ["dirac-equation"]
    assert labels_with_prefix(tex, "topic") == []


def test_predictive_closure_unifies_role_promotion_and_construction():
    assert r"q(h_1)=q(h_2)" in PREDICTIVE_CLOSURE_LATEX
    assert r"T_{\gamma_1}=T_{\gamma_2}" in PREDICTIVE_CLOSURE_LATEX
    assert r"a\longrightarrow X" in ROLE_PROMOTION_CRITERION_LATEX
    assert len(QUANTUM_ROLE_PROMOTIONS) >= 8

    geometry = quantum_role_promotions_for_slug("quantum_gravity")
    entanglement = quantum_role_promotions_for_slug("quantum_entanglement")
    protocol = quantum_role_promotions_for_slug("quantum_simulator")

    assert {row["id"] for row in geometry} >= {"geometry_to_state"}
    assert {row["id"] for row in entanglement} == {"factorization_to_state_space"}
    assert {row["id"] for row in protocol} == {"protocol_to_dynamics"}


def test_quantum_junctions_are_assigned_by_physical_role():
    def page(title):
        return {"wikipedia": {"title": title}, "morphwiki": {}}

    assert explicit_branch(page("Quantum entanglement")) == "states"
    assert explicit_branch(page("Bell's theorem")) == "measurement"
    assert explicit_branch(page("Commutator")) == "incompatibility"
    assert explicit_branch(page("Electron microscope")) == "measurement"
    assert explicit_branch(page("Quantum simulator")) == "protocols"
    assert explicit_branch(page("Quantum biology")) == "states"


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


def test_public_topic_markdown_excludes_scaffolds_and_unverified_links():
    from scripts.export_morphwiki_topic_index import render_markdown

    markdown = render_markdown(
        {
            "wikipedia": {
                "title": "Fermion",
                "summary": "Wikipedia-derived summary.",
                "url": "https://en.wikipedia.org/wiki/Fermion",
            },
            "morphwiki": {
                "takeaway": "Exchange antisymmetry removes coincidence states.",
                "object_view": "Wikipedia-derived summary.",
                "mechanism_view": "The state belongs to an antisymmetric sector.",
                "grammar": {},
                "what_survives": [],
                "what_changes": [],
                "missing_experiments": [],
            },
            "hyperion": {
                "route_profile": {},
                "fiber_profile": {},
                "equation_witnesses": [
                    {
                        "paper_id": "hep-ph/0608226",
                        "arxiv_url": "https://arxiv.org/abs/hep-ph/0608226",
                        "score": 0.9,
                    }
                ],
            },
        }
    )

    assert "Wikipedia" not in markdown
    assert "wikipedia.org" not in markdown
    assert "hep-ph/0608226" not in markdown
    assert "antisymmetric sector" in markdown


def test_quantum_topic_pages_explain_the_construction_in_connected_prose():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    branch = tree["branches"]["context"]
    row = next(
        page
        for page in branch["pages"]
        if page["slug"] == "mathematical_formulation_of_quantum_mechanics"
    )

    markdown = render_derivation_page(ROOT, row, "context", branch)

    assert "## Mechanism" in markdown
    assert "## Physical Meaning" in markdown
    assert "## Invariance And Realization" in markdown
    assert "## Discriminating Consequences" in markdown
    assert "## Checks" not in markdown
    assert "## Connection To The Next Step" not in markdown
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


def test_fermion_page_derives_physical_consequences_and_transfer_limits():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    branch = tree["branches"]["fields"]
    row = next(page for page in branch["pages"] if page["slug"] == "fermion")

    markdown = render_derivation_page(ROOT, row, "fields", branch)

    assert "exchange hole" in markdown
    assert "degeneracy pressure" in markdown
    assert "Jordan--Wigner" in markdown
    assert "hard-core bosons" in markdown
    assert "spectral agreement alone is insufficient" in markdown
    assert derivation_basis(
        json.loads((ROOT / "pages" / "fermion.json").read_text()), row, "fields"
    ) == "topic_model"


def test_public_evidence_requires_source_card_grounding():
    page = {
        "hyperion": {
            "equation_witnesses": [
                {"paper_id": "1111.1111", "equation": "unrelated"},
                {"paper_id": "2222.2222", "equation": "matched"},
            ]
        }
    }
    ungrounded = {"v2_evidence": {"available": False}}
    grounded = {
        "v2_evidence": {
            "available": True,
            "matched_alignment_records": 1,
            "source_examples": [
                {
                    "paper_ids": ["2222.2222"],
                    "equation_preview": "matched",
                    "source_grounded": True,
                }
            ],
        }
    }

    assert top_evidence(page, ungrounded) == []
    assert [row["paper_id"] for row in top_evidence(page, grounded)] == ["2222.2222"]


def test_tree_exports_only_topic_relevant_source_examples():
    index = {
        "available": True,
        "pages": {
            "fermion": {
                "status": "v2_source_grounded",
                "source_examples": [
                    {"paper_ids": ["1111.1111"], "topic_relevance": "not_established"},
                    {"paper_ids": ["2222.2222"], "topic_relevance": "local_context_match"},
                ],
            }
        },
    }

    summary = v2_page_evidence_summary("fermion", index)

    assert summary["available"] is True
    assert summary["matched_source_examples"] == 1
    assert summary["identifier_linked_examples"] == 2
    assert [row["paper_ids"] for row in summary["source_examples"]] == [["2222.2222"]]
    assert summary["source_examples"][0]["source_grounded"] is True


def test_source_card_context_establishes_topic_relevance(tmp_path):
    cards = tmp_path / "source_equation_cards_full_v21.jsonl"
    cards.write_text(
        json.dumps(
            {
                "equation_card_id": "EQC-1",
                "section": {"title": "Fermionic exchange"},
                "context_before": "Identical fermions occupy antisymmetric states.",
                "canonical_equation": r"\{a_i,a_j^\dagger\}=\delta_{ij}",
                "context_after": "This gives the exchange hole.",
            }
        )
        + "\n"
    )
    pages = {
        "fermion": {
            "topic_terms": ["fermion"],
            "source_examples": [{"card_ids": ["EQC-1"]}],
        }
    }

    stats = enrich_with_source_cards(pages, cards)

    assert stats == {"requested_cards": 1, "matched_cards": 1}
    example = pages["fermion"]["source_examples"][0]
    assert example["topic_relevance"] == "local_context_match"
    assert example["topic_terms_matched"] == ["fermion"]


def test_v21_alignment_is_preferred_to_smaller_pilot(tmp_path):
    old = tmp_path / "operator_substrate_source_card_alignment.jsonl"
    v21 = tmp_path / "operator_substrate_v21_source_card_alignment.jsonl"
    old.write_text("{}\n")
    v21.write_text("{}\n")
    old.with_suffix(".json").write_text("{}")
    v21.with_suffix(".json").write_text("{}")

    found = detect(tmp_path, {})

    assert found["source_card_alignment_jsonl"] == str(v21)
