# Bose–Einstein statistics

Rubidium atoms cooled in a magnetic trap to a few hundred nanokelvin collect abruptly in the lowest quantum state of the trap. After the trap is switched off, a narrow peak appears in the velocity distribution above a broad thermal cloud. The temperature at which this happens follows from counting how many atoms the excited states can hold. For noninteracting bosons at temperature $T$ and chemical potential $\mu$, Quantum statistical mechanics gives the mean occupation of a single-particle state of energy $\epsilon$ as $\overline n_B=[e^{\beta(\epsilon-\mu)}-1]^{-1}$, with $\beta=1/k_BT$.

Occupations cannot be negative, so $\mu$ must stay below the lowest single-particle energy, set here to zero. At a fixed $\mu<0$ every excited state holds a finite mean number of particles. For a uniform gas of spinless particles of mass $m$, the excited states can therefore hold at most the density reached as $\mu\to0$:

```math
n_{\rm ex}\leq\int\frac{d^3p}{(2\pi\hbar)^3}\,\frac{1}{e^{\beta p^2/2m}-1}
=\frac{\zeta(3/2)}{\lambda_T^3},\qquad
\lambda_T=\sqrt{\frac{2\pi\hbar^2}{mk_BT}}.
```

Here $\zeta(3/2)\approx2.612$ is a value of the Riemann zeta function and $\lambda_T$ is the thermal de Broglie wavelength. If the density $n$ exceeds this bound, the surplus cannot be accommodated in excited states. It accumulates in the ground state, whose occupation $(e^{-\beta\mu}-1)^{-1}$ grows without limit as $\mu$ approaches zero from below. The condition $n\lambda_T^3=\zeta(3/2)$ defines the transition temperature, and the same bound gives the condensed fraction below it:

```math
k_BT_c=\frac{2\pi\hbar^2}{m}\left(\frac{n}{\zeta(3/2)}\right)^{2/3},\qquad
\frac{N_0}{N}=1-\left(\frac{T}{T_c}\right)^{3/2}.
```

Condensation thus begins when the thermal wavelength becomes comparable with the spacing $n^{-1/3}$ between particles. No attraction between the atoms is involved. The cause is the counting of symmetric states: a bosonic mode can hold any number of particles, and permuting identical particles produces no new state. With Maxwell--Boltzmann weights the corresponding relation is $n\lambda_T^3=e^{\beta\mu}$, which has no upper bound, so excited states accommodate any density.

London applied this result to liquid helium-4 in 1938. A mass density of $0.145\,\mathrm{g\,cm^{-3}}$ gives $n=2.18\times10^{28}\,\mathrm{m^{-3}}$ and $T_c\approx3.1$ K, close to the observed superfluid transition at 2.17 K. The difference reflects the strong interactions in the liquid, for which ideal-gas counting is only a guide. Neutron scattering finds that less than ten percent of the atoms occupy the zero-momentum state even near absolute zero.

Dilute alkali gases approach the ideal limit much more closely. In a harmonic trap with geometric-mean angular frequency $\bar\omega$, the density of states grows as $\epsilon^2$ instead of $\sqrt\epsilon$. The same counting then gives

```math
k_BT_c=\hbar\bar\omega\left(\frac{N}{\zeta(3)}\right)^{1/3}
\approx0.94\,\hbar\bar\omega N^{1/3},\qquad
\frac{N_0}{N}=1-\left(\frac{T}{T_c}\right)^3.
```

For $N=10^6$ atoms and $\bar\omega=2\pi\times100\,\mathrm{s^{-1}}$ this gives $T_c\approx450$ nK. Condensation was observed in rubidium and sodium in 1995 at transition temperatures between about 0.2 and 2 microkelvin. The results assume many particles and weak interactions. A finite particle number lowers $T_c$ by a relative amount of order $N^{-1/3}$, and repulsive interactions shift it by a few percent in traps. In a uniform two-dimensional gas the corresponding integral diverges as $\mu\to0$, and no condensation occurs at finite temperature.

Photons and phonons in thermal equilibrium are not conserved in number. Their chemical potential is therefore zero, and the same occupation gives Planck's law instead of a condensate. Reversing the sign in the denominator gives Fermi--Dirac statistics, which fills states one by one up to a Fermi energy. The symmetric exchange rule itself is discussed under Boson.

## References For The Physical Derivation

- [F. Dalfovo, S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of Bose-Einstein condensation in trapped gases; ideal-gas transition temperature and condensate fraction in uniform and harmonic traps, with finite-size and interaction shifts.](https://arxiv.org/abs/cond-mat/9806038)
