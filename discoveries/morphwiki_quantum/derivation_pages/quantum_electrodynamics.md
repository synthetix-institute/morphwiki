# Quantum electrodynamics

**Physical domain:** Fields, constraints, and scale

## Mechanism

An electromagnetic field can exchange energy and momentum with charged particles. Quantum electrodynamics describes both the charged Dirac field and the electromagnetic field as dynamical quantum degrees of freedom.

Treating the potential as prescribed describes motion in an external field. Allowing the field to fluctuate permits emission, absorption and virtual photon exchange. The additional dynamical variables change which processes the theory can predict.

In natural units $\hbar=c=1$, let $\psi$ be the charged Dirac field, $m$ its mass, $q$ its signed coupling, and $A_\mu$ the electromagnetic potential. Local phase covariance replaces the ordinary derivative in the Dirac equation by $D_\mu$. Expanding that derivative gives the current-potential interaction. The field-strength term supplies the electromagnetic dynamics, so radiation and recoil are calculated within one action rather than prescribed independently.

## Physical Construction

The state carrier is Dirac and electromagnetic field states satisfying the Gauss constraint. The governing operation is the minimally coupled Dirac-Maxwell action and its quantized evolution. Charge conservation, fermionic statistics and gauge constraints restrict amplitudes. The calculated observables are emission and scattering probabilities, energy shifts and electromagnetic response.

## Topic Equations

The metric is (+,-,-,-). The current j^mu is the electric current in this convention. Local phase transformations change psi and A_mu together.

```math
D_\mu=\partial_\mu+iqA_\mu,\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu
\mathcal L_{\mathrm{QED}}=-\frac14F_{\mu\nu}F^{\mu\nu}+\bar\psi(i\gamma^\mu D_\mu-m)\psi
j^\mu=q\bar\psi\gamma^\mu\psi,\qquad\partial_\mu F^{\mu\nu}=j^\nu
\psi'=e^{-iq\chi}\psi,\quad A_\mu'=A_\mu+\partial_\mu\chi,\quad F_{\mu\nu}'=F_{\mu\nu}
k_\mu\Gamma^\mu(p+k,p)=S^{-1}(p+k)-S^{-1}(p)
```

## Physical Meaning

The U(1) connection acts by multiplication, so its components commute and the field strength contains no potential commutator. The classical gauge-field action is quadratic. Photon-photon scattering nevertheless arises through charged-particle loops; absence of a classical photon self-coupling does not mean absence of that quantum process.

A calculation of photon emission can replace a polarization vector by the photon momentum. For a complete on-shell amplitude the resulting longitudinal contribution vanishes. Failure of that cancellation exposes a missing diagram or an inconsistent approximation.

Replacing U(1) by a non-Abelian colour group changes this calculation at the level of the field strength and adds direct gauge-field interactions. The distinction is an algebraic change with physical consequences, not a change of particle names.

## Consequences Forced By The Relation

The antisymmetry of F makes the divergence of Maxwell's equation vanish on its left-hand side, giving conservation of electric current. The Dirac equation and its adjoint give the same continuity relation. Agreement of these two calculations connects matter evolution to the electromagnetic source. For the final identity, $S$ is the full electron propagator and $\Gamma$ is the proper vertex with the overall charge removed. The Ward--Takahashi relation ties a longitudinal photon insertion to the change in inverse propagator. Radiative corrections to the vertex and the electron propagator must respect it together.

## Domain Of The Construction

Gauge fixing is needed to invert the photon kinetic operator in perturbation theory. Observable probabilities are independent of that choice when the state preparation and calculation are treated consistently. A prescribed classical potential is an approximation in which the corresponding field degrees of freedom are not evolved quantum mechanically.

## Invariance And Realization

A simultaneous local phase change of the charged field and gauge transformation of the potential preserves current conservation and physical probabilities.

Replacing a classical field by a quantized field permits its fluctuations and recoil to affect charged matter. Coupling and mass values determine numerical predictions within the theory.

## Discriminating Consequences

The Ward--Takahashi identity compares independently calculated vertex and propagator corrections; an inconsistent truncation can violate it even when both calculations are finite.

## References For The Physical Derivation

- [A. Grozin, Lectures on QED and QCD, sections 3.1-3.7: Lagrangian, Ward identity and charge renormalization.](https://arxiv.org/abs/hep-ph/0508242)
