# Wave function

**Derivation step:** State carrier inside Hilbert space

## Topic Context

In quantum mechanics, a wave function is a mathematical description of the quantum state of an isolated quantum system. The most common symbols for a wave function are the Greek letters ψ and Ψ.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Wave_function)

## Role In The Derivation

Wave function is a basis-dependent representative of a pure-state ray; it is not identical to the abstract state or to physical configuration space.

## Why This Step Is Needed

The wave function is a representation of a state in a chosen continuous basis. Treating it as the state itself can obscure that a Fourier transform changes its shape while preserving all predictions.

## Mechanism

For a configuration space Q with measure mu, the position wave function is the generalized-basis representative psi(x)=<x|psi> of a ray [psi] in L2(Q,mu). Vectors that differ by a nonzero global phase represent the same pure state. Its modulus squared is a probability density only relative to the stated position measure; spin and particle statistics enlarge or constrain the carrier.

## How It Enters The Theory

**Place in the construction.** Wave function contributes a state-carrier role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.

**Admissibility and prediction.** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Topic-specific constructor: abstract state ray, position representation, measure-dependent Born probability, and internal spin carrier.

```math
\mathcal H=L^2(Q,d\mu),\qquad \psi(x)=\langle x|\psi\rangle
\int_Q |\psi(x)|^2\,d\mu(x)=1,\qquad \ket\psi\sim e^{i\alpha}\ket\psi
\Pr(X\in\Delta\mid\psi)=\langle\psi|E_X(\Delta)|\psi\rangle=\int_\Delta|\psi(x)|^2\,d\mu(x)
\mathcal H_{\mathrm{spin}\,s}=L^2(Q,d\mu)\otimes\mathbb C^{2s+1}
```

## How To Read The Relation

Its complex value is a probability amplitude. The squared magnitude gives a position density only in the position representation; phase differences remain essential because they control interference and momentum content. Normalization fixes the total probability.

## Worked Example

A localized wave packet and its momentum-space Fourier transform emphasize different features of one preparation. Their forms differ, but either representation reproduces the same expectation values when the observables are transformed consistently.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Density operators extend this description to mixtures, subsystems, and open-system dynamics.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
