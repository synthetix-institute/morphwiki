# Quantum gravity

A black hole of one solar mass is predicted to emit thermal radiation at about sixty nanokelvin. That prediction comes from quantum fields on a classical curved spacetime. A theory in which the geometry itself is quantized does not yet exist in tested form. The scale at which it should matter follows from dimensional analysis. Planck's constant $\hbar$, Newton's constant $G$ and the speed of light $c$ form only one length, one time and one mass:

```math
l_P=\sqrt{\frac{\hbar G}{c^3}}=1.62\times10^{-35}\,{\rm m},\qquad
t_P=\frac{l_P}{c}=5.39\times10^{-44}\,{\rm s},\\
m_P=\sqrt{\frac{\hbar c}{G}}=2.18\times10^{-8}\,{\rm kg},\qquad
m_Pc^2=1.22\times10^{19}\,{\rm GeV}.
```

Near the Planck mass the Compton wavelength $\hbar/mc$ of a particle equals its Schwarzschild radius $2Gm/c^2$, up to a factor of order one. A probe localized to the Planck length would therefore form a black hole around itself. Gravitational corrections to a scattering amplitude at energy $E$ have relative size $(E/m_Pc^2)^2$. At the 13 TeV of the Large Hadron Collider this ratio is about $10^{-30}$.

The Hawking temperature can be derived in a few steps. Outside a mass $M$ the Schwarzschild metric has $g_{tt}=-(1-r_s/r)c^2$ with $r_s=2GM/c^2$. In a thermal state the imaginary time $\tau=it$ is periodic with period $\hbar/k_BT$. This follows from the Gibbs operator $e^{-\beta H}$ of quantum statistical mechanics, which evolves states in imaginary time. Near the horizon set $r=r_s+\rho^2/4r_s$. The Euclidean metric becomes

```math
ds^2\simeq\Big(\frac{\rho}{2r_s}\Big)^2c^2d\tau^2+d\rho^2,\qquad
\frac{\hbar}{k_BT_H}=\frac{4\pi r_s}{c}
\;\Rightarrow\; T_H=\frac{\hbar c^3}{8\pi GMk_B}.
```

This is a plane in polar coordinates with angle $c\tau/2r_s$. It is smooth at $\rho=0$ only if that angle has period $2\pi$, which fixes the period of $\tau$ and hence the temperature. Hawking obtained the same result from the mixing of positive and negative frequencies of a quantum field during collapse. For a solar mass $T_H=6.2\times10^{-8}$ K. This is far below the 2.7 K of the cosmic microwave background, so such holes absorb more radiation than they emit. Only holes lighter than about $4.5\times10^{22}$ kg, less than a lunar mass, are hotter than the background. The associated Bekenstein--Hawking entropy is $S=k_BA/4l_P^2$, with $A$ the horizon area, about $10^{77}k_B$ for a solar mass.

The calculation treats geometry as classical and matter fields as quantum. It is controlled when the horizon curvature is small on the Planck scale, that is for $M\gg m_P$. Other established results share this semiclassical status. Colella, Overhauser and Werner measured the gravitational phase shift of neutrons in an interferometer. Treating general relativity as an effective field theory gives calculable quantum corrections to the Newtonian potential at energies far below $m_Pc^2$, too small to measure.

A theory valid at the Planck scale itself is not established. Perturbative quantization of general relativity needs new counterterms at each loop order, so it loses predictive power there. Open questions include the final stage of evaporation and whether the radiation carries the information of what fell in. The microscopic origin of the entropy is also open in general. String theory, loop quantum gravity and the AdS/CFT correspondence give partial answers in restricted settings. None of them has been tested by experiment.

## References For The Physical Derivation

- [S. Carlip, Quantum Gravity: a Progress Report; Planck scales, black hole thermodynamics and the status of the approaches.](https://arxiv.org/abs/gr-qc/0108040)
- [C. P. Burgess, Quantum Gravity in Everyday Life: General Relativity as an Effective Field Theory; controlled low-energy quantum corrections.](https://arxiv.org/abs/gr-qc/0311082)
