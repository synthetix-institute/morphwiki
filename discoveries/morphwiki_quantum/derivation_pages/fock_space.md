# Fock space

An excited atom in an empty cavity can decay to its ground state, leaving one photon in a cavity mode. The light of a laser contains no definite number of photons at all. A description with a fixed number of particles cannot represent either situation. Fock space collects the states of zero, one, two and more identical particles in one Hilbert space, so that a single operator can change the particle number.

Let $\mathcal H$ be the one-particle Hilbert space with orthonormal modes $\varphi_1,\varphi_2,\dots$. The $N$-particle space is the symmetric part of $\mathcal H^{\otimes N}$ for bosons and the antisymmetric part for fermions, written $S_\pm\mathcal H^{\otimes N}$. Fock space is their direct sum. Its basis states are labeled by occupation numbers $n_i$, the number of particles in mode $i$:

```math
\mathcal F_\pm=\bigoplus_{N=0}^{\infty}S_\pm\mathcal H^{\otimes N},\qquad
\ket{n_1,n_2,\dots},\qquad \hat N=\sum_ia_i^\dagger a_i.
```

For bosons the creation and annihilation operators change one occupation by one unit, with factors fixed by the commutation relations:

```math
a_i^\dagger\ket{\dots,n_i,\dots}=\sqrt{n_i+1}\,\ket{\dots,n_i+1,\dots},\\
a_i\ket{\dots,n_i,\dots}=\sqrt{n_i}\,\ket{\dots,n_i-1,\dots},\qquad
[a_i,a_j^\dagger]=\delta_{ij}.
```

For fermions $n_i$ is zero or one, the commutator becomes an anticommutator, and each operator carries a sign $(-1)^{\sum_{k<i}n_k}$ fixed by an ordering of the modes. Exchange symmetry is then built in: a state specifies how many particles occupy each mode, not which particle is where. A one-body operator with matrix elements $h_{ij}=\langle\varphi_i|h|\varphi_j\rangle$ becomes $\sum_{ij}h_{ij}a_i^\dagger a_j$, the same expression for every particle number. Processes that create or absorb particles contain unequal numbers of creation and annihilation operators.

The emission of light shows what the factor $\sqrt{n+1}$ does. Consider a two-level atom with ground state $g$ and excited state $e$, coupled to one field mode of angular frequency $\omega$ that contains $n$ photons. Near resonance, in the rotating-wave approximation, the coupling is $\hbar\lambda(\sigma_+a+\sigma_-a^\dagger)$. Here $\sigma_-$ takes the atom from $e$ to $g$, $\sigma_+$ does the reverse, and $\lambda$ is a coupling frequency. The ladder relations give

```math
\langle g,n+1|H_{\rm int}|e,n\rangle=\hbar\lambda\sqrt{n+1},\qquad
\langle e,n-1|H_{\rm int}|g,n\rangle=\hbar\lambda\sqrt{n}.
```

Transition rates are proportional to squared matrix elements. Emission into the mode therefore proceeds at a rate proportional to $n+1$, and absorption at a rate proportional to $n$. The part proportional to $n$ is stimulated emission; the remaining term is spontaneous emission, present even in an empty mode. This is Einstein's relation between his A and B coefficients, here a consequence of the operator algebra. With equilibrium populations $N_e/N_g=e^{-\hbar\omega/k_BT}$, the balance $N_e(n+1)=N_gn$ gives $n=(e^{\hbar\omega/k_BT}-1)^{-1}$, the Planck occupation.

The ratio of stimulated to spontaneous emission into a mode equals its occupation. For visible light at 600 nm in surroundings at 300 K, the thermal occupation is $n\approx2\times10^{-35}$, so thermal sources emit spontaneously. A 1 GHz microwave mode at the same temperature has $n\approx6\times10^3$, and stimulated processes dominate. A laser maintains a large $n$ in one mode by population inversion, which is why its emission is coherent and directional.

A fixed set of modes describes noninteracting particles exactly. Interactions mix occupation states, so the occupation basis remains a basis but its states are no longer stationary. Each mode of a free field is a Quantum harmonic oscillator, and Quantum field theory uses Fock space as the state space of free particles. Bose--Einstein statistics and Fermi--Dirac statistics give the equilibrium distributions of the occupation numbers.

## References For The Physical Derivation

- [H. Tasaki, Introduction to the second quantization formalism for non-relativistic quantum mechanics; Fock space and creation and annihilation operators for bosons and fermions.](https://arxiv.org/abs/1812.10732)
