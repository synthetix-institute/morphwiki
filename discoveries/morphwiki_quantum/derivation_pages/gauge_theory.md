# Gauge theory

**Physical domain:** Fields, constraints, and scale

## Mechanism

Gauge theory defines how internal states are compared at different spacetime points: a connection relates neighboring frames, and curvature records the path dependence that no single gauge choice can remove.

Gauge theory separates physical states from multiple mathematical descriptions related by local transformations. The redundancy is useful because it makes locality and interaction structure explicit, but constraints are required to remove unphysical degrees of freedom.

A local gauge transformation changes the field coordinates used at each point without changing the physical state. Ordinary derivatives compare fields in different local frames and therefore cease to transform covariantly. The gauge connection repairs that comparison. Its commutator gives the field strength, while Wilson loops measure the accumulated transport around a closed path. Gauss constraints select physical states and charges. The connection is representation dependent; curvature, loop observables, and gauge-invariant amplitudes carry the physical content.

## Physical Construction

The state carrier is matter and gauge fields modulo local gauge equivalence, restricted to the physical constraint sector. The calculation involves a covariant derivative and connection whose commutator gives the field strength. Gauss constraints, gauge covariance, operator domains, and boundary conditions select the physical states and charges. The calculated quantities include gauge-invariant contractions of field strengths, traced Wilson loops, physical charges, and scattering amplitudes.

## Topic Equations

```math
D_\mu=\partial_\mu+igA_\mu
[D_\mu,D_\nu]=igF_{\mu\nu}
F_{\mu\nu}'=U F_{\mu\nu}U^{-1}
W(\gamma)=\operatorname{Tr}\,\mathcal P\exp\!\left(-ig\oint_\gamma A_\mu dx^\mu\right)
G^a\ket{\Psi_{\mathrm{phys}}}=0
```

## Physical Meaning

Gauge-related field configurations represent the same physical state. Observable quantities must therefore be gauge invariant, or transform covariantly within a construction whose final predictions are invariant. Gauge fixing chooses one representative without changing the physical equivalence class.

Changing the electromagnetic scalar and vector potentials by a gauge transformation changes their formulas but leaves electric and magnetic fields, phase-consistent amplitudes, and measured forces unchanged.

Renormalization adds a second kind of transformation: changing the scale at which the same theory is parametrized.

## Consequences Forced By The Relation

In a non-Abelian theory the field-strength matrix changes by conjugation. Traces of its products and closed Wilson loops are invariant. For electromagnetism the group is Abelian, so the field strength itself is unchanged. A flat connection can still have nontrivial holonomy on a multiply connected domain. The connection and the topology together determine this global information. The Gauss constraint ties matter charge to the divergence of the electric field. Transformations that act nontrivially at a boundary can carry charges and must be distinguished from gauge redundancies that vanish there.

## Domain Of The Construction

The gauge group, representation, matter content, dimension, and boundary conditions distinguish different physical theories. A measured interference phase includes the connection along the paths and the phases of the charged states. The traced holonomy is gauge invariant; an untraced non-Abelian holonomy transforms by conjugation at its base point.

## Invariance And Realization

Gauge-equivalent potentials give the same physical probabilities, invariant contractions of the field strength, and traced closed-loop observables. Curvature records the infinitesimal holonomy of the connection and cannot be removed by a local gauge choice. The physical state belongs to the constraint sector rather than to an arbitrary field-coordinate representation.

The gauge potential, local basis, gauge-fixing condition, and coordinate description may change. The gauge group, representation, matter content, dimension, and boundary conditions specify different physical theories. Topological sectors and boundary charges can survive even where the local field strength vanishes.

## Discriminating Consequences

A closed-loop phase or Wilson observable distinguishes nontrivial holonomy from a removable local gauge choice. Gauge-related descriptions give identical probabilities for the same physical preparation and observable. An additional field or interaction changes a gauge-invariant observable rather than only the gauge potential.

## Source Equations

- [arXiv:hep-th/0106242](https://arxiv.org/abs/hep-th/0106242)
- [arXiv:hep-th/0010277](https://arxiv.org/abs/hep-th/0010277)

## References For The Physical Derivation

- [G. S. Bali, QCD forces and heavy quark bound states, Appendix B: covariant derivative, curvature and gauge transformations.](https://arxiv.org/abs/hep-ph/0001312)
