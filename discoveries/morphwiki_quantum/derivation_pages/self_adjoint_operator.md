# Self-adjoint operator

A charged particle circulates in a thin ring threaded by magnetic flux. Its momentum values shift with the flux, although the field vanishes where the particle moves. The shift enters through a boundary condition. That boundary condition is exactly what makes the momentum operator self-adjoint.

Let $P=-i\hbar\,d/dx$ act on wave functions on an interval $[0,L]$. Integration by parts leaves a boundary term:

```math
\langle\phi|P\psi\rangle-\langle P\phi|\psi\rangle
=-i\hbar\bigl[\phi^*(L)\psi(L)-\phi^*(0)\psi(0)\bigr].
```

On functions that vanish at both ends the term is zero, so $P$ is symmetric and its expectation values are real. It is not self-adjoint, however. Its adjoint acts on all differentiable functions without any boundary condition, and on that larger domain every $e^{ipx/\hbar}$ with complex $p$ is an eigenfunction. The spectrum of such an operator is not a set of real outcomes.

The deficiency indices measure the mismatch. Count the normalizable solutions of $P^\dagger\psi=\pm i\kappa\psi$ for a fixed $\kappa>0$; they are $e^{\mp\kappa x/\hbar}$. A symmetric operator has self-adjoint extensions only when the two counts $n_\pm$ are equal. The extensions are then labelled by unitary maps between the two solution spaces:

```math
[0,L]:\ (n_+,n_-)=(1,1),\qquad \psi(L)=e^{i\theta}\psi(0),\qquad
p_k=\frac{\hbar(2\pi k+\theta)}{L},\\
[0,\infty):\ (1,0),\ \text{no extension};\qquad
\mathbb R:\ (0,0),\ \text{unique}.
```

On the interval each phase $\theta$ defines a different self-adjoint momentum with its own real spectrum, $k$ an integer. On a ring threaded by flux $\Phi$, a gauge transformation moves the vector potential into this boundary condition, with $\theta=2\pi\Phi/\Phi_0$ and $\Phi_0=h/e=4.14\times10^{-15}$ weber. The energies $p_k^2/2m$ are periodic in the flux with period $\Phi_0$; this is the Aharonov--Bohm effect. Persistent currents in mesoscopic metal rings show this flux period. In a single ring, disorder, temperature and the many electrons of a metal reduce the current amplitude, while the period $h/e$ remains.

On the half line the counts differ, and no self-adjoint momentum exists. A translation toward the wall would push probability through the wall, so no unitary translation group exists there. Stone's theorem then provides no self-adjoint generator. The momentum of a particle confined to $x>0$ can be measured only as a generalized observable.

The kinetic energy on the half line behaves differently, with indices $(1,1)$. Its extensions impose $\psi'(0)=-\psi(0)/b$ for real $b$, with the Dirichlet condition as the limit $b\to0$. For $b>0$ the function $e^{-x/b}$ is a bound state with energy $-\hbar^2/(2mb^2)$, describing a short-range attraction at the wall. On a finite box the kinetic energy has indices $(2,2)$, a family of conditions that includes the Dirichlet, Neumann and periodic cases compared in spectral theory.

Self-adjointness is required for two physical reasons. Only self-adjoint operators have spectral decompositions with real outcomes, and only they generate unitary evolution. Symmetry alone, real expectation values on a restricted domain, provides neither. The choice of domain is part of the physical description of the system, as in the treatments of observables and of the mathematical formulation.

## References For The Physical Derivation

- [G. Bonneau, J. Faraut and G. Valent, Self-adjoint extensions of operators and the teaching of quantum mechanics; momentum and Hamiltonian extensions on an interval and on the half line.](https://arxiv.org/abs/quant-ph/0103153)
- [A. C. Bleszynski-Jayich and colleagues, Persistent currents in normal metal rings: comparing high-precision experiment with theory; flux-periodic currents in single rings and arrays.](https://arxiv.org/abs/0906.4780)
