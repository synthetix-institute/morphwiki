# Quantum Theory: Concepts and Methods

*Historical, bibliographic or interpretive entry.*

Asher Peres's Quantum Theory: Concepts and Methods (1993) treats quantum theory as a set of rules for computing the probabilities of outcomes of tests that follow specified preparations. It does not assign properties to a system between preparation and test. The book joins foundational results to techniques later central to quantum information: composite systems, Bell's theorem, contextuality, information and thermodynamics, semiclassical methods, chaos and the measuring process.

A central tool is the generalized measurement, or positive operator-valued measure (POVM). Its outcomes $k$ correspond to positive operators $E_k$ that need not be projectors; they only have to sum to the identity. Neumark's theorem, discussed in the book, shows that every such measurement is a projective measurement on the system combined with an auxiliary system. In 1988 Peres applied this freedom to two non-orthogonal states $\ket{\psi_1}$ and $\ket{\psi_2}$ prepared with equal probability. No measurement identifies them every time without error. A three-outcome POVM can do so part of the time: two outcomes name the state with certainty, and the third is inconclusive. The probabilities and the largest conclusive fraction are

```math
p_k=\operatorname{Tr}(\rho E_k),\qquad E_k\geq0,\qquad \sum_kE_k=I,\qquad
P_{\rm conclusive}=1-|\langle\psi_1|\psi_2\rangle| .
```

This limit was found independently by Ivanovic, Dieks and Peres. It sets how often an eavesdropper can identify non-orthogonal signal states without error, a quantity used in analyses of quantum key distribution. For orthogonal states the conclusive fraction is one, and for identical states it is zero.

The chapters on inseparability derive the Clauser--Horne--Shimony--Holt inequality for local hidden variables, with $\pm1$ outcomes $A_0,A_1$ on one side and $B_0,B_1$ on the other. The singlet state violates it:

```math
|\langle A_0B_0\rangle+\langle A_0B_1\rangle+\langle A_1B_0\rangle-\langle A_1B_1\rangle|
\leq2,\qquad \text{quantum maximum } 2\sqrt2 .
```

The chapter on contextuality gives a proof of the Kochen--Specker theorem with 33 directions in three-dimensional space. No rule assigns the value 1 to exactly one direction of every orthogonal triad among them. Readers can continue with POVM, Bell's theorem, Quantum nonlocality, Projection-valued measure and Measurement in quantum mechanics.
