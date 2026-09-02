# Quantum simulator

**Physical domain:** Control sequences and quantum channels

## Mechanism

Quantum simulator is a target--carrier--validation construction: a controllable physical system encodes another model, and selected observables test whether the encoded dynamics is faithful.

Quantum simulator specifies an ordered sequence of operations. Order is physical whenever the maps do not commute, so a list of available gates or channels is insufficient to define an algorithm, sensor, communication scheme, or correction cycle.

The simulator Hamiltonian is not by itself the target theory. The claim also needs an encoding between target and device states, a correspondence between their generators or channels, and validation observables with an error budget over the stated time and parameter range.

## Physical Construction

The state carrier is a controllable device state space together with an explicit encoding of the target state space. The governing operation is Device Hamiltonians, channels, or gate sequences intended to reproduce target dynamics under the encoding. Control errors, leakage, finite size, noise, and approximation order define the regime in which the correspondence is claimed. The calculated observables are Encoded target observables compared with independently predicted or calibrated device measurements.

## Topic Equations

Topic-specific constructor: encoding, dynamical correspondence, and observable validation are separate obligations.

```math
V:\mathcal H_{\mathrm{target}}\hookrightarrow\mathcal H_{\mathrm{device}}
\left\|U_{\mathrm{device}}(t)V-VU_{\mathrm{target}}(t)\right\|\le\varepsilon(t)
\left|\langle O\rangle_{\mathrm{target}}-\langle VO V^{\dagger}\rangle_{\mathrm{device}}\right|\le\delta_O
```

## Physical Meaning

The ordered composition carries a prepared input to a final state. Every intermediate map must preserve its stated physical conditions, and conditional operations are tied to explicit measurement outcomes. Performance is quantified through fidelity, error rate, capacity, precision, or success probability.

This is the executable end of the mechanism tree. It also closes the loop: failed predictions can be traced backward to the operation order, the generator, the state preparation, or the mathematical domain rather than attributed to the topic as a whole.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.
