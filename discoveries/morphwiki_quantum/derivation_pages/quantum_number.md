# Quantum number

The visible lines of hydrogen, such as the red Balmer line near 656 nm, are labelled by integers. With higher resolution each line splits into components, and a magnetic field splits them further. Quantum numbers name the stationary states between which these transitions occur. Which integers are good labels depends on which interactions the Hamiltonian contains.

A quantum number labels an eigenvalue of an observable that commutes with the Hamiltonian, so that its value is conserved by the evolution. Several such observables that also commute with one another can be diagonalized together. For the nonrelativistic hydrogen atom with a Coulomb potential, $H$, $L^2$, $L_z$ and $S_z$ form such a set:

```math
[H,L^2]=[H,L_z]=[L^2,L_z]=0,\qquad H\ket{n\,l\,m_l\,m_s}=E_n\ket{n\,l\,m_l\,m_s},\\
E_n=-\frac{R_y}{n^2},\qquad R_y=\frac{m_ee^4}{2(4\pi\varepsilon_0)^2\hbar^2}=13.6\ \mathrm{eV}.
```

Here $n=1,2,\ldots$; for each $n$ the orbital number $l$ runs from $0$ to $n-1$, $m_l$ from $-l$ to $l$, and $m_s=\pm1/2$. The ranges of $l$ and $m_l$ follow from the algebra of the angular momentum operator, and the bound $l\leq n-1$ from the radial equation. The energy depends on $n$ alone, so the number of states in a level is

```math
g_n=\sum_{l=0}^{n-1}2(2l+1)=2n^2.
```

The counts 2, 8, 18 and 32 match the shell capacities of the periodic table. In atoms with many electrons, screening by inner electrons removes the degeneracy in $l$, and the filling order departs from the shell order. The Balmer line connects $n=3$ to $n=2$, with $1/\lambda=(R_y/hc)(1/4-1/9)$ up to a small reduced-mass correction. Electric-dipole transitions obey $\Delta l=\pm1$ and $\Delta m_l=0,\pm1$, so the labels also decide which lines appear.

Spin-orbit coupling adds a term proportional to $\mathbf L\cdot\mathbf S=(J^2-L^2-S^2)/2$, which conserves the total angular momentum $\mathbf J=\mathbf L+\mathbf S$ but not $m_l$ or $m_s$ separately. The good quantum numbers become $n$, $l$, $j=l\pm1/2$ and $m_j$, and the resulting fine-structure splitting is worked out under the Dirac equation.

A magnetic field $B$ whose Zeeman energies are small compared with that splitting shifts each level according to $m_j$. The interaction $\mu_BB(L_z+g_sS_z)/\hbar$ is evaluated within a level of fixed $j$. The spin moment carries $g_s\approx2$ and the orbital moment carries one, so projecting both onto $\mathbf J$ gives the Landé factor:

```math
\Delta E=g_J\mu_BBm_j,\qquad g_J=1+\frac{j(j+1)+s(s+1)-l(l+1)}{2j(j+1)},\\
g_J(s_{1/2})=2,\qquad g_J(p_{1/2})=\tfrac23,\qquad g_J(p_{3/2})=\tfrac43.
```

An electric-dipole photon carries one unit of angular momentum, so only transitions with $\Delta m_j=0,\pm1$ appear. Their photon energies are shifted by $\mu_BB(g'm_j'-gm_j)$, where primes mark the upper level. For the sodium D lines, from $3p_{1/2}$ and $3p_{3/2}$ to $3s_{1/2}$, the shifts in units of $\mu_BB$ are

```math
\mathrm{D}_1:\ \pm\tfrac23,\ \pm\tfrac43\qquad\qquad \mathrm{D}_2:\ \pm\tfrac13,\ \pm1,\ \pm\tfrac53.
```

D1 therefore splits into four components and D2 into six. In a field of 1 T the outer D2 components lie 23 GHz from the line centre, far beyond the Doppler width of about 1.5 GHz in a sodium lamp. The field is still weak in the required sense, because the fine-structure splitting of sodium is 515 GHz. Hyperfine shifts from the nuclear spin are smaller and are neglected here. These patterns, the anomalous Zeeman effect, could be explained only after electron spin with $g_s\approx2$ was introduced. When both levels have zero total spin, as for the red cadmium line at 643.8 nm, $g_J=1$ in both levels. The components then merge into the normal triplet at $0$ and $\pm\mu_BB$. Viewed along the field, the $\Delta m_j=0$ component is absent, a direct test of the selection rule. A strong field decouples $\mathbf L$ from $\mathbf S$ and restores $m_l$ and $m_s$ as approximate labels.

Each quantum number thus records a symmetry of the Hamiltonian at a stated level of approximation. Rotational invariance conserves $j$ and $m_j$, and reflection symmetry gives the parity $(-1)^l$. The extra degeneracy in $l$ of the pure Coulomb problem comes from a further conserved quantity, the Laplace--Runge--Lenz vector. An interaction that breaks a symmetry splits a level into components carrying the new labels, and spectroscopy measures those splittings.

## References For The Physical Derivation

- [M. I. Eides, H. Grotch and V. A. Shelyuto, Theory of Light Hydrogenlike Atoms; Dirac fine structure and the Lamb shift in hydrogen.](https://arxiv.org/abs/hep-ph/0002158)
