# Path integral

**Physical domain:** Dynamics and transformations

## Mechanism

Path integral is an alternate generator constructor: transition amplitudes are obtained by summing phase weights over histories.

Path integral separates quantum kinematics from dynamics. The state space lists what can exist, whereas a Hamiltonian, action, Liouvillian, or channel generator specifies which changes are allowed and on what timescale.

The path integral does not replace the operator constructor. It repackages the generator step as a weighted sum over histories between boundary conditions. It is especially useful when action, symmetry, and field degrees of freedom are more natural than state-vector evolution.

## Physical Construction

The state carrier is a state vector, density operator, wavefunction, field state, or register on a specified domain. The governing operation is Hamiltonian, unitary map, channel generator, action, constraint, or differential operator that transports the state. Self-adjointness, complete positivity, trace preservation, gauge constraints, and boundary/domain conditions decide whether the evolution is legal. The calculated observables are Time-dependent probabilities, spectra, transition amplitudes, conserved quantities, or response functions.

## Topic Equations

Standard constructor skeleton: boundary-to-boundary transition amplitude through action weights.

```math
K(x_f,t_f;x_i,t_i)=\int_{x_i}^{x_f}\mathcal D x(t)\,\exp\!\left(\frac{i}{\hbar}S[x]\right)
\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i
```

## Physical Meaning

The evolution law transports a state without redefining it. Closed-system evolution is unitary; effective open-system evolution must preserve trace and positivity. Equivalent Hamiltonian, propagator, and path-integral descriptions agree on transition amplitudes.

The evolved state becomes experimentally meaningful through an observable whose spectrum and expectation values expose the consequences of the dynamics.

## Invariance And Realization

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Discriminating Consequences

A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation. The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Source Equations

- [arXiv:hep-ph/0110112](https://arxiv.org/abs/hep-ph/0110112)
- [arXiv:hep-ph0110112](https://arxiv.org/abs/hep-ph0110112)
