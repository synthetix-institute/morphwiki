# Quantum information science

**Physical domain:** Control sequences and quantum channels

*Physical-role overview. The representative relation below is shared with other topics in this chapter.*

## Mechanism

Quantum information science is placed at the protocol layer, where the quantum constructor is assembled into engineered sequences of admissible transformations and measurements.

A protocol is an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

Circuits, controls, and sensing sequences are ordered compositions of physical transformations and measurements.

## Physical Construction

The state carrier is an input state, register, encoded subspace, channel state, key, syndrome, or controlled experimental configuration. The calculation involves an ordered sequence of gates, channels, measurements, encodings, corrections, or feedback maps. Each step must belong to the claimed map class and the composition must preserve normalization and positivity. The calculated quantities include output state, fidelity, error rate, key rate, channel capacity, algorithmic success probability, or sensor estimate.

## Representative Relation

```math
\rho_{\rm out}=\mathcal E_n\circ\cdots\circ\mathcal E_1(\rho_{\rm in}),\quad \mathcal E(\rho)=\sum_aK_a\rho K_a^\dagger
```

## Physical Meaning

The ordered composition carries a prepared input to a final state. Every intermediate map must preserve its stated physical conditions, and conditional operations are tied to explicit measurement outcomes. Performance is quantified through fidelity, error rate, capacity, precision, or success probability.

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Invariance And Realization

A protocol turns the quantum constructor into an ordered operation sequence. The stable role is compositional: admissible maps transform an input state into an output state before measurement. Unitary gates, channels, measurements, correction steps, and algorithms are protocolized versions of the same state-map-observable logic.

The local title, representation, and physical realization may change while the constructor role is preserved. The implementation can be a circuit, channel, network, sensor, automaton, or cryptographic protocol. Noise, measurement timing, and correction rules change the realized map. Different hardware can implement the same abstract sequence of completely positive or unitary operations.

## Discriminating Consequences

The topic is physically defined by its state carrier, operator or map, observable consequence, and compatibility condition. Each operation in the sequence is constrained by the map class it claims: unitary, completely positive, trace preserving, measurement, correction, or conditional update. The composed protocol is defined by its output state and outcome probabilities, not only by the names of the gates.
