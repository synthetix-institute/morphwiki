# Commutator

## Central Claim
A commutator measures the physical consequence of exchanging two operations: it governs joint measurability, generated motion, and the leading difference between reversed protocols.

## Formal Role
For two operators defined on a common domain, [A,B]=AB-BA compares the two possible orders. For observables, a nonzero commutator obstructs a common sharp spectral resolution and enters uncertainty bounds. For a Hamiltonian H, [H,A] gives the dynamical change of A in the Heisenberg picture. For short control pulses, [A,B] is the first term that distinguishes the protocols exp(epsilon A)exp(epsilon B) and exp(epsilon B)exp(epsilon A). The same algebraic object therefore connects compatibility, dynamics, and order-sensitive response.

## Formal Contribution
- The page reorganizes the topic by the quantum construction that relates preparation, state space, operator action, spectral decomposition, and probability.
- It separates physical carriers such as particles, waves, fields, qubits, and detectors from the mathematical roles they play in Hilbert space.
- It treats non-commutativity as a constraint on which observables can share a spectral resolution.
- It makes cross-formulation analogy testable: another formulation should preserve state space, admissible transformations, readout basis, and compatibility relations.

## Mechanism Form
- Both operators are defined on a stated common domain.
- The ordered products AB and BA are formed on that domain.
- Their difference determines joint spectral compatibility or order sensitivity.
- A state and observable convert the algebraic difference into a measurable bound or response.

## Topic-Native Formal Skeleton
This is a standard topic-level skeleton used to make the mechanism readable; it is not a raw parser excerpt.
```math
[A,B]=AB-BA
\frac{dA}{dt}=\frac{i}{\hbar}[H,A]+\left(\frac{\partial A}{\partial t}\right)
\Delta A\,\Delta B\geq\frac12|\langle[A,B]\rangle|
e^{\epsilon A}e^{\epsilon B}e^{-\epsilon A}e^{-\epsilon B}=I+\epsilon^2[A,B]+O(\epsilon^3)
```

## Mechanism Roles
- **state:** common operator domain; prepared quantum state
- **operator:** ordered product; commutator; Hamiltonian generator
- **spectrum:** common eigenspace; uncertainty bound; order-dependent response
- **boundary:** operator domain; control-pulse duration
- **incompatibility:** nonzero commutator; absence of common sharp refinement
- **protocol:** AB ordering; BA ordering; short-pulse sequence

## Representation-Stable Content
- The commutator transforms covariantly under a simultaneous unitary change of representation.
- Joint spectral compatibility is unchanged by a consistent representation change.
- The leading order-sensitive response survives when different physical controls realize the same operator algebra.

## Representation-Dependent Content
- The matrix entries, basis, carrier, and physical implementation of the two operations may change.
- Domains can change the meaning of formal commutation relations for unbounded operators.
- The observable consequence depends on the prepared state and on how the operator difference is read out.

## Validation Checks
- Reversing two calibrated operations isolates the part of the response proportional to their commutator.
- A commuting control pair removes the order-sensitive contribution without changing the individual operations.
- Agreement requires the same domain and the same measured observable, not merely similar operator notation.
