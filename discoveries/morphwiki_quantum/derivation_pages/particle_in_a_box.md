# Particle in a box

A cyanine dye carries electrons along a conjugated chain from one nitrogen atom to the other and absorbs visible light. Lengthening the chain moves the absorption to the red. A semiconductor nanocrystal shifts its emission from red to blue as it is made smaller. In both cases electrons move almost freely through a region of fixed size. The simplest model of such confinement is a particle of mass $m$ on an interval $0<x<L$ with no force inside:

```math
-\frac{\hbar^2}{2m}\psi''(x)=E\psi(x),\qquad
\psi(x)=A\sin kx+B\cos kx,\qquad E=\frac{\hbar^2k^2}{2m}.
```

The differential equation is the same for every box. Physically different boxes differ in the condition at the ends. The Hamiltonian must conserve probability, so the boundary term produced by integrating by parts has to vanish for every pair of allowed wave functions $\phi$ and $\psi$:

```math
\int_0^L\big[\phi^*(H\psi)-(H\phi)^*\psi\big]dx
=-\frac{\hbar^2}{2m}\Big[\phi^*\psi'-\phi'^*\psi\Big]_0^L=0.
```

Three common choices satisfy this requirement and describe different devices. Impenetrable walls give the Dirichlet condition $\psi(0)=\psi(L)=0$, the limit of a finite well whose depth tends to infinity. A ring of circumference $L$ gives the periodic condition $\psi(L)=\psi(0)$ and $\psi'(L)=\psi'(0)$. The Neumann condition $\psi'(0)=\psi'(L)=0$ allows a nonzero density at the walls but no current through them. The allowed wave numbers and energies follow directly:

```math
\text{Dirichlet: }E_n=\frac{\pi^2\hbar^2n^2}{2mL^2},\ n=1,2,\dots\qquad
\text{Neumann: same }E_n,\ n=0,1,2,\dots\\
\text{periodic: }E_n=\frac{2\pi^2\hbar^2n^2}{mL^2},\ n=0,\pm1,\pm2,\dots
```

The Dirichlet ground state has energy $\pi^2\hbar^2/(2mL^2)$, and its wave function $\sqrt{2/L}\,\sin(\pi x/L)$ vanishes at both walls. Confinement costs kinetic energy because the wave must curve to meet the walls. The Neumann box has a constant state at zero energy, with the density as large at the ends as in the middle. The periodic box also starts at zero energy, but each higher level is twofold degenerate: $\pm n$ describe the two senses of circulation around the ring. In every case, doubling $L$ lowers each level and each spacing by a factor of four.

In the free-electron model of a cyanine dye, $N$ delocalized electrons fill the Dirichlet levels in pairs up to $n=N/2$. Absorption promotes one electron to $n=N/2+1$, at an energy cost $\pi^2\hbar^2(N+1)/(2mL^2)$. With $h=2\pi\hbar$ and $c$ the speed of light, the absorbed wavelength is

```math
\lambda=\frac{8mcL^2}{h(N+1)}.
```

For $L=1.0$ nm and $N=6$ the formula gives 471 nm, in the blue part of the visible spectrum. Each added CH=CH unit lengthens the box by two bonds of 0.139 nm and adds two electrons. The predicted absorption then moves about 125 nm to the red, while symmetric cyanine dyes show shifts close to 100 nm per unit. The model fails for polyenes, whose alternating bond lengths open an additional gap, so that their absorption wavelength approaches a finite limit.

The periodic box accounts for the electron counts of stable ring molecules. The $n=0$ level holds two electrons and each degenerate pair $\pm n$ holds four. Shells therefore close at 2, 6, 10 electrons, that is, at $4j+2$ for integer $j\geq0$. Benzene, with six $\pi$ electrons, fills $n=0$ and $n=\pm1$ exactly. The free-electron ring thus reproduces the electron count of Hückel's rule for aromatic rings.

Semiconductor nanocrystals, or quantum dots, follow the same $1/L^2$ scaling in three dimensions, with electron and hole effective masses in place of $m$. The scaling holds when the crystal is smaller than the exciton Bohr radius of the bulk material, so that confinement energy dominates the electron--hole attraction. A finite barrier lets the wave function leak into the walls and lowers every level, as calculated under potential well. Under quantum tunnelling the same boundary term becomes a condition matching incoming and outgoing flux.

## References For The Physical Derivation

- [G. Bonneau, J. Faraut and G. Valent, Self-adjoint extensions of operators and the teaching of quantum mechanics; boundary conditions that make the box Hamiltonian self-adjoint and their spectra.](https://arxiv.org/abs/quant-ph/0103153)
