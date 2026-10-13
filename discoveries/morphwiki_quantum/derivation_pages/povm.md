# POVM

A photon arrives polarized either horizontally or diagonally, with equal probability. The two states are not orthogonal, so no measurement identifies them every time without error. A measurement can nevertheless be built that never errs and sometimes declares the result inconclusive.

Write the states as $|\psi_0\rangle$ and $|\psi_1\rangle$ with phases chosen so that $s=\langle\psi_0|\psi_1\rangle$ is real and positive. Let $|\psi_j^\perp\rangle$ be the state orthogonal to $|\psi_j\rangle$. A measurement with three outcomes is defined by the positive operators

```math
E_0=\frac{|\psi_1^\perp\rangle\langle\psi_1^\perp|}{1+s},\qquad
E_1=\frac{|\psi_0^\perp\rangle\langle\psi_0^\perp|}{1+s},\qquad
E_?=I-E_0-E_1.
```

Outcome 0 never occurs for $|\psi_1\rangle$, and outcome 1 never occurs for $|\psi_0\rangle$. The prefactor $1/(1+s)$ is the largest value that keeps $E_?$ positive; its smaller eigenvalue then vanishes. Each state is identified with probability $|\langle\psi_0|\psi_1^\perp\rangle|^2/(1+s)=1-s$. This is the Ivanovic--Dieks--Peres limit, optimal for equal prior probabilities.

For horizontal and diagonal polarization, $s=1/\sqrt2$ and the success probability is $0.293$. A projective measurement in the basis containing $|\psi_0^\perp\rangle$ also never errs, but identifies only $|\psi_1\rangle$, giving an average of $(1-s^2)/2=0.25$. Three nonzero orthogonal projectors cannot fit in a two-dimensional space. This is the general structure: a positive operator-valued measure (POVM) has effects $E_k\geq0$ that sum to the identity, with $p(k)=\operatorname{Tr}(\rho E_k)$.

Naimark's theorem shows how such a measurement is performed. The photon is coupled to an additional mode, the ancilla, prepared in $|0\rangle_a$. A unitary interaction acts as

```math
U|\psi_j\rangle|0\rangle_a=\sqrt{1-s}\,|u_j\rangle|0\rangle_a+\sqrt{s}\,|\chi\rangle|1\rangle_a,
\qquad\langle u_0|u_1\rangle=0.
```

Inner products are preserved, since $(1-s)\langle u_0|u_1\rangle+s=s$, so such a unitary exists. When the ancilla is found in $|0\rangle_a$, the photon is in one of two orthogonal states and a projective measurement identifies it without error. When the ancilla is found in $|1\rangle_a$, both inputs leave the same state $|\chi\rangle$, and the result is inconclusive. Restricting this larger projective measurement to the photon reproduces $E_0$, $E_1$ and $E_?$ exactly.

In general, a POVM fixes only the outcome probabilities. The state after outcome $k$ depends on how the measurement is carried out, through operators $K_{k\alpha}$ with $E_k=\sum_\alpha K_{k\alpha}^\dagger K_{k\alpha}$. Different implementations of the same effects can leave the photon in different states, or absorb it altogether.

Huttner and colleagues realized this scheme in 1996 using polarization-dependent loss in optical fibre. Photons removed by the loss element play the role of the inconclusive outcome. The same measurement underlies the B92 version of quantum key distribution. Missed detections add inconclusive events without creating errors. The sharp special case, with orthogonal projectors, is the projection-valued measure.

## References For The Physical Derivation

- [S. M. Barnett and S. Croke, Quantum state discrimination; unambiguous discrimination, the Ivanovic-Dieks-Peres limit and its optical realizations.](https://arxiv.org/abs/0810.1970)
- [T. Heinosaari and M. Ziman, Guide to Mathematical Concepts of Quantum Theory; POVMs and Naimark dilation.](https://arxiv.org/abs/0810.3536)
