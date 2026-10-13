# Gauge theory

An electron beam split around a long, shielded solenoid recombines with its interference fringes displaced. The electrons travel only where the magnetic field vanishes. The displacement follows from requiring that the phase of a wave function can be chosen independently at every point. Let $\psi(\mathbf r,t)$ be the wave function of a particle of charge $q$. Consider the local change $\psi\to e^{iq\chi/\hbar}\psi$, with $\chi(\mathbf r,t)$ an arbitrary real function.

The probability density is unchanged, but the gradient acquires an extra term: $\nabla(e^{iq\chi/\hbar}\psi)=e^{iq\chi/\hbar}(\nabla\psi+iq\psi\nabla\chi/\hbar)$. The Schrödinger equation with the ordinary gradient therefore changes form. The extra term is cancelled by a vector potential that shifts as $\mathbf A\to\mathbf A+\nabla\chi$, entering through the covariant derivative

```math
\mathbf D=\nabla-\frac{iq}{\hbar}\mathbf A,\qquad
\mathbf D'\big(e^{iq\chi/\hbar}\psi\big)=e^{iq\chi/\hbar}\,\mathbf D\psi,\\
[D_x,D_y]=-\frac{iq}{\hbar}\big(\partial_xA_y-\partial_yA_x\big)=-\frac{iq}{\hbar}B_z.
```

The same argument for the time derivative requires a scalar potential with $\varphi\to\varphi-\partial_t\chi$. The Hamiltonian becomes $(\mathbf p-q\mathbf A)^2/2m+q\varphi$, the minimal coupling of electrodynamics. The commutator of covariant derivatives is the magnetic field. It is the part of the potential that no choice of $\chi$ can remove. Carrying the phase around a closed path $\gamma$ and applying Stokes' theorem gives

```math
\delta_{\rm AB}=\frac{q}{\hbar}\oint_\gamma\mathbf A\cdot d\mathbf l
=\frac{q}{\hbar}\int_\Sigma\mathbf B\cdot d\mathbf S=\frac{q\Phi}{\hbar},
```

where $\Sigma$ is a surface bounded by $\gamma$ and $\Phi$ the enclosed flux. Outside an ideal solenoid the potential $A_\theta=\Phi/2\pi r$ has zero curl, so the field vanishes on both paths. Locally $\mathbf A=\nabla(\Phi\theta/2\pi)$, but the angle $\theta$ is not single valued around the solenoid. The potential therefore cannot be removed everywhere. The beams passing on either side differ in phase by $q\Phi/\hbar$, and only this phase modulo $2\pi$ is observable. For electrons the fringes move by one period when $\Phi$ changes by $h/e=4.14\times10^{-15}$ Wb.

Tonomura and colleagues tested this in 1986 with a toroidal magnet coated by a superconducting layer. The layer kept the electron wave out of the field region and quantized the trapped flux in units of $h/2e$. The measured phase shift was $0$ or $\pi$, as the relation predicts for an even or odd number of flux quanta.

When the internal state has several components, as for the three colours of a quark, the phase becomes a position-dependent unitary matrix $U(x)$. The potential becomes a matrix $A_\mu=A_\mu^aT^a$ built from the generators $T^a$ of the group, and the field strength acquires a commutator:

```math
D_\mu=\partial_\mu-igA_\mu,\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-ig[A_\mu,A_\nu],\\
F_{\mu\nu}\to UF_{\mu\nu}U^{-1},\qquad
W(\gamma)=\operatorname{Tr}\mathcal P\exp\Big(ig\oint_\gamma A_\mu dx^\mu\Big).
```

Here $g$ is the coupling and $\mathcal P$ orders the matrices along the path. The field strength is no longer invariant; it rotates in the internal space. Observables are traces, such as $\operatorname{Tr}F_{\mu\nu}F^{\mu\nu}$ and the Wilson loop $W(\gamma)$ of a test charge carried around $\gamma$. In the Hamiltonian description Gauss's law generates the time-independent gauge transformations, and physical states are those it annihilates. The commutator term makes the gauge field respond to its own charge, so gluons interact with one another; quantum chromodynamics develops this case. The Aharonov--Bohm phase is the Abelian Wilson loop, and the same loop variables underlie the spin networks of loop quantum gravity.

## References For The Physical Derivation

- [E. Cohen, H. Larocque, F. Bouchard, F. Nejadsattari, Y. Gefen and E. Karimi, Geometric phase from Aharonov-Bohm to Pancharatnam-Berry and beyond; the Aharonov-Bohm phase and its measurements.](https://arxiv.org/abs/1912.12596)
- [G. S. Bali, QCD forces and heavy quark bound states; non-Abelian covariant derivative, field strength and Wilson loops.](https://arxiv.org/abs/hep-ph/0001312)


## Source Equations

- [arXiv:hep-th/0106242](https://arxiv.org/abs/hep-th/0106242)
- [arXiv:hep-th/0010277](https://arxiv.org/abs/hep-th/0010277)
