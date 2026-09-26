# How topics become a connected field map

The quantum map groups topics by their role in a prediction. Hilbert space and
subsystem composition specify admissible states. A Hamiltonian specifies
evolution. An observable and a preparation connect that evolution to an
experiment. These dependencies motivate the organization, while individual
topics may contribute to more than one role.

## Reproduce placement without rebuilding the book

```bash
mkdir -p build/tutorial
python3 -B scripts/build_morphwiki_quantum_tree.py \
  --root discoveries/morphwiki_quantum \
  --out-json build/tutorial/quantum_tree.json \
  --out-md build/tutorial/quantum_tree.md
```

The `branches` object contains page rows. Compare one curated assignment with
one row placed by a topic score:

```bash
python3 - <<'PY'
import json
from pathlib import Path

tree = json.loads(Path('build/tutorial/quantum_tree.json').read_text())
rows = [(branch, page) for branch, data in tree['branches'].items()
        for page in data['pages']]
for basis in ('curated_physical_role', 'topic_native_role_score'):
    branch, page = next((branch, page) for branch, page in rows
                        if page['placement_basis'] == basis)
    print(page['title'], '->', branch, '(', basis, ')')
PY
```

Each row also records a secondary branch, route information and any
role-promotion metadata. The two printed examples show that an authored
physical assignment and a score are different grounds for placement.

[assign_pages](../../scripts/build_morphwiki_quantum_tree.py) uses explicit
physical assignments where defined. For other pages, it scores branch route
overlap and keywords, with an optional corpus-derived path contribution.
The branch definitions and their order are supplied in the code. The printed
placements show how the supplied roles and route scores organize the topics.

## Make a branch relation physically specific

For the spin example, the state branch provides the tensor product, the
generator branch the interaction, and the observable branch the measured
magnetization. The resulting calculation introduces a correlation. Here the
commutator computes time evolution; the additional predictive coordinate is
an expectation of the joint state.

A detector also requires an interaction with the system and a physical
implementation of the measurement. These relations tell the reader how the
topic enters a calculation.

## Use the six operations as questions

| Operation | A concrete question |
| --- | --- |
| Complete | Which additional expectation makes the measured response closed? |
| Reattach | Which state and observable maps realize the same evolution in another system? |
| Compose | What is the result of an ordered sequence of allowed maps? |
| Deform | How does a parameter or boundary change the predicted spectrum or response? |
| Observe | Which measurement distinguishes two proposed mechanisms? |
| Revise | Which changed assumption or equation corrects a failed consequence? |

These definitions live in [morphwiki_constructor.py](../../scripts/morphwiki_constructor.py).
The tree organizes possible uses; each operation takes specified equations.
The authored hypotheses in
[analyze_quantum_constructor_rewiring.py](../../scripts/analyze_quantum_constructor_rewiring.py)
carry topic-availability and overlap annotations.

**Exercise.** Find a page marked `curated_physical_role` and one marked
`topic_native_role_score`. Does the assigned branch explain the page's role in
a prediction? Use the secondary branch to investigate ambiguity rather than
treating the primary score as a physical proof.

[Next: rebuild safely](05_build_and_audit.md) · [Tutorial](index.md)
