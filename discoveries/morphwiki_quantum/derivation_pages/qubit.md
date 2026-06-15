# Qubit

**Derivation step:** State carrier inside Hilbert space
**Status:** topic-specific mechanism
**Dominant evidence signal:** observables and spectra

## Role In The Derivation

Qubit is the two-dimensional state-carrier constructor used when the admissible state space is \(\mathbb C^2\).

## Mechanism

A qubit is the minimal quantum state space with a basis, amplitudes, unitary control, and measurement readout. Bloch-vector language is a representation of the same two-dimensional carrier. In the Hyperion profile for this page, the strongest route evidence is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier evidence is local notation, information profile, formula structure.

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

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385), score 0.577; A11[O00 + O12 + O14]
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283), score 0.522; A11[O00 + O12 + O14]
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682), score 0.519; A03[O14 + O16 + O05]
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159), score 0.511; A08[O13 + O19 + O21]
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598), score 0.511; A05[O17 + O11 + O14]
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537), score 0.505; A11[O00 + O12 + O14]
