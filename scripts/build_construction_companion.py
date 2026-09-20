#!/usr/bin/env python3
"""Reproduce the companion calculations using an explicit sibling repository.

No book regeneration, network retrieval or source-alignment promotion occurs.
Each report retains its authored-benchmark provenance. The input equations,
calculation source hashes and software versions travel with the output.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import shutil
import subprocess
import sys

CASES = ("affine_transfer", "ito_square", "quantum_correlations")
EXPECTED = {"affine_transfer": "verified_local_generator_identity",
            "ito_square": "verified_local_generator_identity",
            "quantum_correlations": "verified_finite_dimensional_closure",
            "spin_cancellation_design": "calculated"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_report(name, report):
    if report.get("status") != EXPECTED[name]:
        raise ValueError(f"Calculation did not verify: {name}")
    if report.get("source_alignment_verified") is not False or report.get("novelty_established") is not False:
        raise ValueError("Authored examples must not be promoted to source-grounded discoveries")
    if name == "spin_cancellation_design":
        checks = report.get("checks", {})
        error = checks.get("max_full_hamiltonian_error", float("inf"))
        if (report.get("construction", {}).get("basis") != [["1", "1", "1"]]
                or report.get("nearest_neighbor_comparison", {}).get("solution_dimension") != 0
                or not math.isfinite(error) or error > 1e-10
                or checks.get("uniform_coupling_control_fires") is not True):
            raise ValueError("Inverse design or its direct-dynamics control failed")
    elif name == "quantum_correlations":
        if report.get("observable_dimension") != 2 or report.get("closed_identities") != [True, True]:
            raise ValueError("Expected two-observable quantum closure")
    else:
        if report.get("residual_coefficients") != ["0", "0"]:
            raise ValueError("Both local generator coefficients must agree")
        if name == "ito_square" and report.get("omission_control", {}).get("residual_d_phi") != "1":
            raise ValueError("Missing Ito drift must leave residual 1")


def build(root, output, python=sys.executable, include_spin_design=False):
    root, output = root.resolve(), output.resolve()
    if not (root / "fieldbridge/verification.py").is_file():
        raise ValueError("Pass the updated standalone FieldBridge repository via --fieldbridge-root")
    output.mkdir(parents=True, exist_ok=True)
    manifest_path = output / "manifest.json"
    manifest = {"schema": "morphwiki-construction-companion/1", "status": "building",
                "scope": "Known mathematical constructions, not new physical discoveries or source-aligned book citations.",
                "calculations": []}
    # Invalidate an earlier complete result before a rerun can fail.
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    (output / "README.md").write_text("Construction companion is being rebuilt. Check manifest.json before using the results.\n")
    manifest["implementation_sha256"] = {
        path: digest(root / path) for path in ("fieldbridge/verification.py", "fieldbridge/cli.py", "fieldbridge/__main__.py", "pyproject.toml")}
    manifest["software"] = json.loads(subprocess.check_output(
        [python, "-B", "-c", "import json,sys,sympy; print(json.dumps({'python':sys.version.split()[0],'sympy':sympy.__version__}))"],
        text=True, cwd=root))
    try:
        if include_spin_design:
            manifest["implementation_sha256"]["fieldbridge/inverse_spin.py"] = digest(root / "fieldbridge/inverse_spin.py")
        for name in CASES + (("spin_cancellation_design",) if include_spin_design else ()):
            source = root / "examples/construction" / f"{name}.json"
            case_dir = output / name
            inverse = name == "spin_cancellation_design"
            command = "design-spin-cancellation" if inverse else "verify-construction"
            basename = "design" if inverse else "calculation"
            process = subprocess.run([python, "-B", "-m", "fieldbridge", command, str(source),
                                      "--out-dir", str(case_dir)], cwd=root, capture_output=True, text=True)
            if process.returncode:
                raise RuntimeError(f"FieldBridge calculation {name} failed:\n{process.stderr.strip()}")
            report_path = case_dir / f"{basename}.json"
            report = json.loads(report_path.read_text())
            checked_report(name, report)
            specification = json.loads(source.read_text())
            expected_hash = hashlib.sha256(json.dumps(specification, sort_keys=True).encode()).hexdigest()
            if report["input_sha256"] != expected_hash:
                raise ValueError("Calculation does not correspond to the supplied equations")
            shutil.copy2(source, case_dir / "input.json")
            manifest["calculations"].append({"id": name, "report": f"{name}/{basename}.json",
                "readable_report": f"{name}/{basename}.md",
                "input": f"{name}/input.json", "report_sha256": digest(report_path),
                "input_sha256": report["input_sha256"], "status": report["status"],
                "source_alignment_verified": False, "novelty_established": False})
        manifest["status"] = "complete"
    except Exception:
        manifest["status"] = "failed"
        (output / "README.md").write_text("Construction companion failed. See manifest.json and the reported exception; this is not a completed build.\n")
        raise
    finally:
        manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    lines = ["# Reproducible mechanism constructions", "",
             "These calculations derive consequences of supplied equations. Their input records are authored benchmarks, not equations recovered from the quantum book.", "",
             "| Construction | Derived result | Omission or comparison |",
             "| --- | --- | --- |",
             "| Affine stochastic map | Drift and variance transform with zero local generator residual. | The quadratic-variation drift is zero for an affine map. |",
             "| Squared stochastic coordinate | Target drift is 2 theta + 2 - 2 alpha y; variance is 4 y. | Omitting the additional drift leaves residual 1. |",
             "| Two coupled spins | Two observable expectations form an exact closed dynamics. | Transverse magnetization alone fails to close for nonzero coupling. |", "",
             "## Reproduction records", ""]
    for item in manifest["calculations"]:
        name = item["id"]
        lines.append(f"- [{name}: equations]({name}/input.json), [calculation]({item['readable_report']})")
    if include_spin_design:
        lines += ["", "The inverse spin example solves for uniform Ising couplings, verifies the polarization against full Hamiltonian evolution, and shows that nearest-neighbour Ising interactions give no nonzero solution within this commuting construction. It is an authored design example, not an additional source-grounded discovery."]
    lines += ["", "The manifest records the calculation source hashes and software versions. Boundary realization is outside the scalar local-generator proof; the finite-dimensional Hamiltonian closure holds for every initial density matrix.", ""]
    (output / "README.md").write_text("\n".join(lines))
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fieldbridge-root", required=True, type=Path)
    parser.add_argument("--out-dir", type=Path, default=Path("build/construction_companion"))
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--include-spin-design", action="store_true", help="Also solve and reproduce the three-spin inverse interaction design.")
    args = parser.parse_args()
    report = build(args.fieldbridge_root, args.out_dir, args.python, args.include_spin_design)
    print(json.dumps({"status": report["status"], "calculations": len(report["calculations"]),
                      "output": str(args.out_dir.resolve())}, indent=2))


if __name__ == "__main__":
    main()
