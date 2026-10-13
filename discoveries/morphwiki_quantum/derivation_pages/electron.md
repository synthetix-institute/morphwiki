# Electron

An electron held in a magnetic field precesses its spin slightly faster than it circulates in its cyclotron orbit. The small difference between the two frequencies fixes the electron's magnetic moment with a relative uncertainty of about $10^{-13}$. Through the $g$-factor, it tests the Dirac equation and quantum electrodynamics together.

The electron has charge $-e$, mass $m=0.511\,\mathrm{MeV}/c^2$ and spin one half, with spin operator $\mathbf S=\hbar\boldsymbol\sigma/2$ built from the Pauli matrices $\boldsymbol\sigma$. Its magnetic moment is written $\boldsymbol\mu=-g(e/2m)\mathbf S$. A classical rotating body with equal distributions of charge and mass has $g=1$. In the nonrelativistic limit of the Dirac equation, the two upper spinor components obey a Schrödinger equation with kinetic energy $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2/2m$. Here $\boldsymbol\pi=\mathbf p+e\mathbf A$ is the kinetic momentum in a vector potential $\mathbf A$:

```math
(\boldsymbol\sigma\cdot\boldsymbol\pi)^2=\boldsymbol\pi^2+e\hbar\,\boldsymbol\sigma\cdot\mathbf B,
\qquad
H=\frac{\boldsymbol\pi^2}{2m}+2\,\frac{e}{2m}\,\mathbf S\cdot\mathbf B.
```

The spin term arises because the components of $\boldsymbol\pi$ do not commute in a magnetic field $\mathbf B$: $[\pi_x,\pi_y]=-ie\hbar B_z$, and cyclically. Comparison with $H=-\boldsymbol\mu\cdot\mathbf B$ gives $g=2$. A Schrödinger equation with kinetic energy $\boldsymbol\pi^2/2m$ contains no such term, and the Dirac value is not inserted by hand. With $g=2$ the spin precession frequency $g\,eB/2m$ equals the cyclotron frequency $eB/m$, so the spin keeps a fixed angle to the velocity.

Coupling to the quantized electromagnetic field changes this value slightly. The electron emits and reabsorbs virtual photons, which modifies its response to a slowly varying external field. Schwinger's one-loop calculation of 1948 gave the anomaly $a_e=(g-2)/2=\alpha/2\pi\approx0.0011614$, with $\alpha$ the fine-structure constant. Higher orders form a series in $\alpha/\pi$ whose coefficients are known through the fifth power:

```math
a_e=\frac12\left(\frac{\alpha}{\pi}\right)-0.328479\left(\frac{\alpha}{\pi}\right)^2\\
+1.181241\left(\frac{\alpha}{\pi}\right)^3-1.9122\left(\frac{\alpha}{\pi}\right)^4+\dots
```

In a Penning trap the anomaly is measured directly as a ratio of frequencies. The cyclotron frequency is $\omega_c=eB/m$ and the spin precession frequency is $\omega_s=g\,eB/2m$, so their difference isolates $a_e$:

```math
\omega_a=\omega_s-\omega_c=a_e\,\omega_c,\qquad
\frac{g}{2}=1+\frac{\omega_a}{\omega_c}.
```

At $B=5.36$ T, $\omega_c/2\pi=150$ GHz and $\omega_a/2\pi=174$ MHz. A single electron in a cryogenic trap occupies the lowest cyclotron levels, and quantum jumps between these levels and between spin states are detected one at a time. The 2023 measurement found $a_e=0.00115965218059(13)$. The series summed through $(\alpha/\pi)^5$ gives $0.00115965218$ with the value of $\alpha$ from atom-recoil experiments. The remaining difference, about $4\times10^{-12}$, is of the size of the calculated contributions from virtual muons and hadrons. At this level the comparison is limited by the independent measurements of $\alpha$, which disagree among themselves by more than their stated uncertainties.

The Pauli description with $g=2$ requires fields that vary slowly over the reduced Compton wavelength $\hbar/mc=0.386$ pm and kinetic energies small compared with $mc^2$. Corrections of relative order $(v/c)^2$ give the hydrogen fine structure derived under Dirac equation. The radiative effects that shift $g$ also shift atomic levels, and the Lamb shift discussed in Quantum electrodynamics is their counterpart in hydrogen.

## References For The Physical Derivation

- [X. Fan, T. G. Myers, B. A. D. Sukra and G. Gabrielse, Measurement of the Electron Magnetic Moment; Penning-trap determination of g/2 from cyclotron and anomaly frequencies.](https://arxiv.org/abs/2209.13084)
- [T. Aoyama, T. Kinoshita and M. Nio, Revised and Improved Value of the QED Tenth-Order Electron Anomalous Magnetic Moment; coefficients of the series in alpha/pi and comparison with experiment.](https://arxiv.org/abs/1712.06060)
