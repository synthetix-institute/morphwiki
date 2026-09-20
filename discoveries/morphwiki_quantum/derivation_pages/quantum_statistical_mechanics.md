# Quantum statistical mechanics

Thermal equilibrium assigns probabilities to quantum energy states while respecting the quantities that can be exchanged with the surroundings. For a system that exchanges energy with a large reservoir at temperature $T$ but has fixed particle number, the canonical state is determined by the Hamiltonian $H$:

```math
\rho_\beta=\frac{e^{-\beta H}}{Z},\qquad
Z=\operatorname{Tr}e^{-\beta H},\qquad \beta=(k_BT)^{-1}.
```

The trace sums over the actual many-particle state space, including exchange statistics and boundary conditions. It is not an independent classical distribution imposed on particle positions. Derivatives of the same partition function connect average energy and fluctuations:

```math
\langle H\rangle=-\partial_\beta\log Z,\qquad
\operatorname{Var}H=\partial_\beta^2\log Z,\qquad
C=\frac{\operatorname{Var}H}{k_BT^2}.
```

The last equality holds for a temperature-independent Hamiltonian in the canonical ensemble. It explains why equilibrium energy fluctuations measure the heat capacity: both are responses of the same probability weights to temperature. A different ensemble constrains different fluctuations and must be analyzed separately.

For independent modes of energy $\epsilon$ exchanging particles with a reservoir at chemical potential $\mu$, set $z=\exp[-\beta(\epsilon-\mu)]$. A fermionic mode contributes $1+z$ to the grand partition function because only occupations zero and one are allowed. A bosonic mode contributes the geometric sum $(1-z)^{-1}$ when $z<1$. Differentiation gives

```math
\overline n_F=\frac{1}{e^{\beta(\epsilon-\mu)}+1},\qquad
\overline n_B=\frac{1}{e^{\beta(\epsilon-\mu)}-1}.
```

The sign difference follows from the allowed state occupations. It produces Fermi filling and Bose enhancement before a specific interaction is added. In the dilute limit both expressions approach the Maxwell--Boltzmann weight. Interactions generally prevent factorization into independent mode contributions, although an effective quasiparticle description may recover it approximately.

For a single harmonic mode, the same sum gives $Z=[2\sinh(\beta\hbar\omega/2)]^{-1}$ and mean energy $(\hbar\omega/2)\coth(\beta\hbar\omega/2)$. The mean approaches the zero-point energy as temperature tends to zero; quadrature fluctuations persist while the energy variance vanishes. At high temperature the mean energy approaches $k_BT$. This links the oscillator algebra to thermodynamic response through the choice of preparation.

Equilibrium statistics do not specify the rate of approach to equilibrium. Relaxation requires dynamics, reservoir coupling and sometimes additional conserved quantities. A Gibbs state can describe stationary observables while giving no information about a transport coefficient or memory time. Constructing those predictions requires extending the equilibrium description by the corresponding physical evolution.

## References For The Physical Derivation

- [S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold atomic Fermi gases; ideal and interacting quantum gases.](https://arxiv.org/abs/0706.3360)


## Relations In The Original Papers

[arXiv:1110.3234v1, S2.E27](https://arxiv.org/html/1110.3234v1#S2.E27). A thermal harmonic mode has a geometric distribution of number-state populations. The single-mode bosonic example, not the interacting Fermi-gas discussion.
