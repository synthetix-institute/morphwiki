# Quantum dynamics

A picosecond laser pulse excites an atom into a superposition of Rydberg levels near $n=50$. The electron then moves as a localized packet around a Kepler orbit. After a few revolutions it spreads around the orbit, and later it reassembles. Each stage follows from the spacing of the energy levels.

At short times the centre of a narrow packet follows Newton's law. Differentiating expectation values with the Schrödinger equation gives Ehrenfest's theorem:

```math
\frac{d\langle X\rangle}{dt}=\frac{\langle P\rangle}{m},\qquad
\frac{d\langle P\rangle}{dt}=-\langle V'(X)\rangle\approx-V'(\langle X\rangle).
```

The approximation holds while the force varies little across the packet. For a harmonic potential it is exact at all times, because $V'$ is linear. In other potentials the packet spreads, and the centre no longer obeys a closed classical equation.

The energy spectrum shows how long the classical stage lasts. Expand the packet in energy eigenstates with weights $|c_n|^2$ concentrated around $\bar n$, and expand the energies to second order in $n-\bar n$. The amplitude to return to the initial state and the two resulting times are

```math
A(t)=\sum_n|c_n|^2e^{-iE_nt/\hbar},\qquad
E_n\approx E_{\bar n}+E'(n-\bar n)+\frac{E''}{2}(n-\bar n)^2,\\
T_{\mathrm{cl}}=\frac{2\pi\hbar}{|E'|},\qquad T_{\mathrm{rev}}=\frac{4\pi\hbar}{|E''|}.
```

The linear term brings every component back in phase after the classical period $T_{\mathrm{cl}}$. The quadratic term slowly dephases the components. With a spread $\Delta n$ in $n$, the packet covers the whole orbit after a time of order $T_{\mathrm{rev}}/(2\pi\Delta n^2)$. At $T_{\mathrm{rev}}$ every quadratic phase is a multiple of $2\pi$, because $n-\bar n$ is an integer, and the packet reforms. At rational fractions of $T_{\mathrm{rev}}$ it appears as several smaller packets, the fractional revivals.

For hydrogen $E_n=-R/n^2$ with $R=13.6$ eV, so $E'=2R/n^3$ and $E''=-6R/n^4$. Then $T_{\mathrm{cl}}=\pi\hbar n^3/R$ equals the Kepler period of the classical orbit with the same energy, and $T_{\mathrm{rev}}=(2\bar n/3)T_{\mathrm{cl}}$. For $\bar n=50$ this gives $T_{\mathrm{cl}}=19$ ps and $T_{\mathrm{rev}}=0.63$ ns. Yeazell, Mallalieu and Stroud observed the collapse and revival of such Rydberg packets in 1990.

Higher terms limit the picture. The cubic term adds a phase of about $8(\Delta n)^3/\bar n$ at $T_{\mathrm{rev}}$, so a clean revival requires $(\Delta n)^3\ll\bar n/8$. A direct sum for $\bar n=50$ gives a return probability of 0.91 at the revival for $\Delta n=1$, but only about 0.5 for $\Delta n=2.5$. An evenly spaced spectrum, as in the quantum harmonic oscillator, never dephases. In a classically chaotic system, agreement with a single trajectory lasts only about the Ehrenfest time, of order $\lambda^{-1}\ln(S/\hbar)$, where $\lambda$ is the Lyapunov exponent and $S$ a typical action. This short time scale is one signature of quantum chaos.

## References For The Physical Derivation

- [R. W. Robinett, Quantum wave packet revivals; classical period, revival time, fractional revivals and Rydberg wave packets.](https://arxiv.org/abs/quant-ph/0401031)
