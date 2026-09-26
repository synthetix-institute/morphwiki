"""Mechanism-first introduction, shared by the reproducible book builder."""

OPENING = r"""\chapter{Quantum Mechanisms And Their Predictions}\label{chap:mechanisms-predictions}

An interaction between two quantum systems can make a property of one depend
on their joint preparation. This dependence is responsible both for useful
operations, such as entangling gates, and for the loss of coherence when the
second system is uncontrolled. Explaining either effect requires following
what the interaction changes and how that change becomes observable. The same
calculation can then describe a controlled pair of spins, two coupled effective
two-level systems, or a spin interacting with a fluctuating neighbour, provided
their physical interactions realize the specified Hamiltonian.

Consider two spins with Hamiltonian \(H=\hbar g Z_1Z_2\), where \(g\) is an
angular frequency and \(X_j,Y_j,Z_j\) are Pauli operators acting on spin \(j\).
The eigenvalue of \(Z_2\) determines the sign of the field experienced by spin
1. A superposition of these eigenstates therefore subjects spin 1 to two
conditional rotations and can entangle the pair. For a joint density operator
\(\rho(t)\), the transverse polarization \(x(t)=\operatorname{Tr}[\rho(t)X_1]\)
couples to the correlation \(c(t)=\operatorname{Tr}[\rho(t)Y_1Z_2]\).
The Heisenberg equation gives
\begin{centeredalign}
\dot x=-2gc,\qquad \dot c=2gx,\\
x(t)=x(0)\cos(2gt)-c(0)\sin(2gt).
\end{centeredalign}
Thus a measurement on one spin can reveal a correlation established before
the interaction began. The oscillation is produced by the exchange between
two components of the joint state, even though only one of them is measured.

The dependence on the joint preparation is visible without assuming an
entangled initial state. Let \(I_4\) be the identity on the two-spin space,
and choose real numbers \(x_0,c_0\) satisfying \(x_0^2+c_0^2\leq1\). The states
\begin{centeredalign}
\rho_\pm=\tfrac14(I_4+x_0X_1\pm c_0Y_1Z_2),\\
\operatorname{Tr}_2\rho_\pm=\tfrac12(I_2+x_0X_1)
\end{centeredalign}
have identical reduced states for spin 1. They nevertheless give polarizations
whose difference is \(-2c_0\sin(2gt)\). Positivity follows because \(X_1\) and
\(Y_1Z_2\) anticommute and square to the identity: the eigenvalues of either
state are \((1\pm\sqrt{x_0^2+c_0^2})/4\). The correlation is consequently an
independent physical part of the preparation, not a relabelling of the initial
polarization.

Measuring \(Z_1\) instead would give a constant result, since
\([H,Z_1]=0\). The interaction has not disappeared; that observable is
insensitive to its action. A mechanism in this book means the physical
dependence connecting an interaction and an admissible preparation to a
specified observable consequence. It includes the degrees of freedom through
which the effect is transmitted. A Hamiltonian determines their evolution;
the preparation and measurement determine which part of that evolution is
tested. This distinction is essential when comparing experiments: equal
Hamiltonians with different preparations can produce different signals,
whereas different physical devices can implement the same dependence.

For the polarization above, retaining \((x,c)\) gives a complete pair of
evolution equations. Eliminating \(c\) expresses the same dependence as
\begin{centeredalign}
\dot x(t)=-2gc_0-4g^2\int_0^t x(s)\,\mathrm ds.
\end{centeredalign}
The integral records the correlation generated during the motion; the first
term retains the correlation present at preparation. This is where closure
enters the explanation. A description by \(x\) alone must carry both terms,
or restrict the preparations and observations so that the omitted information
cannot affect a prediction. Closure describes the sufficiency of those chosen
variables. The mechanism is the interaction that made the correlation
physically relevant in the first place.

This example specifies the operational language used in the book. The
carrier \(\Xi\) is the set of density operators on
\(\mathbb C^2\otimes\mathbb C^2\), and the operation
\(\Omega[\rho]=-i[H,\rho]/\hbar\) evolves them. Positivity and unit trace
are the admissibility conditions \(C\). The observable map
\(R_X(\rho)=\operatorname{Tr}(\rho X_1)\) gives the polarization, and the
protocol \(P\) specifies the joint preparation, evolution time and
measurement. A pair of coupled spins realizing \(H\) supplies the physical
implementation \(A\). Thus \(I_{\mathrm{op}}=((\Omega,\Xi);C,R_X,P)\)
records the ingredients needed to predict this signal; their roles follow
from the calculated evolution and measurement.

The reduction to \(x\) shows why these roles cannot be discarded
independently. Define \(\alpha_x(\rho)=R_X(\rho)\). For the two preparations
above, with \(c_0\ne0\),
\begin{centeredalign}
\alpha_x(\rho_+)=\alpha_x(\rho_-)=x_0,\qquad
\alpha_x(\Omega[\rho_\pm])=\mp 2gc_0.
\end{centeredalign}
No evolution law depending only on \(x_0\) can reproduce both initial slopes.
The correlation \(c\) is the extra state coordinate required for autonomous
evolution; when it is eliminated instead, its initial value and the history
integral in the preceding equation retain precisely the information that
\(x\) lost. A state map between descriptions must therefore preserve the
evolution and the specified observable consequence.

The organization of quantum theory follows these dependencies. A spin
Hamiltonian acts on a tensor product of spin spaces; exchange symmetry changes
the admissible many-particle states; a detector couples a particular
observable to an apparatus. These ingredients cannot be assembled in an
arbitrary order. An operator must be defined on the chosen states before its
evolution can be calculated. Predicting a later measurement then requires
both that evolution and the initial preparation. The nested description used below
expresses this dependence. Its roles identify the ingredients of a mechanism
after their physical function has been established.

Constructing another realization means finding an interaction and a
preparation that reproduce the relevant equations and measurement relation.
For the two-spin example, changes of basis are harmless when they transform
the Hamiltonian, state and observable together. Additional couplings require
new commutators: they can connect \(x\) and \(c\) to further correlations and
change the measured signal. The subsequent chapters develop this operation
across interference, quantum statistics, measurement, fields and information
processing. Explicit calculations show which physical dependence is preserved
and which additional term or degree of freedom becomes necessary.
"""
