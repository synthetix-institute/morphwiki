# Recover a relation from its original paper

The error-correction chapter explains why syndrome measurement can identify an
error without measuring an unknown logical superposition. Its central condition
is `P E_a^dagger E_b P = c_ab P`. A paper title containing "quantum error
correction" would not be enough evidence for that equation. The source record
locates Gottesman's equation (2.10), which states the condition in a basis of
logical codewords and explains its necessity and sufficiency.

The [published source record](../../discoveries/morphwiki_quantum/original_source_relations.json)
links directly to [that display](https://arxiv.org/html/quant-ph/9705052#Ch2.E10).
The projector and basis formulations describe the same restriction of the
error overlaps to the code subspace. The chapter then works out a three-spin
bit-flip code; its syndrome table is checked independently in the repository.

## What the record establishes

`paper_id` and `display_id` locate the original equation. `equation_latex`
retains its expression. The document, equation and surrounding-context hashes
identify the inspected material. `relation` states its connection to the
chapter, while `scope` keeps the assumptions alongside that connection.

The records have `source_origin: original_arxiv_html` and
`v2_card_alignment: not_established`. Some papers were already retrieval
candidates. Recovering a suitable equation from such a paper does not prove
that it was the display represented by the earlier feature row. Candidate card
identifiers are retained for later comparison, not promoted to confirmed links.

## Reproduce the recovery

From the repository root, install the lightweight HTML dependencies if needed:

```bash
python3 -m pip install requests beautifulsoup4
python3 -B scripts/recover_quantum_original_sources.py \
  --plan docs/quantum_source_recovery_plan.json \
  --cache build/arxiv_originals --fetch \
  --out build/recovered_original_relations.json
```

This fetches seven public arXiv HTML documents and writes their displays and
surrounding context into `build/arxiv_originals`. Downloads are opt-in and
spaced apart. The output is separate from the published record. With the cache
present, the same command without `--fetch` runs offline.

The selection plan gives an exact display identifier and required expression
terms for each relation. A missing display, truncated expression or changed
required term makes recovery fail. A reviewer must still inspect the equation
and neighbouring definitions: syntax and hashes cannot establish physical
relevance. The public record retains mathematical expressions and authored
descriptions, not copies of the article's surrounding prose.

Inspect the example:

```bash
jq '.records[] | select(.topic == "quantum_error_correction")' \
  build/recovered_original_relations.json
jq '.[] | select(.display_id == "Ch2.E10")' \
  build/arxiv_originals/quant-ph_9705052.displays.json
```

The second record for this topic is from a detected-emission feedback paper.
It has a narrower scope: its error record is known. Keeping both scopes prevents
a result for monitored errors from being presented as arbitrary error correction.

## Check the calculation separately

```bash
python3 -B -m pytest -q tests/test_quantum_mechanism_derivations.py
```

The three-qubit calculation verifies all four bit-flip syndromes and the
correction condition on the stated error set. It also checks that a phase flip
acts as an undetected logical error. That negative control explains the limit
of the mechanism, rather than merely confirming that its formula parses.

## Add another source

Work in a candidate copy as described in [the build tutorial](05_build_and_audit.md).
Choose a paper relevant to a particular relation, inspect its original display
and definitions, then add the exact selection to the plan. After recovery,
compare the public record against the cached display and the chapter's symbols.
Differences in units, sign conventions or assumptions belong in `scope`.

The book builder checks record hashes and refuses records that claim an
unestablished corpus alignment. It renders source links separately from general
references. The preservation check counts original-display topics separately
from corpus-aligned topics and fails if an accepted display link disappears
from the PDF source. The committed records rebuild without network access;
recovery from the articles is a separate reproducibility step.

This process supplies traceable foundations for an explanation of established
physics. A proposed discovery still requires a new consequence and an
independent check of that consequence in its target system.
