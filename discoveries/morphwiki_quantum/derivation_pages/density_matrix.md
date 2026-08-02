# Density matrix

**Derivation step:** State carrier inside Hilbert space

## Topic Context

In quantum mechanics, a density matrix is a matrix used in calculating the probabilities of the outcomes of measurements performed on physical systems. It is a generalization of the state vectors or wavefunctions: while those can only represent pure states, density matrices can also represent mixed ensembles of states. These arise in quantum mechanics in two different situations:when the preparation of a system can randomly produce different pure states, and thus one must deal with the statistics of the ensemble of possible preparations; and when one wants to describe a physical system that is entangled with another, without describing their combined state.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Density_matrix)

## Role In The Derivation

Density matrix is the mixed-state constructor: it keeps probabilistic preparation, entanglement with unobserved degrees of freedom, and partial information in the same state formalism.

## Why This Step Is Needed

The density matrix is required whenever the preparation is statistical, part of an entangled system is ignored, or environmental coupling makes a state-vector description of the subsystem incomplete.

## Mechanism

Density matrices generalize pure states without changing the state-to-spectrum probability assignment rule. They are the correct carrier when the preparation is statistical, when a subsystem is traced out, or when decoherence is being described.

## How It Enters The Theory

**Place in the construction.** Density matrix contributes a state-carrier role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.

**Admissibility and prediction.** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Standard constructor skeleton: mixed state, trace rule, and subsystem reduction.

```math
\rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a},\qquad p_a\ge0,\quad \sum_a p_a=1
\rho\ge0,\qquad \operatorname{Tr}\rho=1
p(i)=\operatorname{Tr}(\rho P_i)
\rho_A=\operatorname{Tr}_B(\rho_{AB})
```

## How To Read The Relation

Diagonal elements in a selected basis give populations and off-diagonal elements carry coherence in that basis. Positivity and unit trace make the Born probabilities legal. Partial tracing produces the state of a subsystem without assigning a pure vector to it.

## Worked Example

Either randomly preparing two spin directions or discarding one member of an entangled pair can produce a mixed state. The density matrix records the observable statistics, even though the physical origins of the mixture differ.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

With the state representation established, unitary and non-unitary maps specify how it changes.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:0912.2823](https://arxiv.org/abs/0912.2823)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
