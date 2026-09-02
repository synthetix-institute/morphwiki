# Measurement problem

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Measurement problem is the junction between unitary system--apparatus coupling, probability assignment, and conditional state update; these are distinct maps and need not be identified.

Measurement problem connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

A measurement model first couples the system to an apparatus or environment. A POVM or instrument then assigns outcome probabilities, and a conditional map specifies the post-record state. The foundational problem concerns the relation between these operations and a definite record, not the absence of a probability formula.

## Physical Construction

The state carrier is a joint system--apparatus state, possibly enlarged by environmental degrees of freedom. The governing operation is a premeasurement interaction followed by a measurement instrument whose components label possible records. The instrument maps are completely positive and their sum is trace preserving; the outcome effects sum to the identity. The calculated observables are Outcome probabilities and conditional post-record states must be stated separately.

## Topic Equations

Topic-specific constructor: premeasurement coupling, outcome probability, conditional update, and unconditioned evolution are separated.

```math
\rho_{SA}'=U_{SA}(\rho_S\otimes\rho_A)U_{SA}^{\dagger}
p(i)=\operatorname{Tr}[\mathcal I_i(\rho_S)]=\operatorname{Tr}(\rho_SE_i)
\rho_{S|i}=\frac{\mathcal I_i(\rho_S)}{p(i)},\qquad \rho_S'=\sum_i\mathcal I_i(\rho_S)
```

## Physical Meaning

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:quant-ph/0612224](https://arxiv.org/abs/quant-ph/0612224)
- [arXiv:quant-ph0612224](https://arxiv.org/abs/quant-ph0612224)
- [arXiv:2203.16157](https://arxiv.org/abs/2203.16157)
- [arXiv:2112.10133](https://arxiv.org/abs/2112.10133)
