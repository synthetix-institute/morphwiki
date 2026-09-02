# Quantum decoherence

**Physical domain:** Quantum states and subsystem structure

## Mechanism

Quantum decoherence is the loss of observable phase coherence in a subsystem when information about alternative amplitudes becomes encoded in environmental correlations.

Interference is lost when alternative system amplitudes become correlated with environmental states that can, even in principle, distinguish them. The missing coherence has then moved into correlations of the larger state rather than being erased by the subsystem equation alone.

The joint system and environment may evolve unitarily while the reduced system loses interference. Interaction correlates different system alternatives with distinguishable environmental states; tracing over the environment then suppresses off-diagonal terms in the selected pointer basis. Decoherence does not select one outcome, and it is not identical to memory. Markovian decoherence is possible when the reduced state still determines its future. Memory begins when discarded correlations return and two preparations with the same reduced state acquire different later statistics.

## Physical Construction

The state carrier is a joint system-environment state together with the reduced density operator accessible to the observer. The governing operation is System-environment unitary evolution followed by partial trace, or the corresponding reduced dynamical map. The joint state remains normalized and positive; a Markovian reduction additionally requires future maps to be fixed by the present reduced state. The calculated observables are Off-diagonal coherence, interference visibility, purity, and history-dependent response.

## Topic Equations

Joint unitary evolution, environmental distinguishability, reduced decoherence, and the semigroup test distinguish loss of interference from dynamical memory.

```math
\rho_S(t)=\operatorname{Tr}_E[U_{SE}(t)\rho_{SE}(0)U_{SE}^{\dagger}(t)]
\frac{\ket0\ket{E_0}+\ket1\ket{E_1}}{\sqrt2},\qquad (\rho_S)_{01}\propto\langle E_1|E_0\rangle
\dot\rho_S=-\frac{i}{\hbar}[H_S,\rho_S]+\sum_k\gamma_k\mathcal D[L_k]\rho_S
V_{t+s}=V_tV_s\quad\text{only in the time-homogeneous Markov limit}
```

## Physical Meaning

Unitary system-environment evolution can suppress the off-diagonal elements of the reduced density matrix after the environment is traced out. The overlap of the corresponding environmental states fixes the remaining visibility. Decoherence can be Markovian; memory requires the stronger condition that hidden correlations later alter evolution from the same reduced state.

In a two-path interferometer, scattering one distinguishable environmental state from each path lowers the fringe visibility in proportion to their overlap. Erasing the distinguishing record can restore interference in suitable conditional measurements.

The distinction between lost visibility and returning correlations leads directly to quantum channels, non-Markovian dynamics, and the composition test for memory.

## Consequences Forced By The Relation

Interference visibility falls with the overlap of the environmental states correlated with the interfering alternatives. The phase information can remain in the joint state even when it is absent from all reduced-system observables. When hidden correlations later alter the reduced dynamics, an auxiliary state coordinate or a memory kernel is required for predictive closure.

## Domain Of The Construction

The preferred basis and decoherence rate depend on the interaction, environmental spectrum, and initial system-environment state. Suppression of off-diagonal terms does not by itself derive a unique recorded outcome.

## Invariance And Realization

The joint state retains phase information transferred from the subsystem into system-environment correlations. Reduced interference visibility is fixed by the overlap of environmental states correlated with the alternatives. Equivalent system-environment dilations give the same reduced channel and system observables.

The preferred basis, decay rate, and recoherence depend on the interaction, environmental spectrum, and initial correlations. Changing the system-environment partition changes which correlations are hidden. A Markov approximation removes returning correlations; retaining them introduces auxiliary coordinates or a memory kernel.

## Discriminating Consequences

Interference visibility is compared with a control in which the environment cannot distinguish the alternatives. Two preparations with the same reduced state determine whether hidden correlations alter later observables. Reversing or decoupling the interaction determines whether coherence remains recoverable in the joint state.

## Source Equations

- [arXiv:quant-ph/0306087](https://arxiv.org/abs/quant-ph/0306087)
- [arXiv:quant-ph0306087](https://arxiv.org/abs/quant-ph0306087)
- [arXiv:quant-ph/0008131](https://arxiv.org/abs/quant-ph/0008131)
- [arXiv:quant-ph0008131](https://arxiv.org/abs/quant-ph0008131)
