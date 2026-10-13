# Quantum Computing: A Gentle Introduction

*Historical, bibliographic or interpretive entry.*

Three polarizing filters can transmit light that two of them block. A horizontal and a vertical polarizer extinguish an unpolarized beam. A third polarizer at $45^\circ$ inserted between them lets one eighth of the original intensity through, $\tfrac12\cos^245^\circ\cos^245^\circ=\tfrac18$. Eleanor Rieffel and Wolfgang Polak introduce the qubit through photon polarization and this experiment in Quantum Computing: A Gentle Introduction (MIT Press, 2011). The authors had earlier written a survey of quantum computing for non-physicists.

The book is written for readers trained in computer science or mathematics rather than physics. Its opening part covers single and multiple qubits, measurement, entanglement, the BB84 key-distribution protocol, unitary gates and reversible versions of classical functions. The middle part treats quantum algorithms, from Deutsch's and Simon's problems to Shor's factoring algorithm and Grover's search. The final part covers entangled subsystems, quantum error correction, fault tolerance, and alternative models such as measurement-based and adiabatic computation.

Grover's algorithm shows the style of argument. A search over $N$ items with one marked item $\ket{w}$ starts from the uniform superposition $\ket{s}$. Each iteration flips the sign of $\ket{w}$ and then reflects about $\ket{s}$. Two reflections make a rotation by $2\theta$ in the plane of $\ket{w}$ and $\ket{s}$, so after $k$ iterations

```math
\sin\theta=\frac{1}{\sqrt N},\qquad P_k=\sin^2\bigl((2k+1)\theta\bigr),\qquad
k_{\rm opt}\approx\frac{\pi}{4}\sqrt N .
```

For $N=4$ a single iteration gives $3\theta=90^\circ$ and finds the marked item with certainty. For $N=10^6$ about 785 iterations replace the half million queries that classical search needs on average. The quadratic gain assumes that the oracle acts coherently on a superposition, and it is known to be optimal for unstructured search. Readers can continue with Qubit, Quantum logic gate, Quantum circuit, Quantum algorithm and Quantum error correction.

## References For The Physical Derivation

- [E. G. Rieffel and W. Polak, An Introduction to Quantum Computing for Non-Physicists; the authors' earlier survey for non-physicists, covering basic principles, cryptography, teleportation, Shor's and Grover's algorithms and error correction.](https://arxiv.org/abs/quant-ph/9809016)
