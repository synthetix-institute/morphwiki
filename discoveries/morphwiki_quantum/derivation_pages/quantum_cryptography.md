# Quantum cryptography

**Derivation step:** Protocol layer: engineered transformations

## Topic Context

Quantum cryptography is the science of exploiting quantum mechanical properties such as quantum entanglement, measurement disturbance, no-cloning theorem, and the principle of superposition to perform various cryptographic tasks. Historically defined as the practice of encoding messages, a concept since referred to as encryption, quantum cryptography plays a crucial role in the secure processing, storage, and transmission of information across various domains.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_cryptography)

## Role In The Derivation

Quantum cryptography belongs to the protocol layer: it packages the quantum constructor into engineered sequences of admissible transformations and observables.

## Why This Step Is Needed

Quantum cryptography specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

## Mechanism

The mechanism is a controlled composition of allowed maps: a sequence that prepares, transforms, protects, transmits, or reads a quantum state.

## How It Enters The Theory

**Place in the construction.** Quantum cryptography contributes an engineered operation-sequence role to the quantum construction. This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.

**State and operation.** An input state, register, channel state, error syndrome, key, or controlled experimental configuration. An ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps.

**Admissibility and prediction.** Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective. Output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.

## Representative Relation

```math
\rho_{\rm out}=\mathcal E_n\circ\cdots\circ\mathcal E_1(\rho_{\rm in}),\quad \mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger
```

## How To Read The Relation

Read the composition from the prepared input toward the final state. Every intermediate map must preserve the mathematical conditions claimed for it, and conditional operations must be tied to explicit measurement outcomes. Performance is assessed through fidelity, error rate, capacity, precision, or success probability.

## What Remains Stable

The mechanism is a controlled composition of allowed maps: a sequence that prepares, transforms, protects, transmits, or reads a quantum state. Quantum cryptography turns the quantum constructor into an ordered operation sequence. The stable role is compositional: admissible maps transform an input state into an output state before measurement. Unitary gates, channels, measurements, correction steps, and algorithms are protocolized versions of the same state-map-observable logic.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The implementation can be a circuit, channel, network, sensor, automaton, or cryptographic protocol. Noise, measurement timing, and correction rules change the realized map. Different hardware can implement the same abstract sequence of completely positive or unitary operations.

## Connection To The Next Step

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Each operation in the sequence is constrained by the map class it claims: unitary, completely positive, trace preserving, measurement, correction, or conditional update.
- The composed protocol is defined by its output state and outcome probabilities, not only by the names of the gates.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
