# Measurement problem

A detector whose pointer can swing left or right interacts with a spin prepared in a superposition of up and down. Linear quantum dynamics applied to spin and detector predicts a superposition of both pointer positions. Each actual run shows one.

Suppose the detector works correctly on the basis states. Starting in a ready state $|A_0\rangle$, the interaction $U$ produces $|{\uparrow}\rangle|A_\uparrow\rangle$ from $|{\uparrow}\rangle|A_0\rangle$ and $|{\downarrow}\rangle|A_\downarrow\rangle$ from $|{\downarrow}\rangle|A_0\rangle$. Linearity then fixes its action on any superposition:

```math
U(\alpha|{\uparrow}\rangle+\beta|{\downarrow}\rangle)|A_0\rangle
=\alpha|{\uparrow}\rangle|A_\uparrow\rangle+\beta|{\downarrow}\rangle|A_\downarrow\rangle.
```

Adding an observer, a camera or a printer extends this correlation to more systems without ending it. The Born rule assigns the probabilities $|\alpha|^2$ and $|\beta|^2$, but the evolution contains no step at which one term is selected.

Decoherence explains part of what is seen. Air molecules and thermal photons scatter from the pointer and acquire states that depend on its position. With environment states $|E_\uparrow\rangle$ and $|E_\downarrow\rangle$, the reduced state of spin and pointer becomes

```math
\rho_{SA}=|\alpha|^2|{\uparrow}A_\uparrow\rangle\langle{\uparrow}A_\uparrow|
+|\beta|^2|{\downarrow}A_\downarrow\rangle\langle{\downarrow}A_\downarrow|\\
+\left(\alpha\beta^*\Gamma|{\uparrow}A_\uparrow\rangle\langle{\downarrow}A_\downarrow|+{\rm h.c.}\right),
\qquad \Gamma=\langle E_\downarrow|E_\uparrow\rangle.
```

If $N$ independent scatterers each leave states with overlap $c$, then $\Gamma=c^N$. With $c=\cos0.1\approx0.995$ and $N=10^4$, $|\Gamma|\approx2\times10^{-22}$, so interference between pointer positions cannot be detected on spin and pointer alone. The pointer basis is selected by the interaction, here position, because scattering depends on where the pointer is.

Decoherence does not select an outcome. The global state still contains both terms, and $\rho_{SA}$ is a reduced description of an entangled state, not a list of which outcome occurred. The measurement problem is that unitary evolution alone yields neither single records nor their probabilities; both enter as separate assumptions. Interpretations divide on how to supply the missing step: by keeping all branches, by adding particle positions, or by changing the dynamics.

The last option makes predictions. In the Ghirardi--Rimini--Weber model each nucleon is spontaneously localized to a length $r_C\approx10^{-7}$ m at a rate $\lambda\approx10^{-16}$ s$^{-1}$. For a pointer whose $N$ nucleons are displaced by more than $r_C$, one localization of any nucleon collapses the whole superposition:

```math
\Gamma_{\rm collapse}=N\lambda\approx10^{23}\times10^{-16}\,{\rm s^{-1}}=10^{7}\,{\rm s^{-1}}.
```

A single nucleon is localized about once in $3\times10^8$ years, while a macroscopic pointer resolves within 0.1 microsecond. The modified dynamics also predicts slight heating and spontaneous radiation. Interferometry with massive molecules and searches for this radiation bound $\lambda$ at each $r_C$. Current upper bounds on $\lambda$ at $r_C=10^{-7}$ m remain above the original value, so the model is constrained but not excluded. Schrödinger's cat poses the same problem for a larger system.

## References For The Physical Derivation

- [M. Schlosshauer, Decoherence, the measurement problem, and interpretations of quantum mechanics; pointer states and what decoherence does not resolve.](https://arxiv.org/abs/quant-ph/0312059)
- [A. Bassi, K. Lochan, S. Satin, T. P. Singh and H. Ulbricht, Models of Wave-function Collapse, Underlying Theories, and Experimental Tests; GRW amplification and experimental bounds.](https://arxiv.org/abs/1204.4325)
