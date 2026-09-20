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

Inspect the `branches` in the JSON. Each page row contains its placement basis,
a secondary branch, route information and any role-promotion metadata.

[assign_pages](../../scripts/build_morphwiki_quantum_tree.py) uses explicit
physical assignments where defined. For other pages, it scores branch route
overlap and keywords, with an optional corpus-derived path contribution.
The branch definitions and their order are supplied in the code. This is a
curated and scored organization, not an unconstrained discovery of the
operation/carrier distinction.

## Make a branch relation physically specific

For the spin example, the state branch provides the tensor product, the
generator branch the interaction, and the observable branch the measured
magnetization. The resulting calculation introduces a correlation. It should
not be filed as “incompatibility” merely because it contains a commutator:
the commutator here computes time evolution, while the missing predictive
coordinate is a property of the joint state.

Likewise, a detector involves a physical implementation and an interaction,
not only an observable label. Preserving such distinctions makes the field
map useful for constructing a calculation rather than simply sorting names.

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
The tree organizes possible uses; executing an operation still requires the
relevant equations. The authored hypotheses in
[analyze_quantum_constructor_rewiring.py](../../scripts/analyze_quantum_constructor_rewiring.py)
are annotated by topic availability and overlap, not derived by those scores.

**Exercise.** Find a page marked `curated_physical_role` and one marked
`topic_native_role_score`. Does the assigned branch explain the page's role in
a prediction? Use the secondary branch to investigate ambiguity rather than
treating the primary score as a physical proof.

[Next: rebuild safely](05_build_and_audit.md) · [Tutorial](index.md)
