# Quantum imaging

**Physical domain:** Measurement, instruments, and probabilities

## Mechanism

Quantum imaging belongs to the measurement step: it connects a prepared state and an operator spectrum to probabilities or state updates.

Quantum imaging connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate.

## Physical Construction

The state carrier is a probe state, sample state, field mode, detector state, or estimation register. The governing operation is an interaction Hamiltonian, transfer map, measurement channel, reconstruction map, or estimator. The instrument must separate sample signal from preparation, detector response, calibration, noise, and reconstruction artifacts. The calculated observables are Counts, images, spectra, phase shifts, trajectories, intensity maps, correlation data, or parameter estimates.

## Representative Relation

```math
\rho_{\rm probe}\mapsto \mathcal E_{\rm sample}(\rho_{\rm probe}),\quad p(y)=\operatorname{Tr}(M_y\mathcal E_{\rm sample}(\rho_{\rm probe})),\quad \hat s=R(\{y_i\})
```

## Physical Meaning

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Invariance And Realization

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate. Quantum imaging connects the state and the spectral question to observed probabilities. The invariant step is the map from state plus measurement operators to a normalized probability distribution. Projection-valued and POVM observables preserve the same role: outcome channels weighted by the state.

The local title, representation, and physical realization may change while the constructor role is preserved. The detector model, basis, and update convention can change. State-vector, density-matrix, projective, and generalized-measurement forms may present the observable differently. Interpretive language about collapse or information update can vary without changing the probability rule.

## Discriminating Consequences

The topic is physically defined by its state carrier, operator or map, observable consequence, and compatibility condition. Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family. Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors.
