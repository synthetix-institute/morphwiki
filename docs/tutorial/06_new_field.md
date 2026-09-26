# Start a field wiki from your own papers

A useful first wiki answers one bounded physical question with a small set of
papers. For active matter, this might be how particle propulsion and wall
interactions determine boundary accumulation. The initial collection should
contain the governing equations, boundary conditions and measured quantities.

The PDF workflow reuses FieldBridge's text extraction and evidence scoring.
It creates linked first-pass pages; a coherent field explanation still needs
the physical derivations that connect them.

## Rehearse with local examples

With FieldBridge next to MorphWiki, install it in the current environment:

```bash
python3 -m pip install -e '../fieldbridge[pdf]'
python3 -B scripts/build_morphwiki_field_from_pdfs.py ../fieldbridge/examples \
  --field-id tutorial_field --label "Tutorial field" \
  --extensions .txt,.tex --max-docs 4 --max-anchors 12 --max-pages 12 \
  --out-dir build/tutorial_field_wiki
```

This uses bundled text and TeX examples, so no PDF corpus or network connection
is needed. Open `build/tutorial_field_wiki/index.md`, then one linked page.
The `fieldbridge/` subdirectory contains the underlying extracted records.

## Supply a research collection

```bash
python3 -B scripts/build_morphwiki_field_from_pdfs.py /path/to/papers \
  --field-id active_matter --label "Active Matter" \
  --out-dir build/active_matter_wiki
```

Text-layer PDFs, TeX, Markdown and plain text are accepted; scanned PDFs require
OCR. The resulting `field_wiki.json` records source files, extraction failures,
recognized roles and generated page paths. Source indexing means a passage can
be traced to an input file, not that every extracted formula has survived PDF
conversion correctly.

## Develop the explanation from the equations

Choose a page with a recoverable equation. Identify the physical state and the
quantity whose behavior is sought. Explain how the boundary, constitutive law
or interaction enters that prediction. Then connect the page to the next
equation required to finish the calculation.

For boundary accumulation, a route score can locate transport and boundary
passages. The actual explanation must show how propulsion and reorientation,
together with the wall condition, affect the density. Simply renaming the
quantum branches would not supply that relation.

The generic builder produces a Markdown field wiki. The quantum book generator
adds authored treatments specific to quantum theory; another field needs its
own physical derivations.

## Add a construction

Recover a source model and state what is to change: a coordinate, boundary,
interaction, measured quantity or operation order. Write the mathematical
relation to be tested. A supported Itô or finite-Hamiltonian problem can use
FieldBridge's exact verifier; another problem requires an appropriate solver
and its own independent checks.

Keep source and target assumptions visible. A successful calculation then
shows why the target response follows. To call it a new discovery candidate,
also establish what consequence was not supplied, how it could be tested,
and how it differs from existing work.

[Source evidence and calculations](09_sources_and_calculations.md) ·
[Physical topic paths](topics/index.md) ·
[Detailed PDF workflow](../PDF_CORPUS_WORKFLOW.md) · [Tutorial](index.md)
