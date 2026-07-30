import json

from scripts.build_morphwiki_field_from_pdfs import build_field_wiki


def test_build_field_wiki_from_document_folder(tmp_path):
    papers = tmp_path / "papers"
    papers.mkdir()
    (papers / "active_memory.txt").write_text(
        """
        A preparation protocol applies a light pulse to material state q.
        The transport operator evolves q under boundary condition C(q)=0.
        Conductance is the readout. A reset control erases the retained state.
        partial_t q = D nabla^2 q - q/tau
        """,
        encoding="utf-8",
    )

    report = build_field_wiki(
        pdf_dir=papers,
        field_id="active_memory",
        label="Active Memory",
        description="Test corpus.",
        out_dir=tmp_path / "wiki",
        max_docs=10,
        max_chunks_per_doc=10,
        max_chars=1200,
        max_anchors=8,
        max_pages=8,
        extensions=(".txt",),
    )

    assert report["documents"] == 1
    assert report["pages"] >= 1
    assert (tmp_path / "wiki" / "index.md").exists()
    payload = json.loads(
        (tmp_path / "wiki" / "field_wiki.json").read_text(encoding="utf-8")
    )
    assert payload["artifact_type"] == "morphwiki_pdf_field_wiki"
    assert payload["constructor_role_profile"]["protocol_execution"] > 0
    page_path = tmp_path / "wiki" / "pages" / payload["pages"][0]["filename"]
    page = page_path.read_text(encoding="utf-8")
    assert "## Topic View" in page
    assert "## Mechanism View" in page
    assert "### P: protocol" in page
    assert "partial_t q" in page
