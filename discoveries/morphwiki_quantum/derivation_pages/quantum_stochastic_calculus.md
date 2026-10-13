# Quantum stochastic calculus

Light leaks out of an optical cavity through a partly transmitting mirror. The emerging beam carries the cavity field, and the same mirror admits vacuum fluctuations from outside. Quantum stochastic calculus describes this exchange with the external field in infinitesimal time steps, in the way Itô calculus describes classical noise.

Treat the external field as a sequence of independent time bins of length $dt$ that pass the mirror one after another. Let $b_{\mathrm{in}}(t)$ be the incoming field operator, with $[b_{\mathrm{in}}(t),b_{\mathrm{in}}^\dagger(t')]=\delta(t-t')$. Define the increment $dA_t=\int_t^{t+dt}b_{\mathrm{in}}(s)\,ds$. For an incoming vacuum, products of increments obey the quantum Itô table:

```math
dA_t\,dA_t^\dagger=dt,\qquad dA_t^\dagger\,dA_t=dA_t\,dA_t=dA_t^\dagger\,dA_t^\dagger=0,
\qquad dt\,dA_t=0.
```

The asymmetry between the two orderings is the vacuum noise. Creating and then removing a quantum in an empty bin leaves a term proportional to $dt$, whereas the reverse order gives zero. A classical Wiener increment gives $dW^2=dt$ for either order. For a thermal input with mean occupation $N$, the table becomes $dA\,dA^\dagger=(N+1)\,dt$ and $dA^\dagger dA=N\,dt$.

Let the system couple to the field through an operator $L$, for example $L=\sqrt\kappa\,a$ for a cavity mode $a$ with energy decay rate $\kappa$. Hudson and Parthasarathy showed that the joint unitary evolution of system and field obeys

```math
dU_t=\Big[-\Big(\frac{i}{\hbar}H+\frac12L^\dagger L\Big)dt
+L\,dA_t^\dagger-L^\dagger dA_t\Big]U_t.
```

The term $-\frac12L^\dagger L\,dt$ is required by unitarity. In $d(U^\dagger U)=dU^\dagger U+U^\dagger dU+dU^\dagger dU$, the last product contributes $L^\dagger L\,dA\,dA^\dagger=L^\dagger L\,dt$, which cancels it exactly. Averaging over the vacuum field gives the Lindblad master equation written under quantum jump. The calculus also yields the outgoing field: it equals the incoming field plus the emission of the system,

```math
dA^{\mathrm{out}}_t=L\,dt+dA_t,\qquad
b_{\mathrm{out}}=b_{\mathrm{in}}+\sqrt\kappa\,a.
```

For a cavity driven through the same mirror by a coherent beam of amplitude $\beta$, detuned by $\Delta$ from resonance, the mean cavity field obeys $\dot a=-(i\Delta+\kappa/2)a-\sqrt\kappa\,\beta$. In the steady state the reflection coefficient is

```math
r(\Delta)=\frac{b_{\mathrm{out}}}{\beta}=\frac{2i\Delta-\kappa}{2i\Delta+\kappa},\qquad
|r|=1,\qquad r(0)=-1.
```

All light returns, as expected for a lossless single-sided cavity, but its phase $\pi-2\arctan(2\Delta/\kappa)$ turns by $2\pi$ across a window of width about $\kappa$. A superconducting qubit that shifts the cavity frequency by $\pm\chi$ therefore imprints reflected phases that differ by $4\arctan(2\chi/\kappa)$. The difference reaches $\pi$ at $\chi=\kappa/2$, where the two reflected coherent states are most distinguishable for a given input flux. Pound--Drever--Hall laser locking uses the same phase near resonance.

The calculus rests on a Markov approximation. The coupling to the external field must be flat in frequency over a band much wider than $\kappa$, and the rotating-wave approximation requires $\kappa$ far below the cavity frequency. Optical cavities and microwave resonators satisfy both conditions well. Structured reservoirs, such as photonic band edges, require a memory kernel instead. Photon counting on the same output field gives the quantum-jump trajectories of quantum optics.

## References For The Physical Derivation

- [K. R. Parthasarathy, Quantum Stochastic Calculus and Quantum Gaussian Processes; the Hudson-Parthasarathy calculus on boson Fock space.](https://arxiv.org/abs/1408.5686)
- [J. Combes, J. Kerckhoff and M. Sarovar, The SLH framework for modeling quantum input-output networks; quantum stochastic differential equations and input-output relations.](https://arxiv.org/abs/1611.00375)
- [A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt and R. J. Schoelkopf, Introduction to Quantum Noise, Measurement and Amplification; cavity input-output theory and dispersive qubit measurement.](https://arxiv.org/abs/0810.4729)
