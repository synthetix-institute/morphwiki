# Quantum bus

Two superconducting qubits on a chip, several millimetres apart, have no direct coupling. Both can couple to one microwave resonator that runs between them. When the qubits are detuned from the resonator, it is excited only virtually, yet it transmits an exchange interaction between them. The resonator then acts as a quantum bus, as demonstrated by Majer and colleagues in 2007.

Let qubits $j=1,2$ have transition frequencies $\omega_j$ and couplings $g_j$ to a resonator mode $a$ of frequency $\omega_r$, with detunings $\Delta_j=\omega_j-\omega_r$. With $\hbar=1$ and the rotating-wave approximation, the Tavis--Cummings Hamiltonian is

```math
H=\omega_ra^\dagger a+\sum_{j=1,2}\Big[\frac{\omega_j}{2}\sigma_z^{(j)}
+g_j\big(a\sigma_+^{(j)}+a^\dagger\sigma_-^{(j)}\big)\Big].
```

Consider the dispersive regime $|\Delta_j|\gg g_j$. The state $|e,g,0\rangle$, with the excitation on qubit 1, couples to $|g,e,0\rangle$ only through the intermediate state $|g,g,1\rangle$. In that state the photon sits in the resonator. The amplitude leaves qubit 1 with strength $g_1$, pays the energy denominator $\Delta$, and arrives at qubit 2 with strength $g_2$. Second-order perturbation theory, or a Schrieffer--Wolff transformation, eliminates the resonator. With the resonator in its vacuum,

```math
H_{\rm eff}=\sum_j\frac{\omega_j+\chi_j}{2}\sigma_z^{(j)}
+J\big(\sigma_+^{(1)}\sigma_-^{(2)}+\sigma_-^{(1)}\sigma_+^{(2)}\big),\\
\chi_j=\frac{g_j^2}{\Delta_j},\qquad J=\frac{g_1g_2}{2}\Big(\frac{1}{\Delta_1}+\frac{1}{\Delta_2}\Big).
```

For equal detunings $\Delta_1=\Delta_2=\Delta$ the exchange rate is $J=g_1g_2/\Delta$. The shifts $\chi_j$ also move each qubit frequency. When the shifted frequencies coincide, an excitation prepared on qubit 1 oscillates to qubit 2:

```math
P_{1\to2}(t)=\sin^2(Jt),\qquad t_{\rm swap}=\frac{\pi}{2J}.
```

With $g/2\pi=100$ MHz and $\Delta/2\pi=1$ GHz, the exchange is $J/2\pi=10$ MHz, and a full transfer takes $25$ ns. Exact diagonalization of the three single-excitation states gives a splitting within 2 percent of $2J$ for these values. At $\Delta=5g$ the deviation grows to 7 percent, a correction of relative order $(g/\Delta)^2$. Stopping the transfer halfway, at $t=\pi/(4J)$, produces an entangling gate of the $\sqrt{i\mathrm{SWAP}}$ type. Detuning the qubits from each other by much more than $J$ switches the exchange off, because it no longer conserves energy.

The derivation needs $g_j\ll|\Delta_j|$ and a resonator photon number below the critical value $n_{\rm crit}=\Delta^2/(4g^2)$. Terms dropped in the rotating-wave approximation contribute with denominators $\omega_j+\omega_r$ and are small when $|\Delta_j|\ll\omega_j+\omega_r$. The bus also costs coherence. Resonator loss at rate $\kappa$ makes each qubit decay at the Purcell rate $\kappa g^2/\Delta^2$.

Beyond the vacuum, the qubit frequency shift becomes $\chi(2a^\dagger a+1)$, so the resonator frequency depends on the qubit state. A microwave tone transmitted through the resonator then measures the qubit without exchanging energy with it. The bus is the Jaynes--Cummings coupling of quantum optics applied to two qubits at once, and it supplies two-qubit gates for a quantum circuit.

## References For The Physical Derivation

- [J. Majer, J. M. Chow, J. M. Gambetta, J. Koch and colleagues, Coupling Superconducting Qubits via a Cavity Bus; resonator-mediated exchange between two transmons.](https://arxiv.org/abs/0709.2135)
- [A. Blais, A. L. Grimsmo, S. M. Girvin and A. Wallraff, Circuit Quantum Electrodynamics; dispersive regime, exchange coupling, critical photon number and Purcell decay.](https://arxiv.org/abs/2005.12667)
