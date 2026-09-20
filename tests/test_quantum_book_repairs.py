import json
from pathlib import Path

import pytest

from scripts.quantum_source_evidence import canonical_arxiv_id, equation_issues, evidence_issues
from scripts.revalidate_quantum_evidence_index import revalidate
from scripts.build_morphwiki_quantum_book import (
    TOPIC_CONSTRUCTOR_OVERRIDES, constructor_block, page_entry, render_derivation_page, top_evidence,
)
from scripts.audit_quantum_book_content_preservation import topic_equations_in_tex, noncanonical_arxiv_links
from scripts.build_morphwiki_v2_quantum_evidence_index import source_first_topic_candidates

ROOT = Path("discoveries/morphwiki_quantum")


def witness(**updates):
    example = {"paper_ids": ["hep-ph/0001312", "hep-ph0001312"], "row_ids": [1], "card_ids": ["card"],
               "equation_preview": r"[D_\mu,D_\nu]=igF_{\mu\nu}", "local_context": "Gauge theory: the covariant derivative gives the field strength.",
               "topic_relevance": "local_context_match", "relation_relevance": "relation_context_match",
               "relation_terms_matched": ["field strength"], "source_grounded": True}
    example.update(updates)
    return example


@pytest.mark.parametrize("identifier,expected", [
    ("cond-mat0005069", "cond-mat/0005069"), ("math.GT0301234v2", "math.GT/0301234v2"),
    ("https://arxiv.org/abs/2401.12345v3", "2401.12345v3"), ("not-a-paper", ""),
])
def test_canonical_identifiers(identifier, expected):
    assert canonical_arxiv_id(identifier) == expected


@pytest.mark.parametrize("equation", ["omega &=&", "nu}&=&", r"\tilde G^<_{", "A=", "=B", "bare text"])
def test_truncated_equations_cannot_be_published(equation):
    assert equation_issues(equation)
    assert top_evidence({}, {"v2_evidence": {"available": True, "source_examples": [witness(equation_preview=equation)]}}) == []


def test_topic_mention_is_not_relation_grounding():
    ex = witness(relation_terms_matched=[], relation_relevance="topic_equation_match")
    assert "relation_not_established" in evidence_issues(ex)
    report = revalidate({"pages": {"qcd": {"status": "v2_source_grounded", "source_examples": [ex]}}})
    assert report["pages"]["qcd"]["status"] == "v2_identifier_linked"
    assert len(report["pages"]["qcd"]["source_examples"]) == 1


def test_aliases_and_feature_rows_do_not_multiply_witnesses():
    a, b = witness(), witness(row_ids=[2])
    report = revalidate({"pages": {"gauge": {"status": "v2_source_grounded", "source_examples": [a, b]}}})
    examples = report["pages"]["gauge"]["source_examples"]
    assert len(examples) == 1
    assert examples[0]["row_ids"] == [1, 2]
    links = top_evidence({"hyperion": {"equation_witnesses": [{"paper_id": "hep-ph/0001312", "equation": "WRONG"}]}},
                         {"v2_evidence": {"available": True, "source_examples": examples}})
    assert len(links) == 1
    assert links[0]["equation_excerpt"] == a["equation_preview"]


def test_conversion_prose_cannot_remove_equation():
    tex = constructor_block("Example", "generators", {"slug": "example"}, {}, [], {"conversion_form": ["A state has a generator."]})
    assert "Defining Relations" in tex
    assert r"\begin{centeredalign}" in tex


def test_book_audit_inspects_tex_equations_and_link_syntax():
    tex = r"\section{A}\label{topic:a}text\section{B}\label{topic:b}\[x=y\]"
    assert topic_equations_in_tex(tex) == {"a": False, "b": True}
    assert noncanonical_arxiv_links(r"\href{https://arxiv.org/abs/cond-mat0005069}{x}") == ["cond-mat0005069"]


def test_qcd_and_qed_have_specific_physical_derivations_in_both_outputs():
    tree = json.loads((ROOT / "quantum_mechanism_tree.json").read_text())
    for slug in ("quantum_chromodynamics", "quantum_electrodynamics"):
        branch = tree["branches"]["fields"]
        row = next(r for r in branch["pages"] if r["slug"] == slug)
        tex = page_entry(ROOT, row, 1, "fields", branch)
        md = render_derivation_page(ROOT, row, "fields", branch)
        assert "References For The Physical Derivation" in tex
        for equation in TOPIC_CONSTRUCTOR_OVERRIDES[slug]["equations"]:
            assert equation in tex
            assert equation in md
        assert "many-mode extension" not in tex
        assert "1904.13372" not in tex


def test_raw_display_recovers_a_broken_canonical_fragment(tmp_path):
    cards = tmp_path / "cards.jsonl"
    cards.write_text(json.dumps({"equation_card_id": "card", "source_id": "2401.00001",
        "canonical_equation": "nu}&=&", "raw_equation": r"[D_\mu,D_\nu]=igF_{\mu\nu}",
        "context_before": "Gauge theory relates the covariant derivative to field strength.",
        "clean_endpoint": True, "quality_flags": ["has_relation"]}) + "\n")
    candidates, _ = source_first_topic_candidates({"gauge_theory": {"title": "Gauge theory"}}, {"gauge_theory": "fields"}, cards, 4, {"card"})
    assert candidates["card"][0][1]["equation_preview"] == r"[D_\mu,D_\nu]=igF_{\mu\nu}"


def test_physical_counterexamples_to_old_claims():
    sym = pytest.importorskip("sympy")
    x = sym.Matrix([[0, 1], [1, 0]])
    z = sym.diag(1, -1)
    u = (sym.eye(2) + sym.I*x) / sym.sqrt(2)
    transformed = sym.simplify(u*z*u.H)
    assert transformed != z
    assert sym.trace(transformed**2) == sym.trace(z**2)
    # Two fermions in the same spatial orbital: the spin singlet is nonzero and antisymmetric.
    singlet = sym.Matrix([0, 1, -1, 0]) / sym.sqrt(2)
    swap = sym.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    assert swap*singlet == -singlet
    assert (singlet.H*singlet)[0] == 1


def test_leading_commutator_is_not_a_gathered_alignment_option():
    source = (Path(__file__).parents[1] / "scripts/build_morphwiki_quantum_book.py").read_text()
    assert r"\begin{gathered}[c]" in source
    assert r"\begin{gathered}}" not in source
