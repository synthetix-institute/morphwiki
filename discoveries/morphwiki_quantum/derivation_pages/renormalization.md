# Renormalization

The strength of the electromagnetic interaction depends on the momentum transfer at which it is measured. Atomic experiments give $\alpha=1/137.036$, while electron-positron scattering at the Z-boson mass of 91 GeV requires $\alpha\approx1/129$. The difference is calculable. Virtual charged pairs screen a charge, and a probe with larger momentum transfer penetrates more of the screening cloud. Renormalization organizes this dependence on scale.

In quantum electrodynamics, loops of charged fermions modify the photon propagator, an effect called vacuum polarization. The interaction between two charges at momentum transfer $Q$ keeps its lowest-order form, with a modified coupling. Let fermion $f$ have mass $m_f$, charge $e_fe$ and $N_c$ colours. For $Q\gg m_f$, and with $\alpha$ defined at zero momentum transfer, the one-loop result is

```math
\alpha(Q)=\frac{\alpha}{1-\Delta\alpha(Q)},\\
\Delta\alpha(Q)=\frac{\alpha}{3\pi}\sum_fN_ce_f^2\left[\ln\frac{Q^2}{m_f^2}-\frac53\right].
```

Differentiating with respect to $\ln Q$ removes the constants and gives the rate of change of the coupling, the beta function. Integrating it between a reference scale $\mu$ and $Q$ gives

```math
\mu\frac{d\alpha}{d\mu}=\beta(\alpha)=\frac{2\alpha^2}{3\pi}\sum_fN_ce_f^2,\\
\frac{1}{\alpha(Q)}=\frac{1}{\alpha(\mu)}-\frac{2}{3\pi}\sum_fN_ce_f^2\ln\frac{Q}{\mu}.
```

The positive beta function expresses screening: the effective charge grows at short distance. Only fermions lighter than $Q$ contribute appreciably, while heavier ones decouple, so the sum changes at each mass threshold. A prediction written in terms of $\alpha(Q)$ does not depend on the reference scale $\mu$ used to define the coupling. This independence is the content of the renormalization group equation.

The three charged leptons give $\Delta\alpha_{\rm lep}(M_Z)=0.0314$ at one loop. Quarks are confined at low momentum, so their contribution is obtained from the measured cross section for $e^+e^-\to\mathrm{hadrons}$ through a dispersion relation, which gives $\Delta\alpha_{\rm had}\approx0.0277$. Together they yield $1/\alpha(M_Z)\approx137.036\times(1-0.059)\approx128.9$. Bhabha scattering at LEP observed the predicted increase of the coupling directly. This running value enters the W-mass relation of the Standard Model.

Wilson's formulation explains why the same structure governs very different systems. Integrating out fluctuations between a cutoff $\Lambda$ and $\Lambda/b$ changes the couplings $g_i$ of the remaining long-wavelength theory. Near a fixed point $g^*$, where all beta functions vanish, small deviations scale with powers of $b$:

```math
\beta_i(g^*)=0,\qquad \delta g_i(b)=b^{y_i}\,\delta g_i(1).
```

Directions with $y_i>0$ grow and are called relevant; those with $y_i<0$ shrink and are called irrelevant. Long-distance behaviour then depends only on the few relevant couplings. For this reason a liquid near its critical point and a uniaxial magnet share the same critical exponents.

The one-loop QED formula holds while $(\alpha/3\pi)\ln(Q^2/m^2)$ remains small. Taken literally with the electron loop alone, it would make $\alpha$ diverge near $10^{280}$ MeV, far beyond the range where the theory is applied. In Quantum chromodynamics the self-interaction of gluons reverses the sign of the beta function, and the strong coupling decreases at short distance.

## References For The Physical Derivation

- [F. Jegerlehner, The running fine structure constant alpha(E) via the Adler function; leptonic and hadronic contributions to the running of alpha.](https://arxiv.org/abs/0807.4206)


## Source Equations

- [arXiv:hep-ph/0106305](https://arxiv.org/abs/hep-ph/0106305)
- [arXiv:hep-th/0104197](https://arxiv.org/abs/hep-th/0104197)
