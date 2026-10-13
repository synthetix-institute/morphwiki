# Measurement in quantum mechanics

A Stern--Gerlach magnet sends silver atoms up or down according to their spin, and a screen records where each atom lands. The spin is never observed directly. It is inferred from a position that the magnet has correlated with it.

Von Neumann's model makes this correlation explicit. Let the measured observable be $A=\sum_aa|a\rangle\langle a|$, and let a pointer have position $q$, momentum $p_q$ and initial wave function $\phi(q)$ of width $\sigma$. A brief interaction $H=g(t)A\otimes p_q$ with total strength $G=\int g\,dt$ translates the pointer by an amount proportional to the eigenvalue:

```math
e^{-iGA\otimes p_q/\hbar}\sum_ac_a|a\rangle\phi(q)
=\sum_ac_a|a\rangle\phi(q-Ga).
```

Finding the pointer at $q$ then has probability density $\sum_a|c_a|^2|\phi(q-Ga)|^2$, a sum of displaced pointer profiles. When $G$ times the eigenvalue spacing greatly exceeds $\sigma$, the peaks separate and outcome $a$ occurs with probability $|c_a|^2$. When the peaks overlap, the record yields only partial information about $A$. The corresponding effects $\sum_a|\phi(q-Ga)|^2|a\rangle\langle a|$ form a POVM rather than a set of projectors.

The same coupling disturbs the system. Tracing over the pointer multiplies each coherence $\rho_{aa'}$ of the system by the overlap of the two displaced pointer states. For a Gaussian pointer,

```math
\rho_{aa'}\;\longmapsto\;\rho_{aa'}\exp\!\left[-\frac{G^2(a-a')^2}{8\sigma^2}\right].
```

Resolution and disturbance are therefore controlled by the same ratio $G|a-a'|/\sigma$. A pointer that separates two eigenvalues cleanly removes the coherence between them, and with it the interference that observables not commuting with $A$ would show. The diagonal elements are untouched because the interaction commutes with $A$. This is the quantum nondemolition condition: an immediate repetition returns the same eigenvalue.

In the Stern--Gerlach magnet, the field gradient $B'$ couples the spin component $\sigma_z$ to the transverse position $z$ through the energy $\mu_BB'z\sigma_z$, with $\mu_B$ the Bohr magneton. The pointer is the transverse momentum, shifted by $\pm\mu_BB'\tau$ during the transit time $\tau$. For silver atoms at 500 m/s in a 3.5 cm magnet with $B'=10^3$ T/m, the two components separate by about 0.25 mm at the exit. This is comparable to the splitting seen in 1922.

The momentum kick far exceeds the momentum spread of a collimated beam. The interference between the spin components is therefore lost, and restoring it would require undoing the kick to within that spread. The update that follows a recorded outcome is discussed under wave function collapse. Continuous monitoring of an emitting atom, in which the pointer is the radiation field, leads to the quantum jump description.

## References For The Physical Derivation

- [A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt and R. J. Schoelkopf, Introduction to Quantum Noise, Measurement and Amplification; von Neumann pointer model, back-action and quantum limits.](https://arxiv.org/abs/0810.4729)
