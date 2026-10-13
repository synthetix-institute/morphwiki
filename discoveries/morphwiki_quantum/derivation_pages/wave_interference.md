# Wave interference

Electrons or molecules sent one at a time through two slits arrive at single points on a screen. After many arrivals the points form bright and dark fringes. The spacing of the fringes is fixed by the de Broglie wavelength and the geometry. The fringes disappear when anything in the surroundings records which slit was taken, even if the particle itself is not deflected.

Let $\psi_1(x)$ and $\psi_2(x)$ be the amplitudes at screen position $x$ for passage through slit 1 or slit 2 alone. With both slits open the amplitude is their sum, and the detection probability contains a cross term:

```math
P(x)=|\psi_1(x)|^2+|\psi_2(x)|^2+2\operatorname{Re}\big[\psi_1^*(x)\psi_2(x)\big].
```

For slits separated by $d$ and a screen at distance $D\gg d$, the two paths to $x$ differ in length by about $dx/D$. The relative phase is $2\pi dx/(\lambda D)$, with $\lambda=h/p$ for a particle of momentum $p$. The cross term therefore oscillates with period

```math
\Delta x=\frac{\lambda D}{d},\qquad \lambda=\frac{h}{p}.
```

This far-field form requires $D\gg d^2/\lambda$; closer to the slits the near-field pattern applies instead. The envelope of the fringes is the diffraction pattern of a single slit. A spread of velocities in the beam smears the higher-order fringes, because each velocity has its own spacing.

Arndt and coworkers diffracted C$_{60}$ fullerene molecules of mass 720 u, moving at about 220 m/s, through a grating with period 100 nm. The de Broglie wavelength is 2.5 pm, about four hundred times smaller than the molecule. The diffraction angle $\lambda/d$ is 25 microradians. At 1.25 m behind the grating the first-order peaks therefore lie 31 micrometres from the central peak, and the far-field condition holds by a wide margin.

Suppose passage through slit $j$ also changes another system, such as an emitted photon or a spin, into the state $\ket{E_j}$. The joint state after the slits is $\psi_1(x)\ket{E_1}+\psi_2(x)\ket{E_2}$. A screen that does not detect the marker averages over its states:

```math
P(x)=|\psi_1|^2+|\psi_2|^2+2\operatorname{Re}\big[\psi_1^*\psi_2\langle E_1|E_2\rangle\big],
\qquad \mathcal V=|\langle E_1|E_2\rangle|.
```

For equal intensities, the fringe visibility $\mathcal V$ equals the overlap of the two marker states. Orthogonal marker states remove the fringes completely, and the screen shows the sum of the two single-slit patterns. No momentum kick is needed; the loss comes from the correlation between path and marker. The trade-off between visibility and the information available about the path is the quantitative content of wave--particle duality. Measuring the marker in a basis that does not distinguish $\ket{E_1}$ from $\ket{E_2}$, and sorting arrivals by its outcome, recovers fringes, as in the quantum eraser experiment.

A hot molecule may emit one photon of wave number $k$ in a random direction. If the molecule was at one of two positions separated by $s$, the marker states have overlap

```math
\langle E_1|E_2\rangle=\int\frac{d\Omega}{4\pi}\,e^{ik\hat{\mathbf n}\cdot\mathbf s}=\frac{\sin ks}{ks}.
```

Photons with wavelengths much longer than $s$ leave the overlap close to one and the fringes intact. Photons with wavelengths comparable to $s$ or shorter carry path information and wash the fringes out. Hackermüller and coworkers heated fullerene molecules before they entered a Talbot--Lau interferometer. The visibility fell as thermal emission increased, in agreement with an overlap calculation of this kind summed over the emission spectrum. The experiment is a direct observation of quantum decoherence by the environment.

## References For The Physical Derivation

- [K. Hornberger, S. Gerlich, P. Haslinger, S. Nimmrichter and M. Arndt, Colloquium: Quantum interference of clusters and molecules; far-field and Talbot-Lau interference of fullerenes.](https://arxiv.org/abs/1109.5937)
- [L. Hackermüller, K. Hornberger, B. Brezger, A. Zeilinger and M. Arndt, Decoherence of matter waves by thermal emission of radiation; loss of fringe visibility by photon emission.](https://arxiv.org/abs/quant-ph/0402146)
