# Wave function

**Derivation step:** State carrier inside Hilbert space
**Status:** topic-specific mechanism

## Role In The Derivation

Wave function is a basis-dependent representative of a pure-state ray; it is not identical to the abstract state or to physical configuration space.

## Mechanism

For a configuration space Q with measure mu, the position wave function is the generalized-basis representative psi(x)=<x|psi> of a ray [psi] in L2(Q,mu). Vectors that differ by a nonzero global phase represent the same pure state. Its modulus squared is a probability density only relative to the stated position measure; spin and particle statistics enlarge or constrain the carrier. The linked equation set is concentrated in state evolution, operator-to-spectrum readout, normalization or admissibility; its mathematical presentation emphasizes local notation, information profile, formula structure.

## Quantum Mechanism Frame

- **Role:** Wave function contributes a state-carrier role to the quantum construction.
- **Placement:** This page is read first as a state-carrier move: it specifies what mathematical object carries prediction.
- **Carrier or domain:** The mathematical state object: vector, wavefunction, density operator, coherent state, field state, or register.
- **Operator or map:** Operators, maps, and observables become meaningful only after this carrier and its domain have been fixed.
- **Admissibility:** Normalization, positivity, inner product, representation, tensor factorization, or superselection conditions define legal states.
- **Readout:** Probability distributions obtained by applying the appropriate observables or measurement maps to the carrier.
- **Check:** Equivalent representations must preserve probabilities and expectation values when the change is only representational.

## Topic Equations

Topic-specific constructor: abstract state ray, position representation, measure-dependent Born probability, and internal spin carrier.

```math
\mathcal H=L^2(Q,d\mu),\qquad \psi(x)=\langle x|\psi\rangle
\int_Q |\psi(x)|^2\,d\mu(x)=1,\qquad \ket\psi\sim e^{i\alpha}\ket\psi
\Pr(X\in\Delta\mid\psi)=\langle\psi|E_X(\Delta)|\psi\rangle=\int_\Delta|\psi(x)|^2\,d\mu(x)
\mathcal H_{\mathrm{spin}\,s}=L^2(Q,d\mu)\otimes\mathbb C^{2s+1}
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
- [arXiv:1604.06537](https://arxiv.org/abs/1604.06537)
- [arXiv:1801.03283](https://arxiv.org/abs/1801.03283)
- [arXiv:1708.03640](https://arxiv.org/abs/1708.03640)
- [arXiv:quant-ph0205159](https://arxiv.org/abs/quant-ph/0205159)
