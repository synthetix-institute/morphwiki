# Quantum complexity theory

**Derivation step:** Protocol layer: engineered transformations

## Topic Context

Quantum complexity theory is the subfield of computational complexity theory that deals with complexity classes defined using quantum computers, a computational model based on quantum mechanics. It studies the hardness of computational problems in relation to these complexity classes, as well as the relationship between quantum complexity classes and classical complexity classes.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_complexity_theory)

## Role In The Derivation

Quantum complexity theory belongs to the protocol layer: it packages the quantum constructor into engineered sequences of admissible transformations and observables.

## Why This Step Is Needed

Quantum complexity theory specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

## Mechanism

This step composes admissible transformations into a circuit, channel, control sequence, sensor, or algorithm.

## How It Enters The Theory

**Place in the construction.** Quantum complexity theory contributes an engineered transformation role to the quantum construction. This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.

**State and operation.** An input state, register, encoded subspace, channel state, key, syndrome, or controlled experimental configuration. An ordered sequence of gates, channels, measurements, encodings, corrections, or feedback maps.

**Admissibility and prediction.** Each step must belong to the claimed map class and the composition must preserve normalization and positivity. Output state, fidelity, error rate, key rate, channel capacity, algorithmic success probability, or sensor estimate.

## Representative Relation

```math
\rho_{\rm out}=\mathcal E_n\circ\cdots\circ\mathcal E_1(\rho_{\rm in}),\quad \mathcal E(\rho)=\sum_aK_a\rho K_a^\dagger
```

## How To Read The Relation

Read the composition from the prepared input toward the final state. Every intermediate map must preserve the mathematical conditions claimed for it, and conditional operations must be tied to explicit measurement outcomes. Performance is assessed through fidelity, error rate, capacity, precision, or success probability.

## What Remains Stable

Quantum complexity theory turns the quantum constructor into an ordered operation sequence. The stable role is compositional: admissible maps transform an input state into an output state before measurement. Unitary gates, channels, measurements, correction steps, and algorithms are protocolized versions of the same state-map-observable logic.

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
- [arXiv:1706.03846](https://arxiv.org/abs/1706.03846)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:1605.07654](https://arxiv.org/abs/1605.07654)
- [arXiv:0908.0752](https://arxiv.org/abs/0908.0752)
- [arXiv:astro-ph0604157](https://arxiv.org/abs/astro-ph/0604157)
