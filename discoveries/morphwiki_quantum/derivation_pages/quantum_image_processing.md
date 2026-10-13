# Quantum image processing

A camera stores a 1024 by 1024 grayscale image as about $10^6$ intensities. Twenty qubits have a state space of dimension $2^{20}$, the same number. Writing the intensities into the amplitudes of those qubits is the most compact quantum encoding of the image. The physical questions are how many operations prepare that state, what a gate does to it, and how many runs recover the pixels.

Number the $N=2^n$ pixels by an index $i$ written in binary on $n$ qubits, and let $x_i\geq0$ be the intensities. Amplitude encoding prepares

```math
|\psi_x\rangle=\frac{1}{\|x\|}\sum_{i=0}^{N-1}x_i|i\rangle,\qquad
\|x\|^2=\sum_i x_i^2,\qquad n=\log_2N.
```

The total brightness $\|x\|$ disappears on normalization and must be stored separately. A generic image fixes $N-1$ real parameters of this state. A single-qubit gate has at most three continuous angles, and a CNOT gate has none. A circuit layout with $g$ single-qubit gates therefore reaches at most a $3g$-dimensional set of states. Preparing every image requires

```math
g\geq\frac{N-1}{3}\approx3.5\times10^5\qquad(N=2^{20}).
```

Known constructions reach this order, $O(N)$ gates. Shorter circuits exist for structured inputs, for example intensity profiles whose sums over dyadic intervals can be computed efficiently (Grover and Rudolph). A quantum random-access memory is sometimes assumed instead, but its hardware also grows in proportion to $N$.

Processing, by contrast, can be cheap. A Hadamard gate on the least significant qubit mixes each pair of neighbouring pixels $2j$ and $2j+1$:

```math
(x_{2j},x_{2j+1})\mapsto\frac{(x_{2j}+x_{2j+1},\;x_{2j}-x_{2j+1})}{\sqrt2},\qquad
P_1=\frac{\sum_j(x_{2j}-x_{2j+1})^2}{2\|x\|^2}.
```

Outcome 1 on that qubit occurs with probability $P_1$. It leaves a state whose amplitudes are the differences of neighbouring pixels, a discrete gradient. Yao and colleagues used this single-gate operation for edge detection. For a row of eight pixels with intensities $(0,0,0,1,1,1,1,1)$, the step lies inside the pair of pixels 2 and 3, and $P_1=1/10$. Edges between pairs appear after the pixel index is shifted by one, which is a permutation of basis states.

The cost returns when the gradient image is to be recovered. A computational-basis measurement returns one pixel index per run, with probability $p_i$ equal to its squared amplitude. In $M$ runs pixel $i$ is counted about $Mp_i$ times, with fluctuation $(Mp_i)^{1/2}$. A relative precision $\delta$ on a typical pixel with $p_i\approx1/N$ therefore needs

```math
M\approx\frac{N}{\delta^2}\approx10^8\qquad(N=2^{20},\ \delta=0.1).
```

Each run consumes a fresh preparation of order $N$ gates, because the measurement destroys the state. The signs of the differences need further measurement bases, as in state tomography. Loading, one gate and complete measurement therefore cost far more than the roughly $N$ operations of a classical gradient filter.

This accounting is established. The qubit number is logarithmic in $N$, generic loading needs order $N$ gates, and recovering a full image needs order $N/\delta^2$ runs. A gain remains possible when the input is already a quantum state, such as light from a scene collected by a quantum sensor, or when only a few numbers are wanted. The edge weight $P_1$ is such a number. Binomial statistics give its estimate to precision $\epsilon$ from about $1/(4\epsilon^2)$ runs, independent of $N$. Which practical image tasks have such inputs and outputs remains open. Quantum imaging treats the related case in which the detected light itself carries the quantum correlations.

## References For The Physical Derivation

- [X.-W. Yao and colleagues, Quantum Image Processing and Its Application to Edge Detection: Theory and Experiment; amplitude encoding and edge detection with one single-qubit operation.](https://arxiv.org/abs/1801.01465)
- [V. V. Shende, S. S. Bullock and I. L. Markov, Synthesis of Quantum Logic Circuits; asymptotically optimal circuits for initializing a register in a generic state.](https://arxiv.org/abs/quant-ph/0406176)
- [L. Grover and T. Rudolph, Creating superpositions that correspond to efficiently integrable probability distributions; efficient loading of structured amplitude profiles.](https://arxiv.org/abs/quant-ph/0208112)
