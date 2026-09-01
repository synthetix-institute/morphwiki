# Photon

## Central Claim
A photon is the one-quantum excitation of an electromagnetic field mode: its identity is fixed by field quantization, massless dispersion, polarization, gauge constraints, and detector readout.

## Formal Role
The photon page should not be reduced to a generic prepared-state template. The native construction starts with the electromagnetic field decomposed into modes. Quantization assigns creation and annihilation operators to those modes; applying a creation operator to the vacuum gives a one-photon state. The readouts are mode occupation, frequency or energy, momentum, polarization, and detection events. The admissibility constraints include massless dispersion and transversality or gauge conditions, which distinguish the photon from a generic quantum particle.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- The electromagnetic field decomposes into modes labelled by wave vector and polarization.
- Each mode is quantized with creation and annihilation operators.
- A one-photon state is the result of applying a creation operator to the vacuum.
- Occupation number, energy, momentum, polarization, and detector clicks are readout channels.
- Massless dispersion and transverse or gauge-compatible polarization define admissibility.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
E=\hbar\omega,\quad \mathbf p=\hbar\mathbf k,\quad \omega=c|\mathbf k|
|1_{\mathbf k,\lambda}\rangle=a_{\mathbf k,\lambda}^{\dagger}|0\rangle
\hat N_{\mathbf k,\lambda}=a_{\mathbf k,\lambda}^{\dagger}a_{\mathbf k,\lambda}
\mathbf k\cdot\boldsymbol\epsilon_{\mathbf k,\lambda}=0
```

## Mechanism Roles
- **state:** one-photon Fock state; electromagnetic mode; polarization state
- **operator:** creation operator; annihilation operator; number operator; field operator
- **spectrum:** frequency; energy; momentum; polarization
- **boundary:** mode boundary; cavity; free-space asymptotic condition; gauge constraint
- **incompatibility:** number-phase relation; polarization basis choice; gauge constraint
- **protocol:** emission; absorption; photodetection; interferometry

## Representation-Stable Content
- the relation between prepared states, observables, and spectral probability measures
- the use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations
- the dependence of the readout on basis, domain, potential, preparation, or measurement context
- the commutator structure that limits which observables can be jointly diagonalized

## Representation-Dependent Content
- the physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation
- the representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields
- where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight
- the implementation of preparation, boundary condition, detector, or readout channel

## Validation Checks
- A transfer target provides a state space, a transformation law, and a spectral or categorical readout, with one compatibility relation experimentally unresolved.
- A useful validation varies the basis, domain, or measurement context and measures whether the allowed readout changes while the underlying transformation law remains identifiable.
- A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.
