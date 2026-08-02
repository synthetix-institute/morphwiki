# Quantum simulator

**Derivation step:** State carrier inside Hilbert space

## Topic Context

Quantum simulators permit the study of a quantum system in a programmable fashion. In this instance, simulators are special purpose devices designed to provide insight about specific physics problems. Quantum simulators may be contrasted with generally programmable "digital" quantum computers, which would be capable of solving a wider class of quantum problems.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_simulator)

## Role In The Derivation

Quantum simulator is a target--carrier--validation construction: a controllable physical system encodes another model, and selected observables test whether the encoded dynamics is faithful.

## Why This Step Is Needed

Quantum simulator specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

## Mechanism

The simulator Hamiltonian is not by itself the target theory. The claim also needs an encoding between target and device states, a correspondence between their generators or channels, and validation observables with an error budget over the stated time and parameter range.

## How It Enters The Theory

**Place in the construction.** Quantum simulator contributes a state or sector role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** A controllable device state space together with an explicit encoding of the target state space. Device Hamiltonians, channels, or gate sequences intended to reproduce target dynamics under the encoding.

**Admissibility and prediction.** Control errors, leakage, finite size, noise, and approximation order define the regime in which the correspondence is claimed. Encoded target observables compared with independently predicted or calibrated device measurements.

## Topic Equations

Topic-specific constructor: encoding, dynamical correspondence, and observable validation are separate obligations.

```math
V:\mathcal H_{\mathrm{target}}\hookrightarrow\mathcal H_{\mathrm{device}}
\left\|U_{\mathrm{device}}(t)V-VU_{\mathrm{target}}(t)\right\|\le\varepsilon(t)
\left|\langle O\rangle_{\mathrm{target}}-\langle VO V^{\dagger}\rangle_{\mathrm{device}}\right|\le\delta_O
```

## How To Read The Relation

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

With the state identified, the next question is how it changes. The generator chapter supplies that lawful transformation; the observable and measurement chapters then turn the transformed state into a prediction.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
