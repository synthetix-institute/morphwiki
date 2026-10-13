# Quantum nonlocality

Three photons are emitted together and sent to three separated laboratories. Each laboratory measures one of two polarization observables. For a Greenberger--Horne--Zeilinger (GHZ) state, certain products of the three records are predicted with certainty. These certain predictions alone contradict any local assignment of values, without averaging an inequality.

Write the state as $(|000\rangle+|111\rangle)/\sqrt2$, with $|0\rangle$ and $|1\rangle$ the eigenstates of the Pauli operator $Z$. Applying the Pauli operators $X$ and $Y$ directly gives the eigenvalue relations

```math
X_1X_2X_3|{\rm GHZ}\rangle=+|{\rm GHZ}\rangle,\\
X_1Y_2Y_3|{\rm GHZ}\rangle=Y_1X_2Y_3|{\rm GHZ}\rangle=Y_1Y_2X_3|{\rm GHZ}\rangle=-|{\rm GHZ}\rangle.
```

Suppose each photon carries predetermined values $x_j=\pm1$ and $y_j=\pm1$, the records it would give if $X$ or $Y$ were measured. Locality requires that these values do not depend on which observables the other two laboratories choose. The three $XYY$-type relations then fix the product of all $x_j$, because each $y_j$ appears twice:

```math
(x_1y_2y_3)(y_1x_2y_3)(y_1y_2x_3)=x_1x_2x_3=(-1)^3=-1.
```

Quantum mechanics predicts $x_1x_2x_3=+1$ with certainty. No local assignment satisfies all four relations. For two spin-1/2 particles, perfect correlations alone do not suffice: the perfect anticorrelations of a singlet along equal axes have a local model. Bell's inequality needs the imperfect correlations at unequal angles. Each run measures only one combination of observables, so the contradiction is established across runs with different settings. Pan, Bouwmeester, Daniell, Weinfurter and Zeilinger performed this test with three-photon GHZ states in 2000. The $XXX$ products came out predominantly $+1$, as quantum mechanics predicts and opposite to the local inference from the $XYY$-type data.

Imperfect states require a bound that tolerates noise. Mermin's combination $M=\langle XXX\rangle-\langle XYY\rangle-\langle YXY\rangle-\langle YYX\rangle$ is at most 2 for local values, while the GHZ state gives 4. If the state is mixed with white noise so that correlations shrink by a factor $v$, then $M=4v$, and a violation requires only $v>1/2$. The two-particle CHSH test of Bell's theorem requires $v>1/\sqrt2$.

These correlations cannot carry a message. Let laboratory 1 measure with effects $E_a$ and laboratory 2 with effects $F_b^y$ for setting $y$. Because the effects of each setting sum to the identity, the record statistics in laboratory 1 do not depend on the distant choice:

```math
\sum_b\operatorname{Tr}[\rho(E_a\otimes F^y_b)]=\operatorname{Tr}(\rho_1E_a),
\qquad \rho_1=\operatorname{Tr}_2\rho.
```

Nonlocality appears only when records from separated laboratories are compared. Entanglement is necessary for it but not sufficient. Werner showed that a singlet mixed with enough white noise remains entangled yet admits a local model for all projective measurements. Device-independent quantum key distribution relies on observed nonlocal correlations rather than on a model of the devices. The Einstein--Podolsky--Rosen paradox is the two-particle argument that preceded these tests.

## References For The Physical Derivation

- [D. M. Greenberger, M. A. Horne and A. Zeilinger, Going Beyond Bell's Theorem; the three-particle argument without inequalities.](https://arxiv.org/abs/0712.0921)
- [N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani and S. Wehner, Bell nonlocality; Mermin inequality, no-signalling and local models of entangled states.](https://arxiv.org/abs/1303.2849)
