# Path integral formulation

A neutron interferometer is tilted so that one beam travels higher in the Earth's gravitational field than the other. The interference signal oscillates as the tilt changes, although the two beams follow nearly identical classical trajectories. The path-integral formulation computes such phases directly from the classical action.

In this formulation the amplitude to go from $x_i$ to $x_f$ is a sum over every history $x(t)$ connecting them, each weighted by $e^{iS[x]/\hbar}$. Here $S=\int L\,dt$ is the classical action and $L=m\dot x^2/2-V(x)$ the Lagrangian. Consider a small deformation $x+\delta x$ with fixed endpoints. The change of action is

```math
\delta S=\int_{t_i}^{t_f}\big[-m\ddot x-V'(x)\big]\,\delta x\,dt,\qquad
\delta S=0\ \Longleftrightarrow\ m\ddot x=-V'(x).
```

Where $\delta S\neq0$, neighbouring paths have phases that differ by many times $2\pi$ once $S$ is large compared with $\hbar$, and their contributions cancel. Paths near a stationary path add with nearly equal phases. The amplitude is therefore dominated by thin tubes around classical trajectories, within which the action varies by about $\hbar$. Expanding the action to second order about each classical path gives the semiclassical propagator

```math
K\simeq\sum_{\mathrm{cl}}\frac{1}{\sqrt{2\pi i\hbar}}
\Big|\frac{\partial^2S_{\mathrm{cl}}}{\partial x_i\,\partial x_f}\Big|^{1/2}
\exp\Big(\frac{i}{\hbar}S_{\mathrm{cl}}-\frac{i\pi\mu}{2}\Big).
```

Here $S_{\mathrm{cl}}$ is the action of a classical path between the endpoints, and $\mu$ counts the focal points the path passes. For a free particle, $S_{\mathrm{cl}}=m(x_f-x_i)^2/2T$, and the prefactor reproduces $\sqrt{m/2\pi i\hbar T}$. For Lagrangians at most quadratic in position and velocity the expression is exact. The approximation fails near caustics, where classical paths merge and the prefactor diverges. As $S/\hbar$ grows, interference fringes become finer than any detector resolves, and only the classical motion remains visible.

A uniform gravitational field gives a linear potential, so the semiclassical form is exact and only classical paths are needed. A neutron beam has a fixed energy rather than a fixed travel time. Evaluating the time integral of the propagator by stationary phase then replaces $S$ by the reduced action, and the phase along a path becomes $\hbar^{-1}\int p\,dx$. Let the two beams enclose a parallelogram of area $A=H\ell$ in a vertical plane. Their horizontal segments of length $\ell$ differ in height by $H$, and the sloping segments contribute equally to both. Energy conservation lowers the momentum on the upper segment from $p=h/\lambda$ to about $p-m^2gH/p$, so that

```math
\Delta\varphi=\frac{\ell}{\hbar}\,\frac{m^2gH}{p}=\frac{mgH\ell}{\hbar v}
=\frac{2\pi m^2g\lambda A}{h^2}.
```

For neutrons of wavelength $0.1445$ nm and an area of $10\,\mathrm{cm}^2$ in a vertical plane, $\Delta\varphi\approx57$ rad, about nine fringes. Colella, Overhauser and Werner observed this gravitationally induced phase in 1975 by rotating a silicon-crystal neutron interferometer about the incident beam. The classical trajectories do not depend on mass; the mass enters the phase through the ratio $m/\hbar$. At fixed wavelength the phase grows as $m^2$.

Light-pulse atom interferometers use the same calculation with laser phases added at each pulse. Their phase $k_{\mathrm{eff}}gT^2$ exceeds $10^6$ rad for rubidium atoms with $T=0.1$ s, and such gravimeters reach parts-per-billion precision in $g$. The derivation of the propagator by time slicing, and its free-particle Gaussian form, are given under path integral.

## References For The Physical Derivation

- [R. MacKenzie, Path Integral Methods and Applications; stationary phase, the classical limit and the semiclassical propagator.](https://arxiv.org/abs/quant-ph/0004090)
- [A. D. Cronin, J. Schmiedmayer and D. E. Pritchard, Atom Interferometers; gravitationally induced phases in neutron and atom interferometers and light-pulse gravimetry.](https://arxiv.org/abs/0712.3703)
