# Hilbert space

**Physical domain:** State space, domain, and representation

## Mechanism

Hilbert space is the admissible state carrier of quantum theory: it supplies the space in which states, operators, bases, spectra, and probabilities become legally defined.

Hilbert space is not merely a container for wave functions. Its inner product defines amplitudes and orthogonality, while the domains of unbounded operators decide whether expressions for position, momentum, and energy are mathematically and physically admissible.

Hilbert space is not physical space and not a geometric background in this book. It is the legal carrier of quantum identity. A state is a vector or density operator on it; the inner product gives amplitudes and norms; observables are self-adjoint operators on it; spectral projectors define possible answers; and unitary evolution preserves norm and probability. Hilbert space is therefore central because it binds state, probability, operator spectrum, and identity preservation into one formal carrier.

## Physical Construction

The state carrier is a complex Hilbert space, or a density-operator state space built on it. The governing operation is Self-adjoint observables, unitary maps, spectral projectors, and domain-restricted generators defined on the carrier. Inner-product structure, normalization, positivity for density states, and operator-domain conditions make states and observables legal. The calculated observables are Born probabilities, spectral projectors, expectation values, and preserved norms.

## Topic Equations

Standard constructor skeleton: normalized states, density states, spectral resolution, Born observable, and unitary identity preservation.

```math
\ket{\psi}\in\mathcal H,\qquad \langle\psi|\psi\rangle=1
\rho\in\mathcal S(\mathcal H),\qquad \rho\ge0,\quad \operatorname{Tr}\rho=1
A=A^\dagger,\qquad A=\int_{\sigma(A)}\lambda\,dE_A(\lambda)
\Pr(\Delta\mid \rho,A)=\operatorname{Tr}\!\left(\rho E_A(\Delta)\right)
\rho_t=U(t)\rho U(t)^\dagger,\qquad U^\dagger U=I
```

## Physical Meaning

The linear structure permits superposition, the inner product converts pairs of states into amplitudes, and completeness guarantees that convergent sequences of approximations remain inside the space. Operator domains must be carried with the operators; the same differential formula on another domain can describe a different physical system.

A qubit lives in a two-dimensional complex space, whereas a particle on a line is described in a space of square-integrable functions. Both obey the same Hilbert-space logic, but their operators, spectra, and boundary conditions are different.

After the arena is fixed, a quantum state selects one preparation or statistical ensemble within it.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
