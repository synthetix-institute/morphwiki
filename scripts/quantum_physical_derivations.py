"""Authored physical derivations for topics previously rendered as role overviews.

Paragraphs and displays follow the individual calculation, not the branch
template. These are expositions of established physics, not extracted text or
claims of automated discovery. Mathematical checks live in the test suite.
"""

NARRATIVES = {
    "quantum_state": [
        ("p", r"Preparing a spin along one axis fixes probabilities for measurements along every other axis. The information needed for those predictions can be collected in a density operator $\rho$. For a two-level system let $\boldsymbol\sigma=(\sigma_x,\sigma_y,\sigma_z)$ be the Pauli matrices and $\mathbf r$ the vector of their expectation values. The three components of $\mathbf r$ determine the state:"),
        ("eq", r"""\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),\qquad |\mathbf r|\leq1."""),
        ("p", r"The bound follows from positivity: the two eigenvalues are $(1\pm|\mathbf r|)/2$. A unit vector describes a pure preparation. An interior point describes a mixed state, which may arise from uncontrolled preparation or from ignoring a correlated partner. Different ensembles can produce the same density operator. A later experiment acting only on this spin cannot distinguish those ensembles unless additional information about the preparation is accessible."),
        ("p", r"A Stern--Gerlach measurement along a unit vector $\mathbf n$ has projectors $E_\pm=(I\pm\mathbf n\cdot\boldsymbol\sigma)/2$. The probability of each outcome is consequently"),
        ("eq", r"""p_\pm=\operatorname{Tr}(\rho E_\pm)=\frac12(1\pm\mathbf r\cdot\mathbf n)."""),
        ("p", r"The same state gives certainty along its preparation axis and an equal distribution along a perpendicular axis. The uncertainty therefore belongs to the relation between preparation and measurement. It is not evidence that a pure state is an unspecified classical direction. Measurements along three independent axes reconstruct the Bloch vector, while measurements along only one axis leave a disk of compatible states."),
        ("p", r"For a composite system the density operator also contains correlations. The singlet and an equal mixture of oppositely aligned spins both give $\rho_A=I/2$ for either individual spin, but they predict different joint measurements. A partial trace retains every expectation of an operator acting on subsystem $A$ alone. It need not retain the information required for subsequent interacting evolution, because the interaction can convert a joint correlation into a local expectation value."),
        ("eq", r"""\langle O_A\rangle=\operatorname{Tr}_{AB}[\rho_{AB}(O_A\otimes I_B)]
=\operatorname{Tr}_A(\rho_A O_A),\qquad \rho_A=\operatorname{Tr}_B\rho_{AB}."""),
        ("p", r"Thus the state required by a mechanism is fixed by the available measurements and subsequent interactions together. Local spin probabilities require $\rho_A$ at the present time; a prediction after coupling to $B$ generally requires the joint state or an independently specified preparation of $B$. This distinction is the physical reason to keep the carrier, interaction and preparation connected in the description."),
    ],
    "two_state_quantum_system": [
        ("p", r"An avoided crossing couples two states that would otherwise evolve independently. In their basis, a constant energy offset contributes only an overall phase, whereas the remaining Hamiltonian determines both transition probabilities and phase evolution. Let $\Delta$ be the angular-frequency detuning between the uncoupled levels and $\Omega$ a real coupling frequency. With $|0\rangle$ and $|1\rangle$ the eigenstates of $\sigma_z$, choose"),
        ("eq", r"""H=\frac{\hbar}{2}(\Delta\sigma_z+\Omega\sigma_x),\qquad \omega_R=\sqrt{\Delta^2+\Omega^2}."""),
        ("p", r"The Pauli algebra gives $(\Delta\sigma_z+\Omega\sigma_x)^2=\omega_R^2I$. Every higher power in the exponential therefore reduces to either the identity or the Hamiltonian. The evolution follows without fitting a transition curve:"),
        ("eq", r"""U(t)=\cos\frac{\omega_Rt}{2}\,I-i\sin\frac{\omega_Rt}{2}\,
\frac{\Delta\sigma_z+\Omega\sigma_x}{\omega_R}."""),
        ("p", r"For the preparation $|0\rangle$, the off-diagonal matrix element of $U$ gives the transition probability"),
        ("eq", r"""P_{0\to1}(t)=\frac{\Omega^2}{\Delta^2+\Omega^2}
\sin^2\!\left(\frac{t}{2}\sqrt{\Delta^2+\Omega^2}\right)."""),
        ("p", r"On resonance the coupling can transfer the entire population; a pulse of duration $\pi/|\Omega|$ interchanges the levels. Detuning increases the oscillation frequency but reduces the greatest achievable population transfer. These two consequences distinguish a changed level splitting from a changed coupling even when a short segment of an oscillation looks similar."),
        ("p", r"The Bloch vector rotates about the effective axis $(\Omega,0,\Delta)$. A second pulse about another axis can convert a relative phase into a population difference. Reversing two such pulses generally changes the result because their Hamiltonians do not commute. The state space is the same in both experiments; the difference lies in the sequence of interactions, and the measured population exposes that difference."),
        ("p", r"This calculation applies to any isolated pair of levels governed by the stated Hamiltonian, including two coupled modes or selected atomic states. Its use for a larger physical system requires that other levels remain unpopulated and environmental relaxation be negligible over the pulse duration. If the Hamiltonian was obtained in a rotating frame, the rotating-wave approximation and the transformation of the measured operator are additional parts of the correspondence. Specifying a two-dimensional matrix does not by itself establish those conditions in a device."),
    ],
    "fourier_transform": [
        ("p", r"A free particle propagates most simply in momentum space, where each momentum component accumulates its own phase. A localized detector, however, asks for a position probability. The Fourier transform connects these descriptions while preserving the physical state. On the real line, for a square-integrable wave function $\psi$ and momentum $p$, take"),
        ("eq", r"""\widetilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}\int_{\mathbb R}
e^{-ipx/\hbar}\psi(x)\,dx,\qquad
\int|\widetilde\psi(p)|^2dp=\int|\psi(x)|^2dx."""),
        ("p", r"For wave functions on a common suitable domain, integration by parts carries the position-space momentum operator $-i\hbar\partial_x$ into multiplication by $p$. Multiplication by position becomes $i\hbar\partial_p$. The kinetic equation and the detector must both be transformed:"),
        ("eq", r"""\mathcal F(-i\hbar\partial_x)\mathcal F^{-1}=p,\qquad
\mathcal F x\mathcal F^{-1}=i\hbar\partial_p,\qquad
\widetilde H=\frac{p^2}{2m}+V(i\hbar\partial_p)."""),
        ("p", r"The last expression is immediately useful for polynomial potentials; for a general potential, multiplication in position space is represented by an integral kernel in momentum space. A local interaction can therefore become nonlocal in the new coordinates without changing the theory. Similarity of displayed formulas is neither necessary nor sufficient for physical equivalence."),
        ("p", r"For a normalized Gaussian packet with initial position variance $\sigma_x^2$, zero position-momentum covariance and minimum uncertainty, the free evolution multiplies each momentum amplitude by $\exp[-ip^2t/(2m\hbar)]$. Transforming back gives"),
        ("eq", r"""\operatorname{Var}x(t)=\sigma_x^2+
\frac{\hbar^2t^2}{4m^2\sigma_x^2}."""),
        ("p", r"The packet broadens because its different momentum components separate during propagation. The momentum distribution itself remains unchanged. This provides a direct comparison between descriptions: one representation makes the conservation of momentum probabilities explicit, while the other displays the spatial spreading produced by those same components."),
        ("p", r"Boundaries change this correspondence. Periodic functions on a finite interval have a discrete Fourier series; Dirichlet eigenfunctions lead instead to a sine expansion. Surface terms must vanish under the actual boundary conditions before the integration-by-parts identity defines the required operator map. The operation of Fourier transformation is transferable, but the domain and measure determine which transform and which spectrum describe the physical system."),
    ],
    "spectral_theory": [
        ("p", r"An observable specifies both possible outcomes and how a prepared state distributes probability among them. For a self-adjoint operator $A$, the spectral measure $E_A$ assigns an orthogonal projector to each measurable set of real outcomes. The operator and its measurement probabilities are reconstructed from this measure:"),
        ("eq", r"""A=\int_{\mathbb R}\lambda\,dE_A(\lambda),\qquad
p(\lambda\in B)=\operatorname{Tr}[\rho E_A(B)]."""),
        ("p", r"Here $B$ is an interval or other measurable outcome set and $\rho$ the density operator. For a discrete spectrum the integral becomes a sum over eigenspace projectors. For position or free-particle momentum it is genuinely continuous; their ideal eigenvectors are generalized distributions rather than normalizable prepared states. A detector with finite resolution measures an interval probability, not a normalizable state at one exact continuum value."),
        ("p", r"The same spectral measure determines functions of the operator. If $H$ is the time-independent Hamiltonian, the function $\exp(-iEt/\hbar)$ gives its unitary evolution. An energy decomposition therefore connects a spectroscopic question to dynamics:"),
        ("eq", r"""U(t)=\int e^{-iEt/\hbar}\,dE_H(E),\qquad
\langle\psi|U(t)|\psi\rangle=\int e^{-iEt/\hbar}\,d\mu_\psi(E),"""),
        ("p", r"where $\mu_\psi(B)=\langle\psi|E_H(B)|\psi\rangle$ is the energy distribution of the preparation. The survival amplitude is its Fourier transform. A narrow energy distribution changes phase slowly relative to itself; a broad distribution can dephase rapidly. This connects spectral width to temporal evolution without assuming irreversible decay."),
        ("p", r"The spectrum belongs to the operator with its domain. On an interval of length $L$, the same differential expression $-\hbar^2\partial_x^2/(2m)$ has a zero-energy constant mode with Neumann conditions, while Dirichlet conditions exclude it and begin at $\pi^2\hbar^2/(2mL^2)$. A change of boundary therefore changes both the energy outcomes and the time evolution, even though the bulk equation is unchanged."),
        ("p", r"Two Hamiltonians with identical energy values can still have different observable matrix elements. Transporting a mechanism requires a correspondence between states and observables, not just a matched list of eigenvalues. Spectral theory supplies the predictions once that correspondence and the operator domains are specified; it also identifies precisely what an isospectral comparison leaves undecided."),
    ],
    "canonical_commutation_relation": [
        ("p", r"Translations in position and changes in momentum act differently when their order is reversed. For a particle on the real line, let $X$ multiply a wave function by $x$ and let $P=-i\hbar\partial_x$. On smooth rapidly decreasing wave functions, direct differentiation gives"),
        ("eq", r"""[X,P]\psi=X(-i\hbar\partial_x\psi)+i\hbar\partial_x(x\psi)
=i\hbar\psi."""),
        ("p", r"The additional term comes from differentiating the coordinate itself. It fixes the relation between the two operations, independently of the Hamiltonian subsequently chosen. With standard deviations defined in the prepared state and finite relevant moments, the Cauchy--Schwarz inequality applied to $(X-\langle X\rangle)\psi$ and $(P-\langle P\rangle)\psi$ then gives"),
        ("eq", r"""\Delta X\,\Delta P\geq\frac{\hbar}{2}."""),
        ("p", r"This bound concerns the spread of outcomes in identically prepared ensembles. A measurement-disturbance experiment introduces an apparatus and a sequence of measurements and requires its own dynamical model. The preparation bound should not be substituted for that separate calculation."),
        ("p", r"The exponentiated relation makes domain issues more transparent. Let $T(a)=\exp(-iaP/\hbar)$ translate a wave function by length $a$, and $B(b)=\exp(ibX/\hbar)$ shift its momentum by $b$. Acting on a wave function in either order gives"),
        ("eq", r"""[T(a)\psi](x)=\psi(x-a),\qquad
T(a)B(b)=e^{-iab/\hbar}B(b)T(a)."""),
        ("p", r"The phase is proportional to the phase-space area enclosed by the two moves. It is common to the state for a single path, but can become a relative phase when the two operation sequences form coherent alternatives. This is the physical content of the central extension represented by the Heisenberg group."),
        ("p", r"No finite-dimensional matrices obey $[X,P]=i\hbar I$ exactly: taking a trace makes the left side zero and the right side nonzero. A truncated oscillator basis or a finite numerical grid must therefore depart from the relation somewhere. Such departures can be approximation effects rather than additional interactions. An exact construction records the representation and tests the states on which the commutator identity is being used."),
    ],
    "heisenberg_group": [
        ("p", r"A displacement of a particle's position followed by a momentum kick traces a rectangle in phase space when both operations are undone. Although the final position and momentum shifts cancel, the quantum amplitude acquires a phase. The Heisenberg group includes this phase as part of the composition law."),
        ("p", r"For canonical operators satisfying $[X,P]=i\hbar I$, define the displacement with position increment $a$ and momentum increment $b$ by $D(a,b)=\exp[i(bX-aP)/\hbar]$. The commutator of the exponents is a scalar, so the Baker--Campbell--Hausdorff series stops after that commutator:"),
        ("eq", r"""D(a,b)D(a',b')=
e^{i(ba'-ab')/(2\hbar)}D(a+a',b+b')."""),
        ("p", r"The antisymmetric combination $ba'-ab'$ is the oriented symplectic area. Its appearance explains why a description retaining only the two displacement coordinates has a projective composition law, whereas adding the phase gives an ordinary group representation. The central coordinate records how operations compose, rather than another position of the particle."),
        ("eq", r"""D(a,0)D(0,b)D(-a,0)D(0,-b)=e^{-iab/\hbar}I."""),
        ("p", r"A common overall phase has no effect on the probability of a single prepared state. To measure the loop phase, the displaced sequence must interfere with a reference sequence, for example through two coherent branches of a controlled operation. The observable is then a relative phase between the branches. A phase generated by a chosen path is compatible with fully specified dynamics."),
        ("p", r"The construction also relates particle motion to oscillator modes. Appropriate dimensionless quadratures express the same displacement algebra through creation and annihilation operators. Acting on the oscillator vacuum produces a coherent state; displacement changes its mean quadratures while preserving the vacuum covariance. The carrier and physical units differ, but the central commutation relation is the same mathematical relation being realized."),
        ("p", r"The uniqueness of the usual irreducible representation requires finitely many canonical pairs, regularity and a fixed nonzero central parameter. Quantum fields contain infinitely many modes and can admit inequivalent representations. Consequently the finite-dimensional symplectic picture cannot be promoted without qualification to an equivalence of arbitrary field-theory vacua. The group provides a precise reusable mechanism of composition within its stated representation assumptions."),
    ],
    "symmetry_in_quantum_mechanics": [
        ("p", r"A rotation of an isolated atom changes the description of its orientation while leaving transition probabilities unchanged. Such transformations act on quantum rays and are represented, under the hypotheses of Wigner's theorem, by unitary or antiunitary maps. Continuous transformations connected to the identity are represented unitarily; their generators turn an invariance of probabilities into a relation between operators."),
        ("p", r"Let a one-parameter symmetry be $U(\epsilon)=\exp(-i\epsilon G/\hbar)$, with self-adjoint generator $G$ and a parameter whose units make the exponent dimensionless. For a time-independent Hamiltonian, invariance under this group implies"),
        ("eq", r"""U(\epsilon)HU(\epsilon)^\dagger=H,
\qquad [G,H]=0,\qquad \frac{d}{dt}\langle G\rangle=0."""),
        ("p", r"The last equality follows from the Heisenberg equation when $G$ has no explicit time dependence and the operator domains permit the calculation. Spatial translations give momentum conservation; rotations give angular momentum conservation. A boundary or an external field can break the symmetry even if a local bulk term remains invariant. Conservation therefore belongs to the full physical problem."),
        ("p", r"Symmetry also controls which transitions can occur. Suppose parity $\Pi$ commutes with $H$ and two nondegenerate states have definite parities $\pi_i,\pi_f=\pm1$. Position is odd under parity. Inserting $\Pi^\dagger\Pi$ into its matrix element yields"),
        ("eq", r"""\langle f|X|i\rangle=-\pi_f\pi_i\langle f|X|i\rangle."""),
        ("p", r"The electric-dipole matrix element vanishes for states of the same parity. This is a selection rule for the pair consisting of the dynamics and the coupling to the probe. It can suppress a spectral line without creating an additional conserved quantity. Conversely, an accidental equality of two energy differences can merge lines without imposing any selection rule. These mechanisms must be distinguished when a spectral pattern simplifies."),
        ("p", r"For a proposed transfer between physical systems, a shared symmetry is useful because it restricts the admissible target interactions and observables. It does not determine their coupling constants or all matrix elements. The construction becomes predictive only after the target representation, Hamiltonian and measurement are fixed. Symmetry then supplies exact relations, such as forbidden transitions, that can test the proposed realization."),
    ],
    "heisenberg_picture": [
        ("p", r"The Schrödinger and Heisenberg pictures assign time dependence to different parts of the same prediction. With unitary evolution $U(t)$, an initial density operator $\rho_0$ and an observable $O$, the expectation can be evaluated either by evolving the state or by evolving the operator:"),
        ("eq", r"""\rho_S(t)=U(t)\rho_0U(t)^\dagger,\qquad
O_H(t)=U(t)^\dagger OU(t),\qquad
\operatorname{Tr}[\rho_S(t)O]=\operatorname{Tr}[\rho_0O_H(t)]."""),
        ("p", r"Differentiating $O_H$ for a time-independent Hamiltonian $H$ gives the Heisenberg equation:"),
        ("eq", r"""\dot O_H=\frac{i}{\hbar}[H,O_H]."""),
        ("p", r"The resulting commutators identify which other observables enter the prediction. This is particularly useful when an experiment observes only a small part of a many-body system."),
        ("p", r"Consider two spins with $H=\hbar g\,Z_1Z_2$, where $X_j,Y_j,Z_j$ denote dimensionless Pauli operators and $g$ is a frequency. If the measured quantity is $x=\langle X_1\rangle$, its derivative contains the correlation $c=\langle Y_1Z_2\rangle$. A second commutator closes the pair:"),
        ("eq", r"""\dot x=-2gc,\qquad \dot c=2gx,\qquad
x(t)=x(0)\cos(2gt)-c(0)\sin(2gt)."""),
        ("p", r"The correlation is physically necessary: preparations with the same initial transverse magnetization but different $c(0)$ give different later magnetizations. Its appearance is fixed by the interaction algebra. Retaining the two expectations supplies a complete closed prediction for this observable even though it does not reconstruct every entry of the two-spin density operator."),
        ("p", r"Eliminating the correlation replaces the pair of first-order equations by a history-dependent equation for $x$. The initial correlation survives as a separate term:"),
        ("eq", r"""\dot x(t)=-2g c(0)-4g^2\int_0^t x(s)\,ds."""),
        ("p", r"Both descriptions give the same signal when they use the same preparation. Discarding the integral or the initial-correlation term gives a different physical prediction. Repeated commutators thus provide a concrete way to construct the set of observables needed by a measurement, and to identify when a smaller description requires memory. For more complicated interactions the sequence may generate a much larger space rather than closing after two steps."),
    ],
    "pauli_matrices": [
        ("p", r"A two-level system has three independent traceless Hermitian observables. Choosing an orthonormal basis of states identifies them with the Pauli matrices. Their multiplication law determines rotations, transition amplitudes and the closure of equations for spin expectations:"),
        ("eq", r"""\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},"""),
        ("eq", r"""\sigma_i\sigma_j=\delta_{ij}I+i\sum_k\epsilon_{ijk}\sigma_k."""),
        ("p", r"For a unit vector $\mathbf n$, this identity gives $(\mathbf n\cdot\boldsymbol\sigma)^2=I$. Exponentiating a Hamiltonian proportional to that operator therefore separates into a cosine and a sine. The rotation of a spinor through angle $\theta$ is"),
        ("eq", r"""U(\theta)=e^{-i\theta\mathbf n\cdot\boldsymbol\sigma/2}
=\cos(\theta/2)I-i\sin(\theta/2)\mathbf n\cdot\boldsymbol\sigma."""),
        ("p", r"A full $2\pi$ rotation gives $-I$. This phase leaves an isolated spin probability unchanged, but becomes observable relative to a coherent reference branch that was not rotated. The Bloch vector itself completes one ordinary spatial rotation. The distinction between spinor amplitude and observable vector is the reason the half-angle appears."),
        ("p", r"Writing a two-level Hamiltonian as $H=E_0I+(\hbar/2)\boldsymbol\omega\cdot\boldsymbol\sigma$ and a state as $\rho=(I+\mathbf r\cdot\boldsymbol\sigma)/2$ gives $\dot{\mathbf r}=\boldsymbol\omega\times\mathbf r$. The identity term contributes only an overall phase, while the traceless part produces precession. The vector's length is conserved by this isolated unitary dynamics; relaxation requires an additional physical coupling."),
        ("p", r"For multiple spins, tensor products of Pauli matrices form an operator basis. Commuting a Hamiltonian with a one-spin observable can produce a two-spin product, showing how a local signal becomes coupled to a correlation. Counting the independent operators generated by those commutators measures the size of that particular observable dynamics. A reduction in this size can result from symmetry, selection rules or equal transition frequencies; the Pauli algebra permits these possibilities to be tested separately."),
    ],
    "angular_momentum_operator": [
        ("p", r"Rotations about different axes change orientation in an order-dependent way. In quantum mechanics their generators $J_x,J_y,J_z$ obey an algebra whose representations determine the allowed angular-momentum values. With $\hbar$ the reduced Planck constant,"),
        ("eq", r"""[J_i,J_j]=i\hbar\sum_k\epsilon_{ijk}J_k,\qquad
[J^2,J_i]=0,\qquad J^2=J_x^2+J_y^2+J_z^2."""),
        ("p", r"A simultaneous eigenstate of $J^2$ and $J_z$ can be labeled $|j,m\rangle$. Define $J_\pm=J_x\pm iJ_y$. Their commutators with $J_z$ show that they raise or lower its eigenvalue by $\hbar$, while preserving $j$. Positivity of the squared norms fixes the endpoints of the ladder:"),
        ("eq", r"""J^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,\qquad
J_z|j,m\rangle=\hbar m|j,m\rangle,"""),
        ("eq", r"""J_\pm|j,m\rangle=\hbar\sqrt{j(j+1)-m(m\pm1)}\,|j,m\pm1\rangle."""),
        ("p", r"The ladder terminates at $m=\pm j$, giving $2j+1$ states. Single-valued orbital wave functions on ordinary three-dimensional space carry integer orbital angular momentum. Intrinsic spin uses representations of the covering group SU(2), allowing half-integer $j$. The same local commutator algebra is therefore realized on carriers with different global transformation properties."),
        ("p", r"For two spins, total angular momentum is $\mathbf J=\mathbf J_1+\mathbf J_2$. An isotropic exchange interaction can be rewritten using the total Casimir:"),
        ("eq", r"""H=\frac{K}{\hbar^2}\mathbf J_1\cdot\mathbf J_2
=\frac{K}{2\hbar^2}(J^2-J_1^2-J_2^2)."""),
        ("p", r"Here $K$ is an energy. Two spin-one-half particles then have a singlet energy $-3K/4$ and a triplet energy $K/4$. The gap is fixed by the coupling and the representation, without diagonalizing a general four-dimensional matrix. A magnetic field separates magnetic sublevels; an anisotropic interaction can also mix sectors that the isotropic model kept separate."),
        ("p", r"This calculation connects symmetry to a measurable excitation energy. Transferring the exchange formula to another object requires identifying which angular-momentum representation its degrees of freedom carry and whether anisotropy, orbital coupling or the environment changes the generator. A common algebra supplies the ladder relations, while the Hamiltonian selects which of those states a physical system occupies."),
    ],
    "quantum_jump": [
        ("p", r"A fluorescence detector records discrete photons, whereas an unobserved excited atom is often described by a smoothly decaying density operator. These descriptions refer to different information about the same atom and its radiation field. Conditioning on the detection record gives quantum trajectories; averaging over records recovers the master equation."),
        ("p", r"For Hamiltonian $H$ and monitored decay operators $L_k$, assume a Markovian reservoir and time-independent detection channels. In a short interval $dt$, the no-count operator $M_0$ and the count operators $M_k$ are"),
        ("eq", r"""M_0=I-\frac{iH\,dt}{\hbar}-\frac{dt}{2}\sum_kL_k^\dagger L_k,
\qquad M_k=\sqrt{dt}\,L_k."""),
        ("p", r"They satisfy $\sum_{k\geq0}M_k^\dagger M_k=I+O(dt^2)$. The probability of a count in channel $k$ is $dt\,\operatorname{Tr}(L_k^\dagger L_k\rho)$; the state after that count is $L_k\rho L_k^\dagger$ divided by its trace. Even the absence of a count changes the conditioned state, because it supplies information about its excited-state population."),
        ("eq", r"""\dot\rho=-\frac{i}{\hbar}[H,\rho]+\sum_k
\left(L_k\rho L_k^\dagger-\frac12\{L_k^\dagger L_k,\rho\}\right)."""),
        ("p", r"This equation follows by summing the unnormalized states for all outcomes, expanding to first order in $dt$ and subtracting the previous density operator. It is the ensemble prediction, not one particular observed sequence. For a two-level atom with $L=\sqrt{\gamma}|g\rangle\langle e|$, no drive and an initially excited state, the survival probability is $e^{-\gamma t}$ and the first-photon waiting-time density is $\gamma e^{-\gamma t}$."),
        ("p", r"Changing the measurement of the outgoing field can change the conditioned trajectories while leaving the ensemble master equation unchanged. Direct photon counting gives jumps; quadrature detection gives a continuous noisy record. Consequently a trajectory belongs to the atom-field dynamics together with the measurement, not to the reduced Hamiltonian alone."),
        ("p", r"Finite efficiency separates the decay operator into observed and unobserved channels. A missed photon still affects the atom, but does not produce an observed jump. Feedback adds a further dependence: the detector record controls a subsequent Hamiltonian or operation. A mechanism assembled from decay, observation and feedback must retain these distinctions to predict both the mean population and the distribution of individual records."),
    ],
    "quantum_amplifier": [
        ("p", r"An amplifier that increases both quadratures of a bosonic signal must also introduce fluctuations. Let $a$ be the input annihilation operator, with $[a,a^\dagger]=1$, and let $G>1$ be the intensity gain. Multiplying $a$ by $\sqrt G$ alone would make the output commutator equal to $G$, so it cannot describe an output mode with the original normalization."),
        ("p", r"A second, independent mode $b$ supplies the required additional degree of freedom. The phase-insensitive amplification relation is"),
        ("eq", r"""a_{\rm out}=\sqrt G\,a_{\rm in}+\sqrt{G-1}\,b_{\rm in}^\dagger,
\qquad [a_{\rm out},a_{\rm out}^\dagger]=G-(G-1)=1."""),
        ("p", r"The creation operator has the opposite commutator sign, exactly compensating the excess from the amplified signal. A parametric interaction realizes this transformation by producing correlated excitations in a signal and an idler. Energy is supplied by a pump; the idler is a physical channel rather than an adjustable numerical correction."),
        ("p", r"Define $X=(a+a^\dagger)/\sqrt2$ and $P=(a-a^\dagger)/(i\sqrt2)$, so vacuum has variance $1/2$ in each quadrature. For uncorrelated inputs and a vacuum idler,"),
        ("eq", r"""\operatorname{Var}X_{\rm out}=G\operatorname{Var}X_{\rm in}+\frac{G-1}{2},
\qquad \langle n_{\rm out}\rangle=G\langle n_{\rm in}\rangle+G-1."""),
        ("p", r"The second expression includes spontaneous output even for vacuum signal input. Referring the quadrature noise back to the input gives an added variance $(G-1)/(2G)$, approaching half a quantum at large gain. A thermally occupied idler adds still more noise. The commutator determines the necessary channel, while its state determines how much fluctuation that channel contributes."),
        ("p", r"A phase-sensitive amplifier follows a different relation: one quadrature is stretched and the conjugate one is compressed, preserving their commutator without amplifying both equally. It can amplify a known quadrature without the same added-noise bound. Thus the bound is attached to a specific physical task, not to every process called amplification."),
        ("p", r"This is an explicit construction from a failed relation. The proposed gain-only map has a nonzero commutator defect; adding an independent idler with the appropriate coefficient restores the algebra and predicts the noise. The correction is already established quantum optics. Its value here is that every additional ingredient changes a calculable experimental consequence."),
    ],
    "quantum_error_correction": [
        ("p", r"A quantum memory must distinguish errors without measuring the unknown logical amplitudes it is intended to preserve. The state is encoded into a subspace in which different correctable errors leave distinguishable information in auxiliary degrees of freedom, while their probabilities reveal no logical-state information."),
        ("p", r"Let $P$ project onto the code subspace and let $E_a$ be the error operators in a specified noise model. Exact correction of their linear span is possible when there is a matrix $c$ such that"),
        ("eq", r"""P E_a^\dagger E_b P=c_{ab}P."""),
        ("p", r"The right side is proportional to the identity within the code. Thus overlaps of the error-affected states depend on the error labels, but not on which logical superposition was stored. Diagonalizing $c$ organizes the error spaces so that a measurement can identify the required correction without resolving the encoded state."),
        ("p", r"For a simple illustration, encode $\alpha|0\rangle+\beta|1\rangle$ as $\alpha|000\rangle+\beta|111\rangle$ and consider at most one bit flip. The commuting observables $Z_1Z_2$ and $Z_2Z_3$ give four distinct syndromes:"),
        ("eq", r"""\begin{array}{c|rrrr}
\text{error}&I&X_1&X_2&X_3\\\hline
(Z_1Z_2,Z_2Z_3)&(+,+)&(-,+)&(-,-)&(+,-)
\end{array}"""),
        ("p", r"Both basis codewords have the same syndrome before an error. The syndrome measurement therefore preserves their coherence. Applying the indicated bit flip restores the encoded state for any $\alpha$ and $\beta$. Measuring the individual $Z_j$ instead would reveal which codeword was present and destroy an unknown superposition."),
        ("p", r"The noise specification matters. A phase flip acts within this code as a logical error and is not identified by those two syndromes. Protecting arbitrary single-qubit errors requires additional structure, such as a code that corrects both bit and phase errors. Increasing the number of spins without changing the encoded subspace and syndrome observables does not automatically supply that protection."),
        ("p", r"Error correction connects interaction, preparation, measurement and conditional dynamics in one mechanism. The environment determines the error operators; encoding determines the carrier subspace; syndrome extraction determines what information becomes observable; and the conditional operation restores the logical state. The algebraic correction condition is an exact test of this assembly. Fault tolerance adds another problem: the physical operations used to extract a syndrome can themselves propagate errors, so those operations must be analyzed as part of the noise model."),
    ],
    "quantum_teleportation": [
        ("p", r"An unknown qubit can be transferred using a shared entangled pair and two classical bits. The entangled resource alone does not transmit a usable signal: a joint measurement at the sender and a correction conditioned on its outcome are essential parts of the mechanism."),
        ("p", r"Let the input be $|\psi\rangle=a|0\rangle+b|1\rangle$ and let the shared pair be $|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2$, with the second member held by the receiver. Define the Bell states $|B_{mn}\rangle=(I\otimes X^nZ^m)|\Phi^+\rangle$, where $m,n\in\{0,1\}$. Expansion in this joint basis gives"),
        ("eq", r"""|\psi\rangle_1|\Phi^+\rangle_{23}
=\frac12\sum_{m,n=0}^{1}|B_{mn}\rangle_{12}\,X^nZ^m|\psi\rangle_3."""),
        ("p", r"Each Bell outcome has probability one quarter, independent of the input amplitudes. Once the sender communicates $m,n$, the receiver applies $Z^mX^n$ and obtains the original state. The measurement determines a known transformation of the state, rather than its unknown amplitudes. This is why transmitting two classical bits suffices when the entangled pair has already been supplied."),
        ("p", r"Without the outcome record the receiver averages the four possible transformed states. For any input density operator $\rho$, that average is"),
        ("eq", r"""\frac14\sum_{m,n}X^nZ^m\rho Z^mX^n=\frac I2."""),
        ("p", r"The receiver's local statistics then contain no dependence on the input. The same calculation establishes that the protocol cannot be used for faster-than-light signalling. The original input has participated in a destructive joint measurement, so the transfer does not create two independently available copies."),
        ("p", r"A nonideal entangled resource changes the resulting channel. For a Bell-diagonal resource, its Bell weights become probabilities of Pauli errors in the corrected output. Resource quality, Bell-measurement fidelity and the conditional correction can therefore be distinguished experimentally; all three can reduce the final state fidelity, but they enter the calculation at different steps."),
        ("p", r"Teleportation illustrates how a mechanism can be transferred across physical carriers. Photonic polarization, internal atomic levels and superconducting circuits may realize the same qubit relation, provided their entangling resource, joint measurement and correction implement the required maps. Changing only the name of the carrier leaves those requirements unresolved; demonstrating the maps establishes the actual correspondence."),
    ],
    "quantum_metrology": [
        ("p", r"A sensor estimates a physical parameter from how that parameter changes a prepared state. Sensitivity depends on the interaction that encodes the parameter, on the fluctuations of its generator in the preparation, and on the measurement used to distinguish nearby states. Entanglement is useful only when it improves this complete estimation problem."),
        ("p", r"Let a dimensionless parameter $\theta$ be encoded by $|\psi_\theta\rangle=e^{-i\theta G}|\psi_0\rangle$, with Hermitian dimensionless generator $G$. For this pure-state unitary family, the quantum Fisher information is"),
        ("eq", r"""F_Q=4(\langle G^2\rangle-\langle G\rangle^2),\qquad
\operatorname{Var}\widehat\theta\geq\frac{1}{\nu F_Q}."""),
        ("p", r"Here $\nu$ counts independent repetitions and the bound applies to locally unbiased estimation, with attainability requiring a suitable measurement and statistical regime. Large generator variance makes neighboring parameter-dependent states more distinguishable. A state that is an eigenstate of $G$ acquires only an overall phase and has no sensitivity to $\theta$ in this task."),
        ("p", r"For $N$ spins exposed to the same phase, choose $G=\tfrac12\sum_j Z_j$. Independent spins prepared along $x$ have $F_Q=N$. The coherent superposition $(|0\rangle^{\otimes N}+|1\rangle^{\otimes N})/\sqrt2$ has $F_Q=N^2$, because the two components acquire phases separated by $N\theta$."),
        ("eq", r"""\Delta\theta_{\rm product}\geq\frac{1}{\sqrt{\nu N}},\qquad
\Delta\theta_{\rm GHZ}\geq\frac{1}{N\sqrt\nu}."""),
        ("p", r"These expressions compare the same single-spin coupling with a counted number of uses. They are not universal bounds for arbitrary many-body Hamiltonians or uncounted preparation resources. The enhanced oscillation also creates phase ambiguities over a broad prior interval, so an estimation scheme must establish which fringe contains the parameter."),
        ("p", r"Independent dephasing exposes the cost of the collective coherence. If a single-spin off-diagonal element decays as $e^{-\gamma t}$, the coherence between the two GHZ branches decays as $e^{-N\gamma t}$. For phase encoding over a fixed duration this gives $F_Q=N^2e^{-2N\gamma t}$. Increasing $N$ can then reduce rather than improve the usable information. Optimizing frequency estimation further requires counting the interrogation time and available repetitions."),
        ("p", r"A proposed sensing mechanism must therefore specify what is being estimated and which resources are fixed. The generator identifies the useful preparation, while environmental coupling and measurement determine how much of its distinguishability is available. This makes sensitivity a calculable property of the assembled experiment rather than a consequence of entanglement alone."),
    ],
    "quantum_key_distribution": [
        ("p", r"Quantum key distribution creates correlated classical data whose secrecy is inferred from a specified quantum communication model. Its physical basis is that information about nonorthogonal signal states cannot be acquired perfectly while leaving those states unchanged. The task is key generation, not the transmission of an encrypted message or the authentication of an unknown partner."),
        ("p", r"In ideal BB84 the sender chooses between the eigenstates of $Z$ and $X$. Write $|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2$. Suppose an eavesdropper's unitary interaction preserves both $|0\rangle$ and $|1\rangle$ while recording them in probe states $|e_0\rangle$ and $|e_1\rangle$. Linearity then requires"),
        ("eq", r"""|+\rangle|e\rangle\longmapsto
\frac{|0\rangle|e_0\rangle+|1\rangle|e_1\rangle}{\sqrt2}."""),
        ("p", r"The signal remains a pure $|+\rangle$ only when the two probe states coincide up to the phase compatible with the signal. Distinguishable probe records suppress its off-diagonal coherence. A check in the complementary basis can therefore detect the disturbance associated with that information gain."),
        ("p", r"After transmission, the legitimate parties disclose their basis choices, retain the compatible outcomes and estimate an error rate from a random sample. Classical error correction reconciles their strings and privacy amplification reduces the information that may remain with an adversary. For the ideal asymptotic single-photon BB84 setting with the relevant bit and phase error rates both bounded by $Q$, the one-way secret fraction per sifted bit has the familiar form"),
        ("eq", r"""r\geq1-2h_2(Q),\qquad
h_2(Q)=-Q\log_2Q-(1-Q)\log_2(1-Q)."""),
        ("p", r"This expression is tied to its security model. Finite data require statistical confidence terms; multiphoton emission, detector imperfections and information disclosed during reconciliation require explicit treatment. An observed low bit-error rate alone does not establish secrecy for an arbitrary device. Loss and source statistics can carry information that a two-level idealization omits."),
        ("p", r"The classical channel must be authenticated. Otherwise an adversary can impersonate each party in a separate quantum exchange. The quantum mechanism supplies a relation between information and disturbance under stated source and measurement assumptions; authentication supplies the identity of the parties using that relation. Keeping these contributions distinct is necessary to transfer a security argument from an ideal qubit model to an optical implementation."),
    ],
    "quantum_harmonic_oscillator": [
        ("p", r"Small oscillations about a stable equilibrium have a quadratic energy. Quantizing that local approximation produces equally spaced excitations and a nonzero ground-state variance. For mass $m$, angular frequency $\omega>0$, position $X$ and momentum $P$, take"),
        ("eq", r"""H=\frac{P^2}{2m}+\frac12m\omega^2X^2,\qquad
a=\sqrt{\frac{m\omega}{2\hbar}}X+\frac{iP}{\sqrt{2m\hbar\omega}}."""),
        ("p", r"The canonical commutator gives $[a,a^\dagger]=1$. Substituting $a$ and $a^\dagger$ into the energy leaves an additive term from their noncommutation:"),
        ("eq", r"""H=\hbar\omega\left(a^\dagger a+\frac12\right),\qquad
E_n=\hbar\omega\left(n+\frac12\right)."""),
        ("p", r"Positivity of $a^\dagger a$ bounds the energy below. Repeated lowering reaches a state annihilated by $a$; raising generates the nonnegative integer occupations. The half-quantum is consequently fixed by the operator algebra. It is not a fitted offset introduced to match a spectrum."),
        ("p", r"The ground state has position variance $\hbar/(2m\omega)$ and momentum variance $m\hbar\omega/2$. Their product saturates the preparation uncertainty relation. Displacing that state changes the mean position and momentum while leaving the variances fixed. Under the harmonic Hamiltonian, those means obey the classical oscillator equation, even though the state retains quantum fluctuations."),
        ("eq", r"""X(t)=X(0)\cos\omega t+\frac{P(0)}{m\omega}\sin\omega t."""),
        ("p", r"The equation is an operator identity. Taking expectations gives the classical motion of the center; taking products gives correlations and variances. A thermal mixture has zero mean displacement but fluctuating energy and a larger position variance. A squeezed state instead redistributes variance between the two quadratures, and that anisotropy rotates in phase space."),
        ("p", r"The same construction describes a normal mode of a vibrating solid or electromagnetic cavity after its generalized coordinate, conjugate momentum and normalization have been identified. The material and boundary conditions determine the frequency and mode shape. Anharmonic interactions couple modes or shift their spacing, while damping adds an environment and its fluctuations. The oscillator is therefore a transferable quadratic mechanism, not an assertion that all its realizations have identical lifetimes, couplings or measurement units."),
        ("p", r"For a finite matrix truncation, the highest retained state breaks the exact ladder algebra. This can be checked directly rather than interpreted as a physical correction. Predictions for low occupations converge as the truncation is enlarged; strong driving that reaches the cutoff requires a larger state space."),
    ],
    "quantum_statistical_mechanics": [
        ("p", r"Thermal equilibrium assigns probabilities to quantum energy states while respecting the quantities that can be exchanged with the surroundings. For a system that exchanges energy with a large reservoir at temperature $T$ but has fixed particle number, the canonical state is determined by the Hamiltonian $H$:"),
        ("eq", r"""\rho_\beta=\frac{e^{-\beta H}}{Z},\qquad
Z=\operatorname{Tr}e^{-\beta H},\qquad \beta=(k_BT)^{-1}."""),
        ("p", r"The trace sums over the actual many-particle state space, including exchange statistics and boundary conditions. It is not an independent classical distribution imposed on particle positions. Derivatives of the same partition function connect average energy and fluctuations:"),
        ("eq", r"""\langle H\rangle=-\partial_\beta\log Z,\qquad
\operatorname{Var}H=\partial_\beta^2\log Z,\qquad
C=\frac{\operatorname{Var}H}{k_BT^2}."""),
        ("p", r"The last equality holds for a temperature-independent Hamiltonian in the canonical ensemble. It explains why equilibrium energy fluctuations measure the heat capacity: both are responses of the same probability weights to temperature. A different ensemble constrains different fluctuations and must be analyzed separately."),
        ("p", r"For independent modes of energy $\epsilon$ exchanging particles with a reservoir at chemical potential $\mu$, set $z=\exp[-\beta(\epsilon-\mu)]$. A fermionic mode contributes $1+z$ to the grand partition function because only occupations zero and one are allowed. A bosonic mode contributes the geometric sum $(1-z)^{-1}$ when $z<1$. Differentiation gives"),
        ("eq", r"""\overline n_F=\frac{1}{e^{\beta(\epsilon-\mu)}+1},\qquad
\overline n_B=\frac{1}{e^{\beta(\epsilon-\mu)}-1}."""),
        ("p", r"The sign difference follows from the allowed state occupations. It produces Fermi filling and Bose enhancement before a specific interaction is added. In the dilute limit both expressions approach the Maxwell--Boltzmann weight. Interactions generally prevent factorization into independent mode contributions, although an effective quasiparticle description may recover it approximately."),
        ("p", r"For a single harmonic mode, the same sum gives $Z=[2\sinh(\beta\hbar\omega/2)]^{-1}$ and mean energy $(\hbar\omega/2)\coth(\beta\hbar\omega/2)$. The mean approaches the zero-point energy as temperature tends to zero; quadrature fluctuations persist while the energy variance vanishes. At high temperature the mean energy approaches $k_BT$. This links the oscillator algebra to thermodynamic response through the choice of preparation."),
        ("p", r"Equilibrium statistics do not specify the rate of approach to equilibrium. Relaxation requires dynamics, reservoir coupling and sometimes additional conserved quantities. A Gibbs state can describe stationary observables while giving no information about a transport coefficient or memory time. Constructing those predictions requires extending the equilibrium description by the corresponding physical evolution."),
    ],
}

