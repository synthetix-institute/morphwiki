# Reproduce the construction calculations

FieldBridge derives consequences of supplied equations. MorphWiki packages
those inputs with the resulting identities, omission checks and software
versions. The three default inputs are authored mathematical benchmarks; the
book's source index records recovered equations separately.

## Run the calculations

Use Python 3.10 or newer. Check out FieldBridge next to MorphWiki. From the
MorphWiki root, create an environment and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e '../fieldbridge[construction]'
python3 -B scripts/build_construction_companion.py \
  --fieldbridge-root ../fieldbridge --out-dir build/construction_companion
```

Expect `status: complete` and `calculations: 3`. The builder checks identities
and omission results, copies each mathematical input, and records implementation
hashes and software versions in `manifest.json`. An unsuccessful rerun marks
the manifest incomplete or failed rather than leaving an earlier completed
manifest in place. The build writes to the selected calculation directory.

The optional [inverse interaction construction](11_inverse_construction.md)
uses `--include-spin-design` and produces a fourth calculation in
`spin_cancellation_design/design.json` and `design.md`.

## Read the output

| File | Purpose |
| --- | --- |
| `README.md` | Summary of the derived results and links to each calculation |
| `manifest.json` | Calculation identities, source hashes and software versions |
| `<case>/input.json` | Supplied equations, assumptions and provenance |
| `<case>/calculation.json` | Derived coefficients or observable basis for the three default cases |
| `<case>/calculation.md` | Readable derivation for the three default cases |

Start with `quantum_correlations/calculation.md` and compare its closed
observable span with the [two-spin derivation](08_quantum_construction.md).
For the optional inverse case, the report names are `design.json` and
`design.md` instead; the manifest records the actual paths.

```text
build/construction_companion/
  manifest.json                 inputs, code identity and case status
  quantum_correlations/
    input.json                  supplied Hamiltonian and observable
    calculation.md             derived closed observable span
    calculation.json           identities and evolution matrix
```

The calculation gives a two-dimensional span. Change the measured operator
as in the [spin exercise](08_quantum_construction.md), and the span falls to
one dimension. This comparison shows what the calculation depends on.

For a retrieved-record demonstration, FieldBridge also provides
`construct --calculate`, with the walkthrough in its
`docs/tutorial/13_retrieval_to_calculation.md`. That path emits its specification
from the selected retrieved source and an explicit correspondence. Its
additional source-binding check relates the retrieved record to the
calculation input. Original-paper alignment identifies the display and nearby
assumptions.

The selected Python environment must contain SymPy; the installation command
above provides it. No atlas download or TeX engine is needed. The scalar
examples verify local differential expressions, while the quantum example
verifies finite Hamiltonian dynamics.

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

The build regenerates the selected output directory. The
[submission module](13_submission_scope.md) assigns the resulting calculations
and the expository book their respective roles.

[Next: submission scope](13_submission_scope.md) · [Tutorial](index.md)
