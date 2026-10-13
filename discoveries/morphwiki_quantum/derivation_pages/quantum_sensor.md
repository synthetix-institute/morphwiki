# Quantum sensor

A nitrogen-vacancy centre in diamond, a trapped ion or an atom in a vapour cell detects a magnetic field through the precession of its spin. A quantum sensor is a probe with well-separated levels whose energy difference depends on the quantity to be measured. The signal accumulates as a relative phase between two states, which is then converted into a population that a detector counts.

In a Ramsey sequence the probe starts in $|0\rangle$, and a $\pi/2$ pulse creates an equal superposition of $|0\rangle$ and $|1\rangle$. During a free evolution time $\tau$, a detuning $\delta$ between the transition and a reference oscillator adds the relative phase $\delta\tau$. A second $\pi/2$ pulse converts this phase into the probability of finding the excited state. For $\nu$ independent probes or repetitions, binomial counting adds projection noise:

```math
P_1=\frac{1+\cos\delta\tau}{2},\qquad \Delta P_1=\sqrt{\frac{P_1(1-P_1)}{\nu}},\qquad
\Delta\delta=\frac{\Delta P_1}{|\partial P_1/\partial\delta|}=\frac{1}{\tau\sqrt\nu}.
```

The frequency uncertainty is independent of the operating point and defines the standard quantum limit for uncorrelated probes. A longer phase accumulation improves it until the coherence time $T_2$ limits $\tau$. Correlated probe states can exceed this limit, as described under quantum metrology.

A different sensor records a weak field in the choice between two macroscopic states. A Kerr parametric oscillator, such as a Josephson microwave resonator pumped at twice its frequency, has two stable oscillation states of opposite phase above a threshold. Swept through the threshold, it amplifies vacuum fluctuations into one of the two states with equal probability. A resonant bias $h$ far below one photon tilts that choice. In the frame rotating at half the pump frequency, with $\hbar=1$,

```math
H=-Ka^{\dagger2}a^2+\frac{i\epsilon_2(t)}{2}\big(a^{\dagger2}-a^2\big)+ih\big(a^\dagger-a\big),\\
\dot\rho=-i[H,\rho]+\kappa(\bar n+1)\mathcal D[a]\rho+\kappa\bar n\,\mathcal D[a^\dagger]\rho.
```

Here $K$ is the Kerr coefficient, $\epsilon_2=rt$ the two-photon drive swept at rate $r$, $\kappa$ the loss rate, $\bar n$ the thermal occupation of the bath, and $\mathcal D[a]\rho=a\rho a^\dagger-\{a^\dagger a,\rho\}/2$. Above threshold, $\epsilon_2>\kappa/2$, each stored state holds $\sqrt{\epsilon_2^2-\kappa^2/4}/(2K)$ photons. While the amplitude is small the Kerr term is negligible. A Gaussian Wigner function evolving under a quadratic Hamiltonian with linear loss obeys exactly the classical Fokker--Planck equation. The amplified quadrature $x=\mathrm{Re}\,\alpha$ therefore follows a classical noisy equation:

```math
\dot x=\big(\epsilon_2-\tfrac{\kappa}{2}\big)x+h+\sqrt{2D}\,\xi(t),\qquad 2D=\frac{\kappa(2\bar n+1)}{4},\\
P=\Phi\!\left(\frac{hI_1}{\sqrt{\sigma_0^2+2DI_2}}\right),\qquad I_k=\int_0^\infty e^{-k\phi(s)}ds,\qquad
\phi(s)=\frac{rs^2-\kappa s}{2}.
```

Here $\xi$ is unit white noise, $\sigma_0^2=(2\bar n_0+1)/4$ the initial variance of $x$, and $\Phi$ the normal distribution function. The bias shifts the mean of the amplified seed, the noise sets its width, and $P$ is the probability of the favoured state. The noise strength $D$ is not a free parameter; vacuum and thermal fluctuations fix it. Evaluating the integrals gives two limits:

```math
\kappa\gg\sqrt r:\ P=\Phi\!\left(\frac{\pi^{1/4}h}{D^{1/2}r^{1/4}}\right),\qquad
\kappa\to0:\ P=\Phi\!\left(h\sqrt{2\pi/r}\right).
```

The strong-loss limit is the selection law of a classical swept pitchfork, derived by Kondepudi and Nelson in 1985, here with the noise fixed by the vacuum. Loss renews the seed during the sweep, and the rate enters with the exponent $-1/4$. Without loss the seed is the initial vacuum, and the exponent becomes $-1/2$. A higher temperature lowers the argument of $\Phi$ as $(2\bar n+1)^{-1/2}$. Gu and colleagues derived the corresponding relation for a sudden step of the gain. Roques-Carmes and colleagues measured it in an optical parametric oscillator, where bias pulses below one photon set the two probabilities.

In units where $\kappa=1$, with $r=0.01$ and $h=0.108$, the law predicts $P=0.90$. Exact density-operator evolution at 27 stored photons gives $0.900$, within $0.001$ of the law. The law requires the choice to be complete before the Kerr term acts, which fails at few photons. With $K=\kappa$ and 1.5 stored photons the same sweep gives $0.68$, because the oscillator switches between its shallow wells while the sweep proceeds. The probability then relaxes toward the selection $P_{\rm eq}$ of the biased steady state, at the slowest decay rate $\Gamma$ of the Lindblad equation:

```math
\frac{dp}{dt}=\Gamma(\epsilon_2)\big[P_{\rm eq}(\epsilon_2)-p\big].
```

This one-mode relaxation reproduces the exact few-photon probability within $0.01$ over two decades of sweep rate. The rate dependence separates the regimes: a probability that rises for slower sweeps comes from the Gaussian stage, and a rate-independent probability from equilibrating wells. Yamaji and colleagues (2025) measured the probability of the favoured state against a one-photon bias in a Josephson oscillator holding about twelve photons. A related selection under a residual bias, studied against the crossing rate, occurs at the Dicke transition of a Bose--Einstein condensate in an optical cavity.

## References For The Physical Derivation

- [C. L. Degen, F. Reinhard and P. Cappellaro, Quantum sensing; Ramsey sequences, projection noise and the standard quantum limit.](https://arxiv.org/abs/1611.02427)
- [A. Gu, J. Sloan, C. Roques-Carmes and colleagues, Quantum sensitivity of parametric oscillators; the bias-probability relation for a step of the gain with the initial quantum state and the gain noise.](https://arxiv.org/abs/2412.02887)
- [C. Roques-Carmes, Y. Salamin, J. Sloan and colleagues, Biasing the quantum vacuum to control macroscopic probability distributions; bias pulses below one photon set the probabilities of the two states of an optical parametric oscillator.](https://arxiv.org/abs/2303.03455)
- [T. Yamaji, S. Masuda, Y. Kano and colleagues, Quantum annealing in capacitively coupled Kerr parametric oscillators using frequency-chirped drives; Josephson Kerr parametric oscillators raised through threshold with one-photon drives, probability of the selected state.](https://arxiv.org/abs/2506.23539)
- [K. Baumann, R. Mottl, F. Brennecke and T. Esslinger, Exploring Symmetry Breaking at the Dicke Quantum Phase Transition; selection between two ordered phases under a small symmetry-breaking field, against the rate of crossing.](https://arxiv.org/abs/1105.0426)
