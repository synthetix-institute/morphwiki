# Quantum geometry

A tetrahedron in flat space is fixed by its six edge lengths. Once its four face areas are known, two further numbers, such as two dihedral angles, specify its shape. Quantum geometry asks what happens when areas and angles become operators. For a single tetrahedron the answer is exact. The face areas can be sharp, but two angles cannot be sharp together when the volume differs from zero.

Describe face $i$ by its area vector $\mathbf A_i$, normal to the face with length equal to its area. For a tetrahedron the four outward vectors sum to zero. Take edge vectors $\mathbf a,\mathbf b,\mathbf c$ from one vertex, so that three faces have $\mathbf A_1=\frac12\mathbf a\times\mathbf b$, $\mathbf A_2=\frac12\mathbf b\times\mathbf c$ and $\mathbf A_3=\frac12\mathbf c\times\mathbf a$. Vector algebra gives $\mathbf A_1\cdot(\mathbf A_2\times\mathbf A_3)=\frac18[\mathbf a\cdot(\mathbf b\times\mathbf c)]^2$, and the volume is $V=|\mathbf a\cdot(\mathbf b\times\mathbf c)|/6$. Hence

```math
\sum_{i=1}^4\mathbf A_i=0,\qquad
V^2=\frac29\,\big|\mathbf A_1\cdot(\mathbf A_2\times\mathbf A_3)\big|.
```

In loop quantum gravity and in spin-foam models each area vector becomes an operator proportional to an angular momentum, $\mathbf A_i=8\pi\gamma l_P^2\,\mathbf J_i$. Here $l_P$ is the Planck length and $\gamma$ the Barbero--Immirzi parameter. Face $i$ carries a spin $j_i$, so its area $8\pi\gamma l_P^2\sqrt{j_i(j_i+1)}$ is sharp. The condition $\sum_i\mathbf J_i=0$ selects the rotation-invariant states of four spins. Their number is the number of ways to couple the four spins to total spin zero. The products $\mathbf J_1\cdot\mathbf J_2$ and $\mathbf J_1\cdot\mathbf J_3$ measure angles between face normals. With $[J^a,J^b]=i\epsilon^{abc}J^c$ and $\hbar=1$, their commutator is

```math
[\mathbf J_1\cdot\mathbf J_2,\,\mathbf J_1\cdot\mathbf J_3]=i\,\mathbf J_1\cdot(\mathbf J_2\times\mathbf J_3)\equiv iQ,\\
V=(8\pi\gamma l_P^2)^{3/2}\sqrt{\tfrac29\,|Q|}.
```

Two angles commute only on states of zero volume. A quantum tetrahedron with volume therefore has an uncertainty relation between its dihedral angles, as a spin has between its components. Its classical shape exists only as a mean value. The relative spread of the angles decreases as the spins grow.

The smallest case has four faces of spin $1/2$. Two pairs of spin-$1/2$ faces couple to total spin zero in two independent ways, so the shape space is two-dimensional. Let faces 1 and 2 couple to spin $k\in\{0,1\}$. Then $\mathbf J_1\cdot\mathbf J_2=[k(k+1)-3/2]/2$ takes the values $-3/4$ and $1/4$. The operator $Q$ has eigenvalues $\pm\sqrt3/4$, one for each orientation. Both give the volume $V\approx0.31\,(8\pi\gamma)^{3/2}l_P^3$, about $4.5\,l_P^3$ for $\gamma=0.2375$. In either volume eigenstate $\mathbf J_1\cdot\mathbf J_2$ has mean $-1/4$ and variance $1/4$: the angle is maximally uncertain.

The numerical prefactor of the volume depends on how the operator is regularized on a graph. The vanishing of $Q$ at nodes with fewer than four faces does not. The calculation is kinematical: it concerns one tetrahedron at one instant, before any dynamics of general relativity is imposed. Gluing quantum tetrahedra gives the four-valent nodes of a spin network, and their histories are summed in spin foam models. Whether these discrete spectra describe physical space depends on that dynamics, which remains open, and on the value of $\gamma$ discussed under loop quantum gravity.

## References For The Physical Derivation

- [A. Barbieri, Quantum tetrahedra and simplicial spin networks; area vectors as spin operators, volume formula and the angle uncertainty relation.](https://arxiv.org/abs/gr-qc/9707010)
- [J. C. Baez and J. W. Barrett, The Quantum Tetrahedron in 3 and 4 Dimensions; Hilbert space of a quantum tetrahedron from geometric quantization.](https://arxiv.org/abs/gr-qc/9903060)
