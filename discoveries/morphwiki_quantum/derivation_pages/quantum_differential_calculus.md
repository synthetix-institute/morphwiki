# Quantum differential calculus

An electron hopping between neighbouring atoms of a crystal changes its position in steps of the lattice constant $a$. Its kinetic energy then involves differences of the wave function between sites, not derivatives. On such a lattice the product rule of ordinary calculus fails. Repairing it gives the simplest example of a quantum differential calculus.

The name comes from quantum groups and noncommutative geometry. It denotes a consistent algebra of functions and differentials, not the quantization of a mechanical system. Take the forward difference $\partial f(x)=[f(x+a)-f(x)]/a$. Expanding the difference of a product gives an extra term:

```math
\partial(fg)=(\partial f)\,g+f\,(\partial g)+a\,(\partial f)(\partial g).
```

The extra term vanishes as $a\to0$. It can be removed exactly at finite $a$ if the differential $dx$ no longer commutes with functions. Define $df=(\partial f)\,dx$ and require the ordinary Leibniz rule $d(fg)=(df)\,g+f\,dg$. Both are consistent only if moving a function across $dx$ shifts its argument:

```math
dx\,f(x)=f(x+a)\,dx,\qquad dx\,x-x\,dx=a\,dx.
```

Functions on the lattice commute with each other, but differentials do not commute with them. This is a noncommutative differential calculus on a commutative algebra. Replacing the translation by a dilation gives Jackson's q-derivative, $D_qf(x)=[f(qx)-f(x)]/[(q-1)x]$, with $dx\,f(x)=f(qx)\,dx$. On powers it produces the q-numbers:

```math
D_qx^n=[n]_qx^{n-1},\qquad [n]_q=\frac{q^n-1}{q-1}=1+q+\cdots+q^{n-1}.
```

The lattice calculus has a measurable consequence. The kinetic energy built from a forward and a backward difference has plane waves $e^{ikx}$ as eigenfunctions, with

```math
E(k)=\frac{2\hbar^2}{ma^2}\sin^2\frac{ka}{2}
=\frac{\hbar^2k^2}{2m}-\frac{\hbar^2a^2k^4}{24m}+\cdots
```

The group velocity $(\hbar/ma)\sin ka$ vanishes at the zone edge $k=\pi/a$. A constant force $F$ advances $k$ uniformly in time, so the velocity oscillates instead of growing. The period of this Bloch oscillation is $2\pi\hbar/(Fa)$. The same structure describes the lowest band of a deep optical lattice, with a hopping energy in place of $\hbar^2/(2ma^2)$. The period does not depend on the hopping. In a vertical lattice of spacing 266 nanometres, gravity gives strontium-88 atoms a Bloch frequency $mga/h$ of about 574 hertz. Bloch oscillations of strontium-88 in a vertical optical lattice have been followed for several seconds and used to measure gravity at micrometre scales. The single-band description holds while the force is too weak to drive transitions to the next band.

The q-calculus has a less direct physical status. For a q-deformed oscillator with $aa^\dagger-qa^\dagger a=1$, the operator $a^\dagger a$ has eigenvalues $[n]_q$, so its levels are unequally spaced. To first order in $q-1$ the spacing changes linearly with $n$, like the anharmonic term of a molecular vibrational ladder. Such fits are phenomenological. It is established that these calculi are consistent algebraic structures. Quantum-group symmetry also appears exactly in integrable models, such as the anisotropic XXZ spin chain with suitable boundary terms. Whether spacetime itself has a deformed differential structure at short distances is open, and no experiment has shown it.

## References For The Physical Derivation

- [A. Dimakis and F. Müller-Hoissen, Discrete differential calculus, graphs, topologies and gauge theory; differential calculus on discrete sets with noncommuting differentials.](https://arxiv.org/abs/hep-th/9404112)
- [G. Ferrari, N. Poli, F. Sorrentino and G. M. Tino, Long-lived Bloch oscillations with bosonic Sr atoms and application to gravity measurement at micrometer scale; lattice dispersion and the Bloch period in gravity.](https://arxiv.org/abs/physics/0605018)
