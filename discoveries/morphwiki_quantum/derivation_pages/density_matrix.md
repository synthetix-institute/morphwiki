# Density matrix

**Derivation step:** State carrier inside Hilbert space
**Status:** topic-specific mechanism

## Role In The Derivation

Density matrix is the mixed-state constructor: it keeps probabilistic preparation, entanglement with unobserved degrees of freedom, and partial information in the same state formalism.

## Mechanism

Density matrices generalize pure states without changing the state-to-spectrum readout rule. They are the correct carrier when the preparation is statistical, when a subsystem is traced out, or when decoherence is being described. In the source-evidence profile for this page, the strongest construction signal is operator-to-spectrum readout, state evolution, normalization or admissibility; the strongest carrier signal is local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Density matrix contributes a state-carrier role to the quantum construction.
- **Placement:** This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.
- **Carrier or domain:** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register.
- **Operator or map:** Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.
- **Admissibility:** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states.
- **Readout:** Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.
- **Check:** Equivalent representations must preserve probabilities and expectation values when the change is only representational.

## Topic Equations

Standard constructor skeleton: mixed state, trace rule, and subsystem reduction.

```math
\rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a},\qquad p_a\ge0,\quad \sum_a p_a=1
\rho\ge0,\qquad \operatorname{Tr}\rho=1
p(i)=\operatorname{Tr}(\rho P_i)
\rho_A=\operatorname{Tr}_B(\rho_{AB})
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
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
