# Quantum biology

Migratory birds orient in the geomagnetic field, whose strength of about 50 microtesla changes the energy of an electron spin by roughly $2\times10^{-7}$ of the thermal energy at body temperature. A thermal population effect of that size is negligible. A chemical reaction controlled by the spin dynamics of a short-lived radical pair can still respond to such a field. This radical-pair mechanism is the most developed proposal for a magnetic sense, and its central calculation is a singlet yield.

Light absorption moves an electron between two molecules and creates two radicals, each with one unpaired electron. The pair starts in the singlet state, with total electron spin zero. In the simplest kinetic model the pair reacts at rate $k$ whatever its spin state, singlet pairs to one product and triplet pairs to another. Between creation and reaction the electron spins evolve under the Zeeman interaction and hyperfine couplings to nuclear spins. With one spin-one-half nucleus $\mathbf I$ on radical 1, isotropic coupling $a$ and equal g-factors,

```math
\frac{H}{\hbar}=\omega(S_{1z}+S_{2z})+a\,\mathbf S_1\cdot\mathbf I,\qquad \omega=\frac{g\mu_BB}{\hbar},
\qquad \Phi_S=k\int_0^\infty e^{-kt}P_S(t)\,dt.
```

Here $P_S(t)$ is the singlet probability and $\Phi_S$ the singlet yield; the nuclear spin starts unpolarized. In zero field, the hyperfine term splits electron 1 and the nucleus into total spin one and zero, separated by $a$, and the singlet probability oscillates at that frequency. In a strong field, $\omega\gg a$, the triplet states with $m=\pm1$ are shifted away. Only the triplet with $m=0$ then mixes with the singlet, at frequency $a/2$. Integrating against the survival factor gives the two yields:

```math
P_S^{(0)}(t)=\tfrac58+\tfrac38\cos at,\qquad P_S^{(\infty)}(t)=\tfrac12+\tfrac12\cos\tfrac{at}{2},\\
\Phi_S^{(0)}=\tfrac58+\tfrac38\,\frac{k^2}{k^2+a^2},\qquad
\Phi_S^{(\infty)}=\tfrac12+\tfrac12\,\frac{k^2}{k^2+a^2/4}.
```

For fast reaction, $k\gg a$, both yields approach one and the field has no effect, because the spins have no time to evolve. For slow reaction the yield falls from 5/8 to 1/2. This 20 percent change is produced by a field whose energy is negligible compared with $k_BT$. A field weaker than $a$ acts through the Zeeman splitting of nearly degenerate levels. In this model fields of $0.05a$ to $0.2a$ lower the slow-reaction yield to about 0.4. That response requires the pair to live, and its spins to stay coherent, longer than the inverse Larmor frequency, 0.11 microseconds at 50 microtesla.

Sensing the direction of the field requires anisotropic hyperfine couplings, so that the yield depends on the angle between the field and the molecule. Cryptochrome proteins in the retina form flavin-tryptophan radical pairs and are the leading candidates. Magnetic field effects on radical-pair reactions are established in spin chemistry. Effects on isolated cryptochromes have been measured in fields of a few millitesla. Whether the avian compass works in this way at 50 microtesla in vivo, and how spin coherence survives for a microsecond in a protein, remain open.

Other parts of quantum biology show the same division between an established microscopic step and an open biological role. Proton and hydride transfer in some enzymes shows kinetic isotope effects far larger than transfer over the barrier allows, which quantum tunnelling explains. Long-lived oscillations in two-dimensional spectra of light-harvesting complexes were initially attributed to electronic coherence. They are now largely assigned to vibrational or vibronic motion, and their functional role is not established. In each case quantum decoherence sets how long a coherent step can last, and the biological question is whether it changes a rate or yield that matters to the organism.

## References For The Physical Derivation

- [N. Lambert and colleagues, Functional Quantum Biology in Photosynthesis and Magnetoreception; radical-pair compass model and coherence in light harvesting.](https://arxiv.org/abs/1205.0883)
- [S. F. Huelga and M. B. Plenio, Vibrations, Quanta and Biology; vibrational and vibronic contributions to energy transfer in light-harvesting complexes.](https://arxiv.org/abs/1307.3530)
- [E. Gauger and colleagues, Sustained Quantum Coherence and Entanglement in the Avian Compass; spin coherence times required by a radical-pair compass.](https://arxiv.org/abs/0906.3725)
