# Qubit

**Physical domain:** Quantum states and subsystem structure

## Mechanism

Qubit is the two-dimensional state-carrier constructor used when the admissible state space is \(\mathbb C^2\).

Qubit specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

A qubit is the minimal quantum state space with a basis, amplitudes, unitary control, and measurement observable. Bloch-vector language is a representation of the same two-dimensional carrier.

## Physical Construction

The state carrier is the mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. The governing operation is Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed. Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. The calculated observables are Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Standard constructor skeleton: two-state carrier, Bloch representation, and basis observable.

```math
\ket{\psi}=\alpha\ket{0}+\beta\ket{1},\qquad |\alpha|^2+|\beta|^2=1
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),\qquad |\mathbf r|\le1
p(0)=|\langle0|\psi\rangle|^2,\qquad p(1)=|\langle1|\psi\rangle|^2
```

## Physical Meaning

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

The Hamiltonian or channel evolves the prepared state. An observable and measurement map then convert that evolved state into outcome probabilities.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

Candidate paper and equation-card identifiers were found, but no source equation has passed topic-level alignment; no citation is assigned.
