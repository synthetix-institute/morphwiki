# Measurement in quantum mechanics

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Measurement in quantum mechanics is the complete measurement junction: it combines a state, a measurement model, probabilities, and sometimes an update rule.

Measurement theory must describe both an outcome distribution and the physical operation that produces a record. Keeping these roles separate prevents an interpretive account of state change from being mistaken for the probability law itself.

Measurement is not the root of quantum theory in this book. It is the junction where a prepared state and an observable or POVM are converted into probabilities and recorded outcomes.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The calculation involves a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated quantities include Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

```math
p(i)=\operatorname{Tr}(\rho E_i)
\rho\mapsto \rho_i=\frac{K_i\rho K_i^\dagger}{\operatorname{Tr}(K_i\rho K_i^\dagger)}
E_i=K_i^\dagger K_i
```

## Physical Meaning

A POVM gives outcome probabilities, whereas a quantum instrument gives the corresponding conditional transformations. Projective measurement is an ideal sharp limit. Real detectors are calibrated by showing that their effects are positive, complete, and consistent with observed frequencies.

A photon counter may report click or no click with non-unit efficiency. A two-effect POVM models those probabilities; the associated instrument is needed only when the state after the event matters.

The incompatibility chapter asks which families of such measurements can be jointly realized or assigned simultaneous sharp values.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family. Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors. The probability assignment is distinct from any optional post-measurement update convention.
