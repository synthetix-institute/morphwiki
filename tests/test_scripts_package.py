from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_local_scripts_beats_a_later_regular_package(tmp_path):
    competitor = tmp_path / "scripts"
    competitor.mkdir()
    (competitor / "__init__.py").write_text("raise RuntimeError('foreign scripts imported')\n")
    code = (
        "import sys; "
        f"sys.path[:0] = [{str(ROOT)!r}, {str(tmp_path)!r}]; "
        "import scripts; "
        f"assert scripts.__file__ == {str(ROOT / 'scripts/__init__.py')!r}; "
        "import scripts.build_morphwiki_v2_quantum_evidence_index; "
        "import scripts.audit_morphwiki_v2_quantum_evidence_index; "
        "import scripts.build_morphwiki_field_from_pdfs"
    )
    result = subprocess.run([sys.executable, "-B", "-c", code], cwd=ROOT,
                            text=True, capture_output=True)
    assert result.returncode == 0, result.stderr
