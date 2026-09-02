# Quantum sensor

**Physical domain:** Control sequences and quantum channels

## Mechanism

Quantum sensor belongs to the protocol layer: it packages the quantum constructor into engineered sequences of admissible transformations and observables.

Quantum sensor specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate.

## Physical Construction

The state carrier is a probe state, sample state, field mode, detector state, or estimation register. The governing operation is an interaction Hamiltonian, transfer map, measurement channel, reconstruction map, or estimator. The instrument must separate sample signal from preparation, detector response, calibration, noise, and reconstruction artifacts. The calculated observables are Counts, images, spectra, phase shifts, trajectories, intensity maps, correlation data, or parameter estimates.

## Representative Relation

```math
\rho_{\rm probe}\mapsto \mathcal E_{\rm sample}(\rho_{\rm probe}),\quad p(y)=\operatorname{Tr}(M_y\mathcal E_{\rm sample}(\rho_{\rm probe})),\quad \hat s=R(\{y_i\})
```

## Physical Meaning

The ordered composition carries a prepared input to a final state. Every intermediate map must preserve its stated physical conditions, and conditional operations are tied to explicit measurement outcomes. Performance is quantified through fidelity, error rate, capacity, precision, or success probability.

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Invariance And Realization

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate. Quantum sensor turns the quantum constructor into an ordered operation sequence. The stable role is compositional: admissible maps transform an input state into an output state before measurement. Unitary gates, channels, measurements, correction steps, and algorithms are protocolized versions of the same state-map-observable logic.

The local title, representation, and physical realization may change while the constructor role is preserved. The implementation can be a circuit, channel, network, sensor, automaton, or cryptographic protocol. Noise, measurement timing, and correction rules change the realized map. Different hardware can implement the same abstract sequence of completely positive or unitary operations.

## Discriminating Consequences

The topic is physically defined by its state carrier, operator or map, observable consequence, and compatibility condition. Each operation in the sequence is constrained by the map class it claims: unitary, completely positive, trace preserving, measurement, correction, or conditional update. The composed protocol is defined by its output state and outcome probabilities, not only by the names of the gates.
