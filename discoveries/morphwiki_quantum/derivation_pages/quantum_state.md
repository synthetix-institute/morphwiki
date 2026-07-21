# Quantum state

**Derivation step:** State carrier inside Hilbert space
**Status:** topic-specific mechanism

## Role In The Derivation

A quantum state can be read as a quantum construction: the potential, domain, initial condition, or boundary condition fixes the admissible state space; the Hamiltonian, whose exponential gives unitary time evolution defines the transformation or question; and spectral projectors with the Born rule determine the recorded probability distribution.

## Mechanism

In quantum-mechanical terms, a quantum state is described by a wave function or density operator defined on the Hilbert space allowed by the system's domain. The physical question is represented by the Hamiltonian, whose exponential gives unitary time evolution; the experimental or mathematical setting is the potential, domain, initial condition, or boundary condition. The observable content is obtained from the eigenvalues and eigenfunctions of the relevant observable. In the local terminology of this topic, the same construction appears through Quantum state or wave function, observable operator or matrix, and eigenstate or spectrum. Probabilities enter only after this spectral decomposition: the Born rule assigns weights to projectors, not to informal object names. When two observables have a non-zero commutator, no single basis diagonalizes both; the limitation is therefore a statement about jointly available spectra, not about detector imperfection. In this page the compatibility condition is expressed through uncertainty relation or incompatible observables. The linked equation set is concentrated in state evolution, operator-to-spectrum readout, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum state contributes a state-carrier role to the quantum construction.
- **Placement:** This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.
- **Carrier or domain:** State terms: Quantum state, wave function, or superposition. Context/domain terms: detector and preparation.
- **Operator or map:** Operator terms: observable and matrix. Protocol or update terms: unitary evolution, projection or measurement update, or path integral weighting.
- **Admissibility:** Compatibility or closure terms: uncertainty and incompatible. These determine which questions, states, or updates are legal.
- **Readout:** Readout terms: eigenstate, spectrum, or eigenvalue. These name the outcome labels, projectors, amplitudes, or records used for testing.
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

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
