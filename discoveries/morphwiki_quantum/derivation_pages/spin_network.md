# Spin network

In a lattice gauge theory, a line of electric flux gives a definite flux through every surface it pierces and none through surfaces it misses. Loop quantum gravity gives space the same structure. Area belongs to lines that pierce a surface, and volume to points where several lines meet. The states with this property are spin networks, built like lattice gauge fields but with the group $SU(2)$ on an arbitrary graph. Each edge $e$ of a graph $\Gamma$ carries a spin $j_e$. Each node $n$ carries an intertwiner $\iota_n$, a tensor that couples the spins meeting there to total spin zero. The state depends on the connection $A$ through the holonomies $h_e$ along the edges:

```math
\Psi_{\Gamma,j,\iota}[A]=\Big(\bigotimes_n\iota_n\Big)\cdot\Big(\bigotimes_e D^{(j_e)}\big(h_e[A]\big)\Big),\qquad
h_e=\mathcal P\exp\int_eA.
```

Here $D^{(j)}$ is the spin-$j$ matrix of a group element, and the dot contracts each matrix index with an index of an intertwiner. Gauge transformations act at the nodes and rotate the indices of all edges meeting there. The state is invariant because each intertwiner is a rotation-invariant tensor. Whether such a tensor exists, and how many independent ones exist, follows from the addition of angular momenta.

The simplest graph is a closed loop with one two-valent node. Two spins couple to total spin zero only if they are equal, and then in exactly one way. The intertwiner is the identity map between the two edges, so the node can be removed. The state is the Wilson loop $\operatorname{Tr}D^{(j)}(h_\gamma)$ of the spin-$j$ representation around the loop $\gamma$. An edge of spin $1/2$ cannot join an edge of spin $1$ at a two-valent node: no invariant exists. The spin along a line therefore changes only where a third edge meets it. At a three-valent node the spins must satisfy $|j_1-j_2|\leq j_3\leq j_1+j_2$ with an integer sum. The intertwiner is again unique, a Clebsch--Gordan coefficient. Four spin-$1/2$ edges admit two independent intertwiners.

Geometric operators act on these states locally. For a surface $S$ crossed by edges at points $p$, with no node on the surface, the area is diagonal. The volume of a region $R$ is a sum of contributions from the nodes inside it:

```math
\hat A(S)\,\Psi=8\pi\gamma l_P^2\sum_{p\in S\cap\Gamma}\sqrt{j_p(j_p+1)}\;\Psi,\qquad
\hat V(R)\,\Psi=\sum_{n\in R}\hat V_n\Psi.
```

Here $\gamma$ is the Barbero--Immirzi parameter and $l_P$ the Planck length. Each crossing contributes the square root of the Casimir operator of its edge. Consider a loop of spin $j$ that crosses a closed surface twice. The area eigenvalue is $16\pi\gamma l_P^2\sqrt{j(j+1)}$. For $j=1/2$ and $\gamma=0.2375$ this is $8\sqrt3\pi\gamma l_P^2\approx10.3\,l_P^2$. The volume of the loop is zero. A node contributes volume only if at least four edges meet there with tangents not all in one plane. For three edges, the triple product of their generators vanishes on the unique invariant state.

The loop therefore carries area but no volume. It is a flux line of geometry, in the same way that a Wilson line in lattice gauge theory is a line of electric flux. The triad measured by the area plays the part of the electric field, and its square gives the Casimir. These statements are kinematical. They hold on the state space before the Hamiltonian constraint is imposed. Diffeomorphism invariance makes only the combinatorics and knotting of the graph physical, not its coordinates. The four-valent node is worked out as the quantum tetrahedron under quantum geometry. The area spectrum and the value of $\gamma$ are discussed under loop quantum gravity.

## References For The Physical Derivation

- [C. Rovelli and L. Smolin, Spin Networks and Quantum Gravity; spin-network basis of loop quantum gravity.](https://arxiv.org/abs/gr-qc/9505006)
- [J. C. Baez, Spin Network States in Gauge Theory; holonomies, intertwiners and gauge-invariant states on graphs.](https://arxiv.org/abs/gr-qc/9411007)
- [C. Rovelli and L. Smolin, Discreteness of area and volume in quantum gravity; area and volume spectra on spin-network states.](https://arxiv.org/abs/gr-qc/9411005)
