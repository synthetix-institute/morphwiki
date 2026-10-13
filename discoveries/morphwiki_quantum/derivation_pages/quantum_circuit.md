# Quantum circuit

Two laboratory operations on a pair of qubits, a Hadamard pulse on one and a controlled-NOT between them, give different results in the two possible orders. In one order the qubits end entangled, with perfectly correlated outcomes; in the other they remain uncorrelated. A quantum circuit specifies such orders. Each gate is a unitary $U_j$ acting on a few qubits, and the register evolves by the time-ordered product:

```math
\rho_{\rm out}=U_m\cdots U_2U_1\,\rho_{\rm in}\,U_1^\dagger U_2^\dagger\cdots U_m^\dagger,
\qquad p(y)=\operatorname{Tr}(M_y\rho_{\rm out}).
```

Here $M_y$ is the measurement operator for outcome $y$, usually a projector on a computational basis state. The Hadamard gate is $H=(X+Z)/\sqrt2$, and the controlled-NOT flips the target qubit when the control qubit is in $|1\rangle$. Starting from $|00\rangle$, the two orders give

```math
\mathrm{CNOT}\,(H\otimes I)|00\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2},\qquad
(H\otimes I)\,\mathrm{CNOT}|00\rangle=\frac{|00\rangle+|10\rangle}{\sqrt2}.
```

In the left state, $Z$ measurements on the two qubits always agree. In the right state, the target qubit is always found in $0$ and the control qubit is random. The circuit diagram is therefore a record of the time order of physical couplings, not a list of available operations.

The roles of control and target depend on the basis in which a gate is viewed. Let $|-\rangle=(|0\rangle-|1\rangle)/\sqrt2$, an eigenstate of $X$ with eigenvalue $-1$. Flipping the target then leaves it unchanged except for a sign, which appears as a phase of the control:

```math
\mathrm{CNOT}\,|x\rangle|-\rangle=(-1)^x|x\rangle|-\rangle,\qquad
(H\otimes H)\,\mathrm{CNOT}_{12}\,(H\otimes H)=\mathrm{CNOT}_{21}.
```

The reversal of control and target follows from the kickback, because Hadamards exchange the $X$ and $Z$ bases on both qubits. This phase kickback is the step by which an oracle writes a function value into a phase, as in the Deutsch--Jozsa circuit described under quantum computing.

Single-qubit rotations together with the controlled-NOT suffice to compose any unitary on $n$ qubits (Barenco and colleagues, 1995). Universality says nothing about cost. A general unitary on $n$ qubits has $4^n-1$ real parameters, while each gate supplies a bounded number. Most unitaries therefore require a number of gates that grows exponentially with $n$. Efficient algorithms are the special unitaries with circuits of polynomial size.

The circuit description assumes that each gate acts only on its intended qubits and that the qubits do not leak into other levels. Noise is then represented by a quantum channel after each gate. If errors are independent with probability $\epsilon$ per gate, a circuit of $n_g$ gates runs without any error with probability

```math
P_{\rm ok}=(1-\epsilon)^{n_g}\approx e^{-n_g\epsilon}.
```

With $\epsilon=0.005$ per two-qubit gate, a circuit of 200 such gates runs without error with probability $0.37$. This fixes the depth that can be reached without quantum error correction. Error correction replaces the exponential decay by repeated syndrome measurements and corrections, which are themselves further gates of the circuit.

## References For The Physical Derivation

- [A. Barenco, C. H. Bennett, R. Cleve, D. P. DiVincenzo, N. Margolus, P. Shor and colleagues, Elementary gates for quantum computation; universality of one-qubit gates with the controlled-NOT and gate counts.](https://arxiv.org/abs/quant-ph/9503016)
- [R. Cleve, A. Ekert, C. Macchiavello and M. Mosca, Quantum Algorithms Revisited; phase kickback and circuits as multi-path interference.](https://arxiv.org/abs/quant-ph/9708016)
