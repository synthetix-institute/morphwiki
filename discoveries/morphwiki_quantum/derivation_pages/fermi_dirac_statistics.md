# Fermi–Dirac statistics

**Derivation step:** Many-mode extension: fields, particles, and scaling

## Topic Context

Fermi–Dirac statistics is a type of quantum statistics that applies to the physics of a system consisting of many non-interacting, identical particles that obey the Pauli exclusion principle. A result is the Fermi–Dirac distribution of particles over energy states. It is named after Enrico Fermi and Paul Dirac, each of whom derived the distribution independently in 1926. Fermi–Dirac statistics is a part of the field of statistical mechanics and uses the principles of quantum mechanics.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Fermi%E2%80%93Dirac_statistics)

## Role In The Derivation

Fermi–Dirac statistics is an antisymmetric-state constructor: exchange statistics restricts which many-fermion occupation patterns are admissible.

## Why This Step Is Needed

Fermi-Dirac statistics is needed because identical fermions do not occupy many-particle states independently. Antisymmetry under particle exchange, and the exclusion principle that follows from it, changes the allowed occupation patterns before any Hamiltonian dynamics is considered.

## Mechanism

Fermi-Dirac statistics is an admissibility rule, not a generator of time evolution. Anticommutation and antisymmetry imply single occupation of each one-particle mode, while the thermal distribution states the mean occupation of those modes.

## How It Enters The Theory

**Place in the construction.** Fermi–Dirac statistics contributes a fermionic state-admissibility role to the quantum construction. This page is read first as a many-mode or field-realization move: it extends the state and operator construction beyond a single-particle carrier.

**State and operation.** A fermionic Fock space assembled from antisymmetric many-particle sectors or occupation-number modes. Creation, annihilation, and number operators obeying canonical anticommutation relations.

**Admissibility and prediction.** Exchange antisymmetry restricts each one-particle mode to occupation zero or one for each internal state. Mode occupations, Fermi energy, particle density, pressure, heat capacity, and other equilibrium response functions.

## Topic Equations

Topic-specific construction: antisymmetric mode algebra, exclusion, and equilibrium occupation.

```math
\{a_i,a_j^\dagger\}=\delta_{ij},\qquad n_i\in\{0,1\}
\bar n_i=\frac{1}{e^{\beta(\varepsilon_i-\mu)}+1}
```

## How To Read The Relation

Single-particle energy levels provide the available modes, while each mode can be occupied at most once per internal state. The Fermi-Dirac distribution gives the mean occupation at thermal equilibrium. At zero temperature it fills modes up to the Fermi energy.

## Worked Example

The degeneracy pressure of an electron gas follows from filling successively higher momentum states even without a repulsive force between the electrons. The effect is a consequence of antisymmetric state construction.

## What Remains Stable

Exchange antisymmetry and canonical anticommutation define the fermionic many-particle sectors. Each one-particle mode has occupation zero or one for each internal state. The Fermi-Dirac function gives the equilibrium mean occupation once energy, temperature, and chemical potential are specified.

## What The Physical Realization Adds

The dispersion relation, dimensionality, degeneracy, density of states, and interaction approximation depend on the physical system. Electrons, atoms, nucleons, and fermionic quasiparticles realize the same exchange rule with different Hamiltonians and observables. Finite temperature smooths the occupation edge that is sharp at the Fermi energy in the ideal zero-temperature limit.

## Connection To The Next Step

Bose-Einstein statistics changes the exchange rule from antisymmetric to symmetric and therefore permits unlimited occupation of one mode.

## Checks

- Recover occupations restricted to zero or one and the ideal zero-temperature Fermi sea.
- Recover the Maxwell-Boltzmann distribution in the dilute low-fugacity limit.
- Integrate the mode occupations against the density of states and verify the specified particle number.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
