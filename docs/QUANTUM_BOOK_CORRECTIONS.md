# Quantum book corrections

These changes repair the source generators and the generated book together.
They preserve the 146 topic sections rather than replacing the book with a
shorter selection. The explanatory organization remains a proposed way to
connect established quantum physics, not a discovery of new quantum laws.

## Physics

### Energy accounting and geometric coefficient, 15 October 2026

The frequency-quench example now separates total mean work, measured relative
to the initial energy, from excitation above the final ground state. Halving
the frequency from 1 to 1/2 gives work -3/16 and excitation 1/16 in units
with hbar = 1. The regular-tetrahedron volume is written explicitly as
`l^3/(6 sqrt(2))`. Independent symbolic tests check both calculations.
The other 144 topic treatments are preserved.

The generic new-field builder now assigns carrier indicators from each
source chunk rather than copying the corpus-average profile into every
page. Adding an unrelated graph paper leaves a probability-diffusion
page's carrier indicators unchanged. This fixes source attribution; it
does not add a general textbook generator for other fields.

### Explanatory revision, 14 October 2026

The opening now derives the measured two-spin polarization from its
commutators, then follows the initial correlation and the memory integral
through the reduction. The seven cross-topic connections have separate
physical calculations in `scripts/quantum_connections.py`. They replace
the role-label, equation, equivalence-condition summaries. All 146 individual
topic sections remain unchanged, including their equations and source links.

The transfer chapter separates linear state maps from nonlinear stochastic
coordinate changes. It derives the oscillator selection law from its
quadrature mean and variance, states the finite-ramp and continued-ramp
limits separately, and defines every coefficient of the quantum generator.
The mechanism appendix explains the nested notation using the spin and
confinement calculations and distinguishes a dynamical correspondence from
an observable correspondence.

The revision also corrects several specific statements:

- The stochastic quadrature is not its deterministic expectation value.
- A single-neighbour spin polarization changes sign at `pi/(2|g|)` and
  returns to its original signed value at `pi/|g|`; its magnitude returns
  earlier. Finite unequal spin baths may recur, so Gaussian short-time
  decay is not irreversible loss.
- The ring-energy sign agrees with the declared boundary twist.
- Noncommuting observables may share particular eigenvectors. They lack
  a common complete eigenbasis, rather than excluding every joint sharp state.
- A switching rate can be identified with the Lindblad gap only where
  the relevant slow mode is separated and represents population switching.
- The oscillator rate scan has a deviation near `6e-4` at its slowest
  reported rate, not less than `6e-5` at every rate.

The two pinned FieldBridge calculations were rerun. The 27-photon example
gives `P_exact = 0.75045` versus `P_Gaussian = 0.75047`, a difference of
`1.3654e-5`. The half-photon example gives `0.6845` versus `0.7505`,
with a biased steady-state value of `0.6856`. These are numerical calculations
of the stated models, not new experimental measurements.

Fifteen additional tests independently check the new examples, including
pulse order, the free propagator, constraint-preserving flips, flux-weighted
transmission, conditional measurement and the encoded spin observable.
The full local suite has 82 passing tests. These checks apply to the
specified calculations; the remaining chapter-wide scientific review
status is unchanged.

### Earlier corrections

- Non-Abelian field strength transforms by conjugation. Its invariant
  contractions and traced Wilson loops are distinguished from its components.
  The parallel-transport sign agrees with the covariant-derivative convention.
- Fermionic antisymmetry exchanges complete position and spin coordinates.
  Opposite-spin fermions can occupy the same spatial orbital; a mode number
  operator has eigenvalues zero and one. Pairing preserves constituent
  antisymmetry. The ideal-gas discussion states its temperature and homogeneity
  assumptions.
- The QCD and QED entries now develop their respective actions, field strengths
  and consequences. QCD includes gluon self-interactions and the limited
  weak-coupling meaning of the one-loop beta function. QED connects the matter
  current, Maxwell equation and Ward--Takahashi identity.
- Curvature, frustrated bond loops and reduced memory are distinguished.
  Nontrivial holonomy does not make a gauge theory incomplete, and adding a
  flux label does not remove frustration. Failure of a time-homogeneous
  semigroup law alone does not establish memory. Hidden preparations and
  subsequent interventions enter the predictive-sufficiency question.
- Deterministic quantum channels are distinguished from the maps for selected
  measurement outcomes, and boundary conditions remain part of the generator.

The added references are arXiv research reviews, separately identified as
references selected for the explanation. They are not counted as automatic
source recovery or constructor discoveries.

## Source evidence and rendering

The earlier source gate could accept a topic mention next to a damaged or
irrelevant display. It also allowed a different equation from the same paper
to stand in for the screened card. The repaired gate checks complete relations,
exact card and row identifiers, and relation-specific local context. Repeated
feature rows for the same source card are deduplicated. Rejected examples remain
in the machine-readable index as retrieval candidates rather than disappearing.

This recheck reduces the number of topics with accepted source examples from
123 to six. It does not mean that the remaining physics is false; it means that
the previous automatic evidence did not establish the claimed connection.
Canonical arXiv identifiers repair legacy links. Equations are now rendered in
the PDF even when a topic also has a prose account of its defining relations.
The common display environment also supplies its alignment argument explicitly:
without it, LaTeX could mistake an opening commutator for an optional argument
and silently omit that part of the equation.
Centering also preserves alignment separators inside matrices and arrays;
removing them along with outer equation alignment would collapse matrix
columns and syndrome tables. The rendered-book test now covers both cases.

