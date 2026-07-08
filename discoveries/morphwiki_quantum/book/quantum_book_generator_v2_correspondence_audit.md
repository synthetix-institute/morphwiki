# Quantum Book Generator/V2 Correspondence Audit

- Readiness: `usable`
- Book TeX: `discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex`
- Generator: `scripts/build_morphwiki_quantum_book.py`
- Tree artifact: `discoveries/morphwiki_quantum/quantum_mechanism_tree.json`
- Sparse-attention artifacts:
  - `discoveries/morphwiki_quantum/sparse_attention/morphwiki_quantum_sparse_attention.json`
  - `discoveries/morphwiki_quantum/sparse_attention/morphwiki_rewrite_transition_sparse_attention.json`

## Audit Question

The audit checks whether the generated quantum book corresponds to its generator and to the current V2 operator/substrate language structure. It also records why the text is original, in the narrow technical sense: it is not a copied exposition of quantum mechanics, but a generated re-indexing of quantum topics by constructor role.

## Main Finding

The book is internally coherent as a **MorphWiki sparse-attention quantum-constructor book**. Its public spine is:

```text
context -> Hilbert-space carrier/domain -> state transport -> observable spectrum -> probability/readout -> compatibility -> boundary/field/protocol realization
```

This corresponds well to the current public generator. It does **not** yet correspond to a fully integrated V2 operator/substrate run. The optional V2 grammar renderer exists in the generator, but it is gated behind `MORPHWIKI_EXPOSE_INTERNAL_METHOD=1`, and the current `quantum_mechanism_tree.json` does not contain `hyperion_v2_language`.

Therefore the correct claim boundary is:

> This book is an original mechanism-indexed quantum synthesis generated from MorphWiki pages, sparse-attention route profiles, generator-side constructor templates, and source-witness links. It is not yet a source-card/V2-row-grounded quantum atlas book.

## Evidence Summary

| Check | Result | Interpretation |
|---|---:|---|
| Literal public V2 symbols (`V2`, `Ω`, `Ξ`, `Λ`, `Γ`, `A00`, `GGAE`, `operator/substrate`) | `0` in generated TeX | Internal V2 language does not leak into the public PDF. |
| `Constructor Regularities` section | `1` | The old `Hidden Rules` title has been replaced. |
| Old title-token rules (`R13`, `R15-R21`) in generated TeX | `0` | Title-token rules are no longer emitted publicly. |
| `no Lagrangian road map available` | `146` | Page-level road text is repeated even though no page-level road map exists. This is a discrepancy. |
| Generic opening `In quantum-mechanical terms, ...` | `93` | Many pages still use family-level template prose rather than page-native constructor text. |
| `quantum_mechanism_tree.json` page records with native constructor/source-equation/V2 fields | `0` | The richer text comes from generator templates and overrides, not from V2/source-card rows. |
| Sparse-attention route counts | `spectral=146`, `transport=146`, `closure=137`, `boundary=54`, `incompatibility=59`, `protocol=32` | Supports the book's state/operator/spectrum/readout spine. |

## Correspondence With The Generator

### Supported Correspondence

1. **Public book spine matches the generator.**

   The generated book defines the compact constructor in `quantum_mechanism_tree_book.tex:77-128`. The generator creates the same structure in `compact_operator_formulation_chapter()` and `render_mechanism_guide()`.

   Example from the generated book:

   ```text
   context -> Hilbert-space carrier and operator domain -> generator/evolution -> observable spectrum -> probability readout -> compatibility constraint -> boundary/protocol realization
   ```

   This is consistent with the sparse-attention route statistics in `quantum_mechanism_tree_book.tex:575-588`.

2. **Constructor regularities now match the curated generator selection.**

   The generator selects exactly:

   ```python
   ["R01", "R02", "R03", "R04", "R05", "R06", "R12", "R22"]
   ```

   in `scripts/build_morphwiki_quantum_book.py:2541-2543`. The generated TeX emits the corresponding eight regularities at `quantum_mechanism_tree_book.tex:589-622`:

   - operator-to-spectrum readout
   - state transport
   - admissibility
   - incompatibility
   - context/boundary
   - ordered protocol
   - junction decomposition
   - geometry as realization

3. **The book intentionally sanitizes internal codebook names.**

   The generator states this explicitly in `scripts/build_morphwiki_quantum_book.py:333-335`:

   ```text
   ordinary quantum vocabulary only; codebook names and internal coordinate symbols are intentionally not emitted into the book
   ```

   This is consistent with the public output having no literal V2 codebook names.

4. **The optional V2 language layer exists, but is not part of the current public build.**

   `render_v2_language_chapter()` is implemented in `scripts/build_morphwiki_quantum_book.py:3339-3438`, but it is only included if:

   ```python
   MORPHWIKI_EXPOSE_INTERNAL_METHOD=1
   ```

   at `scripts/build_morphwiki_quantum_book.py:3719-3722`.

### Unsupported Or Weak Correspondence

