# Quantum teleportation

An unknown qubit can be transferred using a shared entangled pair and two classical bits. The entangled resource alone does not transmit a usable signal: a joint measurement at the sender and a correction conditioned on its outcome are essential parts of the mechanism.

Let the input be $|\psi\rangle=a|0\rangle+b|1\rangle$ and let the shared pair be $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$, with the second member held by the receiver. Define the Bell states $|B_{mn}\rangle=(I\otimes X^nZ^m)|\Phi^+\rangle$, where $m,n\in\{0,1\}$. Expansion in this joint basis gives

```math
|\psi\rangle_1|\Phi^+\rangle_{23}
=\frac12\sum_{m,n=0}^{1}|B_{mn}\rangle_{12}\,X^nZ^m|\psi\rangle_3.
```

Each Bell outcome has probability one quarter, independent of the input amplitudes. Once the sender communicates $m,n$, the receiver applies $Z^mX^n$ and obtains the original state. The measurement determines a known transformation of the state, rather than its unknown amplitudes. This is why transmitting two classical bits suffices when the entangled pair has already been supplied.

Without the outcome record the receiver averages the four possible transformed states. For any input density operator $\rho$, that average is

```math
\frac14\sum_{m,n}X^nZ^m\rho Z^mX^n=\frac I2.
```

The receiver's local statistics then contain no dependence on the input. The same calculation establishes that the protocol cannot be used for faster-than-light signalling. The original input has participated in a destructive joint measurement, so the transfer does not create two independently available copies.

A nonideal entangled resource changes the resulting channel. For a Bell-diagonal resource, its Bell weights become probabilities of Pauli errors in the corrected output. Resource quality, Bell-measurement fidelity and the conditional correction can therefore be distinguished experimentally; all three can reduce the final state fidelity, but they enter the calculation at different steps.

Teleportation illustrates how a mechanism can be transferred across physical carriers. Photonic polarization, internal atomic levels and superconducting circuits may realize the same qubit relation, provided their entangling resource, joint measurement and correction implement the required maps. Changing only the name of the carrier leaves those requirements unresolved; demonstrating the maps establishes the actual correspondence.

## References For The Physical Derivation

- [D. Gottesman, Stabilizer Codes and Quantum Error Correction; entanglement, measurements and teleportation.](https://arxiv.org/abs/quant-ph/9705052)
- [C. Weedbrook and colleagues, Gaussian Quantum Information; continuous-variable realizations and finite-resource effects.](https://arxiv.org/abs/1110.3234)


## Relations In The Original Papers

[arXiv:1110.3234v1, S4.E101](https://arxiv.org/html/1110.3234v1#S4.E101). Teleportation of coherent states with a finite two-mode squeezed resource has fidelity below one. A continuous-variable comparison to the exact ideal qubit protocol; it is not the derivation of the qubit Bell-state identity.
