# Quantum fluctuation

Two uncharged, parallel metal plates a micrometre apart in vacuum attract each other with a pressure of about one millipascal. Casimir predicted this force in 1948. It has been measured since 1997 between a sphere and a plate and between parallel plates. The force follows from the zero-point fluctuations of the electromagnetic field between the plates.

Each mode of the field is a harmonic oscillator of angular frequency $\omega$. As for the quantum harmonic oscillator, its ground state has energy $\hbar\omega/2$ and nonzero variances of both field quadratures: the mean field vanishes, but its square does not. Conducting plates change the allowed modes and therefore the sum of zero-point energies. The logic is clearest for a scalar field in one dimension between mirrors a distance $d$ apart, where the mode frequencies are $\omega_n=n\pi c/d$:

```math
E_0(d)=\sum_{n=1}^\infty\frac{\hbar\omega_n}{2}=\frac{\pi\hbar c}{2d}\sum_{n=1}^\infty n.
```

The sum diverges, but real mirrors become transparent at high frequency. A factor $e^{-\epsilon\omega_n}$, with $\epsilon$ of order the inverse plasma frequency of the metal, represents that transparency. The sum is then elementary, $\sum_nne^{-\lambda n}=\lambda^{-2}-1/12+O(\lambda^2)$ with $\lambda=\epsilon\pi c/d$, and gives

```math
E_0(d)=\frac{\hbar d}{2\pi c\,\epsilon^2}-\frac{\pi\hbar c}{24d}+O(\epsilon^2).
```

The first term is proportional to $d$, with the same energy per length as in free space. In a long cavity divided by a movable mirror, the linear terms from the two sides add to a constant and exert no net force. The remaining term does not depend on the cutoff and gives an attraction of magnitude $\pi\hbar c/24d^2$. For the electromagnetic field between perfectly conducting plates of area $A$, the same steps with two polarizations and all transverse wavevectors give

```math
\frac{E}{A}=-\frac{\pi^2\hbar c}{720\,d^3},\qquad \frac{F}{A}=-\frac{\pi^2\hbar c}{240\,d^4}.
```

At $d=1$ micrometre the pressure is 1.3 mPa, and halving the separation multiplies it by 16. This steep rise makes the force relevant to the sticking of nearby parts in micromachined devices. The ideal-conductor formula requires the separation to exceed the plasma wavelength of the metal, about 0.14 micrometre for gold. At smaller separations finite conductivity weakens the force, and Lifshitz theory with measured dielectric functions replaces the formula. At room temperature thermal photons add a correction once $d$ approaches $\hbar c/k_BT\approx7.6$ micrometres.

The calculation does not show that empty space has a measurable absolute energy density. The force depends on how the plates respond to the field, and it vanishes as their coupling to the field goes to zero. It can be derived equally as the retarded van der Waals attraction between fluctuating charges in the two plates, without reference to vacuum energy. What is established is how the zero-point energy changes with the boundary conditions. The coupling of bound electrons to the same field fluctuations contributes to the Lamb shift treated by quantum electrodynamics. The absolute vacuum energy and its relation to the cosmological constant remain open.

## References For The Physical Derivation

- [M. Bordag, U. Mohideen and V. M. Mostepanenko, New Developments in the Casimir Effect; derivation, finite-conductivity and thermal corrections, measurements.](https://arxiv.org/abs/quant-ph/0106045)
- [R. L. Jaffe, The Casimir Effect and the Quantum Vacuum; the force as a van der Waals interaction independent of absolute vacuum energy.](https://arxiv.org/abs/hep-th/0503158)
