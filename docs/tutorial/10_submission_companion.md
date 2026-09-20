# A reproducible companion to the discovery method

The quantum book and the calculation software answer different reader needs.
The book explains how choices of states, generators, observables and physical
conditions fit together. The software derives consequences from specified
equations and makes the decisive assumptions testable. Together they can
support a methods demonstration without presenting the entire book as a new
quantum theory.

## Reproduction

From MorphWiki, with FieldBridge checked out next to it:

```bash
python3 -m pip install -e '../fieldbridge[construction]'
python3 -B scripts/build_construction_companion.py \
  --fieldbridge-root ../fieldbridge --out-dir build/construction_companion
```

The builder runs three examples, checks their expected identities and
omission results, copies each mathematical input, and records the implementation
hashes and software versions in `manifest.json`. An unsuccessful rerun marks
the manifest incomplete or failed rather than leaving an earlier completed
manifest in place. The full quantum book is not regenerated or overwritten.

The default build has three calculations. Add `--include-spin-design` to
include the [inverse interaction construction](11_inverse_construction.md)
as a fourth. Its outputs are `spin_cancellation_design/design.json` and
`design.md`; the manifest links to the appropriate report for every case.

The output contains:

| File | Purpose |
| --- | --- |
| `README.md` | Summary of the derived results and links to each calculation |
| `manifest.json` | Calculation identities, source hashes and software versions |
| `*/input.json` | Equations, assumptions and provenance for each example |
| `*/calculation.json` | Machine-readable derived coefficients or observable basis |
| `*/calculation.md` | The same calculation in a readable record |

For a retrieved-record demonstration, FieldBridge also provides
`construct --calculate`, with the walkthrough in its
`docs/tutorial/13_retrieval_to_calculation.md`. That path emits its specification
from the selected retrieved source and an explicit correspondence. Its
additional source-binding check should be described separately from original
paper alignment and from a comparison of retrieval methods.

The command uses the supplied FieldBridge path, so no hidden optional package
or atlas download is required. SymPy must be installed in the selected Python
environment. The scalar examples verify local differential expressions; the
quantum example verifies the finite Hamiltonian dynamics. The scope travels
with every result.

## Material for a submission

A focused supplementary account can develop the exact transfer, the derived
stochastic correction and the quantum observable construction. The essential
equations and the physical reason for the correction belong in that account;
input hashes and execution details belong with the reproduction files.

The complete book can be deposited as a separately versioned companion,
together with its source index and a permanent identifier. A code release
should include the inputs, software dependencies, expected outputs and the
same version of the calculation module used to obtain them. These are
packaging recommendations, not a claim that the local book's evidence layer
is already complete.

An additional prospective discovery would require a physical construction
whose distinguishing response was not supplied in its input. That example
should show where the candidate came from, which equation was derived, and
which calculation or measurement tested the prediction. The three current
examples are known mathematical benchmarks and must remain identified as
such. Their role is to establish that a proposed construction can produce
and test an equation, not to increase a discovery count.

## Check the package before sharing it

```bash
python3 - <<'PY'
import json
from pathlib import Path

root = Path('build/construction_companion')
manifest = json.loads((root / 'manifest.json').read_text(encoding='utf-8'))
assert manifest['status'] == 'complete'
assert len(manifest['calculations']) in (3, 4)  # The fourth is the optional inverse design.
for case in manifest['calculations']:
    assert (root / case['input']).is_file()
    assert (root / case['report']).is_file()
    print(case['id'], case['status'])
print('Software:', manifest['software'])
PY
```

Keep this output with the exact input files and code version. The calculation
report contains an input identity; the manifest also hashes the implementation
and generated reports. These make a reproduction specific, while the equations
and controls establish what the reproduction means physically.

| Problem | Remedy |
| --- | --- |
| FieldBridge root is rejected | Pass the standalone repository containing `fieldbridge/verification.py`, not its package subdirectory |
| SymPy is missing | Install `../fieldbridge[construction]` in the Python environment running the builder |
| A different Python is needed | Set `--python /absolute/path/to/python` explicitly |
| Manifest says failed | Read the exception, correct the input or environment, then rerun; do not distribute the old summary alone |
| Book source coverage is missing | Recover or label the book evidence separately; these benchmark calculations do not supply its citations |

The book, manuscript, figures and language-skill files are outside this
companion build. Only the selected output directory is regenerated.

[Tutorial](index.md)
