# Chapter 3: A Mechanism Page

Open the worked example:

```text
discoveries/morphwiki_quantum/derivation_pages/schr_dinger_equation.md
```

The familiar description says that the Schrödinger equation governs a quantum
wavefunction and records its historical origin. The mechanism page asks what
role the equation plays in the field’s construction.

## Operational Reading

```math
i\hbar\,\partial_t|\psi(t)\rangle=H|\psi(t)\rangle,
\qquad
|\psi(t)\rangle=e^{-iHt/\hbar}|\psi(0)\rangle.
```

The page reads this as:

- **carrier:** state vector, wavefunction or density operator on a declared
  domain;
- **operator:** Hamiltonian or lawful generator;
- **closure:** self-adjointness and boundary/domain conditions;
- **readout:** probabilities, transition amplitudes, spectra or conserved
  quantities;
- **check:** norm, positivity or another required invariant is preserved.

The statement

```math
\frac{d}{dt}\langle\psi(t)|\psi(t)\rangle=0
\quad(H=H^\dagger)
```

connects the operator to an admissibility consequence. This is more useful for
construction than a historical paragraph because it states what must remain
true when the equation is represented in another basis or realized in another
system.

## Stable and Realization-Specific Clauses

The page separately lists what remains stable and what changes. The generator
relation may persist while the carrier is described as a particle, field,
qubit or excitation. Coordinates, basis, detector and boundary realization
can change without becoming the identity of the operator itself.

This is the minimum standard for a MorphWiki page: it must expose enough
structure to be challenged, not merely enough prose to sound complete.

Next: [Infer the constructor spine](04_constructor_spine.md).
