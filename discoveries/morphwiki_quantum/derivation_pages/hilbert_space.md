# Hilbert space

A particle between two hard walls a distance $L$ apart is prepared with the same amplitude at every point of the box. A measurement of its energy then returns the lowest level in a definite fraction of runs. Computing that fraction uses the two properties that define a Hilbert space: an inner product and completeness.

The states of the particle are square-integrable functions on the interval. The inner product of two of them gives an amplitude, and its squared modulus gives the probability of finding one prepared state in another. The energy eigenfunctions $\phi_n(x)=\sqrt{2/L}\,\sin(n\pi x/L)$ are orthonormal, and every state is a convergent sum of them:

```math
\langle\phi|\psi\rangle=\int_0^L\phi^*(x)\psi(x)\,dx,\qquad
\psi=\sum_{n\geq1}c_n\phi_n,\\
c_n=\langle\phi_n|\psi\rangle,\qquad
\sum_{n\geq1}|c_n|^2=\langle\psi|\psi\rangle=1.
```

For the flat state $\psi=1/\sqrt L$ the coefficients are $c_n=\sqrt2\,[1-(-1)^n]/(n\pi)$. The even terms vanish because the flat state is symmetric about the centre of the box, while the even eigenfunctions are antisymmetric. The odd terms give

```math
P(E_1)=|c_1|^2=\frac{8}{\pi^2}\approx0.811,\qquad
P(E_n)=\frac{8}{n^2\pi^2}\quad(n\ \text{odd}).
```

The probabilities add up to one because the sum of $1/n^2$ over odd $n$ equals $\pi^2/8$. This is Parseval's identity. It holds because the space is complete: a sequence of finite superpositions whose members approach each other in mean square converges to a state inside the space. The probability missing after the terms up to $n=N$ falls roughly as $4/(\pi^2N)$ for large $N$. The partial sums vanish at the walls themselves and overshoot the flat value by 18 percent next to them, however many terms are kept. Convergence in the norm is nevertheless the physically relevant sense, because the norm controls every probability.

The same state has infinite mean energy. With $E_n=n^2\pi^2\hbar^2/(2mL^2)$, every odd term of the energy sum contributes the same amount:

```math
\langle H\rangle=\sum_{n\ \text{odd}}\frac{8}{n^2\pi^2}\,
\frac{n^2\pi^2\hbar^2}{2mL^2}
=\sum_{n\ \text{odd}}\frac{4\hbar^2}{mL^2}=\infty.
```

The flat wave function belongs to the Hilbert space, but not to the domain of the Hamiltonian. It jumps at the walls, where every eigenfunction vanishes, and an abrupt step needs arbitrarily large momentum components. The divergence comes from the step itself, so walls of finite height do not remove it. A preparation with finite energy must round the edges over some length, and that length cuts off the sum.

The Hilbert space is not physical space. For one particle in three dimensions it is a space of wave functions of three coordinates; for $N$ particles the functions depend on $3N$ coordinates. A single spin needs only the two-dimensional space $\mathbb C^2$, and $N$ spins need dimension $2^N$. A finite set of box modes suffices for questions about low energies, but not for the mean energy of a state with sharp edges. The distinction between the space and an operator's domain recurs in spectral theory and in the treatment of self-adjoint operators.

## References For The Physical Derivation

- [V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; Hilbert spaces, operator domains and spectral decompositions.](https://arxiv.org/abs/1508.06951)
