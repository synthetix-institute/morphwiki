# Macroscopic quantum phenomena

A superconducting ring cooled through its transition in a weak magnetic field traps the flux threading it. The trapped flux takes only discrete values, separated by about $2\times10^{-15}$ Wb, a step fixed by Planck's constant and the electron charge. The ring can be millimetres across, yet its flux, a macroscopic electrical variable, is quantized.

Below the transition temperature, electrons bound in Cooper pairs share one wave function $\psi=\sqrt{n_s}\,e^{i\theta}$, where $n_s$ is the pair density and $\theta$ a phase common to all pairs. A pair has charge $q=-2e$ and mass $m^*=2m_e$. Its current density in a vector potential $\mathbf A$ depends on the phase gradient. Deep inside a ring thicker than the magnetic penetration depth the current vanishes. Integrating around such a path, and requiring $\psi$ to be single-valued, gives

```math
\mathbf j_s=\frac{qn_s}{m^*}\left(\hbar\nabla\theta-q\mathbf A\right)=0
\;\Rightarrow\;2\pi\hbar n=q\oint\mathbf A\cdot d\mathbf l,\\
\Phi=n\,\frac{h}{2e}=n\Phi_0,\qquad \Phi_0=2.07\times10^{-15}\ \mathrm{Wb}.
```

Here $n$ is an integer and the sign of the charge is absorbed into it. Deaver and Fairbank, and independently Doll and Näbauer, measured this quantization in 1961 in small superconducting cylinders. The step $h/2e$, not $h/e$, showed that the condensate carries charge in pairs.

Two superconductors joined through a thin insulating barrier have a phase difference $\varphi$ across it. Pairs tunnel through the barrier, and the Josephson relations connect the current $I$ and the voltage $V$ to that phase:

```math
I=I_c\sin\varphi,\qquad \frac{d\varphi}{dt}=\frac{2eV}{\hbar}.
```

A constant voltage makes the current oscillate at $2eV/h$, which is 483.6 GHz per millivolt. Microwaves of frequency $f$ produce current steps at the voltages $nhf/2e$. Voltage standards use arrays of such junctions, because the step voltages depend only on $f$ and fundamental constants.

The phase difference is itself a dynamical variable. For a junction of capacitance $C$ biased by a current $I$, it moves like a particle of mass $C(\hbar/2e)^2$ in a tilted washboard potential:

```math
U(\varphi)=-E_J\cos\varphi-\frac{\hbar I}{2e}\varphi,\qquad E_J=\frac{\hbar I_c}{2e},\\
\omega_p=\sqrt{\frac{2eI_c}{\hbar C}}\left(1-\frac{I^2}{I_c^2}\right)^{1/4}.
```

Here $\omega_p$ is the frequency of small oscillations in a well. Near $I_c$ each well becomes shallow, and escape from it switches the junction to a finite voltage. At high temperature escape is thermally activated. Below a crossover temperature near $\hbar\omega_p/2\pi k_B$, about 76 mK for $\omega_p/2\pi=10$ GHz, the escape rate stops depending on temperature because the phase tunnels through the barrier. Dissipation reduces the tunnelling rate, as Caldeira and Leggett showed, so the junction must be weakly damped.

Devoret, Martinis and Clarke observed this macroscopic tunnelling in 1985, and microwave spectroscopy resolved quantized energy levels of the phase in the well. This work, recognized by the 2025 Nobel Prize in Physics, underlies superconducting qubits. These effects are established, and their macroscopic character lies in one collective coordinate of very many pairs. Superpositions of macroscopically distinct states, such as opposite currents circulating in a ring, raise a further question. Several measures of macroscopicity have been proposed, and they rank such experiments differently, which leaves the comparison with Schrödinger's cat open.

## References For The Physical Derivation

- [M. H. Devoret, A. Wallraff and J. M. Martinis, Superconducting Qubits: A Short Review; Josephson junction dynamics, macroscopic tunnelling and quantized levels.](https://arxiv.org/abs/cond-mat/0411174)
- [F. Fröwis and colleagues, Macroscopic Quantum States: Measures, Fragility and Implementations; competing measures of macroscopicity.](https://arxiv.org/abs/1706.06173)
