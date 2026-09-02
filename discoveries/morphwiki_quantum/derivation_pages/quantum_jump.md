# Quantum jump

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Quantum jump belongs to the measurement step: it connects a prepared state and an operator spectrum to probabilities or state updates.

Quantum jump connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

A measurement couples a prepared state to recorded outcomes and, when conditioning is retained, to the resulting state change.

## Physical Construction

The state carrier is a prepared state together with the measurement context and any apparatus degrees of freedom retained in the model. The governing operation is a projection-valued measure, POVM, quantum instrument, or detector interaction. Outcome probabilities are positive and normalized; conditional state changes must define completely positive maps. The calculated observables are Outcome probabilities, detector records, ensemble frequencies, and conditional post-measurement states.

## Representative Relation

```math
p(y)=\operatorname{Tr}(\rho E_y),\quad E_y\ge0,\quad \sum_yE_y=I
```

## Physical Meaning

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Invariance And Realization

Quantum jump connects the state and the spectral question to observed probabilities. The invariant step is the map from state plus measurement operators to a normalized probability distribution. Projection-valued and POVM observables preserve the same role: outcome channels weighted by the state.

The local title, representation, and physical realization may change while the constructor role is preserved. The detector model, basis, and update convention can change. State-vector, density-matrix, projective, and generalized-measurement forms may present the observable differently. Interpretive language about collapse or information update can vary without changing the probability rule.

## Discriminating Consequences

The topic is physically defined by its state carrier, operator or map, observable consequence, and compatibility condition. Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family. Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors.
