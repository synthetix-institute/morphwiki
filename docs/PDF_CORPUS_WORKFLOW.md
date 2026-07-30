# Build a Mechanism-First Field Wiki from PDFs

MorphWiki can build a first-pass field wiki from a local folder of scientific
papers. The workflow joins two distinct responsibilities:

1. **FieldBridge** extracts text, equations, operational routes, constructor
   roles, substrate evidence, and source anchors.
2. **MorphWiki** arranges those source anchors into topic, mechanism, and
   construction views.

This separation keeps PDF parsing and operational scoring consistent across the
two repositories.

## Install

Clone the repositories beside one another:

```text
work/
  fieldbridge/
  morphwiki/
```

Then install FieldBridge with PDF support:

```bash
cd morphwiki
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e '../fieldbridge[pdf]'
```

The standard MorphWiki quantum-book build remains independent of FieldBridge.
The dependency is required only for PDF-folder ingestion.

## Input Contract

The folder is searched recursively for:

```text
.pdf  .txt  .tex  .md
```

PDFs must contain an embedded text layer. The workflow does not perform OCR.
Run OCR first for scanned papers. Corrupt or unreadable documents are recorded
and skipped; they do not stop the rest of the corpus.

## Run

```bash
python3 -B scripts/build_morphwiki_field_from_pdfs.py /path/to/papers \
  --field-id active_matter \
  --label "Active Matter" \
  --description "Mechanism-first index of an active-matter paper collection." \
  --out-dir discoveries/morphwiki_active_matter \
  --max-docs 300 \
  --max-chunks-per-doc 40 \
  --max-anchors 120 \
  --max-pages 120
```

For a quick preflight:

```bash
python3 -B scripts/build_morphwiki_field_from_pdfs.py /path/to/papers \
  --field-id active_matter_smoke \
  --max-docs 5 \
  --max-chunks-per-doc 5 \
  --max-anchors 10 \
  --max-pages 10 \
  --out-dir build/active_matter_smoke
```

## Outputs

```text
discoveries/morphwiki_active_matter/
  index.md
  field_wiki.json
  pages/
    <mechanism-anchor>.md
  fieldbridge/
    field_adapters/active_matter.json
    field_pack_evidence/active_matter.json
    kg/active_matter_knowledge_graph.json
    index/core_examples.json
    reports/active_matter_adapter.md
```

Each page contains:

- a topic view tied to the source passage;
- the operational identity \(M=(\Omega,\Xi)\);
- closure, readout, and protocol clauses \(C,R,P\);
- representative equations;
- route and substrate evidence;
- falsifiers found in the source;
- explicit unresolved entries when a clause is absent.

The script does not fill a missing clause from a generic template. This is
important: a fluent page is not evidence that a mechanism is complete.

## Review

Read the files in this order:

1. `fieldbridge/reports/<field_id>_adapter.md`
2. `index.md`
3. pages marked `incomplete_candidate`
4. `fieldbridge/field_pack_evidence/<field_id>.json`
5. the original PDF passages and equations

Before publication:

- merge duplicate anchors from the same paper;
- verify every equation against the source PDF;
- name the field-specific constructor spine;
- check whether each role is supported across several documents;
- keep missing closure, readout, protocol, or control clauses unresolved;
- add empirical or formal validation separately.

The generated wiki is a source-grounded field scaffold, not a completed
textbook and not a validation of the extracted mechanisms.
