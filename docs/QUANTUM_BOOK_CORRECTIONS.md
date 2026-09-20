# Quantum book corrections

These changes repair the source generators and the generated book together.
They preserve the 146 topic sections rather than replacing the book with a
shorter selection. The explanatory organization remains a proposed way to
connect established quantum physics, not a discovery of new quantum laws.

## Physics

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

There are 62 topic-specific treatments, 67 physical-role overviews and 17
historical or interpretive entries. The overviews retain their representative
relations and are explicitly identified as overviews. They still need individual
derivations and suitable references before this can be presented as a fully
reviewed quantum-physics textbook. Independent checks of the accompanying
FieldBridge calculations apply to those calculations alone.

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
