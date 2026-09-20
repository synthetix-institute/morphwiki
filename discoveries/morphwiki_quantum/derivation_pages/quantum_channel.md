# Quantum channel

**Physical domain:** Control sequences and quantum channels

## Mechanism

Quantum channel is the open-system protocol constructor: it maps input states to output states while preserving complete positivity and trace.

A quantum channel is the general transformation available to a state when an environment, uncontrolled degree of freedom, or measurement outcome is not retained. It extends unitary dynamics without abandoning positivity or probability conservation.

A channel is the mechanism for noisy transformations, measurements with forgotten outcomes, and subsystem evolution.

## Physical Construction

The state carrier is Input and output density operators, possibly on different Hilbert spaces or subsystem carriers. The governing operation is a completely positive trace-preserving map, often represented by Kraus operators or by a Stinespring dilation. Complete positivity and trace preservation are the legal conditions; non-trace-preserving maps require an explicitly conditioned outcome. The calculated observables are Output state, final POVM probabilities, fidelity, capacity, error rate, or recovered subsystem statistics.

## Topic Equations

Standard constructor skeleton: completely positive trace-preserving map and observable.

```math
\mathcal E(\rho)=\sum_a K_a\rho K_a^\dagger
\sum_aK_a^\dagger K_a=I
p(y)=\operatorname{Tr}(M_y\mathcal E(\rho))
```

## Physical Meaning

Complete positivity guarantees that the map remains physical when the input is entangled with an untouched system, and trace preservation guarantees total probability. A Kraus representation displays one realization, but different Kraus sets can describe the same channel.

Loss of phase coherence can be represented by a dephasing channel. Its action suppresses off-diagonal density-matrix elements while leaving the corresponding populations unchanged.

Quantum error correction asks whether information can be encoded so that a specified family of channels is detectable and reversible on the code space.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.
