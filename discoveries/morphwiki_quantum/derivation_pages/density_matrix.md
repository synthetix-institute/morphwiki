# Density matrix

**Physical domain:** Quantum states and subsystem structure

## Mechanism

Density matrix is the mixed-state constructor: it keeps probabilistic preparation, entanglement with unobserved degrees of freedom, and partial information in the same state formalism.

The density matrix is required whenever the preparation is statistical, part of an entangled system is ignored, or environmental coupling makes a state-vector description of the subsystem incomplete.

Density matrices generalize pure states without changing the state-to-spectrum probability assignment rule. They are the correct carrier when the preparation is statistical, when a subsystem is traced out, or when decoherence is being described.

## Physical Construction

The state carrier is the mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. The governing operation is Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed. Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. The calculated observables are Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Standard constructor skeleton: mixed state, trace rule, and subsystem reduction.

```math
\rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a},\qquad p_a\ge0,\quad \sum_a p_a=1
\rho\ge0,\qquad \operatorname{Tr}\rho=1
p(i)=\operatorname{Tr}(\rho P_i)
\rho_A=\operatorname{Tr}_B(\rho_{AB})
```

## Physical Meaning

Diagonal elements in a selected basis give populations and off-diagonal elements carry coherence in that basis. Positivity and unit trace make the Born probabilities legal. Partial tracing produces the state of a subsystem without assigning a pure vector to it.

Either randomly preparing two spin directions or discarding one member of an entangled pair can produce a mixed state. The density matrix records the observable statistics, even though the physical origins of the mixture differ.

With the state representation established, unitary and non-unitary maps specify how it changes.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:quant-ph/0008131](https://arxiv.org/abs/quant-ph/0008131)
- [arXiv:quant-ph0008131](https://arxiv.org/abs/quant-ph0008131)
- [arXiv:hep-th/0110224](https://arxiv.org/abs/hep-th/0110224)
- [arXiv:hep-th0110224](https://arxiv.org/abs/hep-th0110224)
