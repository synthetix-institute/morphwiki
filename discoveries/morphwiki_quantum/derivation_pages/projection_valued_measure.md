# Projection-valued measure

A row of detectors along a line registers where a particle lands. Each region of the line corresponds to a yes-or-no question about the particle. Answers for disjoint regions exclude one another, and some region always answers yes.

For a particle on the real line, the question for a region $\Delta$ is represented by an operator $E(\Delta)$. It multiplies the wave function by the indicator function $\chi_\Delta$, which equals 1 inside $\Delta$ and 0 outside. These operators are orthogonal projectors, and they combine like the regions themselves:

```math
[E(\Delta)\psi](x)=\chi_\Delta(x)\psi(x),\qquad
E(\Delta_1)E(\Delta_2)=E(\Delta_1\cap\Delta_2),\qquad E(\mathbb R)=I.
```

For disjoint regions the projectors add, including for countable unions. This family is a projection-valued measure (PVM). The probability of a yes answer in a state $\psi$ is $\langle\psi|E(\Delta)|\psi\rangle=\int_\Delta|\psi|^2dx$. By the spectral theorem every self-adjoint operator has exactly one such measure on the real line, so a PVM is the complete description of a sharp observable. For a discrete observable such as a spin component, the measure is concentrated on the eigenvalues. Then $E(\{m\})$ is the projector onto the eigenspace with eigenvalue $m$, and a Stern--Gerlach magnet sends each eigenspace to its own spot.

Consider the ground state $\sqrt{2/L}\sin(\pi x/L)$ of a particle in a box of length $L$. The probability that a detector covering the middle third responds is

```math
p\left(\tfrac{L}{3}<x<\tfrac{2L}{3}\right)=\frac{2}{L}\int_{L/3}^{2L/3}\sin^2\frac{\pi x}{L}\,dx
=\frac13+\frac{\sqrt3}{2\pi}\approx0.609.
```

The $n=2$ level, with a node at the centre, gives $1/3-\sqrt3/(4\pi)\approx0.196$ instead. Because $E(\Delta)^2=E(\Delta)$, a state that has just answered yes lies in the range of $E(\Delta)$. An immediate repetition then answers yes with certainty, which is the repeatability that defines a sharp measurement.

Commuting observables share a joint measure. The $x$ and $y$ coordinates of a particle give rectangle projectors $E_X(\Delta_x)E_Y(\Delta_y)$, and a camera measures both at once. Position and momentum have no such joint measure. A nonzero wave function cannot vanish outside a bounded interval while its Fourier transform also vanishes outside a bounded interval, so

```math
\operatorname{ran}E_X(\Delta)\cap\operatorname{ran}E_P(\Gamma)=\{0\}
\qquad\text{for bounded }\Delta,\Gamma.
```

No state answers yes with certainty to both questions. This does not follow from the variance bound of the uncertainty principle. It forbids exact confinement to bounded regions of any size, including regions whose product of widths greatly exceeds $\hbar$.

Real pixels have blurred edges. A detector whose response function $\mu_\Delta(x)$ takes values strictly between 0 and 1 near the edges is represented by $F(\Delta)=\int\mu_\Delta(x)\,|x\rangle\langle x|\,dx$, which satisfies $F^2\neq F$. It is a POVM rather than a PVM, and its records need not repeat. The PVM is the ideal limit in which the response is exactly 0 or 1.

## References For The Physical Derivation

- [T. Heinosaari and M. Ziman, Guide to Mathematical Concepts of Quantum Theory; projection-valued measures, joint measurability and smeared observables.](https://arxiv.org/abs/0810.3536)
- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; spectral theorem and projection-valued measures of self-adjoint operators.](https://arxiv.org/abs/1508.06951)
