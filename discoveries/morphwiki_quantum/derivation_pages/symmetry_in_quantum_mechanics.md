# Symmetry in quantum mechanics

A rotation of an isolated atom changes the description of its orientation while leaving transition probabilities unchanged. Such transformations act on quantum rays and are represented, under the hypotheses of Wigner's theorem, by unitary or antiunitary maps. Continuous transformations connected to the identity are represented unitarily; their generators turn an invariance of probabilities into a relation between operators.

Let a one-parameter symmetry be $U(\epsilon)=\exp(-i\epsilon G/\hbar)$, with self-adjoint generator $G$ and a parameter whose units make the exponent dimensionless. For a time-independent Hamiltonian, invariance under this group implies

```math
U(\epsilon)HU(\epsilon)^\dagger=H,
\qquad [G,H]=0,\qquad \frac{d}{dt}\langle G\rangle=0.
```

The last equality follows from the Heisenberg equation when $G$ has no explicit time dependence and the operator domains permit the calculation. Spatial translations give momentum conservation; rotations give angular momentum conservation. A boundary or an external field can break the symmetry even if a local bulk term remains invariant. Conservation therefore belongs to the full physical problem.

Symmetry also controls which transitions can occur. Suppose parity $\Pi$ commutes with $H$ and two nondegenerate states have definite parities $\pi_i,\pi_f=\pm1$. Position is odd under parity. Inserting $\Pi^\dagger\Pi$ into its matrix element yields

```math
\langle f|X|i\rangle=-\pi_f\pi_i\langle f|X|i\rangle.
```

The electric-dipole matrix element vanishes for states of the same parity. This is a selection rule for the pair consisting of the dynamics and the coupling to the probe. It can suppress a spectral line without creating an additional conserved quantity. Conversely, an accidental equality of two energy differences can merge lines without imposing any selection rule. These mechanisms must be distinguished when a spectral pattern simplifies.

For a proposed transfer between physical systems, a shared symmetry is useful because it restricts the admissible target interactions and observables. It does not determine their coupling constants or all matrix elements. The construction becomes predictive only after the target representation, Hamiltonian and measurement are fixed. Symmetry then supplies exact relations, such as forbidden transitions, that can test the proposed realization.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)
