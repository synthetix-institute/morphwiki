# Quantum electrodynamics

In the Dirac theory of hydrogen, the $2S_{1/2}$ and $2P_{1/2}$ levels have exactly equal energies. In 1947 Lamb and Retherford drove microwave transitions between them and found $2S_{1/2}$ higher by about 1000 MHz. The shift arises because the electron is coupled to the quantized electromagnetic field. Quantum electrodynamics treats that field as a dynamical quantum system rather than as a prescribed potential.

In natural units $\hbar=c=1$, let $\psi$ be the electron field with mass $m$ and charge $q=-e$, and let $A_\mu$ be the electromagnetic potential. The theory is defined by the Lagrangian density

```math
\mathcal L_{\rm QED}=-\frac14F_{\mu\nu}F^{\mu\nu}+\bar\psi(i\gamma^\mu D_\mu-m)\psi,\\
D_\mu=\partial_\mu+iqA_\mu,\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
```

Invariance under the local phase change $\psi\to e^{-iq\chi}\psi$, together with $A_\mu\to A_\mu+\partial_\mu\chi$, fixes the coupling term $-qA_\mu\bar\psi\gamma^\mu\psi$. The current $j^\mu=q\bar\psi\gamma^\mu\psi$ is conserved and is the source in Maxwell's equations, $\partial_\mu F^{\mu\nu}=j^\nu$. Gauge invariance also implies the Ward--Takahashi identity, which makes charge renormalization the same for every charged particle. Perturbation theory in $\alpha=e^2/4\pi\approx1/137$ describes emission, absorption and exchange of photons. For a bound electron, emission followed by reabsorption of a photon shifts the energy.

Welton's estimate shows where the shift comes from. Zero-point fluctuations of the field shake the electron, so it samples the Coulomb potential $V$ over a small random displacement $\delta\mathbf r$. Averaging $V$ over that motion adds $\frac16\langle\delta r^2\rangle\nabla^2V$. A field mode of angular frequency $\omega$ drives a displacement proportional to $1/\omega^2$, and the sum over modes gives a logarithm. With $\hbar$ and $c$ restored,

```math
\langle\delta r^2\rangle=\frac{2\alpha}{\pi}\left(\frac{\hbar}{mc}\right)^2
\ln\frac{\omega_{\max}}{\omega_{\min}},\\
\Delta E_{2S}=\frac16\langle\delta r^2\rangle\langle\nabla^2V\rangle
=\frac{\alpha^5mc^2}{6\pi}\ln\frac{\omega_{\max}}{\omega_{\min}}.
```

The last step uses $\nabla^2V=4\pi\alpha\hbar c\,\delta^3(\mathbf r)$ for the Coulomb potential and $|\psi_{2S}(0)|^2=1/8\pi a_0^3$, with $a_0$ the Bohr radius. Only S states have a nonzero density at the nucleus, so $2P_{1/2}$ is not shifted at this order. The upper limit is $\hbar\omega_{\max}\approx mc^2$, where the nonrelativistic treatment fails. The lower limit is set by atomic binding, because the electron does not respond freely to slower fields. Bethe's 1947 calculation used an average excitation energy of about 17.8 Rydberg, or 242 eV.

With $\alpha^5mc^2/6\pi h=135.6$ MHz and a logarithm of 7.65, the estimate is about 1040 MHz, with $2S_{1/2}$ above $2P_{1/2}$. The modern value, 1057.8 MHz, requires a relativistic treatment of the high-frequency modes and further terms. In vacuum polarization, virtual electron-positron pairs screen the proton's charge beyond the electron Compton wavelength, and this lowers $2S$ by 27 MHz. The anomalous magnetic moment of the Electron and nuclear recoil also contribute.

Once the electron mass and charge are fixed by measurement, every term is finite; the procedure is described under Renormalization. The expansion assumes $Z\alpha\ll1$. In heavy hydrogen-like ions the electron must be treated to all orders in the nuclear field, and the same theory is tested there in a strong-field regime.

## References For The Physical Derivation

- [M. I. Eides, H. Grotch and V. A. Shelyuto, Theory of Light Hydrogenlike Atoms; self-energy, vacuum polarization and other contributions to the Lamb shift.](https://arxiv.org/abs/hep-ph/0002158)
