# Fourier transform

A free particle propagates most simply in momentum space, where each momentum component accumulates its own phase. A localized detector, however, asks for a position probability. The Fourier transform connects these descriptions while preserving the physical state. On the real line, for a square-integrable wave function $\psi$ and momentum $p$, take

```math
\widetilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{\mathbb R}
e^{-ipx/\hbar}\psi(x)\,dx,\qquad
\int|\widetilde\psi(p)|^2dp=\int|\psi(x)|^2dx.
```

For wave functions on a common suitable domain, integration by parts carries the position-space momentum operator $-i\hbar\partial_x$ into multiplication by $p$. Multiplication by position becomes $i\hbar\partial_p$. The kinetic equation and the detector must both be transformed:

```math
\mathcal F(-i\hbar\partial_x)\mathcal F^{-1}=p,\qquad
\mathcal F x\mathcal F^{-1}=i\hbar\partial_p,\qquad
\widetilde H=\frac{p^2}{2m}+V(i\hbar\partial_p).
```

The last expression is immediately useful for polynomial potentials; for a general potential, multiplication in position space is represented by an integral kernel in momentum space. A local interaction can therefore become nonlocal in the new coordinates without changing the theory. Similarity of displayed formulas is neither necessary nor sufficient for physical equivalence.

For a normalized Gaussian packet with initial position variance $\sigma_x^2$, zero position-momentum covariance and minimum uncertainty, the free evolution multiplies each momentum amplitude by $\exp[-ip^2t/(2m\hbar)]$. Transforming back gives

```math
\operatorname{Var}x(t)=\sigma_x^2+
\frac{\hbar^2t^2}{4m^2\sigma_x^2}.
```

The packet broadens because its different momentum components separate during propagation. The momentum distribution itself remains unchanged. This provides a direct comparison between descriptions: one representation makes the conservation of momentum probabilities explicit, while the other displays the spatial spreading produced by those same components.

Boundaries change this correspondence. Periodic functions on a finite interval have a discrete Fourier series; Dirichlet eigenfunctions lead instead to a sine expansion. Surface terms must vanish under the actual boundary conditions before the integration-by-parts identity defines the required operator map. The operation of Fourier transformation is transferable, but the domain and measure determine which transform and which spectrum describe the physical system.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)


## Relations In The Original Papers

[arXiv:1508.06951, S2.EGx7](https://arxiv.org/html/1508.06951#S2.EGx7). The Fourier transformation expresses the position wavefunction in wavevector coordinates. This source uses wavevector k; the chapter uses momentum p = hbar k with the corresponding normalization.
