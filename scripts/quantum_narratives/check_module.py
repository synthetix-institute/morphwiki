"""Check one module of authored topic narratives before it enters the quantum book.

Usage: python3.11 -I scripts/quantum_narratives/check_module.py scripts/quantum_narratives/<group>.py

The module must define NARRATIVES = {slug: [("p", text) | ("eq", latex), ...]} and
REFERENCES = {slug: [(arxiv_id, description), ...]}. Paragraphs are typeset as the book typesets
them: inline math between single dollars, every other character escaped, so no LaTeX command may
appear outside $...$. Displays are placed in the book's centred gathered environment. The script
reports structural errors and jargon, then compiles all narratives in a standalone document.
"""
import importlib.util
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))
from build_morphwiki_quantum_book import latex_editorial_math, center_equation_rows  # noqa: E402

JARGON = [r"\bconstructor", r"\bcarrier\b", r"\bcarriers\b", r"\breadout", r"\bphysical role", r"\bmechanism tree",
          r"\boperational identity", r"\brealization layer", r"\bthe page\b", r"\bthis page\b", r"\bnested\b",
          r"\bslot\b", r"\bwe\b", r"\bour\b", r"\bfirst time\b", r"\bnovel\b", r"\bgroundbreaking\b"]


def main(path: str) -> int:
    spec = importlib.util.spec_from_file_location("narratives_under_check", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    errors, warnings = [], []
    nar, refs = getattr(mod, "NARRATIVES", None), getattr(mod, "REFERENCES", None)
    if not isinstance(nar, dict) or not isinstance(refs, dict):
        print("ERROR: module must define dicts NARRATIVES and REFERENCES")
        return 1
    body = []
    for slug, items in nar.items():
        if not re.fullmatch(r"[a-z0-9_]+", slug):
            errors.append(f"{slug}: slug must be lowercase with underscores")
        words = 0
        n_eq = 0
        for i, item in enumerate(items):
            if not (isinstance(item, tuple) and len(item) == 2 and item[0] in ("p", "eq") and isinstance(item[1], str)):
                errors.append(f"{slug}[{i}]: each item must be ('p', text) or ('eq', latex)")
                continue
            kind, text = item
            if kind == "p":
                outside = re.sub(r"\$[^$\n]+\$", "", text)
                if "\\" in outside:
                    errors.append(f"{slug}[{i}]: LaTeX command outside $...$: {outside[outside.index(chr(92)) - 20:outside.index(chr(92)) + 20]!r}")
                if text.count("$") % 2:
                    errors.append(f"{slug}[{i}]: odd number of $")
                words += len(outside.split())
                for pat in JARGON:
                    m = re.search(pat, outside, flags=re.I)
                    if m:
                        warnings.append(f"{slug}[{i}]: avoid '{m.group(0)}'")
                for s in re.split(r"(?<=[.!?])\s+", outside):
                    if len(s.split()) > 38:
                        warnings.append(f"{slug}[{i}]: sentence of {len(s.split())} words")
            else:
                n_eq += 1
                if re.search(r"\n\s*\n", text):
                    errors.append(f"{slug}[{i}]: blank line inside a display")
                if "\\label" in text or "\\begin{align" in text or "\\begin{equation" in text:
                    errors.append(f"{slug}[{i}]: no labels or equation environments inside a display")
        if not 280 <= words <= 900:
            warnings.append(f"{slug}: {words} words of prose (aim 350-650)")
        if n_eq < 2:
            warnings.append(f"{slug}: only {n_eq} display(s)")
        if items and items[0][0] != "p":
            errors.append(f"{slug}: must open with a paragraph that states the physical question")
        body.append(rf"\section*{{{slug.replace('_', ' ')}}}")
        for kind, text in items:
            body.append(latex_editorial_math(text) if kind == "p"
                        else "\\begin{centeredalign}\n" + text + "\n\\end{centeredalign}")
    for slug, rs in refs.items():
        if slug not in nar:
            errors.append(f"REFERENCES has {slug} without a narrative")
        for r in rs:
            if not (isinstance(r, tuple) and len(r) == 2 and re.fullmatch(r"(\d{4}\.\d{4,5}|[a-z\-]+(\.[A-Z]{2})?/\d{7})", r[0])):
                errors.append(f"{slug}: reference {r!r} must be (arxiv_id, description)")
    for slug in nar:
        if not refs.get(slug):
            warnings.append(f"{slug}: no reference")
    tex = "\n".join([
        r"\documentclass[11pt]{book}", r"\usepackage[a4paper,margin=1in]{geometry}", r"\usepackage[T1]{fontenc}",
        r"\usepackage[utf8]{inputenc}", r"\usepackage{amsmath,amssymb}", r"\usepackage{hyperref}",
        r"\newenvironment{centeredalign}{\[\begin{gathered}[c]}{\end{gathered}\]}",
        r"\newcommand{\ket}[1]{\lvert #1\rangle}", r"\newcommand{\bra}[1]{\langle #1\rvert}", r"\begin{document}",
        center_equation_rows("\n\n".join(body)), r"\end{document}"])
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "check.tex").write_text(tex, encoding="utf-8")
        res = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "check.tex"], cwd=tmp,
                             capture_output=True, text=True, env={"PATH": "/Library/TeX/texbin:/usr/bin:/bin"})
        log = (Path(tmp) / "check.log").read_text(errors="replace") if (Path(tmp) / "check.log").exists() else res.stdout
        if res.returncode != 0:
            err = [l for l in log.splitlines() if l.startswith("!")]
            i = log.find("\n!")
            errors.append("LaTeX failed: " + "; ".join(err[:3]) + " | context: " + log[i:i + 400].replace("\n", " "))
        over = len(re.findall(r"Overfull \\hbox \((\d+\.\d+)pt", log))
        if over:
            warnings.append(f"{over} overfull lines in the standalone compile (check long displays)")
    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARN:", w)
    print(f"{len(nar)} narratives, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
