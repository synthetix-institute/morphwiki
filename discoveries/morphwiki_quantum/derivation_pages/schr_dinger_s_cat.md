# Schrödinger's cat

In 1935 Schrödinger imagined a cat sealed in a chamber with a radioactive atom, a Geiger counter and a flask of poison. If the atom decays, the counter releases a hammer that breaks the flask. After the time at which the decay probability is one half, linear evolution of the whole system gives

```math
\ket\Psi=\frac{1}{\sqrt2}\left(\ket{u}\ket{\rm alive}+\ket{d}\ket{\rm dead}\right),
```

where $\ket u$ and $\ket d$ are the undecayed and decayed atom. Schrödinger presented the state as an absurd consequence of applying the wave function to everyday objects. Two physical questions remain: which observation would distinguish this state from a mixture of living and dead cats, and why no such observation succeeds.

Only interference can make the distinction, because it responds to the element $\ket{\rm alive}\bra{\rm dead}$ of the density matrix, and that element is fragile. A laboratory version replaces the cat by a microwave cavity field in a superposition of two coherent states of opposite phase, $\ket\beta+\ket{-\beta}$ up to normalization. The mean photon number is $\bar n=|\beta|^2$. Photons leak out at the energy decay rate $\kappa$. Leakage acts as a weak beam splitter between the cavity and the outside field, and a coherent state divides into two coherent states:

```math
\ket{\pm\beta}_{\rm cav}\ket0_{\rm out}\;\longrightarrow\;
\ket{\pm\beta e^{-\kappa t/2}}_{\rm cav}\,\ket{\pm\beta\sqrt{1-e^{-\kappa t}}}_{\rm out}.
```

Each component leaves its own coherent state in the outside field. Their overlap, $\langle-\gamma|\gamma\rangle=e^{-2|\gamma|^2}$, multiplies the coherence between the components, as for any record left in an environment. With $|\gamma|^2=\bar n(1-e^{-\kappa t})$ and $\beta_t=\beta e^{-\kappa t/2}$, the weight $C$ of the coherence terms $\ket{\pm\beta_t}\bra{\mp\beta_t}$ relative to the population terms becomes

```math
C(t)=\exp\!\left[-2\bar n\left(1-e^{-\kappa t}\right)\right]
\approx e^{-2\bar n\kappa t}\quad(\kappa t\ll1).
```

Each component loses energy at rate $\kappa$, but the coherence between them disappears $2\bar n$ times faster. The rate grows with the squared separation $|2\beta|^2$ of the components in phase space. Coherence falls to $e^{-2}$ once a single photon, on average, has escaped, whatever the size of $\bar n$. Brune, Haroche and colleagues in Paris observed this progressive decoherence in 1996, using fields of a few photons probed by Rydberg atoms. Components further apart lost their coherence faster.

For a massive object the environment is usually scattered gas molecules or thermal radiation. In the quantum Brownian motion model, with relaxation rate $\gamma$ and temperature $T$, a superposition of two positions a distance $\Delta x$ apart loses coherence at the rate

```math
\tau_D^{-1}=\gamma\left(\frac{\Delta x}{\lambda_{\rm th}}\right)^2,\qquad
\lambda_{\rm th}=\frac{\hbar}{\sqrt{2mk_BT}}.
```

For a mass of one gram at 300 K, $\lambda_{\rm th}\approx4\times10^{-23}$ m, and a separation of 1 cm gives $\tau_D\approx10^{-41}/\gamma$. The formula assumes high temperature and a separation shorter than the wavelength of the environmental particles. For larger separations each collision resolves the position, and the rate saturates at the collision rate. Either estimate puts decoherence far below any time on which the motion of the object could be observed.

Decoherence explains why the alive and dead components cannot be made to interfere, and why the record forms in macroscopic configurations. It does not state which component is found. The reduced density matrix of the cat becomes indistinguishable from a mixture, while the global state remains a superposition under unitary evolution. Whether a further physical process selects one outcome, as objective-collapse models propose, is the measurement problem. Interference with ever larger molecules and mechanical oscillators continues to constrain such models.

## References For The Physical Derivation

- [W. H. Zurek, Decoherence and the Transition from Quantum to Classical, Revisited; decoherence time of a macroscopic superposition in quantum Brownian motion.](https://arxiv.org/abs/quant-ph/0306072)
- [S. Deléglise and colleagues, Reconstruction of Non-Classical Cavity Field States with Snapshots of Their Decoherence; cat states of a microwave cavity field and their decay.](https://arxiv.org/abs/0809.1064)
