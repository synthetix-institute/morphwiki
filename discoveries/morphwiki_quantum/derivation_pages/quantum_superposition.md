# Quantum superposition

The Super-Kamiokande detector in Japan counts muon neutrinos produced by cosmic rays in the atmosphere. In 1998 the collaboration reported a deficit of muon neutrinos of a few GeV arriving from below, after crossing up to 13000 km of the Earth. They were about half as numerous as those arriving from above, which travel some 15 km. Electron neutrinos showed no such deficit. The missing muon neutrinos had changed flavour in flight. That change requires each neutrino to travel as a superposition of states with different masses.

The Schrödinger equation is linear. If $\ket a$ and $\ket b$ are possible states, so is every normalized combination of them, and each component evolves with its own phase. For an equal superposition with relative phase $\varphi$, a measurement that projects onto $\ket\pm=(\ket a\pm\ket b)/\sqrt2$ gives

```math
\ket\psi=\frac{1}{\sqrt2}\left(\ket a+e^{i\varphi}\ket b\right),\qquad
P_\pm=|\langle\pm|\psi\rangle|^2=\frac12\left(1\pm\cos\varphi\right).
```

In a two-path interferometer $\ket a$ and $\ket b$ are the paths and the two outputs realize $\ket\pm$. A mixture with equal probability of either state gives a different prediction:

```math
\rho_{\rm mix}=\frac12\left(\ket a\bra a+\ket b\bra b\right),\qquad
P_\pm=\operatorname{Tr}\left(\rho_{\rm mix}\ket\pm\bra\pm\right)=\frac12.
```

Both descriptions assign probability one half to each of $\ket a$ and $\ket b$, so a measurement in that basis cannot tell them apart. Only the superposition responds to $\varphi$. The term $\cos\varphi$ comes from the off-diagonal elements of the density matrix and is the measurable signature of the superposition. Whether a state counts as a superposition depends on the basis: $\ket+$ is a superposition of $\ket a$ and $\ket b$ but an eigenstate of the output measurement.

A neutrino is created by the weak interaction in a flavour state, here $\nu_\mu$ together with a muon. In a two-flavour model the flavour states are rotations of the mass eigenstates $\nu_2$ and $\nu_3$ by a mixing angle $\theta$:

```math
\ket{\nu_\mu}=\cos\theta\ket{\nu_2}+\sin\theta\ket{\nu_3},\qquad
\ket{\nu_\tau}=-\sin\theta\ket{\nu_2}+\cos\theta\ket{\nu_3}.
```

In natural units a mass state of momentum $p\gg m_i$ has energy $E_i\approx p+m_i^2/2E$. After a distance $L\approx t$ the two components have therefore acquired the relative phase $\Delta m^2L/2E$, with $\Delta m^2=m_3^2-m_2^2$. Projecting the evolved state onto $\ket{\nu_\tau}$ gives

```math
P(\nu_\mu\to\nu_\tau)=\sin^22\theta\,\sin^2\frac{\Delta m^2L}{4E}
=\sin^22\theta\,\sin^2\!\left(1.27\,\frac{\Delta m^2[\mathrm{eV}^2]\,L[\mathrm{km}]}{E[\mathrm{GeV}]}\right).
```

The conversion probability returns to zero after the oscillation length $4\pi E/\Delta m^2$. For $\Delta m^2=2.5\times10^{-3}\ \mathrm{eV}^2$ and $E=1$ GeV this is about 990 km, with the first maximum near 500 km. Downward neutrinos, after 15 km, have converted with probability below one percent. Upward neutrinos have passed through several oscillation lengths. Averaged over their spread of energies and path lengths, the second factor gives one half. With nearly maximal mixing, $\sin^22\theta\approx1$, about half of them arrive as $\nu_\tau$, which the detector did not record as muon neutrinos.

Suppose instead that the source emitted an incoherent mixture, $\nu_2$ with probability $\cos^2\theta$ and $\nu_3$ with probability $\sin^2\theta$. Each mass state is stationary and keeps its flavour content, so the conversion probability is $\cos^2\theta\sin^2\theta+\sin^2\theta\cos^2\theta=\tfrac12\sin^22\theta$ at every distance. That value equals the average of the oscillating formula but does not depend on $L$. It would remove half of the downward muon neutrinos as well, which the data exclude. Only the coherent superposition starts as a pure $\nu_\mu$ and develops the conversion with distance.

The coherent description requires the wave packets of the two mass components to overlap at the detector. Over very long distances their different group velocities separate them, and the oscillating term averages away, as described under quantum decoherence. The two-flavour formula neglects the third neutrino; matter in the Earth changes electron-neutrino oscillations but hardly affects the conversion of $\nu_\mu$ into $\nu_\tau$. Superpositions of states with different electric charge are never observed, an example of a superselection rule. Superpositions of macroscopically distinct states are the subject of Schrödinger's cat.

## References For The Physical Derivation

- [Super-Kamiokande Collaboration (Y. Fukuda and colleagues), Evidence for Oscillation of Atmospheric Neutrinos; up-down asymmetry of muon neutrinos.](https://arxiv.org/abs/hep-ex/9807003)
- [M. C. Gonzalez-Garcia and Y. Nir, Neutrino Masses and Mixing: Evidence and Implications; two-flavour oscillation formula and atmospheric parameters.](https://arxiv.org/abs/hep-ph/0202058)
- [E. Kh. Akhmedov, Neutrino Physics; coherence of mass eigenstates, oscillation length and wave-packet separation.](https://arxiv.org/abs/hep-ph/0001264)
