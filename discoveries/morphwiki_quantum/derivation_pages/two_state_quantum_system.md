# Two-state quantum system

An avoided crossing couples two states that would otherwise evolve independently. In their basis, a constant energy offset contributes only an overall phase, whereas the remaining Hamiltonian determines both transition probabilities and phase evolution. Let $\Delta$ be the angular-frequency detuning between the uncoupled levels and $\Omega$ a real coupling frequency. With $|0\rangle$ and $|1\rangle$ the eigenstates of $\sigma_z$, choose

```math
H=\frac{\hbar}{2}(\Delta\sigma_z+\Omega\sigma_x),\qquad \omega_R=\sqrt{\Delta^2+\Omega^2}.
```

The Pauli algebra gives $(\Delta\sigma_z+\Omega\sigma_x)^2=\omega_R^2I$. Every higher power in the exponential therefore reduces to either the identity or the Hamiltonian. The evolution follows without fitting a transition curve:

```math
U(t)=\cos\frac{\omega_Rt}{2}\,I-i\sin\frac{\omega_Rt}{2}\,
\frac{\Delta\sigma_z+\Omega\sigma_x}{\omega_R}.
```

For the preparation $|0\rangle$, the off-diagonal matrix element of $U$ gives the transition probability

```math
P_{0\to1}(t)=\frac{\Omega^2}{\Delta^2+\Omega^2}
\sin^2\!\left(\frac{t}{2}\sqrt{\Delta^2+\Omega^2}\right).
```

On resonance the coupling can transfer the entire population; a pulse of duration $\pi/|\Omega|$ interchanges the levels. Detuning increases the oscillation frequency but reduces the greatest achievable population transfer. These two consequences distinguish a changed level splitting from a changed coupling even when a short segment of an oscillation looks similar.

The Bloch vector rotates about the effective axis $(\Omega,0,\Delta)$. A second pulse about another axis can convert a relative phase into a population difference. Reversing two such pulses generally changes the result because their Hamiltonians do not commute. The state space is the same in both experiments; the difference lies in the sequence of interactions, and the measured population exposes that difference.

This calculation applies to any isolated pair of levels governed by the stated Hamiltonian, including two coupled modes or selected atomic states. Its use for a larger physical system requires that other levels remain unpopulated and environmental relaxation be negligible over the pulse duration. If the Hamiltonian was obtained in a rotating frame, the rotating-wave approximation and the transformation of the measured operator are additional parts of the correspondence. Specifying a two-dimensional matrix does not by itself establish those conditions in a device.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)
