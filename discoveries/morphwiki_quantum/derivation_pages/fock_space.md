# Fock space

**Derivation step:** Many-mode extension: fields, particles, and scaling

## Topic Context

The Fock space is an algebraic construction used in quantum mechanics to construct the quantum states space of a variable or unknown number of identical particles from a single particle Hilbert space H. It is named after V. A. Fock who first introduced it in his 1932 paper "Konfigurationsraum und zweite Quantelung".

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Fock_space)

## Role In The Derivation

Fock space is the occupation-number state space: the construction that replaces a fixed-particle Hilbert space by a direct sum over particle number.

## Why This Step Is Needed

Fock space is needed when particle number can change, collective modes matter, or locality and gauge symmetry organize the admissible states. A single-particle Hilbert space is then replaced by a Fock space, field configuration space, or constrained sector.

## Mechanism

Fock space changes the carrier of the quantum state. Instead of describing one system in one Hilbert space, it builds sectors with zero, one, two, and more identical quanta, then imposes the bosonic or fermionic exchange rule. Creation and annihilation operators are the native coordinates of this page because they move the state between occupation sectors.

## How It Enters The Theory

**Place in the construction.** Fock space contributes a many-mode field or particle-realization role to the quantum construction. This page is read first as a many-mode or field-realization move: it extends the state and operator construction beyond a single-particle carrier.

**State and operation.** Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data. Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector.

**Admissibility and prediction.** Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal. Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.

## Topic Equations

Topic-specific constructor: the equations express variable particle number, exchange symmetry, and occupation-number observable.

```math
\mathcal F_{\pm}(\mathcal H)=\bigoplus_{n=0}^{\infty} \mathcal S_{\pm}\mathcal H^{\otimes n}
[a_i,a_j^\dagger]_{\mp}=\delta_{ij},\qquad [a_i,a_j]_{\mp}=0
N=\sum_i a_i^\dagger a_i,\qquad N\ket{n_1,n_2,\ldots}=\left(\sum_i n_i\right)\ket{n_1,n_2,\ldots}
```

## How To Read The Relation

Creation and annihilation operators change occupation while respecting bosonic or fermionic statistics. Correlation functions replace single-particle wave functions as the principal predictions. Gauge constraints remove redundant descriptions, and renormalization states how parameters change with observational scale.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Field and many-body mechanisms become experimentally useful when assembled into an ordered intervention. The protocol chapter shows how preparation, controlled evolution, measurement, and correction compose into one executable map.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:2308.15676](https://arxiv.org/abs/2308.15676)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:0809.5271](https://arxiv.org/abs/0809.5271)
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
