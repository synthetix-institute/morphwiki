# Born rule

**Derivation step:** Measurement rule: how observables become probabilities

## Topic Context

The Born rule is a postulate of quantum mechanics that gives the probability that a measurement of a quantum system will yield a given result. In one commonly used application, it states that the probability density for finding a particle at a given position is proportional to the square of the amplitude of the system's wavefunction at that position. It was formulated and published by German physicist Max Born in July 1926.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Born_rule)

## Role In The Derivation

Born rule is the probability-observable constructor: it maps a state and a spectral channel to an observed probability.

## Why This Step Is Needed

The Born rule is the bridge from complex amplitudes to experimentally testable probabilities. It is an additional postulate: linear state evolution alone does not say how often a detector outcome should occur.

## Mechanism

The Born rule is the point where the constructor becomes predictive. It does not name an object; it connects state preparation and a legal question to frequencies over outcome channels.

## How It Enters The Theory

**Place in the construction.** Born rule contributes a probability/observable role to the quantum construction. This page is read first as a measurement move: it connects the state and observable to outcome probabilities.

**State and operation.** A state vector or density operator together with the measurement context in which outcome channels are defined. A projection-valued measure, POVM, update map, or instrument map connecting state to record.

**Admissibility and prediction.** Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

Standard constructor skeleton: probability assignment for projective and position observables.

```math
p(i|\rho,\{P_i\})=\operatorname{Tr}(\rho P_i)
\Pr(X\in\Delta|\psi)=\int_\Delta|\psi(x)|^2\,d\mu(x)
\sum_i p(i)=1
```

## How To Read The Relation

For a sharp measurement, the probability of an outcome is the state weight in the corresponding eigenspace. The density-operator form extends the same rule to mixtures and generalized measurements. Completeness of the outcome operators makes the probabilities sum to one.

## Worked Example

A spin prepared equally between two vertical outcomes gives one-half for each vertical detector channel, even though each individual run records only one result.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Measurement theory adds detector coupling and conditional state change without altering this probability assignment.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
