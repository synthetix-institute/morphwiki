# Quantum programming

A quantum program written in a language such as OpenQASM states operations convenient to its author, for example a phase $e^{i\phi}$ applied when two qubits are both 1. A superconducting or trapped-ion processor executes only its native rotations and one entangling gate, between qubits with fixed connections. A compiler translates one description into the other. That translation sets the gate count and hence the accumulated error.

The controlled phase $CP(\phi)=\mathrm{diag}(1,1,1,e^{i\phi})$ illustrates the translation. It multiplies only $|11\rangle$, and $|11\rangle\langle11|=(I-Z_1)(I-Z_2)/4$. The four terms commute, so the exponential factorizes into single-qubit rotations $R_z(\beta)=e^{-i\beta Z/2}$ and one two-qubit factor:

```math
CP(\phi)=e^{i\phi/4}\,[R_z(\phi/2)\otimes R_z(\phi/2)]\,e^{i\phi Z_1Z_2/4}.
```

Conjugating $Z_2$ by a CNOT with control on qubit 1 gives $Z_1Z_2$. The two-qubit factor therefore needs two CNOT gates:

```math
e^{i\phi Z_1Z_2/4}=\mathrm{CNOT}\,[I\otimes R_z(-\phi/2)]\,\mathrm{CNOT}.
```

The global phase $e^{i\phi/4}$ has no observable effect unless the whole gate is later made conditional on another qubit. A compiler applies such rules throughout a program. The quantum Fourier transform on $n$ qubits uses $n$ Hadamard gates and $n(n-1)/2$ controlled phases with angles $\pi/2^m$, hence $n(n-1)$ CNOTs. For three qubits this gives six CNOTs and three Hadamards. The reversal of qubit order at the end costs nothing, because the compiler relabels the outputs. If the qubits couple only along a line, the gate between the outer qubits needs a SWAP, three more CNOTs. With independent CNOT failures of probability 0.01, the success estimate drops from $0.99^6\approx0.94$ to $0.99^9\approx0.91$.

Programs can also measure a qubit during the run and use the result to choose later gates. The corrections in quantum teleportation are of this kind. Measuring qubit 1 in the $Z$ basis and then applying $X^m$ to qubit 2 for outcome $m$ has exactly the effect of a CNOT followed by that measurement:

```math
\sum_{m}(\Pi_m\otimes X^m)\,\rho\,(\Pi_m\otimes X^m)\\
=\sum_{m}(\Pi_m\otimes I)\,\mathrm{CNOT}\,\rho\,\mathrm{CNOT}\,(\Pi_m\otimes I).
```

Here $\Pi_m=|m\rangle\langle m|$ for $m=0,1$. This deferred-measurement identity holds because the CNOT is block diagonal in the basis of its control. Read from right to left, it removes a two-qubit gate whose control is measured immediately afterward. Griffiths and Niu applied it to the Fourier transform followed by measurement, as in phase estimation. In that circuit each qubit, after its Hadamard gate, takes part only in controlled phases that are diagonal in its computational basis. Its final measurement can therefore be moved forward to directly after the Hadamard. Each controlled phase then becomes a $z$ rotation on a later qubit, applied only if the earlier outcome was 1.

The three-qubit transform then needs three Hadamard gates, three measurements and classically conditioned rotations, but no two-qubit gate. A simulation with random input states gives output distributions identical to those of the coherent circuit. The cost moves into classical control, since each outcome must reach the next rotation within the coherence time of the remaining qubits. OpenQASM 3 includes mid-circuit measurement and conditional gates for this purpose. Arbitrary rotation angles are afterwards approximated in a fault-tolerant gate set, as described under quantum logic gates.

## References For The Physical Derivation

- [A. Barenco and colleagues, Elementary gates for quantum computation; decomposition of controlled gates into CNOTs and single-qubit rotations.](https://arxiv.org/abs/quant-ph/9503016)
- [R. B. Griffiths and C.-S. Niu, Semiclassical Fourier Transform for Quantum Computation; replacing two-qubit gates by measurement and classically controlled rotations.](https://arxiv.org/abs/quant-ph/9511007)
- [A. W. Cross and colleagues, OpenQASM 3: A broader and deeper quantum assembly language; mid-circuit measurement and classical control in a program language.](https://arxiv.org/abs/2104.14722)
