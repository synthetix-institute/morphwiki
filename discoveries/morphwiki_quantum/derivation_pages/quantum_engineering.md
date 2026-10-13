# Quantum engineering

Two superconducting pads joined by a thin insulating barrier behave as a single quantum degree of freedom, although they contain a macroscopic number of electrons. Such circuits are designed and fabricated like electrical circuits, and quantum engineering chooses their parameters so that the lowest levels form a usable qubit. The transmon, a widely used design, shows these choices in one calculation.

Let $n$ be the number of Cooper pairs that have tunnelled across the Josephson junction and $\varphi$ the superconducting phase difference, with $[\varphi,n]=i$. The charging energy $E_C=e^2/(2C)$ sets the cost of charge on the capacitance $C$, and the Josephson energy $E_J$ sets the strength of pair tunnelling. The Hamiltonian is

```math
H=4E_C(n-n_g)^2-E_J\cos\varphi.
```

Here $n_g$ is an offset charge set by the electrostatic environment, which fluctuates in time. For $E_J\gg E_C$ the phase stays near zero. Expanding the cosine to fourth order gives a harmonic oscillator with a quartic correction. With $b$ the oscillator lowering operator and $\varphi=(2E_C/E_J)^{1/4}(b+b^\dagger)$,

```math
H\approx\sqrt{8E_JE_C}\Big(b^\dagger b+\frac12\Big)-E_J-\frac{E_C}{12}\big(b+b^\dagger\big)^4.
```

In lowest order the quartic term shifts level $m$ by $-(E_C/2)(m^2+m+1/2)$. The level spacings therefore decrease with $m$, and the two lowest transitions differ by the anharmonicity $\alpha$:

```math
\hbar\omega_{01}\approx\sqrt{8E_JE_C}-E_C,\qquad
\hbar\alpha=\hbar(\omega_{12}-\omega_{01})\approx-E_C.
```

The anharmonicity turns the oscillator into a qubit. A microwave pulse resonant with $\omega_{01}$ drives the $1\to2$ transition with a detuning $|\alpha|$. Pulses much longer than $1/|\alpha|$ therefore keep the population in the two lowest levels. For $E_C/h=250$ MHz and $E_J/E_C=50$, the formulas give $\omega_{01}/2\pi=4.75$ GHz and $\alpha/2\pi=-250$ MHz. Exact diagonalization in the charge basis gives $4.74$ GHz and $-287$ MHz. Since $1/|\alpha|$ is about $0.6$ ns, pulses of tens of nanoseconds keep leakage small, and shaped pulses suppress it further.

The large ratio $E_J/E_C$ is the other design choice. The sensitivity of the levels to the fluctuating offset charge falls as $\exp(-\sqrt{8E_J/E_C})$. In the example, the transition frequency varies with $n_g$ by about 10 kHz. At $E_J/E_C=1$, as in the earlier Cooper-pair box, it varies by almost 800 MHz. The price is a weaker relative anharmonicity, which decreases only as $(8E_J/E_C)^{-1/2}$ (Koch and colleagues, 2007).

The device must also be cold. At $4.74$ GHz the transition energy corresponds to $0.23$ K. At a refrigerator temperature of 20 mK the thermal excited population $e^{-h\nu/k_BT}$ is about $10^{-5}$, although residual excitation measured in devices is often larger. Loss in dielectric interfaces and broken Cooper pairs then limit the coherence times.

The transmon is a quantum harmonic oscillator made weakly anharmonic, and its Josephson term describes tunnelling of Cooper pairs through the barrier. Transmons coupled through a common resonator exchange excitations as described under quantum bus.

## References For The Physical Derivation

- [J. Koch, T. M. Yu, J. Gambetta, A. A. Houck, D. I. Schuster, J. Majer and colleagues, Charge insensitive qubit design derived from the Cooper pair box; transmon spectrum, anharmonicity and charge dispersion.](https://arxiv.org/abs/cond-mat/0703002)
- [P. Krantz, M. Kjaergaard, F. Yan, T. P. Orlando, S. Gustavsson and W. D. Oliver, A Quantum Engineer's Guide to Superconducting Qubits; device design, control pulses and loss mechanisms.](https://arxiv.org/abs/1904.06560)
