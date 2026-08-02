# Measurement problem

**Derivation step:** Measurement rule: how observables become probabilities

## Topic Context

In quantum mechanics, the measurement problem is the problem of definite outcomes: quantum systems have superpositions but quantum measurements only give one definite result.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Measurement_problem)

## Role In The Derivation

Measurement problem is the junction between unitary system--apparatus coupling, probability assignment, and conditional state update; these are distinct maps and need not be identified.

## Why This Step Is Needed

Measurement problem connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

## Mechanism

A measurement model first couples the system to an apparatus or environment. A POVM or instrument then assigns outcome probabilities, and a conditional map specifies the post-record state. The foundational problem concerns the relation between these operations and a definite record, not the absence of a probability formula.

## How It Enters The Theory

**Place in the construction.** Measurement problem contributes a probability/observable role to the quantum construction. This page is read first as a measurement move: it connects the state and observable to outcome probabilities.

**State and operation.** A joint system--apparatus state, possibly enlarged by environmental degrees of freedom. A premeasurement interaction followed by a measurement instrument whose components label possible records.

**Admissibility and prediction.** The instrument maps are completely positive and their sum is trace preserving; the outcome effects sum to the identity. Outcome probabilities and conditional post-record states must be stated separately.

## Topic Equations

Topic-specific constructor: premeasurement coupling, outcome probability, conditional update, and unconditioned evolution are separated.

```math
\rho_{SA}'=U_{SA}(\rho_S\otimes\rho_A)U_{SA}^{\dagger}
p(i)=\operatorname{Tr}[\mathcal I_i(\rho_S)]=\operatorname{Tr}(\rho_SE_i)
\rho_{S|i}=\frac{\mathcal I_i(\rho_S)}{p(i)},\qquad \rho_S'=\sum_i\mathcal I_i(\rho_S)
```

## How To Read The Relation

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
- [arXiv:2501.07524](https://arxiv.org/abs/2501.07524)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
