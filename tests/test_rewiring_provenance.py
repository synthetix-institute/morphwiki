import argparse
import importlib.util
import json
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("rewiring", Path(__file__).resolve().parents[1] / "scripts/analyze_quantum_constructor_rewiring.py")
rewiring = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rewiring)


def test_complete_topic_inventory_does_not_claim_verified_connections(tmp_path):
    topics = sorted({slug for entry in rewiring.CONNECTIONS for slug in entry["topics"]})
    (tmp_path / "pages").mkdir()
    tree = {"branches": {"example": {"pages": [{"slug": slug} for slug in topics]}}}
    (tmp_path / "quantum_mechanism_tree.json").write_text(json.dumps(tree))
    for slug in topics:
        (tmp_path / "pages" / f"{slug}.json").write_text(json.dumps({"hyperion": {"route_profile": {}}}))
    args = argparse.Namespace(root=str(tmp_path), out_json=str(tmp_path / "report.json"), out_md=str(tmp_path / "report.md"))
    report = rewiring.build(args)
    assert report["readiness"] == "usable"
    assert report["connection_origin"] == "authored_definitions"
    assert all(row["mathematical_verification"] == "not_performed" for row in report["connections"])
    assert all(row["source_equation_alignment"] == "not_evaluated" for row in report["connections"])
    assert "named topic pages only" in Path(args.out_md).read_text()
