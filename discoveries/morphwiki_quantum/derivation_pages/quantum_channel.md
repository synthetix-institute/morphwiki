# Quantum channel

An excited atom in free space emits a photon that flies away undetected. The state of the atom afterwards follows from the joint unitary evolution of atom and radiation field, after which the field is ignored. Let $|g\rangle$ and $|e\rangle$ be the ground and excited states, let the field start in its vacuum $|0\rangle_E$, and let $\Gamma$ be the spontaneous emission rate. During a time $t$ the excitation leaves the atom with probability $\gamma=1-e^{-\Gamma t}$:

```math
U|g\rangle|0\rangle_E=|g\rangle|0\rangle_E,\qquad
U|e\rangle|0\rangle_E=\sqrt{1-\gamma}\,|e\rangle|0\rangle_E+\sqrt{\gamma}\,|g\rangle|1\rangle_E.
```

Tracing out the field gives the density operator of the atom alone. Each orthogonal field state $|k\rangle_E$ contributes one term, with the Kraus operator $K_k={}_E\langle k|U|0\rangle_E$. Unitarity of $U$ makes the Kraus operators complete, which is conservation of probability. Any later measurement with operators $M_y$ then has outcome probabilities $p(y)=\operatorname{Tr}[M_y\mathcal E(\rho)]$:

```math
\mathcal E(\rho)=\sum_k K_k\rho K_k^\dagger,\qquad \sum_k K_k^\dagger K_k=I,\\
K_0=|g\rangle\langle g|+\sqrt{1-\gamma}\,|e\rangle\langle e|,\qquad K_1=\sqrt{\gamma}\,|g\rangle\langle e|.
```

In the basis $(|g\rangle,|e\rangle)$ this amplitude-damping channel moves population downward and shrinks the coherence by a smaller factor:

```math
\mathcal E\begin{pmatrix}\rho_{gg}&\rho_{ge}\\ \rho_{eg}&\rho_{ee}\end{pmatrix}
=\begin{pmatrix}\rho_{gg}+\gamma\rho_{ee}&\sqrt{1-\gamma}\,\rho_{ge}\\
\sqrt{1-\gamma}\,\rho_{eg}&(1-\gamma)\rho_{ee}\end{pmatrix}.
```

The excited population decays as $e^{-\Gamma t}$, while the coherence decays as $\sqrt{1-\gamma}=e^{-\Gamma t/2}$. Energy relaxation alone therefore gives a coherence time $T_2=2T_1$, with $T_1=1/\Gamma$. Measured atomic and superconducting qubits obey $T_2\leq2T_1$, and any shortfall comes from additional dephasing, such as slow fluctuations of the transition frequency. Two successive damping intervals compose as $1-\gamma=(1-\gamma_1)(1-\gamma_2)$, consistent with the exponential law.

The Kraus operators are not unique. A random phase flip $Z$ applied with probability $p$ and an unrecorded measurement in the $Z$ basis made with probability $2p$ produce the same channel. Both multiply the coherence by $1-2p$. Two Kraus sets of one channel are always related by a unitary mixing of their operators. Physically, this corresponds to measuring the discarded environment in a different basis.

A channel must remain physical when its input is entangled with an untouched partner, and positivity of $\mathcal E(\rho)$ for single inputs does not ensure this. Matrix transposition $T$ maps every density operator to a density operator. Applied to one half of the Bell state $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$, however, it gives

```math
(\mathrm{id}\otimes T)\big(|\Phi^+\rangle\langle\Phi^+|\big)=\tfrac12\,\mathrm{SWAP},
\qquad \text{eigenvalues } \tfrac12,\tfrac12,\tfrac12,-\tfrac12.
```

The negative eigenvalue would be a negative probability, so no physical process acts as a transposition. The test generalizes: a linear map is completely positive exactly when its Choi matrix $\sum_{ij}|i\rangle\langle j|\otimes\mathcal E(|i\rangle\langle j|)$ is positive. For amplitude damping the eigenvalues are $0$, $0$, $\gamma$ and $2-\gamma$.

The description assumes that the atom and field start uncorrelated and that emitted light never returns. A mirror that reflects the photon back to the atom violates both conditions and makes the evolution depend on its history. Over a short interval, $\gamma=\Gamma\,dt$ turns $K_1$ into the jump operator of the quantum jump description. Quantum error correction asks which channels of this kind can be undone on an encoded subspace.

## References For The Physical Derivation

- [M. M. Wilde, From Classical to Quantum Shannon Theory; Kraus and Stinespring representations, complete positivity, the Choi criterion and the amplitude-damping channel.](https://arxiv.org/abs/1106.1445)
