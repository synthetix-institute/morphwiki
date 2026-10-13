# Electron microscope

A transmission electron microscope sends electrons, accelerated by about 200 kV, through a specimen a few tens of nanometres thick. Its images resolve columns of atoms 0.1 to 0.2 nm apart. The electron wavelength is a few picometres, so lens aberrations rather than diffraction set the resolution.

An electron of rest mass $m_0$ and charge $e$ accelerated through a potential difference $U$ gains kinetic energy $eU$. The relativistic relation $(pc)^2=(eU+m_0c^2)^2-(m_0c^2)^2$ fixes its momentum $p$, and the de Broglie relation gives the wavelength:

```math
\lambda=\frac{h}{\sqrt{2m_0eU\left(1+\dfrac{eU}{2m_0c^2}\right)}},\qquad
\lambda(200\,{\rm kV})=2.51\,{\rm pm}.
```

At 200 kV the electron moves at 0.70 $c$, and the nonrelativistic formula would give 2.74 pm, an error of 9 percent. At 300 kV the wavelength is 1.97 pm. Scattering angles from atomic spacings are then of order 10 mrad, so the electron optics works close to the axis.

A thin specimen barely absorbs the beam. It delays the electron wave by an amount proportional to the projected electrostatic potential $V_p(\mathbf x)$. The transmitted wave is $e^{i\sigma V_p}\approx1+i\sigma V_p$, where $\sigma=2\pi me\lambda/h^2$ with the relativistic mass $m$. At 200 kV, $\sigma=7.29\times10^{-3}$ rad per volt-nanometre. An ideal lens would reproduce $|1+i\sigma V_p|^2\approx1$, and the atoms would be invisible.

A real objective lens adds a phase $\chi(k)$ to the wave scattered at spatial frequency $k$, the scattering angle divided by $\lambda$. Defocus $\Delta f$ and spherical aberration $C_s$ give the leading terms. Interference with the unscattered beam then turns the phase delay into intensity, with image Fourier transform

```math
\chi(k)=\pi\Delta f\,\lambda k^2+\frac{\pi}{2}C_s\lambda^3k^4,\qquad
\widetilde I(\mathbf k)=\delta(\mathbf k)+2\sigma\widetilde V_p(\mathbf k)\sin\chi(k).
```

The factor $\sin\chi$ is the contrast transfer function in this sign convention. Scherzer chose the defocus $\Delta f=-\sqrt{4C_s\lambda/3}$, so that $\sin\chi$ stays close to $-1$ over a broad band while $\chi$ never falls below $-2\pi/3$. The lowest zero of $\sin\chi$ beyond that band gives the point resolution $d\approx0.66\,C_s^{1/4}\lambda^{3/4}$. For $C_s=1$ mm at 200 kV this gives $\Delta f\approx-58$ nm and $d\approx0.23$ nm. The diffraction limit for a 10 mrad aperture would be $0.61\lambda/\alpha\approx0.15$ nm.

Aberration correctors made from multipole lenses reduce $C_s$ and bring the resolution below 0.1 nm. A phase plate that shifts the unscattered beam by $\pi/2$ converts $\sin\chi$ into $\cos\chi$, the electron analogue of Zernike phase contrast in light microscopy. The linear relation holds only for weak phase objects with $\sigma V_p\ll1$. Thicker crystals scatter electrons several times and require dynamical calculations, and partial coherence of the beam damps the highest frequencies. For biological specimens radiation damage limits the dose, so the shot noise of the electron count limits contrast.

The instrument is a direct application of wave-particle duality: the same electrons that strike the detector one at a time form an interference pattern. The specimen potential enters as in the Born approximation of scattering theory, with single scattering from the projected potential.

## References For The Physical Derivation

- [B. Gamm, K. Schultheiss, R. R. Schroder and D. Gerthsen, Effect of a Physical Phase Plate on Contrast Transfer in an Aberration-Corrected Transmission Electron Microscope; weak-phase-object contrast transfer, spherical aberration, defocus and phase plates.](https://arxiv.org/abs/1009.4038)
