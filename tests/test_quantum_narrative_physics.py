"""Independent checks of corrected energy accounting and geometric coefficients."""
import sympy as s

from scripts.quantum_narratives.fields_a import NARRATIVES as FIELDS_A
from scripts.quantum_narratives.fields_b import NARRATIVES as FIELDS_B


def test_frequency_quench_distinguishes_work_from_final_excitation():
    w0, w1 = s.symbols("omega_0 omega_1", positive=True)
    # Initial ground state: <p^2>=omega_0/2, <x^2>=1/(2 omega_0), hbar=m=1.
    energy = w0/4 + w1**2/(4*w0)
    number = (w0-w1)**2/(4*w0*w1)
    assert s.simplify(energy - w1*(number+s.Rational(1, 2))) == 0
    work, excitation = energy-w0/2, energy-w1/2
    assert s.simplify(work - excitation - (w1-w0)/2) == 0
    substitution = {w0: 1, w1: s.Rational(1, 2)}
    assert work.subs(substitution) == -s.Rational(3, 16)
    assert excitation.subs(substitution) == s.Rational(1, 16)
    text = " ".join(body for _, body in FIELDS_A["quantum_field_theory"])
    assert r"\langle W\rangle=E_f-\omega_0/2" in text
    assert r"E_{\rm exc}=E_f-\omega_1/2" in text


def test_regular_tetrahedron_volume_matches_vertex_determinant():
    length = s.symbols("l", positive=True)
    vertices = [s.Matrix(row)*length for row in
                ([0, 0, 0], [1, 0, 0], [s.Rational(1, 2), s.sqrt(3)/2, 0],
                 [s.Rational(1, 2), s.sqrt(3)/6, s.sqrt(s.Rational(2, 3))])]
    edges = s.Matrix.hstack(*(v-vertices[0] for v in vertices[1:]))
    volume = s.simplify(edges.det()/6)
    assert s.simplify(volume-length**3/(6*s.sqrt(2))) == 0
    text = " ".join(body for _, body in FIELDS_B["spin_foam"])
    assert r"V=\frac{l^3}{6\sqrt2}" in text
