# Path integral

**Derivation step:** Generator: lawful change before readout
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Path integral is an alternate generator constructor: transition amplitudes are obtained by summing phase weights over histories.

## Mechanism

The path integral does not replace the operator constructor. It repackages the generator step as a weighted sum over histories between boundary conditions. It is especially useful when action, symmetry, and field degrees of freedom are more natural than state-vector evolution. In the Hyperion profile for this page, the strongest route evidence is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier evidence is local notation, information profile, formula structure.

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

- [arXiv:2107.01923](https://arxiv.org/abs/2107.01923), score 0.313; A03[O06 + O16 + O14]
- [arXiv:0801.3568](https://arxiv.org/abs/0801.3568), score 0.272; A07[O14 + O02 + O07]
- [arXiv:2105.11733](https://arxiv.org/abs/2105.11733), score 0.271; A00[O08 + O15 + O14]
- [arXiv:1706.07300](https://arxiv.org/abs/1706.07300), score 0.264; A03[O14 + O16 + O07]
- [arXiv:cond-mat0108470](https://arxiv.org/abs/cond-mat/0108470), score 0.263; A03[O14 + O16 + O03]
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846), score 0.262; A10[O10 + O09 + O04]
