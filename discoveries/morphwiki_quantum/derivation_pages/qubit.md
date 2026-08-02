# Qubit

**Derivation step:** State carrier inside Hilbert space

## Topic Context

In quantum computing, a qubit or quantum bit is a basic unit of quantum information, the quantum version of the classic binary bit. A qubit can be physically realized with a two-state quantum-mechanical system, one of the simplest quantum systems displaying the peculiarity of quantum mechanics. Examples include the spin of the electron in which the two levels can be taken as spin up and spin down; or the polarization of a single photon in which the two spin states can also be measured as horizontal and vertical linear polarization. In a classical system, a bit would have to be in one state or the other. However, quantum mechanics allows the qubit to be in a coherent superposition of multiple states simultaneously, a property that is fundamental to quantum mechanics and quantum computing.

[Topic scaffold: Wikipedia, CC BY-SA; adapted.](https://en.wikipedia.org/wiki/Qubit)

## Role In The Derivation

Qubit is the two-dimensional state-carrier constructor used when the admissible state space is \(\mathbb C^2\).

## Why This Step Is Needed

Qubit specifies the object from which quantum probabilities are calculated. A Hamiltonian or an observable does not make a prediction by itself; it must act on a normalized state vector, density operator, or statistical sector that records the preparation.

## Mechanism

A qubit is the minimal quantum state space with a basis, amplitudes, unitary control, and measurement observable. Bloch-vector language is a representation of the same two-dimensional carrier.

## How It Enters The Theory

**Place in the construction.** Qubit contributes a state-carrier role to the quantum construction. This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.

**State and operation.** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register. Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.

**Admissibility and prediction.** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states. Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.

## Topic Equations

Standard constructor skeleton: two-state carrier, Bloch representation, and basis observable.

```math
\ket{\psi}=\alpha\ket{0}+\beta\ket{1},\qquad |\alpha|^2+|\beta|^2=1
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),\qquad |\mathbf r|\le1
p(0)=|\langle0|\psi\rangle|^2,\qquad p(1)=|\langle1|\psi\rangle|^2
```

## How To Read The Relation

Normalization guarantees that the probabilities sum to one, while positivity prevents negative probabilities. Pure vectors and density operators are not competing theories: the density-operator form also represents mixtures and reduced states obtained when unobserved degrees of freedom are traced out.

## What Remains Stable

The rule connecting prepared states, observables, and spectral probability measures across wave, matrix, path-integral, circuit, or field notation. The operator-to-spectrum relation: admissible observations are represented through eigenvalues, projections, modes, or outcome channels. The dependence of admissible observable on measurement context or boundary condition. The non-commuting compatibility structure, which survives changes of representation.

## What The Physical Realization Adds

The name of the carrier: particle, wave, field, qubit, or excitation. Where time dependence is represented: on the state, on the operator, or in a path weight. The coordinate system, basis, or geometric picture used to display the same relation. The physical implementation of detector, boundary, preparation, or observable.

## Connection To The Next Step

With the state identified, the next question is how it changes. The generator chapter supplies that lawful transformation; the observable and measurement chapters then turn the transformed state into a prediction.

## Checks

- A concrete transfer target is a material, biological, or collective system with a state, a transformation, and a spectral or categorical observable, but without a tested incompatibility relation.
- The validation criterion is that varying the context changes the admissible observable while the transformation law remains identifiable; shuffled or erased contexts should weaken the effect.

## Evidence Links

- [arXiv:1604.05385](https://arxiv.org/abs/1604.05385)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1612.00682](https://arxiv.org/abs/1612.00682)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
- [arXiv:1506.05598](https://arxiv.org/abs/1506.05598)
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
