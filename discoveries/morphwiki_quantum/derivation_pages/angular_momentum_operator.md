# Angular momentum operator

**Derivation step:** Spectral question: what can be asked

## Topic Context

In quantum mechanics, the angular momentum operator is one of several related operators analogous to classical angular momentum. The angular momentum operator plays a central role in the theory of atomic and molecular physics and other quantum problems involving rotational symmetry. Being an observable, its eigenfunctions represent the distinguishable physical states of a system's angular momentum, and the corresponding eigenvalues the observable experimental values. When applied to a mathematical representation of the state of a system, yields the same state multiplied by its angular momentum value if the state is an eigenstate. In both classical and quantum mechanical systems, angular momentum is one of the three fundamental properties of motion.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Angular_momentum_operator)

## Role In The Derivation

Angular momentum operator belongs to the question step: it turns a physical question into an operator with admissible answers.

## Why This Step Is Needed

Angular momentum operator states which physical question is being asked. The same state supports many incompatible questions, so a prediction requires an operator, spectral measure, or effect family in addition to the state itself.

## Mechanism

This step identifies the physical quantity being represented, its operator, and the possible values supplied by its spectrum.

## How It Enters The Theory

**Place in the construction.** Angular momentum operator contributes an observable and spectral role to the quantum construction. This page is read first as a question-selection move: it identifies the observable and its possible values.

**State and operation.** An admissible quantum state space on which the physical quantity is represented. A self-adjoint operator, operator-valued measure, or algebra element representing the physical question.

**Admissibility and prediction.** Domain, self-adjointness, gauge invariance, and spectral conditions determine whether the quantity is a physical observable. Eigenvalues, spectral measures, expectation values, moments, and response functions associated with the observable.

## Representative Relation

```math
O=\int_{\sigma(O)}\lambda\,dE_O(\lambda),\quad \langle O\rangle_\rho=\operatorname{Tr}(\rho O)
```

## How To Read The Relation

The operator's spectrum lists possible sharp values, while the state determines their weights. Matrix entries depend on basis, but the spectrum, expectation values, and probability distribution are unchanged by an equivalent representation. Domain and self-adjointness conditions are part of the physical definition.

## What Remains Stable

Angular momentum operator defines the legal question being asked of the state. The measurable answers are encoded by the operator spectrum, projectors, or spectral measure. The operator role is preserved across equivalent bases even when matrix entries change.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The same observable may be represented by matrices, differential operators, projectors, or algebraic elements. Degeneracy, basis choice, and domain conditions can change how the spectrum is displayed. Detector implementation changes the physical realization, not the operator role itself.

## Connection To The Next Step

An observable defines possible outcomes. The measurement chapter adds the probability rule and, when needed, the physical interaction that records one of those outcomes.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Self-adjointness, or the appropriate POVM positivity condition, is what makes the question a legal observable.
- A complete spectral resolution supplies all outcome channels for the question being asked.

## Evidence Links

- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
