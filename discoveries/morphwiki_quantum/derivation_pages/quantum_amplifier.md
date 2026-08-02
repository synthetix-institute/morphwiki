# Quantum amplifier

**Derivation step:** Generator: lawful change before measurement

## Topic Context

In physics, a quantum amplifier is an amplifier that uses quantum mechanical methods to amplify a signal; examples include the active elements of lasers and optical amplifiers.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_amplifier)

## Role In The Derivation

Quantum amplifier belongs to the lawful-change step: it specifies how the state changes before a question is asked.

## Why This Step Is Needed

Quantum amplifier separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

## Mechanism

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate.

## How It Enters The Theory

**Place in the construction.** Quantum amplifier contributes an instrument-mediated observable role to the quantum construction. This page is read first as a lawful-transport move: it identifies what changes the state before measurement.

**State and operation.** A probe state, sample state, field mode, detector state, or estimation register. An interaction Hamiltonian, transfer map, measurement channel, reconstruction map, or estimator.

**Admissibility and prediction.** The instrument must separate sample signal from preparation, detector response, calibration, noise, and reconstruction artifacts. Counts, images, spectra, phase shifts, trajectories, intensity maps, correlation data, or parameter estimates.

## Representative Relation

```math
\rho_{\rm probe}\mapsto \mathcal E_{\rm sample}(\rho_{\rm probe}),\quad p(y)=\operatorname{Tr}(M_y\mathcal E_{\rm sample}(\rho_{\rm probe})),\quad \hat s=R(\{y_i\})
```

## How To Read The Relation

The displayed relation should be read as a rule for transporting a state, not as a second definition of the state. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

## What Remains Stable

The mechanism is an apparatus-coupled observable: a prepared probe state interacts with a sample or field, the interaction changes phase, momentum, intensity, or counting statistics, and the instrument reconstructs an image, spectrum, trajectory, or estimate. Quantum amplifier specifies lawful change before measurement. The generator determines the propagator or path weight that carries the state between preparation and measurement. Conserved quantities and symmetries are read from the generator and its commutation relations.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. Time dependence can be assigned to states, operators, propagators, or path amplitudes. Perturbative, Hamiltonian, Lagrangian, and path-integral presentations can represent the same evolution. Approximation schemes change the calculational route without changing the target transition amplitude.

## Connection To The Next Step

A generator predicts a new state but not yet an experimental number. The next step selects an observable, whose spectrum and expectation values expose consequences of the dynamics.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Lawful closed-system evolution preserves norm or trace; open-system evolution must preserve positivity and trace under the stated approximation.
- The short-time and classical limits identify whether the generator has the correct physical regime.

## Evidence Links

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:2108.07838](https://arxiv.org/abs/2108.07838)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
