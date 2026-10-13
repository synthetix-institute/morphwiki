# Observable

A spin-1 atom passing a Stern--Gerlach magnet leaves three spots, one for each value of $S_z$. An apparatus that recombines the two outer beams without recording which one each atom took asks a coarser question. Comparing the two apparatuses shows what an observable specifies.

An observable is a list of outcomes together with orthogonal projectors that sum to the identity. The operator collects them in its spectral decomposition, and the projectors give the probabilities:

```math
A=\sum_ia_iP_i,\qquad P_iP_j=\delta_{ij}P_i,\qquad \sum_iP_i=I,\qquad
p(a_i)=\operatorname{Tr}(\rho P_i).
```

The eigenvalues $a_i$ label detector outputs; the projectors carry the physics. The mean $\operatorname{Tr}(\rho A)$ and the moments $\operatorname{Tr}(\rho A^k)$ follow from the same probabilities. A function $f(A)=\sum_if(a_i)P_i$ relabels the outputs and merges those that receive the same label. After a recorded outcome with minimal disturbance, the state becomes $P_i\rho P_i$ divided by its trace.

For spin 1, $S_z=\hbar(P_{+1}-P_{-1})$, while merging the outer beams measures $S_z^2=\hbar^2(P_{+1}+P_{-1})$. Prepare $|\psi\rangle=(|{+}1\rangle+|{-}1\rangle)/\sqrt2$. A measurement of $S_z$ gives $\pm\hbar$ with probability one half each and leaves $|{+}1\rangle$ or $|{-}1\rangle$. A measurement of $S_z^2$ gives $\hbar^2$ with certainty and leaves $|\psi\rangle$ unchanged, including the relative phase of its components. A later experiment sensitive to that phase distinguishes the two apparatuses, even though one of them gave a certain result.

For spin 1 the three squared components commute with each other. They obey a sum rule:

```math
[S_x^2,S_y^2]=[S_y^2,S_z^2]=[S_z^2,S_x^2]=0,\qquad
S_x^2+S_y^2+S_z^2=2\hbar^2.
```

One apparatus can therefore measure all three. Each has eigenvalues $0$ and $\hbar^2$, and the sum rule forces exactly one zero in every run. The state $|\psi\rangle$ above gives $S_x^2=\hbar^2$, $S_y^2=0$ and $S_z^2=\hbar^2$ with certainty. By contrast, $S_x$ and $S_z$ do not commute, and no apparatus measures both sharply. Commuting triples of this kind underlie the Kochen--Specker theorem discussed under quantum logic.

A real detector can assign an outcome to the wrong beam. Suppose a spin-1/2 analyzer reports the wrong spot with probability $\varepsilon$, for instance because the spots overlap. The report up then corresponds to the positive operator $E_+=(1-\varepsilon)P_\uparrow+\varepsilon P_\downarrow$, and

```math
E_\pm=\frac{I\pm\eta\,\sigma_z}{2},\qquad \eta=1-2\varepsilon,\qquad
p_\pm=\frac{1\pm\eta\,r_z}{2},
```

where $r_z$ is the $z$ component of the Bloch vector. These operators are not projectors, and together they form a positive-operator-valued measure. The mean outcome still determines $r_z$ after division by $\eta$, but no single run gives certainty when $\varepsilon>0$. For continuous spectra the projectors are assigned to intervals of outcomes, as described in spectral theory. Two devices measure the same observable when they assign the same operators to their outcomes, whatever their construction.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; observables, projection-valued and positive-operator-valued measures.](https://arxiv.org/abs/1508.06951)
