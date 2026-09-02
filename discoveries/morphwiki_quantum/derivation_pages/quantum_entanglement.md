# Quantum entanglement

**Physical domain:** Quantum states and subsystem structure

## Mechanism

Quantum entanglement is a property of a composite state that cannot be written as a classical mixture of product states across a chosen subsystem decomposition; for a pure state, this reduces to failure to factor.

Entanglement is required when the state of a composite system cannot be assembled from independent states of its parts. It changes which correlations are possible and makes subsystem states mixed even when the total state is pure.

The tensor-product decomposition specifies what counts as subsystem A and subsystem B. A pure state is entangled when its Schmidt rank exceeds one. Each subsystem can then be mixed even though the joint state is pure, because partial tracing discards the correlations that purify it. Local basis changes preserve the Schmidt coefficients, while a different physical factorization can change whether the same vector is called entangled. Bell measurements test whether the resulting correlations admit a local hidden-variable model.

## Physical Construction

The state carrier is a composite Hilbert space with a physically specified subsystem algebra or tensor-product factorization. The governing operation is Schmidt decomposition, partial trace, local observables, and joint correlation operators. The joint density operator is positive and normalized; separability is defined relative to the chosen subsystem structure. The calculated observables are Reduced-state spectra, entanglement entropy, correlation witnesses, and Bell parameters.

## Topic Equations

Subsystem factorization, Schmidt spectrum, reduced-state entropy, and Bell correlations separate the state relation from its local observable.

```math
\mathcal H_{AB}=\mathcal H_A\otimes\mathcal H_B
\ket{\Psi}_{AB}=\sum_k\sqrt{\lambda_k}\ket{k_A}\ket{k_B},\qquad \sum_k\lambda_k=1
\rho_A=\operatorname{Tr}_B\ket{\Psi}\bra{\Psi},\qquad S_A=-\operatorname{Tr}(\rho_A\log\rho_A)
|S_{\mathrm{CHSH}}|\leq2,\qquad |S_{\mathrm{CHSH}}|_{\mathrm{QM}}\leq2\sqrt2
```

## Physical Meaning

The tensor-product structure defines the proposed subsystems. A state is entangled when it is not separable across that factorization. Partial traces describe each part, while joint observables expose correlations that no product state can reproduce.

In a Bell pair, each spin alone is maximally mixed, yet measurements on the pair are strongly correlated. The information resides in the relation between subsystems rather than in either local state.

Bell's theorem and contextuality determine which entangled correlations are incompatible with classical joint assignments.

## Consequences Forced By The Relation

A pure bipartite state with more than one nonzero Schmidt coefficient gives mixed reduced states and correlations unavailable to product preparations. Local unitary changes of basis preserve the Schmidt coefficients and the pure-state entanglement entropy. Suitable local measurements can violate a Bell inequality even though each subsystem alone carries no corresponding pure state.

## Domain Of The Construction

Entanglement is defined relative to a physical subsystem algebra or tensor-product factorization. For mixed states, nonfactorization of one decomposition is insufficient; separability requires testing all convex product decompositions.

## Invariance And Realization

Schmidt coefficients and pure-state entanglement entropy are invariant under local unitary changes of basis. The reduced-state spectra preserve the amount of bipartite pure-state entanglement. Correlations remain joint properties even when neither subsystem has a pure local state.

The subsystem factorization and accessible observable algebra determine which correlations count as entanglement. Noise, loss, and coarse graining can convert pure-state entanglement into mixed-state correlations. Photons, spins, atoms, modes, and encoded qubits can realize the same Schmidt structure.

## Discriminating Consequences

Local measurements reconstruct a correlation witness or Bell parameter that product preparations cannot reproduce. Independent local-unitary rotations leave the inferred Schmidt spectrum unchanged. A separable-state control fixes the correlation background of the apparatus.
