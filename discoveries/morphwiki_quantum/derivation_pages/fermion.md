# Fermion

Atoms of helium-3, released from a trap and detected far away, arrive in pairs at nearby points less often than uncorrelated particles would. Atoms of helium-4 in the same apparatus arrive together more often. Electrons with parallel spins in a metal similarly avoid one another, even apart from their Coulomb repulsion. These effects follow from the sign that the amplitude of identical fermions acquires under exchange.

Let $z=(\mathbf x,s)$ denote the position and spin projection of one particle. The amplitude of identical fermions changes sign when two complete coordinates are exchanged. With orthonormal one-particle states $\varphi_a,\varphi_b$ for two particles, or $\varphi_1,\dots,\varphi_N$ for $N$ particles, the antisymmetric amplitudes are

```math
\Psi(z_1,z_2)=\frac{\varphi_a(z_1)\varphi_b(z_2)-\varphi_b(z_1)\varphi_a(z_2)}{\sqrt2},\\
\Psi(z_1,\dots,z_N)=\frac{1}{\sqrt{N!}}\det\left[\varphi_i(z_j)\right].
```

A determinant with two equal rows or two equal columns vanishes. Hence $\Psi=0$ if two particles occupy the same one-particle state, which is the Pauli exclusion principle. The amplitude also vanishes whenever $z_1=z_2$, so two particles with equal spin projection are never found at the same point. Opposite spin projections make the complete coordinates different. Two electrons can therefore share one spatial orbital in a spin singlet, as in the helium ground state or the chemical bond treated under Quantum chemistry.

The suppression extends over a finite distance. Consider the ground state of free electrons in a large volume, a Slater determinant of plane waves filling a Fermi sphere of radius $k_F$. Let $n_\sigma=k_F^3/6\pi^2$ be the density of one spin orientation. The probability density of finding a same-spin electron at distance $r$ from a given one, divided by $n_\sigma$, is

```math
g_{\uparrow\uparrow}(r)=1-\left[\frac{3j_1(k_Fr)}{k_Fr}\right]^2,\qquad
j_1(x)=\frac{\sin x-x\cos x}{x^2},\\
n_\sigma\int\left[g_{\uparrow\uparrow}(r)-1\right]d^3r=-1.
```

The bracket is the average of $e^{i\mathbf k\cdot\mathbf r}$ over the filled sphere and comes from the exchange terms of the determinant. The function $g_{\uparrow\uparrow}$ rises from zero at $r=0$ to one half at $k_Fr=1.81$ and approaches one with weak oscillations. The integral shows that this exchange hole contains exactly one missing electron of the same spin. Opposite spins remain uncorrelated in this state, $g_{\uparrow\downarrow}=1$, until the Coulomb interaction is included.

In sodium, with one conduction electron per atom, $k_F=0.92\times10^{10}\,\mathrm{m^{-1}}$, and the same-spin density falls to half within 0.20 nm of each electron. Each electron is thus surrounded by a deficit of negative charge, which lowers its electrostatic energy. For the uniform electron gas this exchange energy is $-(3/4\pi)\,e^2k_F/4\pi\epsilon_0$ per electron. In Rydberg units it is $-0.916/r_s$, with $r_s$ the Wigner--Seitz radius in Bohr radii. Sodium has $r_s=3.93$, which gives $-3.2$ eV per electron, larger in magnitude than the mean kinetic energy of 1.9 eV.

The exchange sign is not an interaction and has no adjustable strength; it is fixed by the identity of the particles. Its connection with half-integer spin, the spin-statistics theorem, requires relativistic quantum field theory with locality and positive energy. In the occupation description of Fock space the same rule is the anticommutation $\{a_i^\dagger,a_j^\dagger\}=0$, so that $(a_i^\dagger)^2=0$. Thermal occupations of fermionic states follow Fermi--Dirac statistics. Quasiparticles confined to two dimensions can have other exchange phases.

## References For The Physical Derivation

- [T. Jeltes and colleagues, Comparison of the Hanbury Brown-Twiss effect for bosons and fermions; antibunching of helium-3 and bunching of helium-4 atoms.](https://arxiv.org/abs/cond-mat/0612278)
- [S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold Fermi gases; occupation and spin-resolved pair correlations of an ideal Fermi gas.](https://arxiv.org/abs/0706.3360)


## Source Equations

- [arXiv:cond-mat/0005069](https://arxiv.org/abs/cond-mat/0005069)
- [arXiv:quant-ph/0305150](https://arxiv.org/abs/quant-ph/0305150)
- [arXiv:hep-ph/0007343](https://arxiv.org/abs/hep-ph/0007343)
