# Quantum error correction

A quantum memory must distinguish errors without measuring the unknown logical amplitudes it is intended to preserve. The state is encoded into a subspace in which different correctable errors leave distinguishable information in auxiliary degrees of freedom, while their probabilities reveal no logical-state information.

Let $P$ project onto the code subspace and let $E_a$ be the error operators in a specified noise model. Exact correction of their linear span is possible when there is a matrix $c$ such that

```math
P E_a^\dagger E_b P=c_{ab}P.
```

The right side is proportional to the identity within the code. Thus overlaps of the error-affected states depend on the error labels, but not on which logical superposition was stored. Diagonalizing $c$ organizes the error spaces so that a measurement can identify the required correction without resolving the encoded state.

For a simple illustration, encode $\alpha|0\rangle+\beta|1\rangle$ as $\alpha|000\rangle+\beta|111\rangle$ and consider at most one bit flip. The commuting observables $Z_1Z_2$ and $Z_2Z_3$ give four distinct syndromes:

```math
\begin{array}{c|rrrr}
\text{error}&I&X_1&X_2&X_3\\\hline
(Z_1Z_2,Z_2Z_3)&(+,+)&(-,+)&(-,-)&(+,-)
\end{array}
```

Both basis codewords have the same syndrome before an error. The syndrome measurement therefore preserves their coherence. Applying the indicated bit flip restores the encoded state for any $\alpha$ and $\beta$. Measuring the individual $Z_j$ instead would reveal which codeword was present and destroy an unknown superposition.

The noise specification matters. A phase flip acts within this code as a logical error and is not identified by those two syndromes. Protecting arbitrary single-qubit errors requires additional structure, such as a code that corrects both bit and phase errors. Increasing the number of spins without changing the encoded subspace and syndrome observables does not automatically supply that protection.

Error correction connects interaction, preparation, measurement and conditional dynamics in one mechanism. The environment determines the error operators; encoding determines the carrier subspace; syndrome extraction determines what information becomes observable; and the conditional operation restores the logical state. The algebraic correction condition is an exact test of this assembly. Fault tolerance adds another problem: the physical operations used to extract a syndrome can themselves propagate errors, so those operations must be analyzed as part of the noise model.

## References For The Physical Derivation

- [D. Gottesman, Stabilizer Codes and Quantum Error Correction; error correction conditions and syndrome measurements.](https://arxiv.org/abs/quant-ph/9705052)


## Relations In The Original Papers

[arXiv:quant-ph/9705052, Ch2.E10](https://arxiv.org/html/quant-ph/9705052#Ch2.E10). Correctable errors have overlaps independent of the logical state inside the code space. A specified code and error set; the three-qubit example corrects single bit flips, not arbitrary single-qubit errors.

[arXiv:quant-ph/0302006, S3.E22](https://arxiv.org/html/quant-ph/0302006#S3.E22). A detected error can be reversed on the code when its norm does not distinguish logical codewords. Detected-emission feedback with a specified error record; it is narrower than correction of an arbitrary unobserved error set.
