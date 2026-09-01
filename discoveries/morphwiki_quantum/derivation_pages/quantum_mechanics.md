# Quantum mechanics

**Physical domain:** State space, domain, and representation

## Mechanism

Quantum mechanics is the baseline constructor: states live in Hilbert space, physical questions are represented by operators, and probabilities are assigned to spectral projectors.

Quantum mechanics is needed because a quantum equation has no fixed meaning until its state space, inner product, representation, and operator domains have been specified. These choices decide which states are admissible and which apparent changes are only changes of coordinates.

The page supplies the general quantum assembly. A preparation gives a state vector or density operator. A self-adjoint observable or measurement operator family gives the possible outcome channels. The Born or trace rule assigns probabilities, while Hamiltonian evolution transports the state between preparation and observable.

## Physical Construction

The state carrier is a Hilbert, Fock, or function space together with the operator domains and representation used in the calculation. The governing operation is a unitary or isometric change of basis, Fourier transform, coordinate map, or representation equivalence. Inner products, domains, normalization, and completeness relations must be preserved by a purely representational change. The calculated observables are Transition amplitudes, expectation values, spectra, and probabilities that remain invariant under an admissible representation change.

## Topic Equations

Topic-specific constructor: the equations express state admissibility, spectral prediction, unitary evolution, and incompatibility.

```math
\rho\ge 0,\qquad \operatorname{Tr}\rho=1
A=\sum_a aP_a,\qquad p(a)=\operatorname{Tr}(\rho P_a)
\rho(t)=U(t)\rho(0)U(t)^\dagger,\qquad U(t)=e^{-iHt/\hbar}
[A,B]\ne0\quad\Rightarrow\quad \text{no generic common sharp eigenbasis}
```

## Physical Meaning

A unitary or isometric change of representation carries the state and operator together. Amplitudes, expectation values, and spectra agree. If they do not, the physical model has changed rather than merely its notation.

A quantum state belongs to this state space, and every Hamiltonian and observable must act on its stated domain. These domain relations determine whether the resulting amplitudes and probabilities are defined.

## Invariance And Realization

The relation between prepared states, observables, and spectral probability measures. The use of eigenvalues, projectors, modes, or outcome channels to represent admissible observations. The dependence of the observable on basis, domain, potential, preparation, or measurement context. The commutator structure that limits which observables can be jointly diagonalized.

The physical carrier: particle, wave, field mode, spin, qubit, detector, or excitation. The representation: wave mechanics, matrix mechanics, density matrices, path integrals, circuits, or fields. Where time dependence is placed: on the state, on the operator, in a propagator, or in a path weight. The implementation of preparation, boundary condition, detector, or outcome channel.

## Discriminating Consequences

A transfer target provides a state space, a transformation law, and a spectral or categorical observable, with one compatibility relation experimentally unresolved. A useful validation varies the basis, domain, or measurement context and measures whether the allowed observable changes while the underlying transformation law remains identifiable. A stronger validation contains two candidate observables whose predicted commutator controls joint resolvability.

## Evidence Links

No V2-aligned source-equation candidate is available for this topic.
