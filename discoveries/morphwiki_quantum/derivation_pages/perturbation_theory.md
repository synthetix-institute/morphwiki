# Perturbation theory

An electric field of 100 kV/cm splits the $n=2$ level of hydrogen into components hundreds of gigahertz apart, while the ground level moves by only a few megahertz. Both shifts come from the same weak addition to the atomic Hamiltonian. Perturbation theory explains why one shift is linear in the field and the other quadratic.

Write $H=H_0+\lambda V$, where the eigenstates $|n\rangle$ and energies $E_n^{(0)}$ of $H_0$ are known and $\lambda$ counts powers of the perturbation. Expand the exact eigenvalue and eigenvector in powers of $\lambda$ and insert them into $H|\psi_n\rangle=E_n|\psi_n\rangle$. Projecting the equation at each order onto $\langle n|$ and onto $\langle m|$ with $m\neq n$ gives the energy and the admixed states:

```math
E_n=E_n^{(0)}+\lambda V_{nn}
+\lambda^2\sum_{m\neq n}\frac{|V_{mn}|^2}{E_n^{(0)}-E_m^{(0)}}+O(\lambda^3),\\
|\psi_n\rangle=|n\rangle+\lambda\sum_{m\neq n}\frac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}|m\rangle+O(\lambda^2),
\qquad V_{mn}=\langle m|V|n\rangle.
```

The expansion is useful when every coupling is small compared with the corresponding gap, $|V_{mn}|\ll|E_n^{(0)}-E_m^{(0)}|$. For the ground state every denominator is negative, so the second-order shift always lowers the energy. The sum runs over the complete set of unperturbed states, including any continuum.

For an electron in a uniform field $F$ along $z$, the perturbation is $V=eFz$. The hydrogen ground state has even parity and $z$ is odd, so $V_{nn}=0$. The leading shift is quadratic, $\Delta E=-\alpha_{\mathrm{pol}}F^2/2$, with static polarizability $\alpha_{\mathrm{pol}}=\tfrac92(4\pi\varepsilon_0)a_0^3$. At 100 kV/cm this gives 5.6 MHz. The bound states supply only 81 percent of the polarizability; the ionization continuum supplies the rest.

The $n=2$ level behaves differently because the $2s$ and $2p$ states have the same unperturbed energy. The denominators vanish, and the expansion must start by diagonalizing $V$ within the degenerate subspace. Only $2s$ and $2p_0$ are coupled, and

```math
\langle2s|z|2p_0\rangle=-3a_0,\qquad E=E_2\pm3ea_0F,\qquad
|\pm\rangle=\frac{|2s\rangle\mp|2p_0\rangle}{\sqrt2}.
```

The mixed states carry permanent electric dipoles of $\mp3ea_0$, so their shift is linear in $F$. At 100 kV/cm the outer components lie $\pm384$ GHz from the unperturbed level, while $2p_{\pm1}$ remains unshifted. Stark observed this linear splitting of the Balmer lines in 1913.

The degenerate treatment assumes that the Stark coupling exceeds the small splittings omitted from the nonrelativistic $H_0$. The fine-structure splitting of $n=2$ is 10.9 GHz, and the Lamb shift between $2s_{1/2}$ and $2p_{1/2}$ is 1.06 GHz. Below a few hundred volts per centimetre the coupling is smaller than the Lamb shift, and the shift of $2s_{1/2}$ becomes quadratic again. In any static field the electron can also tunnel out of the atom, at a rate that vanishes faster than any power of $F$. The levels are therefore resonances, and the series in $F$ is asymptotic rather than convergent. A perturbation that oscillates in time produces transitions instead of shifts. The same expansion then gives Fermi's golden rule for transition rates, used for spectral lines and scattering.

## References For The Physical Derivation

- [U. D. Jentschura, Resummation of the Divergent Perturbation Series for a Hydrogen Atom in an Electric Field; the Stark perturbation series and its divergence.](https://arxiv.org/abs/physics/0010038)
