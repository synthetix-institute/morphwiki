# Fock space

**Physical domain:** Fields, constraints, and scale

## Mechanism

Fock space is the occupation-number state space: the construction that replaces a fixed-particle Hilbert space by a direct sum over particle number.

Fock space places quantum dynamics in a relativistic, many-body, field, gauge, geometric, or scale-dependent setting. The state space and operator domain must therefore be specified for that setting rather than inferred from a single-particle model.

Fock space changes the carrier of the quantum state. Instead of describing one system in one Hilbert space, it builds sectors with zero, one, two, and more identical quanta, then imposes the bosonic or fermionic exchange rule. Creation and annihilation operators are the native coordinates of this page because they move the state between occupation sectors.

## Physical Construction

The state carrier is Fock space, field configuration space, or a sector selected by charge, spin, momentum, statistics, or gauge data. The governing operation is Creation, annihilation, field, charge, spin, Hamiltonian, or scattering operators acting on the admissible sector. Statistics, gauge constraints, commutation or anticommutation rules, domain conditions, and sector labels decide which states are legal. The calculated observables are Occupation number, charge, spin, momentum, energy, correlation function, cross-section, or scattering amplitude.

## Topic Equations

Topic-specific constructor: the equations express variable particle number, exchange symmetry, and occupation-number observable.

```math
\mathcal F_{\pm}(\mathcal H)=\bigoplus_{n=0}^{\infty} \mathcal S_{\pm}\mathcal H^{\otimes n}
[a_i,a_j^\dagger]_{\mp}=\delta_{ij},\qquad [a_i,a_j]_{\mp}=0
N=\sum_i a_i^\dagger a_i,\qquad N\ket{n_1,n_2,\ldots}=\left(\sum_i n_i\right)\ket{n_1,n_2,\ldots}
```

## Physical Meaning

Different topics in this branch use different carriers: spinor wave functions, Fock spaces, many-body states, gauge sectors, geometric states, or effective low-energy sectors. Their physical content is fixed by the associated field equation or Hamiltonian, its constraints and domain, and the amplitudes, spectra, charges, or correlation functions it predicts.

Field and many-body mechanisms become experimentally useful when assembled into an ordered intervention. The protocol chapter shows how preparation, controlled evolution, measurement, and correction compose into one executable map.

## Invariance And Realization

The relation between prepared states, observables, and spectral probability measures. The use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations. The dependence of the observable on basis, domain, potential, preparation, or measurement context. The commutator structure that limits which observables can be jointly diagonalized.

The physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation. The representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields. Where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight. The implementation of preparation, boundary condition, detector, or outcome channel.

## Discriminating Consequences

A transfer target provides a state space, a transformation law, and a spectral or categorical observable, with one compatibility relation experimentally unresolved. A useful validation varies the basis, domain, or measurement context and measures whether the allowed observable changes while the underlying transformation law remains identifiable. A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
