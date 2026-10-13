# Quantum entanglement

Polarization-entangled photon pairs from parametric down-conversion each appear unpolarized when examined alone: a polarizer at any angle passes half of them. When both photons of a pair meet linear polarizers set to a common angle, whichever angle is chosen, their results agree. Pairs with definite and correlated polarizations can reproduce the agreement along one axis, but not along two axes such as $0^\circ$ and $45^\circ$. A joint state that does not factor into states of the two photons accounts for both observations.

For subsystems $A$ and $B$ the joint state space is the tensor product $\mathcal H_A\otimes\mathcal H_B$. Expand a pure state as $\ket\Psi=\sum_{ij}c_{ij}\ket{i}\ket{j}$ in product bases. The singular-value decomposition of the coefficient matrix $c$ rewrites it as a single sum, the Schmidt form:

```math
\ket\Psi=\sum_k\sqrt{\lambda_k}\,\ket{k_A}\ket{k_B},\qquad \sum_k\lambda_k=1,\qquad
\rho_A=\operatorname{Tr}_B\ket\Psi\bra\Psi=\sum_k\lambda_k\ket{k_A}\bra{k_A}.
```

The state is a product exactly when only one Schmidt coefficient is nonzero. Otherwise each subsystem is in a mixed state although the pair is pure. Both reduced states have the eigenvalues $\lambda_k$, so the entanglement entropy is the same on either side:

```math
S_A=-\operatorname{Tr}\rho_A\log_2\rho_A=-\sum_k\lambda_k\log_2\lambda_k=S_B.
```

Local unitary operations change the Schmidt vectors but not the coefficients. Local operations assisted by classical communication cannot increase this entropy on average. For $\cos\theta\ket{HH}+\sin\theta\ket{VV}$ the coefficients are $\cos^2\theta$ and $\sin^2\theta$. The choice $\theta=\pi/4$ gives one bit, the largest value for two-level systems, and $\theta=\pi/8$ gives 0.60 bit.

Noise turns a pure pair into a mixed state, and then the failure of one product decomposition proves nothing. A mixed state is separable when it can be written as $\rho=\sum_kp_k\rho_k^A\otimes\rho_k^B$ with probabilities $p_k$, and entangled otherwise. Transposing only the $B$ factor maps every separable state to a positive operator. The Werner state mixes the singlet $\ket{\Psi^-}$ with white noise, and its partial transpose has the eigenvalues

```math
\rho_W=p\ket{\Psi^-}\bra{\Psi^-}+(1-p)\frac{I}{4},\qquad
\operatorname{spec}\rho_W^{T_B}=\left\{\tfrac{1+p}{4},\tfrac{1+p}{4},\tfrac{1+p}{4},\tfrac{1-3p}{4}\right\}.
```

A negative eigenvalue appears for $p>1/3$, and for two qubits the criterion of Peres and the Horodeckis is also sufficient. The largest Clauser--Horne--Shimony--Holt combination for this state is $2\sqrt2\,p$, so the inequality is violated only for $p>1/\sqrt2\approx0.71$. For $1/3<p\leq1/\sqrt2$ the pairs are entangled, yet their correlations violate no such inequality. Werner constructed a local hidden-variable model for all projective measurements when $p\leq1/2$. Entanglement and Bell nonlocality are therefore different properties; Bell's theorem concerns the second.

Entanglement is defined relative to a stated division into subsystems. A single photon sent through a balanced beam splitter is entangled between the two output modes, while in the input modes it is a product of one photon and vacuum. The relevant division is the one matched to the available operations, such as two separate laboratories. With that division fixed, a shared Bell pair is the resource consumed in quantum teleportation.

## References For The Physical Derivation

- [R. Horodecki, P. Horodecki, M. Horodecki and K. Horodecki, Quantum Entanglement; Schmidt decomposition, entropy, separability, Werner states and Bell inequalities.](https://arxiv.org/abs/quant-ph/0702225)
- [A. Peres, Separability Criterion for Density Matrices; the partial-transpose test and its application to Werner states.](https://arxiv.org/abs/quant-ph/9604005)


## Source Equations

- [arXiv:math-ph/0211065](https://arxiv.org/abs/math-ph/0211065)
