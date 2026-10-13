# Introduction to quantum mechanics

*Historical, bibliographic or interpretive entry.*

A hydrogen lamp viewed through a grating shows sharp lines at fixed wavelengths, the brightest red one at $656$ nm. Classical mechanics allows an electron orbit of any energy and so predicts a continuous spectrum. Quantum mechanics accounts for the lines with three facts that recur throughout the subject: quantized energies, superposition of states, and the Born rule for probabilities.

Quantization. A bound system has a discrete set of energies, the eigenvalues of its Hamiltonian $H$. For the electron in hydrogen, with reduced mass $\mu$, elementary charge $e$ and principal quantum number $n$, the bound energies and the emitted photon frequency $\nu$ are

```math
E_n=-\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\,\frac{1}{n^2}
\approx-\frac{13.6\ \mathrm{eV}}{n^2},\qquad h\nu=E_m-E_n .
```

A photon carries away the energy difference between two levels. The transition from $n=3$ to $n=2$ gives $13.6\times(1/4-1/9)=1.89$ eV, a wavelength of $656$ nm, the observed red Balmer line. Transitions ending on $n=1$ lie in the ultraviolet, beginning at $121.6$ nm. Fine structure, the Lamb shift and hyperfine splitting appear only when relativity, the quantized radiation field and the nuclear spin are added.

Superposition. If $\ket{\psi_1}$ and $\ket{\psi_2}$ are possible states, so is $\alpha\ket{\psi_1}+\beta\ket{\psi_2}$ for complex numbers $\alpha$ and $\beta$. Superposition is not a statement of ignorance: the relative phase of $\alpha$ and $\beta$ changes the outcome of later interference experiments.

Born rule. A measurement whose outcomes correspond to orthonormal states $\ket{a}$ gives outcome $a$ with probability $|\langle a|\psi\rangle|^2$. For a spin-1/2 particle prepared along $z$ and sent through a Stern--Gerlach magnet tilted by the angle $\theta$,

```math
P(\uparrow_\theta)=|\langle\uparrow_\theta|\uparrow_z\rangle|^2=\cos^2\frac{\theta}{2},
\qquad P(\downarrow_\theta)=\sin^2\frac{\theta}{2}.
```

At $\theta=90^\circ$ the two outcomes are equally likely, and each atom still lands in one of only two spots. Repeated runs reproduce the frequencies, not the individual outcomes. Between preparation and measurement the state changes deterministically by the Schrödinger equation $i\hbar\,\partial_t\ket{\psi}=H\ket{\psi}$. Uncertainty relations and tunnelling follow from these rules, and the tensor-product rule for composite systems adds entanglement. The treatments Schrödinger equation, Quantum superposition, Born rule, Spin (physics) and Spectral line develop each step.