# References locate the established framework; the worked calculations above
# are authored here and tested independently where finite symbolic checks apply.
REFERENCES = {slug: [("1508.06951", "V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; states, operators and symmetry.")]
              for slug in ["quantum_state", "two_state_quantum_system", "fourier_transform", "spectral_theory", "canonical_commutation_relation", "heisenberg_group", "symmetry_in_quantum_mechanics", "heisenberg_picture", "pauli_matrices", "angular_momentum_operator"]}
REFERENCES.update({
    "quantum_jump": [("quant-ph/9702007", "M. B. Plenio and P. L. Knight, The Quantum Jump Approach to Dissipative Dynamics in Quantum Optics; conditional and ensemble evolution.")],
    "quantum_amplifier": [("1110.3234", "C. Weedbrook and colleagues, Gaussian Quantum Information; Gaussian channels and amplification.")],
    "quantum_error_correction": [("quant-ph/9705052", "D. Gottesman, Stabilizer Codes and Quantum Error Correction; error correction conditions and syndrome measurements.")],
    "quantum_teleportation": [("quant-ph/9705052", "D. Gottesman, Stabilizer Codes and Quantum Error Correction; entanglement, measurements and teleportation."), ("1110.3234", "C. Weedbrook and colleagues, Gaussian Quantum Information; continuous-variable realizations and finite-resource effects.")],
    "quantum_metrology": [("quant-ph/0509179", "V. Giovannetti, S. Lloyd and L. Maccone, Quantum metrology; generator fluctuations and counted resources.")],
    "quantum_key_distribution": [("0802.4155", "V. Scarani and colleagues, The Security of Practical Quantum Key Distribution; ideal protocols, device assumptions and security bounds.")],
    "quantum_harmonic_oscillator": [("1110.3234", "C. Weedbrook and colleagues, Gaussian Quantum Information; canonical quadratures, Gaussian states and transformations.")],
    "quantum_statistical_mechanics": [("0706.3360", "S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold atomic Fermi gases; ideal and interacting quantum gases.")],
})
