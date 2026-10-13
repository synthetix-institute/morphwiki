# Qubit

A trapped ion, the polarization of a photon and the lowest two levels of a superconducting circuit each provide two states that can be prepared, rotated and distinguished. Whether such a pair works as a qubit depends on how strictly the dynamics stays within the two states. It also depends on how long their relative phase survives. Within the chosen pair a pure state is

```math
\ket\psi=\alpha\ket0+\beta\ket1,\qquad |\alpha|^2+|\beta|^2=1,\qquad
p(0)=|\langle0|\psi\rangle|^2=|\alpha|^2,\qquad p(1)=|\beta|^2.
```

A global phase has no observable effect, so a pure state is fixed by two real numbers: the population ratio and the relative phase. These coordinates form the Bloch sphere described for the quantum state. A measurement in the basis $\{\ket0,\ket1\}$ returns one of two outcomes and removes the relative phase. The continuous amplitudes therefore cannot be read off in one shot. If a bit is encoded in one of two pure states with equal prior probability, any measurement errs with probability at least the Helstrom bound:

```math
P_{\rm err}=\frac12\left(1-\sqrt{1-|\langle\psi_0|\psi_1\rangle|^2}\right).
```

Orthogonal states give zero error, while an overlap $|\langle\psi_0|\psi_1\rangle|=\cos(\pi/8)$ gives 0.31. More generally, Holevo's theorem limits the classical information retrievable from one qubit to one bit, despite the continuum of states. A previously shared entangled pair raises this to two bits in superdense coding.

A superconducting transmon shows what restricting a system to two levels involves. It is a weakly anharmonic oscillator whose lowest transition frequency $\omega_{01}/2\pi$ typically lies between 4 and 6 GHz. The next transition is lower by an anharmonicity $|\eta|/2\pi$ of about 200 to 300 MHz. A control pulse at $\omega_{01}$ also drives the transition from $\ket1$ to $\ket2$, detuned by $\eta$. By the off-resonant Rabi formula of the two-state quantum system, this leakage stays small only when the drive strength and the pulse bandwidth are well below $|\eta|$. Single-qubit gates therefore last tens of nanoseconds.

Relaxation sets the second limit. Energy decay from $\ket1$ to $\ket0$ at rate $1/T_1$, together with additional pure dephasing at rate $\Gamma_\phi$, gives in the Markovian regime at zero temperature

```math
\rho_{11}(t)=\rho_{11}(0)e^{-t/T_1},\qquad |\rho_{01}(t)|=|\rho_{01}(0)|e^{-t/T_2},
\qquad \frac{1}{T_2}=\frac{1}{2T_1}+\Gamma_\phi.
```

The factor one half follows from the decay itself. The amplitude of $\ket1$ falls as $e^{-t/2T_1}$, and the coherence $\rho_{01}$ is proportional to that amplitude. Hence $T_2\leq2T_1$, with equality when energy decay is the only process. An echo experiment measures $T_2$ from the decay of the recovered phase coherence. Comparing it with $T_1$ from a population decay separates loss of energy from loss of phase. Quantum error correction encodes one logical qubit in several physical ones so that errors of both kinds can be detected and reversed.

## References For The Physical Derivation

- [P. Krantz and colleagues, A Quantum Engineer's Guide to Superconducting Qubits; transmon anharmonicity, leakage, gate times, T1 and T2.](https://arxiv.org/abs/1904.06560)
- [J. Koch and colleagues, Charge-Insensitive Qubit Design Derived from the Cooper Pair Box; the transmon and its level structure.](https://arxiv.org/abs/cond-mat/0703002)
- [D. P. DiVincenzo, The Physical Implementation of Quantum Computation; requirements on a physical two-level system used as a qubit.](https://arxiv.org/abs/quant-ph/0002077)
