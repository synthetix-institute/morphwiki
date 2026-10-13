# Boson

Two photons that reach the two input faces of a balanced beam splitter at the same time leave together through one output face, never one through each. This holds provided they are identical in frequency, polarization and arrival time. Hong, Ou and Mandel observed it in 1987 as a dip to near zero in the coincidence rate of two detectors placed behind the outputs. The effect follows from the exchange symmetry of bosons.

The many-particle amplitude of identical bosons is unchanged when two particles are exchanged. In the occupation description of Fock space, creation operators of different modes commute, and one mode can hold any number $n=0,1,2,\dots$ of quanta. Let $a^\dagger$ and $b^\dagger$ create a photon in the two input modes, and $c^\dagger$ and $d^\dagger$ in the two output modes. A lossless 50:50 beam splitter acts linearly on the modes; with one choice of phases,

```math
a^\dagger\mapsto\frac{c^\dagger+d^\dagger}{\sqrt2},\qquad
b^\dagger\mapsto\frac{c^\dagger-d^\dagger}{\sqrt2},\\
a^\dagger b^\dagger\ket{0}\mapsto\frac12\left[(c^\dagger)^2-(d^\dagger)^2\right]\ket{0}
=\frac{\ket{2,0}-\ket{0,2}}{\sqrt2}.
```

The cross terms $-c^\dagger d^\dagger+d^\dagger c^\dagger$ cancel because the operators commute. In terms of paths, both photons transmitted and both photons reflected lead to the same final state with amplitudes of equal magnitude and opposite sign. For fermions, anticommutation makes the same cross terms add while $(c^\dagger)^2=0$, so two identical fermions always leave through different faces. For distinguishable particles the probabilities add, and a coincidence occurs with probability one half.

Real photons are wave packets, and only the overlapping parts of their states interfere. Let the second photon be delayed by $\tau$, and let both have the normalized spectral intensity $|\phi(\omega)|^2$. For a Gaussian spectrum with root-mean-square angular-frequency width $\sigma$, the coincidence probability is

```math
P_c(\tau)=\frac12\left[1-\left|\int|\phi(\omega)|^2e^{i\omega\tau}d\omega\right|^2\right]
=\frac12\left(1-e^{-\sigma^2\tau^2}\right).
```

The width of the dip is set by the inverse bandwidth, not by the wavelength. For photons at 800 nm with a Gaussian spectrum of 5 nm full width at half maximum, $\sigma=6.2\times10^{12}\,\mathrm{s^{-1}}$. The dip then has a full width of 270 fs at half depth, corresponding to about 80 micrometres of path. Translating one input mirror over this range traces the dip. Its depth, the visibility $V=1-P_c(0)/P_c(\infty)$, equals the squared overlap of the two single-photon states.

Visibility measurements therefore test whether photons from separate emitters are identical, a requirement for photonic quantum logic. The calculation assumes exactly one photon in each input. Two independent laser pulses with Poisson photon numbers give at most 50 percent visibility, so a deeper dip excludes a description by classical fields. Loss and finite detector efficiency reduce the coincidence rate by the same factor at every delay and leave the visibility unchanged.

Elementary bosons include the photon, the gluons, the W and Z bosons and the Higgs boson, all with integer spin. Composite particles with an even number of fermion constituents, such as helium-4 atoms, behave as bosons when an experiment cannot resolve their structure. The same commutation rule produces stimulated emission and the condensation described under Bose--Einstein statistics.

## References For The Physical Derivation

- [F. Bouchard and colleagues, Two-photon interference: the Hong-Ou-Mandel effect; beam-splitter transformation of two photons, dip width and visibility.](https://arxiv.org/abs/2006.09335)
