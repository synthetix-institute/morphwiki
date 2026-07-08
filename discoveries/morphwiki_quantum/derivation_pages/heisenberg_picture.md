# Heisenberg picture

**Derivation step:** Generator: lawful change before readout
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

The heisenberg picture can be read as a quantum construction: the potential, domain, initial condition, or boundary condition fixes the admissible state space; the Hamiltonian, whose exponential gives unitary time evolution defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## Mechanism

In quantum-mechanical terms, the Heisenberg picture is described by a wave function or density operator defined on the Hilbert space allowed by the system's domain. The physical question is represented by the Hamiltonian, whose exponential gives unitary time evolution; the experimental or mathematical setting is the potential, domain, initial condition, or boundary condition. The observable content is obtained from the eigenvalues and eigenfunctions of the relevant observable. In the local terminology of this topic, the same construction appears through quantum state or wave function, Hamiltonian or observable operator, and eigenvalue or energy level. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through commutator or non-commuting observables. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Heisenberg picture contributes a topic-native constructor role to the quantum construction.
- **Placement:** This page is read first as a lawful-transport move: it identifies what changes the state before readout.
- **Carrier or domain:** State terms: quantum state. Context/domain terms: basis.
- **Operator or map:** Operator terms: Hamiltonian, observable, or commutator. Protocol or update terms: unitary evolution, projection or measurement update, or path integral weighting.
- **Admissibility:** Compatibility or closure terms: commutator. These determine which questions, states, or updates are legal.
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

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537), score 0.485
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682), score 0.443
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838), score 0.442
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823), score 0.436
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283), score 0.436
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159), score 0.415
