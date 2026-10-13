# Transformation theory (quantum mechanics)

Cold atoms released into a harmonic trap form, after a quarter of an oscillation period, an image of their initial momentum distribution. The explanation is a calculation of the kind introduced by Dirac and Jordan in 1927. Their transformation theory treats every prediction as a product of amplitudes between eigenstates of different observables.

The amplitude $\langle a|b\rangle$ is the transformation function between eigenstates of two observables. Its squared modulus is the probability of finding $a$ after preparing $b$. Amplitudes compose by summing over a complete set of intermediate eigenstates. Wave mechanics and matrix mechanics then differ only in which basis the same amplitudes are written:

```math
\langle a|c\rangle=\int db\,\langle a|b\rangle\langle b|c\rangle,\qquad
\psi(q)=\langle q|\psi\rangle,\qquad \widetilde\psi(p)=\langle p|\psi\rangle.
```

The central transformation function connects position and momentum. Because $[Q,P]=i\hbar$, momentum generates translations, and in the position basis it acts as $-i\hbar\,\partial_q$. Applied to a momentum eigenstate this gives a first-order differential equation. Normalization to $\langle p|p'\rangle=\delta(p-p')$ fixes the constant:

```math
-i\hbar\,\partial_q\langle q|p\rangle=p\,\langle q|p\rangle
\quad\Longrightarrow\quad
\langle q|p\rangle=\frac{e^{ipq/\hbar}}{\sqrt{2\pi\hbar}}.
```

The modulus is the same for every $q$ and $p$. A state of sharp momentum therefore has a uniform position distribution, and the converse also holds. The spin version is $|\langle{\pm}x|{\pm}z\rangle|^2=\tfrac12$: complete knowledge of $S_z$ leaves the outcomes of $S_x$ equally likely.

Time evolution is also a transformation, from positions at one time to positions at another. For a particle of mass $m$ in a harmonic trap of angular frequency $\omega$, the energy eigenfunctions are Hermite functions $h_n$, each acquiring the phase $e^{-i(n+1/2)\omega t}$. At the quarter period $t=\pi/(2\omega)$ this phase equals $e^{-i\pi/4}(-i)^n$. The Hermite functions are also eigenfunctions of the Fourier transform with eigenvalues $(-i)^n$. The quarter-period evolution is therefore the position-to-momentum transformation itself:

```math
\psi\!\left(x,\frac{\pi}{2\omega}\right)=e^{-i\pi/4}\sqrt{m\omega}\;\widetilde\psi(m\omega x),
\qquad |\psi|^2dx=|\widetilde\psi(p)|^2dp\ \ \text{at}\ p=m\omega x.
```

For rubidium-87 in a trap with a frequency of 10 hertz, the quarter period is 25 milliseconds. A momentum of $\hbar$ times one inverse micrometre maps to a displacement of 11.6 micrometres. Experiments with cold gases use this mapping to measure momentum distributions. The image is faithful when interactions are negligible during the quarter period and the trap is harmonic over the size of the cloud; anharmonicity blurs it.

The same composition rule underlies the Fourier transform between representations and the far-field imaging of a freely expanding cloud. Dirac also noted that the transformation function for a short time interval behaves like $\exp(iS/\hbar)$, with $S$ the classical action. Feynman developed that observation into the path integral. Von Neumann later recast the theory in Hilbert space without delta-normalized states; rigged Hilbert spaces restore them as generalized eigenvectors.

## References For The Physical Derivation

- [P. A. Murthy and colleagues, Matter wave Fourier optics with a strongly interacting two-dimensional Fermi gas; imaging momentum distributions by evolution in a harmonic potential.](https://arxiv.org/abs/1408.4680)
- [F. Gieres, Mathematical surprises and Dirac's formalism in quantum mechanics; equivalence of wave mechanics, matrix mechanics and Dirac's formalism, and the status of delta-normalized states.](https://arxiv.org/abs/quant-ph/9907069)
