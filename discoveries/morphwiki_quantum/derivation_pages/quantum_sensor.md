# Quantum sensor

**Physical domain:** Control sequences and quantum channels

## Mechanism

A parametric oscillator swept through its threshold amplifies vacuum fluctuations into one of two states of opposite phase. A bias field far below one photon shifts the probabilities of the two states, so the oscillator senses a sub-photon field through the statistics of its written state.

The sensor is the oscillator itself. A field far below one photon cannot be read directly, but it displaces the seed that the parametric gain amplifies, and the displacement is recorded in which of two macroscopic states the oscillator reaches. The record is a probability, so the sensing is statistical: many sweeps give the bias through the distribution function of the normal law.

In the frame rotating at half the pump frequency, with $\\hbar=1$, the mode $a$ has a Kerr coefficient $K$, a two-photon drive $\\varepsilon_2$ swept at the rate $r$, a one-photon bias $h$ and a loss $\\kappa$ at thermal occupation $\\bar n$. While the amplitude is small, the amplified quadrature obeys the classical equation with a noise fixed by the vacuum and the temperature, $2D=\\kappa(2\\bar n+1)/4$, since the Wigner function of a Gaussian state under a quadratic generator with linear loss obeys exactly the classical Fokker--Planck equation. The probability of the favoured state is the normal distribution function of $hI_1/\\sqrt{\\sigma_0^2+2DI_2}$: for $\\kappa\\gg\\sqrt r$ the selection law of a swept pitchfork with no free parameter, for $\\kappa\\to0$ a law with the exponent $-1/2$ of the rate. Exact evolution at 27 stored photons follows it to $6\\times10^{-5}$. At a few stored photons switching between the shallow wells outruns a slow sweep, and the probability relaxes to the selection $P_{\\mathrm{eq}}$ of the biased steady state at the rate of the Lindbladian's gap $\\Gamma$.

## Physical Construction

The state carrier is the density operator of one field mode in a truncated Fock space. The calculation involves the Lindbladian with the Kerr term, the swept two-photon drive, the one-photon bias and the loss. Positivity and unit trace; the truncation holds the stored states and their Fock tails; the frame rotates at half the pump frequency. The calculated quantities include the sign of the amplified quadrature at the end of the sweep, with its probability over repetitions.

## Topic Equations

```math
H=-Ka^{\dagger2}a^{2}+\tfrac{i}{2}\varepsilon_2(t)(a^{\dagger2}-a^{2})+ih(a^{\dagger}-a),\qquad\dot\rho=-i[H,\rho]+\kappa(\bar n+1)\mathcal D[a]\rho+\kappa\bar n\mathcal D[a^{\dagger}]\rho
\dot\alpha=-\tfrac{\kappa}{2}\alpha+\varepsilon_2\alpha^{*}+2iK|\alpha|^{2}\alpha+h,\qquad |\alpha|^{2}=\frac{\sqrt{\varepsilon_2^{2}-\kappa^{2}/4}}{2K}
\dot x=(\varepsilon_2-\tfrac{\kappa}{2})x+h+\sqrt{2D}\,\xi(t),\qquad 2D=\tfrac{\kappa}{4}(2\bar n+1)
P=\Phi\!\left(\frac{hI_1}{\sqrt{\sigma_0^{2}+2DI_2}}\right),\quad I_k=\int_0^{\infty}e^{-k\varphi(s)}ds,\quad P\to\Phi\!\left(\frac{\pi^{1/4}h}{D^{1/2}r^{1/4}}\right)\ \text{or}\ \Phi\!\left(h\sqrt{2\pi/r}\right)
\frac{dp}{dt}=\Gamma(\varepsilon_2)\,\bigl[P_{\mathrm{eq}}(\varepsilon_2)-p\bigr]
```

## Physical Meaning

The observable is the sign of the amplified quadrature at the end of the sweep, a Born probability of one half-plane. In the semiclassical regime that probability is set in the linear stage and inherits the classical selection law with the vacuum as its noise. In the few-photon regime it is set later, by the balance of the two shallow wells, and the Lindbladian's gap and biased steady state decide it.

