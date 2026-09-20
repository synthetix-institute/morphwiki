"""Independent small calculations for the new worked quantum mechanisms."""
import copy
import json
from pathlib import Path

import pytest
import sympy as s

from scripts.quantum_mechanisms_opening import OPENING
from scripts.quantum_physical_derivations import NARRATIVES
from scripts.quantum_original_sources import load_original_sources, validate_report
from scripts.recover_quantum_original_sources import displays
from scripts.build_morphwiki_quantum_book import page_entry, render_derivation_page, render_book, center_equation_rows

I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)
kron = s.kronecker_product
ROOT = Path("discoveries/morphwiki_quantum")


def comm(a, b):
    return a*b-b*a


def test_interaction_generates_the_correlation_in_the_opening():
    g = s.symbols("g", real=True)
    h = g*kron(Z, Z)  # H / hbar
    a, b = kron(X, I), kron(Y, Z)
    assert s.I*comm(h, a) == -2*g*b
    assert s.I*comm(h, b) == 2*g*a
    assert comm(h, kron(Z, I)) == s.zeros(4)
    x, c, t = s.symbols("x c t", real=True)
    u = s.diag(s.exp(-s.I*g*t), s.exp(s.I*g*t), s.exp(s.I*g*t), s.exp(-s.I*g*t))
    rho = (s.eye(4)+x*a+c*b)/4
    signal = s.simplify(s.expand_complex(s.trace(u*rho*u.adjoint()*a)))
    assert s.trigsimp(signal-x*s.cos(2*g*t)+c*s.sin(2*g*t)) == 0
    assert (x*a+c*b)**2 == (x*x+c*c)*s.eye(4)
    reduced = s.Matrix(2, 2, lambda i,j: sum(rho[2*i+k,2*j+k] for k in range(2)))
    assert reduced == (I+x*X)/2


def test_eliminating_correlation_keeps_initial_term_and_memory():
    g = s.symbols("g", nonzero=True, real=True)
    t, u, x0, c0 = s.symbols("t u x0 c0", real=True)
    x = x0*s.cos(2*g*t)-c0*s.sin(2*g*t)
    integral = s.integrate(x.subs(t,u),(u,0,t))
    assert s.simplify(s.diff(x,t)+2*g*c0+4*g*g*integral) == 0


def test_rabi_probability_and_bloch_positivity():
    d, t = s.symbols("d t", real=True)
    o = s.symbols("o", positive=True)
    h = d*Z+o*X
    assert h*h == (d*d+o*o)*I
    w = s.sqrt(d*d+o*o)
    u = s.cos(w*t/2)*I-s.I*s.sin(w*t/2)*h/w
    assert s.simplify(u.adjoint()*u-I) == s.zeros(2)
    assert s.simplify(u[1,0]*s.conjugate(u[1,0])-o**2*s.sin(w*t/2)**2/w**2) == 0


def test_teleportation_identity_in_the_stated_bell_convention():
    a, b = s.symbols("a b")
    psi = s.Matrix([a,b])
    phi = s.Matrix([1,0,0,1])/s.sqrt(2)
    reconstructed = s.zeros(8,1)
    for m in (0,1):
        for n in (0,1):
            op = X**n*Z**m
            bell = kron(I,op)*phi
            reconstructed += kron(bell,op*psi)/2
            assert Z**m*X**n*op == I
    assert reconstructed == kron(psi,phi)
    rho = s.Matrix([[a,b],[s.conjugate(b),1-a]])
    averaged = sum((X**n*Z**m*rho*Z**m*X**n for m in (0,1) for n in (0,1)),s.zeros(2))/4
    assert s.simplify(averaged-I/2) == s.zeros(2)


def test_three_qubit_code_corrects_bit_flips_but_not_phase_flips():
    code = s.zeros(8,2)
    code[0,0],code[7,1] = 1,1
    errors = [s.eye(8),kron(X,I,I),kron(I,X,I),kron(I,I,X)]
    stabilizers = [kron(Z,Z,I),kron(I,Z,Z)]
    expected = [(1,1),(-1,1),(-1,-1),(1,-1)]
    for error, syndrome in zip(errors,expected):
        affected = error*code
        for operator,sign in zip(stabilizers,syndrome):
            assert operator*affected == sign*affected
        for other in errors:
            block = code.adjoint()*error.adjoint()*other*code
            assert block == block[0,0]*I
    assert code.adjoint()*kron(Z,I,I)*code == Z


