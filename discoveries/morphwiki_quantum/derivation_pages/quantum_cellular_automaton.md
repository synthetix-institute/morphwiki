# Quantum cellular automaton

A particle hops on a lattice in discrete time steps, and its internal two-level state is rotated before each hop. It spreads in a way no classical random walk can. The rule is local, identical at every site and unitary. Such rules define quantum cellular automata: lattices of finite-dimensional cells updated by one global unitary $U$ that is translation invariant and causal. Causality means that for any operator $A_x$ on cell $x$, the evolved operator $U^\dagger A_xU$ acts only on a fixed neighbourhood of $x$.

The simplest automaton carries one particle with a two-level internal state, the coin. Each step applies a coin rotation $C(\theta)$ and then moves the particle one site right if the coin points up and one site left if it points down. Translation invariance lets plane waves with quasimomentum $k$ evolve independently:

```math
U(k)=\begin{pmatrix}e^{-ik}&0\\0&e^{ik}\end{pmatrix}C(\theta),\qquad
C(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}.
```

Since $\det U(k)=1$, its eigenvalues are $e^{\pm i\omega(k)}$ with $2\cos\omega=\operatorname{Tr}U(k)$. The dispersion relation and the group velocity follow directly:

```math
\cos\omega(k)=\cos\theta\cos k,\qquad v(k)=\frac{d\omega}{dk}=\frac{\cos\theta\sin k}{\sin\omega(k)}.
```

The group velocity reaches its largest value $\cos\theta$ at $k=\pi/2$. The shift itself imposes a strict light cone of one site per step. A particle started at one site has a flat distribution of $k$, and both bands share the same $v^2$. Its spread therefore grows ballistically, with a coefficient set by the average of $v^2$ over the Brillouin zone:

```math
\frac{\langle x^2\rangle}{t^2}\ \xrightarrow{\ t\to\infty\ }\ \frac{1}{2\pi}\int_{-\pi}^{\pi}v(k)^2\,dk=1-|\sin\theta|,
\qquad\text{classical walk: }\langle x^2\rangle=t.
```

For the balanced coin $\theta=\pi/4$, whose spreading equals that of the Hadamard walk, the standard deviation is $\sigma\approx0.54\,t$. After 100 steps the distribution is about 54 sites wide, against 10 sites for an unbiased classical random walk. A direct simulation of 400 steps gives $\sigma/t=0.5412$, and no probability appears outside the light cone. Karski and colleagues (2009) implemented such a walk with single neutral atoms in a spin-dependent optical lattice and imaged the final distribution site by site.

Near $k=0$ and for small $\theta$, the dispersion becomes $\omega^2\approx k^2+\theta^2$. With lattice spacing $a$ and time step $\tau$ this is the relativistic relation $E^2=p^2c^2+m^2c^4$, with $c=a/\tau$ and $mc^2=\hbar\theta/\tau$. The automaton is a discretization of the one-dimensional Dirac equation that keeps exact unitarity and a strict light cone.

For many interacting cells the same definition applies. Schumacher and Werner showed that every such automaton is obtained from two layers of blockwise unitaries in a generalized Margolus partitioning of the lattice. In one dimension, an index measures the net flow of quantum information through the lattice (Gross, Nesme, Vogts and Werner). A shift of qubits by one cell has index 2, while every finite-depth circuit of local gates on fixed cells has index 1. A translation is therefore local and reversible, yet no such circuit produces it. The classification in three and more dimensions remains open.

The strict light cone is the discrete counterpart of the Lieb--Robinson bound for lattice Hamiltonians. A digital quantum simulator built from Trotter steps is a circuit of the same layered form, and its gates act within the same kind of light cone.

## References For The Physical Derivation

- [P. Arrighi, An overview of Quantum Cellular Automata; definitions by causality and translation invariance, quantum walks and Dirac limits.](https://arxiv.org/abs/1904.12956)
- [D. Gross, V. Nesme, H. Vogts and R. F. Werner, Index theory of one dimensional quantum walks and cellular automata; the index that separates shifts from local circuits.](https://arxiv.org/abs/0910.3675)
- [M. Karski, L. Forster, J.-M. Choi, A. Steffen, W. Alt, D. Meschede and A. Widera, Quantum Walk in Position Space with Single Optically Trapped Atoms; a walk of single atoms in a spin-dependent optical lattice with site-resolved imaging.](https://arxiv.org/abs/0907.1565)
