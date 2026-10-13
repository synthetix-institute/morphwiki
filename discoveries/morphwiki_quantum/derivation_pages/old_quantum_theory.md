# Old quantum theory

Hydrogen emits light at sharp wavelengths, among them the red Balmer line at 656 nanometres. Between 1913 and 1925 these lines were explained by selecting particular classical orbits, before wave mechanics existed. The selection rule of that period, Bohr--Sommerfeld quantization, worked for hydrogen and for the oscillator, and its failures show what the later theory had to change.

The rule applies to motion that separates into periodic coordinates $q_k$ with conjugate momenta $p_k$. The action integral over one period of each coordinate must be an integer multiple of Planck's constant $h$:

```math
J_k=\oint p_k\,dq_k=n_k h,\qquad n_k=0,1,2,\ldots
```

For an oscillator of mass $m$ and angular frequency $\omega$, the orbit at energy $E$ is an ellipse in phase space with area $2\pi E/\omega$. The rule gives $E_n=n\hbar\omega$, with the spacing $\hbar\omega$ seen in molecular vibrational ladders. The ground energy is wrong, however. Wave mechanics gives $(n+\tfrac12)\hbar\omega$, and isotope shifts in molecular band spectra, analysed by Mulliken in 1924 and 1925, already required the half quantum. The modern semiclassical rule replaces $n$ by $n+\tfrac12$ for motion between two smooth turning points. That correction comes from the phase of the wave at the turning points, which an orbit cannot supply.

For hydrogen, write $k=e^2/(4\pi\varepsilon_0)$ for the Coulomb strength and use circular orbits. Quantized angular momentum $mvr=n\hbar$ together with the force balance $mv^2/r=k/r^2$ gives

```math
r_n=\frac{n^2\hbar^2}{mk}=n^2a_0,\qquad
E_n=-\frac{mk^2}{2\hbar^2n^2}=-\frac{13.6\ \text{eV}}{n^2}.
```

Here $a_0=52.9$ picometres is the Bohr radius. The transition from $n=3$ to $n=2$, with the reduced-mass correction, gives a vacuum wavelength of 656.5 nanometres. Sommerfeld's elliptic orbits add a radial action. The sum of the radial and angular actions depends only on the energy, so the levels depend only on $n=n_r+n_\varphi$. This reproduces the degeneracy of the Kepler problem:

```math
J_r+J_\varphi=2\pi k\sqrt{\frac{m}{-2E}}=(n_r+n_\varphi)h.
```

For large $n$ the spacing of neighbouring levels, divided by $h$, approaches the classical orbital frequency $mk^2/(2\pi\hbar^3n^3)$. Bohr used this correspondence in 1913 to fix the constant in his rule, requiring large orbits to radiate at their classical frequency. Sommerfeld's relativistic treatment of the elliptic orbits gave a fine-structure formula that agrees with the later Dirac result. Semiclassical analysis of the Dirac equation, including the precession of the spin, helps explain that agreement.

The failures are specific. The rule requires $n_\varphi\geq1$, because an orbit with zero angular momentum would pass through the nucleus. The predicted ground state therefore carries angular momentum $\hbar$, whereas the hydrogen ground state has none; wave mechanics gives $L^2=\ell(\ell+1)\hbar^2$ with $\ell=0,\ldots,n-1$. Einstein pointed out in 1917 that the rule can be stated without special coordinates, as conditions on loops around invariant tori in phase space. Motion without such tori cannot be quantized this way. The three-body motion of helium has no such structure, and orbit models failed to reproduce its ionization energy of 24.6 eV. The anomalous Zeeman effect demanded half-integer quantum numbers, later traced to electron spin. Line intensities lay outside the rule, and their calculation led Heisenberg to matrix mechanics in 1925.

The corrected rule survives as the leading term of semiclassical WKB theory. It remains accurate for highly excited Rydberg states and for the vibrational levels of molecules. The quantum harmonic oscillator and the angular momentum operator give the exact results that replaced the orbit picture.

## References For The Physical Derivation

- [S. Keppeler, Semiclassical quantisation rules for the Dirac and Pauli equations; Maslov corrections and the relativistic Kepler problem behind Sommerfeld's fine-structure formula.](https://arxiv.org/abs/quant-ph/0212082)
- [A. Afriat, Einstein and the old quantum theory; Einstein's coordinate-independent quantum conditions on invariant tori.](https://arxiv.org/abs/2112.14194)
