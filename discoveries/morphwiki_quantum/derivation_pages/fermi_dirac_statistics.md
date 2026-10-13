# Fermi–Dirac statistics

The conduction electrons of copper, about one per atom, contribute only about one percent of the heat capacity that a classical gas of free particles would have at room temperature. The classical Drude model could not explain this. The explanation lies in the occupation rule derived in Quantum statistical mechanics. A fermionic state holds zero or one particle, and at temperature $T$ and chemical potential $\mu$ its mean occupation is $f(\epsilon)=[e^{(\epsilon-\mu)/k_BT}+1]^{-1}$.

At $T=0$ the function $f$ is a step. Every state below $E_F=\mu(0)$ is filled and every state above it is empty. For free electrons of mass $m$ with two spin states per wave vector, the filled states form a sphere of radius $k_F$ in wave-vector space. Counting one wave vector per volume $(2\pi)^3/V$ gives the density $n$, the Fermi energy and the density of states at the Fermi energy:

```math
n=\frac{k_F^3}{3\pi^2},\qquad
E_F=\frac{\hbar^2k_F^2}{2m}=\frac{\hbar^2}{2m}(3\pi^2n)^{2/3},\qquad
g(E_F)=\frac{3N}{2E_F}.
```

Copper has $n=8.47\times10^{28}\,\mathrm{m^{-3}}$. This gives $k_F=1.36\times10^{10}\,\mathrm{m^{-1}}$, $E_F=7.0$ eV and a Fermi temperature $T_F=E_F/k_B=8.2\times10^4$ K. Electrons at the Fermi surface move at $1.6\times10^6\,\mathrm{m/s}$ even at absolute zero. The filled sphere exerts a degeneracy pressure $\frac25nE_F\approx38$ GPa without any repulsion between the electrons. Room temperature is a low temperature for this gas: $T/T_F\approx0.004$.

Heating can change occupations only within about $k_BT$ of $E_F$, because deeper electrons have no empty states nearby to move into. Roughly $g(E_F)k_BT$ electrons each gain an energy of order $k_BT$, so the energy rises as $T^2$ and the heat capacity is linear in $T$. The Sommerfeld expansion fixes the coefficient. For a function $H(\epsilon)$ that is smooth near $\mu$,

```math
\int_0^\infty H(\epsilon)f(\epsilon)\,d\epsilon=\int_0^\mu H(\epsilon)\,d\epsilon
+\frac{\pi^2}{6}(k_BT)^2H'(\mu)+O(T^4),\\
C_{\rm el}=\frac{\pi^2}{3}g(E_F)k_B^2T=\frac{\pi^2}{2}Nk_B\frac{T}{T_F}.
```

Applying the expansion to the particle number gives the small downward shift of $\mu$ with temperature; applying it to the energy gives $C_{\rm el}$. Per mole of copper, $C_{\rm el}=\gamma T$ with $\gamma=0.50\,\mathrm{mJ\,mol^{-1}K^{-2}}$. At 300 K this is $0.018R$, where $R$ is the gas constant, compared with the classical value $3R/2$ for free particles and the lattice value $3R$.

Below a few kelvin the lattice contribution falls as $T^3$, and the electronic term dominates. A plot of $C/T$ against $T^2$ is then a straight line whose intercept is $\gamma$. For copper the measured intercept is $0.695\,\mathrm{mJ\,mol^{-1}K^{-2}}$, larger than the free-electron value by a factor of 1.38. The excess measures the density of states at the Fermi energy of the real band structure, enhanced by coupling to lattice vibrations. It is usually reported as a thermal effective mass.

The derivation assumes $k_BT\ll E_F$ and a density of states that is smooth on the scale $k_BT$. Electron-electron interactions change the coefficients but, in a Fermi liquid, keep the linear law. When $T\gg T_F$ all occupations are small and $f$ approaches the Maxwell--Boltzmann weight. The zero-or-one restriction comes from the antisymmetry discussed under Fermion. With a minus sign in the denominator instead, Bose--Einstein statistics allows macroscopic occupation of a single state.

## References For The Physical Derivation

- [S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold Fermi gases; ideal Fermi gas, Fermi energy and low-temperature thermodynamics.](https://arxiv.org/abs/0706.3360)
