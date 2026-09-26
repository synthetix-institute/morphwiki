# Why a physical description has dependent levels

A quantum measurement asks for the probability of an outcome in a prepared
system. Answering it requires a state space, a state on that space, an
evolution and an observable. Each choice constrains the next.
A Hamiltonian acts on a particular space; a partial trace requires a declared
subsystem factorization; an observable must act on the resulting system. A
change in an earlier choice can change the meaning of the later ones.

MorphWiki records these dependencies with a core M=(Omega,Xi), followed by
conditions C, observables R and preparation or ordered operations P. A physical
realization A supplies a particular implementation. These roles specify how
the equations in this tutorial enter a prediction; their assignment is an
organizing choice.

```mermaid
flowchart TD
    X["Carrier Xi: admissible states"] --> M["Core M: operation on its carrier"]
    O["Operation class Omega"] --> M
    M --> C["Constitutive and domain conditions C"]
    C --> E["Specified evolution"]
    E --> R["Observable R"]
    E --> P["Preparation and operation order P"]
    R --> T["Predicted measurement"]
    P --> T
    A["Physical realization A: apparatus and parameter values"] --> T
    A -. "change of domain or degrees of freedom" .-> C
```

The arrows follow the mathematical dependencies. The implementation defines
the clauses in
[`morphwiki_constructor.py`](../../scripts/morphwiki_constructor.py). In
particular, realization attaches to a defined mechanism. An apparatus that
changes the state space or boundary condition also changes the corresponding
inner description.

For a spin experiment, choosing the Hilbert space fixes the possible density
matrices. Choosing the Hamiltonian then fixes how their expectation values
evolve. Specifying only the first spin's magnetization may still leave its
future undetermined if an interaction converts a two-spin correlation into
that magnetization. The needed additional quantity is obtained by applying
the Hamiltonian to the measured operator. This gives a concrete use of the
dependencies, rather than merely assigning each symbol to a category.

Within this representation, the archive identifies recurring families and
candidate transitions. The division into roles was supplied to the analysis;
the book uses it to relate established equations and calculate their
consequences.

## What changes when the experiment changes?

For the two-spin example, the levels become concrete:

| Choice | Supplied object | Effect on the prediction |
| --- | --- | --- |
| Carrier | $\mathbb C^2\otimes\mathbb C^2$ | Defines joint states and two-spin observables |
| Dynamics | $H=gZ\otimes Z$ | Couples transverse magnetization to a correlation |
| Admissibility | Positive, unit-trace density matrices; Hermitian $H$ | Makes state probabilities and unitary evolution well defined |
| Observable | $X\otimes I$ | Selects the signal whose dynamics must close |
| Preparation | Initial expectations of $X\otimes I$ and $Y\otimes Z$ | Fixes the two initial conditions of the reduced prediction |
| Realization | A specified implementation and coupling value | Assigns an experimental time scale and measurement procedure |

Changing the measured operator to $Z\otimes I$ changes the question without
changing the Hamiltonian. That observable commutes with $H$, so its expectation
is constant and requires no extra coordinate. Adding a transverse term to $H$
instead changes the dynamics and may enlarge the required span. The same
material can therefore support different predictive descriptions depending on
the interaction and measurement.

The constructor can ask what must be recalculated after a change rather than
replacing an entire model by analogy. The hierarchy supplies places to record
those choices; the commutator calculation establishes their effect.

[Next: connect sources and calculations](09_sources_and_calculations.md) ·
[Tutorial](index.md)
