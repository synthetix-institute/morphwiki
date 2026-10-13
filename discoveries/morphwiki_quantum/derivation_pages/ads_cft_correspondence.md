# AdS/CFT correspondence

A scalar field in anti-de Sitter space does not radiate away to infinity. Near the boundary its amplitude falls off as a definite power of a radial coordinate. The AdS/CFT correspondence identifies that power with the scaling dimension of an operator in a conformal field theory defined on the boundary. The relation follows from the bulk wave equation alone. In Poincaré coordinates the metric of $(d+1)$-dimensional anti-de Sitter space with curvature radius $L$ is

```math
ds^2=\frac{L^2}{z^2}\big(dz^2+\eta_{\mu\nu}dx^\mu dx^\nu\big),\qquad z>0,
```

where $x^\mu$ are the $d$ coordinates of the boundary, which is reached as $z\to0$. A free scalar of mass $m$ obeys $(\Box-m^2)\phi=0$, with $\Box\phi=g^{-1/2}\partial_a(g^{1/2}g^{ab}\partial_b\phi)$. Near the boundary the derivatives along $x$ carry an extra factor $z^2$ relative to the radial terms. A power law $\phi\propto z^\Delta$ is therefore tested against the radial part only. Using $\sqrt g=(L/z)^{d+1}$ and $g^{zz}=z^2/L^2$ gives

```math
\Box\,z^\Delta=\frac{z^{d+1}}{L^2}\,\partial_z\big(z^{1-d}\partial_z z^\Delta\big)
=\frac{\Delta(\Delta-d)}{L^2}\,z^\Delta
\qquad\Rightarrow\qquad \Delta(\Delta-d)=m^2L^2.
```

The two roots are $\Delta_\pm=d/2\pm\sqrt{d^2/4+m^2L^2}$, and their sum is $d$. A general solution behaves as $\phi\to z^{d-\Delta}\phi_0(x)+z^{\Delta}A(x)$ with $\Delta=\Delta_+$. The coefficient $\phi_0$ of the slower falloff is fixed by a boundary condition. The rescaling $z\to\lambda z$, $x\to\lambda x$ is an isometry of the metric, and under it $\phi_0$ transforms as a field of dimension $d-\Delta$. The correspondence treats $\phi_0$ as a source $J$ coupled to a boundary operator $\mathcal O$. The coupling $\int d^dx\,J\mathcal O$ is dimensionless only if $\mathcal O$ has dimension $\Delta$. The dictionary is an equality of generating functionals:

```math
Z_{\rm CFT}[J]=\Big\langle \exp\int d^dx\,J\,\mathcal O\Big\rangle_{\rm CFT}
=Z_{\rm bulk}\big[\phi\to z^{d-\Delta}J\big].
```

Both roots are real only if $m^2L^2\geq-d^2/4$. This is the Breitenlohner--Freedman bound. A field with slightly negative mass squared is stable in anti-de Sitter space, because the curvature confines it and its gradient energy outweighs the negative mass term. In the conformal field theory $\Delta$ fixes the power law of the two-point function, $\langle\mathcal O(x)\mathcal O(0)\rangle\propto|x|^{-2\Delta}$. The bulk calculation reproduces this from the propagation of $\phi$ between two boundary points.

The best-tested case pairs string theory on $AdS_5\times S^5$ with $\mathcal N=4$ supersymmetric $SU(N)$ gauge theory, so $d=4$. The dilaton is massless in five dimensions, so $\Delta=4$. It couples to the Lagrangian density $\operatorname{Tr}F^2$ of the gauge theory, whose dimension is four. Kaluza--Klein modes on the five-sphere give scalars with $m^2L^2=k(k-4)$ for integers $k\geq2$. The relation gives $\Delta=2+|k-2|=k$, which matches symmetrized traces of $k$ scalar fields of the gauge theory. The $k=2$ mode sits exactly at the bound, $m^2L^2=-4$, and is stable. Supersymmetry protects these dimensions, so the free-field value can be compared with the classical bulk value.

The classical bulk calculation requires $L$ to be large compared with the string length and the Planck length. For the $\mathcal N=4$ theory this means large $N$ and large 't Hooft coupling $\lambda=g_{\rm YM}^2N$, since $L^4/\alpha'^2=\lambda$. Away from that regime string and quantum corrections enter. The correspondence remains a conjecture: it has passed many quantitative checks of protected spectra and correlators, but it has no general proof. Because the bulk contains gravity, it is used to study quantum gravity in anti-de Sitter space through an ordinary gauge theory.

## References For The Physical Derivation

- [O. Aharony, S. S. Gubser, J. Maldacena, H. Ooguri and Y. Oz, Large N Field Theories, String Theory and Gravity; mass-dimension relation, field-operator dictionary and the AdS5 x S5 spectrum.](https://arxiv.org/abs/hep-th/9905111)
- [E. Witten, Anti De Sitter Space And Holography; boundary values of bulk fields as sources of boundary operators.](https://arxiv.org/abs/hep-th/9802150)
- [S. S. Gubser, I. R. Klebanov and A. M. Polyakov, Gauge Theory Correlators from Non-Critical String Theory; generating functional of boundary correlators.](https://arxiv.org/abs/hep-th/9802109)
