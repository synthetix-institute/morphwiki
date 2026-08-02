# Measurement in quantum mechanics

**Derivation step:** Measurement rule: how observables become probabilities

## Topic Context

In quantum physics, a measurement is the testing or manipulation of a physical system to yield a numerical result. A fundamental feature of quantum theory is that the predictions it makes are probabilistic.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Measurement_in_quantum_mechanics)

## Role In The Derivation

Measurement in quantum mechanics is the complete measurement junction: it combines a state, a measurement model, probabilities, and sometimes an update rule.

## Why This Step Is Needed

Measurement theory must describe both an outcome distribution and the physical operation that produces a record. Keeping these roles separate prevents an interpretive account of state change from being mistaken for the probability law itself.

## Mechanism

Measurement is not the root of quantum theory in this book. It is the junction where a prepared state and an observable or POVM are converted into probabilities and recorded outcomes.

## How It Enters The Theory

**Place in the construction.** Measurement in quantum mechanics contributes a probability/observable role to the quantum construction. This page is read first as a measurement move: it connects the state and observable to outcome probabilities.

**State and operation.** A state vector or density operator together with the measurement context in which outcome channels are defined. A projection-valued measure, POVM, update map, or instrument map connecting state to record.

**Admissibility and prediction.** Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Topic Equations

Standard constructor skeleton: generalized measurement probability and conditional update.

```math
p(i)=\operatorname{Tr}(\rho E_i)
\rho\mapsto \rho_i=\frac{K_i\rho K_i^\dagger}{\operatorname{Tr}(K_i\rho K_i^\dagger)}
E_i=K_i^\dagger K_i
```

## How To Read The Relation

A POVM gives outcome probabilities, whereas a quantum instrument gives the corresponding conditional transformations. Projective measurement is an ideal sharp limit. Real detectors are calibrated by showing that their effects are positive, complete, and consistent with observed frequencies.

## Worked Example

A photon counter may report click or no click with non-unit efficiency. A two-effect POVM models those probabilities; the associated instrument is needed only when the state after the event matters.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

The incompatibility chapter asks which families of such measurements can be jointly realized or assigned simultaneous sharp values.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
