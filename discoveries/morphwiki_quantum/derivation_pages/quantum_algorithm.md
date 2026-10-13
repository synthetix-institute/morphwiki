# Quantum algorithm

A list of $N$ entries contains one marked entry, and the only access is a test that answers whether a given entry is marked. A classical search needs about $N/2$ tests on average. Grover's algorithm finds the entry with about $(\pi/4)\sqrt N$ tests by rotating a quantum state, step by step, toward the answer.

Hadamard gates prepare a register of $n=\log_2N$ qubits in the uniform superposition $|s\rangle=N^{-1/2}\sum_x|x\rangle$. Let $|w\rangle$ be the marked state and $|r\rangle$ the normalized superposition of the other $N-1$ states. Then $|s\rangle=\sin\theta\,|w\rangle+\cos\theta\,|r\rangle$ with $\sin\theta=1/\sqrt N$. The test acts as a phase oracle $O$ that flips the sign of the marked amplitude, and a second operation $D$ reflects about $|s\rangle$:

```math
O=I-2|w\rangle\langle w|,\qquad D=2|s\rangle\langle s|-I,\qquad G=DO.
```

Both reflections map the plane spanned by $|w\rangle$ and $|r\rangle$ into itself. The oracle reflects about $|r\rangle$ and $D$ reflects about $|s\rangle$. Two reflections about lines separated by the angle $\theta$ combine into a rotation by $2\theta$. After $k$ iterations the state and the probability of finding the marked entry are

```math
G^k|s\rangle=\sin\big((2k+1)\theta\big)|w\rangle+\cos\big((2k+1)\theta\big)|r\rangle,\qquad
P_k=\sin^2\big((2k+1)\theta\big).
```

The probability is nearest one when $(2k+1)\theta\approx\pi/2$, after $k\approx\pi/(4\theta)-1/2\approx(\pi/4)\sqrt N$ iterations. The oracle sign flip is realized with an ancilla in the state $|-\rangle$, by the phase kickback described under quantum circuit. The reflection $D$ equals $H^{\otimes n}(2|0\rangle\langle0|-I)H^{\otimes n}$, a sign flip of the all-zero state between two layers of Hadamards.

For $N=4$ the angle is $\theta=30^\circ$. One iteration gives $(2k+1)\theta=90^\circ$, so the marked entry is found with certainty after a single query. A classical strategy with one query followed by a guess succeeds with probability one half. Chuang, Gershenfeld and Kubinec ran this two-qubit search with nuclear spins in 1998. For $N=2^{20}$, 804 iterations give a success probability above $0.9999997$, against about half a million classical tests on average.

The rotation does not stop at the answer. Continuing beyond the optimum turns the state past $|w\rangle$; for $N=16$, six iterations give a success probability of only $0.02$, while three give $0.96$. The number of marked entries must therefore be known, or estimated from the eigenphases $\pm2\theta$ of $G$ by phase estimation.

The same geometry applies to any preparation circuit $\mathcal A$ that succeeds with probability $a=\sin^2\theta$. Alternating a reflection that flags success with a reflection about $\mathcal A|0\rangle$ raises the success probability close to one:

```math
k\approx\frac{\pi}{4\sqrt a}\ \text{rounds}\qquad\text{instead of}\qquad\sim\frac1a\ \text{classical repetitions}.
```

This amplitude amplification is a quadratic gain, and for unstructured search it cannot be improved, as shown under quantum complexity theory. In practice noise limits it. Every iteration needs an oracle circuit and an $n$-qubit reflection, and errors accumulated over about $\sqrt N$ iterations dephase the coherent rotation.

## References For The Physical Derivation

- [L. K. Grover, A fast quantum mechanical algorithm for database search; the search algorithm with about the square root of N queries.](https://arxiv.org/abs/quant-ph/9605043)
- [G. Brassard, P. Hoyer, M. Mosca and A. Tapp, Quantum Amplitude Amplification and Estimation; the rotation angle and its estimation for general preparation circuits.](https://arxiv.org/abs/quant-ph/0005055)
