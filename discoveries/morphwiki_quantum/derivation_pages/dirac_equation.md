# Dirac equation

The $n=2$ level of hydrogen is not a single level. Microwave and optical spectroscopy resolve components about 11 GHz apart, a fraction of about $10^{-5}$ of the binding energy of that level. Dirac's relativistic equation for the electron accounts for this fine structure and shows that the electron carries spin one half.

A relativistic wave equation must reproduce $E^2=p^2c^2+m^2c^4$. The Klein--Gordon equation does so with a second time derivative, and its conserved density can be negative. Dirac required instead an equation linear in $\partial_t$, $i\hbar\partial_t\psi=H\psi$, with a Hamiltonian linear in the momentum $\mathbf p$:

```math
H=c\,\boldsymbol\alpha\cdot\mathbf p+\beta mc^2,\\
\alpha_i\alpha_j+\alpha_j\alpha_i=2\delta_{ij},\qquad
\alpha_i\beta+\beta\alpha_i=0,\qquad \beta^2=1.
```

Squaring gives $H^2=c^2p^2+m^2c^4$ exactly when these anticommutation relations hold. The smallest matrices that satisfy them are $4\times4$, so $\psi$ has four components. The density $\psi^\dagger\psi$ is positive and obeys a continuity equation. The free spectrum still contains negative energies $-\sqrt{p^2c^2+m^2c^4}$; in Quantum field theory these solutions describe positrons.

Rotational symmetry then requires spin. The orbital angular momentum $\mathbf L=\mathbf r\times\mathbf p$ does not commute with $H$; instead $[H,\mathbf L]=-i\hbar c\,\boldsymbol\alpha\times\mathbf p$. Let $\boldsymbol\Sigma$ be the $4\times4$ matrix made of two copies of the Pauli matrices. It satisfies $[H,\hbar\boldsymbol\Sigma/2]=i\hbar c\,\boldsymbol\alpha\times\mathbf p$, so the conserved angular momentum is

```math
\mathbf J=\mathbf L+\frac{\hbar}{2}\boldsymbol\Sigma,\qquad [H,\mathbf J]=0,\qquad
\left(\frac{\hbar}{2}\boldsymbol\Sigma\right)^2=\frac34\hbar^2.
```

The internal part has the eigenvalue $s(s+1)\hbar^2$ with $s=1/2$. Spin one half is therefore a consequence of the linear relativistic equation, not an additional postulate. Coupling to a magnetic field in the same equation gives the magnetic moment with $g=2$, as described under Electron.

For an electron bound to a point nucleus of charge $Ze$, the Dirac equation with the Coulomb potential can be solved exactly. With $\alpha$ the fine-structure constant, the energy depends on the principal quantum number $n$ and on the total angular momentum $j$, but not separately on the orbital quantum number $l$:

```math
E_{nj}=mc^2\left[1+\left(\frac{Z\alpha}{n-j-\frac12+\sqrt{(j+\frac12)^2-Z^2\alpha^2}}\right)^2\right]^{-1/2}\\
\approx mc^2-\frac{mc^2(Z\alpha)^2}{2n^2}
-\frac{mc^2(Z\alpha)^4}{2n^4}\left(\frac{n}{j+\frac12}-\frac34\right).
```

The second term is the Bohr energy. The third is smaller by a factor of order $(Z\alpha)^2\approx5\times10^{-5}$ for hydrogen and gives the fine structure. In a nonrelativistic expansion it combines three effects: the relativistic correction to the kinetic energy, spin-orbit coupling with $g=2$, and the Darwin term for S states. For $n=2$ the levels with $j=1/2$ lie below those with $j=3/2$ by $mc^2\alpha^4/32$. With the reduced-mass correction this is 10.943 GHz, compared with the measured $2P_{3/2}$--$2P_{1/2}$ interval of 10.969 GHz.

The remaining 0.2 percent comes mainly from the anomalous magnetic moment of the electron, which multiplies the spin-orbit term by $1+2a_e$. The formula also predicts that $2S_{1/2}$ and $2P_{1/2}$, which share $n=2$ and $j=1/2$, coincide. Their measured separation of 1057.8 MHz, the Lamb shift, is calculated in Quantum electrodynamics. For a point nucleus the solution with $j=1/2$ fails when $Z\alpha>1$. With a finite nucleus the lowest level reaches the negative-energy continuum near $Z\approx170$, where a single-particle equation no longer applies.

## References For The Physical Derivation

- [M. I. Eides, H. Grotch and V. A. Shelyuto, Theory of Light Hydrogenlike Atoms; Dirac energy levels of hydrogen and their radiative and recoil corrections.](https://arxiv.org/abs/hep-ph/0002158)
