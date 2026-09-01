# Quantum circuit

**Physical domain:** Control sequences and quantum channels

## Mechanism

Quantum circuit is the engineered-composition constructor: a finite sequence of admissible maps prepares, transforms, and measures a register.

Quantum circuit specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

A circuit is the protocol layer of the same state-operator-observable machinery. Gates are controlled unitary or channel maps; measurement converts final states into output probabilities.

## Physical Construction

The state carrier is an input state, register, channel state, error syndrome, key, or controlled experimental configuration. The governing operation is an ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps. Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective. The calculated observables are Output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.

## Topic Equations

Standard constructor skeleton: composed gates and final measurement.

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

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
