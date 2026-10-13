# Density matrix

Nuclear spins in a slightly inhomogeneous magnet are tipped by a radio-frequency pulse into the plane perpendicular to the field. The induced signal decays quickly, yet a second pulse can bring it back. Over this time each spin evolves unitarily, precessing at its own local frequency. The decay and the return belong to the ensemble, and the density matrix is the state that describes it.

If a source prepares the pure state $\ket{\psi_a}$ with probability $p_a$, every measurement probability is linear in these weights. Collecting the weights in one operator gives

```math
\rho=\sum_a p_a\ket{\psi_a}\bra{\psi_a},\qquad \rho\geq0,\qquad \operatorname{Tr}\rho=1,
\qquad p(i)=\operatorname{Tr}(\rho P_i),
```

where $P_i$ projects onto outcome $i$. Positivity and unit trace make every such probability nonnegative and their sum one. In a chosen basis the diagonal elements are populations and the off-diagonal elements are coherences; only the coherences produce interference between the basis states. Different ensembles with the same $\rho$ give identical statistics, as described for the quantum state. The purity separates a single pure preparation from a mixture, and for an isolated system $\rho$ obeys the von Neumann equation:

```math
\operatorname{Tr}\rho^2=\sum_{a,b}p_ap_b|\langle\psi_a|\psi_b\rangle|^2\leq1,
\qquad i\hbar\frac{d\rho}{dt}=[H,\rho].
```

The purity equals one only when all prepared states coincide up to a phase. In the energy basis the von Neumann equation keeps the populations fixed and rotates each coherence at its Bohr frequency, $\rho_{mn}(t)=\rho_{mn}(0)e^{-i(E_m-E_n)t/\hbar}$. Unitary evolution of the ensemble therefore preserves its purity.

Now take spin-one-half nuclei that the pulse has left polarized along $x$ with polarization $P$, so that each has $\rho_{01}=P/2$ in the $\sigma_z$ basis. In thermal nuclear magnetic resonance $P$ is small, but it only scales the signal. A nucleus whose local precession frequency differs from the reference by $\delta$ has Hamiltonian $\hbar\delta\sigma_z/2$ in the rotating frame, and its coherence becomes $\tfrac P2e^{-i\delta t}$. If $\delta$ is Gaussian distributed across the sample with standard deviation $\sigma$, the ensemble average is

```math
\rho_{01}(t)=\tfrac P2\langle e^{-i\delta t}\rangle=\tfrac P2e^{-\sigma^2t^2/2},\qquad
\operatorname{Tr}\rho^2=\tfrac12\left(1+P^2e^{-\sigma^2t^2}\right).
```

The transverse magnetization is proportional to $|\rho_{01}|$, so the signal decays on the time $\sqrt2/\sigma$. A frequency spread $\sigma/2\pi=1$ kHz gives 0.23 ms. The ensemble loses purity although every member evolves unitarily. A $\pi$ pulse about $x$ at time $\tau$ exchanges $\rho_{01}$ and $\rho_{10}$, so the phase acquired afterwards cancels the phase acquired before. At $2\tau$ every member returns to $\rho_{01}=P/2$ whatever its $\delta$. This is the Hahn spin echo.

The echo is complete only if each detuning stays constant over the interval $2\tau$. Diffusion of the spins through the field gradient, or coupling to other degrees of freedom, leaves an irreversible decay of the echo. That remaining loss is quantum decoherence: the phase has moved into correlations with an environment. A mixed state of the same kind arises whenever a subsystem is entangled with an unmeasured partner, and then $\rho_A=\operatorname{Tr}_B\rho_{AB}$. At a single time the two origins can give the same density matrix. Only a further operation, such as the echo pulse, separates them.

## References For The Physical Derivation

- [M. M. Wilde, From Classical to Quantum Shannon Theory; density operators, ensembles, purity and partial trace.](https://arxiv.org/abs/1106.1445)
- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states as positive trace-class operators and the trace rule.](https://arxiv.org/abs/1508.06951)
