# Quantum tunnelling

**Derivation step:** Boundary realization: how effects appear

## Topic Context

In physics, quantum tunnelling, barrier penetration, or simply tunnelling is a quantum mechanical phenomenon in which an object such as an electron or atom passes through a potential energy barrier that, according to classical mechanics, should not be passable due to the object not having sufficient energy to pass or surmount the barrier.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_tunnelling)

## Role In The Derivation

Quantum tunnelling is a boundary-realization constructor: a state has nonzero transmission through a classically forbidden region.

## Why This Step Is Needed

Quantum tunnelling tests the consequence of wave evolution across a classically forbidden region. The effect depends jointly on the generator, barrier geometry, matching conditions, and incident state.

## Mechanism

Tunnelling shows that the realization layer matters. A potential barrier changes the admissible wave solutions and produces transmission even where classical kinetic energy would be negative.

## How It Enters The Theory

**Place in the construction.** Quantum tunnelling contributes a boundary-shaped spectrum role to the quantum construction. This page is read first as a realization move: it changes the domain, boundary, geometry, or interface in which the operator acts.

**State and operation.** A Hilbert space with a selected domain, potential, interface, asymptotic channel, cavity, well, or boundary condition. A Hamiltonian, wave operator, transfer operator, or scattering map whose domain is changed by the boundary.

**Admissibility and prediction.** Boundary conditions and matching conditions determine allowed states, resonances, transmission amplitudes, and spectra. Eigenvalues, resonances, tunnelling probabilities, phase shifts, reflection/transmission amplitudes, or scattering data.

## Topic Equations

Standard constructor skeleton: barrier-domain Schrödinger equation and WKB transmission.

```math
T\sim \exp\!\left(-2\int_{x_1}^{x_2}\sqrt{\frac{2m(V(x)-E)}{\hbar^2}}\,dx\right)
-\frac{\hbar^2}{2m}\psi''(x)+V(x)\psi(x)=E\psi(x)
```

## How To Read The Relation

Inside the barrier the stationary wave function is evanescent rather than oscillatory. Continuity and flux conditions connect it to incoming and outgoing waves, producing a nonzero transmission amplitude that falls approximately exponentially with barrier width in the semiclassical regime.

## Worked Example

Changing the barrier width while holding its height and the incident energy fixed isolates the predicted exponential dependence and separates tunnelling from an over-barrier contribution.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Scattering theory generalizes the same matching construction to many incoming, outgoing, and resonant channels.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
