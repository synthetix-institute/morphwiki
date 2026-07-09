# Projection-valued measure

**Derivation step:** Readout rule: how answers become probabilities
**Status:** topic-specific mechanism

## Role In The Derivation

Projection-valued measure is the sharp-readout constructor: mutually exclusive outcome projectors partition the identity.

## Mechanism

A projection-valued measure encodes an ideal sharp measurement. It defines outcome channels that are orthogonal and exhaustive. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Projection-valued measure contributes a probability/readout role to the quantum construction.
- **Placement:** This page is read first as a readout move: it connects the state and question to recorded outcomes.
- **Carrier or domain:** A state vector or density operator together with the measurement context in which outcome channels are defined.
- **Operator or map:** A projection-valued measure, POVM, update map, or instrument map connecting state to record.
- **Admissibility:** Outcome probabilities must be positive, normalized, and tied to a specified readout map rather than to informal observer language.
- **Readout:** Born probabilities, detector records, post-measurement states, ensemble frequencies, or decision probabilities.
- **Check:** The interpretation is constrained by whether it changes the probability rule, the update rule, the detector model, or only the language used for them.

## Topic Equations

Standard constructor skeleton: sharp outcome channels, probability, and projective update.

```math
P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=I
p(i)=\operatorname{Tr}(\rho P_i)
\rho\mapsto \frac{P_i\rho P_i}{\operatorname{Tr}(\rho P_i)}
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

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:2308.15676](https://arxiv.org/abs/2308.15676)
