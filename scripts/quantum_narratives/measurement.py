"""Measurement topics: Bell, Born rule, measurement models, POVM and PVM, erasers, EPR, collapse, duality, imaging, electron microscope."""

NARRATIVES = {
    "bell_s_theorem": [
        ("p", r"Two spin-1/2 particles leave a common source in opposite directions. Each meets a Stern--Gerlach magnet whose orientation is chosen at random just before arrival, and each detector records $+1$ or $-1$. Bell asked whether the correlations of these records can be produced by properties fixed at the source together with the local settings alone."),
        ("p", r"Let each pair carry a variable $\lambda$ with distribution $\rho(\lambda)$. A local model gives outcomes $A_a(\lambda)=\pm1$ and $B_b(\lambda)=\pm1$, where $A$ does not depend on the distant setting $b$ and $\rho$ depends on neither setting. With two settings per side, one bracket below vanishes and the other equals $\pm2$ for every pair:"),
        ("eq", r"""S_\lambda=A_a(B_b+B_{b'})+A_{a'}(B_b-B_{b'})=\pm2\\
|E(a,b)+E(a,b')+E(a',b)-E(a',b')|\leq2"""),
        ("p", r"Here $E(a,b)$ is the average of $A_aB_b$ over $\lambda$. Random local responses do not help, because they are mixtures of deterministic ones and the bound is linear in the probabilities. This is the Clauser--Horne--Shimony--Holt (CHSH) inequality."),
        ("p", r"For the spin singlet, quantum mechanics gives $E(a,b)=-\cos(\theta_a-\theta_b)$, with $\theta$ the magnet angle in a common plane. The angles $0^\circ$ and $90^\circ$ on one side, with $45^\circ$ and $-45^\circ$ on the other, give $|S|=4/\sqrt2=2\sqrt2\approx2.83$."),
        ("p", r"No quantum state and no choice of $\pm1$ observables does better. For the Bell operator $\mathcal B=A\otimes(B+B')+A'\otimes(B-B')$, squaring and using $A^2=B^2=I$ gives"),
        ("eq", r"""\mathcal B^2=4I-[A,A']\otimes[B,B'],\qquad
|\langle\mathcal B\rangle|\leq2\sqrt2."""),
        ("p", r"Each commutator has norm at most 2, so no eigenvalue of $\mathcal B^2$ exceeds 8. This is the Tsirelson bound. It also shows that a violation requires noncommuting settings on both sides; commuting pairs return the classical value 2. If the singlet is mixed with white noise so that correlations shrink by a factor $v$, then $S=2\sqrt2\,v$ and a violation requires $v>1/\sqrt2$."),
        ("p", r"An experiment must also close two gaps in the derivation. If detectors miss many particles, the detected subset may be unrepresentative; for a maximally entangled state the CHSH test needs efficiency above $2(\sqrt2-1)\approx0.83$. If one setting can influence the distant detector before its record is final, a local signal could fix the correlations. The settings must also be statistically independent of $\lambda$."),
        ("p", r"In 2015 Hensen and colleagues entangled electron spins in two diamond defects 1.3 km apart. Settings were chosen randomly and each spin was measured within the light travel time between the sites. In 245 heralded trials, each giving an outcome at both sites, they found $S=2.42\pm0.20$. Photon experiments in Vienna and Boulder closed both gaps in the same year."),
        ("p", r"The theorem constrains local models of the records; it does not modify quantum mechanics. The Einstein--Podolsky--Rosen argument, which motivated it, used predictions with certainty; quantum nonlocality extends the comparison to three particles without an inequality. Device-independent quantum key distribution uses the observed value of $S$ to bound an eavesdropper's information."),
    ],
    "born_rule": [
        ("p", r"A spin prepared up along $z$ enters a Stern--Gerlach magnet tilted by an angle $\theta$. Each atom lands in one of two spots. Over many atoms, the fraction in the upper spot approaches $\cos^2(\theta/2)$, although no single run reveals that number."),
        ("p", r"The spin state up along the tilted axis $\mathbf n$ is $\cos(\theta/2)|{\uparrow}\rangle+\sin(\theta/2)|{\downarrow}\rangle$. Its inner product with the prepared state is the amplitude $\cos(\theta/2)$, and the Born rule assigns probability equal to its squared modulus. For a density operator $\rho$ and an outcome projector $P_k$ the same rule reads"),
        ("eq", r"""p_+=|\langle{+_{\mathbf n}}|{\uparrow_z}\rangle|^2=\cos^2\frac{\theta}{2},\qquad
p(k)=\operatorname{Tr}(\rho P_k)."""),
        ("p", r"The rule refers to relative frequencies in repeated, identically prepared runs. For $N$ independent atoms the observed fraction scatters about $p$ with standard deviation $\sqrt{p(1-p)/N}$. At $\theta=120^\circ$, $p=1/4$, and $10^4$ atoms fix the fraction to about $\pm0.004$. Comparing such fractions at many angles tests the rule, provided detector efficiency and background are calibrated independently."),
        ("p", r"The squared modulus is not an arbitrary choice. Gleason's theorem states that, in a space of dimension three or more, any assignment of probabilities to projectors must take the form $\operatorname{Tr}(\rho P)$. The assumption is that probabilities add over mutually orthogonal projectors and do not depend on which other projectors are measured alongside. The rule thus follows from the projector structure and this additivity, not from the Schrödinger equation."),
        ("p", r"A sharp consequence concerns interference among more than two paths. Let $a$, $b$ and $c$ be the amplitudes at one screen point from three slits $A$, $B$ and $C$. Write $P_{AB}$ for the probability with slits $A$ and $B$ open, and so on. Expanding the squared moduli gives"),
        ("eq", r"""|a+b+c|^2=|a|^2+|b|^2+|c|^2+2\operatorname{Re}(a^*b+b^*c+a^*c),\\
I_3=P_{ABC}-P_{AB}-P_{BC}-P_{AC}+P_A+P_B+P_C=0."""),
        ("p", r"Every cross term appears once in $P_{ABC}$ and once in a two-slit pattern, so the combination $I_3$ cancels identically. A rule in which probability were a higher power of the amplitude would leave a third-order interference term. Sinha and colleagues measured the patterns for every combination of open slits, using single photons and three slits. They bounded the three-path term below one percent of the two-path interference."),
        ("p", r"The cancellation assumes that opening a slit only adds an amplitude. Near-field paths that loop between neighbouring open slits violate this assumption slightly. Within ordinary quantum mechanics they produce a small nonzero $I_3$, which precise tests must subtract."),
        ("p", r"For unsharp detectors the projector is replaced by a positive effect, as described under POVM. The sharp case, with orthogonal projectors that sum to the identity, is described under projection-valued measure. Wave interference supplies the amplitudes; the Born rule converts them into counting rates."),
    ],
    "measurement_in_quantum_mechanics": [
        ("p", r"A Stern--Gerlach magnet sends silver atoms up or down according to their spin, and a screen records where each atom lands. The spin is never observed directly. It is inferred from a position that the magnet has correlated with it."),
        ("p", r"Von Neumann's model makes this correlation explicit. Let the measured observable be $A=\sum_aa|a\rangle\langle a|$, and let a pointer have position $q$, momentum $p_q$ and initial wave function $\phi(q)$ of width $\sigma$. A brief interaction $H=g(t)A\otimes p_q$ with total strength $G=\int g\,dt$ translates the pointer by an amount proportional to the eigenvalue:"),
        ("eq", r"""e^{-iGA\otimes p_q/\hbar}\sum_ac_a|a\rangle\phi(q)
=\sum_ac_a|a\rangle\phi(q-Ga)."""),
        ("p", r"Finding the pointer at $q$ then has probability density $\sum_a|c_a|^2|\phi(q-Ga)|^2$, a sum of displaced pointer profiles. When $G$ times the eigenvalue spacing greatly exceeds $\sigma$, the peaks separate and outcome $a$ occurs with probability $|c_a|^2$. When the peaks overlap, the record yields only partial information about $A$. The corresponding effects $\sum_a|\phi(q-Ga)|^2|a\rangle\langle a|$ form a POVM rather than a set of projectors."),
        ("p", r"The same coupling disturbs the system. Tracing over the pointer multiplies each coherence $\rho_{aa'}$ of the system by the overlap of the two displaced pointer states. For a Gaussian pointer,"),
        ("eq", r"""\rho_{aa'}\;\longmapsto\;\rho_{aa'}\exp\!\left[-\frac{G^2(a-a')^2}{8\sigma^2}\right]."""),
        ("p", r"Resolution and disturbance are therefore controlled by the same ratio $G|a-a'|/\sigma$. A pointer that separates two eigenvalues cleanly removes the coherence between them, and with it the interference that observables not commuting with $A$ would show. The diagonal elements are untouched because the interaction commutes with $A$. This is the quantum nondemolition condition: an immediate repetition returns the same eigenvalue."),
        ("p", r"In the Stern--Gerlach magnet, the field gradient $B'$ couples the spin component $\sigma_z$ to the transverse position $z$ through the energy $\mu_BB'z\sigma_z$, with $\mu_B$ the Bohr magneton. The pointer is the transverse momentum, shifted by $\pm\mu_BB'\tau$ during the transit time $\tau$. For silver atoms at 500 m/s in a 3.5 cm magnet with $B'=10^3$ T/m, the two components separate by about 0.25 mm at the exit. This is comparable to the splitting seen in 1922."),
        ("p", r"The momentum kick far exceeds the momentum spread of a collimated beam. The interference between the spin components is therefore lost, and restoring it would require undoing the kick to within that spread. The update that follows a recorded outcome is discussed under wave function collapse. Continuous monitoring of an emitting atom, in which the pointer is the radiation field, leads to the quantum jump description."),
    ],
    "measurement_problem": [
        ("p", r"A detector whose pointer can swing left or right interacts with a spin prepared in a superposition of up and down. Linear quantum dynamics applied to spin and detector predicts a superposition of both pointer positions. Each actual run shows one."),
        ("p", r"Suppose the detector works correctly on the basis states. Starting in a ready state $|A_0\rangle$, the interaction $U$ produces $|{\uparrow}\rangle|A_\uparrow\rangle$ from $|{\uparrow}\rangle|A_0\rangle$ and $|{\downarrow}\rangle|A_\downarrow\rangle$ from $|{\downarrow}\rangle|A_0\rangle$. Linearity then fixes its action on any superposition:"),
        ("eq", r"""U(\alpha|{\uparrow}\rangle+\beta|{\downarrow}\rangle)|A_0\rangle
=\alpha|{\uparrow}\rangle|A_\uparrow\rangle+\beta|{\downarrow}\rangle|A_\downarrow\rangle."""),
        ("p", r"Adding an observer, a camera or a printer extends this correlation to more systems without ending it. The Born rule assigns the probabilities $|\alpha|^2$ and $|\beta|^2$, but the evolution contains no step at which one term is selected."),
        ("p", r"Decoherence explains part of what is seen. Air molecules and thermal photons scatter from the pointer and acquire states that depend on its position. With environment states $|E_\uparrow\rangle$ and $|E_\downarrow\rangle$, the reduced state of spin and pointer becomes"),
        ("eq", r"""\rho_{SA}=|\alpha|^2|{\uparrow}A_\uparrow\rangle\langle{\uparrow}A_\uparrow|
+|\beta|^2|{\downarrow}A_\downarrow\rangle\langle{\downarrow}A_\downarrow|\\
+\left(\alpha\beta^*\Gamma|{\uparrow}A_\uparrow\rangle\langle{\downarrow}A_\downarrow|+{\rm h.c.}\right),
\qquad \Gamma=\langle E_\downarrow|E_\uparrow\rangle."""),
        ("p", r"If $N$ independent scatterers each leave states with overlap $c$, then $\Gamma=c^N$. With $c=\cos0.1\approx0.995$ and $N=10^4$, $|\Gamma|\approx2\times10^{-22}$, so interference between pointer positions cannot be detected on spin and pointer alone. The pointer basis is selected by the interaction, here position, because scattering depends on where the pointer is."),
        ("p", r"Decoherence does not select an outcome. The global state still contains both terms, and $\rho_{SA}$ is a reduced description of an entangled state, not a list of which outcome occurred. The measurement problem is that unitary evolution alone yields neither single records nor their probabilities; both enter as separate assumptions. Interpretations divide on how to supply the missing step: by keeping all branches, by adding particle positions, or by changing the dynamics."),
        ("p", r"The last option makes predictions. In the Ghirardi--Rimini--Weber model each nucleon is spontaneously localized to a length $r_C\approx10^{-7}$ m at a rate $\lambda\approx10^{-16}$ s$^{-1}$. For a pointer whose $N$ nucleons are displaced by more than $r_C$, one localization of any nucleon collapses the whole superposition:"),
        ("eq", r"""\Gamma_{\rm collapse}=N\lambda\approx10^{23}\times10^{-16}\,{\rm s^{-1}}=10^{7}\,{\rm s^{-1}}."""),
        ("p", r"A single nucleon is localized about once in $3\times10^8$ years, while a macroscopic pointer resolves within 0.1 microsecond. The modified dynamics also predicts slight heating and spontaneous radiation. Interferometry with massive molecules and searches for this radiation bound $\lambda$ at each $r_C$. Current upper bounds on $\lambda$ at $r_C=10^{-7}$ m remain above the original value, so the model is constrained but not excluded. Schrödinger's cat poses the same problem for a larger system."),
    ],
    "povm": [
        ("p", r"A photon arrives polarized either horizontally or diagonally, with equal probability. The two states are not orthogonal, so no measurement identifies them every time without error. A measurement can nevertheless be built that never errs and sometimes declares the result inconclusive."),
        ("p", r"Write the states as $|\psi_0\rangle$ and $|\psi_1\rangle$ with phases chosen so that $s=\langle\psi_0|\psi_1\rangle$ is real and positive. Let $|\psi_j^\perp\rangle$ be the state orthogonal to $|\psi_j\rangle$. A measurement with three outcomes is defined by the positive operators"),
        ("eq", r"""E_0=\frac{|\psi_1^\perp\rangle\langle\psi_1^\perp|}{1+s},\qquad
E_1=\frac{|\psi_0^\perp\rangle\langle\psi_0^\perp|}{1+s},\qquad
E_?=I-E_0-E_1."""),
        ("p", r"Outcome 0 never occurs for $|\psi_1\rangle$, and outcome 1 never occurs for $|\psi_0\rangle$. The prefactor $1/(1+s)$ is the largest value that keeps $E_?$ positive; its smaller eigenvalue then vanishes. Each state is identified with probability $|\langle\psi_0|\psi_1^\perp\rangle|^2/(1+s)=1-s$. This is the Ivanovic--Dieks--Peres limit, optimal for equal prior probabilities."),
        ("p", r"For horizontal and diagonal polarization, $s=1/\sqrt2$ and the success probability is $0.293$. A projective measurement in the basis containing $|\psi_0^\perp\rangle$ also never errs, but identifies only $|\psi_1\rangle$, giving an average of $(1-s^2)/2=0.25$. Three nonzero orthogonal projectors cannot fit in a two-dimensional space. This is the general structure: a positive operator-valued measure (POVM) has effects $E_k\geq0$ that sum to the identity, with $p(k)=\operatorname{Tr}(\rho E_k)$."),
        ("p", r"Naimark's theorem shows how such a measurement is performed. The photon is coupled to an additional mode, the ancilla, prepared in $|0\rangle_a$. A unitary interaction acts as"),
        ("eq", r"""U|\psi_j\rangle|0\rangle_a=\sqrt{1-s}\,|u_j\rangle|0\rangle_a+\sqrt{s}\,|\chi\rangle|1\rangle_a,
\qquad\langle u_0|u_1\rangle=0."""),
        ("p", r"Inner products are preserved, since $(1-s)\langle u_0|u_1\rangle+s=s$, so such a unitary exists. When the ancilla is found in $|0\rangle_a$, the photon is in one of two orthogonal states and a projective measurement identifies it without error. When the ancilla is found in $|1\rangle_a$, both inputs leave the same state $|\chi\rangle$, and the result is inconclusive. Restricting this larger projective measurement to the photon reproduces $E_0$, $E_1$ and $E_?$ exactly."),
        ("p", r"In general, a POVM fixes only the outcome probabilities. The state after outcome $k$ depends on how the measurement is carried out, through operators $K_{k\alpha}$ with $E_k=\sum_\alpha K_{k\alpha}^\dagger K_{k\alpha}$. Different implementations of the same effects can leave the photon in different states, or absorb it altogether."),
        ("p", r"Huttner and colleagues realized this scheme in 1996 using polarization-dependent loss in optical fibre. Photons removed by the loss element play the role of the inconclusive outcome. The same measurement underlies the B92 version of quantum key distribution. Missed detections add inconclusive events without creating errors. The sharp special case, with orthogonal projectors, is the projection-valued measure."),
    ],
    "projection_valued_measure": [
        ("p", r"A row of detectors along a line registers where a particle lands. Each region of the line corresponds to a yes-or-no question about the particle. Answers for disjoint regions exclude one another, and some region always answers yes."),
        ("p", r"For a particle on the real line, the question for a region $\Delta$ is represented by an operator $E(\Delta)$. It multiplies the wave function by the indicator function $\chi_\Delta$, which equals 1 inside $\Delta$ and 0 outside. These operators are orthogonal projectors, and they combine like the regions themselves:"),
        ("eq", r"""[E(\Delta)\psi](x)=\chi_\Delta(x)\psi(x),\qquad
E(\Delta_1)E(\Delta_2)=E(\Delta_1\cap\Delta_2),\qquad E(\mathbb R)=I."""),
        ("p", r"For disjoint regions the projectors add, including for countable unions. This family is a projection-valued measure (PVM). The probability of a yes answer in a state $\psi$ is $\langle\psi|E(\Delta)|\psi\rangle=\int_\Delta|\psi|^2dx$. By the spectral theorem every self-adjoint operator has exactly one such measure on the real line, so a PVM is the complete description of a sharp observable. For a discrete observable such as a spin component, the measure is concentrated on the eigenvalues. Then $E(\{m\})$ is the projector onto the eigenspace with eigenvalue $m$, and a Stern--Gerlach magnet sends each eigenspace to its own spot."),
        ("p", r"Consider the ground state $\sqrt{2/L}\sin(\pi x/L)$ of a particle in a box of length $L$. The probability that a detector covering the middle third responds is"),
        ("eq", r"""p\left(\tfrac{L}{3}<x<\tfrac{2L}{3}\right)=\frac{2}{L}\int_{L/3}^{2L/3}\sin^2\frac{\pi x}{L}\,dx
=\frac13+\frac{\sqrt3}{2\pi}\approx0.609."""),
        ("p", r"The $n=2$ level, with a node at the centre, gives $1/3-\sqrt3/(4\pi)\approx0.196$ instead. Because $E(\Delta)^2=E(\Delta)$, a state that has just answered yes lies in the range of $E(\Delta)$. An immediate repetition then answers yes with certainty, which is the repeatability that defines a sharp measurement."),
        ("p", r"Commuting observables share a joint measure. The $x$ and $y$ coordinates of a particle give rectangle projectors $E_X(\Delta_x)E_Y(\Delta_y)$, and a camera measures both at once. Position and momentum have no such joint measure. A nonzero wave function cannot vanish outside a bounded interval while its Fourier transform also vanishes outside a bounded interval, so"),
        ("eq", r"""\operatorname{ran}E_X(\Delta)\cap\operatorname{ran}E_P(\Gamma)=\{0\}
\qquad\text{for bounded }\Delta,\Gamma."""),
        ("p", r"No state answers yes with certainty to both questions. This does not follow from the variance bound of the uncertainty principle. It forbids exact confinement to bounded regions of any size, including regions whose product of widths greatly exceeds $\hbar$."),
        ("p", r"Real pixels have blurred edges. A detector whose response function $\mu_\Delta(x)$ takes values strictly between 0 and 1 near the edges is represented by $F(\Delta)=\int\mu_\Delta(x)\,|x\rangle\langle x|\,dx$, which satisfies $F^2\neq F$. It is a POVM rather than a PVM, and its records need not repeat. The PVM is the ideal limit in which the response is exactly 0 or 1."),
    ],
    "delayed_choice_quantum_eraser": [
        ("p", r"A photon reaches a detector that scans across a screen, and its position is recorded. Several nanoseconds later its partner photon is sent at random along one of two routes. One leads to a detector that reveals where the pair was emitted; the other leads to a beam splitter that hides this information. Sorting the screen records by the partner's later result reveals interference fringes in some subsets."),
        ("p", r"In the experiment of Kim, Yu, Kulik, Shih and Scully, a pump laser illuminates a nonlinear crystal in two regions $A$ and $B$. Either region may emit a signal and idler pair, so the pair is in the state $(|A\rangle_s|A\rangle_i+|B\rangle_s|B\rangle_i)/\sqrt2$. A lens maps the two signal paths to amplitudes $\psi_A(x)$ and $\psi_B(x)$ at the screen detector $D_0$."),
        ("p", r"The idler meets a 50:50 beam splitter on each path. One output goes to a detector that receives only idlers from $A$ ($D_3$) or only from $B$ ($D_4$). The other outputs are combined on a central beam splitter whose two ports, $D_1$ and $D_2$, cannot tell $A$ from $B$. Projecting both photons onto the detected states gives the joint probabilities"),
        ("eq", r"""P(x,D_{1,2})=\tfrac18|\psi_A(x)\pm\psi_B(x)|^2,\qquad
P(x,D_3)=\tfrac14|\psi_A(x)|^2,\qquad P(x,D_4)=\tfrac14|\psi_B(x)|^2."""),
        ("p", r"Coincidences with $D_1$ show fringes and those with $D_2$ show the complementary antifringes, shifted by half a period. Coincidences with $D_3$ or $D_4$ show the smooth single-path profile. Each idler detector receives a quarter of the pairs."),
        ("p", r"The time order of the two detections plays no part in this calculation. The projector for the signal position and the projector for an idler detector act on different photons and commute. The joint probability is therefore the same whichever record is made earlier, and in any reference frame:"),
        ("eq", r"""P(x,k)=\big\|(\langle x|_s\otimes\langle k|_i)\Psi\big\|^2,\qquad
\sum_kP(x,k)=\tfrac12\big(|\psi_A(x)|^2+|\psi_B(x)|^2\big)."""),
        ("p", r"The screen pattern by itself has no fringes, whatever happens to the idler and whenever it happens. The idler path did not affect where the signal landed. It determines which subset of the existing records is selected, and the fringes appear only when the subsets are compared using the idler records. Those records travel by ordinary means, so no information is sent to the earlier detection."),
        ("p", r"In the 2000 experiment the idler paths were longer, so the idler was registered several nanoseconds after its partner. Ma and colleagues later made the choice with a random number generator spacelike separated from the interference, over a 144 km free-space link between two Canary Islands. Interference again appeared only in the sorted subsets."),
        ("p", r"The calculation is the conditional-fringe analysis of the quantum eraser experiment, applied to an entangled pair whose members are recorded at different times. The commuting projectors are also why the correlations in Bell experiments cannot be used to send messages."),
    ],
    "einstein_podolsky_rosen_paradox": [
        ("p", r"Two particles interact and fly apart so that both their separation and their total momentum are sharply fixed. Measuring the position of one particle then predicts the position of the other, and measuring its momentum predicts the other's momentum. In 1935 Einstein, Podolsky and Rosen argued that both predicted values must correspond to physical properties of the distant particle."),
        ("p", r"Such a state exists because the relative position and the total momentum commute. With $x_j$ and $p_j$ the position and momentum of particle $j$,"),
        ("eq", r"""[x_1-x_2,\;p_1+p_2]=[x_1,p_1]-[x_2,p_2]=i\hbar-i\hbar=0,\\
\psi(x_1,x_2)\propto\delta(x_1-x_2-L)=\frac{1}{2\pi\hbar}\int e^{ip(x_1-x_2-L)/\hbar}dp."""),
        ("p", r"The integral shows that the same state contains every momentum pair $(p,-p)$. A position measurement on particle 1 that gives $\xi$ predicts $x_2=\xi-L$, and a momentum measurement giving $\kappa$ predicts $p_2=-\kappa$. Neither measurement acts on particle 2. EPR concluded that particle 2 has definite position and momentum, which no quantum state of particle 2 alone can describe. Hence, they argued, the quantum description is incomplete."),
        ("p", r"The ideal state is not normalizable, but an optical version is. A nondegenerate parametric amplifier produces two beams in a two-mode squeezed state. Use dimensionless field quadratures with $[x_j,p_j]=i$ and vacuum variance 1/2, and squeezing parameter $r$. Then $\operatorname{Var}(x_1-x_2)=\operatorname{Var}(p_1+p_2)=e^{-2r}$, while each beam alone shows enlarged noise $\cosh(2r)/2$."),
        ("p", r"Reid turned the argument into a measurable test. Let $\Delta^2_{\rm inf}x_2$ be the smallest mean-square error with which $x_2$ can be predicted from a record of $x_1$, and similarly for $p_2$. If beam 2 had a local quantum state, the uncertainty principle would require the product of these inferred variances to be at least 1/4. The best linear prediction gives"),
        ("eq", r"""\Delta^2_{\rm inf}x_2=\Delta^2_{\rm inf}p_2=\frac{1}{2\cosh2r},\qquad
\Delta^2_{\rm inf}x_2\,\Delta^2_{\rm inf}p_2=\frac{1}{4\cosh^22r}<\frac14."""),
        ("p", r"At $r=0.5$ the product is $0.105$, well below the bound. Ou, Pereira, Kimble and Peng observed an inferred-variance product below the bound in 1992. Loss on either beam adds vacuum noise and raises the inferred variances, so the demonstration requires efficient transmission and detection."),
        ("p", r"The EPR argument does not by itself exclude local hidden variables. The Wigner function of the two-mode squeezed state is a positive Gaussian, which can serve as a local probability distribution for all quadrature records. Bell showed that other measurements, such as spin components along several axes, separate the options. Bell's theorem decides between local models and quantum predictions, whereas the EPR test shows that local states of one particle cannot explain the predictions made from the other. Quantum nonlocality treats the stronger correlations in multipartite states."),
    ],
    "electron_microscope": [
        ("p", r"A transmission electron microscope sends electrons, accelerated by about 200 kV, through a specimen a few tens of nanometres thick. Its images resolve columns of atoms 0.1 to 0.2 nm apart. The electron wavelength is a few picometres, so lens aberrations rather than diffraction set the resolution."),
        ("p", r"An electron of rest mass $m_0$ and charge $e$ accelerated through a potential difference $U$ gains kinetic energy $eU$. The relativistic relation $(pc)^2=(eU+m_0c^2)^2-(m_0c^2)^2$ fixes its momentum $p$, and the de Broglie relation gives the wavelength:"),
        ("eq", r"""\lambda=\frac{h}{\sqrt{2m_0eU\left(1+\dfrac{eU}{2m_0c^2}\right)}},\qquad
\lambda(200\,{\rm kV})=2.51\,{\rm pm}."""),
        ("p", r"At 200 kV the electron moves at 0.70 $c$, and the nonrelativistic formula would give 2.74 pm, an error of 9 percent. At 300 kV the wavelength is 1.97 pm. Scattering angles from atomic spacings are then of order 10 mrad, so the electron optics works close to the axis."),
        ("p", r"A thin specimen barely absorbs the beam. It delays the electron wave by an amount proportional to the projected electrostatic potential $V_p(\mathbf x)$. The transmitted wave is $e^{i\sigma V_p}\approx1+i\sigma V_p$, where $\sigma=2\pi me\lambda/h^2$ with the relativistic mass $m$. At 200 kV, $\sigma=7.29\times10^{-3}$ rad per volt-nanometre. An ideal lens would reproduce $|1+i\sigma V_p|^2\approx1$, and the atoms would be invisible."),
        ("p", r"A real objective lens adds a phase $\chi(k)$ to the wave scattered at spatial frequency $k$, the scattering angle divided by $\lambda$. Defocus $\Delta f$ and spherical aberration $C_s$ give the leading terms. Interference with the unscattered beam then turns the phase delay into intensity, with image Fourier transform"),
        ("eq", r"""\chi(k)=\pi\Delta f\,\lambda k^2+\frac{\pi}{2}C_s\lambda^3k^4,\qquad
\widetilde I(\mathbf k)=\delta(\mathbf k)+2\sigma\widetilde V_p(\mathbf k)\sin\chi(k)."""),
        ("p", r"The factor $\sin\chi$ is the contrast transfer function in this sign convention. Scherzer chose the defocus $\Delta f=-\sqrt{4C_s\lambda/3}$, so that $\sin\chi$ stays close to $-1$ over a broad band while $\chi$ never falls below $-2\pi/3$. The lowest zero of $\sin\chi$ beyond that band gives the point resolution $d\approx0.66\,C_s^{1/4}\lambda^{3/4}$. For $C_s=1$ mm at 200 kV this gives $\Delta f\approx-58$ nm and $d\approx0.23$ nm. The diffraction limit for a 10 mrad aperture would be $0.61\lambda/\alpha\approx0.15$ nm."),
        ("p", r"Aberration correctors made from multipole lenses reduce $C_s$ and bring the resolution below 0.1 nm. A phase plate that shifts the unscattered beam by $\pi/2$ converts $\sin\chi$ into $\cos\chi$, the electron analogue of Zernike phase contrast in light microscopy. The linear relation holds only for weak phase objects with $\sigma V_p\ll1$. Thicker crystals scatter electrons several times and require dynamical calculations, and partial coherence of the beam damps the highest frequencies. For biological specimens radiation damage limits the dose, so the shot noise of the electron count limits contrast."),
        ("p", r"The instrument is a direct application of wave-particle duality: the same electrons that strike the detector one at a time form an interference pattern. The specimen potential enters as in the Born approximation of scattering theory, with single scattering from the projected potential."),
    ],
    "quantum_eraser_experiment": [
        ("p", r"Light passing two slits forms fringes on a screen. If each path leaves a mark in another degree of freedom, the fringes fade. A later measurement of that mark in a suitable basis can recover fringes in sorted subsets of the records."),
        ("p", r"Let the screen amplitudes from the two slits be $\psi_1(x)$ and $\psi_2(x)$, and let the paths leave marker states $|m_1\rangle$ and $|m_2\rangle$. The joint state is proportional to $\psi_1(x)|m_1\rangle+\psi_2(x)|m_2\rangle$. Ignoring the marker, the screen intensity is"),
        ("eq", r"""P(x)\propto|\psi_1|^2+|\psi_2|^2+2\operatorname{Re}\big[\psi_1^*\psi_2\langle m_1|m_2\rangle\big]."""),
        ("p", r"The fringe term is multiplied by the marker overlap. For equal intensities the visibility equals $|\langle m_1|m_2\rangle|$, and orthogonal markers remove the fringes entirely. The marking need not deliver any momentum kick. The interference term disappears because the screen amplitude is now correlated with an orthogonal marker state."),
        ("p", r"Now take orthogonal markers and measure them in a rotated basis, with an angle $\beta$ and a phase $\gamma$ that the experimenter sets:"),
        ("eq", r"""|e_+\rangle=\cos\tfrac{\beta}{2}|m_1\rangle+e^{i\gamma}\sin\tfrac{\beta}{2}|m_2\rangle,\\
|e_-\rangle=\sin\tfrac{\beta}{2}|m_1\rangle-e^{i\gamma}\cos\tfrac{\beta}{2}|m_2\rangle."""),
        ("p", r"Conditioning on each outcome projects the marker and leaves a definite screen amplitude. The two conditional patterns have the same visibility:"),
        ("eq", r"""\psi_+=\cos\tfrac{\beta}{2}\,\psi_1+e^{-i\gamma}\sin\tfrac{\beta}{2}\,\psi_2,\qquad
\psi_-=\sin\tfrac{\beta}{2}\,\psi_1-e^{-i\gamma}\cos\tfrac{\beta}{2}\,\psi_2,\\
V_{\rm cond}=|\sin\beta|."""),
        ("p", r"At $\beta=0$ the marker measurement reveals the path and the subsets show no fringes. At $\beta=\pi/2$ the marker basis is unbiased with respect to the paths; each subset shows full-contrast fringes, one shifted by half a period relative to the other. The two subsets always add to the unmarked, fringe-free pattern. Erasure therefore selects subsets, and the total distribution on the screen is unchanged."),
        ("p", r"Walborn, Terra Cunha, Pádua and Monken carried this out with polarization-entangled photon pairs from parametric down-conversion. Quarter-wave plates in front of the two slits marked the path in the circular polarization of the signal photon, and the coincidence fringes vanished. A polarizer on the distant idler photon then projected the pair onto a basis unbiased with respect to the paths. Fringes and antifringes reappeared in the coincidence counts."),
        ("p", r"The entangled partner matters. If a single photon carries its own polarization mark, a polarizer at $45^\circ$ before the screen recovers fringes. That version is reproduced by classical polarization optics, through the Fresnel--Arago laws. With an entangled partner, the basis is chosen on a photon that never passes the slits, and the fringes exist only in coincidence data."),
        ("p", r"The trade-off between partial marking and partial visibility is the subject of wave-particle duality. The delayed-choice quantum eraser applies the same conditioning to an idler recorded after its partner."),
    ],
    "quantum_imaging": [
        ("p", r"Imaging a faintly absorbing sample with few photons, such as a cell that light damages, is limited by the random arrival of photons. Light from parametric down-conversion comes in pairs. Counting the partner photons measures that randomness, which can then be subtracted."),
        ("p", r"Consider one pixel and an object with transmission $t=1-\alpha$. With coherent light, the transmitted count $N_t$ is Poisson distributed with mean $t\bar N$. The estimate $\hat t=N_t/\bar N$ then has variance $t/\bar N$, the shot-noise limit. In twin beams, signal and idler pixel pairs contain equal photon numbers. The idler count $N_i$ therefore tells how many photons entered the sample in the matching signal pixel."),
        ("p", r"Each photon then survives the object independently with probability $t$. The signal count $N_s$ is binomially distributed given $N_i$, and the ratio $\hat t=N_s/N_i$ has a smaller variance:"),
        ("eq", r"""\operatorname{Var}\hat t_{\rm coh}=\frac{t}{\bar N},\qquad
\operatorname{Var}\hat t_{\rm twin}=\frac{t(1-t)}{\bar N},\qquad
\frac{\operatorname{Var}\hat t_{\rm twin}}{\operatorname{Var}\hat t_{\rm coh}}=\alpha."""),
        ("p", r"Fluctuations in the number of pairs cancel, because they appear equally in both beams. Only the randomness of absorption itself remains. For a sample absorbing $\alpha=1\%$, the variance falls a hundredfold. The same precision is then reached with a hundredth of the photons, an important saving for light-sensitive samples."),
        ("p", r"Real detectors miss photons. If each beam is detected with efficiency $\eta$, a missed idler is mistaken for an absent photon. The statistic used in experiments is the noise reduction factor. For a transparent region of the sample it becomes"),
        ("eq", r"""\frac{\operatorname{Var}(N_s-N_i)}{\langle N_s+N_i\rangle}=1-\eta\qquad(t=1),"""),
        ("p", r"compared with 1 for two independent beams at the shot-noise level. The advantage thus requires high efficiency. Each pixel must also collect both members of most pairs, so pixels must be larger than the coherence area of the down-converted light. That area sets the spatial resolution."),
        ("p", r"Brida, Genovese and Ruo Berchera demonstrated sub-shot-noise imaging in 2010. They recorded twin beams from parametric down-conversion on a CCD camera, placed a weakly absorbing object in one beam, and subtracted the matching pixels of the other. The object appeared with a larger signal-to-noise ratio than with classical illumination at the same photon number."),
        ("p", r"Ghost imaging also uses pair correlations. A detector without spatial resolution collects light behind the object, while a camera in the other beam forms the image in coincidence counts. Ghost images can also be formed with classical thermal light at lower visibility, so a ghost image alone is not a signature of quantum correlations. The photon-number difference above is quantum, because classical fields cannot push the noise reduction factor below 1. Quantum metrology treats the same comparison of precision per photon in general form."),
    ],
    "quantum_nonlocality": [
        ("p", r"Three photons are emitted together and sent to three separated laboratories. Each laboratory measures one of two polarization observables. For a Greenberger--Horne--Zeilinger (GHZ) state, certain products of the three records are predicted with certainty. These certain predictions alone contradict any local assignment of values, without averaging an inequality."),
        ("p", r"Write the state as $(|000\rangle+|111\rangle)/\sqrt2$, with $|0\rangle$ and $|1\rangle$ the eigenstates of the Pauli operator $Z$. Applying the Pauli operators $X$ and $Y$ directly gives the eigenvalue relations"),
        ("eq", r"""X_1X_2X_3|{\rm GHZ}\rangle=+|{\rm GHZ}\rangle,\\
X_1Y_2Y_3|{\rm GHZ}\rangle=Y_1X_2Y_3|{\rm GHZ}\rangle=Y_1Y_2X_3|{\rm GHZ}\rangle=-|{\rm GHZ}\rangle."""),
        ("p", r"Suppose each photon carries predetermined values $x_j=\pm1$ and $y_j=\pm1$, the records it would give if $X$ or $Y$ were measured. Locality requires that these values do not depend on which observables the other two laboratories choose. The three $XYY$-type relations then fix the product of all $x_j$, because each $y_j$ appears twice:"),
        ("eq", r"""(x_1y_2y_3)(y_1x_2y_3)(y_1y_2x_3)=x_1x_2x_3=(-1)^3=-1."""),
        ("p", r"Quantum mechanics predicts $x_1x_2x_3=+1$ with certainty. No local assignment satisfies all four relations. For two spin-1/2 particles, perfect correlations alone do not suffice: the perfect anticorrelations of a singlet along equal axes have a local model. Bell's inequality needs the imperfect correlations at unequal angles. Each run measures only one combination of observables, so the contradiction is established across runs with different settings. Pan, Bouwmeester, Daniell, Weinfurter and Zeilinger performed this test with three-photon GHZ states in 2000. The $XXX$ products came out predominantly $+1$, as quantum mechanics predicts and opposite to the local inference from the $XYY$-type data."),
        ("p", r"Imperfect states require a bound that tolerates noise. Mermin's combination $M=\langle XXX\rangle-\langle XYY\rangle-\langle YXY\rangle-\langle YYX\rangle$ is at most 2 for local values, while the GHZ state gives 4. If the state is mixed with white noise so that correlations shrink by a factor $v$, then $M=4v$, and a violation requires only $v>1/2$. The two-particle CHSH test of Bell's theorem requires $v>1/\sqrt2$."),
        ("p", r"These correlations cannot carry a message. Let laboratory 1 measure with effects $E_a$ and laboratory 2 with effects $F_b^y$ for setting $y$. Because the effects of each setting sum to the identity, the record statistics in laboratory 1 do not depend on the distant choice:"),
        ("eq", r"""\sum_b\operatorname{Tr}[\rho(E_a\otimes F^y_b)]=\operatorname{Tr}(\rho_1E_a),
\qquad \rho_1=\operatorname{Tr}_2\rho."""),
        ("p", r"Nonlocality appears only when records from separated laboratories are compared. Entanglement is necessary for it but not sufficient. Werner showed that a singlet mixed with enough white noise remains entangled yet admits a local model for all projective measurements. Device-independent quantum key distribution relies on observed nonlocal correlations rather than on a model of the devices. The Einstein--Podolsky--Rosen paradox is the two-particle argument that preceded these tests."),
    ],
    "wave_function_collapse": [
        ("p", r"A trapped ion is driven from one hyperfine level to another by a resonant radio-frequency field. If the level is checked repeatedly during the drive, the transfer slows down. Frequent enough checks nearly stop it."),
        ("p", r"The calculation uses the update rule for a recorded outcome. For a measurement with orthogonal projectors $P_k$, the Lüders rule replaces the density operator $\rho$ after outcome $k$ by the normalized projection. If the outcome is not recorded, the state becomes the probability-weighted average:"),
        ("eq", r"""\rho\;\longmapsto\;\frac{P_k\rho P_k}{\operatorname{Tr}(\rho P_k)},\qquad
\rho\;\longmapsto\;\sum_kP_k\rho P_k."""),
        ("p", r"Because $P_k^2=P_k$, an immediate repetition returns outcome $k$ with certainty. The second map removes the coherences between different outcomes and keeps their populations."),
        ("p", r"Let the drive rotate the Bloch vector of the two-level ion about the $x$ axis, completing a $\pi$ rotation in time $T$. Without interruption it transfers the ion completely. Divide $T$ into $N$ intervals, each rotating the vector by $\pi/N$ and followed by a measurement of the level. Each measurement removes the transverse components, so the $z$ component is multiplied by $\cos(\pi/N)$ at every step:"),
        ("eq", r"""P_N=\frac12\left[1-\cos^N\frac{\pi}{N}\right]\approx\frac{\pi^2}{4N}\qquad(N\gg1)."""),
        ("p", r"One interruption gives full transfer, two give 0.5, and 64 give 0.037. Itano, Heinzen, Bollinger and Wineland observed this suppression in 1990. They drove a hyperfine transition of beryllium ions with a 256 ms radio-frequency pulse, interrupted by up to 64 short laser pulses. Ions in one of the levels scattered light from each pulse, and the measured transfer followed the prediction. This slowing is the quantum Zeno effect."),
        ("p", r"The suppression relies on the quadratic start of the transfer: with Rabi frequency $\Omega$, the probability of leaving the initial level grows as $(\Omega t/2)^2$ at short times. A decay into a broad continuum is quadratic only for times shorter than the correlation time of the continuum. Ordinary radioactive decay is therefore not slowed by any realistic observation. Each laser pulse must also dephase the two levels completely without driving the radio-frequency transition."),
        ("p", r"The same suppression follows when each laser pulse is treated as a coupling of the ion to the scattered light, without invoking the update rule. The experiment therefore confirms that a strong probe removes the coherence between levels. It does not show that collapse is a physical process distinct from that interaction. Whether the update describes a physical change or a revision of information is the measurement problem. The quantum jump description gives the same conditioning for continuous photon counting."),
    ],
    "wave_particle_duality": [
        ("p", r"Electrons sent one at a time through a two-path interferometer arrive at single points, yet their accumulated positions form fringes. A detector that records which path each electron took reduces the fringe contrast. Englert's inequality states exactly how much path information can coexist with how much contrast."),
        ("p", r"The wave behaviour follows from the de Broglie relation $\lambda=h/p$, which the diffraction of electrons by a nickel crystal confirmed, as described under the wave function."),
        ("p", r"Now let a beam splitter send the particle into path 1 or 2 with probabilities $w_1$ and $w_2$. An internal degree of freedom, the marker, is left in state $|m_1\rangle$ or $|m_2\rangle$. After recombination with relative phase $\phi$, the two output ports have probabilities $\frac12[1\pm2\sqrt{w_1w_2}\operatorname{Re}(e^{i\phi}\langle m_1|m_2\rangle)]$. The visibility and the a priori predictability of the path are"),
        ("eq", r"""V=2\sqrt{w_1w_2}\,|\langle m_1|m_2\rangle|,\qquad P=|w_1-w_2|."""),
        ("p", r"Path information stored in the marker is quantified by the distinguishability $D$. A measurement on the marker identifies the path correctly with probability at most $(1+D)/2$. Helstrom's result for discriminating two states gives $D$ as a trace norm, which for pure markers can be evaluated in closed form:"),
        ("eq", r"""D=\big\|w_1|m_1\rangle\langle m_1|-w_2|m_2\rangle\langle m_2|\big\|_1
=\sqrt{1-4w_1w_2|\langle m_1|m_2\rangle|^2},\\
V^2+D^2=1\ \ \text{(pure markers)},\qquad V^2+D^2\leq1\ \ \text{(general)}."""),
        ("p", r"If the marker is mixed, or part of it escapes to an environment that is not examined, the equality becomes an inequality. Without a marker, $D$ reduces to $P$ and the relation becomes $V^2+P^2\leq1$. For equal paths and a marker overlap of $\cos30^\circ$, the fringes keep 87 percent contrast while the path can be guessed correctly 75 percent of the time. Intermediate cases have partial fringes and partial path knowledge, related by this single inequality."),
        ("p", r"The bound refers to the information available in the marker, not to what an experimenter actually measures. A marker measurement in a basis unrelated to the paths extracts no path information. Fringes then reappear in subsets of the records, as in the quantum eraser experiment."),
        ("p", r"Dürr, Nonn and Rempe tested the mechanism in an atom interferometer in 1998. A microwave field stored the path in the internal hyperfine state of each atom, and the fringes vanished. The momentum transferred by the microwave photons was far too small to wash out the fringes by random kicks. The loss of contrast came from the correlation between path and marker, as the formula states."),
        ("p", r"The relation applies to any two-path interferometer whose marker can be modelled as a quantum state. With a thermal environment as the unread marker, the same overlap describes decoherence. The electron microscope uses the wave side of this relation, forming images from interference between scattered and unscattered electrons."),
    ],
}

