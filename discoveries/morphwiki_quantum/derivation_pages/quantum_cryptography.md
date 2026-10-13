# Quantum cryptography

A banknote that cannot be copied needs a physical feature that no measurement reproduces. Classical features can in principle always be measured precisely and copied. Around 1970 Stephen Wiesner proposed storing, together with a serial number, qubits prepared in randomly chosen states. The proposal, published in 1983, later led to quantum key distribution. Its security rests on the no-cloning theorem.

Suppose a unitary $U$ copied two states onto a blank qubit, $U|\psi\rangle|0\rangle=|\psi\rangle|\psi\rangle$ and $U|\phi\rangle|0\rangle=|\phi\rangle|\phi\rangle$. Unitary maps preserve inner products, so

```math
\langle\psi|\phi\rangle=\langle\psi|\phi\rangle^2\quad\Longrightarrow\quad
\langle\psi|\phi\rangle\in\{0,1\}.
```

Copying is possible only for orthogonal or identical states. For $|0\rangle$ and $|+\rangle=(|0\rangle+|1\rangle)/\sqrt2$ the overlap $1/\sqrt2$ differs from its square $1/2$, so no device copies both. An ancilla or an intermediate measurement does not help. Any physical operation is a unitary on a larger system, and the same inner-product argument applies there.

In Wiesner's scheme the bank prepares each of $n$ qubits in one of the four states $|0\rangle$, $|1\rangle$, $|+\rangle$ and $|-\rangle$, chosen at random. It keeps the list of choices secret under the serial number of the note. To verify a note, the bank measures each qubit in its recorded basis, and a genuine note passes with certainty.

A counterfeiter with one note tries to produce two notes that both pass. The simplest attack measures each qubit in the $Z$ basis and prepares two copies of the outcome. With the right basis both copies pass; with the wrong basis each copy passes with probability one half. The success probabilities per qubit, and for a whole note, are

```math
p_{\rm meas}=\frac12\cdot1+\frac12\cdot\frac14=\frac58,\qquad p_{\rm opt}=\frac34,\qquad
P_{\rm forge}=\Big(\frac34\Big)^n.
```

The optimum over all physical operations, $3/4$ per qubit, was found by Molina, Vidick and Watrous (2012) using semidefinite programming over channels from one qubit to two. A dual bound and an explicit attack both give $3/4$. They also showed that entangled attacks on several qubits do no better than independent ones. A note of $n=50$ qubits is therefore forged with probability $(3/4)^{50}\approx6\times10^{-7}$.

The scheme assumes that only the bank verifies notes and that the bases stay secret. If the bank hands back notes that fail verification, repeated queries reveal the states one qubit at a time (Lutomirski, 2010). Even returning only valid notes permits an attack based on interaction-free measurement. Issuing a fresh note after every verification removes both attacks. A practical bank must also tolerate a small fraction of failed qubits, which raises the forging probability by an amount fixed by the tolerated error.

Notes that anyone could verify without the secret list, public-key quantum money, cannot be secure against unbounded adversaries. Proposed constructions rely on computational assumptions whose security against quantum attacks is still being tested. The four Wiesner states and their trade-off between information and disturbance reappear in BB84 quantum key distribution. The counterfeiter's operation is a quantum channel from one qubit to two, constrained by complete positivity.

## References For The Physical Derivation

- [A. Molina, T. Vidick and J. Watrous, Optimal counterfeiting attacks and generalizations for Wiesner's quantum money; the optimal success probability (3/4)^n.](https://arxiv.org/abs/1202.4010)
- [A. Brodutch, D. Nagaj, O. Sattath and D. Unruh, An adaptive attack on Wiesner's quantum money; attacks when valid notes are returned, based on interaction-free measurement.](https://arxiv.org/abs/1404.1507)
- [A. Broadbent and C. Schaffner, Quantum Cryptography Beyond Quantum Key Distribution; quantum money and other cryptographic tasks.](https://arxiv.org/abs/1510.06120)
