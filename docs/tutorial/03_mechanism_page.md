# Write a page around a calculable prediction

A page about the Schrödinger equation should explain how an initial quantum
state determines later probabilities. Start with a time-independent
self-adjoint Hamiltonian $H$, a state $|\psi(0)\rangle$ in the chosen
Hilbert space, and a measurement described by an effect $E$.
The prediction is

```math
|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle,
\qquad
p_E(t)=\langle\psi(t)|E|\psi(t)\rangle.
```

The equation connects evolution to something an experiment can determine.
The state, Hamiltonian, domain and measurement are introduced because this
prediction needs them, not because a page template has an empty slot.

## Explain why the conditions matter

Self-adjointness gives unitary evolution for the closed system. In finite
dimensions this means a Hermitian Hamiltonian matrix. For an unbounded
differential operator, its domain and boundary conditions are essential;
a formally symmetric differential expression alone is insufficient.

A change of orthonormal basis transforms the state, Hamiltonian and effect
together. With a unitary $U$, replacing them by
$U|\psi\rangle$, $UHU^\dagger$ and $UEU^\dagger$ preserves
the probability. Changing only the physical boundary is a different operation:
it may change the generator and its spectrum rather than re-express the same
experiment.

These distinctions give the reader a reason for the conditions and a concrete
test of the proposed correspondence.

## Connect this page to the next question

For the interacting-spin example, the full state evolution predicts the
magnetization, but the experiment may need only a few expectation values.
The next question is which ones. Taking a Heisenberg derivative of the measured
operator produces the correlation that must be retained. That is a natural
connection from the Schrödinger page to composite states and observable
dynamics, developed in [the quantum calculation](08_quantum_construction.md).

## Locate the explanation in the repository

The generated page is
[schr_dinger_equation.md](../../discoveries/morphwiki_quantum/derivation_pages/schr_dinger_equation.md).
The [book builder](../../scripts/build_morphwiki_quantum_book.py) combines
topic-specific treatments, source evidence and fallbacks. A durable content
correction belongs in the relevant input or renderer; editing only a generated
page will be lost on rebuild.

**Exercise.** Read one generated page and identify the physical question, the
equation that answers it, and the assumption that permits the step. If it
contains only a role list, add the missing relation to the authored treatment
before increasing the word count.

[Next: how topics are placed](04_constructor_spine.md) · [Tutorial](index.md)
