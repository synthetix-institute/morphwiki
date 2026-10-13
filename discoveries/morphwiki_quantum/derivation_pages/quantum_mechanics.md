# Quantum mechanics

A beam of silver atoms passing an inhomogeneous magnet splits into two spots instead of a continuous smear. Stern and Gerlach observed this in 1922. Sequences of such magnets display most of the structure of quantum mechanics in one experiment.

The magnetic moment of a silver atom comes from one unpaired electron spin. Its spin state is a unit vector $|\psi\rangle=\alpha|\uparrow\rangle+\beta|\downarrow\rangle$ in a two-dimensional complex space. A magnet with its field gradient along $z$ sends the atom up or down with probabilities $|\alpha|^2$ and $|\beta|^2$. Blocking the lower beam prepares $|\uparrow\rangle$: every atom of the upper beam goes up again in a second $z$ magnet.

A magnet tilted by an angle $\theta$ from $z$ in the $xz$ plane has its own pair of output states. The probability of each output is the squared modulus of an overlap, the Born rule:

```math
|{+}\mathbf n\rangle=\cos\tfrac\theta2|\uparrow\rangle+\sin\tfrac\theta2|\downarrow\rangle,\qquad
p({+}\mathbf n\,|\uparrow)=|\langle{+}\mathbf n|\uparrow\rangle|^2=\cos^2\tfrac\theta2.
```

At $\theta=60^\circ$ three quarters of the atoms take the upper path; at $90^\circ$ half do. Single atoms arrive at random, and only the relative counts approach these values.

Now place a third magnet along $z$ after the tilted one. Suppose the path through the tilted magnet is recorded. The probabilities of the two paths then add, and atoms that entered as $|\uparrow\rangle$ leave as $|\downarrow\rangle$ with probability $\tfrac12\sin^2\theta$. If the two paths are recombined without any record, the amplitudes add instead. Completeness of the two output states then gives zero:

```math
p_{\rm recorded}(\downarrow)=\sum_\pm|\langle\downarrow|{\pm}\mathbf n\rangle|^2|\langle{\pm}\mathbf n|\uparrow\rangle|^2
=\tfrac12\sin^2\theta,\\
p_{\rm recombined}(\downarrow)=\Bigl|\sum_\pm\langle\downarrow|{\pm}\mathbf n\rangle\langle{\pm}\mathbf n|\uparrow\rangle\Bigr|^2=0.
```

The difference between the two lines is set by whether any physical system keeps information about the path. Coherent recombination is demanding, because the two paths must overlap again in position and momentum. A full-loop Stern--Gerlach interferometer driven by the precise field of an atom chip has achieved it.

The spin components $S_z$ and $S_x$ are represented by noncommuting operators, $[S_z,S_x]=i\hbar S_y$. No preparation gives definite values to both. After the $x$ magnet selects its upper beam, a $z$ magnet again splits the atoms evenly. The commutator and the uncertainty principle treat this incompatibility quantitatively.

Between magnets the state evolves by the Schrödinger equation. In a uniform field $B$ along $z$, take $H=\omega S_z$ with $\omega$ proportional to $B$. A spin prepared along $x$ precesses about $z$, and the probability of finding it along $x$ oscillates:

```math
i\hbar\frac{d}{dt}|\psi\rangle=H|\psi\rangle,\qquad
p_{+x}(t)=\cos^2\frac{\omega t}{2}.
```

For an electron spin, $\omega/2\pi$ equals 28.0 gigahertz for each tesla of field. The same rules extend to any system. States are unit vectors or density operators, and outcomes are eigenvalues of self-adjoint operators. Probabilities are squared overlaps, evolution between measurements is unitary, and composite systems use tensor products. The two spots appear only when the gradient separates the paths by more than the beam width. With weaker gradients the spots overlap, and the magnet performs an unsharp measurement of the kind discussed under observables.

## References For The Physical Derivation

- [Y. Margalit and colleagues, Realization of a complete Stern-Gerlach interferometer; coherent recombination of the two spin paths with an atom-chip field.](https://arxiv.org/abs/1801.02708)
