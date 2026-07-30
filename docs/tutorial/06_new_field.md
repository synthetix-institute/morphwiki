# Chapter 6: Create a Wiki for Another Field

The reusable object is the field-wiki contract, not the quantum chapter list.
A new field needs its own corpus and its own measured constructor spine.

## Step 1: Define the Public Entry Points

Create a newline-separated topic file from Wikipedia titles, review sections
or a curated field vocabulary:

```text
active matter
motility-induced phase separation
active stress
collective motion
boundary accumulation
```

## Step 2: Export Source-Grounded Pages

For a folder of PDFs, use the shared FieldBridge ingestion path:

```bash
python3 -m pip install -e '../fieldbridge[pdf]'
python3 -B scripts/build_morphwiki_field_from_pdfs.py /path/to/papers \
  --field-id active_matter \
  --label "Active Matter" \
  --out-dir discoveries/morphwiki_active_matter
```

This produces source-indexed topic, mechanism, and construction views. PDFs
must contain a text layer; scanned papers require OCR first. Full details are
in [PDF_CORPUS_WORKFLOW.md](../PDF_CORPUS_WORKFLOW.md).

For Wikipedia or a curated topic list, use the topic exporter:

```bash
python3 -B scripts/export_morphwiki_topic_index.py \
  --topic-file topics/active_matter.txt \
  --expand-wikipedia-links \
  --hyperion-index discoveries/fieldbridge_static_index/hyperion_static_index.json \
  --out-dir discoveries/morphwiki_active_matter
```

This stage creates the topic and operational-evidence views. It does not yet
justify a constructor order.

## Step 3: Infer the Field Roles

Profile the pages for recurrent carriers, operations, closure conditions,
readouts and protocols. Candidate active-matter roles might include particle
or field state, propulsion, transport/interaction, density or stress closure,
boundary coupling, collective readout and perturbation protocol. These labels
must be inferred and audited against the field corpus rather than copied from
the quantum spine.

## Step 4: Build Three Synchronized Views

```text
topic view        familiar field vocabulary and sources
mechanism view    Omega, Xi, C, R, P clauses for each page
construction view dependencies and missing obligations
```

## Step 5: Audit Before Publication

A publishable field wiki should report:

- page coverage and source coverage;
- stability of the inferred role structure;
- pages with insufficient equation evidence;
- overloaded topics assigned to several incompatible roles;
- unresolved constructor dependencies;
- links back to the original sources and equations.

## Cross-Field Use

Once two field wikis use the same upper-level contract, they can be linked by
mechanism-preserving transformations. The link should state which operation is
retained, which carrier or completion clause changes and which observation
would reject the proposed transfer. That is how MorphWiki becomes a map of
fields organized by mechanisms rather than a collection of AI summaries.

Return to the [tutorial index](index.md).