REFERENCES = {
    "bell_s_theorem": [
        ("1303.2849", "N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani and S. Wehner, Bell nonlocality; CHSH inequality, Tsirelson bound and loopholes."),
        ("1508.05949", "B. Hensen and colleagues, Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km; S = 2.42 in 245 trials."),
    ],
    "born_rule": [
        ("1007.4193", "U. Sinha, C. Couteau, T. Jennewein, R. Laflamme and G. Weihs, Ruling Out Multi-Order Interference in Quantum Mechanics; three-slit bound on third-order interference."),
        ("gr-qc/9401003", "R. D. Sorkin, Quantum Mechanics as Quantum Measure Theory; hierarchy of sum rules in which quantum probabilities have only pairwise interference."),
    ],
    "measurement_in_quantum_mechanics": [
        ("0810.4729", "A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt and R. J. Schoelkopf, Introduction to Quantum Noise, Measurement and Amplification; von Neumann pointer model, back-action and quantum limits."),
    ],
    "measurement_problem": [
        ("quant-ph/0312059", "M. Schlosshauer, Decoherence, the measurement problem, and interpretations of quantum mechanics; pointer states and what decoherence does not resolve."),
        ("1204.4325", "A. Bassi, K. Lochan, S. Satin, T. P. Singh and H. Ulbricht, Models of Wave-function Collapse, Underlying Theories, and Experimental Tests; GRW amplification and experimental bounds."),
    ],
    "povm": [
        ("0810.1970", "S. M. Barnett and S. Croke, Quantum state discrimination; unambiguous discrimination, the Ivanovic-Dieks-Peres limit and its optical realizations."),
        ("0810.3536", "T. Heinosaari and M. Ziman, Guide to Mathematical Concepts of Quantum Theory; POVMs and Naimark dilation."),
    ],
    "projection_valued_measure": [
        ("0810.3536", "T. Heinosaari and M. Ziman, Guide to Mathematical Concepts of Quantum Theory; projection-valued measures, joint measurability and smeared observables."),
        ("1508.06951", "V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; spectral theorem and projection-valued measures of self-adjoint operators."),
    ],
    "delayed_choice_quantum_eraser": [
        ("quant-ph/9903047", "Y.-H. Kim, R. Yu, S. P. Kulik, Y. H. Shih and M. O. Scully, A Delayed Choice Quantum Eraser; the two-region down-conversion experiment analysed here."),
        ("1206.6578", "X.-S. Ma and colleagues, Quantum erasure with causally disconnected choice; spacelike-separated choice over 144 km."),
        ("1407.2930", "X.-S. Ma, J. Kofler and A. Zeilinger, Delayed-choice gedanken experiments and their realizations; review of the time-order analysis."),
    ],
    "einstein_podolsky_rosen_paradox": [
        ("0806.0270", "M. D. Reid and colleagues, The Einstein-Podolsky-Rosen paradox: from concepts to applications; inferred-variance criterion and two-mode squeezed states."),
    ],
    "electron_microscope": [
        ("1009.4038", "B. Gamm, K. Schultheiss, R. R. Schroder and D. Gerthsen, Effect of a Physical Phase Plate on Contrast Transfer in an Aberration-Corrected Transmission Electron Microscope; weak-phase-object contrast transfer, spherical aberration, defocus and phase plates."),
    ],
    "quantum_eraser_experiment": [
        ("quant-ph/0106078", "S. P. Walborn, M. O. Terra Cunha, S. Padua and C. H. Monken, A double-slit quantum eraser; polarization marking and erasure with entangled photons."),
        ("1407.2930", "X.-S. Ma, J. Kofler and A. Zeilinger, Delayed-choice gedanken experiments and their realizations; quantum erasers and complementarity."),
    ],
    "quantum_imaging": [
        ("1004.1274", "G. Brida, M. Genovese and I. Ruo Berchera, Experimental realization of sub-shot-noise quantum imaging; twin-beam absorption imaging."),
        ("1601.06066", "M. Genovese, Real applications of quantum imaging; sub-shot-noise and ghost imaging."),
    ],
    "quantum_nonlocality": [
        ("0712.0921", "D. M. Greenberger, M. A. Horne and A. Zeilinger, Going Beyond Bell's Theorem; the three-particle argument without inequalities."),
        ("1303.2849", "N. Brunner, D. Cavalcanti, S. Pironio, V. Scarani and S. Wehner, Bell nonlocality; Mermin inequality, no-signalling and local models of entangled states."),
    ],
    "wave_function_collapse": [
        ("quant-ph/0612187", "W. M. Itano, Perspectives on the quantum Zeno paradox; the 1990 trapped-ion experiment and its interpretation."),
    ],
    "wave_particle_duality": [
        ("1403.4687", "P. J. Coles, J. Kaniewski and S. Wehner, Equivalence of wave-particle duality to entropic uncertainty; visibility-distinguishability relations."),
        ("2507.19801", "H. Lin, Y.-K. Lu, V. Fedoseev, Y. K. Lee, J. Lyu and W. Ketterle, Fringe visibility and which-way information in Young's double slit experiments with light scattered from single atoms; motional states of trapped atoms as which-path markers."),
    ],
}
