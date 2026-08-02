# Particle in a box

**Derivation step:** Boundary realization: how effects appear

## Topic Context

In quantum mechanics, the particle in a box model describes the movement of a free particle in a small space surrounded by impenetrable barriers. The model is mainly used as a hypothetical example to illustrate the differences between classical and quantum systems. In classical systems, for example, a particle trapped inside a large box can move at any speed within the box and it is no more likely to be found at one position than another. However, when the well becomes very narrow, quantum effects become important. The particle may only occupy certain positive energy levels. Likewise, it can never have zero energy, meaning that the particle can never "sit still".

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Particle_in_a_box)

## Role In The Derivation

Particle in a box is a boundary-spectrum constructor: a spatial domain and boundary condition discretize the allowed energy spectrum.

## Why This Step Is Needed

The particle in a box shows in the simplest form that a boundary condition is part of the Hamiltonian's physical definition. Confinement turns a continuous free-particle spectrum into discrete allowed energies.

## Mechanism

The page shows how a boundary condition changes the domain of the Hamiltonian and therefore the allowed spectra.

## How It Enters The Theory

**Place in the construction.** Particle in a box contributes a many-mode field or particle-realization role to the quantum construction. This page is read first as a realization move: it changes the domain, boundary, geometry, or interface in which the operator acts.

**State and operation.** Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data. Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector.

**Admissibility and prediction.** Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal. Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.

## Topic Equations

Standard constructor skeleton: boundary condition and discrete spectrum.

```math
\psi(0)=\psi(L)=0
\psi_n(x)=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}
E_n=\frac{\hbar^2\pi^2n^2}{2mL^2}
```

## How To Read The Relation

The wave function satisfies the same differential equation inside the box as a free particle, but vanishing boundary values select standing waves. Only wavelengths fitting the interval are admissible, and their curvature fixes the quantized energies.

## Worked Example

Doubling the box length reduces every level spacing by a factor of four. This follows from the boundary-selected wavelength and provides a direct check of the construction.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Replacing an impenetrable wall by a finite barrier leads to tunnelling, resonances, and scattering channels.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:0908.0752](https://arxiv.org/abs/0908.0752)
