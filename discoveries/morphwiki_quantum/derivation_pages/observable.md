# Observable

**Derivation step:** Spectral question: what can be asked

## Topic Context

In physics, an observable is a physical property or physical quantity that can be measured. In classical mechanics, an observable is a real-valued "function" on the set of all possible system states, e.g., position and momentum. In quantum mechanics, an observable is described by a linear operator. For example, these operators might represent submitting the system to various electromagnetic fields and eventually reading a value.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Observable)

## Role In The Derivation

Observable is the legal-question constructor: it turns a physical question into an operator with spectral outcome channels.

## Why This Step Is Needed

An observable converts a broad physical question such as position, energy, or spin into an operator with a defined domain and spectrum. Without that operator, the state alone does not specify which distribution is being predicted.

## Mechanism

An observable is the mathematical form of a question that can be asked of a state. Its spectral decomposition defines the possible answers.

## How It Enters The Theory

**Place in the construction.** Observable contributes an observable and spectral role to the quantum construction. This page is read first as a question-selection move: it identifies the observable and its possible values.

**State and operation.** An admissible quantum state space on which the physical quantity is represented. A self-adjoint operator, operator-valued measure, or algebra element representing the physical question.

**Admissibility and prediction.** Domain, self-adjointness, gauge invariance, and spectral conditions determine whether the quantity is a physical observable. Eigenvalues, spectral measures, expectation values, moments, and response functions associated with the observable.

## Topic Equations

Standard constructor skeleton: self-adjoint question, spectral projectors, and Born probabilities.

```math
A=A^\dagger
A=\sum_i a_iP_i
p(a_i)=\operatorname{Tr}(\rho P_i)
```

## How To Read The Relation

The spectral measure decomposes the observable into possible outcome sectors. Pairing those sectors with the state gives probabilities, and weighting them by their spectral values gives expectation values. Degenerate eigenspaces correspond to outcomes that do not resolve every state component.

## Worked Example

A spin state has different probability distributions for measurements along different axes. The preparation is unchanged; the observable selects the question.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

The Born rule supplies the probability assigned to each spectral sector, and measurement theory describes its physical registration.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
