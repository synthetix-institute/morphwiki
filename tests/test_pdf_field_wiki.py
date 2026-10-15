import json

from scripts.build_morphwiki_field_from_pdfs import build_field_wiki, render_mechanism_page


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


def test_carrier_indicators_are_local_to_the_source_passage(tmp_path):
    papers = tmp_path / "papers"
    papers.mkdir()
    text = "A probability distribution obeys stochastic diffusion. partial_t p = D nabla^2 p"
    (papers / "diffusion.txt").write_text(text, encoding="utf-8")

    def build(destination):
        build_field_wiki(pdf_dir=papers, field_id="local_evidence", label="Local evidence", description="Test",
                         out_dir=destination, max_docs=10, max_chunks_per_doc=10, max_chars=1200,
                         max_anchors=8, max_pages=8, extensions=(".txt",))
        pages = json.loads((destination / "field_wiki.json").read_text())["pages"]
        return next(page for page in pages if "txt:diffusion.txt" in page["sources"])

    before = build(tmp_path / "before")
    (papers / "network.txt").write_text(
        "A graph network has nodes, edges and adjacency. A graph Laplacian acts on the network. y = L x",
        encoding="utf-8")
    after = build(tmp_path / "after")
    assert before["substrates"] == after["substrates"]
    assert after["substrate_evidence_scope"] == "source_chunk"
    assert any(row["id"] == "probability_space" for row in after["substrates"])
    assert all(row["id"] != "graph_topology" for row in after["substrates"])


def test_legacy_record_without_local_scores_leaves_carrier_unresolved():
    page, record = render_mechanism_page(record={"title": "Legacy source"}, field_label="Test")
    assert record["substrates"] == [] and record["substrate_evidence_scope"] == "unresolved"
    assert "no source-local carrier indicator" in page
