# Quantum logic

Two crossed polarizers block all light. A third polarizer inserted between them at 45 degrees lets one eighth of unpolarized light through. The propositions tested by polarizers do not combine like the propositions of classical logic, and quantum logic describes how they do combine.

The proposition that a photon passes a polarizer at angle $\theta$ corresponds to the projector $P_\theta$ onto that polarization. Its negation is the orthogonal polarization. The conjunction of two propositions is certain exactly when both are certain; it corresponds to the intersection of their subspaces. The disjunction corresponds to the smallest closed subspace containing both. Birkhoff and von Neumann showed in 1936 that these operations form a lattice:

```math
a\wedge b\leftrightarrow \operatorname{ran}P_a\cap\operatorname{ran}P_b,\qquad
a\vee b\leftrightarrow \overline{\operatorname{ran}P_a+\operatorname{ran}P_b},\qquad
\neg a\leftrightarrow I-P_a.
```

No polarization passes the $0^\circ$ and $45^\circ$ polarizers with certainty, so their conjunction is the zero subspace. Yet light does pass the sequence of three polarizers. A sequence of filters is not a conjunction. Von Neumann showed that the conjunction is the limit of infinitely many alternations of the two projectors. For $0^\circ$ and $45^\circ$, each further polarizer of an alternating stack transmits half the light:

```math
(P_aP_b)^n\longrightarrow P_{a\wedge b}\quad(n\to\infty),\qquad
I_m=I_1\cos^{2m}45^\circ=2^{-m}I_1.
```

The intensity after $m$ further polarizers tends to zero, the empty conjunction. For commuting projectors the product $P_aP_b$ is already the conjunction.

The distributive law fails. Let $a$ be horizontal polarization, $b$ the diagonal one and $\neg b$ the antidiagonal one. The disjunction $b\vee\neg b$ is the whole space, while neither $a\wedge b$ nor $a\wedge\neg b$ contains a nonzero vector:

```math
a\wedge(b\vee\neg b)=a\neq0=(a\wedge b)\vee(a\wedge\neg b).
```

Physically, a diagonal analyzer always gives one of its two outcomes for a horizontal photon, but neither outcome is certain in advance. No polarization makes both horizontal and diagonal certain. A description that assigned every photon a definite answer to both questions would satisfy the distributive law.

A weaker law remains, the orthomodular law: if $a\leq b$ then $b=a\vee(b\wedge\neg a)$. Within any set of mutually commuting projectors the lattice is Boolean, so classical logic holds for compatible propositions. The failures appear only across incompatible measurements. The Kochen--Specker theorem sharpens this. In dimension three or more, no assignment of true or false to all projectors makes exactly one member of every complete orthogonal set true. Kirchmair and coworkers tested a state-independent form with trapped ions in 2009, measuring triples of commuting two-qubit observables. The measured correlations exceeded the bound obeyed by any such assignment.

The lattice structure, Gleason's theorem and the Kochen--Specker theorem are established mathematics with tested consequences. The proposal that this lattice should replace classical logic in reasoning, argued by Putnam in 1968, is not generally accepted. Reasoning about experiments uses ordinary logic, while the lattice describes the propositions that experiments test. Projectors also generate the operator algebras discussed under von Neumann algebras.

## References For The Physical Derivation

- [M. L. Dalla Chiara and R. Giuntini, Quantum Logic; lattices of sharp and unsharp quantum propositions.](https://arxiv.org/abs/quant-ph/0101028)
- [G. Kirchmair and colleagues, State-independent experimental test of quantum contextuality; trapped-ion test of noncontextual value assignments.](https://arxiv.org/abs/0904.1655)
