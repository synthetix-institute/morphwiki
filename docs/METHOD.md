# Method

MorphWiki represents a scientific theory by the physical roles required to
produce a prediction. A second graph records the paper, equation, and local
context supporting each relation.

## Predictive Closure

At a chosen resolution, a state must retain enough information to determine
future observable probabilities:

```math
q(h_1)=q(h_2)
\Longrightarrow
p(y,t\mid h_1)=p(y,t\mid h_2).
```

Two histories that produce the same declared state must therefore give the same
future probabilities. A violation identifies a missing state coordinate or a
history-dependent evolution law.

Allowed transformations must also compose consistently. If two physically
equivalent paths `gamma_1` and `gamma_2` connect the same descriptions, then

```math
T_{\gamma_1}=T_{\gamma_2}.
```

A non-neutral closed composition records information absent from the endpoint
variables. Depending on the physics, the required enlargement can be a
connection, curvature, frustrated sector, boundary contribution, hidden state,
or memory kernel.

## Physical Identity

The common hierarchy is

```text
(Omega, Xi) -> M -> I_op=(M; C, R, P) -> I_real=(I_op; A)
```

`q in Xi` is a physical state at the chosen resolution. `Omega` is an operation
defined on `Xi`; their pair is the mechanism core `M`. Closure `C` fixes
normalization, positivity, domains, gauge restrictions, or constitutive
relations. The observable map `R` produces a probability, spectrum, correlator,
current, or other measured quantity. The protocol `P` fixes the order of
preparation, intervention, evolution, and measurement. The realization `A`
supplies fields, material, parameters, geometry, boundary values, drives,
devices, and trajectories.

The hierarchy records physical dependence rather than temporal order. A
derivation can add a missing clause, project a complete relation onto one
consequence, or rewrite the same mechanism in another representation.

## Physical Role Promotion

A realization parameter remains external while it selects a member of one fixed
mechanism. It is promoted when changing it changes the state space, operator
domain, dynamical map, closure, observable, or protocol:

```math
a\in A\quad\text{while}\quad
(\Xi,\Omega,C,R,P)_a=(\Xi,\Omega,C,R,P),
```

```math
a\longrightarrow X\in\{\Xi,\Omega,C,R,P\}
\quad\text{when the typed object }X\text{ changes}.
```

This criterion separates parameter variation from a change of theory. Moving a
wall can vary one realization. Changing the boundary condition can instead
select another self-adjoint domain and another spectrum. Quantizing a prescribed
field enlarges the Hilbert space and dynamics. Retaining environmental
correlations enlarges the state or introduces memory. Representing a detector as
an interacting subsystem turns apparatus into a quantum instrument.

## Quantum Specialization

A broad quantum mechanism has the form

```math
\Xi_Q=(\mathcal H,\mathcal D,\mathcal S),\qquad
\rho_0\in\mathcal S(\mathcal H),
```

```math
\rho_P=\mathcal E_P(\rho_0),\qquad
p(y\mid P)=\operatorname{Tr}(E_y\rho_P).
```

The Hilbert or Fock space, state class, and operator domain define `Xi_Q`. The
channel `E_P` describes evolution under protocol `P`. The positive operators
`E_y` define measurement outcomes. Normalization, complete positivity,
self-adjointness, gauge closure, and domain conditions enter through `C_Q`.

This form includes closed and open dynamics, projective and generalized
measurements, feedback, and quantum-information protocols. For a closed system
with a time-independent self-adjoint Hamiltonian,
`E_P(rho)=U(t)rho U(t)^dagger` with `U(t)=exp(-iHt/hbar)`.

## Transformations

Two physical descriptions are connected only after the retained relation is
specified:

```math
I_i=((\Omega_i,\Xi_i);C_i,R_i,P_i)
\xrightarrow{T}
I_j=((\Omega_j,\Xi_j);C_j,R_j,P_j).
```

The retained relation can be an amplitude, expectation value, operator algebra,
conserved current, probability law, correlator, or controlled approximation.
For state and output maps `alpha` and `beta`, compatibility is measured by

```math
\Delta_{\alpha,\beta}=\Omega_j\alpha-\beta\Omega_i.
```

A vanishing residual and matching observables identify the same retained
mechanism in another realization. A reproducible residual can become a new
physical term when it obeys a closure relation and changes an independent
observable. The promoted term may modify the operation, enlarge the state,
select a new domain, define a memory law, or require another realization.

## Construction Operations

The public constructor uses six operations:

1. `complete`: derive a missing closure, observable, or protocol;
2. `reattach`: place a law on another state space through explicit maps;
3. `compose`: join supported transformations;
4. `deform`: vary a parameter, boundary, scale, or representation while tracking an invariant;
5. `observe`: derive the measurement that distinguishes the construction;
6. `revise`: replace the physical role identified by a failed consequence.

A construction starts from a retained relation and a permitted change. It ends
with a complete physical identity, a realization, and a consequence that can be
compared with an alternative.

## Source Equations

The public book cites a paper only when one of its equations supports the topic
relation in its local source context. Identifier overlap alone does not create a
citation. Each accepted source record contains the paper identifier, equation,
nearby text, and the physical role supported by that equation.

The current local build contains 111 identifier-linked candidates and no
equation-level confirmations. Its public pages therefore contain no source
links. The full V2.1 build reads the source-card alignment and equation cards to
resolve those candidates.

## From Papers To A Field Map

1. Retain each equation with its paper and local context.
2. Identify the state space, operation, closure, observable, protocol, and realization.
3. Assign each topic by the physical relation supplied by its equations.
4. Record role promotions and the observable change associated with each one.
5. Recover transformations and name their invariant relation.
6. Compute the compatibility residual for proposed transfers.
7. Write source equations beside the physical claim they establish.
8. Compile the book and verify topic, equation, and citation preservation.

## Physical Standard

A quantum construction must satisfy the relevant domain and self-adjointness
conditions, positivity and normalization, complete positivity for channels,
gauge or constraint closure, dimensional consistency, and a defined probability
law. A proposed realization must also specify parameters, initial and boundary
data, controls, and a measurement that distinguishes it from the nearest
alternative.
