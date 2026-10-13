# Quantum chromodynamics

Electrons scattered from protons at large momentum transfer behave as if they struck nearly free point-like quarks. At low momentum transfer the same quarks are never observed in isolation. Both facts follow from the dependence of the strong coupling on the resolution scale. Quantum chromodynamics is an $SU(3)$ gauge theory. Each quark field $q_f$ of flavour $f$ and mass $m_f$ has three colour components. Eight gluon fields $A^a_\mu$ act on them through generators $T^a$ with $[T^a,T^b]=if^{abc}T^c$ and $\operatorname{Tr}T^aT^b=\delta^{ab}/2$. In natural units $\hbar=c=1$,

```math
\mathcal L=-\frac12\operatorname{Tr}F_{\mu\nu}F^{\mu\nu}
+\sum_f\bar q_f\big(i\gamma^\mu D_\mu-m_f\big)q_f,\\
D_\mu=\partial_\mu-ig_sA^a_\mu T^a,\qquad
F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu-ig_s[A_\mu,A_\nu].
```

Squaring the commutator term gives three-gluon and four-gluon vertices, so gluons carry colour themselves. Virtual quarks and gluons make the effective coupling depend on the momentum scale $\mu$ at which it is measured. At one loop,

```math
\mu\frac{dg_s}{d\mu}=-\frac{\beta_0}{16\pi^2}g_s^3,\qquad
\beta_0=\frac{11}{3}C_A-\frac43T_Fn_f=11-\frac23n_f,
```

with $C_A=3$ the quadratic Casimir of the gluon representation, $T_F=1/2$ the normalization of the quark generators, and $n_f$ the number of quark flavours light compared with $\mu$. The two signs have a physical origin. A quark loop polarizes the vacuum as an electron loop does in electrodynamics: virtual pairs screen a test charge. In a background colour-magnetic field, a massless field of spin $s$ contributes in proportion to $(-1)^{2s}[(2s)^2-1/3]$. The term $-1/3$ is the diamagnetic response of orbital motion, and $(2s)^2$ is the paramagnetic response of the spin. The factor $(-1)^{2s}$ is the sign of a fermion loop.

For gluons, $s=1$ gives $4-1/3=11/3$, and the spin term dominates. A Dirac quark gives $-2/3$ per flavour. The vacuum then acts as a medium with magnetic permeability above one. Relativistic invariance makes its dielectric constant the inverse, below one, so a colour charge is antiscreened. In terms of $\alpha_s=g_s^2/4\pi$ the equation integrates to

```math
\alpha_s(Q^2)=\frac{\alpha_s(\mu^2)}{1+\frac{\beta_0}{4\pi}\alpha_s(\mu^2)\ln(Q^2/\mu^2)}
=\frac{4\pi}{\beta_0\ln(Q^2/\Lambda^2)}.
```

With five light flavours $\beta_0=23/3$. Starting from the measured $\alpha_s=0.118$ at the $Z$ mass, $91.2$ GeV, the one-loop formula gives $\alpha_s=0.173$ at 10 GeV and $0.088$ at 1 TeV. Determinations from tau decays, quarkonia, jet rates and the $Z$ width follow this decrease. The one-loop scale is $\Lambda\approx90$ MeV. Higher orders and the renormalization scheme change $\Lambda$, so its value is quoted with both specified. Asymptotic freedom requires $\beta_0>0$, that is at most sixteen flavours.

The formula holds while $\alpha_s$ is small. Its divergence as $Q$ approaches $\Lambda$ marks the breakdown of perturbation theory, not a measured infinity. Confinement and hadron masses are computed by lattice simulation. There the Wilson loop of a static quark--antiquark pair gives a potential that grows linearly with separation. The slope, the string tension, is close to 1 GeV per femtometre, until pair creation breaks the flux tube. A similar tension fixes the slope of meson Regge trajectories, which motivated the string models described under string theory. The underlying covariant derivative is derived under gauge theory.

## References For The Physical Derivation

- [A. Deur, S. J. Brodsky and G. F. de Teramond, The QCD Running Coupling; beta function, running of alpha_s and its measurements.](https://arxiv.org/abs/1604.08082)
- [F. Wilczek, Asymptotic Freedom: From Paradox to Paradigm; antiscreening by gluons and its physical interpretation.](https://arxiv.org/abs/hep-ph/0502113)
- [G. S. Bali, QCD forces and heavy quark bound states; static potential and string tension from Wilson loops.](https://arxiv.org/abs/hep-ph/0001312)
