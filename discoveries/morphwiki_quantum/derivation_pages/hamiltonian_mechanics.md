# Hamiltonian mechanics

A pendulum, a planet or a charged particle in a magnet is fully described at one instant by its coordinates and momenta. As time passes, each point of this phase space moves, and a small patch of initial conditions deforms while keeping its area. Hamiltonian mechanics generates this motion from one function, the energy $H(q,p)$.

Start from a Lagrangian $L(q,\dot q)$ and define the canonical momentum $p=\partial L/\partial\dot q$. The Legendre transform $H=p\dot q-L$, written as a function of $q$ and $p$, yields Hamilton's equations. For any phase-space function $f(q,p)$ they combine into one rule through the Poisson bracket:

```math
\dot q_i=\frac{\partial H}{\partial p_i},\qquad \dot p_i=-\frac{\partial H}{\partial q_i},
\qquad \frac{df}{dt}=\{f,H\},\\
\{f,g\}=\sum_i\Big(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\Big),\qquad \{q_i,p_j\}=\delta_{ij}.
```

Three consequences follow. A function $G$ with $\{G,H\}=0$ is conserved, and the flow that $G$ generates leaves $H$ unchanged, which links symmetry to conservation as in Noether's theorem. The flow has zero divergence, so phase-space volume is conserved, which is Liouville's theorem. The bracket of a coordinate with its momentum is the same constant for every system.

Quantum mechanics keeps this structure and changes the bracket. Dirac's rule replaces functions by operators and the Poisson bracket by a commutator divided by $i\hbar$:

```math
\{f,g\}\;\longrightarrow\;\frac{1}{i\hbar}\big[\hat f,\hat g\big],\qquad
[\hat q_i,\hat p_j]=i\hbar\,\delta_{ij},\qquad
\frac{d\hat f}{dt}=\frac{1}{i\hbar}\big[\hat f,\hat H\big].
```

The equation of motion keeps its form and becomes the Heisenberg equation. Conserved quantities and symmetry generators carry over, and the conservation of phase-space volume is replaced by the unitarity of time evolution.

A charge $q$ of mass $m$ moving in the plane perpendicular to a uniform field $B$, with $qB>0$, shows the rule at work. In the symmetric gauge the canonical momenta are $p_x$ and $p_y$, but the velocity is fixed by the kinetic momenta $\pi_x=p_x+qBy/2$ and $\pi_y=p_y-qBx/2$. Their Poisson bracket does not vanish:

```math
\{\pi_x,\pi_y\}=qB\;\longrightarrow\;[\hat\pi_x,\hat\pi_y]=i\hbar qB,\qquad
H=\frac{\hat\pi_x^2+\hat\pi_y^2}{2m},\\
E_n=\hbar\omega_c\Big(n+\frac12\Big),\qquad \omega_c=\frac{qB}{m}.
```

Classically, the bracket produces circular motion at the cyclotron frequency $\omega_c$. Quantum mechanically, $\hat\pi_x/\sqrt{qB}$ and $\hat\pi_y/\sqrt{qB}$ form a canonical pair, and $H$ becomes a harmonic oscillator of frequency $\omega_c$. These Landau levels are spaced by 0.116 meV for a free electron in 1 T, equivalent to a temperature of 1.3 K. The orbit centre forms a second canonical pair that commutes with $H$, so each level holds $qB/h$ states per unit area. Landau quantization underlies the Shubnikov--de Haas oscillations and the quantum Hall effect, seen when the level spacing exceeds the thermal energy.

Dirac's rule is exact for the canonical pairs and for functions at most quadratic in them. It cannot hold for all higher polynomials at once: the Groenewold--van Hove theorem shows that no consistent map sends every Poisson bracket to the corresponding commutator. Operator ordering, such as $qp\to(\hat q\hat p+\hat p\hat q)/2$, then matters, and the brackets differ at order $\hbar^2$. The classical Hamiltonian guides the choice of quantum Hamiltonian but does not fix it uniquely. The operator side of this correspondence is developed under the canonical commutation relation and the Heisenberg picture.

## References For The Physical Derivation

- [M. J. Gotay, Obstructions to Quantization; the Groenewold-van Hove theorem and the limits of the Poisson-bracket to commutator rule.](https://arxiv.org/abs/math-ph/9809011)
- [D. Tong, Lectures on the Quantum Hall Effect; Landau levels from the kinetic momenta, their degeneracy and the quantum Hall effect.](https://arxiv.org/abs/1606.06687)
