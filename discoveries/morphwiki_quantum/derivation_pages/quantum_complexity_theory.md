# Quantum complexity theory

**Derivation step:** Hilbert-space context: admissible carrier and basis
**Status:** topic-specific mechanism
**Dominant evidence signal:** preparation and boundary context

## Role In The Derivation

A quantum complexity theory can be read as a quantum construction: the chosen basis, pulse sequence, or measurement axis fixes the admissible state space; a Hamiltonian or unitary matrix rotating that state between preparation and measurement defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## Mechanism

In quantum-mechanical terms, a quantum complexity theory is described by a two-dimensional Hilbert space, usually written as a qubit state or a density matrix. The physical question is represented by a Hamiltonian or unitary matrix rotating that state between preparation and measurement; the experimental or mathematical setting is the chosen basis, pulse sequence, or measurement axis. The observable content is obtained from projectors onto the two eigenstates of the measured observable. In the local terminology of this topic, the same construction appears through state vector or wave function, Hamiltonian or observable operator, and eigenvalue or energy level. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or uncertainty relation. In the source-evidence profile for this page, the strongest construction signal is preparation, basis, or boundary context, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum complexity theory contributes a topic-native constructor role to the quantum construction.
- **Placement:** This page is read first as a context-setting move: it fixes the arena in which states, domains, and questions are legal.
- **Carrier or domain:** State terms: state vector. Context/domain terms: context.
- **Operator or map:** Operator terms: Hamiltonian, observable operator, or generator. Protocol or update terms: unitary evolution, projection or measurement update, or path integral weighting.
- **Admissibility:** Compatibility or closure terms: commutator, uncertainty relation, or non-commuting transformations. These determine which questions, states, or updates are legal.
- **Readout:** Readout terms: eigenvalue, energy level, or measurement outcome. These name the outcome labels, projectors, amplitudes, or records used for testing.
- **Check:** A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.

## Topic Equations

```math
B \longmapsto \rho_B \quad \text{(context specifies an admissible state)}
\rho_t = U_t \rho_B U_t^\dagger \quad \text{(unitary evolution from preparation to readout)}
O = \sum_i \lambda_i P_i,\quad p_i=\operatorname{Tr}(P_i\rho_t) \quad \text{(spectral probability measure)}
[O_1,O_2]\neq 0 \quad \text{(incompatible observables: no common sharp basis)}
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

## Validation Boundary

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823), score 0.520
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846), score 0.515
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640), score 0.499
- [arXiv:1605.07654](https://arxiv.org/abs/1605.07654), score 0.494
- [arXiv:0908.0752](https://arxiv.org/abs/0908.0752), score 0.492
- [arXiv:astro-ph0604157](https://arxiv.org/abs/astro-ph/0604157), score 0.490
