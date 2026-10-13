# Wave function

Electrons accelerated through 54 volts and directed onto a nickel crystal leave its surface preferentially at about $50^\circ$ from the incident beam. Davisson and Germer observed this peak in 1927. Point particles scattered by the surface atoms give no reason for such a sharp preferred angle, whereas a wave of definite wavelength does. The wave function supplies that wave and also the probability of detecting each electron at a given place.

For one spinless particle, the state $\ket\psi$ is represented in the position basis by the complex function $\psi(\mathbf x)=\langle\mathbf x|\psi\rangle$. The Born rule gives the probability that a detector covering the region $\Delta$ responds:

```math
\Pr(\mathbf x\in\Delta)=\int_\Delta|\psi(\mathbf x)|^2d^3x,\qquad
\int|\psi|^2d^3x=1,\qquad \psi\sim e^{i\alpha}\psi.
```

A constant overall phase $e^{i\alpha}$ changes no probability, so $\psi$ and $e^{i\alpha}\psi$ describe the same state. Phase differences between regions are physical. The Schrödinger equation $i\hbar\partial_t\psi=-(\hbar^2/2m)\nabla^2\psi+V\psi$ conserves probability locally, and the current through a surface depends on the phase gradient. Writing $\psi=R\,e^{iS/\hbar}$ with real $R$ and $S$ gives

```math
\partial_t|\psi|^2+\nabla\cdot\mathbf j=0,\qquad
\mathbf j=\frac{\hbar}{m}\operatorname{Im}(\psi^*\nabla\psi)=\frac{R^2\,\nabla S}{m}.
```

The phase gradient divided by the mass acts as a local velocity. A plane wave $e^{i\mathbf k\cdot\mathbf x}$ carries a uniform current, is an eigenfunction of the momentum operator $-i\hbar\nabla$ with eigenvalue $\hbar\mathbf k$, and has wavelength $\lambda=2\pi/k=h/p$. For an electron of kinetic energy $E$ this gives

```math
\lambda=\frac{h}{\sqrt{2m_eE}}=0.167\ \mathrm{nm}\ \ (E=54\ \mathrm{eV}),\qquad
D\sin\theta=\lambda.
```

Waves scattered from parallel rows of surface atoms with spacing $D$ add in phase when their path difference $D\sin\theta$ equals one wavelength. With $D=0.215$ nm for nickel, the first-order angle is $50.9^\circ$, close to the observed peak. The electron speed is about 1.5 percent of the speed of light, so the nonrelativistic relation suffices. The angle arises from the relative phases of the waves from different atoms; adding the probabilities $|\psi|^2$ contributed by each atom would give no peak.

For several particles the wave function lives on configuration space. Two particles require $\psi(\mathbf x_1,\mathbf x_2)$, a function of six coordinates, not two waves in ordinary space. Because $\psi$ need not factor into a function of $\mathbf x_1$ times one of $\mathbf x_2$, quantum entanglement is possible. Spin adds discrete components, so a particle of spin $s$ has a wave function with $2s+1$ components. For identical particles $\psi$ must be symmetric or antisymmetric under exchange of their coordinates. The wave function is not recorded by a single detector. Its modulus follows from position statistics of identically prepared particles, and its phase from interference or from momentum statistics. The Fourier transform gives the equivalent momentum-space wave function, and a statistical preparation requires a density matrix.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; wave functions as elements of L2, rays and the position measure.](https://arxiv.org/abs/1508.06951)
