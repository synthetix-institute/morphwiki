"""Independent calculations behind the expanded connecting chapters."""
import json
from pathlib import Path

import sympy as s

from scripts.build_morphwiki_quantum_book import constructor_rewiring_chapter, render_book
from scripts.quantum_connections import CONNECTION_TREATMENTS
from scripts import quantum_framework_chapters as frame

ROOT = Path("discoveries/morphwiki_quantum")
I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
kron = s.kronecker_product


def test_every_connection_is_explained_instead_of_splicing_role_fragments():
    records = json.loads((ROOT / "quantum_constructor_rewiring.json").read_text())["connections"]
    assert set(CONNECTION_TREATMENTS) == {r["id"] for r in records}
    chapter = constructor_rewiring_chapter(ROOT)
    for body in CONNECTION_TREATMENTS.values():
        assert body in chapter
        assert r"\begin{centeredalign}" in body
    assert "Both descriptions give the same" not in chapter
    assert "Equivalence requires" not in chapter
    assert "Related topics:" not in chapter


def test_spin_pictures_and_energy_statistics_agree():
    phase = s.symbols("phi", real=True)
    u = s.diag(s.exp(-s.I*phase/2), s.exp(s.I*phase/2))
    state = s.Matrix([1, 1])/s.sqrt(2)
    rho = state*state.H
    operator = s.simplify(s.expand_complex(u.H*X*u))
    assert s.simplify(s.expand_complex(operator-X*s.cos(phase)+Y*s.sin(phase))) == s.zeros(2)
    assert s.simplify(s.trace(u*rho*u.H*X)-s.cos(phase)) == 0
    assert s.trace(rho*(I+Z)/2) == s.Rational(1, 2)


def test_pulse_order_changes_the_stated_measurement():
    ux, uz = (I-s.I*X)/s.sqrt(2), (I-s.I*Z)/s.sqrt(2)
    up, plus_x = s.Matrix([1, 0]), s.Matrix([1, 1])/s.sqrt(2)
    probability = lambda state: s.simplify((plus_x.H*state)[0]*s.conjugate((plus_x.H*state)[0]))
    assert probability(uz*ux*up) == 1
    assert probability(ux*uz*up) == s.Rational(1, 2)


def test_free_propagator_satisfies_schrodinger_equation():
    x, x0 = s.symbols("x x0", real=True)
    m, hbar, t = s.symbols("m hbar t", positive=True)
    kernel = s.sqrt(m/(2*s.pi*s.I*hbar*t))*s.exp(s.I*m*(x-x0)**2/(2*hbar*t))
    residual = s.I*hbar*s.diff(kernel, t)+hbar**2*s.diff(kernel, x, 2)/(2*m)
    assert s.simplify(residual) == 0


def test_reduced_singlet_is_unpolarized():
    singlet = s.Matrix([0, 1, -1, 0])/s.sqrt(2)
    rho = singlet*singlet.H
    reduced = s.Matrix(2, 2, lambda i, j: sum(rho[2*i+k, 2*j+k] for k in range(2)))
    assert reduced == I/2
    assert s.trace(rho*kron(Z, Z)) == -1


def test_constraint_selects_the_pair_flip():
    constraint = kron(Z, Z)-s.eye(4)
    pair_flip, single_flip = kron(X, X), kron(X, I)
    code = s.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
    assert constraint*code == s.zeros(4, 2)
    assert constraint*pair_flip*code == s.zeros(4, 2)
    assert constraint*single_flip*code != s.zeros(4, 2)
    assert pair_flip*code == code*X


def test_scattering_step_requires_velocity_weighted_transmission():
    ki, ko = s.symbols("k_in k_out", positive=True)
    reflection = (ki-ko)/(ki+ko)
    transmission = 2*ki/(ki+ko)
    assert s.simplify(reflection**2+ko*transmission**2/ki) == 1
    assert s.simplify(reflection**2+transmission**2) != 1


def test_discarded_measurement_record_removes_coherence():
    plus = s.Matrix([1, 1])/s.sqrt(2)
    rho = plus*plus.H
    operators = [(I+Z)/2, (I-Z)/2]
    outcome_states = [op*rho*op.H for op in operators]
    assert sum(outcome_states, s.zeros(2)) == I/2
    assert [s.trace(state) for state in outcome_states] == [s.Rational(1, 2)]*2


def test_spin_encoding_preserves_hamiltonian_and_joint_observable():
    v = s.Matrix([[1, 0], [0, 0], [0, 0], [0, 1]])
    assert v.H*v == I
    assert kron(Z, I)*v == v*Z
    assert kron(X, X)*v == v*X
    assert kron(X, I)*v != v*X


def test_noncommuting_observables_can_share_a_sharp_state():
    a = s.diag(1, 2, 3)
    b = s.Matrix([[4, 0, 0], [0, 0, 1], [0, 1, 0]])
    common = s.Matrix([1, 0, 0])
    assert a*b != b*a
    assert a*common == common
    assert b*common == 4*common


def test_signed_spin_recurrence_and_geometric_potential():
    assert s.cos(2*s.pi/2) == -1
    assert s.cos(2*s.pi) == 1
    k1, k2 = s.symbols("k1 k2", real=True)
    mean, gaussian = (k1+k2)/2, k1*k2
    assert s.expand(mean**2-gaussian-(k1-k2)**2/4) == 0


def test_stochastic_coordinate_is_separate_from_its_mean():
    assert r"\widehat x=(a+a^\dagger)/2" in frame.TRANSFER_EXAMPLE_INTRO
    assert r"dx=[(\varepsilon_2(t)-\kappa/2)x+h]\,dt" in frame.TRANSFER_EXAMPLE_INTRO
    assert r"x=\operatorname{Re}\langle a\rangle" not in frame.TRANSFER_EXAMPLE_INTRO
    assert r"\hbar=1" in frame.TRANSFER_EXAMPLE_INTRO


def test_linear_generator_condition_is_not_asserted_for_nonlinear_state_maps():
    assert "linear map" in frame.TRANSFER_CHAPTER_HEAD
    assert "test" in frame.TRANSFER_CHAPTER_HEAD
    assert r"R_t\alpha=\beta R_s" in frame.NOTATION_APPENDIX
    book = render_book(ROOT)
    assert book.count(r"\chapter{Notation Of The Mechanism Descriptions}") == 1


def test_ring_energy_agrees_with_the_declared_boundary_twist():
    angle, n, flux = s.symbols("varphi n flux", real=True)
    wave = s.exp(s.I*(n+flux)*angle)
    assert s.simplify(-s.diff(wave, angle, 2)/wave) == (n+flux)**2


def test_box_transition_spacing_and_position_matrix_elements():
    x, length = s.symbols("x L", positive=True)
    wall_1 = s.sqrt(2/length)*s.sin(s.pi*x/length)
    wall_2 = s.sqrt(2/length)*s.sin(2*s.pi*x/length)
    slope_0 = 1/s.sqrt(length)
    slope_1 = s.sqrt(2/length)*s.cos(s.pi*x/length)
    assert s.integrate(wall_1*x*wall_2, (x, 0, length)) != 0
    assert s.integrate(slope_0*x*slope_1, (x, 0, length)) != 0
    assert (2**2-1**2)/(1**2-0**2) == 3
