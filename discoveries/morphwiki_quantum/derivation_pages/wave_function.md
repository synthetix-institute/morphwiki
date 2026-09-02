# Wave function

**Physical domain:** Quantum states and subsystem structure

## Mechanism

Wave function is a basis-dependent representative of a pure-state ray; it is not identical to the abstract state or to physical configuration space.

The wave function is a representation of a state in a chosen continuous basis. Treating it as the state itself can obscure that a Fourier transform changes its shape while preserving all predictions.

For a configuration space Q with measure mu, the position wave function is the generalized-basis representative psi(x)=<x|psi> of a ray [psi] in L2(Q,mu). Vectors that differ by a nonzero global phase represent the same pure state. Its modulus squared is a probability density only relative to the stated position measure; spin and particle statistics enlarge or constrain the carrier.

## Physical Construction

The state carrier is the mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. The governing operation is Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed. Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. The calculated observables are Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Topic-specific constructor: abstract state ray, position representation, measure-dependent Born probability, and internal spin carrier.

```math
\mathcal H=L^2(Q,d\mu),\qquad \psi(x)=\langle x|\psi\rangle
\int_Q |\psi(x)|^2\,d\mu(x)=1,\qquad \ket\psi\sim e^{i\alpha}\ket\psi
\Pr(X\in\Delta\mid\psi)=\langle\psi|E_X(\Delta)|\psi\rangle=\int_\Delta|\psi(x)|^2\,d\mu(x)
\mathcal H_{\mathrm{spin}\,s}=L^2(Q,d\mu)\otimes\mathbb C^{2s+1}
```

## Physical Meaning

Its complex value is a probability amplitude. The squared magnitude gives a position density only in the position representation; phase differences remain essential because they control interference and momentum content. Normalization fixes the total probability.

A localized wave packet and its momentum-space Fourier transform emphasize different features of one preparation. Their forms differ, but either representation reproduces the same expectation values when the observables are transformed consistently.

Density operators extend this description to mixtures, subsystems, and open-system dynamics.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:hep-th/0007005](https://arxiv.org/abs/hep-th/0007005)
- [arXiv:hep-th0007005](https://arxiv.org/abs/hep-th0007005)