1. **The public book does not use the full V2 operator/substrate language as its evidence base.**

   The V2 identity structure is now:

   ```text
   I = (operator coordinate, substrate/carrier coordinate; closure, readout/current, protocol/order)
   ```

   The optional chapter maps this to:

   ```text
   I = (Ω, Ξ; C, R, P)
   ```

   but the current tree artifact has no `hyperion_v2_language` field and no V2-row/source-card alignment fields. Thus the book's public constructor is compatible with V2 conceptually, but it is not data-grounded in V2 assignments.

2. **The validation chapter still refers to unavailable old evidence layers.**

   In the generated TeX, `Mechanism Validation Layers` reports placeholders:

   ```text
   The run promoted ? strict currents and ? near currents.
   The run scanned ? Gromov-Wasserstein candidates, hardened ? bridge records, and retained ? artifact-validated method bridges.
   ```

   These lines appear at `quantum_mechanism_tree_book.tex:528-546` and originate from `validation_layers_chapter()` in `scripts/build_morphwiki_quantum_book.py:2264-2460`.

   This is not acceptable as publication text. If the evidence files are absent, the chapter should either be skipped or rewritten as a clear limitation. It should not print question marks.

3. **Page-level Lagrangian roads are absent but printed on every page.**

   Every page currently includes:

   ```text
   Lagrangian construction road. no Lagrangian road map available; road score 0.00.
   ```

   This occurs `146` times. Example: `quantum_mechanism_tree_book.tex:751`.

   This is a generator mismatch: the book has no page-coordinate road map, but the page template still emits a road field. For the public book, this line should be suppressed unless a real page-level road class exists.

4. **Many mechanism readings are still family-level templates.**

   The phrase `In quantum-mechanical terms, ...` appears `93` times. These pages are not all wrong, but they are often generic.

   Example: `Transformation theory (quantum mechanics)` at `quantum_mechanism_tree_book.tex:884-895` is read through a generic Hamiltonian/eigenvalue template. The frame is plausible but not specific enough for transformation theory as a historical/formal change-of-basis program.

   Example: `Introduction to quantum mechanics` at `quantum_mechanism_tree_book.tex:9313-9325` is described as a two-dimensional Hilbert-space/qubit-like construction. That is too narrow for an introductory page and should be treated as an annotation/pedagogical compression page, not as a qubit constructor.

5. **The book reports a page-count inconsistency.**

   The generated book says `147 quantum pages`, `145 topic-specific`, and `1 core-derived` at `quantum_mechanism_tree_book.tex:140`. The tree artifact currently contains `146` branch pages. The transition sparse-attention artifact reports `147`, `145`, and `2`.

   This is a bookkeeping discrepancy between the book tree and the sparse-attention transition artifact. It does not invalidate the constructor reading, but the text should not present inconsistent counts.

6. **The public text still contains method-language residue.**

   The generated TeX contains `17` method/internal terms such as `MorphWiki`, `sparse-attention`, `artifact`, or `diagnostic`. Some are acceptable in the source boundary or methodology framing. Others are too internal for a quantum book.

   Example: `Read anomalies as diagnostics` at `quantum_mechanism_tree_book.tex:135` is still a method instruction. For a public book it should become:

   ```text
   Read anomalies as junctions: a page is structurally interesting when it joins several roles at once.
   ```

## Correspondence With Current V2 Structure

The current V2 structure separates:

```text
primitive factor spaces: operator apparatus and substrate/carrier
attached completion fibers: closure, readout/current, protocol/order
relation layers: typed roads, source-local transitions, bridge families, variational/current candidates, repeated motifs
constructor layers: V2 constructor-completion DAG and source-grounded constructor graph
```

The quantum book corresponds to this only after translation into ordinary quantum language:

| V2 role | Public quantum-book equivalent | Current status in book |
|---|---|---|
| Operator apparatus | Hamiltonian, unitary/channel, observable algebra, commutator, generator | Strongly represented. |
| Substrate/carrier | Hilbert space, Fock space, density-state space, domain, boundary/detector context | Strongly represented, but not explicitly learned from V2 assignments. |
| Closure | normalization, positivity, self-adjointness, gauge/boundary/domain constraints | Represented as admissibility. |
| Readout/current | Born rule, spectral projectors, POVM, detector record, conserved quantity | Represented as probability/readout. |
| Protocol/order | preparation-evolution-measurement order, circuit, channel composition | Represented but sparse. |
| Typed roads / transfer / Gamma | bridge, transfer, and Lagrangian language | Mentioned, but not page-grounded. |
| V2 constructor DAG | constructor-completion order | Conceptually represented as “DAG before constructor,” not backed by V2 DAG rows in this book. |

The book is therefore **V2-compatible but not V2-native**. This distinction should be preserved.

## Why The Text Is Original

The originality is not that the equations of quantum mechanics are new. They are standard. The original contribution is the generated organization and the role-indexed reading.

### 1. It changes the index of the book

A conventional quantum text is indexed by topics such as particle, measurement, wave function, tunnelling, field, interpretation, and algorithm. The generated book re-indexes these topics by construction role:

```text
context -> carrier -> generator -> spectral question -> probability readout -> compatibility -> realization/protocol
```

This is visible in the opening mechanism guide at `quantum_mechanism_tree_book.tex:77-128`.

### 2. It treats topic names as realizations, not roots

Example: `Particle` is not treated as the primitive unit. The book reads it as a stable field/mode/readout realization of the state-operator-spectrum constructor (`quantum_mechanism_tree_book.tex:625`).

Example: `Tunnelling` and boundary-spectrum topics are not separate primitives; they become changes in domain/boundary that alter spectral or transmission readout.

### 3. It identifies junction pages

The book marks pages such as EPR, measurement, quantum biology, wave function, and quantum gravity as junctions. Their importance comes from joining several roles, not from being singular objects.

Example: the constructor regularity `Junction pages require decomposition` appears at `quantum_mechanism_tree_book.tex:615-618`.

### 4. It gives a transferable reading recipe

The public recipe is:

```text
locate the branch -> fill the compact tuple -> separate topic-specific pages from core-derived pages -> read anomalies as junctions -> use transfer only when role contracts survive
```

This is original as an operational reading method, even though every individual quantum ingredient is standard.

### 5. It produces new teaching order, not a new interpretation

The text explicitly says that the constructor order is not a new postulate of quantum mechanics. It is a cleaner order for presenting the existing formalism. That is the correct originality claim.

## Examples Of Good Correspondence

### Hilbert Space

The book says Hilbert space is the admissible carrier, not physical coordinate space. This matches both ordinary quantum mechanics and the V2 substrate/carrier coordinate.

- Generated text: `quantum_mechanism_tree_book.tex:91-101`
- V2 correspondence: substrate/carrier plus closure/admissibility.

### Operator-To-Spectrum

The book places observable spectra as the readout spine. This is supported by route statistics: observable spectra have mean signal `0.327` and are active on `146` pages.

- Generated text: `quantum_mechanism_tree_book.tex:575-588`
- V2 correspondence: operator apparatus plus readout/current fiber.

### Geometry

The book treats geometry as realization or reconstruction rather than invariant root.

- Generated text: `quantum_mechanism_tree_book.tex:619-622`
- V2 correspondence: substrate/realization layer, not the operator identity itself.

## Examples Of Problematic Correspondence

### Repeated Missing Lagrangian Roads

The line “no Lagrangian road map available” appears on every page. This tells the reader what is missing in the build, not what the topic means.

Recommended change:

- Suppress page-level road text unless page road evidence exists.
- Keep one short global limitation in `Source Boundary` or `Mechanism Validation Layers`.

### Generic Page Readings

The generic template is useful as a fallback but should not be allowed to imply page-specific derivation.

Problem example:

```text
Introduction to quantum mechanics is described by a two-dimensional Hilbert space...
```

This is too narrow. It should become an annotation/compression page with several roles, or be removed from mechanism pages.

### Missing V2 Grounding

The book can describe the V2-compatible identity structure in public quantum language, but it should not imply that the current quantum book consumed the full V2 language unless `hyperion_v2_language` artifacts are actually present.

## Recommended Fixes Before Publication

1. **Suppress per-page Lagrangian road lines when road evidence is absent.**

   Do not print `road score 0.00` on every page. Use one global limitation instead.

2. **Gate the validation chapter on real files.**

   If `noether_tau_gw_self_cognition.json`, `lagrangian_landscape_report.json`, or `atlas_void_lagrangian_report.json` are absent, skip the quantitative claims or print a short limitation. Never print `?` counts.

3. **Rename method-facing terms.**

   - `diagnostic` -> `junction reading`
   - `artifact` -> `source record` or `evidence record`
   - `sparse-attention` -> `role-attention analysis` or move to method appendix
   - `MorphWiki` -> keep only in source boundary or method note

4. **Separate page-native constructors from family templates.**

   Pages with generic family templates should be marked as `core-derived` unless they have explicit topic equations or source-card evidence.

5. **Fix page counts.**

   Use a single source of truth for page count. The generated book currently mixes `146` tree pages with `147` sparse-attention pages.

6. **Keep V2 language as hidden method unless fully grounded.**

   Do not expose Ω/Ξ/etc in the quantum book. If V2 is used, translate it into public quantum roles: operator apparatus, admissible carrier, closure, readout/current, protocol/order.

## Bottom Line

The text is original as a generated constructor-indexed synthesis of quantum theory. It is strongest where it explains the compact quantum constructor and the eight constructor regularities. It is weakest where it still exposes missing method layers: repeated absent Lagrangian roads, old GW/role-current placeholders, and generic page templates.

The publication-safe claim is:

> The book reorganizes quantum topics by construction role. Its current evidence supports a compact state-operator-spectrum-readout spine with admissibility, compatibility, realization, and protocol layers. It is compatible with the V2 operator/substrate grammar, but the current public build is not yet a fully V2-grounded source-card constructor book.
