# Von Neumann algebra

An experimenter who controls one of two entangled spins, or the field inside one region of space, can apply only some operations. The set of those operations is an algebra closed under products, adjoints and limits. Von Neumann algebras describe such sets. Their structure decides whether the subsystem has a density matrix and how thermal equilibrium can be defined.

The commutant $M'$ of a set $M$ of operators contains every operator that commutes with all of $M$. Von Neumann's bicommutant theorem states that an algebra containing the identity, closed under adjoints and under weak limits, equals its double commutant. For two spins the operations on $A$ and on $B$ are each other's commutants:

```math
M'=\{B:\ [A,B]=0\ \text{for all}\ A\in M\},\qquad M''=M,\\
\bigl(\mathcal B(\mathcal H_A)\otimes I\bigr)'=I\otimes\mathcal B(\mathcal H_B).
```

The centre $M\cap M'$ contains operators that commute with everything in the algebra. If it holds more than multiples of the identity, the states split into sectors with no coherent superpositions between them. Total electric charge separates sectors in this way.

Algebras with trivial centre are called factors, and they come in types. A subsystem of finitely many degrees of freedom gives type I, where every state is a density matrix $\rho_A$ with $\langle A\rangle=\operatorname{Tr}(\rho_AA)$. An infinite chain of Bell pairs gives, on one side, an algebra with a normalized trace but no minimal projector, of type $\mathrm{II}_1$. The algebra of a region in relativistic quantum field theory has type III, with no trace at all. There the entanglement entropy of a region diverges unless a short-distance cutoff is imposed.

Thermal equilibrium can be stated without a density matrix. For a finite system, the Gibbs state $\rho=e^{-\beta H}/Z$ with $\beta=1/k_BT$ satisfies the Kubo--Martin--Schwinger condition. It follows from cyclicity of the trace, with $e^{-\beta H}$ acting as an evolution in imaginary time:

```math
\langle A(t)B\rangle_\beta=\langle B\,A(t+i\hbar\beta)\rangle_\beta,\qquad
A(t)=e^{iHt/\hbar}Ae^{-iHt/\hbar}.
```

In an infinite system $e^{-\beta H}$ has no trace, but the condition still makes sense on the algebra and defines equilibrium. Several solutions at the same temperature describe coexisting phases, such as the two magnetizations of a ferromagnet. Tomita--Takesaki theory shows that every faithful normal state of a von Neumann algebra satisfies this condition for a flow of its own, the modular flow.

The condition has a measured consequence. Fourier transforming it for the correlation function of an observable gives detailed balance, with $\omega>0$ the energy taken up by the system:

```math
S(\omega)=\int dt\,e^{i\omega t}\langle A(t)A(0)\rangle_\beta,\qquad
S(-\omega)=e^{-\beta\hbar\omega}S(\omega).
```

In Raman scattering from silicon at 300 kelvin, the optical phonon at 520 inverse centimetres gives an anti-Stokes to Stokes ratio of $e^{-2.49}\approx0.083$. This value holds after correction for the frequency dependence of scattering. The ratio serves as a contactless thermometer. The Bisognano--Wichmann theorem applies the same condition to the vacuum restricted to a wedge of spacetime, with boosts as the flow. It predicts the Unruh temperature $\hbar a/(2\pi ck_B)$, about 0.41 kelvin for an acceleration of $10^{20}$ metres per second squared. The theorem is established; a direct observation of the Unruh effect is still lacking. Quantum statistical mechanics uses the finite-system form of the same condition.

## References For The Physical Derivation

- [E. Witten, Notes on Some Entanglement Properties of Quantum Field Theory; local algebras, modular theory and the Bisognano--Wichmann theorem.](https://arxiv.org/abs/1803.04993)
- [J. Yngvason, The Role of Type III Factors in Quantum Field Theory; type I and type III algebras and their physical consequences.](https://arxiv.org/abs/math-ph/0411058)
