# Projection-valued measure

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Projection-valued measure is the sharp-observable constructor: mutually exclusive outcome projectors partition the identity.

The measurement rule connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

A projection-valued measure encodes an ideal sharp measurement. It defines outcome channels that are orthogonal and exhaustive.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The calculation involves a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated quantities include Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

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

Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family. Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors. The probability assignment is distinct from any optional post-measurement update convention.
