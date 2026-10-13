# QBism

*Historical, bibliographic or interpretive entry.*

Two experimenters with different information about how a spin was prepared may assign it different density operators. QBism, the quantum-Bayesian interpretation developed by Carlton Caves, Christopher Fuchs and Rüdiger Schack from about 2002, takes this as the general case. A quantum state is an agent's personal degrees of belief about the outcomes of that agent's own future actions on a system. The outcomes are the agent's experiences. The formalism is unchanged; what changes is the meaning of a state assignment.

QBists read the Born rule as a consistency condition linking probabilities for different experiments, comparable to the rules that keep a gambler's bets coherent. Fuchs and Schack made this explicit with a symmetric informationally complete measurement (SIC). In dimension $d$ it has $d^2$ outcomes $H_i=\Pi_i/d$, whose rank-one projectors satisfy $\operatorname{Tr}(\Pi_i\Pi_j)=1/(d+1)$ for $i\neq j$. The probabilities $p(i)$ of this reference measurement fix the state completely. For any other measurement with outcomes $D_j$, the Born rule becomes

```math
q(j)=\sum_{i=1}^{d^2}\Bigl[(d+1)\,p(i)-\frac1d\Bigr]\,r(j|i),\qquad
r(j|i)=\operatorname{Tr}(\Pi_iD_j) .
```

Here $r(j|i)$ is the probability of $D_j$ if the reference measurement had been performed and had given $i$. A classical agent would use the law of total probability, $q(j)=\sum_ip(i)\,r(j|i)$. The quantum rule differs by the factor $d+1$ and the shift $1/d$, and QBism takes these numbers as the empirical content of quantum theory. For a qubit the four SIC states point to the corners of a regular tetrahedron on the Bloch sphere.

On this reading, a measurement on one member of an entangled pair updates only the measuring agent's expectations about the distant member. No physical influence travels, and QBists describe quantum mechanics as local. Critics reply that this leaves open why the Born rule succeeds and what the world is like apart from agents. QBism predicts no measured statistics different from standard quantum mechanics. Readers can continue with Born rule, POVM, Quantum state and Measurement problem.

## References For The Physical Derivation

- [C. A. Fuchs, N. D. Mermin and R. Schack, An Introduction to QBism with an Application to the Locality of Quantum Mechanics; the interpretation and its account of entangled correlations.](https://arxiv.org/abs/1311.5253)
- [C. A. Fuchs and R. Schack, Quantum-Bayesian Coherence: The No-Nonsense Version; the Born rule written with a SIC reference measurement.](https://arxiv.org/abs/1301.3274)
