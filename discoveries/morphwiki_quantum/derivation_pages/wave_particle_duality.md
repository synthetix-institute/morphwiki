# Wave–particle duality

Electrons sent one at a time through a two-path interferometer arrive at single points, yet their accumulated positions form fringes. A detector that records which path each electron took reduces the fringe contrast. Englert's inequality states exactly how much path information can coexist with how much contrast.

The wave behaviour follows from the de Broglie relation $\lambda=h/p$, which the diffraction of electrons by a nickel crystal confirmed, as described under the wave function.

Now let a beam splitter send the particle into path 1 or 2 with probabilities $w_1$ and $w_2$. An internal degree of freedom, the marker, is left in state $|m_1\rangle$ or $|m_2\rangle$. After recombination with relative phase $\phi$, the two output ports have probabilities $\frac12[1\pm2\sqrt{w_1w_2}\operatorname{Re}(e^{i\phi}\langle m_1|m_2\rangle)]$. The visibility and the a priori predictability of the path are

```math
V=2\sqrt{w_1w_2}\,|\langle m_1|m_2\rangle|,\qquad P=|w_1-w_2|.
```

Path information stored in the marker is quantified by the distinguishability $D$. A measurement on the marker identifies the path correctly with probability at most $(1+D)/2$. Helstrom's result for discriminating two states gives $D$ as a trace norm, which for pure markers can be evaluated in closed form:

```math
D=\big\|w_1|m_1\rangle\langle m_1|-w_2|m_2\rangle\langle m_2|\big\|_1
=\sqrt{1-4w_1w_2|\langle m_1|m_2\rangle|^2},\\
V^2+D^2=1\ \ \text{(pure markers)},\qquad V^2+D^2\leq1\ \ \text{(general)}.
```

If the marker is mixed, or part of it escapes to an environment that is not examined, the equality becomes an inequality. Without a marker, $D$ reduces to $P$ and the relation becomes $V^2+P^2\leq1$. For equal paths and a marker overlap of $\cos30^\circ$, the fringes keep 87 percent contrast while the path can be guessed correctly 75 percent of the time. Intermediate cases have partial fringes and partial path knowledge, related by this single inequality.

The bound refers to the information available in the marker, not to what an experimenter actually measures. A marker measurement in a basis unrelated to the paths extracts no path information. Fringes then reappear in subsets of the records, as in the quantum eraser experiment.

Dürr, Nonn and Rempe tested the mechanism in an atom interferometer in 1998. A microwave field stored the path in the internal hyperfine state of each atom, and the fringes vanished. The momentum transferred by the microwave photons was far too small to wash out the fringes by random kicks. The loss of contrast came from the correlation between path and marker, as the formula states.

The relation applies to any two-path interferometer whose marker can be modelled as a quantum state. With a thermal environment as the unread marker, the same overlap describes decoherence. The electron microscope uses the wave side of this relation, forming images from interference between scattered and unscattered electrons.

## References For The Physical Derivation

- [P. J. Coles, J. Kaniewski and S. Wehner, Equivalence of wave-particle duality to entropic uncertainty; visibility-distinguishability relations.](https://arxiv.org/abs/1403.4687)
- [H. Lin, Y.-K. Lu, V. Fedoseev, Y. K. Lee, J. Lyu and W. Ketterle, Fringe visibility and which-way information in Young's double slit experiments with light scattered from single atoms; motional states of trapped atoms as which-path markers.](https://arxiv.org/abs/2507.19801)
