# Operator theory

The energy of an electron in an atom can take arbitrarily large values, while a spin-1/2 component never exceeds $\hbar/2$ in magnitude. Operator theory distinguishes these cases as unbounded and bounded operators. The distinction decides which mathematical statements hold, and it explains why a hydrogen atom does not collapse.

The norm $\|A\|$ is the largest factor by which $A$ can stretch a unit vector. For an observable it is the largest magnitude of an outcome. A bounded operator acts on every state. An unbounded symmetric operator, such as the kinetic energy, cannot act on every state. By the Hellinger--Toeplitz theorem, a symmetric operator defined everywhere is bounded.

Position and momentum cannot both be bounded. Suppose $[A,B]=cI$ with $c\neq0$. Induction gives $[A,B^n]=ncB^{n-1}$. Taking norms of both sides yields

```math
n|c|\,\|B^{n-1}\|\leq2\|A\|\,\|B\|\,\|B^{n-1}\|.
```

No power of $B$ vanishes, because $B^{n-1}=0$ would force $B^{n-2}=0$ and so on down to $I=0$. Dividing by $\|B^{n-1}\|$ gives $n\leq2\|A\|\|B\|/|c|$ for every $n$, which is impossible. This argument of Wielandt holds in infinite dimensions; the finite-dimensional trace argument appears under the canonical commutation relation. Canonical pairs therefore require unbounded operators, and with them stated domains.

In hydrogen, $H=p^2/2m-k/r$ with $k=e^2/(4\pi\varepsilon_0)$. The Coulomb term is unbounded below, and a classical electron would radiate and spiral into the nucleus. The kinetic energy controls the singularity through Hardy's inequality, valid for wave functions in three dimensions:

```math
\int|\nabla\psi|^2d^3x\geq\frac14\int\frac{|\psi|^2}{r^2}\,d^3x
\quad\Longrightarrow\quad
H\geq\frac{\hbar^2}{8mr^2}-\frac{k}{r}\geq-\frac{2mk^2}{\hbar^2}.
```

The last step minimizes the function of $r$ at $r=\hbar^2/(4mk)$. The bound equals four rydbergs below zero, $-54.4$ eV, compared with the exact ground energy of $-13.6$ eV. It is not sharp, but it proves that the energy is bounded below. Compressing the wave function raises its kinetic energy faster than the Coulomb attraction lowers its potential energy.

The same comparison shows that the Coulomb term is small relative to the kinetic energy. The Kato--Rellich theorem then makes $H$ self-adjoint on the domain of the kinetic energy, as Kato proved for atoms in 1951. The evolution $e^{-iHt/\hbar}$ is therefore uniquely defined.

The argument fails for stronger singularities. For $V=-g/r^2$, Hardy's inequality gives $H\geq0$ when $g\leq\hbar^2/(8m)$. For larger $g$ the energy is unbounded below, and the Hamiltonian needs an extra condition at the origin to define the dynamics. A point electric dipole produces an inverse-square potential with angular dependence. It can bind an electron only above a critical moment of about 1.63 debye. The relativistic kinetic energy $\sqrt{p^2c^2+m^2c^4}$ grows only linearly with momentum. A Coulomb potential of nuclear charge $Ze$ then keeps the energy bounded below only for $Z\alpha\leq2/\pi$. Self-adjointness and spectral theory build on these estimates.

## References For The Physical Derivation

- [F. Gieres, Mathematical surprises and Dirac's formalism in quantum mechanics; unbounded operators, domains and the canonical commutation relation.](https://arxiv.org/abs/quant-ph/9907069)
- [E. H. Lieb, The Stability of Matter and Quantum Electrodynamics; stability of the hydrogen atom and of matter, with and without relativistic kinetic energy.](https://arxiv.org/abs/math-ph/0209034)
