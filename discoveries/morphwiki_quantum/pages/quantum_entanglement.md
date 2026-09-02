# Quantum entanglement

## Central Claim
Entanglement is a property of a composite state that cannot be written as a classical mixture of product states across a chosen subsystem decomposition; for a pure state, this reduces to failure to factor.

## Formal Role
The tensor-product decomposition specifies what counts as subsystem A and subsystem B. A pure state is entangled when its Schmidt rank exceeds one. Each subsystem can then be mixed even though the joint state is pure, because partial tracing discards the correlations that purify it. Local basis changes preserve the Schmidt coefficients, while a different physical factorization can change whether the same vector is called entangled. Bell measurements test whether the resulting correlations admit a local hidden-variable model.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- A physical subsystem algebra or tensor-product factorization is stated.
- The joint state is decomposed into Schmidt modes or tested for separability.
- Partial traces give the states available to local observers.
- Correlation observables distinguish the joint state from independent local preparations.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
|\Psi\rangle=\sum_k\sqrt{\lambda_k}|k_A\rangle|k_B\rangle,\quad \sum_k\lambda_k=1
\rho_A=\operatorname{Tr}_B|\Psi\rangle\langle\Psi|
S(\rho_A)=-\operatorname{Tr}(\rho_A\log\rho_A)
|S_{\mathrm{CHSH}}|\leq2,\qquad |S_{\mathrm{CHSH}}|_{\mathrm{QM}}\leq2\sqrt2
```

## Mechanism Roles
- **state:** bipartite state; Schmidt decomposition; reduced density operator
- **operator:** partial trace; local observable; correlation operator
- **spectrum:** Schmidt spectrum; entanglement entropy; Bell correlator
- **boundary:** subsystem algebra; tensor-product factorization
- **incompatibility:** nonseparability; Bell inequality violation
- **protocol:** local preparation; separated measurement; correlation readout

## Representation-Stable Content
- Schmidt coefficients and entanglement entropy are invariant under local unitary changes of basis.
- The reduced-state spectra preserve the amount of pure-state bipartite entanglement.
- Correlations remain joint properties even when neither subsystem has a pure local state.

## Representation-Dependent Content
- The chosen subsystem factorization and accessible observable algebra determine which correlations count as entanglement.
- Noise, loss, and coarse graining can convert pure-state entanglement into mixed-state correlations.
- Different platforms realize the same Schmidt structure with photons, spins, atoms, modes, or encoded qubits.

## Validation Checks
- Local measurements reconstruct a correlation witness or Bell parameter that product preparations cannot reproduce.
- Independent local-unitary rotations leave the inferred Schmidt spectrum unchanged.
- A separable-state control fixes the correlation background of the apparatus.
