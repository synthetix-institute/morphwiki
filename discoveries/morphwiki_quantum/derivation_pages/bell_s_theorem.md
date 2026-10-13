# Bell's theorem

Two spin-1/2 particles leave a common source in opposite directions. Each meets a Stern--Gerlach magnet whose orientation is chosen at random just before arrival, and each detector records $+1$ or $-1$. Bell asked whether the correlations of these records can be produced by properties fixed at the source together with the local settings alone.

Let each pair carry a variable $\lambda$ with distribution $\rho(\lambda)$. A local model gives outcomes $A_a(\lambda)=\pm1$ and $B_b(\lambda)=\pm1$, where $A$ does not depend on the distant setting $b$ and $\rho$ depends on neither setting. With two settings per side, one bracket below vanishes and the other equals $\pm2$ for every pair:

```math
S_\lambda=A_a(B_b+B_{b'})+A_{a'}(B_b-B_{b'})=\pm2\\
|E(a,b)+E(a,b')+E(a',b)-E(a',b')|\leq2
```

Here $E(a,b)$ is the average of $A_aB_b$ over $\lambda$. Random local responses do not help, because they are mixtures of deterministic ones and the bound is linear in the probabilities. This is the Clauser--Horne--Shimony--Holt (CHSH) inequality.

For the spin singlet, quantum mechanics gives $E(a,b)=-\cos(\theta_a-\theta_b)$, with $\theta$ the magnet angle in a common plane. The angles $0^\circ$ and $90^\circ$ on one side, with $45^\circ$ and $-45^\circ$ on the other, give $|S|=4/\sqrt2=2\sqrt2\approx2.83$.

No quantum state and no choice of $\pm1$ observables does better. For the Bell operator $\mathcal B=A\otimes(B+B')+A'\otimes(B-B')$, squaring and using $A^2=B^2=I$ gives

```math
\mathcal B^2=4I-[A,A']\otimes[B,B'],\qquad
|\langle\mathcal B\rangle|\leq2\sqrt2.
```

Each commutator has norm at most 2, so no eigenvalue of $\mathcal B^2$ exceeds 8. This is the Tsirelson bound. It also shows that a violation requires noncommuting settings on both sides; commuting pairs return the classical value 2. If the singlet is mixed with white noise so that correlations shrink by a factor $v$, then $S=2\sqrt2\,v$ and a violation requires $v>1/\sqrt2$.

An experiment must also close two gaps in the derivation. If detectors miss many particles, the detected subset may be unrepresentative; for a maximally entangled state the CHSH test needs efficiency above $2(\sqrt2-1)\approx0.83$. If one setting can influence the distant detector before its record is final, a local signal could fix the correlations. The settings must also be statistically independent of $\lambda$.

In 2015 Hensen and colleagues entangled electron spins in two diamond defects 1.3 km apart. Settings were chosen randomly and each spin was measured within the light travel time between the sites. In 245 heralded trials, each giving an outcome at both sites, they found $S=2.42\pm0.20$. Photon experiments in Vienna and Boulder closed both gaps in the same year.

The theorem constrains local models of the records; it does not modify quantum mechanics. The Einstein--Podolsky--Rosen argument, which motivated it, used predictions with certainty; quantum nonlocality extends the comparison to three particles without an inequality. Device-independent quantum key distribution uses the observed value of $S$ to bound an eavesdropper's information.

## References For The Physical Derivation

- [N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani and S. Wehner, Bell nonlocality; CHSH inequality, Tsirelson bound and loopholes.](https://arxiv.org/abs/1303.2849)
- [B. Hensen and colleagues, Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km; S = 2.42 in 245 trials.](https://arxiv.org/abs/1508.05949)
