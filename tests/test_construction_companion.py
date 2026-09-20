import importlib.util
import json
from pathlib import Path

import pytest

SPEC = importlib.util.spec_from_file_location("companion", Path(__file__).resolve().parents[1] / "scripts/build_construction_companion.py")
companion = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(companion)


def test_rejects_false_source_or_discovery_promotion():
    report = {"status": "verified_local_generator_identity", "source_alignment_verified": True,
              "novelty_established": False, "residual_coefficients": ["0", "0"]}
    with pytest.raises(ValueError, match="promoted"):
        companion.checked_report("affine_transfer", report)


def test_rejects_unverified_diffusion_coefficient():
    report = {"status": "verified_local_generator_identity", "source_alignment_verified": False,
              "novelty_established": False, "residual_coefficients": ["0", "2*x"]}
    with pytest.raises(ValueError, match="Both"):
        companion.checked_report("affine_transfer", report)


def test_missing_sibling_is_explicit(tmp_path):
    with pytest.raises(ValueError, match="standalone FieldBridge"):
        companion.build(tmp_path, tmp_path / "output")


def test_inverse_design_checks_dynamics_and_infeasible_comparison():
    report = {"status": "calculated", "source_alignment_verified": False,
              "novelty_established": False, "construction": {"basis": [["1", "1", "1"]]},
              "nearest_neighbor_comparison": {"solution_dimension": 0},
              "checks": {"max_full_hamiltonian_error": 1e-14, "uniform_coupling_control_fires": True}}
    companion.checked_report("spin_cancellation_design", report)
    report["checks"]["max_full_hamiltonian_error"] = float("nan")
    with pytest.raises(ValueError, match="Inverse design"):
        companion.checked_report("spin_cancellation_design", report)
    report["checks"]["max_full_hamiltonian_error"] = 1e-14
    report["nearest_neighbor_comparison"]["solution_dimension"] = 1
    with pytest.raises(ValueError, match="Inverse design"):
        companion.checked_report("spin_cancellation_design", report)
