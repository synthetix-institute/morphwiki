# Hamiltonian (quantum mechanics)

Ammonia absorbs microwaves near 24 GHz, and its line at 23.87 GHz was used in the ammonia maser of 1954. The same frequency describes a motion: a nitrogen atom placed on one side of the plane of the three hydrogens tunnels to the other side and back. One operator, the Hamiltonian $H$, fixes both the energy outcomes and this time evolution.

For a closed system with time-independent $H$, the energy eigenstates $|E_n\rangle$ form a basis, and evolution multiplies each component by its own phase. Write the prepared state as $|\psi\rangle=\sum_nc_n|E_n\rangle$. For any observable $O$ with matrix elements $O_{mn}=\langle E_m|O|E_n\rangle$,

```math
H|E_n\rangle=E_n|E_n\rangle,\qquad
U(t)=e^{-iHt/\hbar}=\sum_ne^{-iE_nt/\hbar}|E_n\rangle\langle E_n|,\\
\langle O\rangle(t)=\sum_{m,n}c_m^*c_n\,O_{mn}\,e^{i(E_m-E_n)t/\hbar}.
```

Only energy differences enter, so a constant added to $H$ changes no prediction. The weights $|c_n|^2$ never change, which is energy conservation. Every observable oscillates at the Bohr frequencies $(E_m-E_n)/\hbar$, the same frequencies a spectrometer records as absorption or emission lines. An eigenstate acquires only an overall phase, so all its expectation values are constant. Motion requires a superposition of different energies.

In ammonia the umbrella-inversion coordinate has two equivalent minima. Let $|L\rangle$ and $|R\rangle$ be states localized in each well with equal energy $E_0$, and let $A>0$ be the tunnelling amplitude through the barrier between them. Within this pair of states,

```math
H=\begin{pmatrix}E_0&-A\\-A&E_0\end{pmatrix},\qquad E_\pm=E_0\pm A,\qquad
P_L(t)=\cos^2\frac{\Delta E\,t}{2\hbar},\qquad \Delta E=2A.
```

The symmetric combination of $|L\rangle$ and $|R\rangle$ is the lower level, and the antisymmetric combination lies higher by $\Delta E$. A molecule prepared in $|L\rangle$ is an equal superposition of the two. Its probability $P_L$ of remaining on the left therefore oscillates at the line frequency $\Delta E/h$. A line at 23.87 GHz gives $\Delta E=9.9\times10^{-5}$ eV, or $0.80\,\mathrm{cm}^{-1}$, and a crossing time $\pi\hbar/\Delta E\approx21$ ps.

The maser used the same two levels. An inhomogeneous electric field shifts them in opposite directions, so it separates molecules in the upper level from those in the lower level. Molecules in the upper level were focused into a microwave cavity, where they emitted at $\Delta E/h$.

The two-level description holds because the next vibrational level of the umbrella motion lies near $950\,\mathrm{cm}^{-1}$, far above the splitting. Rotation changes the splitting slightly, which spreads the inversion lines over a band near 24 GHz. More generally, $H$ must be self-adjoint for $U(t)$ to be unitary, and bounded below for a ground state to exist. For a particle in a potential, $H=P^2/2m+V(X)$ follows from the classical energy, as described under Hamiltonian mechanics. When $H$ depends on time, energy is not conserved and $U$ becomes a time-ordered product, treated under the Schrödinger picture.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; self-adjoint Hamiltonians, spectral decomposition and the unitary evolution they generate.](https://arxiv.org/abs/1508.06951)
