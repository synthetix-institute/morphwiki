# S-matrix

A detector far from a target sees only outgoing waves. If the target cannot absorb, every particle that enters the interaction region must leave it again, and only the phase of each outgoing wave can change. The S-matrix records those changes. Probability conservation then limits how large a cross-section can be and ties the forward amplitude to the total number of scattered particles.

Consider a particle of wave number $k$ scattered by a spherically symmetric potential of finite range. Angular momentum is conserved, so each partial wave of angular momentum $\ell$ scatters independently. Outside the potential, the radial function $u_\ell(r)=rR_\ell(r)$ combines an incoming and an outgoing spherical wave. The interaction can change only the coefficient of the outgoing wave:

```math
u_\ell(r)\propto e^{-i(kr-\ell\pi/2)}-S_\ell\,e^{i(kr-\ell\pi/2)},\qquad
|S_\ell|=1\ \Rightarrow\ S_\ell=e^{2i\delta_\ell}.
```

Equal incoming and outgoing flux in each partial wave forces $|S_\ell|=1$. With several channels, such as inelastic excitation of the target, the same conservation becomes unitarity of the full matrix, $S^\dagger S=I$. The phase shift $\delta_\ell$ measures how far the outgoing wave is advanced or delayed relative to free motion. Subtracting the free wave, for which $S_\ell=1$, gives the scattering amplitude and the total cross-section:

```math
f(\theta)=\frac1k\sum_{\ell=0}^\infty(2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta),\\
\sigma=\frac{4\pi}{k^2}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell=\frac{4\pi}{k}\operatorname{Im}f(0).
```

Each partial wave contributes at most $4\pi(2\ell+1)/k^2$, the unitarity limit, reached when $\delta_\ell=\pi/2$. The last equality is the optical theorem: at $\theta=0$ every Legendre polynomial equals one, and the imaginary part of $f$ reproduces the sum. Physically, the forward scattered wave interferes destructively with the incident wave. It removes from the beam exactly the flux that appears at other angles, and this deficit is the shadow behind the target.

A hard sphere of radius $a$ forces the wave to vanish at $r=a$. For $\ell=0$ the outside solution is $\sin(kr+\delta_0)$, so $\delta_0=-ka$. Higher partial waves have $\delta_\ell\propto(ka)^{2\ell+1}$, because the centrifugal barrier keeps them away from the sphere, and they are negligible when $ka\ll1$. The cross-section has two limits:

```math
\sigma\to\frac{4\pi}{k^2}\sin^2ka\approx4\pi a^2\quad(ka\ll1),\qquad
\sigma\to2\pi a^2\quad(ka\gg1).
```

A wave much longer than the sphere cannot resolve its shape. It is scattered equally in all directions with amplitude $f=-a$, so the cross-section is four times the geometric area $\pi a^2$. At high energy, about $ka$ partial waves contribute and the sum approaches $2\pi a^2$. Half of it is reflected as a classical particle would be. The other half forms a diffraction peak in the forward direction, of angular width about $1/(ka)$. That peak is the shadow required by the optical theorem.

For any short-range potential at low energy, $\delta_0\approx-ka_s$ defines the scattering length $a_s$, and $\sigma\approx4\pi a_s^2$. In ultracold gases a magnetic field tunes $a_s$ through Feshbach resonances, where a bound state of another channel crosses the collision threshold. In one dimension the same unitarity gives $|r|^2+|t|^2=1$ for the reflection and transmission amplitudes of quantum tunnelling. When every phase shift is small, the amplitude becomes linear in the phase shifts. To first order in the potential it then coincides with the Born approximation treated under scattering.

## References For The Physical Derivation

- [C. Chin, R. Grimm, P. Julienne and E. Tiesinga, Feshbach Resonances in Ultracold Gases; s-wave phase shift, scattering length and its magnetic tuning.](https://arxiv.org/abs/0812.1496)
