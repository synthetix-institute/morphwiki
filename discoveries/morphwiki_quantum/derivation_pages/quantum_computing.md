# Quantum computing

A function $f$ on $n$-bit strings returns $0$ or $1$ and is promised to be either constant or balanced, giving $0$ on exactly half of its inputs. A deterministic classical procedure may need $2^{n-1}+1$ evaluations to decide which. A quantum computer decides it with one evaluation, through interference among all $2^n$ inputs. This Deutsch--Jozsa calculation shows where the advantage of quantum computing comes from, and where it does not.

The register holds $n$ qubits and one ancilla. The function is accessed through the unitary $U_f|x\rangle|y\rangle=|x\rangle|y\oplus f(x)\rangle$, where $\oplus$ is addition modulo two. With the ancilla in $|-\rangle$, phase kickback turns the call into the sign $(-1)^{f(x)}$. Hadamard gates on all $n$ qubits before and after the call give

```math
|0\rangle^{\otimes n}\ \xrightarrow{H^{\otimes n}}\ \frac{1}{2^{n/2}}\sum_x|x\rangle
\ \xrightarrow{U_f}\ \frac{1}{2^{n/2}}\sum_x(-1)^{f(x)}|x\rangle
\ \xrightarrow{H^{\otimes n}}\ \sum_yc_y|y\rangle,
```

```math
c_y=\frac{1}{2^n}\sum_x(-1)^{f(x)+x\cdot y},\qquad c_{0}=\frac{1}{2^n}\sum_x(-1)^{f(x)}.
```

Here $x\cdot y$ is the bitwise inner product modulo two. For a constant function $c_0=\pm1$, so measuring all qubits returns $00\ldots0$ with certainty. For a balanced function the terms cancel exactly, $c_0=0$, and the all-zero outcome never occurs. The decisive step is the second layer of Hadamards, which makes the $2^n$ phase-carrying paths interfere at a single output.

The state after the call contains all $2^n$ function values as signs, but a measurement returns only $n$ bits. Holevo's bound forbids extracting more than $n$ classical bits from $n$ qubits. A quantum computer therefore does not evaluate every input and report the results. It gains only when a global property of $f$ can be turned into an interference pattern. The comparison also has a limit. A randomized classical procedure that checks $k$ random inputs errs with probability at most $2^{1-k}$, independent of $n$. The exponential separation holds for exact computation only.

The circuit has been run with nuclear spins in liquid-state NMR. Gulde and colleagues (2003) ran it with a single trapped calcium ion, using an electronic transition as one qubit and a vibrational mode as the other. The same pattern, a superposition, a phase oracle and an interfering transform, underlies Simon's algorithm and the Fourier transform in Shor's factoring algorithm.

Several facts are established. Universal gate sets exist, as described under quantum circuit. Quantum error correction can protect stored information, and the threshold theorem shows that below a constant error rate per gate, arbitrarily long computations succeed with polylogarithmic overhead. Processors with hundreds of physical qubits operate, and logical qubits whose errors decrease with code size have been demonstrated. Open questions remain: building machines large enough to factor numbers of cryptographic size, and finding practical problems with proven speedups beyond the simulation of quantum systems.

## References For The Physical Derivation

- [R. Cleve, A. Ekert, C. Macchiavello and M. Mosca, Quantum Algorithms Revisited; the Deutsch-Jozsa circuit with phase kickback and interference of computational paths.](https://arxiv.org/abs/quant-ph/9708016)
- [J. Preskill, Quantum Computing in the NISQ era and beyond; noisy processors, error correction and open questions about practical speedups.](https://arxiv.org/abs/1801.00862)
