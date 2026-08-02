# Quantum jump

**Derivation step:** Measurement rule: how observables become probabilities

## Topic Context

A quantum jump is the abrupt transition of a quantum system from one quantum state to another, from one energy level to another. When the system absorbs energy, there is a transition to a higher energy level (excitation); when the system loses energy, there is a transition to a lower energy level.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_jump)

## Role In The Derivation

Quantum jump belongs to the measurement step: it connects a prepared state and an operator spectrum to probabilities or state updates.

## Why This Step Is Needed

Quantum jump connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

## Mechanism

This step connects a prepared state and a measurement to outcome probabilities and, when required, conditional state change.

## How It Enters The Theory

**Place in the construction.** Quantum jump contributes a probability and measurement role to the quantum construction. This page is read first as a measurement move: it connects the state and observable to outcome probabilities.

**State and operation.** A prepared state together with the measurement context and any apparatus degrees of freedom retained in the model. A projection-valued measure, POVM, quantum instrument, or detector interaction.

**Admissibility and prediction.** Outcome probabilities are positive and normalized; conditional state changes must define completely positive maps. Outcome probabilities, detector records, ensemble frequencies, and conditional post-measurement states.

## Representative Relation

```math
p(y)=\operatorname{Tr}(\rho E_y),\quad E_y\ge0,\quad \sum_yE_y=I
```

## How To Read The Relation

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

## What Remains Stable

Quantum jump connects the state and the spectral question to observed probabilities. The invariant step is the map from state plus measurement operators to a normalized probability distribution. Projection-valued and POVM observables preserve the same role: outcome channels weighted by the state.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The detector model, basis, and update convention can change. State-vector, density-matrix, projective, and generalized-measurement forms may present the observable differently. Interpretive language about collapse or information update can vary without changing the probability rule.

## Connection To The Next Step

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family.
- Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:0805.4565](https://arxiv.org/abs/0805.4565)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
