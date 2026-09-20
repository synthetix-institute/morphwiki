# Follow a topic back to its evidence

A chapter may have a familiar title, a mathematically correct explanation and
several candidate paper identifiers. To cite one of those papers for a specific
equation, the equation and its assumptions must actually be located there.
MorphWiki retains these stages separately.

Start with a cached record; no network request or rebuild is needed:

```bash
python3 -m json.tool \
  discoveries/morphwiki_quantum/pages/schr_dinger_equation.json
```

The record's `wikipedia` field stores legacy topic metadata and attribution.
Its `hyperion` field includes route profiles and candidate witnesses. Other
fields hold the topic's explanation. A witness retrieved through a route match
may be about a different physical problem with similar notation.

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

The legacy Wikipedia scaffold can help locate topics, but it is excluded from
the public theory-book explanation and its scientific source pointers. For a
new paper-based field, start with the
[local-corpus workflow](06_new_field.md) instead of downloading an encyclopedia.

## Inspect the source index of the artifact you have

```bash
python3 -m json.tool \
  discoveries/morphwiki_quantum/v2_quantum_evidence_index.json
```

Use this index with the book generated from it. A newer cluster build and an
older local book can have different evidence coverage; a readiness statement
from one cannot certify the other.

**Exercise.** Choose one candidate identifier from a topic record. Find whether
it appears as a confirmed local equation witness in the evidence index. If it
does not, record which link is missing rather than filling the citation from
the topic name.

[Next: build an explanatory page](03_mechanism_page.md) · [Tutorial](index.md)
