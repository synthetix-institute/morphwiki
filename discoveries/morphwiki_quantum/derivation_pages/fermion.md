# Fermion

**Physical domain:** Fields, constraints, and scale

## Mechanism

Fermion is an exchange-antisymmetry construction: exchanging two identical fermions reverses the many-body amplitude, so coincident one-particle states are removed from the admissible state space.

The tensor product of one-particle spaces contains both symmetric and antisymmetric states. Identical fermions occupy its antisymmetric sector: exchanging the complete position and spin coordinates changes the sign of the amplitude. This restriction determines which many-particle occupations are allowed for a specified Hamiltonian.

Let $z=(x,\sigma)$ denote the complete one-particle coordinate, including spin. Antisymmetry makes the amplitude vanish when two $z$ coordinates coincide. Equal positions with opposite spins do not satisfy that condition: two electrons may occupy one spatial orbital in a spin singlet. The anticommutation relations impose the same exclusion when particles are added to individual spin-orbitals.

## Physical Construction

The state carrier is the antisymmetric many-particle sector of the one-particle Hilbert space, including spin. The governing operation is the many-body Hamiltonian and fermionic creation and annihilation operators. Exchange antisymmetry restricts states and mode occupations; the Hamiltonian specifies interactions and evolution. The calculated observables are mode occupations, spin-resolved correlations, energies and thermodynamic response.

## Topic Equations

Each index i labels a complete spin-orbital. The number operator has eigenvalues zero and one; its expectation can take any value between them. Exterior Fock space extends the antisymmetric state construction to variable particle number.

```math
z_i=(x_i,\sigma_i),\qquad \Psi(\ldots,z_i,\ldots,z_j,\ldots)=-\Psi(\ldots,z_j,\ldots,z_i,\ldots)
\Psi(\ldots,z,\ldots,z,\ldots)=0
\mathcal F_{-}(\mathcal H)=\bigoplus_{n=0}^{\infty}\wedge^n\mathcal H
\{a_i,a_j^\dagger\}=\delta_{ij},\qquad \{a_i,a_j\}=0
n_i=a_i^\dagger a_i,\qquad n_i^2=n_i,\qquad\operatorname{spec}(n_i)=\{0,1\}
```

## Physical Meaning

The minus sign acquired under exchange makes every Slater determinant vanish when two columns coincide. In occupation language the same restriction is encoded by anticommutation and by eigenvalues zero or one of each mode-number operator. These are equivalent descriptions of one state-space constraint.

A zero-temperature ideal Fermi gas fills all momentum modes up to the Fermi momentum. Compressing the gas therefore forces particles into higher-momentum states and raises its pressure even when the interaction potential is set to zero.

Fermi--Dirac statistics adds thermal occupation to this exchange-constrained state space. Pairing, bosonization and Jordan--Wigner transformations then test which consequences of fermionic algebra survive on a different carrier.

## Consequences Forced By The Relation

Antisymmetry forces the wave function to vanish when two identical fermions occupy the same one-particle state. The resulting exchange hole is present before a dynamical interaction is specified. For a homogeneous ideal gas at zero temperature, filling distinct momentum spin-orbitals up to the Fermi energy produces degeneracy pressure without pairwise repulsion. Pairing preserves antisymmetry of the constituent fermions. A pair has even fermion parity and may support a bosonic collective order parameter, as in superconductors and superfluid helium-3; it need not be a tightly bound elementary boson.

## Transformations To Other Physical Realizations

In one dimension, hard-core bosons and free fermions can share the same density spectrum. The map changes exchange phases and off-diagonal correlations, so equality of energies does not imply identity of all observables. A Jordan--Wigner map carries local fermionic occupation into spins by adding a parity string. The exchange algebra survives, but locality is transferred into an ordered, generally nonlocal operator. In two dimensions, exchanges are classified by braids rather than only by permutations. Anyonic statistics therefore extends, rather than merely interpolates between, the boson and fermion constructions.

## Domain Of The Construction

The relativistic spin--statistics theorem additionally requires locality, positive energy and the relativistic field framework. Antisymmetric lattice or effective quasiparticle models do not by themselves establish that theorem. Fermi surfaces and degeneracy pressure require a many-mode spectrum and a specified density or particle-number constraint; they do not follow from the word fermion alone.

## Invariance And Realization

Exchange antisymmetry, exterior-product state space, canonical anticommutation and zero-or-one mode occupation are equivalent forms of the fermionic restriction. The node at equal complete coordinates and the same-spin exchange hole survive changes between first-quantized wave functions and second-quantized fields. Antisymmetric correlated states can require a superposition of Slater determinants. Fermion parity remains meaningful when particle number changes, including in paired and superconducting states.

Mass, charge, dispersion, dimensionality, interaction law and gauge representation belong to the physical realization and are not fixed by exchange statistics. A change of carrier can turn local fermion operators into nonlocal strings, as in the Jordan--Wigner transformation. Two-dimensional braid statistics and composite-particle structure alter the exchange construction beyond the elementary boson--fermion dichotomy.

## Discriminating Consequences

The defining relation is antisymmetry or canonical anticommutation and the resulting zero-or-one occupation spectrum. At fixed one-particle spectrum, compare with distinguishable-particle and sign-erased controls to isolate exchange. For a claimed transfer, compare correlations and locality as well as energies; spectral agreement alone is insufficient.

## Source Equations

- [arXiv:cond-mat/0005069](https://arxiv.org/abs/cond-mat/0005069)
- [arXiv:quant-ph/0305150](https://arxiv.org/abs/quant-ph/0305150)
- [arXiv:hep-ph/0007343](https://arxiv.org/abs/hep-ph/0007343)

## References For The Physical Derivation

- [S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold atomic Fermi gases, sections II and V.2.2: occupation and spin-resolved correlations.](https://arxiv.org/abs/0706.3360)
