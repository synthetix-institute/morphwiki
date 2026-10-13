# Commutator

Rotating a spin by a small angle about $x$, then about $y$, and then reversing both rotations in the same order leaves it rotated about $z$. The net rotation is of second order in the angle. Its size and axis are fixed by the commutator of the two generators, not by either rotation alone.

The commutator $[A,B]=AB-BA$ compares the two orders of applying two operators. For generators $X$ and $Y$ of transformations, the Baker--Campbell--Hausdorff formula gives $e^Xe^Y=\exp(X+Y+\tfrac12[X,Y]+\cdots)$. The four-step loop therefore has the commutator as its leading term. For spin rotations $R_{\mathbf n}(\varepsilon)=e^{-i\varepsilon\,\mathbf n\cdot\boldsymbol\sigma/2}$, with $[\sigma_x,\sigma_y]=2i\sigma_z$, this gives

```math
e^Xe^Ye^{-X}e^{-Y}=e^{[X,Y]+O(3)},\\
R_x(\varepsilon)R_y(\varepsilon)R_x(-\varepsilon)R_y(-\varepsilon)=R_z(\varepsilon^2)+O(\varepsilon^3).
```

The operator product acts from right to left. For $\varepsilon=0.1$ radian the exact product is a rotation by 0.0100 radian about an axis tilted about four degrees from $z$. Reversing the orientation of the loop reverses the sense of the rotation. Pulse sequences in magnetic resonance generate rotations about $z$ from $x$ and $y$ pulses alone. More generally, repeated commutators of the available Hamiltonians determine which operations a set of controls can reach.

The same term measures the error of splitting an evolution. Approximating $e^{-i(A+B)t/\hbar}$ by alternating $A$ and $B$ gives

```math
e^{-iAt/\hbar}e^{-iBt/\hbar}
=\exp\!\left(-\frac{i(A+B)t}{\hbar}-\frac{t^2}{2\hbar^2}[A,B]+\cdots\right).
```

Divided into $n$ steps, the error is bounded to leading order by $t^2\|[A,B]\|/(2n\hbar^2)$, which sets the cost of digital quantum simulation. Commuting terms can be split without error.

Two identities make commutators computable. The Leibniz rule $[A,BC]=[A,B]C+B[A,C]$ reduces composite expressions to simple ones, and the Jacobi identity relates commutators of commutators. For example, $[L_z,x]=i\hbar y$ and $[L_z,y]=-i\hbar x$ give $[L_z,x^2+y^2]=0$. The generator of rotations about $z$ therefore commutes with any potential that depends on $x$ and $y$ only through $x^2+y^2$.

Commuting Hermitian operators share an eigenbasis. If $[A,B]=0$ and $A|a\rangle=a|a\rangle$, then $A(B|a\rangle)=aB|a\rangle$, so $B$ maps each eigenspace of $A$ into itself and can be diagonalized there. The labels $n,\ell,m$ of hydrogen come from the commuting set $H$, $L^2$, $L_z$. A measurement of $L_x$ on such an eigenstate preserves $n$ and $\ell$, because $L_x$ also commutes with $H$ and $L^2$, but it generally leaves no definite value of $m$. A nonzero commutator excludes a complete common eigenbasis but not every common eigenvector: all three components of $L$ annihilate an $\ell=0$ state.

For unbounded operators, commuting on a common dense domain does not guarantee that the spectral projectors commute. Nelson constructed operators with that property whose unitary groups fail to commute. Compatibility is therefore defined through the projectors or the unitary groups. The uncertainty principle turns a nonzero commutator into a bound on spreads, and the Heisenberg picture uses $[H,A]$ for the time dependence of $A$.

## References For The Physical Derivation

- [A. M. Childs, Y. Su, M. C. Tran, N. Wiebe and S. Zhu, A Theory of Trotter Error; product-formula errors controlled by commutators of the Hamiltonian terms.](https://arxiv.org/abs/1912.08854)


## Source Equations

- [arXiv:quant-ph/0005019](https://arxiv.org/abs/quant-ph/0005019)
- [arXiv:quant-ph/0001056](https://arxiv.org/abs/quant-ph/0001056)
- [arXiv:hep-ph/0104068](https://arxiv.org/abs/hep-ph/0104068)
