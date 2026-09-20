# Quantum state

Preparing a spin along one axis fixes probabilities for measurements along every other axis. The information needed for those predictions can be collected in a density operator $\rho$. For a two-level system let $\boldsymbol\sigma=(\sigma_x,\sigma_y,\sigma_z)$ be the Pauli matrices and $\mathbf r$ the vector of their expectation values. The three components of $\mathbf r$ determine the state:

```math
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),\qquad |\mathbf r|\leq1.
```

The bound follows from positivity: the two eigenvalues are $(1\pm|\mathbf r|)/2$. A unit vector describes a pure preparation. An interior point describes a mixed state, which may arise from uncontrolled preparation or from ignoring a correlated partner. Different ensembles can produce the same density operator. A later experiment acting only on this spin cannot distinguish those ensembles unless additional information about the preparation is accessible.

A Stern--Gerlach measurement along a unit vector $\mathbf n$ has projectors $E_\pm=(I\pm\mathbf n\cdot\boldsymbol\sigma)/2$. The probability of each outcome is consequently

```math
p_\pm=\operatorname{Tr}(\rho E_\pm)=\frac12(1\pm\mathbf r\cdot\mathbf n).
```

The same state gives certainty along its preparation axis and an equal distribution along a perpendicular axis. The uncertainty therefore belongs to the relation between preparation and measurement. It is not evidence that a pure state is an unspecified classical direction. Measurements along three independent axes reconstruct the Bloch vector, while measurements along only one axis leave a disk of compatible states.

For a composite system the density operator also contains correlations. The singlet and an equal mixture of oppositely aligned spins both give $\rho_A=I/2$ for either individual spin, but they predict different joint measurements. A partial trace retains every expectation of an operator acting on subsystem $A$ alone. It need not retain the information required for subsequent interacting evolution, because the interaction can convert a joint correlation into a local expectation value.

```math
\langle O_A\rangle=\operatorname{Tr}_{AB}[\rho_{AB}(O_A\otimes I_B)]
=\operatorname{Tr}_A(\rho_A O_A),\qquad \rho_A=\operatorname{Tr}_B\rho_{AB}.
```

Thus the state required by a mechanism is fixed by the available measurements and subsequent interactions together. Local spin probabilities require $\rho_A$ at the present time; a prediction after coupling to $B$ generally requires the joint state or an independently specified preparation of $B$. This distinction is the physical reason to keep the carrier, interaction and preparation connected in the description.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.](https://arxiv.org/abs/1508.06951)


## Relations In The Original Papers

[arXiv:1508.06951, S3.Ex131](https://arxiv.org/html/1508.06951#S3.Ex131). The spectral probability of an observable is the trace of the density operator with its spectral projector. Density operators and projection-valued measurements; the Bloch-state example is derived in the chapter.
