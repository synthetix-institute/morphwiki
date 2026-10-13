# Quantum finite automaton

A photon passes through a row of identical polarization rotators, each turning its linear polarization by the same angle. A polarizer at the end transmits or absorbs it. The transmission probability depends only on the number of rotators. A quantum finite automaton uses this arrangement to decide a property of an input word. Each letter applies a fixed unitary to a small quantum system, and one measurement after the last letter gives accept or reject.

In the measure-once model of Moore and Crutchfield the system has a finite orthonormal basis. Letter $\sigma$ acts by a unitary $U_\sigma$, the initial state is $|\psi_0\rangle$, and $P_{\rm acc}$ projects onto the accepting states. A word $w=\sigma_1\sigma_2\cdots\sigma_k$ is accepted with probability

```math
P_{\rm acc}(w)=\big\|P_{\rm acc}\,U_{\sigma_k}\cdots U_{\sigma_2}U_{\sigma_1}|\psi_0\rangle\big\|^2.
```

The measure-many model of Kondacs and Watrous instead measures after every letter. Consider words $a^k$ over a single letter and the language $L_p$ of words whose length is divisible by $p$. Two basis states suffice. Let $U_a$ rotate the real plane spanned by $|0\rangle$ and $|1\rangle$ through the angle $2\pi/p$, start in $|0\rangle$ and accept on $|0\rangle$:

```math
U_a^k|0\rangle=\cos\frac{2\pi k}{p}|0\rangle+\sin\frac{2\pi k}{p}|1\rangle,\qquad
P_{\rm acc}(a^k)=\cos^2\frac{2\pi k}{p}.
```

Every word in $L_p$ returns the state to its start and is accepted with certainty. Other words are accepted with probability below one. For odd $p$, however, the largest such value is $\cos^2(\pi/p)$, reached at $k=(p\pm1)/2$. For $p=7$ it equals 0.81, so a single run separates the two classes poorly.

The separation improves with a superposition of $d$ rotation planes. Plane $j$ is rotated through $2\pi k_j/p$ per letter, with integer multipliers $k_j$. The initial state is the equal superposition of the starting vectors of all planes, and acceptance projects back onto it. The acceptance probability is then a squared return amplitude:

```math
P_{\rm acc}(a^n)=\Big[\frac1d\sum_{j=1}^{d}\cos\frac{2\pi k_jn}{p}\Big]^2.
```

For odd $p$ choose $k_j=1,2,\ldots,(p-1)/2$. If $p$ does not divide $n$, the phases $e^{2\pi ijn/p}$ with $j=1,\ldots,p-1$ sum to $-1$. Pairing $j$ with $p-j$ shows that the cosines in the bracket sum to $-1/2$. Every non-member is therefore accepted with probability exactly $1/(p-1)^2$. For $p=7$, three planes with six basis states accept members with certainty and every other length with probability $1/36\approx0.028$.

This choice needs almost as many states as a classical counter modulo $p$. Ambainis and Freivalds showed that a number of planes of order $\log p$, with suitable multipliers, keeps every non-member below a fixed acceptance bound. For $p=10007$, a search over random multipliers finds 37 planes, or 74 basis states, with no non-member accepted above probability 0.15. Any deterministic automaton for $L_p$ needs $p$ states. For prime $p$ the same holds for a probabilistic automaton with bounded error.

Mereghetti and colleagues built this automaton with single-photon polarization and linear optics, reducing the error by combining independent runs. The eigenphases $\pm2\pi k_j/p$ of the letter unitary play the role of energies. The acceptance amplitude is thus the survival amplitude of spectral theory, evaluated at integer times.

The limits of the model follow from unitarity. Each letter acts reversibly, so the automaton cannot erase information about earlier letters. With bounded error, measure-once automata recognize exactly the group languages, whose letters permute the states of the minimal classical automaton (Brodsky and Pippenger). The regular language of words ending in $a$ is excluded, because recognizing it requires forgetting every earlier letter. Intermediate measurements, as in the measure-many model, enlarge the class but still miss some regular languages. General dissipative operations recover all of them, since a quantum operation can map each basis state to the next state of any classical automaton.

## References For The Physical Derivation

- [A. Ambainis and R. Freivalds, 1-way quantum finite automata: strengths, weaknesses and generalizations; the automaton for lengths divisible by p with O(log p) states and the classical state count.](https://arxiv.org/abs/quant-ph/9802062)
- [A. Brodsky and N. Pippenger, Characterizations of 1-Way Quantum Finite Automata; measure-once automata with bounded error and the measure-many model.](https://arxiv.org/abs/quant-ph/9903014)
- [C. Mereghetti and colleagues, Photonic Realization of a Quantum Finite Automaton; polarization implementation of the periodic-language automaton with error reduction.](https://arxiv.org/abs/2001.10749)