def test_exchange_energy_and_spinor_rotation():
    exchange = (kron(X,X)+kron(Y,Y)+kron(Z,Z))/4
    assert exchange.eigenvals() == {s.Rational(-3,4):1,s.Rational(1,4):3}
    assert (-s.I*s.pi*Z).exp() == -I


def test_amplifier_noise_required_by_commutator():
    gain, noise = s.symbols("G n", positive=True)
    # Independent canonical modes: [a,a†]=1 and [b†,b]=-1.
    assert s.simplify(gain-(gain-1)) == 1
    output_var = gain/s.Integer(2)+(gain-1)*(noise+s.Rational(1,2))
    assert s.simplify(output_var.subs(noise,0)-(gain-s.Rational(1,2))) == 0


def test_oscillator_thermal_variance_and_high_temperature_limit():
    beta, e = s.symbols("beta e", positive=True)
    logz = -s.log(2*s.sinh(beta*e/2))
    mean = -s.diff(logz,beta)
    variance = s.diff(logz,beta,2)
    assert s.simplify(mean-e*s.coth(beta*e/2)/2) == 0
    assert s.limit(variance,beta,s.oo) == 0
    assert s.limit(beta*mean,beta,0,dir="+") == 1


def test_source_parser_preserves_first_commutator_and_exact_location():
    html = br'<html><section><h2>Algebra</h2><p class="ltx_para">Operators act on a common domain.</p><table class="ltx_equation" id="eq1"><math alttext="[X,P]=i\hbar I"></math></table></section></html>'
    row, = displays(html)
    assert row["display_id"] == "eq1"
    assert row["equation_latex"] == r"[X,P]=i\hbar I"
    assert not row["syntax_issues"]
    assert row["context"]


def test_split_alignment_cells_are_not_mistaken_for_a_complete_equation():
    html = b'<table class="ltx_equation" id="broken"><math alttext="A"></math><math alttext="="></math><math alttext="B"></math></table>'
    row, = displays(html)
    assert "fragmented_math_cells" in row["syntax_issues"]


def test_original_equations_are_not_silently_promoted_to_corpus_cards():
    report = load_original_sources(ROOT)
    assert report["topic_count"] >= 15
    changed = copy.deepcopy(report)
    changed["records"][0]["equation_latex"] = "0=1"
    assert any("hash mismatch" in e for e in validate_report(changed))
    changed = copy.deepcopy(report)
    changed["records"][0]["v2_card_alignment"] = "confirmed"
    assert any("unsupported source-card" in e for e in validate_report(changed))


def test_every_new_derivation_is_rendered_in_both_editions():
    tree = json.loads((ROOT/"quantum_mechanism_tree.json").read_text())
    found = set()
    for branch_id,branch in tree["branches"].items():
        for row in branch["pages"]:
            slug = row["slug"]
            if slug not in NARRATIVES:
                continue
            found.add(slug)
            tex = page_entry(ROOT,row,1,branch_id,branch)
            md = render_derivation_page(ROOT,row,branch_id,branch)
            for kind,body in NARRATIVES[slug]:
                if kind == "eq":
                    assert body in tex and body in md
            assert "Physical-role overview" not in tex
    assert found == set(NARRATIVES)


def test_book_begins_with_mechanism_before_formal_roles():
    tex = render_book(ROOT)
    assert "Quantum Mechanisms And Their Predictions" in OPENING
    assert tex.index(OPENING) < tex.index(r"\chapter{The Physical Identity Of A Quantum Mechanism}")
    assert tex.index(OPENING) < tex.index(r"\chapter*{When External Conditions Become Quantum Physics}")
    assert "Through Physical Roles" not in tex


def test_centering_preserves_matrix_and_syndrome_table_columns():
    text = r"\begin{centeredalign}A&=\begin{pmatrix}0&1\\1&0\end{pmatrix}\end{centeredalign}"
    result = center_equation_rows(text)
    assert "A=" in result
    assert r"\begin{pmatrix}0&1\\1&0\end{pmatrix}" in result
    book = render_book(ROOT)
    for slug in ("pauli_matrices", "quantum_error_correction"):
        for kind,body in NARRATIVES[slug]:
            if kind == "eq" and "&" in body:
                assert body in book
