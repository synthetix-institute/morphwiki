# Quantum chemistry

A proton and a hydrogen atom bind into the molecular ion $\mathrm H_2^+$. The bond is held by a single electron, and the depth of the potential well is 2.79 eV. The binding comes from the wave nature of the electron: its amplitudes near the two nuclei interfere. The simplest calculation that shows this, the linear combination of atomic orbitals, is also the starting point of molecular-orbital theory.

Protons are 1836 times heavier than electrons and move much more slowly. In the Born--Oppenheimer approximation they are held at a fixed separation $R$. The electronic energy at each $R$, including the proton repulsion, then serves as the potential for nuclear motion. In atomic units the electronic Hamiltonian is $H=-\tfrac12\nabla^2-1/r_a-1/r_b+1/R$, with $r_a$ and $r_b$ the distances to the two protons. The trial states combine the hydrogen 1s orbitals $\phi_a$ and $\phi_b$ centred on each proton:

```math
\psi_\pm=\frac{\phi_a\pm\phi_b}{\sqrt{2(1\pm S)}},\qquad
E_\pm(R)=-\frac12+\frac1R-\frac{J\pm K}{1\pm S}.
```

The variational principle selects these combinations. The $2\times2$ matrices of $H$ and of the overlap in the basis $\phi_a,\phi_b$ are unchanged when the protons are interchanged, so their eigenvectors are the even and odd combinations. Each $E_\pm$ is an upper bound to the exact energy of that symmetry. The three integrals are the overlap $S=\langle\phi_a|\phi_b\rangle$, the attraction $J=\langle\phi_a|r_b^{-1}|\phi_a\rangle$ of one atomic cloud to the other proton, and the resonance integral $K=\langle\phi_a|r_a^{-1}|\phi_b\rangle$. The last exists only because the orbitals overlap:

```math
S=e^{-R}\left(1+R+\frac{R^2}{3}\right),\qquad
J=\frac1R-e^{-2R}\left(1+\frac1R\right),\qquad
K=e^{-R}(1+R).
```

In the even, bonding state the electron density accumulates between the protons, where both attract it. In the odd, antibonding state it has a node on the midplane. Minimizing $E_+(R)$ gives an equilibrium separation of 2.49 bohr, or 0.132 nm, and a well depth of 1.76 eV below a hydrogen atom and a free proton. The exact Born--Oppenheimer solution gives 2.00 bohr, or 0.106 nm, and 2.79 eV. Letting the orbital exponent vary with $R$ already improves the result to 2.00 bohr and 2.35 eV.

The antibonding curve $E_-(R)$ is repulsive at all separations. Light that promotes the electron from the bonding to the antibonding state therefore dissociates the ion into a proton and a hydrogen atom. The two-orbital problem is a Two-state quantum system: the coupling between two localized states splits them into symmetric and antisymmetric combinations, as at an avoided crossing. The Born--Oppenheimer separation fails where two electronic energy surfaces approach each other, as in many photochemical reactions.

In $\mathrm H_2$ two electrons occupy the bonding orbital with opposite spins, in a singlet. The antisymmetry discussed under Fermion forces additional electrons into the antibonding orbital. With four electrons, as in $\mathrm{He}_2$, bonding and antibonding contributions cancel and no chemical bond forms. Electron repulsion makes the single-orbital description of $\mathrm H_2$ inaccurate at large separation, where it gives equal weight to ionic and covalent configurations.

Configuration interaction and coupled-cluster methods add this correlation systematically. Density-functional theory includes it through an approximate functional of the electron density. Each computes the same Born--Oppenheimer energy surface. The cost of an exact calculation grows exponentially with the number of orbitals, so strongly correlated molecules, such as many transition-metal complexes, remain difficult. Computing such energies is one proposed application of quantum computers; demonstrations so far concern small molecules.

## References For The Physical Derivation

- [S. McArdle, S. Endo, A. Aspuru-Guzik, S. Benjamin and X. Yuan, Quantum computational chemistry; the Born-Oppenheimer electronic structure problem, basis sets, correlation methods and quantum algorithms.](https://arxiv.org/abs/1808.10402)
