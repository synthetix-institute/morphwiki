# Wave function collapse

A trapped ion is driven from one hyperfine level to another by a resonant radio-frequency field. If the level is checked repeatedly during the drive, the transfer slows down. Frequent enough checks nearly stop it.

The calculation uses the update rule for a recorded outcome. For a measurement with orthogonal projectors $P_k$, the Lüders rule replaces the density operator $\rho$ after outcome $k$ by the normalized projection. If the outcome is not recorded, the state becomes the probability-weighted average:

```math
\rho\;\longmapsto\;\frac{P_k\rho P_k}{\operatorname{Tr}(\rho P_k)},\qquad
\rho\;\longmapsto\;\sum_kP_k\rho P_k.
```

Because $P_k^2=P_k$, an immediate repetition returns outcome $k$ with certainty. The second map removes the coherences between different outcomes and keeps their populations.

Let the drive rotate the Bloch vector of the two-level ion about the $x$ axis, completing a $\pi$ rotation in time $T$. Without interruption it transfers the ion completely. Divide $T$ into $N$ intervals, each rotating the vector by $\pi/N$ and followed by a measurement of the level. Each measurement removes the transverse components, so the $z$ component is multiplied by $\cos(\pi/N)$ at every step:

```math
P_N=\frac12\left[1-\cos^N\frac{\pi}{N}\right]\approx\frac{\pi^2}{4N}\qquad(N\gg1).
```

One interruption gives full transfer, two give 0.5, and 64 give 0.037. Itano, Heinzen, Bollinger and Wineland observed this suppression in 1990. They drove a hyperfine transition of beryllium ions with a 256 ms radio-frequency pulse, interrupted by up to 64 short laser pulses. Ions in one of the levels scattered light from each pulse, and the measured transfer followed the prediction. This slowing is the quantum Zeno effect.

The suppression relies on the quadratic start of the transfer: with Rabi frequency $\Omega$, the probability of leaving the initial level grows as $(\Omega t/2)^2$ at short times. A decay into a broad continuum is quadratic only for times shorter than the correlation time of the continuum. Ordinary radioactive decay is therefore not slowed by any realistic observation. Each laser pulse must also dephase the two levels completely without driving the radio-frequency transition.

The same suppression follows when each laser pulse is treated as a coupling of the ion to the scattered light, without invoking the update rule. The experiment therefore confirms that a strong probe removes the coherence between levels. It does not show that collapse is a physical process distinct from that interaction. Whether the update describes a physical change or a revision of information is the measurement problem. The quantum jump description gives the same conditioning for continuous photon counting.

## References For The Physical Derivation

- [W. M. Itano, Perspectives on the quantum Zeno paradox; the 1990 trapped-ion experiment and its interpretation.](https://arxiv.org/abs/quant-ph/0612187)
