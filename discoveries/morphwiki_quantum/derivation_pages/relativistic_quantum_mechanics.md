# Relativistic quantum mechanics

The $n=2$ level of hydrogen is not a single level. Spectroscopy resolves components 10.9 GHz apart, about $1.3\times10^{-5}$ of the binding energy, while the Schrödinger equation predicts exact degeneracy. The electron moves at about $\alpha c$, so relativistic kinematics is the natural place to look for the splitting.

Replace the nonrelativistic energy by $E^2=p^2c^2+m^2c^4$ and substitute $E\to i\hbar\partial_t$ and $\mathbf p\to-i\hbar\nabla$. For a spin-zero particle in an electrostatic potential energy $V$, this gives the Klein--Gordon equation and its conserved density:

```math
\big(i\hbar\partial_t-V\big)^2\phi=\big(-\hbar^2c^2\nabla^2+m^2c^4\big)\phi,\\
\rho=\frac{i\hbar}{2mc^2}\big(\phi^*\partial_t\phi-\phi\,\partial_t\phi^*\big)-\frac{V}{mc^2}|\phi|^2.
```

The equation is of second order in time, so $\phi$ and $\partial_t\phi$ are independent initial data, and $\rho$ is not positive. A stationary solution with energy $E$ has $\rho=(E-V)|\phi|^2/mc^2$, which is negative for the negative-energy solutions that the quadratic relation allows. The density is therefore a charge density, not a probability density. A single-particle reading is consistent only when the potential is weak compared with $2mc^2$ and varies slowly over the Compton wavelength $\hbar/mc$, which is 386 fm for an electron. Stronger or steeper potentials create particle-antiparticle pairs, as the Klein paradox shows, and require quantum field theory.

For an attractive Coulomb potential $V=-Z\alpha\hbar c/r$, the radial equation keeps the hydrogen form with $l(l+1)$ replaced by $l(l+1)-(Z\alpha)^2$. The exact levels and their expansion in $Z\alpha$ are

```math
E_{nl}=mc^2\Big[1+\frac{(Z\alpha)^2}
{\big(n-l-\frac12+\sqrt{(l+\frac12)^2-(Z\alpha)^2}\big)^2}\Big]^{-1/2},\\
E_{nl}\approx mc^2\Big[1-\frac{(Z\alpha)^2}{2n^2}
-\frac{(Z\alpha)^4}{2n^4}\Big(\frac{n}{l+\frac12}-\frac34\Big)\Big].
```

The second term is the Bohr energy. The third depends on $l$, so relativistic kinematics does lift the degeneracy. For hydrogen it is smaller than the Bohr energy by a factor of order $\alpha^2$, about $10^{-5}$, which matches the observed scale of the splitting. At $n=2$ it places $2s$ below $2p$ by $mc^2\alpha^4/12$, which is 29 GHz. Observation disagrees: $2s_{1/2}$ and $2p_{1/2}$ nearly coincide, and the 10.9 GHz splitting separates $2p_{1/2}$ from $2p_{3/2}$. Schrödinger met this mismatch before publishing his nonrelativistic equation. The Dirac equation, which includes spin, replaces $l+\frac12$ by $j+\frac12$ and reproduces the observed pattern, apart from the 1.06 GHz Lamb shift.

For spin-zero particles the Klein--Gordon equation is correct. In pionic atoms a negative pion replaces the electron. X-ray energies between orbits of high $l$, where the strong interaction is negligible, are calculated with this equation and small QED corrections. Such measurements determine the charged-pion mass. The exact formula also marks a limit. For $s$ states the square root becomes imaginary when $Z\alpha>\frac12$, that is for $Z\geq69$. A point nucleus is then unphysical, and the finite nuclear size must be included.

## References For The Physical Derivation

- [A. Calogeracos and N. Dombey, History and Physics of the Klein Paradox; single-particle relativistic wave equations and pair creation in strong potentials.](https://arxiv.org/abs/quant-ph/9905076)
- [M. Trassinelli, D. F. Anagnostopoulos, G. Borchert and colleagues, Measurement of the charged pion mass using X-ray spectroscopy of exotic atoms; Klein-Gordon energies of pionic atoms.](https://arxiv.org/abs/1605.03300)
