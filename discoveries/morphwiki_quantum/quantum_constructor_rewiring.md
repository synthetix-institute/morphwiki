# Quantum Constructor Rewiring

- Readiness: `usable`
- Connections: `7`

## One operator, two roles: generator and observable

- Topics: Hamiltonian (quantum mechanics), Observable, Spectral theory
- Move: `dual_role_split`
- Invariant: the self-adjoint operator and its domain
- Mean route overlap: `0.894`

Read the same operator through its exponential for transport and through its spectral measure for energy readout.

Equations:

```math
U(t)=e^{-iHt/\hbar}
H=\int_{\sigma(H)}E\,dP_H(E)
```

Test: Check domain and self-adjointness once, then verify separately that the generated dynamics is unitary and that the spectral measure reproduces energy statistics.

## Schrodinger, Heisenberg, and path-integral representations

- Topics: Schrödinger picture, Heisenberg picture, Path integral formulation
- Move: `representation_change`
- Invariant: transition amplitudes and expectation values
- Mean route overlap: `0.959`

Move time dependence between states and operators, or replace the propagator by an action-weighted integral.

Equations:

```math
A_H(t)=U(t)^\dagger A_SU(t)
\langle q_f|U(t_f-t_i)|q_i\rangle=\int\mathcal Dq\,e^{iS[q]/\hbar}
```

Test: Specify domains, measure, boundary conditions, and regularization; the formulations are connected only where they yield the same amplitudes or correlators.

## Carrier factorization defines locality

- Topics: Quantum entanglement, Quantum information, Quantum field theory
- Move: `carrier_refactorization`
- Invariant: the global state and algebraic predictions
- Mean route overlap: `0.949`

Change the tensor-product or algebraic subsystem decomposition and track which observables remain local.

Equations:

```math
\mathcal H=\mathcal H_A\otimes\mathcal H_B
\rho_A=\operatorname{Tr}_B\rho_{AB}
```

Test: State the subsystem algebra or tensor factorization explicitly; entanglement and locality claims are not invariant under arbitrary refactorization.

## Constraints define physical readout

- Topics: Gauge theory, Quantum gravity, Measurement in quantum mechanics
- Move: `completion_attachment`
- Invariant: predictions on the physical state space
- Mean route overlap: `0.922`

Attach gauge or diffeomorphism closure before assigning outcome effects to physical observables.

Equations:

```math
\widehat{\mathcal C}_a|\psi_{\rm phys}\rangle=0
[\widehat O_{\rm phys},\widehat{\mathcal C}_a]|\psi_{\rm phys}\rangle=0
```

Test: Verify that candidate effects descend to the constrained or quotient state space; gauge-dependent quantities cannot be promoted directly to physical records.

## Boundary conditions are spectral control variables

- Topics: Particle in a box, Quantum tunnelling, Scattering, Spectral theory
- Move: `realization_change`
- Invariant: the differential operator family and probability conservation
- Mean route overlap: `0.916`

Change domain, boundary conditions, or asymptotic channels and follow the induced spectrum or transmission map.

Equations:

```math
H_D=-\frac{\hbar^2}{2m}\Delta_D+V
S:\mathcal H_{\rm in}\to\mathcal H_{\rm out}
```

Test: A claimed connection must identify the operator domain and conserved flux; similar-looking wave equations with different domains need not have comparable spectra.

## Measurement, channels, and error correction share an instrument calculus

- Topics: Quantum channel, Measurement in quantum mechanics, Quantum error correction
- Move: `protocol_attachment`
- Invariant: complete positivity and total probability
- Mean route overlap: `0.999`

Retain or discard the classical outcome of a quantum instrument, then condition a recovery channel on that outcome.

Equations:

```math
\mathcal I_i(\rho)=\sum_\alpha K_{i\alpha}\rho K_{i\alpha}^\dagger
\mathcal E=\sum_i\mathcal I_i
\mathcal R_i\circ\mathcal I_i
```

Test: Check complete positivity, normalization, and recovery fidelity with a reference system; state-update rules alone are insufficient.

## Duality and simulation require an intertwining map

- Topics: Quantum simulator, AdS/CFT correspondence, Quantum error correction
- Move: `carrier_transfer`
- Invariant: a selected operator algebra and its correlators
- Mean route overlap: `0.932`

Encode one carrier in another and require the encoding to intertwine the relevant dynamics and readouts.

Equations:

```math
VH_{\rm target}\simeq H_{\rm carrier}V
VO_{\rm target}\simeq O_{\rm carrier}V
```

Test: Validate more than state overlap: compare a generating set of observables or correlators and report the approximation regime and error bounds.
