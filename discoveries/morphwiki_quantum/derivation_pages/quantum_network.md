# Quantum network

Telecom fiber at a wavelength of 1550 nm attenuates light by about 0.2 decibels per kilometre. One photon in a hundred survives 100 km, and one in $10^{20}$ survives 1000 km. Entanglement between distant laboratories cannot simply be amplified on the way, because amplifying an unknown quantum state adds noise, as the quantum amplifier shows. Quantum networks instead combine heralded short links, quantum memories and entanglement swapping.

For attenuation $\alpha$ in decibels per kilometre, the transmission over length $L$ is $\eta=10^{-\alpha L/10}=e^{-L/L_{\rm att}}$, with $L_{\rm att}\approx22$ km for $\alpha=0.2$. A source emitting pairs at rate $R_0$ delivers $\eta R_0$ of them. Pirandola and colleagues proved a stronger statement for a pure-loss channel. Without intermediate stations, no protocol distributes entanglement faster than

```math
R\leq-\log_2(1-\eta)\approx1.44\,\eta\quad\text{ebits per channel use}\qquad(\eta\ll1).
```

For a 10 GHz source and 1000 km this allows about $10^{-10}$ pairs per second, roughly one pair every two centuries. Loss lowers the rate but need not lower the quality of delivered pairs. If the arrival of a photon is detected and announced, failed attempts are discarded. Imperfect sources, memory dephasing and dark counts lower instead the fidelity $F=\langle\Phi^+|\rho|\Phi^+\rangle$ with the Bell state $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$. A common model is the Werner state $\rho=F|\Phi^+\rangle\langle\Phi^+|+(1-F)(I-|\Phi^+\rangle\langle\Phi^+|)/3$.

Entanglement swapping joins two links. Node B holds one qubit entangled with A and another entangled with C. A Bell measurement on the two qubits at B projects A and C onto a Bell state labelled by the outcome, by the same expansion as in quantum teleportation. A Pauli correction then gives $|\Phi^+\rangle$. For Werner links of fidelities $F_1$ and $F_2$, direct evaluation gives

```math
F_{AC}=F_1F_2+\frac{(1-F_1)(1-F_2)}{3},\qquad w_{AC}=w_1w_2,\qquad w=\frac{4F-1}{3}.
```

The parameter $w$ multiplies along a chain. With $F=0.95$ per link, eight links give $F=0.68$ and sixteen give $0.499$. A Werner state with $F\leq1/2$ is separable, because its partial transpose is then positive. Long chains therefore need entanglement purification, which consumes several noisy pairs to produce fewer pairs of higher fidelity, much as quantum error correction uses redundancy.

Swapping changes the rate scaling when the links are stored. Divide $L$ into $N$ segments with quantum memories at the nodes. Each segment retries until its photon arrives, with success probability $\eta^{1/N}$ per attempt, and a memory holds each success while the other segments retry. Swaps then join the segments, and the rate scales as

```math
R\propto\eta^{1/N},\qquad \eta^{1/8}\approx3\times10^{-3}\ \text{for 1000 km, against}\ \eta=10^{-20}.
```

Factors from waiting for the slowest segment and from the swap success probability multiply this scaling. The memories must stay coherent over many attempts, each lasting at least the signalling time across a segment, about 0.6 ms for 125 km. Bell measurements with linear optics and no auxiliary photons succeed at most half the time, which lowers the rate further.

Hensen and colleagues used this scheme with two electron spins in diamond, 1.3 km apart. Each spin emitted a photon entangled with it, and a Bell measurement on the two photons at a middle station heralded entanglement of the spins. In 245 heralded trials the spins violated the CHSH form of Bell's inequality, with $S=2.42\pm0.20$ against the local bound of 2.

## References For The Physical Derivation

- [S. Pirandola, R. Laurenza, C. Ottaviani and L. Banchi, Fundamental Limits of Repeaterless Quantum Communications; the rate bound for a pure-loss channel.](https://arxiv.org/abs/1510.08863)
- [N. Sangouard, C. Simon, H. de Riedmatten and N. Gisin, Quantum repeaters based on atomic ensembles and linear optics; heralding, memories, swapping and rate scaling.](https://arxiv.org/abs/0906.2699)
- [B. Hensen and colleagues, Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km; event-ready entanglement of distant spins.](https://arxiv.org/abs/1508.05949)
