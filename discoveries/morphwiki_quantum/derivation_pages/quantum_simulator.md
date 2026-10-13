# Quantum simulator

A chain of fifty interacting spins has $2^{50}\approx10^{15}$ amplitudes, about 18 petabytes in double precision. A controllable quantum device can instead be made to follow the same dynamics, for example trapped ions with laser-driven spin couplings or ultracold atoms in optical lattices. In an analog simulator the device Hamiltonian is engineered to match the target. In a digital simulator the target evolution is decomposed into gates.

Let the target Hamiltonian be a sum $H=A+B$ of two parts that the device can apply separately, such as spin couplings $A$ and a transverse field $B$. Set $\hbar=1$, divide the time $t$ into $n$ steps of length $\delta=t/n$, and alternate the two evolutions. The Baker--Campbell--Hausdorff expansion of one step gives

```math
e^{-iA\delta}e^{-iB\delta}=\exp\!\Big[-i(A+B)\delta-\frac{\delta^2}{2}[A,B]+O(\delta^3)\Big].
```

Each step therefore carries an error of size $\delta^2\|[A,B]\|/2$, where $\|\cdot\|$ is the operator norm. Unitary evolution preserves norms, so the errors of the $n$ steps add at most linearly:

```math
\Big\|e^{-i(A+B)t}-\big(e^{-iAt/n}e^{-iBt/n}\big)^n\Big\|\leq\frac{t^2}{2n}\,\big\|[A,B]\big\|.
```

The error falls as $1/n$ and vanishes when $A$ and $B$ commute. A symmetric step places a half step of $A$ on each side of a full step of $B$. It cancels the commutator term and leaves an error of order $t^3/n^2$, set by double commutators.

For two spins with $A=JZ_1Z_2$ and $B=h(X_1+X_2)$, the commutator is $[A,B]=2iJh(Y_1Z_2+Z_1Y_2)$, with norm $4Jh$. For $J=h$, $Jt=1$ and ten steps the bound is $0.2$. Direct computation gives an actual error of $0.071$, which halves when the number of steps doubles. The symmetric step gives $0.006$. For a ring of $N$ spins the triangle inequality bounds the commutator by $4NJh$, so the required number of steps grows in proportion to $NJht^2/\epsilon$ for a target error $\epsilon$.

Real gates are imperfect. If every step adds an error of at most $\epsilon_s$, the total error is bounded by $at^2/n+n\epsilon_s$ with $a=\|[A,B]\|/2$. The bound is smallest at $n^*=t\sqrt{a/\epsilon_s}$, where it equals $2t\sqrt{a\epsilon_s}$. Beyond this number of steps, finer time steps make the simulation worse.

A simulation claim also requires an encoding $V$ of target states into device states, with $V^\dagger V=I$. If the device evolution differs from the encoded target evolution by at most $\varepsilon(t)$, every bounded observable $O$ inherits a bounded error:

```math
\big\|U_{\rm dev}(t)V-VU_{\rm tar}(t)\big\|\leq\varepsilon(t)\ \Longrightarrow\
\big|\langle O\rangle_{\rm tar}-\langle VOV^\dagger\rangle_{\rm dev}\big|\leq2\|O\|\,\varepsilon(t).
```

Analog simulators are validated differently. In the experiment of Greiner and colleagues (2002), atoms in an optical lattice realized the Bose--Hubbard model. Raising the lattice depth drove the transition from a superfluid to a Mott insulator, seen as the loss of interference peaks after release from the lattice. No Trotter bound applies there. The error budget comes instead from calibrating tunnelling, interaction and residual trapping against independent measurements. The commutator that sets the Trotter error is the same one that makes gate order matter in a quantum circuit.

## References For The Physical Derivation

- [A. M. Childs, Y. Su, M. C. Tran, N. Wiebe and S. Zhu, A Theory of Trotter Error; commutator bounds for product formulas.](https://arxiv.org/abs/1912.08854)
- [I. M. Georgescu, S. Ashhab and F. Nori, Quantum Simulation; analog and digital simulators and their platforms.](https://arxiv.org/abs/1308.6253)
