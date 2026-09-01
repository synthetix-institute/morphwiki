# Measurement in quantum mechanics

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Measurement in quantum mechanics is the complete measurement junction: it combines a state, a measurement model, probabilities, and sometimes an update rule.

Measurement theory must describe both an outcome distribution and the physical operation that produces a record. Keeping these roles separate prevents an interpretive account of state change from being mistaken for the probability law itself.

Measurement is not the root of quantum theory in this book. It is the junction where a prepared state and an observable or POVM are converted into probabilities and recorded outcomes.

## Physical Construction

The state carrier is a state vector or density operator together with the measurement context in which outcome channels are defined. The governing operation is a projection-valued measure, POVM, update map, or instrument map connecting state to record. Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. The calculated observables are Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

Standard constructor skeleton: generalized measurement probability and conditional update.

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

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
