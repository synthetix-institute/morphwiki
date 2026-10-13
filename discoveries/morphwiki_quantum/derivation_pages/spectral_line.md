# Spectral line

The yellow light of a sodium lamp, examined with a high-resolution spectrometer, does not have one sharp frequency. Each line has a width and a shape. Part of the width comes from the finite lifetime of the excited atom, and part from the thermal motion of the emitting atoms. The two mechanisms produce different line shapes, with widths that differ by two orders of magnitude.

An atom in its excited state $\ket e$ decays to $\ket g$ by emitting into the continuum of electromagnetic modes. When the coupling to each mode is weak and the mode density varies smoothly near the transition frequency $\omega_0$, the excited amplitude decays exponentially. This is the Wigner--Weisskopf result. The emitted field inherits this time dependence, and its Fourier transform fixes the spectrum:

```math
c_e(t)=e^{-i\omega_0t-\gamma t/2},\qquad
I(\omega)\propto\Big|\int_0^\infty e^{i\omega t}c_e(t)\,dt\Big|^2=\frac{1}{(\omega-\omega_0)^2+\gamma^2/4}.
```

This Lorentzian has a full width at half maximum $\gamma$, equal to the inverse lifetime $1/\tau$. The decay rate follows from the transition dipole moment $d=|\langle g|e\mathbf r|e\rangle|$ by summing the emission probability over all field modes:

```math
\gamma=\frac{\omega_0^3d^2}{3\pi\varepsilon_0\hbar c^3},\qquad
\Delta\nu_{\rm nat}=\frac{\gamma}{2\pi}=\frac{1}{2\pi\tau}.
```

For the hydrogen $2p\to1s$ transition, $d=0.745\,ea_0$ and $\hbar\omega_0=10.2$ eV give $\gamma=6.3\times10^8\ \mathrm{s}^{-1}$, a lifetime of 1.6 ns. For the sodium D2 line at 589 nm the measured lifetime is 16.2 ns, so the natural width is 9.8 MHz. The cubic dependence on frequency makes spontaneous emission far slower for microwave transitions than for optical ones. The broadening is homogeneous: every atom has the same decay rate and the same centre frequency.

Thermal motion shifts the frequency measured in the laboratory. An atom with velocity component $v_z$ along the line of sight emits at $\omega_0(1+v_z/c)$, to first order in $v_z/c$. For atoms of mass $M$ at temperature $T$, the Maxwell distribution of $v_z$ is Gaussian, and so is the line:

```math
I_D(\omega)\propto\exp\Big[-\frac{Mc^2(\omega-\omega_0)^2}{2k_BT\omega_0^2}\Big],\qquad
\frac{\Delta\nu_D}{\nu_0}=\sqrt{\frac{8k_BT\ln2}{Mc^2}}.
```

For sodium vapour at 400 K the Doppler width is 1.5 GHz, about 150 times the natural width. This broadening is inhomogeneous: each atom keeps a narrow Lorentzian response centred at its own shifted frequency. Saturated-absorption spectroscopy sends two counter-propagating beams through the vapour. Both beams act on the same atoms only when $v_z\approx0$, which produces a feature much narrower than the Doppler profile at the line centre.

When both mechanisms act, the profile is their convolution, the Voigt profile. Its core is Gaussian when the Doppler width dominates, but its far wings remain Lorentzian. The Gaussian falls off as $\exp(-\delta^2)$ in the detuning $\delta$, whereas the Lorentzian falls only as $1/\delta^2$. Collisions add a further Lorentzian width proportional to the gas pressure, because each collision interrupts the phase of the emitted wave. The relation between width and lifetime is the Fourier relation between an energy distribution and the survival amplitude, discussed under spectral theory. The decay of a single atom, photon by photon, is described under quantum jump.
