"""Editorial physical explanations, distinct from extracted equation witnesses.

The references support the named relations. They are not counted as successful
corpus extraction or as new results produced by the constructor.
"""

REFERENCES = {
    "gauge_theory": [
        ("hep-ph/0001312", "G. S. Bali, QCD forces and heavy quark bound states, Appendix B: covariant derivative, curvature and gauge transformations."),
    ],
    "fermion": [
        ("0706.3360", "S. Giorgini, L. P. Pitaevskii and S. Stringari, Theory of ultracold atomic Fermi gases, sections II and V.2.2: occupation and spin-resolved correlations."),
    ],
    "quantum_chromodynamics": [
        ("hep-ph/0001312", "G. S. Bali, QCD forces and heavy quark bound states, sections 3-4 and Appendices B-C: colour fields, static potential and running coupling."),
    ],
    "quantum_electrodynamics": [
        ("hep-ph/0508242", "A. Grozin, Lectures on QED and QCD, sections 3.1-3.7: Lagrangian, Ward identity and charge renormalization."),
    ],
}

CONSTRUCTORS = {
    "quantum_chromodynamics": {
        "editorial_inline_math": True,
        "claim": "Quarks carry three colour components. Quantum chromodynamics couples them to eight gluon fields through a local SU(3) connection.",
        "reading": r"The colour matrices do not commute. Their commutator enters the field strength, so the gluon field contributes to its own interactions as well as mediating interactions between quarks. With natural units $\hbar=c=1$, the quark field of flavour $f$ is $q_f$, its mass is $m_f$, the coupling is $g_s$, and $A_\mu$ is a matrix in colour space. The action joins their covariant Dirac motion to the energy of the colour field.",
        "equation_note": r"The Hermitian colour generators and their normalization are given first. The metric has one positive timelike component and three negative spacelike components; $f$ labels quark flavours. In the final equation, $\mu$ is the renormalization scale and $n_f$ the number of active flavours. The sign of the commutator follows the stated covariant-derivative convention.",
        "equations": [
            r"[T^a,T^b]=if^{abc}T^c,\qquad\operatorname{Tr}(T^aT^b)=\frac12\delta^{ab}",
            r"A_\mu=A_\mu^aT^a,\qquad D_\mu=\partial_\mu+ig_s A_\mu",
            r"F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+ig_s[A_\mu,A_\nu]",
            r"\mathcal L_{\mathrm{QCD}}=-\frac12\operatorname{Tr}(F_{\mu\nu}F^{\mu\nu})+\sum_f\bar q_f(i\gamma^\mu D_\mu-m_f)q_f",
            r"\mu\frac{d g_s}{d\mu}=-\frac{11-2n_f/3}{16\pi^2}g_s^3+O(g_s^5)",
        ],
        "forced_consequences": [
            "Squaring the field strength produces terms cubic and quartic in the gauge potential. These are the three-gluon and four-gluon interactions. They disappear when the gauge algebra is replaced by an Abelian one; the covariant derivative alone is therefore not the whole distinction between QCD and electrodynamics.",
            "For $n_f$ active flavours with $11-2n_f/3$ positive, the weak-coupling beta function makes the coupling decrease as the energy scale increases. This permits short-distance perturbation theory. The same expansion loses accuracy when the coupling grows at hadronic scales; confinement is investigated through nonperturbative calculations rather than inferred by extrapolating the one-loop formula.",
        ],
        "scope_conditions": [
            "The beta function is the one-loop result for SU(3) with fundamental quarks. Active flavour thresholds require matching. Hadron masses and long-distance forces additionally depend on quark masses and the nonperturbative state of the gauge field.",
        ],
    },
    "quantum_electrodynamics": {
        "editorial_inline_math": True,
        "claim": "An electromagnetic field can exchange energy and momentum with charged particles. Quantum electrodynamics describes both the charged Dirac field and the electromagnetic field as dynamical quantum degrees of freedom.",
        "reading": r"In natural units $\hbar=c=1$, let $\psi$ be the charged Dirac field, $m$ its mass, $q$ its signed coupling, and $A_\mu$ the electromagnetic potential. Local phase covariance replaces the ordinary derivative in the Dirac equation by $D_\mu$. Expanding that derivative gives the current-potential interaction. The field-strength term supplies the electromagnetic dynamics, so radiation and recoil are calculated within one action rather than prescribed independently.",
        "equation_note": "The metric is (+,-,-,-). The current j^mu is the electric current in this convention. Local phase transformations change psi and A_mu together.",
        "equations": [
            r"D_\mu=\partial_\mu+iqA_\mu,\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu",
            r"\mathcal L_{\mathrm{QED}}=-\frac14F_{\mu\nu}F^{\mu\nu}+\bar\psi(i\gamma^\mu D_\mu-m)\psi",
            r"j^\mu=q\bar\psi\gamma^\mu\psi,\qquad\partial_\mu F^{\mu\nu}=j^\nu",
            r"\psi'=e^{-iq\chi}\psi,\quad A_\mu'=A_\mu+\partial_\mu\chi,\quad F_{\mu\nu}'=F_{\mu\nu}",
            r"k_\mu\Gamma^\mu(p+k,p)=S^{-1}(p+k)-S^{-1}(p)",
        ],
        "forced_consequences": [
            "The antisymmetry of F makes the divergence of Maxwell's equation vanish on its left-hand side, giving conservation of electric current. The Dirac equation and its adjoint give the same continuity relation. Agreement of these two calculations connects matter evolution to the electromagnetic source.",
            r"For the final identity, $S$ is the full electron propagator and $\Gamma$ is the proper vertex with the overall charge removed. The Ward--Takahashi relation ties a longitudinal photon insertion to the change in inverse propagator. Radiative corrections to the vertex and the electron propagator must respect it together.",
        ],
        "scope_conditions": [
            "Gauge fixing is needed to invert the photon kinetic operator in perturbation theory. Observable probabilities are independent of that choice when the state preparation and calculation are treated consistently. A prescribed classical potential is an approximation in which the corresponding field degrees of freedom are not evolved quantum mechanically.",
        ],
    },
}

