# Use the calculations and book in a submission

The [calculation package](10_submission_companion.md) and the quantum book have
different evidential roles. The package derives consequences of specified
equations. The book explains how state spaces, dynamics, observables and
physical conditions fit together across established quantum theory. The
default calculation inputs are authored benchmarks.

## Focus the methods account

A methods supplement can develop the exact affine transfer, the stochastic
correction and the two-spin observable construction. Give the equations and
the physical reason for each result there; keep input hashes, software versions
and machine-readable reports with the calculation package. The optional
[inverse spin construction](11_inverse_construction.md) shows how interaction
coefficients follow from a commutation requirement.

## Keep the expository book separate

The [expository edition](../../discoveries/morphwiki_quantum/book/companion/quantum_mechanism_tree_book.pdf)
retains all 62 topic-specific treatments. Its reference index also records 63
overview subjects, four alternative names and 17 historical or interpretive
entries, without presenting repeated branch equations as individual derivations.
The [full reference edition](../../discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.pdf)
remains available separately. Both editions state the authorship of the
mechanism tree on the title page. Paper links appear beside the relations they
support. Counts and equation identifiers are kept in the
[edition manifest](../../discoveries/morphwiki_quantum/book/companion/edition_manifest.json)
rather than repeated as prefatory comments on every topic page.

The opening two-spin calculation explains the nested notation through a
prediction. Density operators on the joint spin space form the carrier
$\Xi$; the commutator with the Hamiltonian supplies $\Omega$; positivity
and normalization constrain states; and measuring $X_1$ defines the
observable. Two allowed preparations have the same measured polarization
but different initial slopes. The eliminated spin correlation is therefore
required for a closed evolution of that polarization. The book derives
this result before using the notation to compare other mechanisms.

Rebuild both editions from the existing cached records with:

```bash
bash scripts/run_quantum_expository_companion.sh
```

The [book integrity report](../../discoveries/morphwiki_quantum/book/companion/companion_integrity.md)
compares every retained treatment with the full edition, checks the reference
index separately, and checks that source links remain at the relevant
treatments. Scientific review remains incomplete; executable checks currently
cover selected identities.

The expository edition can be deposited as a separately versioned companion
with its source index and a permanent identifier. The local build has no DOI.
The book supplies background exposition; a discovery claim would rest on its
own derivation and target-system test. A code release
should include the inputs, dependencies, expected outputs and the calculation
module version. The book's source coverage is reported separately from the
exactness of the benchmark calculations.

## Distinguish a new construction

The three default calculations are known mathematical benchmarks. A prospective
discovery would require a distinguishing consequence absent from the input,
its derivation, a test in the target system and a comparison with established
results. The methods examples demonstrate the calculation and its controls.

[Run the calculation package](10_submission_companion.md) · [Tutorial](index.md)
