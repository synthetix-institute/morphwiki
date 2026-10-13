# Creation and annihilation operators

A short density pulse made at the centre of an elongated Bose--Einstein condensate travels along it at a few millimetres per second. That speed, and the change from sound to free-particle motion at short wavelengths, follow from the algebra of the operators that add or remove one atom from a mode.

Let $i$ label orthonormal single-particle modes, such as plane waves in a box or the vibrational modes of a trap. A state with $n_i$ quanta in mode $i$ is written $|\dots,n_i,\dots\rangle$. For bosons the creation operator $a_i^\dagger$ and the annihilation operator $a_i$ act as follows, while fermion operators $c_i$ obey anticommutators:

```math
a_i^\dagger|\dots,n_i,\dots\rangle=\sqrt{n_i+1}\,|\dots,n_i+1,\dots\rangle,\qquad
a_i|\dots,n_i,\dots\rangle=\sqrt{n_i}\,|\dots,n_i-1,\dots\rangle,\\
N_i=a_i^\dagger a_i,\qquad [a_i,a_j^\dagger]=\delta_{ij},\qquad
\{c_i,c_j^\dagger\}=\delta_{ij},\qquad \{c_i,c_j\}=0.
```

The square-root factors make $N_i$ count the quanta in mode $i$, and they follow from the commutator alone. Setting $i=j$ in $\{c_i,c_j\}=0$ gives $(c_i^\dagger)^2=0$, so no mode can hold two fermions. This is the Pauli exclusion principle, obtained without writing an antisymmetric wave function.

One-body observables are sums of single products: if $o_{ij}$ is the matrix element of a single-particle operator between modes, the many-particle operator is $O=\sum_{ij}o_{ij}a_i^\dagger a_j$. A two-body interaction needs two creation and two annihilation operators. Consider bosons of mass $m$ in a box of volume $V$, with plane-wave modes $\mathbf k$ and a contact interaction of strength $g=4\pi\hbar^2a_s/m$ fixed by the s-wave scattering length $a_s$:

```math
H=\sum_{\mathbf k}\epsilon_k\,a_{\mathbf k}^\dagger a_{\mathbf k}
+\frac{g}{2V}\sum_{\mathbf k,\mathbf k',\mathbf q}
a_{\mathbf k+\mathbf q}^\dagger a_{\mathbf k'-\mathbf q}^\dagger a_{\mathbf k'}a_{\mathbf k},
\qquad \epsilon_k=\frac{\hbar^2k^2}{2m}.
```

Each interaction term removes atoms from modes $\mathbf k$ and $\mathbf k'$ and returns them with momentum $\hbar\mathbf q$ exchanged, so total momentum is conserved. In the condensate nearly all $N$ atoms occupy $\mathbf k=0$, where $a_0$ and $a_0^\dagger$ multiply by about $\sqrt N$. Bogoliubov replaced both by $\sqrt N$ and kept the terms quadratic in the other operators. With density $n=N/V$,

```math
H\approx\frac{gnN}{2}+\sum_{\mathbf k\neq0}\Big[(\epsilon_k+gn)\,a_{\mathbf k}^\dagger a_{\mathbf k}
+\frac{gn}{2}\big(a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger+a_{\mathbf k}a_{-\mathbf k}\big)\Big].
```

The pair terms move two atoms with opposite momenta out of the condensate or back into it. They are removed by mixing $a_{\mathbf k}$ with $a_{-\mathbf k}^\dagger$:

```math
b_{\mathbf k}=u_ka_{\mathbf k}+v_ka_{-\mathbf k}^\dagger,\qquad
u_k^2=\frac12\Big(\frac{\epsilon_k+gn}{E_k}+1\Big),\qquad v_k^2=u_k^2-1,\\
H=E_0+\sum_{\mathbf k\neq0}E_k\,b_{\mathbf k}^\dagger b_{\mathbf k},\qquad
E_k=\sqrt{\epsilon_k(\epsilon_k+2gn)}.
```

The condition $u_k^2-v_k^2=1$ keeps $[b_{\mathbf k},b_{\mathbf k}^\dagger]=1$, so $b_{\mathbf k}$ removes one quasiparticle with bosonic statistics. At long wavelength $E_k\approx\hbar ck$, a sound wave with speed $c=\sqrt{gn/m}$. At short wavelength $E_k\approx\epsilon_k+gn$, a free atom raised by the mean interaction energy. The crossover lies at the healing length $\xi=\hbar/\sqrt{2mgn}$, where $\epsilon_k=gn$ for $k=1/\xi$.

For sodium, $a_s=2.75$ nm. At a density of $10^{14}\,\mathrm{cm}^{-3}$ this gives $c=5.1$ mm/s and $\xi=0.38\,\mu\mathrm m$. Andrews and colleagues excited density pulses in elongated sodium condensates in 1997 and imaged them as they moved. The measured speeds were several millimetres per second and grew with density as the theory predicts. In a cigar-shaped cloud the pulse samples the whole cross-section. The speed is then set by the density averaged over that section, half the central value for a Thomas--Fermi profile, which lowers $c$ by a factor $\sqrt2$.

The treatment requires a dilute gas, $na_s^3\ll1$. Even at zero temperature the pair terms keep a fraction $(8/3)\sqrt{na_s^3/\pi}$ of the atoms outside the condensate, 0.2 percent for these numbers. Because $E_k/\hbar k$ never falls below $c$, an impurity moving slower than $c$ cannot create excitations, which is Landau's criterion for superfluidity. A single mode reproduces the ladder of the quantum harmonic oscillator, and the same pair terms describe squeezed light in quantum optics.

## References For The Physical Derivation

- [F. Dalfovo, S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of Bose-Einstein condensation in trapped gases; Bogoliubov theory, the excitation spectrum, sound, healing length and depletion.](https://arxiv.org/abs/cond-mat/9806038)
- [E. Zaremba, Sound propagation in a cylindrical Bose-condensed gas; pulses in elongated condensates travel at a speed set by the density averaged over the cross-section.](https://arxiv.org/abs/cond-mat/9708237)
