# Quantum amplifier

An amplifier that increases both quadratures of a bosonic signal must also introduce fluctuations. Let $a$ be the input annihilation operator, with $[a,a^\dagger]=1$, and let $G>1$ be the intensity gain. Multiplying $a$ by $\sqrt G$ alone would make the output commutator equal to $G$, so it cannot describe an output mode with the original normalization.

A second, independent mode $b$ supplies the required additional degree of freedom. The phase-insensitive amplification relation is

```math
a_{\rm out}=\sqrt G\,a_{\rm in}+\sqrt{G-1}\,b_{\rm in}^\dagger,
\qquad [a_{\rm out},a_{\rm out}^\dagger]=G-(G-1)=1.
```

The creation operator has the opposite commutator sign, exactly compensating the excess from the amplified signal. A parametric interaction realizes this transformation by producing correlated excitations in a signal and an idler. Energy is supplied by a pump; the idler is a physical channel rather than an adjustable numerical correction.

Define $X=(a+a^\dagger)/\sqrt2$ and $P=(a-a^\dagger)/(i\sqrt2)$, so vacuum has variance $1/2$ in each quadrature. For uncorrelated inputs and a vacuum idler,

```math
\operatorname{Var}X_{\rm out}=G\operatorname{Var}X_{\rm in}+\frac{G-1}{2},
\qquad \langle n_{\rm out}\rangle=G\langle n_{\rm in}\rangle+G-1.
```

The second expression includes spontaneous output even for vacuum signal input. Referring the quadrature noise back to the input gives an added variance $(G-1)/(2G)$, approaching half a quantum at large gain. A thermally occupied idler adds still more noise. The commutator determines the necessary channel, while its state determines how much fluctuation that channel contributes.

A phase-sensitive amplifier follows a different relation: one quadrature is stretched and the conjugate one is compressed, preserving their commutator without amplifying both equally. It can amplify a known quadrature without the same added-noise bound. Thus the bound is attached to a specific physical task, not to every process called amplification.

This is an explicit construction from a failed relation. The proposed gain-only map has a nonzero commutator defect; adding an independent idler with the appropriate coefficient restores the algebra and predicts the noise. The correction is already established quantum optics. Its value here is that every additional ingredient changes a calculable experimental consequence.

## References For The Physical Derivation

- [C. Weedbrook and colleagues, Gaussian Quantum Information; Gaussian channels and amplification.](https://arxiv.org/abs/1110.3234)


## Relations In The Original Papers

[arXiv:1110.3234v1, S5.E110](https://arxiv.org/html/1110.3234v1#S5.E110). Complete positivity ties the noise covariance to the gain of a one-mode Gaussian channel. The source uses vacuum quadrature variance one; the chapter uses one half. Its minimum noise follows after this normalization change.
