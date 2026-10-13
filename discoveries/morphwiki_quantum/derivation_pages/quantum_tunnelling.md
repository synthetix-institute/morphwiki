# Quantum tunnelling

A scanning tunnelling microscope holds a metal tip a few tenths of a nanometre above a conducting surface. A bias of a fraction of a volt drives about a nanoampere across the vacuum gap, although the electrons lack the energy to pass over it. Moving the tip by 0.1 nm changes the current by nearly a factor of ten. A rectangular barrier shows where this sensitivity comes from.

Let a particle of mass $m$ and energy $E$ meet a barrier of height $V_0>E$ occupying $0<x<a$. Outside the barrier the solutions are travelling waves with wave number $k=\sqrt{2mE}/\hbar$. Inside, the kinetic energy is negative, and the solutions grow or decay with $\kappa=\sqrt{2m(V_0-E)}/\hbar$:

```math
\psi(x)=\begin{cases}e^{ikx}+r\,e^{-ikx}, & x<0,\\
C e^{\kappa x}+D e^{-\kappa x}, & 0<x<a,\\
t\,e^{ikx}, & x>a.\end{cases}
```

Continuity of $\psi$ and $\psi'$ at both edges gives four linear equations for $r$, $C$, $D$ and $t$. The probability current $j=(\hbar/m)\operatorname{Im}(\psi^*\psi')$ is the same on both sides, so $|r|^2+|t|^2=1$. Solving for the transmitted fraction gives

```math
T=|t|^2=\left[1+\frac{V_0^2\sinh^2\kappa a}{4E(V_0-E)}\right]^{-1}
\\ \kappa a\gg1:\qquad T\approx\frac{16E(V_0-E)}{V_0^2}\,e^{-2\kappa a}.
```

The approximation holds for a thick barrier, where the decaying exponential inside dominates. The prefactor varies slowly with energy, while the exponent depends on the width and on the square root of the barrier height above $E$. For $E>V_0$ the hyperbolic sine becomes an ordinary sine. Transmission is then incomplete, except at the resonances $a\sqrt{2m(E-V_0)}/\hbar=n\pi$ where reflections from the two edges cancel. The amplitudes $r$ and $t$ for waves arriving from either side form the two-channel S-matrix of the barrier.

In the microscope the barrier height is approximately the work function of the metals, 4 to 5 eV above the Fermi level. With $\phi=4.5$ eV, the decay constant is $\kappa=1.09$ per ångström. The current at small bias is proportional to $e^{-2\kappa d}$ for a gap $d$, so a change of 0.1 nm alters it by a factor of 8.8. A height change of 10 pm, a small fraction of an atomic diameter, changes the current by about 24 per cent. Feedback that holds the current constant therefore follows the surface height with picometre precision. A full treatment adds the image-charge potential, which lowers and rounds the barrier, and the electronic states of tip and sample. These change the prefactor and the effective barrier height, but keep the exponential dependence on distance.

For a smoothly varying barrier, the local decay constant $\kappa(x)=\sqrt{2m[V(x)-E]}/\hbar$ replaces $\kappa$, and the exponent becomes an integral between the classical turning points. This WKB estimate requires $\kappa$ to change little over one decay length, $|d\kappa/dx|\ll\kappa^2$, and the exponent to be large:

```math
T\approx\exp\Big(-2\int_{x_1}^{x_2}\kappa(x)\,dx\Big),\\
2G=\frac{2\sqrt{2\mu E}\,b}{\hbar}\Big[\arccos\sqrt{R/b}-\sqrt{(R/b)(1-R/b)}\Big].
```

In alpha decay the barrier is the Coulomb repulsion between the alpha particle and a daughter nucleus of charge $Ze$. It extends from the nuclear radius $R$ to the turning point $b=2Ze^2/(4\pi\varepsilon_0E)$, where $E$ is the decay energy and $\mu$ the reduced mass. The integral gives the Gamow exponent $2G$ above. Take $R=1.2\,(A^{1/3}+4^{1/3})$ fm, with $A$ the mass number of the daughter. The exponents for uranium-238 ($E=4.27$ MeV) and polonium-212 ($E=8.95$ MeV) then differ by about 56. The exponent alone predicts a half-life ratio near $10^{24}$, and the measured ratio is $5\times10^{23}$. A factor of two in energy changes the lifetime by 24 orders of magnitude, which is the Geiger--Nuttall systematics. As $V_0$ grows without limit, the decay length vanishes and the walls of particle in a box are recovered.

## References For The Physical Derivation

- [C. Qi, A. N. Andreyev, M. Huyse, R. J. Liotta, P. Van Duppen and R. Wyss, On the Validity of the Geiger-Nuttall Alpha-Decay Law and its Microscopic Basis; barrier penetration and the energy dependence of alpha-decay half-lives.](https://arxiv.org/abs/1405.5633)
