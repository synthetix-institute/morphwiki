# Scattering

Geiger and Marsden directed alpha particles at a thin gold foil and counted the scintillations at each angle. The count fell steeply with angle, as $1/\sin^4(\theta/2)$, yet a few particles were scattered backwards. The angular distribution of scattered particles measures the interaction. When the interaction is weak, it measures the Fourier transform of the potential.

A beam of particles with mass $m$ and wave vector $\mathbf k$ meets a potential $V(\mathbf r)$ of finite extent. Far from the target the stationary wave is the incident plane wave plus an outgoing spherical wave. The amplitude $f$ of the spherical wave fixes the number of particles per unit solid angle, divided by the incident flux:

```math
\psi(\mathbf r)\to e^{i\mathbf k\cdot\mathbf r}+f(\theta,\varphi)\frac{e^{ikr}}{r},\qquad
\frac{d\sigma}{d\Omega}=|f(\theta,\varphi)|^2.
```

The Schrödinger equation with this boundary condition can be rewritten as an integral equation. In it, the wave at the target acts as the source of the outgoing wave. If the potential changes the wave only slightly, the incident plane wave can be used inside the integral. This Born approximation gives the amplitude as the Fourier transform of the potential at the momentum transfer $\mathbf q=\mathbf k'-\mathbf k$:

```math
f_B(\mathbf q)=-\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf q\cdot\mathbf r}V(\mathbf r)\,d^3r,
\qquad |\mathbf q|=2k\sin\frac\theta2.
```

Each volume element of the target emits a secondary wave, and $f_B$ adds those waves with phases set by their path differences. Large angles require large $q$ and therefore probe short distances. The approximation is valid when $|V|\ll\hbar^2/(mb^2)$ for a potential of range $b$. At high energy the weaker condition $|V|b\ll\hbar v$, with $v$ the particle speed, suffices.

For a screened Coulomb, or Yukawa, potential $V=V_0e^{-\mu r}/r$, the integral is elementary. With $E=\hbar^2k^2/(2m)$ the amplitude and the unscreened limit are

```math
f_B=-\frac{2mV_0/\hbar^2}{\mu^2+q^2},\qquad
\frac{d\sigma}{d\Omega}\Big|_{\mu\to0}=\frac{V_0^2}{16E^2\sin^4(\theta/2)}.
```

With $V_0=Z_1Z_2e^2/(4\pi\varepsilon_0)$ the limit is the Rutherford cross-section. A finite range $1/\mu$ removes the divergence at small angles: the total cross-section is $\sigma=4\pi(2mV_0/\hbar^2)^2/[\mu^2(\mu^2+4k^2)]$, which is finite only for $\mu>0$. In a neutral atom the electrons screen the nucleus over roughly the atomic size. They set $\mu$ and cut off the forward peak that the bare Coulomb law would make infinite.

For 5 MeV alpha particles on gold, the Coulomb parameter $Z_1Z_2e^2/(4\pi\varepsilon_0\hbar v)$ is about 22, so the Born approximation is not justified. The Rutherford formula nevertheless holds, because the exact Coulomb amplitude differs from the Born amplitude only by a phase. Classical mechanics gives the same cross-section, which is why Rutherford's analysis succeeded. Deviations appear only when the closest approach in a head-on collision, $Z_1Z_2e^2/(4\pi\varepsilon_0E)$, reaches the nuclear radius. For 5 MeV alpha particles on gold this distance is 45 fm, far outside the nucleus.

For a target with an extended charge distribution, the point-charge Born amplitude acquires a factor $F(q)$. This form factor is the Fourier transform of the charge density. Electron scattering measured $F(q)$ for nuclei and for the proton. Its slope at small $q$, $F\approx1-q^2\langle r^2\rangle/6$, gives the mean square charge radius. The partial-wave description of the same process, with exact unitarity, is developed under S-matrix. The sum over secondary waves is the same superposition that produces wave interference.

## References For The Physical Derivation

- [C. F. Perdrisat, V. Punjabi and M. Vanderhaeghen, Nucleon Electromagnetic Form Factors; electron scattering, form factors and charge radii.](https://arxiv.org/abs/hep-ph/0612014)
