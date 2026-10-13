"""Generators of quantum dynamics: Hamiltonians, unitary maps, wave equations, propagators, perturbations and noise."""

NARRATIVES = {
    "creation_and_annihilation_operators": [
        ("p", r"A short density pulse made at the centre of an elongated Bose--Einstein condensate travels along it at a few millimetres per second. That speed, and the change from sound to free-particle motion at short wavelengths, follow from the algebra of the operators that add or remove one atom from a mode."),
        ("p", r"Let $i$ label orthonormal single-particle modes, such as plane waves in a box or the vibrational modes of a trap. A state with $n_i$ quanta in mode $i$ is written $|\dots,n_i,\dots\rangle$. For bosons the creation operator $a_i^\dagger$ and the annihilation operator $a_i$ act as follows, while fermion operators $c_i$ obey anticommutators:"),
        ("eq", r"""a_i^\dagger|\dots,n_i,\dots\rangle=\sqrt{n_i+1}\,|\dots,n_i+1,\dots\rangle,\qquad
a_i|\dots,n_i,\dots\rangle=\sqrt{n_i}\,|\dots,n_i-1,\dots\rangle,\\
N_i=a_i^\dagger a_i,\qquad [a_i,a_j^\dagger]=\delta_{ij},\qquad
\{c_i,c_j^\dagger\}=\delta_{ij},\qquad \{c_i,c_j\}=0."""),
        ("p", r"The square-root factors make $N_i$ count the quanta in mode $i$, and they follow from the commutator alone. Setting $i=j$ in $\{c_i,c_j\}=0$ gives $(c_i^\dagger)^2=0$, so no mode can hold two fermions. This is the Pauli exclusion principle, obtained without writing an antisymmetric wave function."),
        ("p", r"One-body observables are sums of single products: if $o_{ij}$ is the matrix element of a single-particle operator between modes, the many-particle operator is $O=\sum_{ij}o_{ij}a_i^\dagger a_j$. A two-body interaction needs two creation and two annihilation operators. Consider bosons of mass $m$ in a box of volume $V$, with plane-wave modes $\mathbf k$ and a contact interaction of strength $g=4\pi\hbar^2a_s/m$ fixed by the s-wave scattering length $a_s$:"),
        ("eq", r"""H=\sum_{\mathbf k}\epsilon_k\,a_{\mathbf k}^\dagger a_{\mathbf k}
+\frac{g}{2V}\sum_{\mathbf k,\mathbf k',\mathbf q}
a_{\mathbf k+\mathbf q}^\dagger a_{\mathbf k'-\mathbf q}^\dagger a_{\mathbf k'}a_{\mathbf k},
\qquad \epsilon_k=\frac{\hbar^2k^2}{2m}."""),
        ("p", r"Each interaction term removes atoms from modes $\mathbf k$ and $\mathbf k'$ and returns them with momentum $\hbar\mathbf q$ exchanged, so total momentum is conserved. In the condensate nearly all $N$ atoms occupy $\mathbf k=0$, where $a_0$ and $a_0^\dagger$ multiply by about $\sqrt N$. Bogoliubov replaced both by $\sqrt N$ and kept the terms quadratic in the other operators. With density $n=N/V$,"),
        ("eq", r"""H\approx\frac{gnN}{2}+\sum_{\mathbf k\neq0}\Big[(\epsilon_k+gn)\,a_{\mathbf k}^\dagger a_{\mathbf k}
+\frac{gn}{2}\big(a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger+a_{\mathbf k}a_{-\mathbf k}\big)\Big]."""),
        ("p", r"The pair terms move two atoms with opposite momenta out of the condensate or back into it. They are removed by mixing $a_{\mathbf k}$ with $a_{-\mathbf k}^\dagger$:"),
        ("eq", r"""b_{\mathbf k}=u_ka_{\mathbf k}+v_ka_{-\mathbf k}^\dagger,\qquad
u_k^2=\frac12\Big(\frac{\epsilon_k+gn}{E_k}+1\Big),\qquad v_k^2=u_k^2-1,\\
H=E_0+\sum_{\mathbf k\neq0}E_k\,b_{\mathbf k}^\dagger b_{\mathbf k},\qquad
E_k=\sqrt{\epsilon_k(\epsilon_k+2gn)}."""),
        ("p", r"The condition $u_k^2-v_k^2=1$ keeps $[b_{\mathbf k},b_{\mathbf k}^\dagger]=1$, so $b_{\mathbf k}$ removes one quasiparticle with bosonic statistics. At long wavelength $E_k\approx\hbar ck$, a sound wave with speed $c=\sqrt{gn/m}$. At short wavelength $E_k\approx\epsilon_k+gn$, a free atom raised by the mean interaction energy. The crossover lies at the healing length $\xi=\hbar/\sqrt{2mgn}$, where $\epsilon_k=gn$ for $k=1/\xi$."),
        ("p", r"For sodium, $a_s=2.75$ nm. At a density of $10^{14}\,\mathrm{cm}^{-3}$ this gives $c=5.1$ mm/s and $\xi=0.38\,\mu\mathrm m$. Andrews and colleagues excited density pulses in elongated sodium condensates in 1997 and imaged them as they moved. The measured speeds were several millimetres per second and grew with density as the theory predicts. In a cigar-shaped cloud the pulse samples the whole cross-section. The speed is then set by the density averaged over that section, half the central value for a Thomas--Fermi profile, which lowers $c$ by a factor $\sqrt2$."),
        ("p", r"The treatment requires a dilute gas, $na_s^3\ll1$. Even at zero temperature the pair terms keep a fraction $(8/3)\sqrt{na_s^3/\pi}$ of the atoms outside the condensate, 0.2 percent for these numbers. Because $E_k/\hbar k$ never falls below $c$, an impurity moving slower than $c$ cannot create excitations, which is Landau's criterion for superfluidity. A single mode reproduces the ladder of the quantum harmonic oscillator, and the same pair terms describe squeezed light in quantum optics."),
    ],
    "hamiltonian_quantum_mechanics": [
        ("p", r"Ammonia absorbs microwaves near 24 GHz, and its line at 23.87 GHz was used in the ammonia maser of 1954. The same frequency describes a motion: a nitrogen atom placed on one side of the plane of the three hydrogens tunnels to the other side and back. One operator, the Hamiltonian $H$, fixes both the energy outcomes and this time evolution."),
        ("p", r"For a closed system with time-independent $H$, the energy eigenstates $|E_n\rangle$ form a basis, and evolution multiplies each component by its own phase. Write the prepared state as $|\psi\rangle=\sum_nc_n|E_n\rangle$. For any observable $O$ with matrix elements $O_{mn}=\langle E_m|O|E_n\rangle$,"),
        ("eq", r"""H|E_n\rangle=E_n|E_n\rangle,\qquad
U(t)=e^{-iHt/\hbar}=\sum_ne^{-iE_nt/\hbar}|E_n\rangle\langle E_n|,\\
\langle O\rangle(t)=\sum_{m,n}c_m^*c_n\,O_{mn}\,e^{i(E_m-E_n)t/\hbar}."""),
        ("p", r"Only energy differences enter, so a constant added to $H$ changes no prediction. The weights $|c_n|^2$ never change, which is energy conservation. Every observable oscillates at the Bohr frequencies $(E_m-E_n)/\hbar$, the same frequencies a spectrometer records as absorption or emission lines. An eigenstate acquires only an overall phase, so all its expectation values are constant. Motion requires a superposition of different energies."),
        ("p", r"In ammonia the umbrella-inversion coordinate has two equivalent minima. Let $|L\rangle$ and $|R\rangle$ be states localized in each well with equal energy $E_0$, and let $A>0$ be the tunnelling amplitude through the barrier between them. Within this pair of states,"),
        ("eq", r"""H=\begin{pmatrix}E_0&-A\\-A&E_0\end{pmatrix},\qquad E_\pm=E_0\pm A,\qquad
P_L(t)=\cos^2\frac{\Delta E\,t}{2\hbar},\qquad \Delta E=2A."""),
        ("p", r"The symmetric combination of $|L\rangle$ and $|R\rangle$ is the lower level, and the antisymmetric combination lies higher by $\Delta E$. A molecule prepared in $|L\rangle$ is an equal superposition of the two. Its probability $P_L$ of remaining on the left therefore oscillates at the line frequency $\Delta E/h$. A line at 23.87 GHz gives $\Delta E=9.9\times10^{-5}$ eV, or $0.80\,\mathrm{cm}^{-1}$, and a crossing time $\pi\hbar/\Delta E\approx21$ ps."),
        ("p", r"The maser used the same two levels. An inhomogeneous electric field shifts them in opposite directions, so it separates molecules in the upper level from those in the lower level. Molecules in the upper level were focused into a microwave cavity, where they emitted at $\Delta E/h$."),
        ("p", r"The two-level description holds because the next vibrational level of the umbrella motion lies near $950\,\mathrm{cm}^{-1}$, far above the splitting. Rotation changes the splitting slightly, which spreads the inversion lines over a band near 24 GHz. More generally, $H$ must be self-adjoint for $U(t)$ to be unitary, and bounded below for a ground state to exist. For a particle in a potential, $H=P^2/2m+V(X)$ follows from the classical energy, as described under Hamiltonian mechanics. When $H$ depends on time, energy is not conserved and $U$ becomes a time-ordered product, treated under the Schrödinger picture."),
    ],
    "path_integral": [
        ("p", r"A particle released near one point at time $t_i$ is later detected near another point at time $t_f$. The amplitude for this transition is the propagator $K(x_f,t_f;x_i,t_i)=\langle x_f|U(t_f-t_i)|x_i\rangle$. It evolves any initial wave function by $\psi(x_f,t_f)=\int K(x_f,t_f;x_i,t_i)\psi(x_i,t_i)\,dx_i$. The path integral computes $K$ by cutting the time interval into many short steps."),
        ("p", r"Divide $T=t_f-t_i$ into $N$ steps of length $\epsilon=T/N$, and insert a complete set of position states at each intermediate time. For $H=P^2/2m+V(X)$, the Trotter product formula factors each short step into a kinetic and a potential part, with an error of order $\epsilon^2$ per step. The kinetic factor is Gaussian in momentum, and integrating over momentum gives"),
        ("eq", r"""K=\lim_{N\to\infty}\Big(\frac{m}{2\pi i\hbar\epsilon}\Big)^{N/2}
\int dx_1\cdots dx_{N-1}\,e^{iS_N/\hbar},\\
S_N=\sum_{k=0}^{N-1}\epsilon\Big[\frac m2\Big(\frac{x_{k+1}-x_k}{\epsilon}\Big)^2-V(x_k)\Big],
\qquad x_0=x_i,\quad x_N=x_f."""),
        ("p", r"Each set of intermediate positions defines a broken-line path, and $S_N$ is the classical action along it. The limit is written $\int\mathcal Dx\,e^{iS[x]/\hbar}$. The measure has no meaning apart from this limit: the factors $(m/2\pi i\hbar\epsilon)^{1/2}$ diverge as $\epsilon\to0$ and are compensated by the oscillating integrals. In imaginary time the weights become Gaussian probabilities, the limit exists as a Wiener integral, and typical paths are continuous but nowhere differentiable."),
        ("p", r"For a free particle every integral is Gaussian. Integrating over one intermediate point joins two free kernels of durations $t_1$ and $t_2$ into one of duration $t_1+t_2$, because completing the square leaves an exponent quadratic in the endpoints. Repeating the step $N-1$ times gives the exact free propagator:"),
        ("eq", r"""\int K_0(x_f,x;t_2)\,K_0(x,x_i;t_1)\,dx=K_0(x_f,x_i;t_1+t_2),\\
K_0(x_f,x_i;T)=\sqrt{\frac{m}{2\pi i\hbar T}}\,
\exp\Big[\frac{im(x_f-x_i)^2}{2\hbar T}\Big]."""),
        ("p", r"This kernel solves the free Schrödinger equation and tends to $\delta(x_f-x_i)$ as $T\to0$. Its modulus is the same for every endpoint. A particle released from a point therefore reaches all positions with equal amplitude magnitude, while the phase records the velocity $(x_f-x_i)/T$ needed to arrive."),
        ("p", r"Applied to a packet of width $\sigma$, the kernel gives the time-of-flight relation. For $T\gg m\sigma^2/\hbar$ the phase $mx_i^2/2\hbar T$ is negligible across the packet. The remaining integral is a Fourier transform evaluated at the momentum $mx/T$:"),
        ("eq", r"""|\psi(x,T)|^2\;\to\;\frac mT\,\Big|\widetilde\psi\Big(\frac{mx}{T}\Big)\Big|^2,
\qquad T\gg\frac{m\sigma^2}{\hbar}."""),
        ("p", r"Absorption images of ultracold atoms taken after release from a trap therefore record the momentum distribution. Two condensates released a distance $d$ apart overlap with fringes of spacing $hT/(md)$, as observed by Andrews and colleagues in 1997. For sodium with $d=40\,\mu\mathrm m$ and $T=40$ ms the spacing is about $17\,\mu\mathrm m$."),
        ("p", r"The relation assumes free flight. Gravity adds a linear potential, for which the slicing is again exactly Gaussian, whereas interactions during the early expansion must be treated separately. For a charge in a magnetic field the potential term depends on velocity, and the midpoint of each step must be used to obtain the correct Hamiltonian. How the integral is dominated by classical paths when the action is large compared with $\hbar$ is treated under path integral formulation."),
    ],
    "path_integral_formulation": [
        ("p", r"A neutron interferometer is tilted so that one beam travels higher in the Earth's gravitational field than the other. The interference signal oscillates as the tilt changes, although the two beams follow nearly identical classical trajectories. The path-integral formulation computes such phases directly from the classical action."),
        ("p", r"In this formulation the amplitude to go from $x_i$ to $x_f$ is a sum over every history $x(t)$ connecting them, each weighted by $e^{iS[x]/\hbar}$. Here $S=\int L\,dt$ is the classical action and $L=m\dot x^2/2-V(x)$ the Lagrangian. Consider a small deformation $x+\delta x$ with fixed endpoints. The change of action is"),
        ("eq", r"""\delta S=\int_{t_i}^{t_f}\big[-m\ddot x-V'(x)\big]\,\delta x\,dt,\qquad
\delta S=0\ \Longleftrightarrow\ m\ddot x=-V'(x)."""),
        ("p", r"Where $\delta S\neq0$, neighbouring paths have phases that differ by many times $2\pi$ once $S$ is large compared with $\hbar$, and their contributions cancel. Paths near a stationary path add with nearly equal phases. The amplitude is therefore dominated by thin tubes around classical trajectories, within which the action varies by about $\hbar$. Expanding the action to second order about each classical path gives the semiclassical propagator"),
        ("eq", r"""K\simeq\sum_{\mathrm{cl}}\frac{1}{\sqrt{2\pi i\hbar}}
\Big|\frac{\partial^2S_{\mathrm{cl}}}{\partial x_i\,\partial x_f}\Big|^{1/2}
\exp\Big(\frac{i}{\hbar}S_{\mathrm{cl}}-\frac{i\pi\mu}{2}\Big)."""),
        ("p", r"Here $S_{\mathrm{cl}}$ is the action of a classical path between the endpoints, and $\mu$ counts the focal points the path passes. For a free particle, $S_{\mathrm{cl}}=m(x_f-x_i)^2/2T$, and the prefactor reproduces $\sqrt{m/2\pi i\hbar T}$. For Lagrangians at most quadratic in position and velocity the expression is exact. The approximation fails near caustics, where classical paths merge and the prefactor diverges. As $S/\hbar$ grows, interference fringes become finer than any detector resolves, and only the classical motion remains visible."),
        ("p", r"A uniform gravitational field gives a linear potential, so the semiclassical form is exact and only classical paths are needed. A neutron beam has a fixed energy rather than a fixed travel time. Evaluating the time integral of the propagator by stationary phase then replaces $S$ by the reduced action, and the phase along a path becomes $\hbar^{-1}\int p\,dx$. Let the two beams enclose a parallelogram of area $A=H\ell$ in a vertical plane. Their horizontal segments of length $\ell$ differ in height by $H$, and the sloping segments contribute equally to both. Energy conservation lowers the momentum on the upper segment from $p=h/\lambda$ to about $p-m^2gH/p$, so that"),
        ("eq", r"""\Delta\varphi=\frac{\ell}{\hbar}\,\frac{m^2gH}{p}=\frac{mgH\ell}{\hbar v}
=\frac{2\pi m^2g\lambda A}{h^2}."""),
        ("p", r"For neutrons of wavelength $0.1445$ nm and an area of $10\,\mathrm{cm}^2$ in a vertical plane, $\Delta\varphi\approx57$ rad, about nine fringes. Colella, Overhauser and Werner observed this gravitationally induced phase in 1975 by rotating a silicon-crystal neutron interferometer about the incident beam. The classical trajectories do not depend on mass; the mass enters the phase through the ratio $m/\hbar$. At fixed wavelength the phase grows as $m^2$."),
        ("p", r"Light-pulse atom interferometers use the same calculation with laser phases added at each pulse. Their phase $k_{\mathrm{eff}}gT^2$ exceeds $10^6$ rad for rubidium atoms with $T=0.1$ s, and such gravimeters reach parts-per-billion precision in $g$. The derivation of the propagator by time slicing, and its free-particle Gaussian form, are given under path integral."),
    ],
    "schr_dinger_equation": [
        ("p", r"Atomic hydrogen absorbs ultraviolet light only at sharp wavelengths, and its Lyman series ends at 91.2 nm, the ionization threshold of 13.6 eV. A wave equation for the electron's amplitude must reproduce these numbers. Its form follows from the de Broglie relations and the nonrelativistic energy."),
        ("p", r"A plane wave $e^{i(\mathbf k\cdot\mathbf x-\omega t)}$ with $\mathbf p=\hbar\mathbf k$ and $E=\hbar\omega$ satisfies $i\hbar\partial_t\psi=E\psi$ and $-i\hbar\nabla\psi=\mathbf p\psi$. Requiring $E=p^2/2m+V$ for every component, and linearity so that superpositions of solutions remain solutions, gives"),
        ("eq", r"""i\hbar\frac{\partial\psi}{\partial t}=-\frac{\hbar^2}{2m}\nabla^2\psi+V(\mathbf x)\,\psi,
\qquad i\hbar\frac{d}{dt}|\psi(t)\rangle=H|\psi(t)\rangle."""),
        ("p", r"For a constant potential this argument is complete. For a varying $V$ the equation is postulated, and its predictions test it. It contains a single time derivative, so the wave function at one instant fixes it at all later times. For real $V$, multiplying by $\psi^*$ and subtracting the complex conjugate equation gives a local conservation law:"),
        ("eq", r"""\frac{\partial|\psi|^2}{\partial t}+\nabla\cdot\mathbf j=0,\qquad
\mathbf j=\frac{\hbar}{m}\,\mathrm{Im}\big(\psi^*\nabla\psi\big)."""),
        ("p", r"Probability flows from one region to another, but it is not created or destroyed. An imaginary part of $V$ would act as a source or sink, which is how absorption into unobserved channels is sometimes modelled. If $V$ does not depend on time, separable solutions $\psi=\phi(\mathbf x)e^{-iEt/\hbar}$ reduce the equation to the eigenvalue problem $H\phi=E\phi$. Normalizable solutions exist only for particular energies, which is the origin of discrete levels. A general preparation is a superposition of such stationary states, and its probability density changes in time only through interference between components of different energy."),
        ("p", r"For hydrogen, $V=-k/r$ with $k=e^2/4\pi\varepsilon_0$. Try the spherically symmetric function $\phi=e^{-r/a}$, for which $\nabla^2\phi=(1/a^2-2/ar)\phi$. Substitution gives"),
        ("eq", r"""H\phi=\Big[-\frac{\hbar^2}{2ma^2}+\Big(\frac{\hbar^2}{ma}-k\Big)\frac1r\Big]\phi,\\
a_0=\frac{\hbar^2}{mk}=0.0529\ \mathrm{nm},\qquad
E_1=-\frac{mk^2}{2\hbar^2}=-13.6\ \mathrm{eV}."""),
        ("p", r"The $1/r$ term must vanish for $\phi$ to be an eigenfunction, which fixes the Bohr radius $a_0$. The remaining constant is the ground-state energy. The full solution gives $E_n=E_1/n^2$, so the Lyman limit lies at $hc/|E_1|=91.1$ nm. Replacing $m$ by the reduced mass of electron and proton moves it to the observed 91.2 nm."),
        ("p", r"The equation treats the electron as nonrelativistic. In hydrogen its typical speed is $\alpha c$, with $\alpha\approx1/137$, so corrections of relative size $\alpha^2\approx5\times10^{-5}$ appear. They split levels of equal $n$ into the fine structure described under relativistic quantum mechanics. Spin, nuclear size and the coupling to the radiation field add smaller corrections, such as the Lamb shift. The abstract form $i\hbar\,d|\psi\rangle/dt=H|\psi\rangle$ applies to any closed system, and the organization of its solutions in time is treated under the Schrödinger picture."),
    ],
    "unitary_operator": [
        ("p", r"A lossless beam splitter divides a light beam between two output ports. Whatever phase is then added in one arm of an interferometer, the detection probabilities at the outputs add to one. Transformations that preserve probabilities in this way are tightly restricted, and Wigner's theorem states the restriction."),
        ("p", r"A pure state is a ray, a unit vector defined up to a phase. Consider a bijective map of rays that preserves every transition probability $|\langle\phi|\psi\rangle|^2$. Wigner's theorem states that the map is implemented on vectors by an operator that is either unitary or antiunitary, unique up to an overall phase:"),
        ("eq", r"""\langle U\phi|U\psi\rangle=\langle\phi|\psi\rangle,\qquad
\langle A\phi|A\psi\rangle=\langle\phi|\psi\rangle^*,\qquad
A(a\phi+b\psi)=a^*A\phi+b^*A\psi."""),
        ("p", r"A unitary operator is linear and satisfies $U^\dagger U=UU^\dagger=I$; an antiunitary operator is antilinear. Transformations that can be reached continuously from the identity, such as time evolution, rotations and translations, are unitary. Each is the square of a transformation half as large, and the square of either kind of operator is unitary. Their self-adjoint generators are discussed under symmetry in quantum mechanics."),
        ("p", r"A single photon in two spatial modes shows the unitary case. A lossless beam splitter with transmission amplitude $t$ and reflection amplitude $r$ acts on the two-component amplitude vector. Conservation of total probability for every input is equivalent to $B^\dagger B=I$:"),
        ("eq", r"""B=\begin{pmatrix}t&r\\r&t\end{pmatrix},\qquad |t|^2+|r|^2=1,\qquad t^*r+r^*t=0."""),
        ("p", r"The second condition places the reflected amplitude at a phase of $\pm\pi/2$ relative to the transmitted one. Take the balanced case $t=1/\sqrt2$ and $r=i/\sqrt2$. A Mach--Zehnder interferometer applies the splitter, a phase $\varphi$ in one arm and a second splitter. For a photon entering port 1, the output probabilities are"),
        ("eq", r"""U(\varphi)=B\begin{pmatrix}e^{i\varphi}&0\\0&1\end{pmatrix}B,\qquad
p_1=\sin^2\frac\varphi2,\qquad p_2=\cos^2\frac\varphi2."""),
        ("p", r"Scanning $\varphi$ moves probability between the detectors and keeps the sum at one, which is unitarity in measured form. Absorption in one arm, with amplitude transmission $\eta<1$, makes the $2\times2$ matrix non-unitary. The missing probability goes into other modes, and the fringe visibility falls to $2\eta/(1+\eta^2)$."),
        ("p", r"Time reversal is the antiunitary case. It must leave positions unchanged, reverse momenta and turn $e^{-iHt/\hbar}$ into $e^{iHt/\hbar}$. A unitary operator could do this only by anticommuting with $H$, which would map each energy $E$ onto $-E$. That is impossible for an energy bounded below, so time reversal is antiunitary. For one spin one-half it is $T=-i\sigma_yK$, with $K$ complex conjugation in the $\sigma_z$ basis, and"),
        ("eq", r"""T^2=-I,\qquad T^2=(-1)^N\ \text{for }N\text{ electrons},\\
[H,T]=0,\quad H\psi=E\psi\ \Longrightarrow\ H(T\psi)=E\,T\psi,\quad \langle T\psi|\psi\rangle=0."""),
        ("p", r"The orthogonality follows from antilinearity. The rule $\langle A\phi|A\chi\rangle=\langle\chi|\phi\rangle$ with $\phi=\psi$ and $\chi=T\psi$ gives $\langle T\psi|T^2\psi\rangle=\langle T\psi|\psi\rangle$. With $T^2=-I$ the left side equals $-\langle T\psi|\psi\rangle$, so both vanish. Every energy level of a system with an odd number of electrons is therefore at least two-fold degenerate when no magnetic field acts. This is Kramers' theorem."),
        ("p", r"The ion $\mathrm{Er}^{3+}$ has eleven 4f electrons and a ground multiplet with $J=15/2$, sixteen states. An electric crystal field of any symmetry, however low, is even under time reversal. It splits the multiplet into at most eight levels, each a Kramers doublet. The ion $\mathrm{Pr}^{3+}$ has two 4f electrons and $J=4$, and a low-symmetry field can split its nine states into nine singlets. A magnetic field is odd under time reversal and splits each Kramers doublet linearly in the field, which produces the electron paramagnetic resonance lines of odd-electron rare-earth ions."),
        ("p", r"The degeneracy survives any electric field, spin-orbit coupling and lattice distortion. It is lifted only by perturbations odd under time reversal, such as an applied magnetic field or the internal field of magnetic order. Time evolution generated by the Hamiltonian is the most important unitary map; the Fourier transform and the change between Schrödinger and Heisenberg pictures are others."),
    ],
    "hamiltonian_mechanics": [
        ("p", r"A pendulum, a planet or a charged particle in a magnet is fully described at one instant by its coordinates and momenta. As time passes, each point of this phase space moves, and a small patch of initial conditions deforms while keeping its area. Hamiltonian mechanics generates this motion from one function, the energy $H(q,p)$."),
        ("p", r"Start from a Lagrangian $L(q,\dot q)$ and define the canonical momentum $p=\partial L/\partial\dot q$. The Legendre transform $H=p\dot q-L$, written as a function of $q$ and $p$, yields Hamilton's equations. For any phase-space function $f(q,p)$ they combine into one rule through the Poisson bracket:"),
        ("eq", r"""\dot q_i=\frac{\partial H}{\partial p_i},\qquad \dot p_i=-\frac{\partial H}{\partial q_i},
\qquad \frac{df}{dt}=\{f,H\},\\
\{f,g\}=\sum_i\Big(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\Big),\qquad \{q_i,p_j\}=\delta_{ij}."""),
        ("p", r"Three consequences follow. A function $G$ with $\{G,H\}=0$ is conserved, and the flow that $G$ generates leaves $H$ unchanged, which links symmetry to conservation as in Noether's theorem. The flow has zero divergence, so phase-space volume is conserved, which is Liouville's theorem. The bracket of a coordinate with its momentum is the same constant for every system."),
        ("p", r"Quantum mechanics keeps this structure and changes the bracket. Dirac's rule replaces functions by operators and the Poisson bracket by a commutator divided by $i\hbar$:"),
        ("eq", r"""\{f,g\}\;\longrightarrow\;\frac{1}{i\hbar}\big[\hat f,\hat g\big],\qquad
[\hat q_i,\hat p_j]=i\hbar\,\delta_{ij},\qquad
\frac{d\hat f}{dt}=\frac{1}{i\hbar}\big[\hat f,\hat H\big]."""),
        ("p", r"The equation of motion keeps its form and becomes the Heisenberg equation. Conserved quantities and symmetry generators carry over, and the conservation of phase-space volume is replaced by the unitarity of time evolution."),
        ("p", r"A charge $q$ of mass $m$ moving in the plane perpendicular to a uniform field $B$, with $qB>0$, shows the rule at work. In the symmetric gauge the canonical momenta are $p_x$ and $p_y$, but the velocity is fixed by the kinetic momenta $\pi_x=p_x+qBy/2$ and $\pi_y=p_y-qBx/2$. Their Poisson bracket does not vanish:"),
        ("eq", r"""\{\pi_x,\pi_y\}=qB\;\longrightarrow\;[\hat\pi_x,\hat\pi_y]=i\hbar qB,\qquad
H=\frac{\hat\pi_x^2+\hat\pi_y^2}{2m},\\
E_n=\hbar\omega_c\Big(n+\frac12\Big),\qquad \omega_c=\frac{qB}{m}."""),
        ("p", r"Classically, the bracket produces circular motion at the cyclotron frequency $\omega_c$. Quantum mechanically, $\hat\pi_x/\sqrt{qB}$ and $\hat\pi_y/\sqrt{qB}$ form a canonical pair, and $H$ becomes a harmonic oscillator of frequency $\omega_c$. These Landau levels are spaced by 0.116 meV for a free electron in 1 T, equivalent to a temperature of 1.3 K. The orbit centre forms a second canonical pair that commutes with $H$, so each level holds $qB/h$ states per unit area. Landau quantization underlies the Shubnikov--de Haas oscillations and the quantum Hall effect, seen when the level spacing exceeds the thermal energy."),
        ("p", r"Dirac's rule is exact for the canonical pairs and for functions at most quadratic in them. It cannot hold for all higher polynomials at once: the Groenewold--van Hove theorem shows that no consistent map sends every Poisson bracket to the corresponding commutator. Operator ordering, such as $qp\to(\hat q\hat p+\hat p\hat q)/2$, then matters, and the brackets differ at order $\hbar^2$. The classical Hamiltonian guides the choice of quantum Hamiltonian but does not fix it uniquely. The operator side of this correspondence is developed under the canonical commutation relation and the Heisenberg picture."),
    ],
    "perturbation_theory": [
        ("p", r"An electric field of 100 kV/cm splits the $n=2$ level of hydrogen into components hundreds of gigahertz apart, while the ground level moves by only a few megahertz. Both shifts come from the same weak addition to the atomic Hamiltonian. Perturbation theory explains why one shift is linear in the field and the other quadratic."),
        ("p", r"Write $H=H_0+\lambda V$, where the eigenstates $|n\rangle$ and energies $E_n^{(0)}$ of $H_0$ are known and $\lambda$ counts powers of the perturbation. Expand the exact eigenvalue and eigenvector in powers of $\lambda$ and insert them into $H|\psi_n\rangle=E_n|\psi_n\rangle$. Projecting the equation at each order onto $\langle n|$ and onto $\langle m|$ with $m\neq n$ gives the energy and the admixed states:"),
        ("eq", r"""E_n=E_n^{(0)}+\lambda V_{nn}
+\lambda^2\sum_{m\neq n}\frac{|V_{mn}|^2}{E_n^{(0)}-E_m^{(0)}}+O(\lambda^3),\\
|\psi_n\rangle=|n\rangle+\lambda\sum_{m\neq n}\frac{V_{mn}}{E_n^{(0)}-E_m^{(0)}}|m\rangle+O(\lambda^2),
\qquad V_{mn}=\langle m|V|n\rangle."""),
        ("p", r"The expansion is useful when every coupling is small compared with the corresponding gap, $|V_{mn}|\ll|E_n^{(0)}-E_m^{(0)}|$. For the ground state every denominator is negative, so the second-order shift always lowers the energy. The sum runs over the complete set of unperturbed states, including any continuum."),
        ("p", r"For an electron in a uniform field $F$ along $z$, the perturbation is $V=eFz$. The hydrogen ground state has even parity and $z$ is odd, so $V_{nn}=0$. The leading shift is quadratic, $\Delta E=-\alpha_{\mathrm{pol}}F^2/2$, with static polarizability $\alpha_{\mathrm{pol}}=\tfrac92(4\pi\varepsilon_0)a_0^3$. At 100 kV/cm this gives 5.6 MHz. The bound states supply only 81 percent of the polarizability; the ionization continuum supplies the rest."),
        ("p", r"The $n=2$ level behaves differently because the $2s$ and $2p$ states have the same unperturbed energy. The denominators vanish, and the expansion must start by diagonalizing $V$ within the degenerate subspace. Only $2s$ and $2p_0$ are coupled, and"),
        ("eq", r"""\langle2s|z|2p_0\rangle=-3a_0,\qquad E=E_2\pm3ea_0F,\qquad
|\pm\rangle=\frac{|2s\rangle\mp|2p_0\rangle}{\sqrt2}."""),
        ("p", r"The mixed states carry permanent electric dipoles of $\mp3ea_0$, so their shift is linear in $F$. At 100 kV/cm the outer components lie $\pm384$ GHz from the unperturbed level, while $2p_{\pm1}$ remains unshifted. Stark observed this linear splitting of the Balmer lines in 1913."),
        ("p", r"The degenerate treatment assumes that the Stark coupling exceeds the small splittings omitted from the nonrelativistic $H_0$. The fine-structure splitting of $n=2$ is 10.9 GHz, and the Lamb shift between $2s_{1/2}$ and $2p_{1/2}$ is 1.06 GHz. Below a few hundred volts per centimetre the coupling is smaller than the Lamb shift, and the shift of $2s_{1/2}$ becomes quadratic again. In any static field the electron can also tunnel out of the atom, at a rate that vanishes faster than any power of $F$. The levels are therefore resonances, and the series in $F$ is asymptotic rather than convergent. A perturbation that oscillates in time produces transitions instead of shifts. The same expansion then gives Fermi's golden rule for transition rates, used for spectral lines and scattering."),
    ],
    "quantum_chaos": [
        ("p", r"Slow neutrons striking heavy nuclei excite many narrow resonances, and neighbouring resonances are rarely found close together. The levels of a particle in a rectangular box with incommensurate sides behave differently, because near coincidences are common there. The difference reflects the classical motion, which is regular in the box and chaotic or highly complex in the nucleus."),
        ("p", r"Consider two neighbouring levels that may be coupled. When the system is invariant under time reversal, the Hamiltonian can be chosen real and symmetric. The $2\times2$ block and its level spacing are"),
        ("eq", r"""H=\begin{pmatrix}h_{11}&h_{12}\\h_{12}&h_{22}\end{pmatrix},\qquad
s=E_+-E_-=\sqrt{(h_{11}-h_{22})^2+4h_{12}^2}."""),
        ("p", r"A degeneracy requires two independent conditions, $h_{11}=h_{22}$ and $h_{12}=0$. If the matrix elements are spread smoothly, the probability of a spacing below $s$ scales as $s^2$, and the spacing density vanishes linearly. This is level repulsion, described by von Neumann and Wigner. Independent Gaussian matrix elements define the Gaussian orthogonal ensemble. Scaling the spacing to unit mean gives the Wigner surmise. Without time-reversal invariance $h_{12}$ is complex, three conditions are needed, and the density vanishes as $s^2$:"),
        ("eq", r"""P_{\mathrm{Poisson}}(s)=e^{-s},\qquad
P_{\mathrm{GOE}}(s)=\frac{\pi s}{2}\,e^{-\pi s^2/4},\\
P_{\mathrm{GUE}}(s)=\frac{32s^2}{\pi^2}\,e^{-4s^2/\pi}."""),
        ("p", r"In an integrable system, levels carry independent quantum numbers, and levels with different labels do not repel. Their sequence is uncorrelated, which gives the Poisson law, as Berry and Tabor argued for generic integrable systems. The laws differ most at small spacing. The probability of a spacing below one tenth of the mean is 0.095 for Poisson statistics, 0.0078 for the Wigner surmise and 0.0011 for the unitary ensemble."),
        ("p", r"Bohigas, Giannoni and Schmit conjectured in 1984 that quantum systems with a chaotic classical limit follow these random-matrix laws. The conjecture is supported by stadium and Sinai billiards, by microwave cavities of the same shapes, by hydrogen in strong magnetic fields and by the nuclear data ensemble of neutron resonances. Semiclassical sums over periodic orbits explain the spectral correlations. A general proof remains open."),
        ("p", r"These statistics require care. Before any comparison the spectrum is unfolded, by rescaling energies with the smooth level density so that the mean spacing is one everywhere. Levels must also be sorted by exact symmetry. Independent sequences of different parity or angular momentum superpose without repulsion and look Poissonian. The random-matrix laws hold only over energy ranges smaller than $h$ divided by the period of the shortest periodic orbit. Eigenstates concentrated along unstable periodic orbits, called scars, show that eigenfunctions also deviate from random behaviour."),
        ("p", r"In the time domain, chaos limits how long a wave packet follows a single classical trajectory, a theme of quantum dynamics. The random-matrix character of chaotic eigenstates also underlies thermalization of isolated systems in quantum statistical mechanics."),
    ],
    "quantum_dynamics": [
        ("p", r"A picosecond laser pulse excites an atom into a superposition of Rydberg levels near $n=50$. The electron then moves as a localized packet around a Kepler orbit. After a few revolutions it spreads around the orbit, and later it reassembles. Each stage follows from the spacing of the energy levels."),
        ("p", r"At short times the centre of a narrow packet follows Newton's law. Differentiating expectation values with the Schrödinger equation gives Ehrenfest's theorem:"),
        ("eq", r"""\frac{d\langle X\rangle}{dt}=\frac{\langle P\rangle}{m},\qquad
\frac{d\langle P\rangle}{dt}=-\langle V'(X)\rangle\approx-V'(\langle X\rangle)."""),
        ("p", r"The approximation holds while the force varies little across the packet. For a harmonic potential it is exact at all times, because $V'$ is linear. In other potentials the packet spreads, and the centre no longer obeys a closed classical equation."),
        ("p", r"The energy spectrum shows how long the classical stage lasts. Expand the packet in energy eigenstates with weights $|c_n|^2$ concentrated around $\bar n$, and expand the energies to second order in $n-\bar n$. The amplitude to return to the initial state and the two resulting times are"),
        ("eq", r"""A(t)=\sum_n|c_n|^2e^{-iE_nt/\hbar},\qquad
E_n\approx E_{\bar n}+E'(n-\bar n)+\frac{E''}{2}(n-\bar n)^2,\\
T_{\mathrm{cl}}=\frac{2\pi\hbar}{|E'|},\qquad T_{\mathrm{rev}}=\frac{4\pi\hbar}{|E''|}."""),
        ("p", r"The linear term brings every component back in phase after the classical period $T_{\mathrm{cl}}$. The quadratic term slowly dephases the components. With a spread $\Delta n$ in $n$, the packet covers the whole orbit after a time of order $T_{\mathrm{rev}}/(2\pi\Delta n^2)$. At $T_{\mathrm{rev}}$ every quadratic phase is a multiple of $2\pi$, because $n-\bar n$ is an integer, and the packet reforms. At rational fractions of $T_{\mathrm{rev}}$ it appears as several smaller packets, the fractional revivals."),
        ("p", r"For hydrogen $E_n=-R/n^2$ with $R=13.6$ eV, so $E'=2R/n^3$ and $E''=-6R/n^4$. Then $T_{\mathrm{cl}}=\pi\hbar n^3/R$ equals the Kepler period of the classical orbit with the same energy, and $T_{\mathrm{rev}}=(2\bar n/3)T_{\mathrm{cl}}$. For $\bar n=50$ this gives $T_{\mathrm{cl}}=19$ ps and $T_{\mathrm{rev}}=0.63$ ns. Yeazell, Mallalieu and Stroud observed the collapse and revival of such Rydberg packets in 1990."),
        ("p", r"Higher terms limit the picture. The cubic term adds a phase of about $8(\Delta n)^3/\bar n$ at $T_{\mathrm{rev}}$, so a clean revival requires $(\Delta n)^3\ll\bar n/8$. A direct sum for $\bar n=50$ gives a return probability of 0.91 at the revival for $\Delta n=1$, but only about 0.5 for $\Delta n=2.5$. An evenly spaced spectrum, as in the quantum harmonic oscillator, never dephases. In a classically chaotic system, agreement with a single trajectory lasts only about the Ehrenfest time, of order $\lambda^{-1}\ln(S/\hbar)$, where $\lambda$ is the Lyapunov exponent and $S$ a typical action. This short time scale is one signature of quantum chaos."),
    ],
    "quantum_stochastic_calculus": [
        ("p", r"Light leaks out of an optical cavity through a partly transmitting mirror. The emerging beam carries the cavity field, and the same mirror admits vacuum fluctuations from outside. Quantum stochastic calculus describes this exchange with the external field in infinitesimal time steps, in the way Itô calculus describes classical noise."),
        ("p", r"Treat the external field as a sequence of independent time bins of length $dt$ that pass the mirror one after another. Let $b_{\mathrm{in}}(t)$ be the incoming field operator, with $[b_{\mathrm{in}}(t),b_{\mathrm{in}}^\dagger(t')]=\delta(t-t')$. Define the increment $dA_t=\int_t^{t+dt}b_{\mathrm{in}}(s)\,ds$. For an incoming vacuum, products of increments obey the quantum Itô table:"),
        ("eq", r"""dA_t\,dA_t^\dagger=dt,\qquad dA_t^\dagger\,dA_t=dA_t\,dA_t=dA_t^\dagger\,dA_t^\dagger=0,
\qquad dt\,dA_t=0."""),
        ("p", r"The asymmetry between the two orderings is the vacuum noise. Creating and then removing a quantum in an empty bin leaves a term proportional to $dt$, whereas the reverse order gives zero. A classical Wiener increment gives $dW^2=dt$ for either order. For a thermal input with mean occupation $N$, the table becomes $dA\,dA^\dagger=(N+1)\,dt$ and $dA^\dagger dA=N\,dt$."),
        ("p", r"Let the system couple to the field through an operator $L$, for example $L=\sqrt\kappa\,a$ for a cavity mode $a$ with energy decay rate $\kappa$. Hudson and Parthasarathy showed that the joint unitary evolution of system and field obeys"),
        ("eq", r"""dU_t=\Big[-\Big(\frac{i}{\hbar}H+\frac12L^\dagger L\Big)dt
+L\,dA_t^\dagger-L^\dagger dA_t\Big]U_t."""),
        ("p", r"The term $-\frac12L^\dagger L\,dt$ is required by unitarity. In $d(U^\dagger U)=dU^\dagger U+U^\dagger dU+dU^\dagger dU$, the last product contributes $L^\dagger L\,dA\,dA^\dagger=L^\dagger L\,dt$, which cancels it exactly. Averaging over the vacuum field gives the Lindblad master equation written under quantum jump. The calculus also yields the outgoing field: it equals the incoming field plus the emission of the system,"),
        ("eq", r"""dA^{\mathrm{out}}_t=L\,dt+dA_t,\qquad
b_{\mathrm{out}}=b_{\mathrm{in}}+\sqrt\kappa\,a."""),
        ("p", r"For a cavity driven through the same mirror by a coherent beam of amplitude $\beta$, detuned by $\Delta$ from resonance, the mean cavity field obeys $\dot a=-(i\Delta+\kappa/2)a-\sqrt\kappa\,\beta$. In the steady state the reflection coefficient is"),
        ("eq", r"""r(\Delta)=\frac{b_{\mathrm{out}}}{\beta}=\frac{2i\Delta-\kappa}{2i\Delta+\kappa},\qquad
|r|=1,\qquad r(0)=-1."""),
        ("p", r"All light returns, as expected for a lossless single-sided cavity, but its phase $\pi-2\arctan(2\Delta/\kappa)$ turns by $2\pi$ across a window of width about $\kappa$. A superconducting qubit that shifts the cavity frequency by $\pm\chi$ therefore imprints reflected phases that differ by $4\arctan(2\chi/\kappa)$. The difference reaches $\pi$ at $\chi=\kappa/2$, where the two reflected coherent states are most distinguishable for a given input flux. Pound--Drever--Hall laser locking uses the same phase near resonance."),
        ("p", r"The calculus rests on a Markov approximation. The coupling to the external field must be flat in frequency over a band much wider than $\kappa$, and the rotating-wave approximation requires $\kappa$ far below the cavity frequency. Optical cavities and microwave resonators satisfy both conditions well. Structured reservoirs, such as photonic band edges, require a memory kernel instead. Photon counting on the same output field gives the quantum-jump trajectories of quantum optics."),
    ],
    "relativistic_quantum_mechanics": [
        ("p", r"The $n=2$ level of hydrogen is not a single level. Spectroscopy resolves components 10.9 GHz apart, about $1.3\times10^{-5}$ of the binding energy, while the Schrödinger equation predicts exact degeneracy. The electron moves at about $\alpha c$, so relativistic kinematics is the natural place to look for the splitting."),
        ("p", r"Replace the nonrelativistic energy by $E^2=p^2c^2+m^2c^4$ and substitute $E\to i\hbar\partial_t$ and $\mathbf p\to-i\hbar\nabla$. For a spin-zero particle in an electrostatic potential energy $V$, this gives the Klein--Gordon equation and its conserved density:"),
        ("eq", r"""\big(i\hbar\partial_t-V\big)^2\phi=\big(-\hbar^2c^2\nabla^2+m^2c^4\big)\phi,\\
\rho=\frac{i\hbar}{2mc^2}\big(\phi^*\partial_t\phi-\phi\,\partial_t\phi^*\big)-\frac{V}{mc^2}|\phi|^2."""),
        ("p", r"The equation is of second order in time, so $\phi$ and $\partial_t\phi$ are independent initial data, and $\rho$ is not positive. A stationary solution with energy $E$ has $\rho=(E-V)|\phi|^2/mc^2$, which is negative for the negative-energy solutions that the quadratic relation allows. The density is therefore a charge density, not a probability density. A single-particle reading is consistent only when the potential is weak compared with $2mc^2$ and varies slowly over the Compton wavelength $\hbar/mc$, which is 386 fm for an electron. Stronger or steeper potentials create particle-antiparticle pairs, as the Klein paradox shows, and require quantum field theory."),
        ("p", r"For an attractive Coulomb potential $V=-Z\alpha\hbar c/r$, the radial equation keeps the hydrogen form with $l(l+1)$ replaced by $l(l+1)-(Z\alpha)^2$. The exact levels and their expansion in $Z\alpha$ are"),
        ("eq", r"""E_{nl}=mc^2\Big[1+\frac{(Z\alpha)^2}
{\big(n-l-\frac12+\sqrt{(l+\frac12)^2-(Z\alpha)^2}\big)^2}\Big]^{-1/2},\\
E_{nl}\approx mc^2\Big[1-\frac{(Z\alpha)^2}{2n^2}
-\frac{(Z\alpha)^4}{2n^4}\Big(\frac{n}{l+\frac12}-\frac34\Big)\Big]."""),
        ("p", r"The second term is the Bohr energy. The third depends on $l$, so relativistic kinematics does lift the degeneracy. For hydrogen it is smaller than the Bohr energy by a factor of order $\alpha^2$, about $10^{-5}$, which matches the observed scale of the splitting. At $n=2$ it places $2s$ below $2p$ by $mc^2\alpha^4/12$, which is 29 GHz. Observation disagrees: $2s_{1/2}$ and $2p_{1/2}$ nearly coincide, and the 10.9 GHz splitting separates $2p_{1/2}$ from $2p_{3/2}$. Schrödinger met this mismatch before publishing his nonrelativistic equation. The Dirac equation, which includes spin, replaces $l+\frac12$ by $j+\frac12$ and reproduces the observed pattern, apart from the 1.06 GHz Lamb shift."),
        ("p", r"For spin-zero particles the Klein--Gordon equation is correct. In pionic atoms a negative pion replaces the electron. X-ray energies between orbits of high $l$, where the strong interaction is negligible, are calculated with this equation and small QED corrections. Such measurements determine the charged-pion mass. The exact formula also marks a limit. For $s$ states the square root becomes imaginary when $Z\alpha>\frac12$, that is for $Z\geq69$. A point nucleus is then unphysical, and the finite nuclear size must be included."),
    ],
    "schr_dinger_picture": [
        ("p", r"Two atomic levels are swept through an avoided crossing by a ramped electric field. If the sweep is slow, the atom ends in the other diabatic level; if it is fast, the atom stays where it started. A prediction for a Hamiltonian that changes in time is most directly written for a time-dependent state, which is the Schrödinger picture."),
        ("p", r"In this picture observables, such as a level projector, stay fixed, and the state carries all the time dependence. For a Hamiltonian $H(t)$, the evolution operator obeys $i\hbar\,\partial_tU(t,t_0)=H(t)U(t,t_0)$. When Hamiltonians at different times do not commute, the solution is a time-ordered exponential:"),
        ("eq", r"""|\psi(t)\rangle=U(t,t_0)|\psi(t_0)\rangle,\qquad
U(t,t_0)=\mathcal T\exp\Big[-\frac{i}{\hbar}\int_{t_0}^{t}H(s)\,ds\Big]."""),
        ("p", r"The ordering symbol $\mathcal T$ places operators at later times to the left. Expanding it gives the Dyson series, the starting point of time-dependent perturbation theory. Without the ordering, the exponential gives wrong predictions whenever $[H(s),H(s')]\neq0$. A measurement at an intermediate time is applied to the state at that time, so a sequence of operations is followed in the order in which it occurs."),
        ("p", r"For the swept atom, let $|1\rangle$ and $|2\rangle$ be the diabatic states, whose energies cross linearly in time at rate $\alpha$, and let $\Delta$ be the minimum gap set by their coupling. Then"),
        ("eq", r"""H(t)=\frac12\big(\alpha t\,\sigma_z+\Delta\,\sigma_x\big),\qquad
P_{1\to1}=\exp\Big(-\frac{\pi\Delta^2}{2\hbar\alpha}\Big)."""),
        ("p", r"Here $\sigma_z$ and $\sigma_x$ are Pauli matrices in the diabatic basis, and $P_{1\to1}$ is the probability of remaining in $|1\rangle$ after the crossing. Landau, Zener, Stückelberg and Majorana obtained this result in 1932 by solving the time-dependent equation exactly. For a sweep of duration $t$ centred on the crossing, the naive exponential of the integrated Hamiltonian would give a rotation about $x$ by the angle $\Delta t/\hbar$. That prediction oscillates with the duration and does not depend on the sweep rate."),
        ("p", r"For a slow sweep, $\hbar\alpha\ll\Delta^2$, the state follows the instantaneous eigenstate, whose character changes from $|1\rangle$ to $|2\rangle$; this adiabatic passage transfers the population completely. For a fast sweep the state cannot follow and remains in $|1\rangle$. In frequency units the exponent is $\pi^2f_\Delta^2/\dot\nu$, where $f_\Delta=\Delta/h$ and $\dot\nu$ is the sweep rate. A gap of 10 MHz crossed at $1\,\mathrm{GHz}/\mu\mathrm s$ leaves 37 percent in the initial diabatic state."),
        ("p", r"Rubbmark, Kash, Littman and Kleppner measured this dependence with Rydberg atoms in 1981, and superconducting qubits reproduce it with swept flux. To lowest order in $\Delta$ the transition probability is $\pi\Delta^2/2\hbar\alpha$, which is what time-dependent perturbation theory gives. In the slow limit the diabatic probability vanishes faster than any power of $\alpha$, so no finite order of an expansion in the sweep rate captures it."),
        ("p", r"The formula assumes an isolated pair of levels and a sweep extending far beyond the crossing time, the larger of $\Delta/\alpha$ and $\sqrt{\hbar/\alpha}$. Finite sweeps add small oscillations, and dephasing during the passage reduces the adiabatic transfer. The Heisenberg picture yields the same probabilities, but its equations contain $U^\dagger H(t)U$ and therefore require the same time-ordered evolution. The position-space form of the same evolution law is the Schrödinger equation."),
    ],
}

