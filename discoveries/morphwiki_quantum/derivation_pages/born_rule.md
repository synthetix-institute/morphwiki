# Born rule

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Born rule is the probability-observable constructor: it maps a state and a spectral channel to an observed probability.

The Born rule is the bridge from complex amplitudes to experimentally testable probabilities. It is an additional postulate: linear state evolution alone does not say how often a detector outcome should occur.

The Born rule is the point where the constructor becomes predictive. It does not name an object; it connects state preparation and a legal question to frequencies over outcome channels.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The governing operation is a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated observables are Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

Standard constructor skeleton: probability assignment for projective and position observables.

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

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:1003.5582](https://arxiv.org/abs/1003.5582)
- [arXiv:2212.14568](https://arxiv.org/abs/2212.14568)
- [arXiv:quant-ph/0703020](https://arxiv.org/abs/quant-ph/0703020)
- [arXiv:quant-ph0703020](https://arxiv.org/abs/quant-ph0703020)
