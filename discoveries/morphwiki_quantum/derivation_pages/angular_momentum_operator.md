# Angular momentum operator

Rotations about different axes change orientation in an order-dependent way. In quantum mechanics their generators $J_x,J_y,J_z$ obey an algebra whose representations determine the allowed angular-momentum values. With $\hbar$ the reduced Planck constant,

```math
[J_i,J_j]=i\hbar\sum_k\epsilon_{ijk}J_k,\qquad
[J^2,J_i]=0,\qquad J^2=J_x^2+J_y^2+J_z^2.
```

A simultaneous eigenstate of $J^2$ and $J_z$ can be labeled $|j,m\rangle$. Define $J_\pm=J_x\pm iJ_y$. Their commutators with $J_z$ show that they raise or lower its eigenvalue by $\hbar$, while preserving $j$. Positivity of the squared norms fixes the endpoints of the ladder:

```math
J^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,\qquad
J_z|j,m\rangle=\hbar m|j,m\rangle,
```

```math
J_\pm|j,m\rangle=\hbar\sqrt{j(j+1)-m(m\pm1)}\,|j,m\pm1\rangle.
```

The ladder terminates at $m=\pm j$, giving $2j+1$ states. Single-valued orbital wave functions on ordinary three-dimensional space carry integer orbital angular momentum. Intrinsic spin uses representations of the covering group SU(2), allowing half-integer $j$. The same local commutator algebra is therefore realized on carriers with different global transformation properties.

For two spins, total angular momentum is $\mathbf J=\mathbf J_1+\mathbf J_2$. An isotropic exchange interaction can be rewritten using the total Casimir:

```math
H=\frac{K}{\hbar^2}\mathbf J_1\cdot\mathbf J_2
=\frac{K}{2\hbar^2}(J^2-J_1^2-J_2^2).
```

Here $K$ is an energy. Two spin-one-half particles then have a singlet energy $-3K/4$ and a triplet energy $K/4$. The gap is fixed by the coupling and the representation, without diagonalizing a general four-dimensional matrix. A magnetic field separates magnetic sublevels; an anisotropic interaction can also mix sectors that the isotropic model kept separate.

This calculation connects symmetry to a measurable excitation energy. Transferring the exchange formula to another object requires identifying which angular-momentum representation its degrees of freedom carry and whether anisotropy, orbital coupling or the environment changes the generator. A common algebra supplies the ladder relations, while the Hamiltonian selects which of those states a physical system occupies.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)
