# Photon

Light from an attenuated laser falling on a 50:50 beam splitter occasionally produces simultaneous clicks in detectors behind both outputs. Light emitted by a single atom or quantum dot after one excitation does not: one detector clicks, never both. Grangier, Roger and Aspect observed this anticorrelation in 1986 with photons from an atomic cascade, using the partner photon of each pair to announce the event. The quantity that distinguishes the two cases is the second-order correlation $g^{(2)}(0)$.

The electromagnetic field in a volume $V$ is a set of modes labeled by a wave vector $\mathbf k$ and a transverse polarization vector $\boldsymbol\epsilon_\lambda$, with $\mathbf k\cdot\boldsymbol\epsilon_\lambda=0$. Each mode is a harmonic oscillator with angular frequency $\omega=c|\mathbf k|$ and annihilation operator $a_{\mathbf k\lambda}$, where $[a,a^\dagger]=1$. A photon is one quantum of such a mode:

```math
E=\hbar\omega,\qquad \mathbf p=\hbar\mathbf k,\qquad
\ket{1_{\mathbf k\lambda}}=a_{\mathbf k\lambda}^\dagger\ket{0},\\
\mathbf E^{(+)}(\mathbf r,t)=i\sum_{\mathbf k,\lambda}\sqrt{\frac{\hbar\omega}{2\epsilon_0V}}\,
\boldsymbol\epsilon_\lambda a_{\mathbf k\lambda}e^{i(\mathbf k\cdot\mathbf r-\omega t)}.
```

Here $\mathbf E^{(+)}$ is the positive-frequency part of the electric field operator, and $\epsilon_0$ is the vacuum permittivity. A one-photon state has zero mean electric field, although it carries energy $\hbar\omega$ above the vacuum. An absorbing detector registers normally ordered products of field operators. For two detectors viewing the same mode, the ratio of the coincidence rate to the product of the single rates at zero delay is

```math
g^{(2)}(0)=\frac{\langle a^\dagger a^\dagger aa\rangle}{\langle a^\dagger a\rangle^2}
=\frac{\langle n(n-1)\rangle}{\langle n\rangle^2}.
```

For a number state $|n\rangle$ this equals $1-1/n$, which vanishes for one photon. A coherent state, the output of an ideal laser, has a Poisson number distribution and $g^{(2)}(0)=1$. Thermal light has $g^{(2)}(0)=2$, the bunching measured by Hanbury Brown and Twiss. A classical fluctuating intensity $I$ gives $\langle I^2\rangle/\langle I\rangle^2$, which the Cauchy--Schwarz inequality keeps at or above one. A value below one therefore has no description by a classical wave.

A two-level emitter, such as a semiconductor quantum dot, must be excited again after each emission before it can emit another photon. Under pulsed excitation the coincidence histogram consists of peaks separated by the pulse period. The value of $g^{(2)}(0)$ is the area of the peak at zero delay divided by the area of a distant peak. If a pulse yields one photon with probability $p_1$ and two photons with a small probability $p_2$, then $g^{(2)}(0)\approx2p_2/p_1^2$. Quantum dots in optical microcavities reach values of order 0.01 and below.

An attenuated laser behaves differently. With mean photon number $\bar n$ per pulse, the ratio of two-photon to one-photon pulses is $\bar n/2$, and $g^{(2)}(0)$ remains 1. Multiphoton events can then be suppressed only by reducing the rate of single photons as well. This difference matters in quantum key distribution, where a second photon in a pulse can leak information.

Linear loss removes photons independently and leaves $g^{(2)}(0)$ unchanged. Background light, detector dark counts and timing jitter raise the measured value above that of the emitted state. A small $g^{(2)}(0)$ certifies few multiphoton events but not that successive photons are identical. That property is tested by the Hong--Ou--Mandel interference described under Boson. The temporal shape of each photon is set by the spontaneous decay treated under Quantum jump.

## References For The Physical Derivation

- [S. Buckley, K. Rivoire and J. Vuckovic, Engineered Quantum Dot Single Photon Sources; second-order correlation, antibunching and cavity-enhanced single-photon emission.](https://arxiv.org/abs/1210.1234)
