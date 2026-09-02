# Observable

**Physical domain:** Observables and spectra

## Mechanism

Observable is the legal-question constructor: it turns a physical question into an operator with spectral outcome channels.

An observable converts a broad physical question such as position, energy, or spin into an operator with a defined domain and spectrum. Without that operator, the state alone does not specify which distribution is being predicted.

An observable is the mathematical form of a question that can be asked of a state. Its spectral decomposition defines the possible answers.

## Physical Construction

The state carrier is an admissible quantum state space on which the physical quantity is represented. The governing operation is a self-adjoint operator, operator-valued measure, or algebra element representing the physical question. Domain, self-adjointness, gauge invariance, and spectral conditions determine whether the quantity is a physical observable. The calculated observables are Eigenvalues, spectral measures, expectation values, moments, and response functions associated with the observable.

## Topic Equations

Standard constructor skeleton: self-adjoint question, spectral projectors, and Born probabilities.

```math
A=A^\dagger
A=\sum_i a_iP_i
p(a_i)=\operatorname{Tr}(\rho P_i)
```

## Physical Meaning

The spectral measure decomposes the observable into possible outcome sectors. Pairing those sectors with the state gives probabilities, and weighting them by their spectral values gives expectation values. Degenerate eigenspaces correspond to outcomes that do not resolve every state component.

A spin state has different probability distributions for measurements along different axes. The preparation is unchanged; the observable selects the question.

The Born rule supplies the probability assigned to each spectral sector, and measurement theory describes its physical registration.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:gr-qc/0008032](https://arxiv.org/abs/gr-qc/0008032)
- [arXiv:gr-qc0008032](https://arxiv.org/abs/gr-qc0008032)
