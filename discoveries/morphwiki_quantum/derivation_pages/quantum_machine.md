# Quantum machine

A single spin in a magnetic field can run a heat engine. Its two levels are separated by $\hbar\omega$, and the field sets $\omega$. Contact with a hot bath fixes one level population, contact with a cold bath another. Changing the field between the contacts exchanges energy with the field. The efficiency of this quantum Otto cycle follows from the populations alone.

Let $H(\omega)=\hbar\omega\sigma_z/2$ and let $p$ be the probability of the upper level, so the mean energy is $\hbar\omega(p-1/2)$. A change of $p$ at fixed $\omega$ is heat, and a change of $\omega$ at fixed $p$ is work. Thermal contact at temperature $T$ gives the two-level occupation of quantum statistical mechanics:

```math
p(\omega,T)=\frac{1}{e^{\hbar\omega/k_BT}+1}.
```

The cycle has four strokes. Contact with the hot bath at splitting $\omega_h$ raises the population from $p_c$ to $p_h=p(\omega_h,T_h)$. The spin is then isolated and the field lowered to $\omega_c$. Contact with the cold bath returns the population to $p_c=p(\omega_c,T_c)$. Finally the isolated spin is returned to $\omega_h$. Adding the energy changes of the four strokes gives

```math
Q_h=\hbar\omega_h(p_h-p_c),\qquad W=\hbar(\omega_h-\omega_c)(p_h-p_c),\\
\eta=\frac{W}{Q_h}=1-\frac{\omega_c}{\omega_h}.
```

The engine delivers work only if $p_h>p_c$, which means $\hbar\omega_h/k_BT_h<\hbar\omega_c/k_BT_c$. This is the condition $\omega_c/\omega_h>T_c/T_h$, so the efficiency stays below the Carnot value $1-T_c/T_h$. It reaches that value only where $p_h=p_c$ and the work per cycle vanishes. Run backwards with $\omega_c/\omega_h<T_c/T_h$, the cycle pumps heat out of the cold bath. Its coefficient of performance $\omega_c/(\omega_h-\omega_c)$ again stays below the Carnot bound $T_c/(T_h-T_c)$.

```math
\eta=1-\frac{\omega_c}{\omega_h}<1-\frac{T_c}{T_h},\qquad
\frac{\omega_c}{\omega_h-\omega_c}<\frac{T_c}{T_h-T_c}.
```

As an example take $\hbar\omega_h=k_BT_h$, $\omega_c=\omega_h/2$ and $T_c=T_h/4$. Then $p_h=1/(e+1)=0.269$ and $p_c=1/(e^2+1)=0.119$. Each cycle delivers $W=0.075\,k_BT_h$ at efficiency 0.50, while the Carnot value for these baths is 0.75. Peterson and colleagues ran such a cycle on a nuclear spin with magnetic-resonance techniques. At maximum power they measured an efficiency near 42 percent, close to the ideal value of 44 percent for their cycle.

The derivation assumes unchanged populations during the isolated strokes. For $H\propto\sigma_z$ the Hamiltonians at different times commute, so the populations are conserved at any speed. If the field also turns, the eigenbasis rotates, and a fast stroke creates coherence between the instantaneous levels. That coherence carries extra energy, which the next bath contact dissipates. This loss, called quantum friction, lowers the work, and slow strokes avoid it at the cost of power. Incomplete thermalization in a contact reduces the population difference. It lowers the work per cycle but leaves the ratio $1-\omega_c/\omega_h$ unchanged.

A harmonic oscillator whose frequency is switched between $\omega_h$ and $\omega_c$ has the same Otto efficiency, because every level scales in proportion to $\omega$. A sudden frequency change, however, does alter its occupations. The strokes must then be slow compared with the oscillation period to avoid friction. This oscillator version has been realized with the motion of a single trapped ion.

## References For The Physical Derivation

- [H. T. Quan, Y.-x. Liu, C. P. Sun and F. Nori, Quantum Thermodynamic Cycles and quantum heat engines; heat and work in quantum Otto and Carnot cycles.](https://arxiv.org/abs/quant-ph/0611275)
- [R. Kosloff and Y. Rezek, The quantum harmonic Otto cycle; oscillator Otto engine, friction in finite-time strokes and the single-ion realization.](https://arxiv.org/abs/1612.03582)
- [J. P. S. Peterson and colleagues, Experimental characterization of a spin quantum heat engine; NMR Otto cycle with efficiency near 42 percent against a limit of 44 percent.](https://arxiv.org/abs/1803.06021)
