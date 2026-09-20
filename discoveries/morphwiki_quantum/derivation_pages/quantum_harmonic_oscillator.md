# Quantum harmonic oscillator

Small oscillations about a stable equilibrium have a quadratic energy. Quantizing that local approximation produces equally spaced excitations and a nonzero ground-state variance. For mass $m$, angular frequency $\omega>0$, position $X$ and momentum $P$, take

```math
H=\frac{P^2}{2m}+\frac12m\omega^2X^2,\qquad
a=\sqrt{\frac{m\omega}{2\hbar}}X+\frac{iP}{\sqrt{2m\hbar\omega}}.
```

The canonical commutator gives $[a,a^\dagger]=1$. Substituting $a$ and $a^\dagger$ into the energy leaves an additive term from their noncommutation:

```math
H=\hbar\omega\left(a^\dagger a+\frac12\right),\qquad
E_n=\hbar\omega\left(n+\frac12\right).
```

Positivity of $a^\dagger a$ bounds the energy below. Repeated lowering reaches a state annihilated by $a$; raising generates the nonnegative integer occupations. The half-quantum is consequently fixed by the operator algebra. It is not a fitted offset introduced to match a spectrum.

The ground state has position variance $\hbar/(2m\omega)$ and momentum variance $m\hbar\omega/2$. Their product saturates the preparation uncertainty relation. Displacing that state changes the mean position and momentum while leaving the variances fixed. Under the harmonic Hamiltonian, those means obey the classical oscillator equation, even though the state retains quantum fluctuations.

```math
X(t)=X(0)\cos\omega t+\frac{P(0)}{m\omega}\sin\omega t.
```

The equation is an operator identity. Taking expectations gives the classical motion of the center; taking products gives correlations and variances. A thermal mixture has zero mean displacement but fluctuating energy and a larger position variance. A squeezed state instead redistributes variance between the two quadratures, and that anisotropy rotates in phase space.

The same construction describes a normal mode of a vibrating solid or electromagnetic cavity after its generalized coordinate, conjugate momentum and normalization have been identified. The material and boundary conditions determine the frequency and mode shape. Anharmonic interactions couple modes or shift their spacing, while damping adds an environment and its fluctuations. The oscillator is therefore a transferable quadratic mechanism, not an assertion that all its realizations have identical lifetimes, couplings or measurement units.

For a finite matrix truncation, the highest retained state breaks the exact ladder algebra. This can be checked directly rather than interpreted as a physical correction. Predictions for low occupations converge as the truncation is enlarged; strong driving that reaches the cutoff requires a larger state space.

## References For The Physical Derivation

- [C. Weedbrook and colleagues, Gaussian Quantum Information; canonical quadratures, Gaussian states and transformations.](https://arxiv.org/abs/1110.3234)


## Relations In The Original Papers

[arXiv:1110.3234v1, S2.E3](https://arxiv.org/html/1110.3234v1#S2.E3). The annihilation operator lowers an oscillator number state with amplitude equal to the square root of its occupation. An infinite bosonic Fock space; finite truncations change the commutator at the upper boundary.
