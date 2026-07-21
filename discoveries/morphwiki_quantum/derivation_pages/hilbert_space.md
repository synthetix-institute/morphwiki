# Hilbert space

**Derivation step:** Hilbert-space context: admissible carrier and basis
**Status:** topic-specific mechanism

## Role In The Derivation

Hilbert space is the admissible state carrier of quantum theory: it supplies the space in which states, operators, bases, spectra, and probabilities become legally defined.

## Mechanism

Hilbert space is not physical space and not a geometric background in this book. It is the legal carrier of quantum identity. A state is a vector or density operator on it; the inner product gives amplitudes and norms; observables are self-adjoint operators on it; spectral projectors define possible answers; and unitary evolution preserves norm and probability. Hilbert space is therefore central because it binds state, probability, operator spectrum, and identity preservation into one formal carrier. The linked equation set is concentrated in operator-to-spectrum readout, state evolution, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Hilbert space contributes a state-carrier role to the quantum construction.
- **Placement:** This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.
- **Carrier or domain:** A complex Hilbert space, or a density-operator state space built on it.
- **Operator or map:** Self-adjoint observables, unitary maps, spectral projectors, and domain-restricted generators defined on the carrier.
- **Admissibility:** Inner-product structure, normalization, positivity for density states, and operator-domain conditions make states and observables legal.
- **Readout:** Born probabilities, spectral projectors, expectation values, and preserved norms.
- **Check:** Changing basis or representation should preserve probabilities and expectation values when the change is unitary.

## Topic Equations

Standard constructor skeleton: normalized states, density states, spectral resolution, Born readout, and unitary identity preservation.

```math
\ket{\psi}\in\mathcal H,\qquad \langle\psi|\psi\rangle=1
\rho\in\mathcal S(\mathcal H),\qquad \rho\ge0,\quad \operatorname{Tr}\rho=1
A=A^\dagger,\qquad A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)
\Pr(\Delta\mid \rho,A)=\operatorname{Tr}\!\left(\rho E_A(\Delta)\right)
\rho_t=U(t)\rho U(t)^\dagger,\qquad U^\dagger U=I
```

## What Remains Stable

- the rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation
- the operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels
- the dependence of admissible readout on measurement context or boundary condition
- the non-commuting compatibility structure, which survives changes of representation

## What Changes With Realization

- the name of the carrier: particle, wave, field, qubit, or excitation
- where time dependence is represented: on the state, on the operator, or in a path weight
- the coordinate system, basis, or geometric picture used to display the same relation
- the physical implementation of detector, boundary, preparation, or readout

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:2308.15676](https://arxiv.org/abs/2308.15676)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:0809.5271](https://arxiv.org/abs/0809.5271)
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733)
