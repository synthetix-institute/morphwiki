# Quantum information

A sender encodes bits in single photons, horizontal polarization for 0 and diagonal polarization for 1. The two states overlap, so no detector distinguishes them with certainty. The physical question is how many bits per photon a receiver can extract, measuring the photons one at a time or jointly.

The uncertainty of a preparation is measured by the von Neumann entropy of its density operator $\rho$. For a qubit with Bloch vector $\mathbf r$, as in the treatment of the quantum state, the eigenvalues are $(1\pm|\mathbf r|)/2$. Hence

```math
S(\rho)=-\operatorname{Tr}\rho\log_2\rho,\qquad S=h_2\Big(\frac{1+|\mathbf r|}{2}\Big),\\
h_2(q)=-q\log_2q-(1-q)\log_2(1-q).
```

A pure state has zero entropy and the maximally mixed qubit has one bit. Schumacher compression gives the entropy an operational meaning. Long sequences from a source of pure states with average $\rho$ can be stored in $S(\rho)$ qubits per signal.

Let letter $x$ occur with probability $p_x$ and be sent as the state $\rho_x$. The receiver's system is then described by $\rho=\sum_xp_x\rho_x$, and a measurement yields an outcome $Y$ correlated with $X$. Holevo's bound limits their classical mutual information:

```math
I(X{:}Y)\leq\chi=S(\rho)-\sum_xp_xS(\rho_x)\leq\log_2d.
```

The argument has two steps. Record the letter in a classical register, giving the joint state $\sum_xp_x|x\rangle\langle x|\otimes\rho_x$. Evaluating the entropies of this block-diagonal state shows that its quantum mutual information $S(X)+S(Q)-S(XQ)$ equals $\chi$. A measurement is a physical operation on the system alone, and mutual information cannot increase under local operations. This data-processing inequality follows from strong subadditivity of the entropy. After the measurement the quantity becomes the classical $I(X{:}Y)$. The second inequality uses $S(\rho)\leq\log_2d$ for a $d$-dimensional system and $S(\rho_x)\geq0$. A qubit therefore conveys at most one bit, although its pure states form a continuous sphere.

For the two polarizations sent with equal probability, the overlap is $s=|\langle0|+\rangle|=1/\sqrt2$. The average state has eigenvalues $(1\pm s)/2$, and the pure signals have zero entropy. For one photon at a time, the best measurement is the symmetric projective one that minimizes the error, with error probability $P_e=[1-(1-s^2)^{1/2}]/2$. It turns each photon into a binary symmetric channel:

```math
\chi=h_2\Big(\frac{1+s}{2}\Big)=0.601,\qquad
I_{\rm single}=1-h_2(P_e)=0.399\ \text{bits}.
```

A numerical search over all projective measurements and random three-outcome measurements finds no single-photon value above 0.399 bits. The gap to 0.601 bits is physical. Long code words built from the two states, measured jointly, reach any rate below $\chi$ with vanishing error; this is the Holevo--Schumacher--Westmoreland theorem. The additional 0.2 bits per photon therefore require measurements that entangle many photons, not better single-photon detectors.

The bound concerns the system that actually reaches the receiver. In superdense coding one transmitted qubit carries two bits. The receiver, however, already holds the other half of an entangled pair, and the bound for the two-qubit system is $\log_24=2$. Quantum teleportation performs the reverse trade, two classical bits and a shared pair for one qubit. In quantum key distribution the same quantity $\chi$, evaluated for an eavesdropper's probe, bounds what that probe reveals about the key.

## References For The Physical Derivation

- [J. Preskill, Quantum Shannon Theory; von Neumann entropy, compression, accessible information and the Holevo bound.](https://arxiv.org/abs/1604.07450)
- [M. M. Wilde, From Classical to Quantum Shannon Theory; data processing, the Holevo bound and the Holevo--Schumacher--Westmoreland theorem.](https://arxiv.org/abs/1106.1445)
