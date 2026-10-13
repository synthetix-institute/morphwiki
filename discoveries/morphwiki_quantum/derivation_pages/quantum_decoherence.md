# Quantum decoherence

Fullerene molecules sent through a grating interferometer produce clear fringes. When gas is admitted to the vacuum chamber, or when the molecules are heated before they enter, the contrast falls, although every molecule still passes the gratings. Collisions with gas molecules and thermally emitted photons leave a record of the path in the surroundings. Decoherence is the loss of interference that follows from such records.

Consider a particle in an equal superposition of two paths, $\ket L$ and $\ket R$, and an environment initially in $\ket E$. A scattering event that depends on the path leaves the environment in $\ket{E_L}$ or $\ket{E_R}$. The joint evolution is unitary. Tracing out the environment gives the reduced density matrix of the particle:

```math
\tfrac{1}{\sqrt2}(\ket L+\ket R)\ket E\;\longrightarrow\;
\tfrac{1}{\sqrt2}\left(\ket L\ket{E_L}+\ket R\ket{E_R}\right),\\
\rho_S=\tfrac12\left(\ket L\bra L+\ket R\bra R+\langle E_R|E_L\rangle\ket L\bra R
+\langle E_L|E_R\rangle\ket R\bra L\right).
```

At the screen the path amplitudes $\psi_L(x)$ and $\psi_R(x)$ overlap, and the interference term is multiplied by $\langle E_R|E_L\rangle$. For equal intensities the fringe visibility equals $|\langle E_R|E_L\rangle|$. Visibility is lost to the extent that the environment could in principle identify the path; nobody needs to examine the scattered particle.

Independent collisions multiply their overlaps. Suppose collisions occur at random with mean rate $\Gamma$, and each leaves a real overlap $\chi$ between zero and one. Averaging $\chi^N$ over the Poisson distribution of the number $N$ of collisions in time $t$ gives

```math
V(t)=\sum_{N=0}^\infty e^{-\Gamma t}\frac{(\Gamma t)^N}{N!}\,\chi^N=e^{-\Gamma(1-\chi)t}.
```

The decoherence rate $\Gamma(1-\chi)$ depends on how well one collision resolves the path. A scattered wave whose wavelength $\lambda$ greatly exceeds the path separation $d$ gives $\chi$ close to one, with $1-\chi$ growing as $(d/\lambda)^2$. When $d\gg\lambda$, a single event suffices and the rate saturates at $\Gamma$. Since $\Gamma$ is proportional to the gas pressure, the visibility falls exponentially with pressure. This dependence was measured for $\mathrm{C}_{70}$ molecules in a Talbot--Lau interferometer. Heated molecules emit more thermal photons and lose visibility in the same way.

Over times long compared with one collision, the same decay follows from a Lindblad master equation with a dephasing operator. With $\sigma_z=\ket L\bra L-\ket R\bra R$ and rate $\gamma=\Gamma(1-\chi)$,

```math
\frac{d\rho}{dt}=-\frac{i}{\hbar}[H,\rho]+\frac{\gamma}{2}\left(\sigma_z\rho\sigma_z-\rho\right),
\qquad \frac{d\rho_{LR}}{dt}\Big|_{\rm env}=-\gamma\rho_{LR}.
```

The populations of the two paths are unchanged; only their coherence decays. Coherence is lost in the basis in which the interaction is diagonal, here position. Decoherence therefore explains why records form in that basis. It does not determine on which path a given molecule is found; that question belongs to the measurement problem.

The master equation assumes that each scattered particle leaves and never returns, so that records made at different times are independent. A small environment violates this assumption. For one environmental spin, initially up along its $z$ axis and coupled through $\hbar g\sigma_z\otimes\sigma_x^E$, the overlap is $\cos2gt$, and the visibility $|\cos2gt|$ returns to one at $t=\pi/2g$. Such revivals, and the restored fringes of the quantum eraser experiment, show that the phase information has moved into system-environment correlations rather than being destroyed. A Markovian master equation for the particle alone cannot describe them.

## References For The Physical Derivation

- [K. Hornberger, Introduction to Decoherence Theory; which-path records, reduced dynamics and master equations.](https://arxiv.org/abs/quant-ph/0612118)
- [K. Hornberger and colleagues, Collisional Decoherence Observed in Matter Wave Interferometry; exponential loss of fullerene fringe visibility with gas pressure.](https://arxiv.org/abs/quant-ph/0303093)
- [W. H. Zurek, Decoherence, Einselection, and the Quantum Origins of the Classical; pointer basis and the role of the environment.](https://arxiv.org/abs/quant-ph/0105127)


## Source Equations

- [arXiv:quant-ph/0306087](https://arxiv.org/abs/quant-ph/0306087)
- [arXiv:quant-ph/0008131](https://arxiv.org/abs/quant-ph/0008131)
- [arXiv:quant-ph/0211096](https://arxiv.org/abs/quant-ph/0211096)
