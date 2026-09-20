# Heisenberg picture

The Schrodinger and Heisenberg pictures assign time dependence to different parts of the same prediction. With unitary evolution $U(t)$, an initial density operator $\rho_0$ and an observable $O$, the expectation can be evaluated either by evolving the state or by evolving the operator:

```math
\rho_S(t)=U(t)\rho_0U(t)^\dagger,\qquad
O_H(t)=U(t)^\dagger OU(t),\qquad
\operatorname{Tr}[\rho_S(t)O]=\operatorname{Tr}[\rho_0O_H(t)].
```

Differentiating $O_H$ for a time-independent Hamiltonian $H$ gives the Heisenberg equation:

```math
\dot O_H=\frac{i}{\hbar}[H,O_H].
```

The resulting commutators identify which other observables enter the prediction. This is particularly useful when an experiment observes only a small part of a many-body system.

Consider two spins with $H=\hbar g\,Z_1Z_2$, where $X_j,Y_j,Z_j$ denote dimensionless Pauli operators and $g$ is a frequency. If the measured quantity is $x=\langle X_1\rangle$, its derivative contains the correlation $c=\langle Y_1Z_2\rangle$. A second commutator closes the pair:

```math
\dot x=-2gc,\qquad \dot c=2gx,\qquad
x(t)=x(0)\cos(2gt)-c(0)\sin(2gt).
```

The correlation is physically necessary: preparations with the same initial transverse magnetization but different $c(0)$ give different later magnetizations. Its appearance is fixed by the interaction algebra. Retaining the two expectations supplies a complete closed prediction for this observable even though it does not reconstruct every entry of the two-spin density operator.

Eliminating the correlation replaces the pair of first-order equations by a history-dependent equation for $x$. The initial correlation survives as a separate term:

```math
\dot x(t)=-2g c(0)-4g^2\int_0^t x(s)\,ds.
```

Both descriptions give the same signal when they use the same preparation. Discarding the integral or the initial-correlation term gives a different physical prediction. Repeated commutators thus provide a concrete way to construct the set of observables needed by a measurement, and to identify when a smaller description requires memory. For more complicated interactions the sequence may generate a much larger space rather than closing after two steps.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)


## Relations In The Original Papers

[arXiv:1508.06951, S3.Ex177](https://arxiv.org/html/1508.06951#S3.Ex177). State evolution and observable evolution give identical spectral probabilities. The source chooses its unitary convention explicitly. The two-spin calculation uses U = exp(-iHt/hbar).
