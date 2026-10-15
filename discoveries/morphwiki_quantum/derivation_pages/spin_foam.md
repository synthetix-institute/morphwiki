# Spin foam

The amplitude for a particle to travel between two points is a sum over the paths joining them. Spin foam models apply the same rule to the geometry of space, described at each instant by a spin network. The history of a spin network is a two-dimensional complex whose faces carry spins and whose edges carry rotation-invariant couplings of those spins. In three spacetime dimensions the construction can be checked against classical gravity through the Ponzano--Regge model. Spacetime is triangulated by tetrahedra, and each edge $e$ is labelled by a spin $j_e$. The spin is read as a length $l_e=j_e+1/2$ in units of the three-dimensional Planck length. Up to sign conventions the amplitude is

```math
Z=\sum_{\{j_e\}}\ \prod_e(2j_e+1)\ \prod_t\begin{Bmatrix}j_1&j_2&j_3\\ j_4&j_5&j_6\end{Bmatrix}_t .
```

Here the bracket is the Wigner $6j$ symbol of the six spins on tetrahedron $t$. It is the recoupling coefficient of three angular momenta known from atomic spectroscopy. The factor $2j_e+1$ is the dimension of the spin-$j_e$ representation. The $6j$ symbol vanishes unless each triangle obeys the triangle inequality with an integer sum of spins. Only spins that can form real triangles contribute.

The connection with gravity appears at large spins. Ponzano and Regge found the following asymptotic form, and Roberts later proved it:

```math
\begin{Bmatrix}j_1&j_2&j_3\\ j_4&j_5&j_6\end{Bmatrix}\simeq
\frac{1}{\sqrt{12\pi V}}\cos\Big(\sum_{e=1}^6 l_e\theta_e+\frac\pi4\Big),\qquad l_e=j_e+\tfrac12.
```

Here $V$ is the volume of the Euclidean tetrahedron with edge lengths $l_e$. The angle $\theta_e$ is the exterior dihedral angle at edge $e$, between the outward normals of the two faces that share it. The sum $\sum_el_e\theta_e$ is the Regge action of the tetrahedron. Regge calculus is the discrete form of general relativity, with curvature concentrated on edges as deficit angles. The amplitude is therefore a sum of $e^{iS}$ and $e^{-iS}$ for the two orientations. This is the form expected of a gravitational path integral in the semiclassical limit.

For a regular tetrahedron with all spins equal to $N$, the volume is $V=\frac{l^3}{6\sqrt2}$ with $l=N+1/2$. Every exterior angle is $\pi-\arccos(1/3)\approx1.911$. At $N=20$ the exact $6j$ symbol is $-5.029\times10^{-3}$, and the asymptotic formula gives $-5.034\times10^{-3}$. At $N=40$ the two agree to three parts in $10^4$. The sign changes with $N$ follow the phase $6l\theta$ of the cosine.

In three dimensions gravity has no local propagating degrees of freedom, and the Ponzano--Regge model is a quantization of it. The sum over spins diverges for triangulations with interior vertices. The divergence reflects a residual symmetry and is removed by gauge fixing. With a positive cosmological constant the model is replaced by the finite Turaev--Viro state sum. In four dimensions, models such as that of Engle, Pereira, Rovelli and Livine assign amplitudes to four-simplices. Their large-spin limit again contains the Regge action. Whether sums over many simplices reproduce general relativity, with its gravitational waves, is not established. The boundary states of a spin foam are the spin networks of loop quantum gravity, and each tetrahedron is the quantum tetrahedron described under quantum geometry.

## References For The Physical Derivation

- [J. C. Baez, An Introduction to Spin Foam Models of Quantum Gravity and BF Theory; spin foams as histories of spin networks and the Ponzano-Regge model.](https://arxiv.org/abs/gr-qc/9905087)
- [J. Roberts, Classical 6j-symbols and the tetrahedron; proof of the Ponzano-Regge asymptotic formula.](https://arxiv.org/abs/math-ph/9812013)
- [A. Perez, The Spin Foam Approach to Quantum Gravity; three- and four-dimensional models and their semiclassical limits.](https://arxiv.org/abs/1205.2019)
