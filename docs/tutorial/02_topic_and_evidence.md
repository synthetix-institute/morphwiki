# Follow a topic back to its evidence

A chapter may have a familiar title, a mathematically correct explanation and
several candidate paper identifiers. To cite one of those papers for a specific
equation, the equation and its assumptions must actually be located there.
MorphWiki retains these stages separately.

Start with a cached record. The page
and evidence index are large, so inspect the fields needed for one question:

```bash
python3 - <<'PY'
import json
from pathlib import Path

root = Path('discoveries/morphwiki_quantum')
page = json.loads((root / 'pages/schr_dinger_equation.json').read_text())
index = json.loads((root / 'v2_quantum_evidence_index.json').read_text())
evidence = index['pages']['schr_dinger_equation']
print('Topic:', page['wikipedia']['title'])
print('Candidate paper identifiers:', evidence['legacy_arxiv_ids'][:3])
print('Corpus evidence status:', evidence['status'])
print('Topic-relevant source examples:', evidence['topic_relevant_source_examples'])
PY
```

The record's `wikipedia` field stores legacy topic metadata and attribution.
Its `hyperion` field includes route profiles and candidate witnesses. Other
fields hold the topic's explanation. A witness retrieved through a route match
may be about a different physical problem with similar notation. In the
current cached example, the status is `v2_identifier_linked` and the number of
topic-relevant source examples is zero: candidate identifiers have not become
confirmed witnesses for this relation.

## Read the evidence in layers

| Record | Question it answers |
| --- | --- |
| Topic metadata | What page or concept was used to organize the material? |
| Candidate paper identifier | Where might relevant material be found? |
| Source card and local context | What equation and assumptions were recovered? |
| V2.1 equation alignment | Which extracted equation record corresponds to that context? |
| Topic-relation check | Does the recovered context support the relation this chapter explains? |

[build_morphwiki_v2_quantum_evidence_index.py](../../scripts/build_morphwiki_v2_quantum_evidence_index.py)
joins candidates to source-card evidence.
[audit_morphwiki_v2_quantum_evidence_index.py](../../scripts/audit_morphwiki_v2_quantum_evidence_index.py)
checks the required topic relation, including the stricter central examples.
This is why a paper identifier alone is not published as a confirmed source
pointer.

Legacy Wikipedia metadata locates topic names. The theory-book explanations
and equation citations use physical derivations and inspected papers. A new
paper collection can enter through the
[local-corpus workflow](06_new_field.md).

## Keep evidence with its edition

Use the index with the book generated from it. A newer cluster build and an
older local book can have different evidence coverage. The
[original-paper records](12_original_sources.md) locate specific displays
through a separate source route; V2.1 card alignment has its own status.

**Exercise.** Choose one candidate identifier from a topic record. Find whether
it appears as a confirmed local equation witness in the evidence index. If it
does not, record which link is missing rather than filling the citation from
the topic name.

[Next: build an explanatory page](03_mechanism_page.md) · [Tutorial](index.md)
