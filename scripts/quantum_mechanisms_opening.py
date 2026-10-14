"""Mechanism-first introduction, shared by the reproducible book builder."""

OPENING = r"""\chapter{Quantum Mechanisms And Their Predictions}\label{chap:mechanisms-predictions}

A spin prepared perpendicular to a magnetic field precesses, and its
transverse polarization oscillates. Coupling it to a second spin changes
the problem: the field acting on the first now depends on the second.
The measured polarization can fall and return even though the pair is
isolated and no energy is dissipated. A controlled experiment uses this
interaction to generate correlations; an experiment that leaves the
neighbour uncontrolled sees a loss of coherence. Both observations follow
from the same joint evolution.

Consider two spin-1/2 systems with Hamiltonian \(H=\hbar gZ_1Z_2\), where
\(g\) is an angular frequency. The dimensionless Pauli operators
\(X_j,Y_j,Z_j\) represent the components of spin \(j\), in units of
\(\hbar/2\). Each \(Z_j\) has eigenvalues \(+1\) and \(-1\), and
\([Z_j,X_j]=2iY_j\). When spin 2 is in a \(Z_2\) eigenstate, spin 1
experiences the Hamiltonian \(+\hbar gZ_1\) or \(-\hbar gZ_1\).
It therefore precesses in opposite directions in the two cases. A
superposition of those alternatives can entangle the spins.

Let the apparatus measure the transverse polarization of spin 1,
\(x(t)=\operatorname{Tr}[\rho(t)X_1]\), where \(\rho\) is the joint
density operator. Its time derivative follows from the Heisenberg
equation \(d\langle O\rangle/dt=(i/\hbar)\langle[H,O]\rangle\).
The commutator contains the joint operator \(Y_1Z_2\), so a correlation
\(c(t)=\operatorname{Tr}[\rho(t)Y_1Z_2]\) enters the measured motion.
Taking its derivative returns the original polarization:
\begin{centeredalign}
\frac{i}{\hbar}[H,X_1]=-2gY_1Z_2,\qquad
\frac{i}{\hbar}[H,Y_1Z_2]=2gX_1,\\
\dot x=-2gc,\qquad \dot c=2gx,\\
x(t)=x(0)\cos(2gt)-c(0)\sin(2gt).
\end{centeredalign}
The two expectation values form a closed pair of equations: their
derivatives require no further operator. This is a smaller description
than the full two-spin density matrix, yet it determines this
polarization exactly. For an initial state with \(x(0)=1\) and
\(c(0)=0\), the apparatus observes \(x(t)=\cos(2gt)\). At
\(t=\pi/(4g)\), for \(g>0\), the transverse polarization is zero
and the correlation has reached one. The vanishing signal represents
a transfer into a joint correlation, rather than disappearance of the
joint state. The polarization later returns.

Measuring \(Z_1\) would give a constant expectation, because
\([H,Z_1]=0\). Thus the same Hamiltonian generates visible motion
for one observable and no motion for another. The interaction and
the measured quantity together determine which part of the state
must be followed. In a larger spin network, repeated commutators
can introduce further correlations; the number required by a
particular measurement is a physical property of the interactions,
not the number of topics used to describe them.

The initial correlation matters independently of the initial
polarization. Let \(I_4\) denote the identity on the two-spin space
and choose real \(x_0,c_0\) with \(x_0^2+c_0^2\leq1\). The two
preparations
\begin{centeredalign}
\rho_\pm=\tfrac14(I_4+x_0X_1\pm c_0Y_1Z_2),\qquad
\operatorname{Tr}_2\rho_\pm=\tfrac12(I_2+x_0X_1)
\end{centeredalign}
give the same reduced density operator for spin 1. Every immediate
measurement on that spin consequently has identical statistics.
The states are physical: \(X_1\) and \(Y_1Z_2\) anticommute and
square to the identity, giving eigenvalues
\((1\pm\sqrt{x_0^2+c_0^2})/4\). After the interaction begins,
their polarizations differ by \(-2c_0\sin(2gt)\). In particular,
\begin{centeredalign}
x(0)=x_0\ \text{for both},\qquad \dot x(0)=\mp2gc_0.
\end{centeredalign}
No evolution law depending only on \(x_0\) can reproduce both initial slopes.
The two preparations are distinguished by a joint quantity that the
interaction converts into a local signal. Predicting that signal therefore
requires \(c_0\), even though the apparatus measures only \(x\).

Integrating \(\dot c=2gx\) gives
\(c(t)=c_0+2g\int_0^t x(s)\,\mathrm ds\). Substituting this into
the polarization equation eliminates the correlation without
losing its effect:
\begin{centeredalign}
\dot x(t)=-2gc_0-4g^2\int_0^t x(s)\,\mathrm ds.
\end{centeredalign}
The first term carries the correlation present at preparation.
The integral carries the correlation produced during the motion.
Setting \(c_0=0\) removes the former, but leaves the history
dependence. The two first-order equations and this memory equation
predict the same signal because both retain the physical influence
of the second expectation value.

These calculations explain what is meant here by a mechanism: the
interaction through which a specified preparation produces a
measurable change. Its description has dependent parts. The joint
spin space makes \(Z_1Z_2\) and \(Y_1Z_2\) meaningful operators;
the Hamiltonian generates the motion; positivity and normalization
make the preparation physical; the measured polarization selects
the required expectations. Preparing the state, applying the
interaction for a given duration and choosing the measurement
complete the experiment. A particular pair of spins supplies the
coupling \(g\), whose value fixes the time scale.

The dependence of these parts is the reason for organizing quantum
theory as a mechanism tree. An operator acts on a chosen space of
states. Its spectrum and evolution depend on its domain, including
boundary conditions. A prediction uses that evolution together
with a preparation and a measured operator. Material parameters
then specify an experimental realization of this problem. The
tree records these mathematical and physical dependencies; it
does not prescribe a chronological order in which a researcher
must choose them. A change in an outer part can require a change
within: replacing a measuring apparatus that observes \(X_1\)
by one that observes \(Z_1\) changes which equations are needed,
while adding a new interaction can enlarge their closed set.

The following chapters use this dependence to connect familiar
subjects. Confinement fixes an operator domain and changes energy
levels. Quantizing a field introduces states whose fluctuations
act on an atom. Eliminating an environment retains its influence
as decoherence or memory. Changing representation moves states
and observables together while preserving predictions. These
relations explain how different physical systems can realize the
same equations and where a changed interaction, boundary or
preparation requires another term. The individual topic
treatments develop the spectra, interference patterns and
correlations through which those changes are measured.
"""
