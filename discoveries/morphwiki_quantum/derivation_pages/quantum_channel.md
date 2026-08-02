# Quantum channel

**Derivation step:** Protocol layer: engineered transformations

## Topic Context

In quantum information theory, a quantum channel is a communication channel that can transmit quantum information, as well as classical information. An example of quantum information is the general dynamics of a qubit. An example of classical information is a text document transmitted over the Internet.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Quantum_channel)

## Role In The Derivation

Quantum channel is the open-system protocol constructor: it maps input states to output states while preserving complete positivity and trace.

## Why This Step Is Needed

A quantum channel is the general transformation available to a state when an environment, uncontrolled degree of freedom, or measurement outcome is not retained. It extends unitary dynamics without abandoning positivity or probability conservation.

## Mechanism

A channel is the mechanism for noisy transformations, measurements with forgotten outcomes, and subsystem evolution.

## How It Enters The Theory

**Place in the construction.** Quantum channel contributes an engineered operation-sequence role to the quantum construction. This page is read first as an operation-sequence move: it specifies an ordered composition of allowed maps.

**State and operation.** Input and output density operators, possibly on different Hilbert spaces or subsystem carriers. A completely positive trace-preserving map, often represented by Kraus operators or by a Stinespring dilation.

**Admissibility and prediction.** Complete positivity and trace preservation are the legal conditions; non-trace-preserving maps require an explicitly conditioned outcome. Output state, final POVM probabilities, fidelity, capacity, error rate, or recovered subsystem statistics.

## Topic Equations

Standard constructor skeleton: completely positive trace-preserving map and observable.

```math
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger
\sum_aK_a^\dagger K_a=I
p(y)=\operatorname{Tr}(M_y\mathcal E(\rho))
```

## How To Read The Relation

Complete positivity guarantees that the map remains physical when the input is entangled with an untouched system, and trace preservation guarantees total probability. A Kraus representation displays one realization, but different Kraus sets can describe the same channel.

## Worked Example

Loss of phase coherence can be represented by a dephasing channel. Its action suppresses off-diagonal density-matrix elements while leaving the corresponding populations unchanged.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

Quantum error correction asks whether information can be encoded so that a specified family of channels is detectable and reversible on the code space.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:0805.4565](https://arxiv.org/abs/0805.4565)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
