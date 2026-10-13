# Quantum chaos

Slow neutrons striking heavy nuclei excite many narrow resonances, and neighbouring resonances are rarely found close together. The levels of a particle in a rectangular box with incommensurate sides behave differently, because near coincidences are common there. The difference reflects the classical motion, which is regular in the box and chaotic or highly complex in the nucleus.

Consider two neighbouring levels that may be coupled. When the system is invariant under time reversal, the Hamiltonian can be chosen real and symmetric. The $2\times2$ block and its level spacing are

```math
H=\begin{pmatrix}h_{11}&h_{12}\\h_{12}&h_{22}\end{pmatrix},\qquad
s=E_+-E_-=\sqrt{(h_{11}-h_{22})^2+4h_{12}^2}.
```

A degeneracy requires two independent conditions, $h_{11}=h_{22}$ and $h_{12}=0$. If the matrix elements are spread smoothly, the probability of a spacing below $s$ scales as $s^2$, and the spacing density vanishes linearly. This is level repulsion, described by von Neumann and Wigner. Independent Gaussian matrix elements define the Gaussian orthogonal ensemble. Scaling the spacing to unit mean gives the Wigner surmise. Without time-reversal invariance $h_{12}$ is complex, three conditions are needed, and the density vanishes as $s^2$:

```math
P_{\mathrm{Poisson}}(s)=e^{-s},\qquad
P_{\mathrm{GOE}}(s)=\frac{\pi s}{2}\,e^{-\pi s^2/4},\\
P_{\mathrm{GUE}}(s)=\frac{32s^2}{\pi^2}\,e^{-4s^2/\pi}.
```

In an integrable system, levels carry independent quantum numbers, and levels with different labels do not repel. Their sequence is uncorrelated, which gives the Poisson law, as Berry and Tabor argued for generic integrable systems. The laws differ most at small spacing. The probability of a spacing below one tenth of the mean is 0.095 for Poisson statistics, 0.0078 for the Wigner surmise and 0.0011 for the unitary ensemble.

Bohigas, Giannoni and Schmit conjectured in 1984 that quantum systems with a chaotic classical limit follow these random-matrix laws. The conjecture is supported by stadium and Sinai billiards, by microwave cavities of the same shapes, by hydrogen in strong magnetic fields and by the nuclear data ensemble of neutron resonances. Semiclassical sums over periodic orbits explain the spectral correlations. A general proof remains open.

These statistics require care. Before any comparison the spectrum is unfolded, by rescaling energies with the smooth level density so that the mean spacing is one everywhere. Levels must also be sorted by exact symmetry. Independent sequences of different parity or angular momentum superpose without repulsion and look Poissonian. The random-matrix laws hold only over energy ranges smaller than $h$ divided by the period of the shortest periodic orbit. Eigenstates concentrated along unstable periodic orbits, called scars, show that eigenfunctions also deviate from random behaviour.

In the time domain, chaos limits how long a wave packet follows a single classical trajectory, a theme of quantum dynamics. The random-matrix character of chaotic eigenstates also underlies thermalization of isolated systems in quantum statistical mechanics.

## References For The Physical Derivation

- [T. Guhr, A. Mueller-Groeling and H. A. Weidenmueller, Random Matrix Theories in Quantum Physics: Common Concepts; level spacing statistics, the Wigner surmise, nuclear data and chaotic billiards.](https://arxiv.org/abs/cond-mat/9707301)
- [L. D'Alessio, Y. Kafri, A. Polkovnikov and M. Rigol, From Quantum Chaos and Eigenstate Thermalization to Statistical Mechanics and Thermodynamics; random-matrix statistics and thermalization of isolated systems.](https://arxiv.org/abs/1509.06411)
