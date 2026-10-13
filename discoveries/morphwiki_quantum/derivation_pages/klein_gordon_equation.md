# Klein–Gordon equation

Nuclear forces fall to negligible strength within a few femtometres, whereas the Coulomb force has unlimited range. In 1935 Yukawa attributed the short range to the mass of an exchanged particle, later identified as the pion. The relation between mass and range follows from the Klein--Gordon equation, the relativistic wave equation for a particle without spin.

Replacing $E$ by $i\hbar\partial_t$ and $\mathbf p$ by $-i\hbar\nabla$ in $E^2=p^2c^2+m^2c^4$ gives an equation for a field $\phi(\mathbf x,t)$. Plane waves solve it for either sign of the energy:

```math
\left(\frac{1}{c^2}\frac{\partial^2}{\partial t^2}-\nabla^2+\frac{m^2c^2}{\hbar^2}\right)\phi=0,\\
\phi=e^{i(\mathbf p\cdot\mathbf x-Et)/\hbar},\qquad E=\pm\sqrt{p^2c^2+m^2c^4}.
```

The negative-energy solutions have no lower bound. A particle described by them could, once coupled to the electromagnetic field, radiate without limit. A second difficulty concerns probability. The equation implies a continuity equation $\partial_t\rho+\nabla\cdot\mathbf j=0$, with

```math
\rho=\frac{i\hbar}{2mc^2}\left(\phi^*\partial_t\phi-\phi\,\partial_t\phi^*\right),\qquad
\mathbf j=\frac{\hbar}{2mi}\left(\phi^*\nabla\phi-\phi\nabla\phi^*\right),\\
\rho=\frac{E}{mc^2}|\phi|^2\quad\text{for a plane wave}.
```

For negative-energy plane waves $\rho$ is negative. More generally, because the equation is second order in time, $\phi$ and $\partial_t\phi$ can be chosen independently at an initial instant, and $\rho$ can be made negative anywhere. It is therefore not a probability density. Pauli and Weisskopf resolved this in 1934 by treating $\phi$ as a quantized field. Multiplied by the charge, $\rho$ becomes a charge density whose sign distinguishes particles from antiparticles. Positive-frequency solutions describe $\pi^+$ mesons, and negative-frequency solutions describe $\pi^-$ mesons with positive energy.

For a static point source of strength $g$ the field obeys $(\nabla^2-\mu^2)\phi=-g\,\delta^3(\mathbf r)$, with $\mu=mc/\hbar$. The solution falls off exponentially, and a second nucleon coupled to the same field acquires a potential energy proportional to it:

```math
\phi(r)=\frac{g\,e^{-\mu r}}{4\pi r},\qquad
V(r)\propto-\frac{e^{-r/\lambda}}{r},\qquad \lambda=\frac{\hbar}{mc}.
```

The range is the reduced Compton wavelength of the exchanged particle. With the charged-pion mass $139.57\,\mathrm{MeV}/c^2$ and $\hbar c=197.33$ MeV fm, $\lambda=1.41$ fm. Nucleon-nucleon scattering in partial waves of high angular momentum, which probe large separations, follows the one-pion-exchange potential. Because the pion is pseudoscalar, that potential also contains spin and isospin factors and a tensor part, but its central part has this Yukawa form. Below about 1 fm, heavier mesons and the quark structure of nucleons take over.

The Klein--Gordon equation with a Coulomb potential also describes pionic atoms, in which a $\pi^-$ replaces an electron. Their X-ray transition energies are used to determine the charged-pion mass. As a single-particle equation it applies when potentials change slowly over $\lambda$ and energies remain well below the pair-creation threshold $2mc^2$. For particles of spin one half it is replaced by the Dirac equation, although each component of a free Dirac spinor still satisfies it. In Quantum field theory every free relativistic field obeys it, as the dispersion relation of each mode.

## References For The Physical Derivation

- [R. Machleidt and D. R. Entem, Chiral effective field theory and nuclear forces; one-pion exchange as the long-range part of the nucleon-nucleon interaction.](https://arxiv.org/abs/1105.2919)
- [M. Trassinelli and colleagues, Measurement of the charged pion mass using X-ray spectroscopy of exotic atoms; pionic-atom transitions and the charged-pion mass.](https://arxiv.org/abs/1605.03300)
