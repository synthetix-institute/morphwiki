# Coherence (physics)

A Michelson interferometer illuminated by a filtered lamp shows fringes only while its two arms have nearly equal lengths. With a single-frequency laser, fringes persist over path differences of many metres. The fringe contrast as a function of the delay between the arms is a measurable property of the light, its first-order coherence.

Let $E(t)$ be the complex field amplitude at the detector, let one arm delay it by $\tau$, and let a balanced beam splitter recombine the two parts. Averaged over the fluctuations of a stationary source of intensity $I_0$, the detected intensity is

```math
I(\tau)=\frac{I_0}{2}\left[1+\operatorname{Re}g^{(1)}(\tau)\right],\qquad
g^{(1)}(\tau)=\frac{\langle E^*(t)E(t+\tau)\rangle}{\langle|E(t)|^2\rangle}.
```

As $\tau$ changes over one optical period, $I$ oscillates between maxima and minima with visibility $V=|g^{(1)}(\tau)|$. By the Wiener--Khinchin theorem, $g^{(1)}$ is the Fourier transform of the normalized power spectrum $S(\omega)$. A Lorentzian line centred at $\omega_0$ with full width $\Gamma$ at half maximum gives

```math
g^{(1)}(\tau)=\int S(\omega)\,e^{-i\omega\tau}d\omega=e^{-i\omega_0\tau-\Gamma|\tau|/2}.
```

Fringes therefore fade once the delay exceeds a time of order $1/\Gamma$. In terms of path difference, light of wavelength $\lambda$ and spectral width $\Delta\lambda$ has a coherence length of order $\lambda^2/\Delta\lambda$. A filter 1 nm wide at 600 nm gives about 0.36 mm, and a laser line 1 MHz wide gives about 300 m. The same quantity describes one photon in a two-path interferometer. There the visibility equals $2|\rho_{LR}|$, twice the coherence between the paths in the density matrix, and quantum decoherence reduces it.

Intensity correlations distinguish sources with identical spectra. Hanbury Brown and Twiss correlated the photocurrents of two detectors and found correlated intensity fluctuations in thermal light. Chaotic light is the sum of fields from very many independent emitters, so the field has Gaussian statistics. Its fourth moment then factorizes into pairs of second moments, which gives the Siegert relation:

```math
g^{(2)}(\tau)=\frac{\langle I(t)I(t+\tau)\rangle}{\langle I\rangle^2}=1+|g^{(1)}(\tau)|^2,
\qquad g^{(2)}(0)=\frac{\langle n(n-1)\rangle}{\langle n\rangle^2}=2.
```

At zero delay the intensity correlation is twice the uncorrelated value; in photon terms, thermal light arrives in bunches. The same value 2 follows from the geometric distribution of photon numbers $n$ in one thermal mode. The excess lasts about one coherence time, and a detector much slower than that averages most of it away. Hanbury Brown and Twiss nevertheless measured how the excess declined with the separation of two telescopes, and obtained the angular diameter of Sirius in 1956.

A classical intensity satisfies $\langle I^2\rangle\geq\langle I\rangle^2$, which forces $g^{(2)}(0)\geq1$, and an ideal laser beam gives exactly one. Values below one, which no fluctuating classical wave can produce, come from single-photon sources treated under photon. First-order coherence cannot separate these cases, because sources with the same spectrum give the same fringes.

## References For The Physical Derivation

- [G. Baym, The Physics of Hanbury Brown--Twiss Intensity Interferometry: From Stars to Nuclear Collisions; first- and second-order coherence and stellar interferometry.](https://arxiv.org/abs/nucl-th/9804026)
