# Fermion

**Physical domain:** Fields, constraints, and scale

## Mechanism

Fermion is an exchange-antisymmetry construction: exchanging two identical fermions reverses the many-body amplitude, so coincident one-particle states are removed from the admissible state space.

A many-particle Hilbert space does not specify how identical particles are exchanged. Choosing the antisymmetric representation removes coincidence states and changes the spectrum, pressure, correlations, and admissible collective phases before a particular interaction Hamiltonian is chosen.

The defining object is the antisymmetric many-body sector, not a particle name. Its nodal set contains every coincidence configuration, and the canonical anticommutation relations preserve that restriction while particles are added or removed. Filling distinct one-particle modes then produces an exchange hole, a Fermi surface and degeneracy pressure even in the absence of a repulsive potential.

## Physical Construction

The state carrier is Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data. The governing operation is Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector. Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal. The calculated observables are Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.

## Topic Equations

The exchange sign fixes the admissible state space; exterior Fock space and anticommutation extend it to variable particle number.

```math
\Psi(\ldots,x_i,\ldots,x_j,\ldots)=-\Psi(\ldots,x_j,\ldots,x_i,\ldots),\qquad \Psi(\ldots,x,\ldots,x,\ldots)=0
\mathcal F_{-}(\mathcal H)=\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H
\{a_i,a_j^\dagger\}=\delta_{ij},\qquad \{a_i,a_j\}=0
n_i=a_i^\dagger a_i\in\{0,1\}
```

## Physical Meaning

The minus sign acquired under exchange makes every Slater determinant vanish when two columns coincide. In occupation language the same restriction is encoded by anticommutation and by eigenvalues zero or one of each mode-number operator. These are equivalent descriptions of one state-space constraint.

A zero-temperature ideal Fermi gas fills all momentum modes up to the Fermi momentum. Compressing the gas therefore forces particles into higher-momentum states and raises its pressure even when the interaction potential is set to zero.

Fermi--Dirac statistics adds thermal occupation to this exchange-constrained state space. Pairing, bosonization and Jordan--Wigner transformations then test which consequences of fermionic algebra survive on a different carrier.

## Consequences Forced By The Relation

Antisymmetry forces the wave function to vanish when two identical fermions occupy the same one-particle state. The resulting exchange hole is present before a dynamical interaction is specified. At finite density, distinct momentum states fill up to the Fermi surface. The associated kinetic energy and degeneracy pressure arise from state counting rather than from pairwise repulsion. Pairing changes the exchange sector: a bound state of two fermions has even fermion parity and can acquire bosonic collective behaviour, as in superconductors and superfluid helium-3.

## Transformations To Other Physical Realizations

In one dimension, hard-core bosons and free fermions can share the same density spectrum. The map changes exchange phases and off-diagonal correlations, so equality of energies does not imply identity of all observables. A Jordan--Wigner map carries local fermionic occupation into spins by adding a parity string. The exchange algebra survives, but locality is transferred into an ordered, generally nonlocal operator. In two dimensions, exchanges are classified by braids rather than only by permutations. Anyonic statistics therefore extends, rather than merely interpolates between, the boson and fermion constructions.

## Domain Of The Construction

The relativistic spin--statistics theorem additionally requires locality, positive energy and the relativistic field framework. Antisymmetric lattice or effective quasiparticle models do not by themselves establish that theorem. Fermi surfaces and degeneracy pressure require a many-mode spectrum and a specified density or particle-number constraint; they do not follow from the word fermion alone.

## Invariance And Realization

Exchange antisymmetry, exterior-product state space, canonical anticommutation and zero-or-one mode occupation are equivalent forms of the fermionic restriction. The coincidence node and exchange hole survive changes between first-quantized wave functions, Slater determinants and second-quantized fields. Fermion parity remains meaningful when particle number changes, including in paired and superconducting states.

Mass, charge, dispersion, dimensionality, interaction law and gauge representation belong to the physical realization and are not fixed by exchange statistics. A change of carrier can turn local fermion operators into nonlocal strings, as in the Jordan--Wigner transformation. Two-dimensional braid statistics and composite-particle structure alter the exchange construction beyond the elementary boson--fermion dichotomy.

## Discriminating Consequences

The defining relation is antisymmetry or canonical anticommutation and the resulting zero-or-one occupation spectrum. At fixed one-particle spectrum, compare with distinguishable-particle and sign-erased controls to isolate exchange. For a claimed transfer, compare correlations and locality as well as energies; spectral agreement alone is insufficient.

## Source Equations

- [arXiv:cond-mat/0005069](https://arxiv.org/abs/cond-mat/0005069)
- [arXiv:cond-mat0005069](https://arxiv.org/abs/cond-mat0005069)
- [arXiv:quant-ph/0305150](https://arxiv.org/abs/quant-ph/0305150)
- [arXiv:quant-ph0305150](https://arxiv.org/abs/quant-ph0305150)
- [arXiv:hep-ph/0007343](https://arxiv.org/abs/hep-ph/0007343)
- [arXiv:hep-ph0007343](https://arxiv.org/abs/hep-ph0007343)
