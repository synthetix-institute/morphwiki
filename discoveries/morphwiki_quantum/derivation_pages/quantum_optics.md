# Quantum optics

A single atom inside a small cavity of two facing mirrors can absorb a photon, re-emit it into the same mode and absorb it again. When this exchange is faster than the loss of the photon or of the atomic excitation, a weak probe beam no longer finds one cavity resonance. It finds two lines, split although no photon was present before the probe arrived. The Jaynes--Cummings model accounts for the splitting and predicts how it grows with photon number.

Let one cavity mode of angular frequency $\omega_c$ have annihilation operator $a$, and let a two-level atom with transition frequency $\omega_a$ have lowering operator $\sigma_-=\ket{g}\bra{e}$. The electric-dipole coupling, after the rotating-wave approximation, gives

```math
H=\hbar\omega_c a^\dagger a+\hbar\omega_a\sigma_+\sigma_-
+\hbar g\,(a\sigma_++a^\dagger\sigma_-),\\
g=\frac{d}{\hbar}\sqrt{\frac{\hbar\omega_c}{2\varepsilon_0V}}.
```

Here $d$ is the transition dipole moment along the cavity field and $V$ the mode volume. The coupling grows as the cavity shrinks, because the field of one photon is concentrated in a smaller volume. The rotating-wave approximation drops the terms $a\sigma_-$ and $a^\dagger\sigma_+$, which change the number of excitations by two. It is valid when $g$ and the detuning $\Delta=\omega_a-\omega_c$ are small compared with $\omega_c$. The remaining Hamiltonian conserves $a^\dagger a+\sigma_+\sigma_-$. It couples only the pairs $\ket{e,n-1}$ and $\ket{g,n}$, each a two-state system with coupling $\hbar g\sqrt n$:

```math
E_{n,\pm}=n\hbar\omega_c+\frac{\hbar\Delta}{2}\pm\frac{\hbar}{2}\sqrt{\Delta^2+4g^2n},
\qquad n=1,2,\dots
```

The factor $\sqrt n$ comes from $a^\dagger\ket{n-1}=\sqrt n\ket{n}$. On resonance the lowest doublet is split by $2\hbar g$, the vacuum Rabi splitting, although the cavity holds no photon. An atom prepared in $\ket{e,0}$ then oscillates with excited-state probability $\cos^2(gt)$. The higher doublets are split by $2\hbar g\sqrt n$, so the ladder is not equally spaced. A probe tuned to the lowest doublet cannot add a second photon at the same frequency, an effect called photon blockade.

In circuit quantum electrodynamics the atom is a superconducting qubit and the cavity is a coplanar microwave resonator. Wallraff and coworkers measured a transmission doublet split by $2g/2\pi\approx11.6$ MHz. The photon loss rate was about 0.8 MHz and the qubit decay rate about 0.7 MHz, so the two peaks were well resolved. The condition $g\gg\kappa,\gamma$, with $\kappa$ and $\gamma$ the photon and atomic loss rates, defines strong coupling. Single atoms in optical cavities of high finesse show the same doublet.

The $\sqrt n$ ladder distinguishes a quantized field from a classical one. Suppose the atom starts excited and the field starts in a coherent state with mean photon number $\bar n$. Each photon-number component makes the atom oscillate at its own frequency:

```math
P_e(t)=\frac12+\frac12\sum_{n=0}^\infty p_n\cos\big(2g\sqrt{n+1}\,t\big),
\qquad p_n=e^{-\bar n}\frac{\bar n^{\,n}}{n!}.
```

The oscillations dephase after a time of order $1/g$ and revive near $t=2\pi\sqrt{\bar n}/g$, when neighbouring frequencies return into phase. A classical field of the same mean intensity would give undamped Rabi oscillations instead. Brune and coworkers observed the frequencies in the ratio $1:\sqrt2:\sqrt3$ with Rydberg atoms crossing a microwave cavity. Each doublet follows the dynamics of the two-state quantum system, while the cavity mode is a quantum harmonic oscillator.

## References For The Physical Derivation

- [A. Wallraff and colleagues, Circuit Quantum Electrodynamics: Coherent Coupling of a Single Photon to a Cooper Pair Box; measured vacuum Rabi splitting in a microwave resonator.](https://arxiv.org/abs/cond-mat/0407325)
- [A. Blais, A. L. Grimsmo, S. M. Girvin and A. Wallraff, Circuit Quantum Electrodynamics; Jaynes-Cummings model, strong coupling and circuit realizations.](https://arxiv.org/abs/2005.12667)
- [J. Larson and Th. K. Mavrogordatos, The Jaynes-Cummings model and its descendants; excitation-number doublets, collapse and revival.](https://arxiv.org/abs/2202.00330)
