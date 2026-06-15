# Getting Started

This guide is for researchers who can run Python scripts and want to inspect,
modify, or extend MorphWiki.

MorphWiki turns a topic collection into a mechanism-first knowledge object. The
first release uses quantum theory as the test case.

## 1. Install

The core pipeline uses only the Python standard library.

```bash
git clone https://github.com/synthetix-institute/morphwiki.git
cd morphwiki
```

Optional: create a virtual environment if you plan to add PDF parsing, notebooks,
or plotting.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## 2. Build The Quantum Book

Run:

```bash
bash scripts/run_quantum_book.sh
```

This runs three stages:

```text
topic pages -> mechanism tree -> sparse-attention analysis -> LaTeX book
```

Outputs:

```text
discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex
discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.pdf
```

The PDF is built only if `xelatex` or `lualatex` is installed. If no LaTeX engine
is present, the `.tex` file is still generated.

## 3. Inspect The Important Artifacts

Start here:

```text
discoveries/morphwiki_quantum/mechanism_tree.json
discoveries/morphwiki_quantum/rewrite_transition_sparse_attention.json
discoveries/morphwiki_quantum/book/quantum_mechanism_tree_book.tex
```

The tree answers:

```text
Where does each topic sit in the constructor sequence?
```

The sparse-attention file answers:

```text
Which roles dominate?
Which pages are overloaded?
Which pages are easy to place but hard to construct?
Which topics need better equation evidence?
```

The book answers:

```text
How does the mechanism-first rewrite look to a human reader?
```

## 4. Rebuild Topic Pages

The repo includes cached data. You do not need network access for the standard
book build.

To refetch Wikipedia topic pages and rebuild the topic index:

```bash
python -B scripts/export_morphwiki_topic_index.py \
  --topic-preset quantum \
  --expand-wikipedia-links \
  --max-expanded-topics 160 \
  --hyperion-index discoveries/fieldbridge_static_index/hyperion_static_index.json \
  --out-dir discoveries/morphwiki_quantum
```

Then rerun:

```bash
bash scripts/run_quantum_book.sh
```

## 5. Read One Topic As Data

Each topic has a generated Markdown/JSON representation. For example:

```bash
ls discoveries/morphwiki_quantum/pages | head
```

A useful topic record should contain:

```text
standard topic description
mechanism reading
operational grammar
route/fiber evidence
Hyperion witness links
boundary statement
```

If a page reads like a generic paragraph, that is a failure mode. Improve either
the placement rules, the evidence link, or the topic-specific constructor text.

## 6. What To Modify First

If you want to contribute quickly, work in this order.

### Improve a topic

Find a weak page in:

```text
discoveries/morphwiki_quantum/pages/
```

Then update the generator logic in:

```text
scripts/export_morphwiki_topic_index.py
scripts/build_morphwiki_quantum_book.py
```

Do not hand-edit generated pages unless you are only drafting an example.

### Improve the tree

Edit:

```text
scripts/build_morphwiki_quantum_tree.py
```

Then rerun:

```bash
bash scripts/run_quantum_book.sh
```

### Improve anomaly detection

Edit:

```text
scripts/analyze_morphwiki_rewrite_transition.py
```

Useful anomalies are not labels such as “interesting.” They should say what is
mechanistically wrong or overloaded:

```text
operator role missing
readout unclear
boundary does too much work
protocol replaces dynamics
topic joins several incompatible roles
```

## 7. Add A New Field

A new field needs four ingredients:

```text
topic list
source pages or documents
role vocabulary
evidence index
```

The current quantum preset is the template. To add another field, duplicate the
quantum workflow with a new output root:

```text
discoveries/morphwiki_<field>/
```

The important rule is reproducibility: every generated claim must point back to
source pages, equation witnesses, or explicit deterministic scoring logic.

## 8. Scientific Discipline

MorphWiki should not produce mystical or generic prose. Every page should answer
four questions:

```text
What is the state or carrier?
What operator or transformation acts?
What spectrum, readout, or measurement is produced?
What compatibility condition makes the statement legal?
```

If those questions cannot be answered, the page should be marked unresolved
rather than forced into a fake explanation.
