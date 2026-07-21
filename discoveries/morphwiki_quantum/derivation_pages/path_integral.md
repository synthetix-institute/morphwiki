# Path integral

**Derivation step:** Generator: lawful change before readout
**Status:** topic-specific mechanism

## Role In The Derivation

Path integral is an alternate generator constructor: transition amplitudes are obtained by summing phase weights over histories.

## Mechanism

The path integral does not replace the operator constructor. It repackages the generator step as a weighted sum over histories between boundary conditions. It is especially useful when action, symmetry, and field degrees of freedom are more natural than state-vector evolution. The linked equation set is concentrated in operator-to-spectrum readout, state evolution, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Path integral contributes a lawful state-transport role to the quantum construction.
- **Placement:** This page is read first as a lawful-transport move: it identifies what changes the state before readout.
- **Carrier or domain:** A state vector, density operator, wavefunction, field state, or register on a specified domain.
- **Operator or map:** Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state.
- **Admissibility:** Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal.
- **Readout:** Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.
- **Check:** The generator must predict the observed evolution while preserving the relevant normalization, positivity, symmetry, or conservation constraint.

## Topic Equations

Standard constructor skeleton: boundary-to-boundary transition amplitude through action weights.

```math
K(x_f,t_f;x_i,t_i)=\int_{x_i}^{x_f}\mathcal D x(t)\,\exp\!\left(\frac{i}{\hbar}S[x]\right)
\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i
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

- [arXiv:2107.01923](https://arxiv.org/abs/2107.01923)
- [arXiv:0801.3568](https://arxiv.org/abs/0801.3568)
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733)
- [arXiv:1706.07300](https://arxiv.org/abs/1706.07300)
- [arXiv:cond-mat0108470](https://arxiv.org/abs/cond-mat/0108470)
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
