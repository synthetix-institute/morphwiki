# Self-adjoint operator

**Physical domain:** Observables and spectra

## Mechanism

Self-adjoint operator is the admissible-observable condition: it gives real spectra and well-defined spectral measures.

Self-adjoint operator states which physical question is being asked. The same state supports many incompatible questions, so a prediction requires an operator, spectral measure, or effect family in addition to the state itself.

Self-adjointness is not a technical decoration. It is the condition that makes an operator a legitimate spectral question in ordinary quantum mechanics.

## Physical Construction

The state carrier is an admissible quantum state space on which the physical quantity is represented. The governing operation is a self-adjoint operator, operator-valued measure, or algebra element representing the physical question. Domain, self-adjointness, gauge invariance, and spectral conditions determine whether the quantity is a physical observable. The calculated observables are Eigenvalues, spectral measures, expectation values, moments, and response functions associated with the observable.

## Topic Equations

Standard constructor skeleton: spectral theorem form of a legitimate observable.

```math
A=A^\dagger
A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)
\Pr(\Delta)=\operatorname{Tr}(\rho E_A(\Delta))
```

## Physical Meaning

The operator's spectrum lists possible sharp values, while the state determines their weights. Matrix entries depend on basis, but the spectrum, expectation values, and probability distribution are unchanged by an equivalent representation. Domain and self-adjointness conditions are part of the physical definition.

An observable defines possible outcomes. The measurement chapter adds the probability rule and, when needed, the physical interaction that records one of those outcomes.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.
