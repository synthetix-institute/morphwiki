# Canonical commutation relation

Translations in position and changes in momentum act differently when their order is reversed. For a particle on the real line, let $X$ multiply a wave function by $x$ and let $P=-i\hbar\partial_x$. On smooth rapidly decreasing wave functions, direct differentiation gives

```math
[X,P]\psi=X(-i\hbar\partial_x\psi)+i\hbar\partial_x(x\psi)
=i\hbar\psi.
```

The additional term comes from differentiating the coordinate itself. It fixes the relation between the two operations, independently of the Hamiltonian subsequently chosen. With standard deviations defined in the prepared state and finite relevant moments, the Cauchy--Schwarz inequality applied to $(X-\langle X\rangle)\psi$ and $(P-\langle P\rangle)\psi$ then gives

```math
\Delta X\,\Delta P\geq\frac{\hbar}{2}.
```

This bound concerns the spread of outcomes in identically prepared ensembles. A measurement-disturbance experiment introduces an apparatus and a sequence of measurements and requires its own dynamical model. The preparation bound should not be substituted for that separate calculation.

The exponentiated relation makes domain issues more transparent. Let $T(a)=\exp(-iaP/\hbar)$ translate a wave function by length $a$, and $B(b)=\exp(ibX/\hbar)$ shift its momentum by $b$. Acting on a wave function in either order gives

```math
[T(a)\psi](x)=\psi(x-a),\qquad
T(a)B(b)=e^{-iab/\hbar}B(b)T(a).
```

The phase is proportional to the phase-space area enclosed by the two moves. It is common to the state for a single path, but can become a relative phase when the two operation sequences form coherent alternatives. This is the physical content of the central extension represented by the Heisenberg group.

No finite-dimensional matrices obey $[X,P]=i\hbar I$ exactly: taking a trace makes the left side zero and the right side nonzero. A truncated oscillator basis or a finite numerical grid must therefore depart from the relation somewhere. Such departures can be approximation effects rather than additional interactions. An exact construction records the representation and tests the states on which the commutator identity is being used.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)


## Relations In The Original Papers

[arXiv:1508.06951, S1.E21](https://arxiv.org/html/1508.06951#S1.E21). Position and momentum obey the canonical commutation relations on a common invariant domain. The surrounding derivation specifies Schwartz functions; the finite-matrix obstruction is calculated separately in the chapter.
