# Wave function collapse

**Derivation step:** Measurement rule: how observables become probabilities

## Topic Context

In various interpretations of quantum mechanics, wave function collapse, also called reduction of the state vector, occurs when a wave function—initially in a superposition of several eigenstates—reduces to a single eigenstate due to interaction with the external world. This interaction is called an observation and is the essence of a measurement in quantum mechanics, which connects the wave function with classical observables such as position and momentum. Collapse is one of the two processes by which quantum systems evolve in time; the other is the continuous evolution governed by the Schrödinger equation.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Wave_function_collapse)

## Role In The Derivation

Wave function collapse belongs to the measurement step: it connects a prepared state and an operator spectrum to probabilities or state updates.

## Why This Step Is Needed

Wave function collapse connects the formal state and observable to experimental frequencies. It distinguishes the probability assigned to an outcome from the conditional state change that may follow a recorded event.

## Mechanism

The topic modifies how a state is connected to recorded outcomes. The stable machinery is the spectral measure or POVM together with the probability rule.

## How It Enters The Theory

**Place in the construction.** Wave function collapse contributes a probability/observable role to the quantum construction. This page is read first as a measurement move: it connects the state and observable to outcome probabilities.

**State and operation.** A state vector or density operator together with the measurement context in which outcome channels are defined. A projection-valued measure, POVM, update map, or instrument map connecting state to record.

**Admissibility and prediction.** Outcome probabilities must be positive, normalized, and tied to a specified measurement map rather than to informal observer language. Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.

## Representative Relation

```math
\Pr(\Delta)=\operatorname{Tr}(\rho E(\Delta)),\quad \rho\mapsto \frac{M_y\rho M_y^\dagger}{\operatorname{Tr}(M_y\rho M_y^\dagger)}
```

## How To Read The Relation

Each positive effect represents an outcome channel and the effects sum to the identity, which enforces normalized probabilities. A projective measurement is a special case. A complete detector model may further specify a quantum instrument, whose maps describe both the outcome probability and the corresponding post-measurement state.

## What Remains Stable

The topic modifies how a state is connected to recorded outcomes. The stable machinery is the spectral measure or POVM together with the probability rule. Wave function collapse connects the state and the spectral question to observed probabilities. The invariant step is the map from state plus measurement operators to a normalized probability distribution. Projection-valued and POVM observables preserve the same role: outcome channels weighted by the state.

## What The Physical Realization Adds

The local title, representation, and physical realization may change while the constructor role is preserved. The detector model, basis, and update convention can change. State-vector, density-matrix, projective, and generalized-measurement forms may present the observable differently. Interpretive language about collapse or information update can vary without changing the probability rule.

## Connection To The Next Step

Once the probability rule is explicit, incompatibility can be tested rather than asserted. Commutators, uncertainty relations, and Bell-type constraints identify when several measurement questions cannot share one sharp assignment.

## Checks

- Specify the topic's state carrier, operator or map, observable or predicted quantity, and compatibility condition in its own quantum language.
- Outcome probabilities are non-negative and normalized because the observable acts on a valid state with a complete effect family.
- Projective measurement is the sharp limit of the same probability rule when effects become orthogonal projectors.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
