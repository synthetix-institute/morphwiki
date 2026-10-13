# Schrödinger picture

Two atomic levels are swept through an avoided crossing by a ramped electric field. If the sweep is slow, the atom ends in the other diabatic level; if it is fast, the atom stays where it started. A prediction for a Hamiltonian that changes in time is most directly written for a time-dependent state, which is the Schrödinger picture.

In this picture observables, such as a level projector, stay fixed, and the state carries all the time dependence. For a Hamiltonian $H(t)$, the evolution operator obeys $i\hbar\,\partial_tU(t,t_0)=H(t)U(t,t_0)$. When Hamiltonians at different times do not commute, the solution is a time-ordered exponential:

```math
|\psi(t)\rangle=U(t,t_0)|\psi(t_0)\rangle,\qquad
U(t,t_0)=\mathcal T\exp\Big[-\frac{i}{\hbar}\int_{t_0}^{t}H(s)\,ds\Big].
```

The ordering symbol $\mathcal T$ places operators at later times to the left. Expanding it gives the Dyson series, the starting point of time-dependent perturbation theory. Without the ordering, the exponential gives wrong predictions whenever $[H(s),H(s')]\neq0$. A measurement at an intermediate time is applied to the state at that time, so a sequence of operations is followed in the order in which it occurs.

For the swept atom, let $|1\rangle$ and $|2\rangle$ be the diabatic states, whose energies cross linearly in time at rate $\alpha$, and let $\Delta$ be the minimum gap set by their coupling. Then

```math
H(t)=\frac12\big(\alpha t\,\sigma_z+\Delta\,\sigma_x\big),\qquad
P_{1\to1}=\exp\Big(-\frac{\pi\Delta^2}{2\hbar\alpha}\Big).
```

Here $\sigma_z$ and $\sigma_x$ are Pauli matrices in the diabatic basis, and $P_{1\to1}$ is the probability of remaining in $|1\rangle$ after the crossing. Landau, Zener, Stückelberg and Majorana obtained this result in 1932 by solving the time-dependent equation exactly. For a sweep of duration $t$ centred on the crossing, the naive exponential of the integrated Hamiltonian would give a rotation about $x$ by the angle $\Delta t/\hbar$. That prediction oscillates with the duration and does not depend on the sweep rate.

For a slow sweep, $\hbar\alpha\ll\Delta^2$, the state follows the instantaneous eigenstate, whose character changes from $|1\rangle$ to $|2\rangle$; this adiabatic passage transfers the population completely. For a fast sweep the state cannot follow and remains in $|1\rangle$. In frequency units the exponent is $\pi^2f_\Delta^2/\dot\nu$, where $f_\Delta=\Delta/h$ and $\dot\nu$ is the sweep rate. A gap of 10 MHz crossed at $1\,\mathrm{GHz}/\mu\mathrm s$ leaves 37 percent in the initial diabatic state.

Rubbmark, Kash, Littman and Kleppner measured this dependence with Rydberg atoms in 1981, and superconducting qubits reproduce it with swept flux. To lowest order in $\Delta$ the transition probability is $\pi\Delta^2/2\hbar\alpha$, which is what time-dependent perturbation theory gives. In the slow limit the diabatic probability vanishes faster than any power of $\alpha$, so no finite order of an expansion in the sweep rate captures it.

The formula assumes an isolated pair of levels and a sweep extending far beyond the crossing time, the larger of $\Delta/\alpha$ and $\sqrt{\hbar/\alpha}$. Finite sweeps add small oscillations, and dephasing during the passage reduces the adiabatic transfer. The Heisenberg picture yields the same probabilities, but its equations contain $U^\dagger H(t)U$ and therefore require the same time-ordered evolution. The position-space form of the same evolution law is the Schrödinger equation.

## References For The Physical Derivation

- [S. N. Shevchenko, S. Ashhab and F. Nori, Landau-Zener-Stuckelberg interferometry; the Landau-Zener transition probability, adiabatic and fast limits, and realizations with qubits.](https://arxiv.org/abs/0911.1917)
