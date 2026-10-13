# Delayed-choice quantum eraser

A photon reaches a detector that scans across a screen, and its position is recorded. Several nanoseconds later its partner photon is sent at random along one of two routes. One leads to a detector that reveals where the pair was emitted; the other leads to a beam splitter that hides this information. Sorting the screen records by the partner's later result reveals interference fringes in some subsets.

In the experiment of Kim, Yu, Kulik, Shih and Scully, a pump laser illuminates a nonlinear crystal in two regions $A$ and $B$. Either region may emit a signal and idler pair, so the pair is in the state $(|A\rangle_s|A\rangle_i+|B\rangle_s|B\rangle_i)/\sqrt2$. A lens maps the two signal paths to amplitudes $\psi_A(x)$ and $\psi_B(x)$ at the screen detector $D_0$.

The idler meets a 50:50 beam splitter on each path. One output goes to a detector that receives only idlers from $A$ ($D_3$) or only from $B$ ($D_4$). The other outputs are combined on a central beam splitter whose two ports, $D_1$ and $D_2$, cannot tell $A$ from $B$. Projecting both photons onto the detected states gives the joint probabilities

```math
P(x,D_{1,2})=\tfrac18|\psi_A(x)\pm\psi_B(x)|^2,\qquad
P(x,D_3)=\tfrac14|\psi_A(x)|^2,\qquad P(x,D_4)=\tfrac14|\psi_B(x)|^2.
```

Coincidences with $D_1$ show fringes and those with $D_2$ show the complementary antifringes, shifted by half a period. Coincidences with $D_3$ or $D_4$ show the smooth single-path profile. Each idler detector receives a quarter of the pairs.

The time order of the two detections plays no part in this calculation. The projector for the signal position and the projector for an idler detector act on different photons and commute. The joint probability is therefore the same whichever record is made earlier, and in any reference frame:

```math
P(x,k)=\big\|(\langle x|_s\otimes\langle k|_i)\Psi\big\|^2,\qquad
\sum_kP(x,k)=\tfrac12\big(|\psi_A(x)|^2+|\psi_B(x)|^2\big).
```

The screen pattern by itself has no fringes, whatever happens to the idler and whenever it happens. The idler path did not affect where the signal landed. It determines which subset of the existing records is selected, and the fringes appear only when the subsets are compared using the idler records. Those records travel by ordinary means, so no information is sent to the earlier detection.

In the 2000 experiment the idler paths were longer, so the idler was registered several nanoseconds after its partner. Ma and colleagues later made the choice with a random number generator spacelike separated from the interference, over a 144 km free-space link between two Canary Islands. Interference again appeared only in the sorted subsets.

The calculation is the conditional-fringe analysis of the quantum eraser experiment, applied to an entangled pair whose members are recorded at different times. The commuting projectors are also why the correlations in Bell experiments cannot be used to send messages.

## References For The Physical Derivation

- [Y.-H. Kim, R. Yu, S. P. Kulik, Y. H. Shih and M. O. Scully, A Delayed Choice Quantum Eraser; the two-region down-conversion experiment analysed here.](https://arxiv.org/abs/quant-ph/9903047)
- [X.-S. Ma and colleagues, Quantum erasure with causally disconnected choice; spacelike-separated choice over 144 km.](https://arxiv.org/abs/1206.6578)
- [X.-S. Ma, J. Kofler and A. Zeilinger, Delayed-choice gedanken experiments and their realizations; review of the time-order analysis.](https://arxiv.org/abs/1407.2930)
