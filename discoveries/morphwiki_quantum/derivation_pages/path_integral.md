# Path integral

A particle released near one point at time $t_i$ is later detected near another point at time $t_f$. The amplitude for this transition is the propagator $K(x_f,t_f;x_i,t_i)=\langle x_f|U(t_f-t_i)|x_i\rangle$. It evolves any initial wave function by $\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i$. The path integral computes $K$ by cutting the time interval into many short steps.

Divide $T=t_f-t_i$ into $N$ steps of length $\epsilon=T/N$, and insert a complete set of position states at each intermediate time. For $H=P^2/2m+V(X)$, the Trotter product formula factors each short step into a kinetic and a potential part, with an error of order $\epsilon^2$ per step. The kinetic factor is Gaussian in momentum, and integrating over momentum gives

```math
K=\lim_{N\to\infty}\Big(\frac{m}{2\pi i\hbar\epsilon}\Big)^{N/2}
\int dx_1\cdots dx_{N-1}\,e^{iS_N/\hbar},\\
S_N=\sum_{k=0}^{N-1}\epsilon\Big[\frac m2\Big(\frac{x_{k+1}-x_k}{\epsilon}\Big)^2-V(x_k)\Big],
\qquad x_0=x_i,\quad x_N=x_f.
```

Each set of intermediate positions defines a broken-line path, and $S_N$ is the classical action along it. The limit is written $\int\mathcal Dx\,e^{iS[x]/\hbar}$. The measure has no meaning apart from this limit: the factors $(m/2\pi i\hbar\epsilon)^{1/2}$ diverge as $\epsilon\to0$ and are compensated by the oscillating integrals. In imaginary time the weights become Gaussian probabilities, the limit exists as a Wiener integral, and typical paths are continuous but nowhere differentiable.

For a free particle every integral is Gaussian. Integrating over one intermediate point joins two free kernels of durations $t_1$ and $t_2$ into one of duration $t_1+t_2$, because completing the square leaves an exponent quadratic in the endpoints. Repeating the step $N-1$ times gives the exact free propagator:

```math
\int K_0(x_f,x;t_2)\,K_0(x,x_i;t_1)\,dx=K_0(x_f,x_i;t_1+t_2),\\
K_0(x_f,x_i;T)=\sqrt{\frac{m}{2\pi i\hbar T}}\,
\exp\Big[\frac{im(x_f-x_i)^2}{2\hbar T}\Big].
```

This kernel solves the free Schrödinger equation and tends to $\delta(x_f-x_i)$ as $T\to0$. Its modulus is the same for every endpoint. A particle released from a point therefore reaches all positions with equal amplitude magnitude, while the phase records the velocity $(x_f-x_i)/T$ needed to arrive.

Applied to a packet of width $\sigma$, the kernel gives the time-of-flight relation. For $T\gg m\sigma^2/\hbar$ the phase $mx_i^2/2\hbar T$ is negligible across the packet. The remaining integral is a Fourier transform evaluated at the momentum $mx/T$:

```math
|\psi(x,T)|^2\;\to\;\frac mT\,\Big|\widetilde\psi\Big(\frac{mx}{T}\Big)\Big|^2,
\qquad T\gg\frac{m\sigma^2}{\hbar}.
```

Absorption images of ultracold atoms taken after release from a trap therefore record the momentum distribution. Two condensates released a distance $d$ apart overlap with fringes of spacing $hT/(md)$, as observed by Andrews and colleagues in 1997. For sodium with $d=40\,\mu\mathrm m$ and $T=40$ ms the spacing is about $17\,\mu\mathrm m$.

The relation assumes free flight. Gravity adds a linear potential, for which the slicing is again exactly Gaussian, whereas interactions during the early expansion must be treated separately. For a charge in a magnetic field the potential term depends on velocity, and the midpoint of each step must be used to obtain the correct Hamiltonian. How the integral is dominated by classical paths when the action is large compared with $\hbar$ is treated under path integral formulation.

## References For The Physical Derivation

- [R. MacKenzie, Path Integral Methods and Applications; time slicing, the free-particle Gaussian integrals and the propagator.](https://arxiv.org/abs/quant-ph/0004090)
- [C. Grosche, An Introduction into the Feynman Path Integral; the lattice definition of the path integral and its ordering prescriptions.](https://arxiv.org/abs/hep-th/9302097)
