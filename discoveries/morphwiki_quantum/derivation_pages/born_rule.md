# Born rule

A spin prepared up along $z$ enters a Stern--Gerlach magnet tilted by an angle $\theta$. Each atom lands in one of two spots. Over many atoms, the fraction in the upper spot approaches $\cos^2(\theta/2)$, although no single run reveals that number.

The spin state up along the tilted axis $\mathbf n$ is $\cos(\theta/2)|{\uparrow}\rangle+\sin(\theta/2)|{\downarrow}\rangle$. Its inner product with the prepared state is the amplitude $\cos(\theta/2)$, and the Born rule assigns probability equal to its squared modulus. For a density operator $\rho$ and an outcome projector $P_k$ the same rule reads

```math
p_+=|\langle{+_{\mathbf n}}|{\uparrow_z}\rangle|^2=\cos^2\frac{\theta}{2},\qquad
p(k)=\operatorname{Tr}(\rho P_k).
```

The rule refers to relative frequencies in repeated, identically prepared runs. For $N$ independent atoms the observed fraction scatters about $p$ with standard deviation $\sqrt{p(1-p)/N}$. At $\theta=120^\circ$, $p=1/4$, and $10^4$ atoms fix the fraction to about $\pm0.004$. Comparing such fractions at many angles tests the rule, provided detector efficiency and background are calibrated independently.

The squared modulus is not an arbitrary choice. Gleason's theorem states that, in a space of dimension three or more, any assignment of probabilities to projectors must take the form $\operatorname{Tr}(\rho P)$. The assumption is that probabilities add over mutually orthogonal projectors and do not depend on which other projectors are measured alongside. The rule thus follows from the projector structure and this additivity, not from the Schrödinger equation.

A sharp consequence concerns interference among more than two paths. Let $a$, $b$ and $c$ be the amplitudes at one screen point from three slits $A$, $B$ and $C$. Write $P_{AB}$ for the probability with slits $A$ and $B$ open, and so on. Expanding the squared moduli gives

```math
|a+b+c|^2=|a|^2+|b|^2+|c|^2+2\operatorname{Re}(a^*b+b^*c+a^*c),\\
I_3=P_{ABC}-P_{AB}-P_{BC}-P_{AC}+P_A+P_B+P_C=0.
```

Every cross term appears once in $P_{ABC}$ and once in a two-slit pattern, so the combination $I_3$ cancels identically. A rule in which probability were a higher power of the amplitude would leave a third-order interference term. Sinha and colleagues measured the patterns for every combination of open slits, using single photons and three slits. They bounded the three-path term below one percent of the two-path interference.

The cancellation assumes that opening a slit only adds an amplitude. Near-field paths that loop between neighbouring open slits violate this assumption slightly. Within ordinary quantum mechanics they produce a small nonzero $I_3$, which precise tests must subtract.

For unsharp detectors the projector is replaced by a positive effect, as described under POVM. The sharp case, with orthogonal projectors that sum to the identity, is described under projection-valued measure. Wave interference supplies the amplitudes; the Born rule converts them into counting rates.

## References For The Physical Derivation

- [U. Sinha, C. Couteau, T. Jennewein, R. Laflamme and G. Weihs, Ruling Out Multi-Order Interference in Quantum Mechanics; three-slit bound on third-order interference.](https://arxiv.org/abs/1007.4193)
- [R. D. Sorkin, Quantum Mechanics as Quantum Measure Theory; hierarchy of sum rules in which quantum probabilities have only pairwise interference.](https://arxiv.org/abs/gr-qc/9401003)
