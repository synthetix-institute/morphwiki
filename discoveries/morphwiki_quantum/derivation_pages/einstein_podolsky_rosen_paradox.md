# Einstein–Podolsky–Rosen paradox

Two particles interact and fly apart so that both their separation and their total momentum are sharply fixed. Measuring the position of one particle then predicts the position of the other, and measuring its momentum predicts the other's momentum. In 1935 Einstein, Podolsky and Rosen argued that both predicted values must correspond to physical properties of the distant particle.

Such a state exists because the relative position and the total momentum commute. With $x_j$ and $p_j$ the position and momentum of particle $j$,

```math
[x_1-x_2,\;p_1+p_2]=[x_1,p_1]-[x_2,p_2]=i\hbar-i\hbar=0,\\
\psi(x_1,x_2)\propto\delta(x_1-x_2-L)=\frac{1}{2\pi\hbar}\int e^{ip(x_1-x_2-L)/\hbar}dp.
```

The integral shows that the same state contains every momentum pair $(p,-p)$. A position measurement on particle 1 that gives $\xi$ predicts $x_2=\xi-L$, and a momentum measurement giving $\kappa$ predicts $p_2=-\kappa$. Neither measurement acts on particle 2. EPR concluded that particle 2 has definite position and momentum, which no quantum state of particle 2 alone can describe. Hence, they argued, the quantum description is incomplete.

The ideal state is not normalizable, but an optical version is. A nondegenerate parametric amplifier produces two beams in a two-mode squeezed state. Use dimensionless field quadratures with $[x_j,p_j]=i$ and vacuum variance 1/2, and squeezing parameter $r$. Then $\operatorname{Var}(x_1-x_2)=\operatorname{Var}(p_1+p_2)=e^{-2r}$, while each beam alone shows enlarged noise $\cosh(2r)/2$.

Reid turned the argument into a measurable test. Let $\Delta^2_{\rm inf}x_2$ be the smallest mean-square error with which $x_2$ can be predicted from a record of $x_1$, and similarly for $p_2$. If beam 2 had a local quantum state, the uncertainty principle would require the product of these inferred variances to be at least 1/4. The best linear prediction gives

```math
\Delta^2_{\rm inf}x_2=\Delta^2_{\rm inf}p_2=\frac{1}{2\cosh2r},\qquad
\Delta^2_{\rm inf}x_2\,\Delta^2_{\rm inf}p_2=\frac{1}{4\cosh^22r}<\frac14.
```

At $r=0.5$ the product is $0.105$, well below the bound. Ou, Pereira, Kimble and Peng observed an inferred-variance product below the bound in 1992. Loss on either beam adds vacuum noise and raises the inferred variances, so the demonstration requires efficient transmission and detection.

The EPR argument does not by itself exclude local hidden variables. The Wigner function of the two-mode squeezed state is a positive Gaussian, which can serve as a local probability distribution for all quadrature records. Bell showed that other measurements, such as spin components along several axes, separate the options. Bell's theorem decides between local models and quantum predictions, whereas the EPR test shows that local states of one particle cannot explain the predictions made from the other. Quantum nonlocality treats the stronger correlations in multipartite states.

## References For The Physical Derivation

- [M. D. Reid and colleagues, The Einstein-Podolsky-Rosen paradox: from concepts to applications; inferred-variance criterion and two-mode squeezed states.](https://arxiv.org/abs/0806.0270)
