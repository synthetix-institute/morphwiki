# Quantum chromodynamics

**Physical domain:** Fields, constraints, and scale

## Mechanism

Quarks carry three colour components. Quantum chromodynamics couples them to eight gluon fields through a local SU(3) connection.

The colour connection specifies how quark amplitudes at neighbouring spacetime points are compared. Its action is inseparable from the colour representation of the quark: replacing the three-component carrier by an uncharged scalar would remove the very interaction being described.

The colour matrices do not commute. Their commutator enters the field strength, so the gluon field contributes to its own interactions as well as mediating interactions between quarks. With natural units $\hbar=c=1$, the quark field of flavour $f$ is $q_f$, its mass is $m_f$, the coupling is $g_s$, and $A_\mu$ is a matrix in colour space. The action joins their covariant Dirac motion to the energy of the colour field.

## Physical Construction

The state carrier is quark and gluon field states in the physical SU(3) constraint sector. The governing operation is the QCD action, with covariant Dirac motion and non-Abelian field strength. Gauss constraints, quark statistics and specified boundary conditions select physical states. The calculated observables are colour-singlet spectra, correlation functions and scattering cross sections.

## Topic Equations

The Hermitian colour generators and their normalization are given first. The metric has one positive timelike component and three negative spacelike components; $f$ labels quark flavours. In the final equation, $\mu$ is the renormalization scale and $n_f$ the number of active flavours. The sign of the commutator follows the stated covariant-derivative convention.

```math
[T^a,T^b]=if^{abc}T^c,\qquad\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}
A_\mu=A_\mu^aT^a,\qquad D_\mu=\partial_\mu+ig_s A_\mu
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+ig_s[A_\mu,A_\nu]
\mathcal L_{\mathrm{QCD}}=-\frac12\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu})+\sum_f\bar q_f(i\gamma^\mu D_\mu-m_f)q_f
\mu\frac{d g_s}{d\mu}=-\frac{11-2n_f/3}{16\pi^2}g_s^3+O(g_s^5)
```

## Physical Meaning

Physical observables include colour-singlet correlation functions, hadron energies and scattering cross sections. A Wilson loop follows a heavy test colour charge around a closed contour and traces over its colour index. Its large-time decay defines the static quark-antiquark potential after the self-energy convention is fixed.

In pure gauge theory a long confining flux tube gives an approximately linear static potential. With dynamical quarks the tube can break through pair creation. The observable must therefore be specified along with the matter content; the same loop notation does not impose the same long-distance force in both theories.

Changing resolution replaces short-distance fluctuations by effective couplings and operators. Heavy-quark effective descriptions preserve selected QCD amplitudes through matching, which supplies a concrete example of transferring a physical relation between different sets of variables.

## Consequences Forced By The Relation

Squaring the field strength produces terms cubic and quartic in the gauge potential. These are the three-gluon and four-gluon interactions. They disappear when the gauge algebra is replaced by an Abelian one; the covariant derivative alone is therefore not the whole distinction between QCD and electrodynamics. For $n_f$ active flavours with $11-2n_f/3$ positive, the weak-coupling beta function makes the coupling decrease as the energy scale increases. This permits short-distance perturbation theory. The same expansion loses accuracy when the coupling grows at hadronic scales; confinement is investigated through nonperturbative calculations rather than inferred by extrapolating the one-loop formula.

## Domain Of The Construction

The beta function is the one-loop result for SU(3) with fundamental quarks. Active flavour thresholds require matching. Hadron masses and long-distance forces additionally depend on quark masses and the nonperturbative state of the gauge field.

## Invariance And Realization

Gauge changes rotate colour coordinates while leaving colour-singlet probabilities unchanged. Matching to an effective theory preserves the amplitudes included at the stated order.

Quark masses, the coupling, temperature and volume change spectra and correlations. A different gauge group changes the interaction algebra itself.

## Discriminating Consequences

Static potentials, hadron spectra and short-distance cross sections probe different regimes of the same action and require the corresponding controlled approximations.

## References For The Physical Derivation

- [G. S. Bali, QCD forces and heavy quark bound states, sections 3-4 and Appendices B-C: colour fields, static potential and running coupling.](https://arxiv.org/abs/hep-ph/0001312)
