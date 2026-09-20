# Quantum key distribution

Quantum key distribution creates correlated classical data whose secrecy is inferred from a specified quantum communication model. Its physical basis is that information about nonorthogonal signal states cannot be acquired perfectly while leaving those states unchanged. The task is key generation, not the transmission of an encrypted message or the authentication of an unknown partner.

In ideal BB84 the sender chooses between the eigenstates of $Z$ and $X$. Write $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$. Suppose an eavesdropper's unitary interaction preserves both $|0\rangle$ and $|1\rangle$ while recording them in probe states $|e_0\rangle$ and $|e_1\rangle$. Linearity then requires

```math
|+\rangle|e\rangle\longmapsto
\frac{|0\rangle|e_0\rangle+|1\rangle|e_1\rangle}{\sqrt2}.
```

The signal remains a pure $|+\rangle$ only when the two probe states coincide up to the phase compatible with the signal. Distinguishable probe records suppress its off-diagonal coherence. A check in the complementary basis can therefore detect the disturbance associated with that information gain.

After transmission, the legitimate parties disclose their basis choices, retain the compatible outcomes and estimate an error rate from a random sample. Classical error correction reconciles their strings and privacy amplification reduces the information that may remain with an adversary. For the ideal asymptotic single-photon BB84 setting with the relevant bit and phase error rates both bounded by $Q$, the one-way secret fraction per sifted bit has the familiar form

```math
r\geq1-2h_2(Q),\qquad
h_2(Q)=-Q\log_2Q-(1-Q)\log_2(1-Q).
```

This expression is tied to its security model. Finite data require statistical confidence terms; multiphoton emission, detector imperfections and information disclosed during reconciliation require explicit treatment. An observed low bit-error rate alone does not establish secrecy for an arbitrary device. Loss and source statistics can carry information that a two-level idealization omits.

The classical channel must be authenticated. Otherwise an adversary can impersonate each party in a separate quantum exchange. The quantum mechanism supplies a relation between information and disturbance under stated source and measurement assumptions; authentication supplies the identity of the parties using that relation. Keeping these contributions distinct is necessary to transfer a security argument from an ideal qubit model to an optical implementation.

## References For The Physical Derivation

- [V. Scarani and colleagues, The Security of Practical Quantum Key Distribution; ideal protocols, device assumptions and security bounds.](https://arxiv.org/abs/0802.4155)


## Relations In The Original Papers

[arXiv:0802.4155, S4.EGx43](https://arxiv.org/html/0802.4155#S4.EGx43). For the specified entanglement-based protocol, the asymptotic key rate subtracts phase-error information and error-correction leakage. Ideal single-photon assumptions and asymptotic rates; setting leakage to binary entropy gives the bound discussed in the chapter.
