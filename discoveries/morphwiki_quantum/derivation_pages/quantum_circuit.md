# Quantum circuit

**Derivation step:** Protocol layer: engineered transformations

## Topic Context

In quantum information theory, a quantum circuit is a model for quantum computation, similar to classical circuits, in which a computation is a sequence of quantum gates, measurements, initializations of qubits to known values, and possibly other actions. The minimum set of actions that a circuit needs to be able to perform on the qubits to enable quantum computation is known as DiVincenzo's criteria.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_circuit)

## Role In The Derivation

Quantum circuit is the engineered-composition constructor: a finite sequence of admissible maps prepares, transforms, and measures a register.

## Why This Step Is Needed

Quantum circuit specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

## Mechanism

A circuit is the protocol layer of the same state-operator-observable machinery. Gates are controlled unitary or channel maps; measurement converts final states into output probabilities.

## How It Enters The Theory

**Place in the construction.** Quantum circuit contributes an engineered operation-sequence role to the quantum construction. This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.

**State and operation.** An input state, register, channel state, error syndrome, key, or controlled experimental configuration. An ordered sequence of gates, channels, measurements, corrections, encodings, or conditional maps.

**Admissibility and prediction.** Each step must belong to the claimed map class: unitary, completely positive, trace-preserving, projective, conditional, or corrective. Output state, key, error rate, fidelity, channel capacity, algorithmic success probability, or sensor estimate.

## Topic Equations

Standard constructor skeleton: composed gates and final measurement.

```math
\rho_{\mathrm{out}}=U_m\cdots U_2U_1\,\rho_{\mathrm{in}}\,U_1^\dagger U_2^\dagger\cdots U_m^\dagger
p(y)=\operatorname{Tr}(M_y\rho_{\mathrm{out}})
```

## How To Read The Relation

Read the composition from the prepared input toward the final state. Every intermediate map must preserve the mathematical conditions claimed for it, and conditional operations must be tied to explicit measurement outcomes. Performance is assessed through fidelity, error rate, capacity, precision, or success probability.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:0805.4565](https://arxiv.org/abs/0805.4565)
