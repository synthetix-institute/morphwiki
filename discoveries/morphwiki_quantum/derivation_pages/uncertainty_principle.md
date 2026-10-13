# Uncertainty principle

A beam of molecules passing a slit spreads as the slit is narrowed. Nairz, Arndt and Zeilinger measured this broadening for C70 fullerene molecules at a temperature of 900 kelvin. The slit width times the momentum transfer to the first diffraction minimum equalled Planck's constant $h$. A narrower position distribution forces a wider momentum distribution, a statement that holds for every preparation, not only for a disturbed one.

For observables $A$ and $B$ and a normalized state $\psi$, define $f=(A-\langle A\rangle)\psi$ and $g=(B-\langle B\rangle)\psi$. The variances are $\sigma_A^2=\langle f|f\rangle$ and $\sigma_B^2=\langle g|g\rangle$. The overlap $\langle f|g\rangle$ has a real part equal to the covariance and an imaginary part equal to $\langle[A,B]\rangle/2i$. The Cauchy--Schwarz inequality $|\langle f|g\rangle|^2\leq\langle f|f\rangle\langle g|g\rangle$ then gives the Robertson--Schrödinger relation:

```math
\sigma_A^2\sigma_B^2\geq
\left(\tfrac12\langle\{A,B\}\rangle-\langle A\rangle\langle B\rangle\right)^2
+\left|\frac{\langle[A,B]\rangle}{2i}\right|^2.
```

Dropping the covariance gives Robertson's form $\sigma_A\sigma_B\geq\tfrac12|\langle[A,B]\rangle|$. For position and momentum it becomes $\hbar/2$, as derived under the canonical commutation relation.

The bound depends on the state. For a spin 1/2 with Bloch vector $\mathbf r$, the spin components give $\sigma_{S_x}^2=\tfrac{\hbar^2}{4}(1-r_x^2)$, $\sigma_{S_y}^2=\tfrac{\hbar^2}{4}(1-r_y^2)$ and $\langle[S_x,S_y]\rangle=i\hbar^2r_z/2$. For a spin along $x$ the Robertson bound is zero, although $S_y$ is maximally spread. Pure states satisfy the full relation with equality, because in two dimensions $f$ and $g$ are both orthogonal to $\psi$ and hence parallel:

```math
(1-r_x^2)(1-r_y^2)=r_z^2+r_x^2r_y^2\qquad (|\mathbf r|=1).
```

An entropic form removes the state dependence. Maassen and Uffink proved that the Shannon entropies of two measurements obey $H(A)+H(B)\geq-2\log_2c$, where $c$ is the largest overlap between their eigenvectors. For $S_z$ and $S_x$ of a spin 1/2, $c=1/\sqrt2$:

```math
H(Z)+H(X)\geq1\ \text{bit}.
```

A $z$ eigenstate attains the bound with $H(Z)=0$ and $H(X)=1$. This form enters the security proofs of quantum key distribution.

Standard deviations can also fail to describe a measurement. A slit of width $w$ with uniform amplitude has position spread $w/\sqrt{12}$. Its momentum amplitude is proportional to $\sin(pw/2\hbar)/p$, whose variance is infinite, so the variance relation holds trivially and says nothing. The central diffraction peak, between zeros at $p=\pm h/w$, contains 90.3 percent of the probability. The product of slit width and peak half-width is $h$, the relation found in the fullerene experiment. A width that contains a fixed fraction of the probability is therefore the meaningful measure of spread here.

These relations concern spreads in identically prepared ensembles. Relations between the error of one measurement and the disturbance it causes to another are separate inequalities with their own definitions. One such relation, proposed by Ozawa, has been tested with successive measurements of neutron spins. The commutator and the Fourier transform give the operator and wave pictures of the same incompatibility.

## References For The Physical Derivation

- [O. Nairz, M. Arndt and A. Zeilinger, Experimental verification of the Heisenberg uncertainty principle for hot fullerene molecules; slit width times momentum transfer to the first minimum equals h.](https://arxiv.org/abs/quant-ph/0105061)
- [P. J. Coles, M. Berta, M. Tomamichel and S. Wehner, Entropic Uncertainty Relations and their Applications; the Maassen--Uffink bound and its cryptographic uses.](https://arxiv.org/abs/1511.04857)
- [J. Erhart and colleagues, Experimental demonstration of a universally valid error-disturbance uncertainty relation in spin-measurements; neutron test of Ozawa's relation.](https://arxiv.org/abs/1201.1833)
