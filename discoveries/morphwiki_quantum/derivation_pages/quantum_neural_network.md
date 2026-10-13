# Quantum neural network

A parametrized circuit used as a neural network takes an input number $x$ as a rotation angle, applies trainable gates, and reports the average of a measured spin. Repeating the experiment for many inputs traces a curve $f(x)$. The frequencies present in such curves are fixed by the eigenvalues of the generators that encode $x$, much as level differences fix the lines of a spectrum.

Let the circuit alternate trainable unitaries $W_\ell$ with $L$ encoding gates $S(x)=e^{-ixG/2}$, where the Hermitian generator $G$ has eigenvalues $\lambda_j$. With measured observable $M$ and initial state $|0\rangle$,

```math
f_\theta(x)=\langle0|U^\dagger MU|0\rangle,\qquad
U=W_L\,S(x)\,W_{L-1}\cdots W_1\,S(x)\,W_0.
```

In the eigenbasis of $G$, each encoding multiplies an amplitude by $e^{-ix\lambda_j/2}$. After $L$ encodings each amplitude is a sum of terms carrying $e^{-ix\Lambda/2}$, where $\Lambda$ is a sum of $L$ eigenvalues, one from each encoding. The average multiplies one amplitude by the complex conjugate of another, so only differences of such sums appear:

```math
f_\theta(x)=\sum_{\omega\in\Omega}c_\omega(\theta)\,e^{i\omega x},\qquad
\Omega=\Big\{\frac{\Lambda_k-\Lambda_j}{2}\Big\},\qquad c_{-\omega}=c_\omega^*.
```

For a Pauli generator, $\lambda=\pm1$ and $\Omega=\{-L,\ldots,L\}$. The model is then a trigonometric polynomial of degree $L$ in $x$. The trainable gates set only the coefficients $c_\omega$, and adding trainable layers adds no frequencies (Schuld, Sweke and Meyer). Encoding $x$ once on each of $n$ qubits in parallel also gives degree $n$.

A one-qubit example makes this concrete. Apply $R_y(\theta)$ to $|0\rangle$, encode with $R_x(x)$, apply $R_y(\phi)$ and measure $Z$. Following the Bloch vector through the three rotations gives the first expression below. The circuit $R_x(x)R_y(\phi)R_x(x)$ acting on $|0\rangle$, with the input encoded twice, gives the second:

```math
L=1:\ f=\cos\theta\cos\phi\cos x-\sin\theta\sin\phi,\\
L=2:\ f=\frac{\cos\phi-1}{2}+\frac{\cos\phi+1}{2}\cos2x.
```

The single-encoding circuit cannot represent $\cos2x$ for any angles. Its best mean-square approximation within degree one is zero, because $\cos2x$ is orthogonal to $1$, $\cos x$ and $\sin x$. The two-encoding circuit produces it exactly at $\phi=0$. Repeated encoding of the data is how such models gain frequencies. Their coefficients are trained by the parameter-shift rule of quantum machine learning, and their gradients face the same barren plateaus.

For a single encoding layer and a fixed initial layer $W_0$, the model is $f_\theta(x)=\operatorname{Tr}[\rho(x)M_\theta]$. Here $\rho(x)=S(x)W_0|0\rangle\langle0|W_0^\dagger S(x)^\dagger$ is the encoded state and $M_\theta=W_1^\dagger MW_1$. The model is linear in $\rho(x)$, and the dependence on $x$ enters only through the encoding. Schuld showed that supervised models of this kind are kernel methods, in which data enter through overlaps of encoded states. The name neural network refers to the layered trainable structure, not to neuron-like nonlinear units.

Established are the Fourier structure, the role of the encoding and the kernel form. Liu, Arunachalam and Temme proved a speed-up for one classification problem constructed from the discrete logarithm, assuming that this logarithm is classically hard to compute. That result requires a fault-tolerant computer and specially built data. Whether such models outperform classical networks on practical data is open.

## References For The Physical Derivation

- [M. Schuld, R. Sweke and J. J. Meyer, The effect of data encoding on the expressive power of variational quantum machine learning models; Fourier spectrum fixed by the encoding gates.](https://arxiv.org/abs/2008.08605)
- [M. Schuld, Supervised quantum machine learning models are kernel methods; linearity in the encoded state and the kernel form.](https://arxiv.org/abs/2101.11020)
- [Y. Liu, S. Arunachalam and K. Temme, A rigorous and robust quantum speed-up in supervised machine learning; separation for a classification problem built on the discrete logarithm.](https://arxiv.org/abs/2010.02174)
