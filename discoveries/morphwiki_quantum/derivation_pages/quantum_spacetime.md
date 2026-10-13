# Quantum spacetime

To locate an event within a distance $\Delta x$, a probe must carry momentum of order $\hbar/\Delta x$. Its energy also curves spacetime. When $\Delta x$ approaches the Planck length, the probe would collapse into a black hole larger than the region probed. Heuristic arguments of this kind, together with estimates from string scattering, suggest a smallest resolvable length. Quantum spacetime models encode it by deforming commutators of positions and momenta. None has been derived from a complete theory or confirmed by experiment. They are proposals whose consequences can be calculated and bounded.

A one-dimensional model of Kempf, Mangano and Mann replaces the canonical commutator by a momentum-dependent one. The Robertson relation $\Delta x\,\Delta p\geq|\langle[x,p]\rangle|/2$, with $\langle p^2\rangle=(\Delta p)^2+\langle p\rangle^2$, then gives

```math
[x,p]=i\hbar\big(1+\beta p^2\big),\qquad
\Delta x\,\Delta p\geq\frac\hbar2\Big(1+\beta(\Delta p)^2+\beta\langle p\rangle^2\Big),
```

where $\beta>0$ has dimensions of inverse momentum squared. For $\langle p\rangle=0$, dividing by $\Delta p$ shows that the bound on $\Delta x$ is smallest at $\Delta p=1/\sqrt\beta$. No state can have a smaller position uncertainty than

```math
\Delta x_{\min}=\hbar\sqrt\beta,\qquad
\beta=\frac{\beta_0}{(m_Pc)^2}\;\Rightarrow\;\Delta x_{\min}=\sqrt{\beta_0}\,l_P,
```

with $\beta_0$ dimensionless and $m_P$ the Planck mass. Position eigenstates no longer exist; the most localized states are packets of width $\Delta x_{\min}$. Momentum can still be sharp, and a momentum-space wave function describes the state. As an effective description the model is meant for momenta well below $m_Pc/\sqrt{\beta_0}$, where the deformation is small.

A harmonic oscillator of mass $m$ and frequency $\omega$ shows a concrete consequence. In the variable $u=\arctan(\sqrt\beta\,p)$ the position acts as $i\hbar\sqrt\beta\,\partial_u$. The eigenvalue problem becomes a Pöschl--Teller equation with the exact spectrum

```math
E_n=\hbar\omega\Big[\big(n+\tfrac12\big)\sqrt{1+\tfrac{\kappa^2}{4}}+\frac\kappa2\big(n^2+n+\tfrac12\big)\Big],
\qquad \kappa=\beta m\hbar\omega.
```

For small $\kappa$ each level shifts by $\beta m\hbar^2\omega^2(2n^2+2n+1)/4$, and the spacing grows linearly with $n$. The size is the issue. For an electron with $\hbar\omega=1$ meV and $\beta_0=1$, $\kappa\approx3\times10^{-54}$. Experiments therefore bound $\beta_0$ rather than measure it, and the bounds lie many orders of magnitude above one. How the deformation applies to composite bodies is unresolved, which complicates tests with massive oscillators.

Other proposals act on spacetime coordinates directly. Snyder in 1947 made coordinates fail to commute, with commutators proportional to the Lorentz generators and to a length squared. Lorentz symmetry is kept, and the spatial coordinates acquire discrete spectra. Doplicher, Fredenhagen and Roberts derived spacetime uncertainty relations such as $\Delta x^0\sum_i\Delta x^i\gtrsim l_P^2$. Their condition is that localizing an event must not create a horizon. Loop quantum gravity instead quantizes areas and volumes of space, and string theory limits resolution through the size of the string. The scales involved are set out under quantum gravity.

## References For The Physical Derivation

- [A. Kempf, G. Mangano and R. B. Mann, Hilbert Space Representation of the Minimal Length Uncertainty Relation; deformed commutator, minimal length and the oscillator spectrum.](https://arxiv.org/abs/hep-th/9412167)
- [S. Hossenfelder, Minimal Length Scale Scenarios for Quantum Gravity; arguments for a minimal length, Snyder-type models and experimental bounds.](https://arxiv.org/abs/1203.6191)
- [S. Doplicher, K. Fredenhagen and J. E. Roberts, The quantum structure of spacetime at the Planck scale and quantum fields; spacetime uncertainty relations from the absence of horizons.](https://arxiv.org/abs/hep-th/0303037)
