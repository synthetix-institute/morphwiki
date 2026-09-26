# Quantum circuit

**Physical domain:** Control sequences and quantum channels

## Mechanism

Quantum circuit is the engineered-composition constructor: a finite sequence of admissible maps prepares, transforms, and measures a register.

A protocol is an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

A circuit is the protocol layer of the same state-operator-observable machinery. Gates are controlled unitary or channel maps; measurement converts final states into output probabilities.

## Physical Construction

The state carrier is an input state, register, channel state, error syndrome, key, or controlled experimental configuration. The calculation involves an ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps. Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective. The calculated quantities include output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.

## Topic Equations

```math
\rho_{\mathrm{out}}=U_m\cdots U_2U_1\,\rho_{\mathrm{in}}\,U_1^\dagger U_2^\dagger\cdots U_m^\dagger
p(y)=\operatorname{Tr}(M_y\rho_{\mathrm{out}})
```

## Physical Meaning

The ordered composition carries a prepared input to a final state. Every intermediate map must preserve its stated physical conditions, and conditional operations are tied to explicit measurement outcomes. Performance is quantified through fidelity, error rate, capacity, precision, or success probability.

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

Each operation in the sequence is constrained by the map class it claims: unitary, completely positive, trace preserving, measurement, correction, or conditional update. The composed protocol is defined by its output state and outcome probabilities, not only by the names of the gates. Changing operation order or replacing a quantum channel with a classical control identifies which part of the protocol carries the effect.