A Josephson Kerr parametric oscillator with 27 stored photons, swept at a rate one hundredth of the square of its loss rate and biased so that the law predicts a probability of 0.9, reaches 0.899; the same oscillator with 1.5 stored photons reaches 0.68, the value of its biased steady state, and keeps that value for any slower sweep.

The same calculation is the quantum counterpart of a classical write into a bistable material: the symmetric write of the memory of matter, with the swept pitchfork and the probit law, transferred to a quantum carrier where the seed is fixed by the vacuum. The failure of the transfer at a few photons promotes the switching between the wells into the dynamics, as the chapter on transfer and obstruction describes.

## Consequences Forced By The Relation

The noise that seeds the choice is not a parameter. In the semiclassical regime the probability of the favoured state depends on $\kappa$ and $\bar n$ only through $D=\kappa(2\bar n+1)/8$, so raising the temperature lowers the argument of $\Phi$ as $(2\bar n+1)^{-1/2}$. The exponent of the sweep rate tells which seed is amplified: $-1/4$ when the loss renews the seed during the sweep, $-1/2$ when the seed is the preparation; the crossover is set by $\kappa/\sqrt r$. At a few stored photons the probability becomes independent of the sweep rate and equals the selection of the biased steady state; raising the photon number at fixed bias and rate restores the law. The deficit below the law grows as $K^{2}$ at large photon numbers.

## Domain Of The Construction

The Gaussian-stage law needs the decision to be complete before the Kerr term acts, which holds when the stored states contain many photons; the few-photon statements rest on exact evolution of the density operator in a truncated Fock space at $K/\kappa$ between $0.01$ and $1$. The classical limit is the selection law of Kondepudi and Nelson (Nature 314, 438, 1985); the step-of-gain form of the same relation is derived by Gu et al. (2025).

## Invariance And Realization

A rotation of the pump phase rotates the amplified quadrature and the bias together; the probability depends on the bias only through its projection on that quadrature. Changing the loss and the temperature at fixed D leaves the semiclassical law unchanged.

The Kerr coefficient sets the photon number of the stored states and thereby which regime applies. A thermal bath enters through 2n+1. The sweep rate decides which seed is amplified and, at a few photons, whether the wells equilibrate.

## Discriminating Consequences

The dependence on the sweep rate separates the regimes: a probability rising with slower sweeps belongs to the linear stage, a probability independent of the rate to the balance of the wells. A superconducting oscillator can be prepared in both regimes by its Kerr coefficient.

## References For The Physical Derivation

- [C. Roques-Carmes et al., Biasing the quantum vacuum to control macroscopic probability distributions, Science 381, 205 (2023): bias pulses below one photon set the probabilities of the two states of an optical parametric oscillator.](https://arxiv.org/abs/2303.03455)
- [A. Gu et al., Quantum sensitivity of parametric oscillators, Phys. Rev. Research 7, L022056 (2025): the bias-probability relation for a step of the gain, with the initial quantum state and the gain noise.](https://arxiv.org/abs/2412.02887)
- [M. Marthaler and M. I. Dykman, Switching via quantum activation: a parametrically modulated oscillator, Phys. Rev. A 73, 042108 (2006): switching between the two states of the oscillator.](https://arxiv.org/abs/cond-mat/0602288)
- [N. E. Frattini et al., Observation of pairwise level degeneracies and the quantum regime of the Arrhenius law in a double-well parametric oscillator, Phys. Rev. X 14, 031040 (2024), posted as The squeezed Kerr oscillator: spectral kissing and phase-flip robustness: a few-photon Kerr parametric oscillator.](https://arxiv.org/abs/2209.03934)
- [T. Yamaji et al., Spectroscopic observation of the crossover from a classical Duffing oscillator to a Kerr parametric oscillator, Phys. Rev. A 105, 023519 (2022): branch selection by an injected signal.](https://arxiv.org/abs/2010.02621)
- [M. M. Rams, J. Dziarmaga and W. H. Zurek, Symmetry breaking bias and the dynamics of a quantum phase transition, Phys. Rev. Lett. 123, 130603 (2019): a bias across a swept transition.](https://arxiv.org/abs/1905.05783)