The content checks now examine equation environments inside actual TeX topic
sections, not only the Markdown archive. They check public identifiers and
reject unsupported source-grounding labels. A passing build remains a statement
about artifact integrity, not certification of all scientific content.

## Remaining review

There are 125 topic-specific treatments, four alternative-name entries and
17 historical or interpretive entries; no physical-role overview remains (see
the section on worked treatments below). The treatments still need independent
scientific review before this can be presented as a fully reviewed
quantum-physics textbook. Independent checks of the accompanying FieldBridge
calculations apply to those calculations alone.

## One edition

The expository companion and the full reference edition were merged on
2026-10-13 into one book. Once every physical subject had a worked treatment,
the two differed only in the 17 historical and interpretive entries, which the
book now prints with short accounts of the physics they concern. Two existing
derivations, for the quantum Hamiltonian and the path-integral formulation, are
printed rather than hidden by alternative-name redirects.

The title page attributes the organization of the book to the authors. Source
links sit beside the relations they support. Per-page build comments have been
removed; the edition manifest records the source route and equation identifiers
for each topic. Corpus-aligned equations remain distinct from separately
inspected original-paper displays. The scientific review remains incomplete.

The generator repairs the broken Schrödinger spelling and capitalized sentence
fragments. The book integrity checks require exactly one section for every
subject, equations in every treatment and source links at the relevant
relation. Duplicate labels, deleted equations and generic representative-relation
blocks fail these checks. Build integrity is reported separately from scientific
review.

Rebuild the book and run its checks with `bash scripts/render_quantum_book.sh`.

## Repeated and generic text

Every topic page carried the same two validation sentences, about transfer
targets and shuffled contexts, whatever its physics. They have been removed
from the cached pages and from the generator. A treatment without a
topic-specific consequence now states the physical consequences of its
chapter's role, as treatments with constructor overrides already did; no page
states what the constructor itself requires.

Branch-level sentences no longer make a topic the subject of a physical role.
A topic is placed at a step, for example "Quantum biology is placed at the
state step, where the carrier of prediction is specified", and the step
carries the role. Chapter 1 defines the roles on two coupled spins and
Chapter 2 nests them; the unnumbered chapter that follows refers back instead
of repeating the definitions.

## Mechanisms before roles

The first scientific chapter now develops a two-spin interaction and derives
its measured polarization from the Heisenberg equation. Two admissible joint
preparations have the same local density operator but different subsequent
signals. Retaining the relevant correlation closes the prediction; eliminating
it produces both a history integral and an initial-correlation term. This
calculation introduces the mechanism before the terminology used to describe
it. The original chapters on physical identity, external conditions and global
composition remain in the book, after that explanation.

Eighteen former generic overviews now have individual derivations: quantum
state, two-state dynamics, Fourier transformation, spectral theory, canonical
commutators, the Heisenberg group, symmetry, the Heisenberg picture, Pauli
matrices, angular momentum, quantum jumps, amplification, error correction,
teleportation, metrology, key distribution, the oscillator and quantum
statistical mechanics. Their narrative paragraphs follow the calculations
instead of repeating the branch template. The new tests independently check
the opening spin dynamics, Rabi evolution, teleportation convention, error
syndromes, exchange energies, amplifier noise and oscillator thermal limits.

Original-paper recovery supplies 16 displays for 15 topics from seven arXiv
documents. Each record contains the original expression, article fragment
identifier, equation and document hashes, and an authored account of what the
display supports. The article text remains in the local build cache. These
records are explicitly distinct from the six corpus-aligned topics: a valid
original-paper relation does not repair the missing row-to-card correspondence.
See [the source-recovery tutorial](tutorial/12_original_sources.md).

Rebuild with the cached evidence, without launching source extraction:

```bash
MORPHWIKI_BUILD_V2_EVIDENCE_INDEX=0 bash scripts/run_quantum_book.sh
```

The runner revalidates the saved evidence before generating the book. A fresh
corpus extraction remains a separate operation requiring the source-card data.

## Worked treatments for every topic (2026-10-12)

The generic overviews and the template sections of the remaining treatments
(the one-line constructor label, Physical Construction, Invariance And
Realization and Discriminating Consequences) were replaced by individual
treatments. Each opens with a physical question, derives the relation that
answers it, works one example to a number or a named experiment, and states
the conditions of validity. The 124 new treatments, including short accounts
for the 17 historical and interpretive entries, live in
`scripts/quantum_narratives/`, one module per chapter, and are merged by
`scripts/quantum_physical_derivations.py`. Each module passes
`scripts/quantum_narratives/check_module.py`, which typesets it as the book does,
rejects internal vocabulary and compiles it. Key equations were checked
symbolically or numerically when written, and every arXiv reference was
confirmed against the arXiv API; experimental details quoted without a
reference remain to be checked against the original papers.

The opening part was rewritten around physical examples (boundary conditions
and spectra, the vacuum Rabi oscillation, decay and revival in a spin bath, the
spin echo, the Aharonov--Bohm ring, the Berry phase, a frustrated triangle, the
geometric potential of a curved surface) in `scripts/quantum_framework_chapters.py`.
The role notation of the mechanism descriptions appears only in the closing
appendix. The content contract was rebased on the new edition: topic words rose
from 63,619 to 71,373 and displayed equations from 129 to 379, while the PDF fell
from 311 to 255 pages because repeated boilerplate was removed.
