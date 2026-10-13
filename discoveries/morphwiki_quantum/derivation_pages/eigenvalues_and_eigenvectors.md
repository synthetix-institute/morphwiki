# Eigenvalues and eigenvectors

Sodium vapour illuminated by light with two optical frequencies fluoresces brightly, except where the difference of the two frequencies matches the splitting of two ground levels. There the fluorescence drops sharply. Alzetta and coworkers observed such dark lines in 1976. They are explained by an eigenvector of the atom-light Hamiltonian that has no excited-state component.

An eigenvector of the Hamiltonian, $H|n\rangle=E_n|n\rangle$, changes in time only by a phase, so all of its probabilities stay constant. A general state is a sum of eigenvectors, each with its own phase. Expectation values therefore oscillate at the Bohr frequencies $(E_n-E_m)/\hbar$:

```math
|\psi(t)\rangle=\sum_nc_ne^{-iE_nt/\hbar}|n\rangle,\qquad
\langle A\rangle(t)=\sum_{m,n}c_m^*c_nA_{mn}\,e^{-i(E_n-E_m)t/\hbar}.
```

Spectral lines appear at differences of eigenvalues for this reason. For a Hermitian $H$, evaluate $\langle m|H|n\rangle$ by acting to the right and to the left. The two results give $(E_n-E_m^*)\langle m|n\rangle=0$. Setting $m=n$ shows that eigenvalues are real, and distinct eigenvalues have orthogonal eigenvectors. In finite dimensions the eigenvalues are the roots of $\det(H-EI)=0$.

In the dark-resonance experiment, two ground levels $|1\rangle$ and $|2\rangle$ couple to one excited level $|e\rangle$. Two light fields drive the transitions with Rabi frequencies $\Omega_p$ and $\Omega_c$. In a frame rotating with the fields, within the rotating-wave approximation and with both fields on resonance, the Hamiltonian in the basis $(|1\rangle,|2\rangle,|e\rangle)$ is

```math
H=\frac\hbar2\begin{pmatrix}0&0&\Omega_p\\0&0&\Omega_c\\ \Omega_p&\Omega_c&0\end{pmatrix},\qquad
\det(H-EI)=-E\left(E^2-\frac{\hbar^2\Omega^2}{4}\right),
```

with $\Omega^2=\Omega_p^2+\Omega_c^2$. The eigenvalues are $0$ and $\pm\hbar\Omega/2$. The eigenvector with eigenvalue zero is

```math
|D\rangle=\frac{\Omega_c|1\rangle-\Omega_p|2\rangle}{\Omega}.
```

Its excited-state amplitude vanishes because the two excitation paths interfere destructively. An atom in $|D\rangle$ neither absorbs nor fluoresces. Spontaneous decay from $|e\rangle$ returns atoms to the ground levels at random, and atoms accumulate in $|D\rangle$. This is coherent population trapping. The state remains an exact eigenvector for any common detuning of the two fields, as long as their frequency difference matches the ground splitting. A mismatch $\delta$ couples $|D\rangle$ to the other states in proportion to $\delta$, and fluorescence returns.

The width of the dark resonance is set by the decay of the coherence between the ground levels and by power broadening. It can be far narrower than the optical linewidth. Compact atomic clocks use this resonance to lock a laser frequency difference to the cesium ground-state splitting of 9.192631770 gigahertz.

Eigenvalues alone would not explain the effect: the spectrum $0,\pm\hbar\Omega/2$ says nothing about fluorescence. The prediction depends on the composition of the eigenvector. When eigenvalues are degenerate, the eigenvectors are not unique, and a perturbation selects the physically relevant combinations, as in perturbation theory. The two-state quantum system gives the simplest case of the same calculation.

## References For The Physical Derivation

- [N. Belcher, E. E. Mikhailov and I. Novikova, Atomic Clocks and Coherent Population Trapping: Experiments for Undergraduate Laboratories; dark states and the measurement of a ground-state splitting.](https://arxiv.org/abs/0810.2071)