EXPLANATIONS = {
    "quantum_chromodynamics": {
        "why": "The colour connection specifies how quark amplitudes at neighbouring spacetime points are compared. Its action is inseparable from the colour representation of the quark: replacing the three-component carrier by an uncharged scalar would remove the very interaction being described.",
        "reading": "Physical observables include colour-singlet correlation functions, hadron energies and scattering cross sections. A Wilson loop follows a heavy test colour charge around a closed contour and traces over its colour index. Its large-time decay defines the static quark-antiquark potential after the self-energy convention is fixed.",
        "example": "In pure gauge theory a long confining flux tube gives an approximately linear static potential. With dynamical quarks the tube can break through pair creation. The observable must therefore be specified along with the matter content; the same loop notation does not impose the same long-distance force in both theories.",
        "connection": "Changing resolution replaces short-distance fluctuations by effective couplings and operators. Heavy-quark effective descriptions preserve selected QCD amplitudes through matching, which supplies a concrete example of transferring a physical relation between different sets of variables.",
    },
    "quantum_electrodynamics": {
        "why": "Treating the potential as prescribed describes motion in an external field. Allowing the field to fluctuate permits emission, absorption and virtual photon exchange. The additional dynamical variables change which processes the theory can predict.",
        "reading": "The U(1) connection acts by multiplication, so its components commute and the field strength contains no potential commutator. The classical gauge-field action is quadratic. Photon-photon scattering nevertheless arises through charged-particle loops; absence of a classical photon self-coupling does not mean absence of that quantum process.",
        "example": "A calculation of photon emission can replace a polarization vector by the photon momentum. For a complete on-shell amplitude the resulting longitudinal contribution vanishes. Failure of that cancellation exposes a missing diagram or an inconsistent approximation.",
        "connection": "Replacing U(1) by a non-Abelian colour group changes this calculation at the level of the field strength and adds direct gauge-field interactions. The distinction is an algebraic change with physical consequences, not a change of particle names.",
    },
}

FRAMES = {
    "fermion": {
        "role": "antisymmetric quantum statistics",
        "carrier": "the antisymmetric many-particle sector of the one-particle Hilbert space, including spin",
        "operator": "the many-body Hamiltonian and fermionic creation and annihilation operators",
        "admissibility": "Exchange antisymmetry restricts states and mode occupations; the Hamiltonian specifies interactions and evolution",
        "readout": "mode occupations, spin-resolved correlations, energies and thermodynamic response",
        "test": "The same-spin pair amplitude vanishes at equal positions, while opposite-spin particles can share a spatial orbital.",
    },
    "quantum_chromodynamics": {
        "role": "colour gauge dynamics",
        "carrier": "quark and gluon field states in the physical SU(3) constraint sector",
        "operator": "the QCD action, with covariant Dirac motion and non-Abelian field strength",
        "admissibility": "Gauss constraints, quark statistics and specified boundary conditions select physical states",
        "readout": "colour-singlet spectra, correlation functions and scattering cross sections",
        "test": "Gauge identities and continuum extrapolation constrain a calculation of the chosen observable.",
    },
    "quantum_electrodynamics": {
        "role": "charged matter and electromagnetic dynamics",
        "carrier": "Dirac and electromagnetic field states satisfying the Gauss constraint",
        "operator": "the minimally coupled Dirac-Maxwell action and its quantized evolution",
        "admissibility": "Charge conservation, fermionic statistics and gauge constraints restrict amplitudes",
        "readout": "emission and scattering probabilities, energy shifts and electromagnetic response",
        "test": "Longitudinal-photon contributions cancel in physical amplitudes.",
    },
}

SUPPORT = {
    "quantum_chromodynamics": (
        ["Gauge changes rotate colour coordinates while leaving colour-singlet probabilities unchanged. Matching to an effective theory preserves the amplitudes included at the stated order."],
        ["Quark masses, the coupling, temperature and volume change spectra and correlations. A different gauge group changes the interaction algebra itself."],
        ["Static potentials, hadron spectra and short-distance cross sections probe different regimes of the same action and require the corresponding controlled approximations."],
    ),
    "quantum_electrodynamics": (
        ["A simultaneous local phase change of the charged field and gauge transformation of the potential preserves current conservation and physical probabilities."],
        ["Replacing a classical field by a quantized field permits its fluctuations and recoil to affect charged matter. Coupling and mass values determine numerical predictions within the theory."],
        ["The Ward--Takahashi identity compares independently calculated vertex and propagator corrections; an inconsistent truncation can violate it even when both calculations are finite."],
    ),
}
