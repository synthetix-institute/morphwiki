# Loop quantum gravity

If space is quantized, the area of a surface should take discrete values, as the energy of an atom does. Loop quantum gravity gives a definite spectrum for area. It quantizes general relativity written with an $SU(2)$ connection $A^i_a$ and its conjugate momentum $E^a_i$, a densitized triad that encodes the spatial metric. In units with $c=1$, the Poisson bracket and the area of a surface $S$ are

```math
\{A^i_a(x),E^b_j(y)\}=8\pi G\gamma\,\delta^b_a\delta^i_j\,\delta^3(x-y),\\
A(S)=\int_Sd^2\sigma\,\sqrt{n_aE^a_i\,n_bE^b_i}.
```

Here $\gamma$ is the Barbero--Immirzi parameter, $a$ a spatial index, $i$ an internal index and $n_a$ the normal to $S$. The states are functions of holonomies, the path-ordered exponentials of $A$ along the edges of a graph $\Gamma$. Each edge carries a spin $j$. Quantization turns $E$ into $-i\,8\pi\gamma l_P^2\,\delta/\delta A$, with $l_P^2=\hbar G$. On an edge crossing $S$, the flux of $E$ through $S$ acts as $8\pi\gamma l_P^2$ times the $SU(2)$ generator $\mathbf J$ of that edge. The square root of $\mathbf J^2=j(j+1)$ then gives a finite contribution from each crossing:

```math
\hat A(S)\,|\Gamma,\{j\}\rangle=8\pi\gamma l_P^2\sum_{p\in S\cap\Gamma}\sqrt{j_p(j_p+1)}\;|\Gamma,\{j\}\rangle.
```

The sum runs over the points where edges puncture the surface. A surface crossed by no edge has zero area. The spectrum is discrete, and its smallest nonzero eigenvalue comes from one spin-$1/2$ puncture: $a_0=4\sqrt3\pi\gamma l_P^2$. The formula holds for punctures by edges; nodes lying on the surface add further terms. The result is kinematical. The operator is defined before the Hamiltonian constraint is solved, and whether its spectrum survives in the full dynamics is debated.

The parameter $\gamma$ is the main ambiguity. Classically it labels a family of canonical variables, $A=\Gamma+\gamma K$, built from the spin connection $\Gamma$ and the extrinsic curvature $K$. Every value describes the same general relativity. After quantization the area spectrum scales with $\gamma$, and different values give inequivalent quantum theories. The classical theory does not fix it.

The usual way to fix $\gamma$ is to count horizon states. A black-hole horizon of area $A$ is punctured by many edges. Counting the spin configurations compatible with that area gives an entropy proportional to $A/\gamma$. Requiring the Bekenstein--Hawking value $S=k_BA/4l_P^2$ yields an equation for $\gamma$. In the counting of Domagala and Lewandowski, and of Meissner, it reads

```math
1=\sum_{j=1/2,\,1,\,3/2,\ldots}2\,e^{-2\pi\gamma\sqrt{j(j+1)}}
\qquad\Rightarrow\qquad \gamma=0.2375\ldots,\qquad a_0\approx5.2\,l_P^2.
```

With this value the smallest area is about $1.4\times10^{-69}$ m$^2$. An earlier count kept only spin-$1/2$ punctures and gave $\gamma=\ln2/(\pi\sqrt3)\approx0.127$. Other counting rules give other values, and the logarithmic correction to the entropy also depends on the rule. The procedure therefore matches one parameter; it does not predict the entropy. No experiment has resolved areas at this scale. Within the theory, the discreteness of area and volume for spin-network states is established, as described under spin network. The dynamics is formulated through spin foams and remains open.

## References For The Physical Derivation

- [A. Ashtekar and J. Lewandowski, Background Independent Quantum Gravity: A Status Report; connection variables, the Barbero-Immirzi parameter and the area operator.](https://arxiv.org/abs/gr-qc/0404018)
- [C. Rovelli and L. Smolin, Discreteness of area and volume in quantum gravity; discrete spectra of geometric operators on spin-network states.](https://arxiv.org/abs/gr-qc/9411005)
- [M. Domagala and J. Lewandowski, Black hole entropy from Quantum Geometry; corrected horizon state counting and the resulting value of the Barbero-Immirzi parameter.](https://arxiv.org/abs/gr-qc/0407051)
