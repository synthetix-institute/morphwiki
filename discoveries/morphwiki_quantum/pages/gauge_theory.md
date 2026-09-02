# Gauge theory

## Central Claim
Gauge theory defines how internal states are compared at different spacetime points: a connection relates neighboring frames, and curvature records the path dependence that no single gauge choice can remove.

## Formal Role
A local gauge transformation changes the field coordinates used at each point without changing the physical state. Ordinary derivatives compare fields in different local frames and therefore cease to transform covariantly. The gauge connection repairs that comparison. Its commutator gives the field strength, while Wilson loops measure the accumulated transport around a closed path. Gauss constraints select physical states and charges. The connection is representation dependent; curvature, loop observables, and gauge-invariant amplitudes carry the physical content.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- A local symmetry group acts on matter or field variables.
- A connection defines covariant comparison between neighboring points.
- The commutator of covariant derivatives gives the field strength.
- Constraints remove gauge-equivalent descriptions from the physical state space.
- Wilson loops, charges, scattering amplitudes, or field strengths provide observables.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
D_\mu=\partial_\mu+igA_\mu
[D_\mu,D_\nu]=igF_{\mu\nu}
W(\gamma)=\operatorname{Tr}\,\mathcal P\exp\left(ig\oint_\gamma A_\mu dx^\mu\right)
G^a|\Psi_{\mathrm{phys}}\rangle=0
```

## Mechanism Roles
- **state:** gauge-equivalence class; matter field; physical constraint sector
- **operator:** covariant derivative; connection; Gauss constraint
- **spectrum:** charge sector; Wilson loop; gauge-invariant amplitude
- **boundary:** gauge choice; bundle patch; boundary charge
- **incompatibility:** curvature; nontrivial holonomy; constraint anomaly
- **protocol:** parallel transport; closed-loop transport; gauge fixing

## Representation-Stable Content
- Gauge-equivalent potentials give the same gauge-invariant amplitudes, field strengths, charges, and loop observables.
- Curvature records the infinitesimal holonomy of the connection and cannot be removed by a local gauge choice.
- The physical state belongs to the constraint sector rather than to an arbitrary field coordinate representation.

## Representation-Dependent Content
- The gauge potential, local basis, gauge-fixing condition, and coordinate description may change.
- The gauge group, representation, matter content, dimension, and boundary conditions specify different physical theories.
- Topological sectors and boundary charges can survive even where the local field strength vanishes.

## Validation Checks
- A closed-loop phase or Wilson observable distinguishes nontrivial holonomy from a removable local gauge choice.
- Gauge-related descriptions must give identical probabilities for the same physical preparation and readout.
- A proposed extra field or interaction must change a gauge-invariant observable rather than only the gauge potential.
