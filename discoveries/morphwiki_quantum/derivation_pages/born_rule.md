# Born rule

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Born rule is the probability-observable constructor: it maps a state and a spectral channel to an observed probability.

The Born rule is the bridge from complex amplitudes to experimentally testable probabilities. It is an additional postulate: linear state evolution alone does not say how often a detector outcome should occur.

The Born rule is the point where the constructor becomes predictive. It does not name an object; it connects state preparation and a legal question to frequencies over outcome channels.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The calculation involves a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated quantities include Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

```math
p(i|\rho,\{P_i\})=\operatorname{Tr}(\rho P_i)
\Pr(X\in\Delta|\psi)=\int_\Delta|\psi(x)|^2\,d\mu(x)
\sum_i p(i)=1
```

## Physical Meaning

For a sharp measurement, the probability of an outcome is the state weight in the corresponding eigenspace. The density-operator form extends the same rule to mixtures and generalized measurements. Completeness of the outcome operators makes the probabilities sum to one.

A spin prepared equally between two vertical outcomes gives one-half for each vertical detector channel, even though each individual run records only one result.

Measurement theory adds detector coupling and conditional state change without altering this probability assignment.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family. Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors. The probability assignment is distinct from any optional post-measurement update convention.
