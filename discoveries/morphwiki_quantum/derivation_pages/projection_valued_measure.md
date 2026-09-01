# Projection-valued measure

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Projection-valued measure is the sharp-observable constructor: mutually exclusive outcome projectors partition the identity.

Projection-valued measure connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

A projection-valued measure encodes an ideal sharp measurement. It defines outcome channels that are orthogonal and exhaustive.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The governing operation is a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated observables are Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

Standard constructor skeleton: sharp outcome channels, probability, and projective update.

```math
P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=I
p(i)=\operatorname{Tr}(\rho P_i)
\rho\mapsto \frac{P_i\rho P_i}{\operatorname{Tr}(\rho P_i)}
```

## Physical Meaning

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
