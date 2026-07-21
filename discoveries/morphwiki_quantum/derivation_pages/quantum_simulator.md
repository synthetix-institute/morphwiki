# Quantum simulator

**Derivation step:** State carrier inside Hilbert space
**Status:** topic-specific mechanism

## Role In The Derivation

Quantum simulator is a target--carrier--validation construction: a controllable physical system encodes another model, and selected observables test whether the encoded dynamics is faithful.

## Mechanism

The simulator Hamiltonian is not by itself the target theory. The claim also needs an encoding between target and device states, a correspondence between their generators or channels, and validation observables with an error budget over the stated time and parameter range. The linked equation set is concentrated in operator-to-spectrum readout, state evolution, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Quantum simulator contributes an unresolved constructor role to the quantum construction.
- **Placement:** This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.
- **Carrier or domain:** A controllable device state space together with an explicit encoding of the target state space.
- **Operator or map:** Device Hamiltonians, channels, or gate sequences intended to reproduce target dynamics under the encoding.
- **Admissibility:** Control errors, leakage, finite size, noise, and approximation order define the regime in which the correspondence is claimed.
- **Readout:** Encoded target observables compared with independently predicted or calibrated device measurements.
- **Check:** Validation requires observables and error bounds beyond agreement with the programmed control Hamiltonian.

## Topic Equations

Topic-specific constructor: encoding, dynamical correspondence, and observable validation are separate obligations.

```math
V:\mathcal H_{\mathrm{target}}\hookrightarrow\mathcal H_{\mathrm{device}}
\left\|U_{\mathrm{device}}(t)V-VU_{\mathrm{target}}(t)\right\|\le\varepsilon(t)
\left|\langle O\rangle_{\mathrm{target}}-\langle VO V^{\dagger}\rangle_{\mathrm{device}}\right|\le\delta_O
```

## What Remains Stable

- the rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation
- the operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels
- the dependence of admissible readout on measurement context or boundary condition
- the non-commuting compatibility structure, which survives changes of representation

## What Changes With Realization

- the name of the carrier: particle, wave, field, qubit, or excitation
- where time dependence is represented: on the state, on the operator, or in a path weight
- the coordinate system, basis, or geometric picture used to display the same relation
- the physical implementation of detector, boundary, preparation, or readout

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical readout, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible readout while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
