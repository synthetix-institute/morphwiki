# Hilbert space

**Derivation step:** Formal context: carrier, domain, and representation

## Topic Context

The mathematical concept of a Hilbert space generalizes the notion of Euclidean space. It extends the methods of Euclidean geometry and calculus from the two-dimensional Euclidean plane and three-dimensional space to spaces of any finite or infinite dimension. A Hilbert space is an abstract vector space, and it has the additional structure of an inner product that allows length and angle to be measured. Finally, Hilbert spaces are required to be complete, a property that stipulates the existence of enough limits in the space to allow the techniques of calculus to be used.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Hilbert_space)

## Role In The Derivation

Hilbert space is the admissible state carrier of quantum theory: it supplies the space in which states, operators, bases, spectra, and probabilities become legally defined.

## Why This Step Is Needed

Hilbert space is not merely a container for wave functions. Its inner product defines amplitudes and orthogonality, while the domains of unbounded operators decide whether expressions for position, momentum, and energy are mathematically and physically admissible.

## Mechanism

Hilbert space is not physical space and not a geometric background in this book. It is the legal carrier of quantum identity. A state is a vector or density operator on it; the inner product gives amplitudes and norms; observables are self-adjoint operators on it; spectral projectors define possible answers; and unitary evolution preserves norm and probability. Hilbert space is therefore central because it binds state, probability, operator spectrum, and identity preservation into one formal carrier.

## How It Enters The Theory

**Place in the construction.** Hilbert space contributes a state-carrier role to the quantum construction. This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.

**State and operation.** A complex Hilbert space, or a density-operator state space built on it. Self-adjoint observables, unitary maps, spectral projectors, and domain-restricted generators defined on the carrier.

**Admissibility and prediction.** Inner-product structure, normalization, positivity for density states, and operator-domain conditions make states and observables legal. Born probabilities, spectral projectors, expectation values, and preserved norms.

## Topic Equations

Standard constructor skeleton: normalized states, density states, spectral resolution, Born observable, and unitary identity preservation.

```math
\ket{\psi}\in\mathcal H,\qquad \langle\psi|\psi\rangle=1
\rho\in\mathcal S(\mathcal H),\qquad \rho\ge0,\quad \operatorname{Tr}\rho=1
A=A^\dagger,\qquad A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)
\Pr(\Delta\mid \rho,A)=\operatorname{Tr}\!\left(\rho E_A(\Delta)\right)
\rho_t=U(t)\rho U(t)^\dagger,\qquad U^\dagger U=I
```

## How To Read The Relation

The linear structure permits superposition, the inner product converts pairs of states into amplitudes, and completeness guarantees that convergent sequences of approximations remain inside the space. Operator domains must be carried with the operators; the same differential formula on another domain can describe a different physical system.

## Worked Example

A qubit lives in a two-dimensional complex space, whereas a particle on a line is described in a space of square-integrable functions. Both obey the same Hilbert-space logic, but their operators, spectra, and boundary conditions are different.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

After the arena is fixed, a quantum state selects one preparation or statistical ensemble within it.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:2308.15676](https://arxiv.org/abs/2308.15676)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:0809.5271](https://arxiv.org/abs/0809.5271)
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733)
