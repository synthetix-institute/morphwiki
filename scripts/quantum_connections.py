"""Physical explanations of the seven connections used in the quantum book.

These passages develop established relations from explicit models. They are
exposition, rather than claims inferred from topic-profile overlap.
"""

CONNECTION_TREATMENTS = {
    "generator_observable_duality": r"""
Preparing a system in an energy eigenstate gives a definite energy, but its
state vector still evolves. For a time-independent, self-adjoint Hamiltonian
\(H\), the eigenvalue equation \(H|n\rangle=E_n|n\rangle\) gives
\(U(t)|n\rangle=e^{-iE_nt/\hbar}|n\rangle\). The phase of an individual
eigenstate leaves every measurement probability unchanged. A superposition of
two energies accumulates a relative phase, which an observable connecting the
two states can reveal.

For a two-level system with \(H=\hbar\omega Z/2\), prepare
\(|+x\rangle=(|+z\rangle+|-z\rangle)/\sqrt2\). An energy measurement gives
\(\pm\hbar\omega/2\) with equal probabilities. A later measurement of \(X\)
instead detects the relative phase:
\begin{centeredalign}
U(t)=e^{-iHt/\hbar},\qquad
\langle X\rangle_t=\cos(\omega t),\\
H=\int_{\sigma(H)}E\,dP_H(E),\qquad
U(t)=\int_{\sigma(H)}e^{-iEt/\hbar}\,dP_H(E).
\end{centeredalign}
Here \(P_H\) is the projection-valued spectral measure of \(H\); it assigns
a projector to each energy interval. The probability of an energy in an
interval \(B\) is \(\operatorname{Tr}[\rho P_H(B)]\). The same projectors
weight the phases in the evolution operator. Energy as a measured quantity
and energy as the generator of time evolution are therefore two uses of the
same operator, rather than two mechanisms inferred from similar notation.

For a particle in a box, the boundary conditions enter the domain of \(H\)
and hence both integrals. Changing those conditions changes the allowed
energies and the evolution together. The treatments of
\hyperref[topic:hamiltonian-quantum-mechanics]{the Hamiltonian} and
\hyperref[topic:spectral-theory]{spectral theory} develop the two uses in
greater detail.
""",
    "representation_triangle": r"""
The oscillation in the preceding section can be calculated by evolving the
prepared spin state or by evolving its measured operator. These are the
Schr\"odinger and Heisenberg pictures. Starting from the same density operator
\(\rho_0\) and unitary evolution \(U(t)\), they give
\begin{centeredalign}
\rho_S(t)=U(t)\rho_0U(t)^\dagger,\qquad
A_H(t)=U(t)^\dagger A_SU(t),\\
\operatorname{Tr}[\rho_S(t)A_S]
=\operatorname{Tr}[\rho_0A_H(t)].
\end{centeredalign}
The equality follows by moving the final \(U^\dagger\) around the trace.
For \(H=\hbar\omega Z/2\), the Heisenberg operator is
\(X_H(t)=X\cos(\omega t)-Y\sin(\omega t)\). Its expectation in
\(|+x\rangle\) gives the same cosine as the moving state. The measured
polarization has not changed; only the location of time dependence has.

For a particle, a third representation follows by splitting the evolution
time into short intervals and inserting complete position states between
them. Each intermediate position is summed over. In the limit, the
propagator is expressed as an integral over paths joining the prescribed
endpoints:
\begin{centeredalign}
\langle q_f|U(t_f-t_i)|q_i\rangle
=\int_{q(t_i)=q_i}^{q(t_f)=q_f}\mathcal Dq\,e^{iS[q]/\hbar}.
\end{centeredalign}
The measure includes the normalization inherited from the short-time
propagators. For a free particle of mass \(m\), evaluating the Gaussian
integrals gives, for \(T>0\),
\begin{centeredalign}
\langle q_f|U(T)|q_i\rangle
=\sqrt{\frac{m}{2\pi i\hbar T}}
\exp\!\left[\frac{im(q_f-q_i)^2}{2\hbar T}\right].
\end{centeredalign}
This kernel also solves the free Schr\"odinger equation and tends to a delta
function as \(T\) approaches zero. Boundary conditions or constraints must
enter the short-time kernels before the limit is taken. Thus the path
integral represents a specified Hamiltonian evolution; an action written
without its measure and domain does not yet specify the same problem.
\hyperref[topic:path-integral-formulation]{The path-integral treatment}
explains the construction for a potential and for imaginary time.
""",
    "factorization_locality": r"""
When a detector acts on one spin of a pair, its operator has the form
\(O_A\otimes I_B\). The tensor-product decomposition identifies the two
subsystems and therefore what the detector can measure locally. For a joint
state \(\rho_{AB}\), all such measurements are reproduced by its reduced
state:
\begin{centeredalign}
\mathcal H=\mathcal H_A\otimes\mathcal H_B,\qquad
\rho_A=\operatorname{Tr}_B\rho_{AB},\\
\operatorname{Tr}[\rho_{AB}(O_A\otimes I_B)]
=\operatorname{Tr}(\rho_AO_A).
\end{centeredalign}
The singlet \((|01\rangle-|10\rangle)/\sqrt2\) gives \(\rho_A=I/2\).
Every direction of spin measurement is equally likely on either spin,
although measurements on the pair are perfectly anticorrelated along a
common axis. The reduced state has retained local probabilities and
discarded joint information. During an interaction, that joint information
can return to a local measurement, as the polarization--correlation pair of
Chapter~\ref{chap:mechanisms-predictions} shows.

A change of basis preserves the full experiment when it transforms both
states and operators. For a unitary \(V\), the transformed objects are
\(V\rho V^\dagger\) and \(VOV^\dagger\), and their trace is unchanged.
An entangling \(V\) generally turns a local operator into a joint operator.
If only the state is transformed while the same physical detector is kept,
the experiment has changed. This is why an arbitrary change of tensor
factors can change which states are called entangled without changing the
abstract dimension of the total Hilbert space.

In a spatial experiment the interactions and accessible detectors determine
the relevant subsystem algebras. In a quantum field theory, locality is
expressed by observable algebras associated with regions; a simple tensor
factorization for every region need not exist. The common physical question
is which measurements belong to each subsystem and which correlations
their combination can expose. The chapters on
\hyperref[topic:quantum-entanglement]{entanglement} and
\hyperref[topic:quantum-field-theory]{fields} develop these distinct settings.
""",
    "constraint_before_readout": r"""
A redundant coordinate description assigns several mathematical states to
one physical state. Gauge constraints remove this redundancy. In a Dirac
description, constraint operators \(\widehat{\mathcal C}_a\) annihilate
physical states. An operator representing a physical measurement must act
within that state space:
\begin{centeredalign}
\widehat{\mathcal C}_a|\psi_{\rm phys}\rangle=0,\qquad
[\widehat O_{\rm phys},\widehat{\mathcal C}_a]
|\psi_{\rm phys}\rangle=0.
\end{centeredalign}
The second relation follows by applying the first to
\(\widehat O_{\rm phys}|\psi_{\rm phys}\rangle\). It is a condition on
physical states; it need not be an operator identity throughout a larger
auxiliary space. In continuum gauge theories, defining the physical inner
product and the constraint domains is also part of the construction.

A finite example makes the restriction explicit. In a two-spin space impose
\(\mathcal C=Z_1Z_2-I\). The allowed subspace is spanned by
\(|00\rangle\) and \(|11\rangle\). The single-spin flip \(X_1\) sends
either state outside this subspace. The paired flip \(X_1X_2\) interchanges
the two allowed states and commutes with the constraint. Consequently a
Hamiltonian \(H=\hbar gX_1X_2\) gives physical motion inside the subspace:
\begin{centeredalign}
e^{-iHt/\hbar}|00\rangle
=\cos(gt)|00\rangle-i\sin(gt)|11\rangle,\qquad
P(11,t)=\sin^2(gt).
\end{centeredalign}
The example is an algebraic constrained system, not a model of an
electromagnetic gauge field. In an actual gauge theory, Gauss's law similarly
restricts the allowed matter and field states, and observables such as
electric fields or closed-loop quantities respect the restriction.

The measured probability is defined only after this choice of physical
states. For a positive measurement effect \(E_y\), its restriction to the
physical space must remain positive and the complete set of effects must
sum to the identity on that space. Constraints, evolution and measurement
therefore enter one calculation. Their roles in electromagnetic fields and
in gravitational theories are developed under
\hyperref[topic:gauge-theory]{gauge theory} and
\hyperref[topic:quantum-gravity]{quantum gravity}.
""",
    "boundary_spectrum_family": r"""
The energies of a confined particle and the transmission of a wave through
a barrier both follow from the Schr\"odinger equation. What distinguishes
them is how solutions are joined to the boundary or to incoming and
outgoing waves. The differential expression alone describes neither
experiment. Writing
\begin{centeredalign}
H_D=-\frac{\hbar^2}{2m}\Delta_D+V
\end{centeredalign}
uses the subscript \(D\) to retain the operator domain, including its
boundary conditions. The wall and zero-slope spectra of
Chapter~\ref{chap:physical-identity} are different operators in this sense.
Their common bulk expression does not make their level spacings equal.

For scattering on the line, a stationary wave at energy \(E\) is specified
by an incident amplitude and reflected and transmitted amplitudes. In
regions of constant potential its probability current is
\begin{centeredalign}
j=\frac{\hbar}{m}\operatorname{Im}(\psi^*\partial_x\psi),\qquad
\mathcal R=|r|^2,\qquad
\mathcal T=\frac{k_{\rm out}}{k_{\rm in}}|t|^2,\qquad
\mathcal R+\mathcal T=1.
\end{centeredalign}
Here \(r\) and \(t\) are amplitudes relative to the incident wave, and
\(k_{\rm in}\) and \(k_{\rm out}\) are positive wavenumbers in propagating
channels of equal mass. The velocity factor in \(\mathcal T\) is needed
because equal amplitudes need not carry equal current. For a real,
time-independent potential with no absorption, matching the wave function
and its appropriate derivative conserves this current.

Collecting all propagating channels gives a scattering map
\begin{centeredalign}
S:\mathcal H_{\rm in}\to\mathcal H_{\rm out},\qquad S^\dagger S=I,
\end{centeredalign}
when amplitudes are normalized to unit flux and all open channels are
included. Transmission probabilities then follow from its matrix elements.
A confining wall, a finite barrier and an absorbing boundary impose
different physical conditions. Changing between them constructs a different
spectral or scattering problem; it is not a change of notation. The
\hyperref[topic:particle-in-a-box]{box},
\hyperref[topic:quantum-tunnelling]{tunnelling} and
\hyperref[topic:scattering]{scattering} treatments calculate these outcomes.
""",
    "channel_instrument_correction": r"""
A measurement does two things: it assigns a probability to each recorded
outcome and it changes the state conditioned on that outcome. An instrument
\(\mathcal I_i\) keeps both pieces. If its Kraus operators are
\(K_{i\alpha}\), the outcome probability and the conditional state are
\begin{centeredalign}
\mathcal I_i(\rho)=\sum_\alpha K_{i\alpha}\rho K_{i\alpha}^\dagger,
\qquad p_i=\operatorname{Tr}\mathcal I_i(\rho),\\
\rho_i=\frac{\mathcal I_i(\rho)}{p_i}\quad(p_i>0),\qquad
\sum_{i,\alpha}K_{i\alpha}^\dagger K_{i\alpha}=I.
\end{centeredalign}
If the outcome is discarded, the state is instead
\(\mathcal E(\rho)=\sum_i\mathcal I_i(\rho)\). For a projective
measurement of \(Z\), the two operators are \((I\pm Z)/2\). Keeping
the outcome prepares the corresponding spin direction. Discarding it
removes coherence between those directions: an input \(|+x\rangle\)
becomes \(I/2\). The same coupling to a measuring apparatus has produced
different available information depending on whether its record is kept.

Error correction uses a record without measuring the unknown logical
amplitudes. In the three-qubit repetition code, the logical state is
\(a|000\rangle+b|111\rangle\). Measuring \(Z_1Z_2\) and \(Z_2Z_3\)
gives a syndrome that distinguishes no error from a flip of any one spin,
while leaving \(a\) and \(b\) undetermined. The syndrome selects a
recovery operation \(\mathcal R_i\). The complete corrected channel is
\begin{centeredalign}
\mathcal E=\sum_i\mathcal I_i,\qquad
\mathcal R_i\circ\mathcal I_i,\qquad
\rho_{\rm corrected}=\sum_i(\mathcal R_i\circ\mathcal I_i)(\rho_{\rm noisy}).
\end{centeredalign}
For a mixture of no error and single-spin flips, the recovered logical
state equals the original one. The code does not correct a phase flip:
that error acts inside the code space and gives no changed syndrome.

Complete positivity ensures that these maps also give physical states
when the encoded system is entangled with a reference. For successful
quantum correction the recovered correlations with that reference must
be preserved, not merely the populations of two chosen basis states.
\hyperref[topic:quantum-error-correction]{Quantum error correction}
derives the general condition for this preservation.
""",
    "encoding_intertwiner": r"""
A quantum simulator represents the states and interactions of one model
in another physical device. An encoding \(V\) sends a target state into
a chosen subspace of the device. When \(V^\dagger V=I\), the encoding
preserves norms and inner products. Its Hamiltonian must also preserve
the encoded evolution:
\begin{centeredalign}
VH_{\rm target}=H_{\rm carrier}V,\qquad
VO_{\rm target}=O_{\rm carrier}V.
\end{centeredalign}
The first relation implies
\(Ve^{-iH_{\rm target}t/\hbar}=e^{-iH_{\rm carrier}t/\hbar}V\).
The second identifies which device measurement represents a target
observable. Together they preserve the predicted expectation for every
encoded preparation.

For example, encode one spin by
\(V|0\rangle=|00\rangle\) and \(V|1\rangle=|11\rangle\).
The target Hamiltonian \(H_{\rm target}=\hbar\omega Z/2\) is
represented by \(H_{\rm carrier}=\hbar\omega Z_1/2\) within the
code space, and the target \(X\) is represented by \(X_1X_2\).
Starting from the encoded \(|+x\rangle\), the pair therefore gives
\begin{centeredalign}
\langle X_1X_2\rangle_t=\cos(\omega t)=\langle X\rangle_t.
\end{centeredalign}
Measuring \(X_1\) alone would give a different answer: its action
leaves the encoded subspace. The observable correspondence is as
necessary as the Hamiltonian correspondence.

For an approximate simulation write
\(D=H_{\rm carrier}V-VH_{\rm target}\), so that
\(VH_{\rm target}\simeq H_{\rm carrier}V\). Integrating the derivative
of the two unitary evolutions gives, for bounded operators and \(t\geq0\),
\begin{centeredalign}
\big\|e^{-iH_{\rm carrier}t/\hbar}V
-Ve^{-iH_{\rm target}t/\hbar}\big\|
\leq\frac{t}{\hbar}\|D\|.
\end{centeredalign}
Similarly, \(VO_{\rm target}\simeq O_{\rm carrier}V\) introduces
a separate measurement error. A small discrepancy at preparation can
thus grow during evolution, and its scale determines the duration over
which the simulation predicts accurately. Dualities and field-theory
correspondences require their own domains and observable maps; the
finite-spin encoding is an explicit example of the calculation, not
a proof of those broader correspondences.
""",
}
