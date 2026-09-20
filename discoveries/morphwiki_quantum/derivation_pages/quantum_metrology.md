# Quantum metrology

A sensor estimates a physical parameter from how that parameter changes a prepared state. Sensitivity depends on the interaction that encodes the parameter, on the fluctuations of its generator in the preparation, and on the measurement used to distinguish nearby states. Entanglement is useful only when it improves this complete estimation problem.

Let a dimensionless parameter $\theta$ be encoded by $|\psi_\theta\rangle=e^{-i\theta G}|\psi_0\rangle$, with Hermitian dimensionless generator $G$. For this pure-state unitary family, the quantum Fisher information is

```math
F_Q=4(\langle G^2\rangle-\langle G\rangle^2),\qquad
\operatorname{Var}\widehat\theta\geq\frac{1}{\nu F_Q}.
```

Here $\nu$ counts independent repetitions and the bound applies to locally unbiased estimation, with attainability requiring a suitable measurement and statistical regime. Large generator variance makes neighboring parameter-dependent states more distinguishable. A state that is an eigenstate of $G$ acquires only an overall phase and has no sensitivity to $\theta$ in this task.

For $N$ spins exposed to the same phase, choose $G=\tfrac12\sum_j Z_j$. Independent spins prepared along $x$ have $F_Q=N$. The coherent superposition $(|0\rangle^{\otimes N}+|1\rangle^{\otimes N})/\sqrt2$ has $F_Q=N^2$, because the two components acquire phases separated by $N\theta$.

```math
\Delta\theta_{\rm product}\geq\frac{1}{\sqrt{\nu N}},\qquad
\Delta\theta_{\rm GHZ}\geq\frac{1}{N\sqrt\nu}.
```

These expressions compare the same single-spin coupling with a counted number of uses. They are not universal bounds for arbitrary many-body Hamiltonians or uncounted preparation resources. The enhanced oscillation also creates phase ambiguities over a broad prior interval, so an estimation scheme must establish which fringe contains the parameter.

Independent dephasing exposes the cost of the collective coherence. If a single-spin off-diagonal element decays as $e^{-\gamma t}$, the coherence between the two GHZ branches decays as $e^{-N\gamma t}$. For phase encoding over a fixed duration this gives $F_Q=N^2e^{-2N\gamma t}$. Increasing $N$ can then reduce rather than improve the usable information. Optimizing frequency estimation further requires counting the interrogation time and available repetitions.

A proposed sensing mechanism must therefore specify what is being estimated and which resources are fixed. The generator identifies the useful preparation, while environmental coupling and measurement determine how much of its distinguishability is available. This makes sensitivity a calculable property of the assembled experiment rather than a consequence of entanglement alone.

## References For The Physical Derivation

- [V. Giovannetti, S. Lloyd and L. Maccone, Quantum metrology; generator fluctuations and counted resources.](https://arxiv.org/abs/quant-ph/0509179)


## Relations In The Original Papers

[arXiv:quant-ph/0509179, S0.EGx4](https://arxiv.org/html/quant-ph/0509179#S0.EGx4). An entangled probe gives an uncertainty bound scaling inversely with the number of uses of the parameter generator. Unitary encoding, counted resources and the estimator assumptions of the source; noise changes the attainable scaling.
