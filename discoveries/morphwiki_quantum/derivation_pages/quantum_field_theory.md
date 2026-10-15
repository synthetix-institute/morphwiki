# Quantum field theory

A mirror moving at a speed close to that of light emits photons even when no light was present before. In 2011 Wilson and coworkers observed this dynamical Casimir effect in a superconducting circuit, where microwave photons appeared in correlated pairs. Two features of quantum field theory explain it: particle number is not conserved, and the vacuum depends on the Hamiltonian.

Consider a real scalar field $\phi(\mathbf x,t)$ in a box of volume $V$, in units with $\hbar=c=1$. Its conjugate momentum is $\pi=\dot\phi$, and its energy contains kinetic, gradient and mass terms. Expanding in plane waves decouples the field into one oscillator for each wave vector $\mathbf k$:

```math
H=\int d^3x\left[\frac{\pi^2}{2}+\frac{(\nabla\phi)^2}{2}+\frac{m^2\phi^2}{2}\right]
=\sum_{\mathbf k}\omega_{\mathbf k}\left(a_{\mathbf k}^\dagger a_{\mathbf k}+\frac12\right),\\
\phi(\mathbf x)=\sum_{\mathbf k}\frac{a_{\mathbf k}e^{i\mathbf k\cdot\mathbf x}
+a_{\mathbf k}^\dagger e^{-i\mathbf k\cdot\mathbf x}}{\sqrt{2\omega_{\mathbf k}V}},\qquad
\omega_{\mathbf k}=\sqrt{\mathbf k^2+m^2}.
```

The operators obey $[a_{\mathbf k},a_{\mathbf k'}^\dagger]=\delta_{\mathbf k\mathbf k'}$. Each mode is a Quantum harmonic oscillator, and its occupation number counts particles of momentum $\mathbf k$ and energy $\omega_{\mathbf k}$. States with any number of particles form a Fock space. The vacuum is the state annihilated by every $a_{\mathbf k}$, so it is defined with respect to these particular oscillators. Correlation functions such as $\langle0|T\{\phi(x)\phi(y)\}|0\rangle$ describe the propagation of a quantum between two spacetime points and are the elements of perturbative scattering amplitudes.

A single mode shows what happens when the Hamiltonian changes. Let a mode of unit mass have angular frequency $\omega_0$ for $t<0$ and be prepared in its ground state, which $a$ annihilates. At $t=0$ the frequency jumps to $\omega_1$. An instantaneous change leaves the state unchanged, but the new Hamiltonian is diagonalized by different operators. Expressing the coordinate and momentum through $a$ and $a^\dagger$ gives the Bogoliubov transformation and the mean number of new quanta:

```math
b=u\,a+v\,a^\dagger,\qquad
u=\frac{\omega_0+\omega_1}{2\sqrt{\omega_0\omega_1}},\qquad
v=\frac{\omega_1-\omega_0}{2\sqrt{\omega_0\omega_1}},\\
\langle n_1\rangle=\langle0|b^\dagger b|0\rangle=v^2=\frac{(\omega_0-\omega_1)^2}{4\omega_0\omega_1}.
```

The relation $u^2-v^2=1$ preserves $[b,b^\dagger]=1$. The old ground state is not the new one: it contains new quanta, always in even numbers, because the transformation mixes $a$ with $a^\dagger$. Halving the frequency gives $\langle n_1\rangle=1/8$, with probability 0.943 of finding no quanta and 0.052 of finding two. The final mean energy is $E_f=\omega_1(\langle n_1\rangle+\frac12)$ in the units $\hbar=1$ used here. Its excess above the final ground-state energy is $E_{\rm exc}=E_f-\omega_1/2$, whereas the mean work done on the mode is $\langle W\rangle=E_f-\omega_0/2$. For $\omega_0=1$ and $\omega_1=1/2$, these are $E_{\rm exc}=1/16$ and $\langle W\rangle=-3/16$: the mode is excited relative to its new ground state while releasing energy to the agent that lowers its frequency. If the frequency changes slowly, with $|\dot\omega|\ll\omega^2$, the mode follows its instantaneous ground state and no quanta appear; the work is then the ground-state energy change $(\omega_1-\omega_0)/2$.

In a field, a change that is uniform in space, such as a sudden change of the mass $m$, conserves momentum. It therefore mixes each $a_{\mathbf k}$ only with $a_{-\mathbf k}^\dagger$:

```math
b_{\mathbf k}=u_{\mathbf k}a_{\mathbf k}+v_{\mathbf k}a_{-\mathbf k}^\dagger,\qquad
\langle n_{\mathbf k}\rangle=|v_{\mathbf k}|^2,\qquad
u_{\mathbf k}^2-|v_{\mathbf k}|^2=1.
```

Quanta are created in pairs of opposite momentum, so the total momentum stays zero while the total number changes. A periodic modulation at angular frequency $\Omega$ acts as a parametric drive and creates pairs whose frequencies add up to $\Omega$. In cosmology the same transformation describes the creation of field quanta by the expansion of space.

In the Wilson experiment a coplanar microwave waveguide is terminated by a SQUID, whose inductance depends on the magnetic flux through it. Modulating the flux near 11 GHz moves the effective end of the line back and forth at a few percent of the speed of light in the line. A material mirror cannot approach such speeds, and for small amplitudes the number of created quanta grows as the square of the speed ratio. The circuit was cooled so that thermal photons were negligible. The emitted radiation was symmetric about half the drive frequency, and its two-mode squeezing showed that photons at $\omega$ and $\Omega-\omega$ were produced together, as pair creation requires.

The static attraction between conducting plates, which arises from the zero-point energy of the same modes, is treated under Quantum fluctuation. These calculations assume free fields. With interactions the vacuum itself becomes a correlated state, and Renormalization relates the parameters of the theory to measured masses and charges.

## References For The Physical Derivation

- [C. M. Wilson and colleagues, Observation of the Dynamical Casimir Effect in a Superconducting Circuit; photon pairs and two-mode squeezing from a SQUID-modulated transmission line.](https://arxiv.org/abs/1105.4714)
- [P. D. Nation, J. R. Johansson, M. P. Blencowe and F. Nori, Stimulating uncertainty: Amplifying the quantum vacuum with superconducting circuits; Bogoliubov transformations and the dynamical Casimir effect.](https://arxiv.org/abs/1103.0835)
