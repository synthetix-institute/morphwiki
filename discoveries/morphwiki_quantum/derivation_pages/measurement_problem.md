# Measurement problem

**Derivation step:** Readout rule: how answers become probabilities
**Status:** topic-specific mechanism

## Role In The Derivation

Measurement problem is the junction between unitary system--apparatus coupling, probability readout, and conditional state update; these are distinct maps and need not be identified.

## Mechanism

A measurement model first couples the system to an apparatus or environment. A POVM or instrument then assigns outcome probabilities, and a conditional map specifies the post-record state. The foundational problem concerns the relation between these operations and a definite record, not the absence of a probability formula. The linked equation set is concentrated in state evolution, preparation, basis, or boundary context, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Measurement problem contributes a probability/readout role to the quantum construction.
- **Placement:** This page is read first as a readout move: it connects the state and question to recorded outcomes.
- **Carrier or domain:** A joint system--apparatus state, possibly enlarged by environmental degrees of freedom.
- **Operator or map:** A premeasurement interaction followed by a measurement instrument whose components label possible records.
- **Admissibility:** The instrument maps are completely positive and their sum is trace preserving; the outcome effects sum to the identity.
- **Readout:** Outcome probabilities and conditional post-record states must be stated separately.
- **Check:** A proposed resolution must identify where a definite record enters and how its prediction differs from the unconditioned state evolution.

## Topic Equations

Topic-specific constructor: premeasurement coupling, outcome probability, conditional update, and unconditioned evolution are separated.

```math
\rho_{SA}'=U_{SA}(\rho_S\otimes\rho_A)U_{SA}^{\dagger}
p(i)=\operatorname{Tr}[\mathcal I_i(\rho_S)]=\operatorname{Tr}(\rho_SE_i)
\rho_{S|i}=\frac{\mathcal I_i(\rho_S)}{p(i)},\qquad \rho_S'=\sum_i\mathcal I_i(\rho_S)
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
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
- [arXiv:2501.07524](https://arxiv.org/abs/2501.07524)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
