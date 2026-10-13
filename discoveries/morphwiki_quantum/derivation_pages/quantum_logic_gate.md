# Quantum logic gate

In a trapped-ion processor, laser pulses rotate the internal two-level state of each ion, and a further pulse couples two ions through their shared motion. Every computation on the register must be assembled from these few physical operations. Two facts make this possible. Three rotations produce any single-qubit unitary, and one entangling gate between pairs completes the set.

A resonant pulse rotates the Bloch vector about an axis fixed by the drive phase, as in the two-state system. Let $X,Y,Z$ be the Pauli matrices, $R_y(\gamma)=e^{-i\gamma Y/2}$ and $R_z(\beta)=e^{-i\beta Z/2}$. Every single-qubit unitary has the form

```math
U=e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta),\qquad H=e^{i\pi/2}R_y(\pi/2)R_z(\pi).
```

After a global phase is removed, $U$ has determinant one. It is then the matrix with rows $(a,-b^*)$ and $(b,a^*)$, where $|a|^2+|b|^2=1$. Setting $|a|=\cos(\gamma/2)$ fixes $\gamma$, and the phases of $a$ and $b$ fix $\beta+\delta$ and $\beta-\delta$. The Hadamard gate $H$, which exchanges the $Z$ and $X$ bases, is shown as an example.

Single-qubit gates cannot create entanglement, so an interaction is required. An Ising coupling proportional to $Z_1Z_2$ occurs naturally in spin and ion systems. The controlled-$Z$ gate changes the sign of $|11\rangle$ only. Since $|11\rangle\langle11|=(I-Z_1)(I-Z_2)/4$ and commuting terms exponentiate separately,

```math
CZ=e^{i\pi/4}e^{-i\pi Z_1/4}e^{-i\pi Z_2/4}e^{i\pi Z_1Z_2/4},\qquad
\mathrm{CNOT}=(I\otimes H)\,CZ\,(I\otimes H).
```

The coupling, applied until its phase reaches $\pi/4$, supplies the last factor, and local $z$ rotations remove the rest. Hadamard gates on the target exchange $Z$ and $X$, converting the sign change into the bit flip of the CNOT gate.

Barenco and colleagues showed that CNOT together with all single-qubit gates is exactly universal. The key step builds any controlled single-qubit gate. Choose $A=R_z(\beta)R_y(\gamma/2)$, $B=R_y(-\gamma/2)R_z(-(\beta+\delta)/2)$ and $C=R_z((\delta-\beta)/2)$. Then $ABC=I$. Conjugation by $X$ reverses both rotation angles, so $XBX=R_y(\gamma/2)R_z((\beta+\delta)/2)$ and $AXBXC=e^{-i\alpha}U$. With $P_\alpha=\mathrm{diag}(1,e^{i\alpha})$ acting on the control,

```math
C\text{-}U=(P_\alpha\otimes A)\,\mathrm{CNOT}\,(I\otimes B)\,\mathrm{CNOT}\,(I\otimes C).
```

Operators act from right to left. If the control is 0, the target receives $ABC=I$. If it is 1, the target receives $e^{-i\alpha}U$, and the phase gate restores $e^{i\alpha}$. For the controlled Hadamard, $\alpha=\pi/2$, $\beta=0$, $\gamma=\pi/2$ and $\delta=\pi$. Then $A=R_y(\pi/4)$, $B=R_y(-\pi/4)R_z(-\pi/2)$, $C=R_z(\pi/2)$ and $P_\alpha=\mathrm{diag}(1,i)$. Multiplying the five matrices reproduces the controlled Hadamard exactly. Toffoli gates and general multi-qubit unitaries follow by repeating such constructions.

Universality says nothing about efficiency. Each single-qubit gate has at most three angles and a CNOT has none. A generic $n$-qubit unitary has $4^n-1$ real parameters and therefore needs at least $(4^n-1)/3$ single-qubit gates. Fault-tolerant hardware offers only a finite set, such as $H$, $T=\mathrm{diag}(1,e^{i\pi/4})$ and CNOT. The Solovay--Kitaev theorem guarantees that any single-qubit gate is approximated to accuracy $\epsilon$ by a sequence from this set. The Dawson--Nielsen algorithm uses $O(\log^{3.97}(1/\epsilon))$ gates. Errors of individual approximated gates add at most linearly:

```math
\|U_m\cdots U_1-V_m\cdots V_1\|\leq\sum_{k=1}^{m}\|U_k-V_k\|.
```

The bound follows from the triangle inequality and unitarity by replacing one factor at a time. A circuit of $m$ gates therefore needs accuracy of about $\epsilon/m$ per gate for a total error $\epsilon$. The translation of whole programs into such gate sequences is treated under quantum programming.

## References For The Physical Derivation

- [A. Barenco and colleagues, Elementary gates for quantum computation; universality of CNOT with single-qubit gates and controlled-U constructions.](https://arxiv.org/abs/quant-ph/9503016)
- [C. M. Dawson and M. A. Nielsen, The Solovay-Kitaev algorithm; approximation of single-qubit gates from a finite set with O(log^3.97(1/epsilon)) gates.](https://arxiv.org/abs/quant-ph/0505030)
