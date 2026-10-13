# Schrödinger equation

Atomic hydrogen absorbs ultraviolet light only at sharp wavelengths, and its Lyman series ends at 91.2 nm, the ionization threshold of 13.6 eV. A wave equation for the electron's amplitude must reproduce these numbers. Its form follows from the de Broglie relations and the nonrelativistic energy.

A plane wave $e^{i(\mathbf k\cdot\mathbf x-\omega t)}$ with $\mathbf p=\hbar\mathbf k$ and $E=\hbar\omega$ satisfies $i\hbar\partial_t\psi=E\psi$ and $-i\hbar\nabla\psi=\mathbf p\psi$. Requiring $E=p^2/2m+V$ for every component, and linearity so that superpositions of solutions remain solutions, gives

```math
i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\nabla^2\psi+V(\mathbf x)\,\psi,
\qquad i\hbar\frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle.
```

For a constant potential this argument is complete. For a varying $V$ the equation is postulated, and its predictions test it. It contains a single time derivative, so the wave function at one instant fixes it at all later times. For real $V$, multiplying by $\psi^*$ and subtracting the complex conjugate equation gives a local conservation law:

```math
\frac{\partial|\psi|^2}{\partial t}+\nabla\cdot\mathbf j=0,\qquad
\mathbf j=\frac{\hbar}{m}\,\mathrm{Im}\big(\psi^*\nabla\psi\big).
```

Probability flows from one region to another, but it is not created or destroyed. An imaginary part of $V$ would act as a source or sink, which is how absorption into unobserved channels is sometimes modelled. If $V$ does not depend on time, separable solutions $\psi=\phi(\mathbf x)e^{-iEt/\hbar}$ reduce the equation to the eigenvalue problem $H\phi=E\phi$. Normalizable solutions exist only for particular energies, which is the origin of discrete levels. A general preparation is a superposition of such stationary states, and its probability density changes in time only through interference between components of different energy.

For hydrogen, $V=-k/r$ with $k=e^2/4\pi\varepsilon_0$. Try the spherically symmetric function $\phi=e^{-r/a}$, for which $\nabla^2\phi=(1/a^2-2/ar)\phi$. Substitution gives

```math
H\phi=\Big[-\frac{\hbar^2}{2ma^2}+\Big(\frac{\hbar^2}{ma}-k\Big)\frac1r\Big]\phi,\\
a_0=\frac{\hbar^2}{mk}=0.0529\ \mathrm{nm},\qquad
E_1=-\frac{mk^2}{2\hbar^2}=-13.6\ \mathrm{eV}.
```

The $1/r$ term must vanish for $\phi$ to be an eigenfunction, which fixes the Bohr radius $a_0$. The remaining constant is the ground-state energy. The full solution gives $E_n=E_1/n^2$, so the Lyman limit lies at $hc/|E_1|=91.1$ nm. Replacing $m$ by the reduced mass of electron and proton moves it to the observed 91.2 nm.

The equation treats the electron as nonrelativistic. In hydrogen its typical speed is $\alpha c$, with $\alpha\approx1/137$, so corrections of relative size $\alpha^2\approx5\times10^{-5}$ appear. They split levels of equal $n$ into the fine structure described under relativistic quantum mechanics. Spin, nuclear size and the coupling to the radiation field add smaller corrections, such as the Lamb shift. The abstract form $i\hbar\,d|\psi\rangle/dt=H|\psi\rangle$ applies to any closed system, and the organization of its solutions in time is treated under the Schrödinger picture.

## References For The Physical Derivation

- [A. Galler, J. Canfield and J. K. Freericks, Schrödinger's original quantum-mechanical solution for hydrogen; the 1926 wave-mechanical derivation of the hydrogen spectrum.](https://arxiv.org/abs/2007.14798)
