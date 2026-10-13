# Applications of quantum mechanics

*Historical, bibliographic or interpretive entry.*

Several widespread technologies work only because energy levels are discrete and transitions between them follow quantum rules. Lasers, magnetic resonance imaging, atomic clocks and transistors are the best known. Two of them show the physics in a single relation each.

Laser. In 1917 Einstein showed that radiation can stimulate an atom in its upper level $2$ to emit a photon of the same frequency, direction and phase as the incident one. Requiring thermal equilibrium with Planck's radiation law fixes the ratio of spontaneous to stimulated emission. Amplification then requires a positive gain coefficient $g(\nu)$:

```math
\frac{A_{21}}{B_{21}}=\frac{8\pi h\nu^3}{c^3},\qquad
g(\nu)=\sigma(\nu)\Bigl(N_2-\frac{g_2}{g_1}N_1\Bigr)>0 .
```

Here $A_{21}$ is the spontaneous emission rate, $B_{21}$ the stimulated emission coefficient per unit spectral energy density, $\sigma(\nu)$ the transition cross section, $N_{1,2}$ the level populations and $g_{1,2}$ their degeneracies. In thermal equilibrium $N_2/g_2<N_1/g_1$, so gain requires a population inversion produced by pumping through other levels. In a helium--neon laser, collisions with excited helium atoms pump the neon level whose decay emits at $632.8$ nm. The $\nu^3$ factor makes short-wavelength lasers harder to build, since spontaneous emission drains the inversion faster.

Magnetic resonance. A proton has spin $1/2$ and a magnetic moment. In a field $B$ its two spin states differ in energy by $\hbar\gamma B$, where $\gamma$ is the gyromagnetic ratio. The spin precesses at the Larmor frequency, and thermal equilibrium at temperature $T$ gives a small net polarization:

```math
\omega_L=\gamma B,\qquad \frac{\gamma}{2\pi}=42.58\ \mathrm{MHz\,T^{-1}},\qquad
\frac{N_\uparrow-N_\downarrow}{N}\approx\frac{\hbar\gamma B}{2k_BT}.
```

In a $1.5$ T scanner the resonance lies at $63.9$ MHz, and at body temperature the net polarization is about five protons per million. The signal is still measurable because water contains about $6.7\times10^{28}$ protons per cubic metre. A magnetic field gradient makes the frequency depend on position, which forms the image. Relaxation times of the precessing magnetization differ between tissues and provide contrast.

Atomic clocks use the same resonance principle with a hyperfine transition; the SI second is defined by the caesium-133 frequency $9\,192\,631\,770$ Hz. Transistors depend on the $1.12$ eV band gap of silicon and on the Fermi--Dirac occupation of electron states. Readers can continue with Quantum optics, Spin (physics), Two-state quantum system, Quantum metrology and Fermi--Dirac statistics.
