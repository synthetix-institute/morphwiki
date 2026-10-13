# Mathematical formulation of quantum mechanics

A neutron spin rotated through a full turn points in its original direction again, but its state vector changes sign. In 1975 the groups of Rauch and of Werner observed this sign with neutron interferometers, in which one of two beams crossed a magnetic field. Predicting the measured intensity uses each rule of the standard formulation once.

The outcomes of a measurement correspond to mutually orthogonal projectors $P_a$ on a complex Hilbert space, with $\sum_aP_a=I$. Probabilities must add over orthogonal projectors, and the probability of $P_a$ must not depend on which other projectors complete the measurement. In dimension three or more, Gleason's theorem shows that every such assignment has the trace form, so the state is a density operator $\rho$:

```math
p(a)=\operatorname{Tr}(\rho P_a),\qquad \rho\geq0,\qquad \operatorname{Tr}\rho=1.
```

In dimension two, additional assumptions are needed for the same conclusion. Reversible evolution must preserve probabilities and compose in time. If it is continuous, Stone's theorem gives a self-adjoint generator $H$, and the Schrödinger equation follows:

```math
U(t+s)=U(t)U(s),\qquad U(t)=e^{-iHt/\hbar},\qquad
\rho(t)=U(t)\rho\,U(t)^\dagger.
```

A measurement that would repeat its result immediately changes the state to $P_a\rho P_a$ divided by its trace, the Lüders rule. If the outcome is not recorded, the state becomes the sum $\sum_aP_a\rho P_a$. Composite systems are described on tensor products of the component spaces.

In the interferometer a silicon crystal splits each neutron into two paths, $|1\rangle$ and $|2\rangle$, and later recombines them. The state space is the tensor product of this path space with the spin space $\mathbb C^2$. In path 2 a field $B$ along $z$ acts over a length $L$. For a neutron of speed $v$ and gyromagnetic ratio $\gamma_n$, the field Hamiltonian generates a spin rotation by the angle $\alpha=\gamma_nBL/v$:

```math
U(\alpha)=e^{-i\alpha\sigma_z/2},\qquad U(2\pi)=-I,\qquad U(4\pi)=I.
```

Let $\rho_s$ be the incoming spin state and $\chi$ the phase difference between the paths without field. The trace rule, with the projector onto one output beam, gives the fraction of neutrons leaving that beam. For an unpolarized beam, $\rho_s=I/2$:

```math
I(\alpha)=\frac12\Bigl[1+\operatorname{Re}\bigl(e^{i\chi}\operatorname{Tr}\rho_sU(\alpha)\bigr)\Bigr]
=\frac12\Bigl[1+\cos\chi\,\cos\frac{\alpha}{2}\Bigr].
```

The interference term reverses its sign at $\alpha=2\pi$ and returns only at $\alpha=4\pi$. A single beam cannot show the sign, because $-I$ multiplies every spin state by the same factor. The unrotated path supplies the reference. Thermal neutrons of wavelength 0.18 nanometres move at about 2200 metres per second. A full turn then needs $BL=2\pi v/\gamma_n\approx7.5\times10^{-5}$ tesla metre, for example 7.5 millitesla over one centimetre. Both 1975 experiments found the intensity periodic in the field with this 4$\pi$ period. A spread of neutron speeds spreads $\alpha$ in proportion to its size, which lowers the contrast after many turns.

A measurement of the spin in path 2 changes the prediction. Its outcomes correspond to the projectors $|2\rangle\langle2|\otimes P_\pm$, completed by $|1\rangle\langle1|\otimes I$ for neutrons in path 1. The Lüders rule removes every term of the density operator that connects the two paths, so the interference term vanishes. The intensity becomes one half for every field and every $\chi$. The record shows which path was taken, whether or not anyone reads it.

The formulation does not state which interactions count as measurements; decoherence and the measurement problem address that physical question. Within its rules, it gives the probability of any sequence of outcomes. The half-angle in $U(\alpha)$ comes from the spin-1/2 representation of rotations described under the Pauli matrices.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; Gleason's theorem, Stone's theorem and the Lüders rule.](https://arxiv.org/abs/1508.06951)
- [J. Klepp, S. Sponar and Y. Hasegawa, Fundamental phenomena of quantum mechanics explored with neutron interferometers; spinor rotation, spin-path states and measurements in neutron interferometry.](https://arxiv.org/abs/1407.2526)
