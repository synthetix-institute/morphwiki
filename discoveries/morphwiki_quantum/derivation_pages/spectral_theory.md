# Spectral theory

An observable specifies both possible outcomes and how a prepared state distributes probability among them. For a self-adjoint operator $A$, the spectral measure $E_A$ assigns an orthogonal projector to each measurable set of real outcomes. The operator and its measurement probabilities are reconstructed from this measure:

```math
A=\int_{\mathbb R}\lambda\,dE_A(\lambda),\qquad
p(\lambda\in B)=\operatorname{Tr}[\rho E_A(B)].
```

Here $B$ is an interval or other measurable outcome set and $\rho$ the density operator. For a discrete spectrum the integral becomes a sum over eigenspace projectors. For position or free-particle momentum it is genuinely continuous; their ideal eigenvectors are generalized distributions rather than normalizable prepared states. A detector with finite resolution measures an interval probability, not a normalizable state at one exact continuum value.

The same spectral measure determines functions of the operator. If $H$ is the time-independent Hamiltonian, the function $\exp(-iEt/\hbar)$ gives its unitary evolution. An energy decomposition therefore connects a spectroscopic question to dynamics:

```math
U(t)=\int e^{-iEt/\hbar}\,dE_H(E),\qquad
\langle\psi|U(t)|\psi\rangle=\int e^{-iEt/\hbar}\,d\mu_\psi(E),
```

where $\mu_\psi(B)=\langle\psi|E_H(B)|\psi\rangle$ is the energy distribution of the preparation. The survival amplitude is its Fourier transform. A narrow energy distribution changes phase slowly relative to itself; a broad distribution can dephase rapidly. This connects spectral width to temporal evolution without assuming irreversible decay.

The spectrum belongs to the operator with its domain. On an interval of length $L$, the same differential expression $-\hbar^2\partial_x^2/(2m)$ has a zero-energy constant mode with Neumann conditions, while Dirichlet conditions exclude it and begin at $\pi^2\hbar^2/(2mL^2)$. A change of boundary therefore changes both the energy outcomes and the time evolution, even though the bulk equation is unchanged.

Two Hamiltonians with identical energy values can still have different observable matrix elements. Transporting a mechanism requires a correspondence between states and observables, not just a matched list of eigenvalues. Spectral theory supplies the predictions once that correspondence and the operator domains are specified; it also identifies precisely what an isospectral comparison leaves undecided.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)


## Relations In The Original Papers

[arXiv:1508.06951, S2.EGx25](https://arxiv.org/html/1508.06951#S2.EGx25). Functions of a self-adjoint observable are defined by integration against its spectral measure. The domain of an unbounded function of the operator must be retained.
