# Quantum metamaterial

Microwaves in a superconducting transmission line can be sent through a row of artificial atoms. Each atom is a superconducting qubit with a transition frequency of several gigahertz, and the qubits sit far closer together than one wavelength. A microwave then responds to the row as to a continuous medium with a refractive index. That index, and the frequencies at which the medium stops transmitting, follow from the scattering of one qubit.

Let a qubit of transition frequency $\omega_0$ emit into the line at rate $\Gamma_{1D}$, shared equally between the two directions. For weak probe power the qubit stays close to its ground state and responds linearly. A wave of frequency $\omega$ and wave number $k=\omega/v$, with $v$ the phase velocity of the line, is then reflected and transmitted with amplitudes

```math
r=-\frac{i\Gamma_{1D}/2}{\omega-\omega_0+i\Gamma_{1D}/2},\qquad t=1+r.
```

On resonance the reflection is complete, so a single qubit acts as a mirror one atom wide. Now place identical qubits at spacing $d$. Between neighbours the wave propagates freely, and at each qubit it is scattered with $r$ and $t$. The transfer matrix of one period has unit determinant. Bloch's theorem requires its eigenvalues to be $e^{\pm iqd}$, where $q$ is the wave number of the collective wave. Half the trace of the matrix gives the dispersion relation

```math
\cos qd=\cos kd+\frac{\Gamma_{1D}}{2(\omega-\omega_0)}\sin kd.
```

When the right side exceeds one in magnitude, $q$ is complex and the wave decays along the array. For subwavelength spacing, $kd\ll1$, expanding both sides to second order gives an effective permittivity of Lorentz form:

```math
\varepsilon_{\rm eff}(\omega)=\frac{q^2}{k^2}\approx1+\frac{\Gamma_{1D}}{kd\,(\omega_0-\omega)},
\qquad \varepsilon_{\rm eff}<0\ \text{ for }\ \omega_0<\omega<\omega_0+\frac{\Gamma_{1D}}{k_0d}.
```

Below resonance the index exceeds one and the microwaves slow down. Just above resonance the permittivity is negative, and a stop band opens with width about $\Gamma_{1D}/(k_0d)$, where $k_0=\omega_0/v$. The band is much wider than the linewidth of one qubit, because many qubits within a wavelength respond together. For $\Gamma_{1D}/2\pi=10$ MHz and a spacing of about one sixtieth of a wavelength, $k_0d\approx0.1$, the stop band is about 100 MHz wide. Arrays of transmon qubits on a coplanar waveguide show such a band in transmission, and tuning the qubits with magnetic flux moves it.

Three approximations enter. The probe must be weak, because a qubit that holds one excitation cannot absorb a second; at higher power the reflection saturates and the medium becomes nonlinear. Losses into other channels and dephasing must be small compared with $\Gamma_{1D}$; they add an imaginary part to $\omega_0$ and round the band edges. The coupling must also be weak compared with $\omega_0$, so that the resonant form of $r$ holds.

The medium differs from a classical metamaterial because each element is a two-level quantum system. Its saturation at the level of single photons produces strong photon--photon interactions, and its state can be prepared in superpositions. The linear band structure and the tunable stop band are established experimentally. Using the quantum state of the whole array to control propagation remains largely a proposal. The reflection by one qubit is the waveguide form of the atom--field coupling treated under quantum optics. The band calculation repeats the Kronig--Penney construction for an electron in a periodic array of potential wells.

## References For The Physical Derivation

- [J. D. Brehm, A. N. Poddubny, A. Stehli, T. Wolz, H. Rotzinger and A. V. Ustinov, Waveguide Bandgap Engineering with an Array of Superconducting Qubits; polaritonic band gap of eight tunable transmons in a waveguide.](https://arxiv.org/abs/2006.03330)
- [A. S. Sheremet, M. I. Petrov, I. V. Iorsh, A. V. Poshakinskiy and A. N. Poddubny, Waveguide quantum electrodynamics: collective radiance and photon-photon correlations; single-emitter reflection and band structure of emitter arrays.](https://arxiv.org/abs/2103.06824)
- [A. L. Rakhmanov, A. M. Zagoskin, S. Savel'ev and F. Nori, Quantum metamaterials: Electromagnetic waves in a Josephson qubit line; proposal in which the qubit quantum state controls propagation.](https://arxiv.org/abs/0709.1314)