# References locate the established framework for each worked calculation; the
# equations and numbers above were checked separately with symbolic and numerical scripts.
REFERENCES = {
    "creation_and_annihilation_operators": [
        ("cond-mat/9806038", "F. Dalfovo, S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of Bose-Einstein condensation in trapped gases; Bogoliubov theory, the excitation spectrum, sound, healing length and depletion."),
        ("cond-mat/9708237", "E. Zaremba, Sound propagation in a cylindrical Bose-condensed gas; pulses in elongated condensates travel at a speed set by the density averaged over the cross-section."),
    ],
    "hamiltonian_quantum_mechanics": [
        ("1508.06951", "V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; self-adjoint Hamiltonians, spectral decomposition and the unitary evolution they generate."),
    ],
    "path_integral": [
        ("quant-ph/0004090", "R. MacKenzie, Path Integral Methods and Applications; time slicing, the free-particle Gaussian integrals and the propagator."),
        ("hep-th/9302097", "C. Grosche, An Introduction into the Feynman Path Integral; the lattice definition of the path integral and its ordering prescriptions."),
    ],
    "path_integral_formulation": [
        ("quant-ph/0004090", "R. MacKenzie, Path Integral Methods and Applications; stationary phase, the classical limit and the semiclassical propagator."),
        ("0712.3703", "A. D. Cronin, J. Schmiedmayer and D. E. Pritchard, Atom Interferometers; gravitationally induced phases in neutron and atom interferometers and light-pulse gravimetry."),
    ],
    "schr_dinger_equation": [
        ("2007.14798", "A. Galler, J. Canfield and J. K. Freericks, Schrödinger's original quantum-mechanical solution for hydrogen; the 1926 wave-mechanical derivation of the hydrogen spectrum."),
    ],
    "unitary_operator": [
        ("0808.0779", "R. Simon, N. Mukunda, S. Chaturvedi and V. Srinivasan, Two elementary proofs of the Wigner theorem on symmetry in quantum mechanics; symmetries of rays as unitary or antiunitary operators."),
        ("1508.06951", "V. Moretti, Mathematical Foundations of Quantum Mechanics: An Advanced Short Course; unitary and antiunitary operators and the representation of symmetries."),
    ],
    "hamiltonian_mechanics": [
        ("math-ph/9809011", "M. J. Gotay, Obstructions to Quantization; the Groenewold-van Hove theorem and the limits of the Poisson-bracket to commutator rule."),
        ("1606.06687", "D. Tong, Lectures on the Quantum Hall Effect; Landau levels from the kinetic momenta, their degeneracy and the quantum Hall effect."),
    ],
    "perturbation_theory": [
        ("physics/0010038", "U. D. Jentschura, Resummation of the Divergent Perturbation Series for a Hydrogen Atom in an Electric Field; the Stark perturbation series and its divergence."),
    ],
    "quantum_chaos": [
        ("cond-mat/9707301", "T. Guhr, A. Mueller-Groeling and H. A. Weidenmueller, Random Matrix Theories in Quantum Physics: Common Concepts; level spacing statistics, the Wigner surmise, nuclear data and chaotic billiards."),
        ("1509.06411", "L. D'Alessio, Y. Kafri, A. Polkovnikov and M. Rigol, From Quantum Chaos and Eigenstate Thermalization to Statistical Mechanics and Thermodynamics; random-matrix statistics and thermalization of isolated systems."),
    ],
    "quantum_dynamics": [
        ("quant-ph/0401031", "R. W. Robinett, Quantum wave packet revivals; classical period, revival time, fractional revivals and Rydberg wave packets."),
    ],
    "quantum_stochastic_calculus": [
        ("1408.5686", "K. R. Parthasarathy, Quantum Stochastic Calculus and Quantum Gaussian Processes; the Hudson-Parthasarathy calculus on boson Fock space."),
        ("1611.00375", "J. Combes, J. Kerckhoff and M. Sarovar, The SLH framework for modeling quantum input-output networks; quantum stochastic differential equations and input-output relations."),
        ("0810.4729", "A. A. Clerk, M. H. Devoret, S. M. Girvin, F. Marquardt and R. J. Schoelkopf, Introduction to Quantum Noise, Measurement and Amplification; cavity input-output theory and dispersive qubit measurement."),
    ],
    "relativistic_quantum_mechanics": [
        ("quant-ph/9905076", "A. Calogeracos and N. Dombey, History and Physics of the Klein Paradox; single-particle relativistic wave equations and pair creation in strong potentials."),
        ("1605.03300", "M. Trassinelli, D. F. Anagnostopoulos, G. Borchert and colleagues, Measurement of the charged pion mass using X-ray spectroscopy of exotic atoms; Klein-Gordon energies of pionic atoms."),
    ],
    "schr_dinger_picture": [
        ("0911.1917", "S. N. Shevchenko, S. Ashhab and F. Nori, Landau-Zener-Stuckelberg interferometry; the Landau-Zener transition probability, adiabatic and fast limits, and realizations with qubits."),
    ],
}
