# Quantum eraser experiment

Light passing two slits forms fringes on a screen. If each path leaves a mark in another degree of freedom, the fringes fade. A later measurement of that mark in a suitable basis can recover fringes in sorted subsets of the records.

Let the screen amplitudes from the two slits be $\psi_1(x)$ and $\psi_2(x)$, and let the paths leave marker states $|m_1\rangle$ and $|m_2\rangle$. The joint state is proportional to $\psi_1(x)|m_1\rangle+\psi_2(x)|m_2\rangle$. Ignoring the marker, the screen intensity is

```math
P(x)\propto|\psi_1|^2+|\psi_2|^2+2\operatorname{Re}\big[\psi_1^*\psi_2\langle m_1|m_2\rangle\big].
```

The fringe term is multiplied by the marker overlap. For equal intensities the visibility equals $|\langle m_1|m_2\rangle|$, and orthogonal markers remove the fringes entirely. The marking need not deliver any momentum kick. The interference term disappears because the screen amplitude is now correlated with an orthogonal marker state.

Now take orthogonal markers and measure them in a rotated basis, with an angle $\beta$ and a phase $\gamma$ that the experimenter sets:

```math
|e_+\rangle=\cos\tfrac{\beta}{2}|m_1\rangle+e^{i\gamma}\sin\tfrac{\beta}{2}|m_2\rangle,\\
|e_-\rangle=\sin\tfrac{\beta}{2}|m_1\rangle-e^{i\gamma}\cos\tfrac{\beta}{2}|m_2\rangle.
```

Conditioning on each outcome projects the marker and leaves a definite screen amplitude. The two conditional patterns have the same visibility:

```math
\psi_+=\cos\tfrac{\beta}{2}\,\psi_1+e^{-i\gamma}\sin\tfrac{\beta}{2}\,\psi_2,\qquad
\psi_-=\sin\tfrac{\beta}{2}\,\psi_1-e^{-i\gamma}\cos\tfrac{\beta}{2}\,\psi_2,\\
V_{\rm cond}=|\sin\beta|.
```

At $\beta=0$ the marker measurement reveals the path and the subsets show no fringes. At $\beta=\pi/2$ the marker basis is unbiased with respect to the paths; each subset shows full-contrast fringes, one shifted by half a period relative to the other. The two subsets always add to the unmarked, fringe-free pattern. Erasure therefore selects subsets, and the total distribution on the screen is unchanged.

Walborn, Terra Cunha, Pádua and Monken carried this out with polarization-entangled photon pairs from parametric down-conversion. Quarter-wave plates in front of the two slits marked the path in the circular polarization of the signal photon, and the coincidence fringes vanished. A polarizer on the distant idler photon then projected the pair onto a basis unbiased with respect to the paths. Fringes and antifringes reappeared in the coincidence counts.

The entangled partner matters. If a single photon carries its own polarization mark, a polarizer at $45^\circ$ before the screen recovers fringes. That version is reproduced by classical polarization optics, through the Fresnel--Arago laws. With an entangled partner, the basis is chosen on a photon that never passes the slits, and the fringes exist only in coincidence data.

The trade-off between partial marking and partial visibility is the subject of wave-particle duality. The delayed-choice quantum eraser applies the same conditioning to an idler recorded after its partner.

## References For The Physical Derivation

- [S. P. Walborn, M. O. Terra Cunha, S. Padua and C. H. Monken, A double-slit quantum eraser; polarization marking and erasure with entangled photons.](https://arxiv.org/abs/quant-ph/0106078)
- [X.-S. Ma, J. Kofler and A. Zeilinger, Delayed-choice gedanken experiments and their realizations; quantum erasers and complementarity.](https://arxiv.org/abs/1407.2930)
