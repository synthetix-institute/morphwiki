# Quantum complexity theory

Grover's algorithm finds one marked entry among $N$ with about $(\pi/4)\sqrt N$ queries. Whether a cleverer quantum algorithm could use far fewer is a statement about all possible circuits, not about one of them. Quantum complexity theory answers such questions by fixing a model of computation and counting resources.

The standard model is a uniform family of circuits. For each input length $m$, a classical procedure running in time polynomial in $m$ writes down a circuit of polynomially many gates from a fixed universal set. The circuit acts on the input and on ancillas prepared in $|0\rangle$, and one qubit is measured at the end. A decision problem belongs to BQP, bounded-error quantum polynomial time, when the correct answer appears with probability at least $2/3$ for every input:

```math
\Pr[\text{output}=\text{answer}]\geq\frac23,\qquad
\Pr[\text{majority of }k\text{ runs wrong}]\leq e^{-k/18}.
```

The constant $2/3$ is conventional. Repeating the circuit $k$ times and taking the majority lowers the error exponentially by the Hoeffding inequality, so 373 repetitions bring it below $10^{-9}$. Classical bounded-error probabilistic computation, BPP, is contained in BQP. BQP is contained in PSPACE, because each outcome probability can be computed as a sum over paths using polynomial memory. Factoring lies in BQP through Shor's algorithm and has no known efficient classical algorithm. Whether BQP is strictly larger than BPP is not proven.

Lower bounds can be proven in the query model, where the input is a black box. For search, the oracle $O_x$ flips the sign of the query basis state $|x\rangle$. Any algorithm alternates fixed unitaries with $T$ oracle calls. Compare a run with the oracle for marked entry $x$ against a run in which every oracle call is replaced by the identity. Let $|\psi_t\rangle$ be the state of the second run after $t$ calls, and $\alpha_{x,t}$ the norm of its component with query input $x$, so that $\sum_x|\alpha_{x,t}|^2=1$. One call can separate the two runs by at most $2|\alpha_{x,t}|$, and the Cauchy--Schwarz inequality then bounds the total separation:

```math
\big\|\psi_T^x-\psi_T\big\|\leq2\sum_{t=0}^{T-1}|\alpha_{x,t}|,\qquad
\sum_x\big\|\psi_T^x-\psi_T\big\|^2\leq4T\sum_{t=0}^{T-1}\sum_x|\alpha_{x,t}|^2=4T^2.
```

Success requires that the final state for each $x$ outputs $x$ with probability at least $2/3$. For at least half of the values $x$, the run without a marked entry outputs $x$ with probability at most $2/N$. For each such $x$ the two final states differ in norm by at least $2/3-2/N$, which gives

```math
\frac N2\Big(\frac23-\frac2N\Big)^2\leq4T^2\quad\Longrightarrow\quad
T\geq\sqrt{\frac N8}\Big(\frac23-\frac2N\Big)\approx0.24\sqrt N.
```

For $N=10^6$ entries any quantum algorithm needs at least 236 queries. Grover's algorithm uses 785, and a classical search about $5\times10^5$ on average. The square-root gain is therefore optimal up to a constant factor, and Zalka showed that $(\pi/4)\sqrt N$ is exactly optimal for near-certain success. Grover's algorithm almost saturates the inequality: for $N=1024$ and 25 iterations the sum of squared separations is 2032, against the bound 2500.

This hybrid argument is due to Bennett, Bernstein, Brassard and Vazirani (1997). It shows that unstructured search admits no exponential quantum speedup. It also yields an oracle relative to which NP is not contained in BQP, although the unrelativized question remains open. Problems with algebraic structure escape the argument; period finding in Shor's algorithm is the standard example. The matching upper bound is the amplitude-amplification angle under quantum algorithm, and the polynomial-size condition counts gates of a quantum circuit.

## References For The Physical Derivation

- [C. H. Bennett, E. Bernstein, G. Brassard and U. Vazirani, Strengths and Weaknesses of Quantum Computing; the hybrid argument and the square-root lower bound for search.](https://arxiv.org/abs/quant-ph/9701001)
- [C. Zalka, Grover's quantum searching algorithm is optimal; the exact constant pi/4 for near-certain success.](https://arxiv.org/abs/quant-ph/9711070)
- [J. Watrous, Quantum Computational Complexity; uniform circuit families, BQP and its relations to classical classes.](https://arxiv.org/abs/0804.3401)
