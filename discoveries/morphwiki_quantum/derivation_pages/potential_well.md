# Potential well

An electron in a thin layer of gallium arsenide between layers of aluminium gallium arsenide is trapped in one direction. The trap has a finite depth, set by the offset between the conduction bands of the two materials. The electron occupies a small number of discrete levels, and its wave function extends into the barriers. Both the energies and the number of levels follow from one matching condition.

Take a well of depth $V_0$ and width $2a$, with $V=-V_0$ for $|x|<a$ and $V=0$ outside. A bound state has $-V_0<E<0$. Inside the well it oscillates with wave number $k=\sqrt{2m(E+V_0)}/\hbar$; outside it decays as $e^{-\kappa|x|}$ with $\kappa=\sqrt{-2mE}/\hbar$. The potential is even, so each state is even or odd. Continuity of $\psi'/\psi$ at $x=a$ gives

```math
\text{even: }\kappa=k\tan ka,\qquad \text{odd: }\kappa=-k\cot ka,\qquad
k^2+\kappa^2=\frac{2mV_0}{\hbar^2}.
```

The last relation holds because $E$ cancels. In the dimensionless variables $\xi=ka$ and $\eta=\kappa a$, every solution lies on a circle in the positive quadrant. The bound states are the intersections of that circle with the curves $\eta=\xi\tan\xi$ and $\eta=-\xi\cot\xi$. Even and odd branches alternate, each starting from $\eta=0$ at a multiple of $\pi/2$:

```math
\xi^2+\eta^2=R^2,\qquad R=\frac{a\sqrt{2mV_0}}{\hbar},\qquad
N=1+\left\lfloor\frac{2R}{\pi}\right\rfloor.
```

A branch is intersected only if it starts inside the circle. The number $N$ of bound states therefore grows by one each time $R$ passes a multiple of $\pi/2$. The even branch starting at $\xi=0$ is always intersected, so a one-dimensional well of any depth binds at least one state. The count has a direct physical reading. $N-1$ is the integer part of $\sqrt{V_0/E_1}$, where $E_1=\pi^2\hbar^2/[2m(2a)^2]$ is the ground energy of an infinite box of the same width.

In a shallow well, $R\ll1$, the single bound state has $\eta\approx R^2$, so $E\approx-2ma^2V_0^2/\hbar^2$. This energy depends only on the product $2aV_0$, as for a delta-function well of the same strength, and the decay length $1/\kappa$ far exceeds the well width. In a deep well the roots approach $\xi=n\pi/2$, the Dirichlet levels of particle in a box. Penetration into the walls lowers every level below the corresponding box value.

Consider a 10 nm GaAs layer with effective mass $0.067\,m_e$ and a conduction-band offset of 0.24 eV, appropriate for an aluminium fraction near 0.3 in the barriers. Then $R=3.25$ and the well holds three bound states. The ground level lies 32 meV above the well bottom, compared with 56 meV for an infinite box of the same width. Its wave function decays into the barrier over 1.7 nm. The third level lies only about 2 meV below the barrier top, so its existence depends on the precise offset. The calculation assumes the same effective mass in both materials. Otherwise current conservation requires $\psi'/m^*$ rather than $\psi'$ to be continuous, which shifts the levels slightly. Transitions between such levels are used in quantum-well infrared detectors and quantum cascade lasers.

Dimension changes the binding threshold. In a spherical well of radius $a$ with zero angular momentum, the radial function $u=r\psi$ must vanish at the origin. Only the odd one-dimensional solutions survive, so a bound state requires $R>\pi/2$. The deuteron, bound by 2.2 MeV in a well tens of MeV deep, is a weakly bound state of this kind. At positive energy the same matching condition gives the phase shifts and resonances treated under scattering and S-matrix.

## References For The Physical Derivation

- [K. Razi Naqvi and S. Waldenstrøm, The finite square well: whatever is worth teaching at all is worth teaching well; tutorial review of the matching conditions, bound-state count and quantum-well applications.](https://arxiv.org/abs/1505.03376)
