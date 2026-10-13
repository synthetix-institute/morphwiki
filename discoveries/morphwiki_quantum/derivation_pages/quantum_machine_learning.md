# Quantum machine learning

A quantum processor runs a fixed sequence of gates in which some rotation angles can be set. Each run ends with a measurement of a spin, and the average over many runs estimates an expectation value. Training adjusts the angles to lower a cost built from such averages, and it needs derivatives with respect to the angles. These derivatives can be measured on the same device by shifting each angle by a quarter turn.

Let one gate be $U(\theta)=e^{-i\theta G/2}$, where the generator $G$ is a product of Pauli matrices, so $G^2=I$. Collect all earlier gates into the input state $|\psi\rangle$. Collect all later gates, together with the measured observable, into a Hermitian operator $A$. The measured average is $f(\theta)=\langle\psi|U(\theta)^\dagger AU(\theta)|\psi\rangle$. Because $G^2=I$, the gate equals $\cos(\theta/2)I-i\sin(\theta/2)G$. The average contains only products of $\cos(\theta/2)$ and $\sin(\theta/2)$, and hence

```math
f(\theta)=a+b\cos\theta+c\sin\theta,\qquad
\frac{df}{d\theta}=\frac{f(\theta+\pi/2)-f(\theta-\pi/2)}{2}.
```

The rule follows from $\cos(\theta+\pi/2)-\cos(\theta-\pi/2)=-2\sin\theta$ and the corresponding identity for the sine. It is exact rather than a finite-difference estimate. Because the shifts are large, the difference is not divided by a small step, and shot noise is not amplified. For a qubit prepared in $|0\rangle$, rotated by $R_y(\theta)$ and measured along $z$, $f=\cos\theta$ and the rule returns $-\sin\theta$. If $A$ has eigenvalues $\pm1$ and each average uses $M$ runs, the gradient estimate has variance at most $1/(2M)$. Generators with more than two eigenvalues need rules with more shifts.

Whether the gradients are large enough to measure is a separate question. McClean and colleagues considered circuits in which the gates on each side of the parameter reproduce the first two moments of uniformly random unitaries. Such an ensemble is called a 2-design. For $n$ qubits the gradient then averages to zero, and its variance decreases exponentially:

```math
\langle\partial_kf\rangle=0,\qquad \operatorname{Var}(\partial_kf)\propto2^{-n}.
```

For Pauli generator and observable, a direct sampling of random unitaries on both sides gives a variance close to $2^{-(n+1)}$. Resolving the sign of such a gradient requires a shot-noise variance $1/(2M)$ below it. For 50 qubits this means of order $10^{15}$ runs per gradient component.

The condition matters. Cerezo and colleagues proved that observables acting on few qubits, with circuit depth of order $\log n$, give at worst polynomially small gradients. Global observables give exponentially small gradients even in shallow circuits. A simulation of layered $y$ rotations and controlled-$Z$ gates shows both regimes. For the product of $Z$ over all qubits, the gradient variance decreased roughly as $2^{-n}$ from $n=2$ to 12 at depth two. For $Z$ on one qubit at the same depth it stayed between 0.35 and 0.39.

Established are the shift rule, the trigonometric dependence on each angle, and the exponential suppression of gradients under the stated randomness. Open is whether such circuits, trained on classical data, outperform classical learning on tasks of practical interest. Proven separations exist for specially constructed problems, discussed under quantum neural networks. The same derivative of an average with respect to a phase sets the sensitivity in quantum metrology.

## References For The Physical Derivation

- [M. Schuld, V. Bergholm, C. Gogolin, J. Izaac and N. Killoran, Evaluating analytic gradients on quantum hardware; parameter-shift rules for gate derivatives.](https://arxiv.org/abs/1811.11184)
- [J. R. McClean and colleagues, Barren plateaus in quantum neural network training landscapes; exponentially small gradients for circuits forming 2-designs.](https://arxiv.org/abs/1803.11173)
- [M. Cerezo and colleagues, Cost Function Dependent Barren Plateaus in Shallow Parametrized Quantum Circuits; global versus local observables at logarithmic depth.](https://arxiv.org/abs/2001.00550)
