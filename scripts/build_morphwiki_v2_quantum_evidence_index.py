#!/usr/bin/env python3
"""Build a page-level MorphWiki quantum evidence index from V2 artifacts.

This is an evidence adapter. It keeps V2 symbolic artifacts private and links
quantum pages to source-card examples only when identifiers overlap.
"""
from __future__ import annotations

import argparse, json, re, hashlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Iterable

ARXIV_RE = re.compile(r"(?:arxiv:\s*)?(?:(?P<old>[a-z][a-z-]+/[0-9]{7})|(?P<oldflat>[a-z][a-z-]+[0-9]{7})|(?P<new>[0-9]{4}\.[0-9]{4,5}))(?:v[0-9]+)?", re.I)
TOKEN_RE = re.compile(r"(?:Ω|Ξ|Λ|T|Τ|Γ|J|Π)[0-9]{2,3}|(?:A\*?|Α)[0-9]{2}")
ROLES = {"operator_apparatus","real_substrate_geometry","selector","selector_context","closure_constraints","readout_current","protocol_order"}
ROUTES = {"transport_flow","spectral_operator","boundary_weak_form","constraint_closure","discrete_protocol","commutator_incompatibility","unclassified"}


def load_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def try_json(path: str | Path | None) -> Any:
    if not path:
        return None
    p = Path(path)
    if not p.exists() or not p.is_file():
        return None
    try:
        return load_json(p)
    except Exception:
        return None

def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def variants(value: Any) -> set[str]:
    if value is None:
        return set()
    text = str(value).lower().replace('https://arxiv.org/abs/', ' ').replace('http://arxiv.org/abs/', ' ')
    out = set()
    for m in ARXIV_RE.finditer(text):
        raw = (m.group('old') or m.group('oldflat') or m.group('new') or '').lower()
        raw = re.sub(r'v[0-9]+$', '', raw)
        if not raw:
            continue
        out.add(raw); out.add(raw.replace('/', ''))
        mm = re.match(r'^([a-z][a-z-]+)([0-9]{7})$', raw)
        if mm:
            out.add(mm.group(1) + '/' + mm.group(2))
    return out

def collect_ids(obj: Any, limit: int = 64) -> set[str]:
    found: set[str] = set()
    def walk(x: Any) -> None:
        if len(found) >= limit:
            return
        if isinstance(x, Mapping):
            for k, v in x.items():
                ks = str(k).lower()
                if any(s in ks for s in ('arxiv','paper','source','doc','url','example')):
                    found.update(variants(v))
                if isinstance(v, (Mapping, list, tuple)):
                    walk(v)
        elif isinstance(x, (list, tuple)):
            for y in x:
                walk(y)
        elif isinstance(x, str):
            found.update(variants(x))
    walk(obj)
    return found

def detect(v2_root: Path, explicit: Mapping[str, str]) -> dict[str, str]:
    pats = {
        'hierarchical_language': ['*hierarchical_language.json'],
        'symbolic_language': ['*symbolic_language.json'],
        'symbolic_full_assignment': ['*symbolic_full_assignment.json'],
        'grammar_rules': ['*grammar_rule_learner.json', '*grammar_rules.json'],
        'source_language_examples': ['*source_language_examples_full.json', '*source_language_examples.json'],
        'source_card_alignment': ['*source_card_alignment.json'],
        'source_card_alignment_jsonl': ['*source_card_alignment.jsonl'],
        'source_constructor_graph': ['*source_constructor_graph.json'],
        'v2_dag': ['*v2_dag.json'],
        'gamma_bridges': ['*gamma_bridges.json', '*gamma_bridge*.json'],
        'readout_application_coverage': ['*readout_application_coverage.json'],
        'apparatus_basin_a00': ['*apparatus_basin_A00_audit.json'],
    }
    out = {}
    for k, v in explicit.items():
        if v and Path(v).is_file():
            out[k] = str(Path(v))
    if v2_root.exists():
        for k, ps in pats.items():
            if k in out:
                continue
            found = []
            for p in ps:
                found += sorted(v2_root.glob(p))
            if found:
                if k == 'source_language_examples':
                    chosen = sorted(found, key=lambda x: ('full' not in x.name, x.name))[0]
                else:
                    chosen = sorted(found, key=lambda x: (x.stat().st_size, x.name))[0]
                out[k] = str(chosen)
    return out

def brief(path: str) -> dict[str, Any]:
    d = try_json(path)
    if not isinstance(d, Mapping):
        return {'path': path, 'available': False}
    out = {'path': path, 'available': True, 'report_type': d.get('report_type'), 'readiness': d.get('readiness')}
    for k in ['language_counts','logical_compactness','recommendation','coverage','cards_loaded','cards_aligned','links_written','claim_scope']:
        if k in d:
            val = d[k]
            if k == 'coverage' and isinstance(val, Mapping):
                out[k] = {kk: {a: b for a, b in dict(v).items() if a in {'source_grounded_rate','tokens_with_examples','known_tokens','grounding_rate','checked','grounded'}} for kk, v in val.items() if isinstance(v, Mapping)}
            else:
                out[k] = val
    if isinstance(d.get('hierarchy'), Mapping):
        out['hierarchy'] = {
            'grammar_rules': d.get('grammar_rules') or {},
            'claims_supported': (d.get('claims_supported') or [])[:8],
            'source_grounding': ((d.get('hierarchy') or {}).get('source_grounding') or {}).get('by_kind'),
        }
    return out

def load_pages(root: Path) -> tuple[dict[str, dict[str, Any]], dict[str, set[str]]]:
    pages, id_to_slugs = {}, defaultdict(set)
    for p in sorted((root / 'pages').glob('*.json')):
        try:
            d = load_json(p)
        except Exception:
            continue
        slug = p.stem
        title = ((d.get('wikipedia') or {}).get('title') or slug.replace('_',' ')).strip()
        witnesses = (d.get('hyperion') or {}).get('equation_witnesses') or []
        ids = set()
        for w in witnesses:
            ids.update(collect_ids(w, 16))
        pages[slug] = {'slug': slug, 'title': title, 'path': str(p), 'legacy_witness_count': len(witnesses), 'legacy_arxiv_ids': sorted(ids)}
        for i in ids:
            id_to_slugs[i].add(slug)
    return pages, id_to_slugs

def empty_page(meta: Mapping[str, Any], max_examples: int) -> dict[str, Any]:
    return {'title': meta.get('title'), 'legacy_witness_count': meta.get('legacy_witness_count',0), 'legacy_arxiv_ids': meta.get('legacy_arxiv_ids',[]), 'status': 'legacy_witness_only' if meta.get('legacy_witness_count') else 'no_evidence', 'matched_alignment_records': 0, 'matched_source_examples': 0, 'matched_v2_row_ids': [], 'matched_source_card_ids': [], 'tokens': {}, 'routes': {}, 'constructor_roles': {}, 'source_examples': [], 'max_examples': max_examples, '_tokens': Counter(), '_routes': Counter(), '_roles': Counter()}

def tokens(obj: Any) -> list[str]:
    try:
        text = obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False)
    except Exception:
        text = str(obj)
    return TOKEN_RE.findall(text)

def routes(obj: Any) -> list[str]:
    out = []
    if isinstance(obj, Mapping):
        for k, v in obj.items():
            base = str(k).replace('_route','')
            if base in ROUTES:
                try:
                    if not isinstance(v, (int,float)) or float(v) > 0:
                        out.append(base)
                except Exception:
                    out.append(base)
            if str(k) in {'routes','route','route_tokens','target_route'}:
                vals = v.items() if isinstance(v, Mapping) else (v if isinstance(v, list) else re.split(r'[,;\s]+', str(v)))
                for item in vals:
                    name = (item[0] if isinstance(item, tuple) else item)
                    name = str(name).replace('_route','')
                    if name in ROUTES:
                        out.append(name)
            if isinstance(v, (Mapping, list, tuple)):
                out.extend(routes(v))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(routes(v))
    return out

def roles(obj: Any) -> list[str]:
    out = []
    if isinstance(obj, Mapping):
        for k, v in obj.items():
            if str(k) in ROLES and bool(v):
                out.append(str(k))
            if str(k) in {'roles','constructor_roles','role','constructor_role'}:
                vals = v if isinstance(v, list) else re.split(r'[,;\s]+', str(v))
                out.extend([str(x) for x in vals if str(x) in ROLES])
            if isinstance(v, (Mapping, list, tuple)):
                out.extend(roles(v))
    elif isinstance(obj, list):
        for v in obj:
            out.extend(roles(v))
    return out

def preview(obj: Mapping[str, Any]) -> str:
    for k in ['equation_preview','equation','source_equation','target_equation','latex','text','subject','object']:
        if obj.get(k):
            return re.sub(r'\s+', ' ', str(obj[k])).strip()[:240]
    return ''

def row_ids(obj: Any) -> set[int]:
    out = set()
    if isinstance(obj, Mapping):
        for k, v in obj.items():
            if str(k) in {'row_id','v2_row_id','feature_row_id','src','dst','row'}:
                try: out.add(int(v))
                except Exception: pass
            elif str(k) in {'row_ids','v2_row_ids','feature_row_ids'} and isinstance(v, list):
                for x in v:
                    try: out.add(int(x))
                    except Exception: pass
            elif isinstance(v, (Mapping, list, tuple)):
                out.update(row_ids(v))
    elif isinstance(obj, list):
        for v in obj:
            out.update(row_ids(v))
    return out

def card_ids(obj: Any) -> set[str]:
    out = set()
    if isinstance(obj, Mapping):
        for k, v in obj.items():
            if str(k) in {'card_id','source_card_id','equation_card_id','node_id'} and v:
                out.add(str(v))
            elif isinstance(v, (Mapping, list, tuple)):
                out.update(card_ids(v))
    elif isinstance(obj, list):
        for v in obj:
            out.update(card_ids(v))
    return out

def example_records(obj: Any) -> Iterable[Mapping[str, Any]]:
    if isinstance(obj, Mapping):
        keys = set(map(str, obj.keys()))
        if keys & {'equation_preview','equation','source_equation','target_equation','latex','paper_id','source_id','v2_row_id','equation_card_id','token'}:
            if collect_ids(obj, 4) or tokens(obj) or preview(obj):
                yield obj
        for k, v in obj.items():
            if k == 'cleanliness':
                continue
            if isinstance(v, (Mapping, list, tuple)):
                yield from example_records(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from example_records(v)

def stream_jsonl(path: Path, max_rows: int) -> Iterable[Mapping[str, Any]]:
    with path.open('r', encoding='utf-8', errors='replace') as f:
        for n, line in enumerate(f):
            if max_rows and n >= max_rows:
                break
            try:
                d = json.loads(line)
            except Exception:
                continue
            if isinstance(d, Mapping):
                yield d

def add_match(page: dict[str, Any], obj: Mapping[str, Any], source: str, max_examples: int) -> None:
    if source == 'source_language_examples': page['matched_source_examples'] += 1
    if source == 'alignment_jsonl': page['matched_alignment_records'] += 1
    page['_tokens'].update(tokens(obj)); page['_routes'].update(routes(obj)); page['_roles'].update(roles(obj))
    page['matched_v2_row_ids'] = sorted((set(page['matched_v2_row_ids']) | row_ids(obj)))[:64]
    page['matched_source_card_ids'] = sorted((set(page['matched_source_card_ids']) | card_ids(obj)))[:64]
    if len(page['source_examples']) < max_examples:
        page['source_examples'].append({'source': source, 'paper_ids': sorted(collect_ids(obj,8)), 'tokens': tokens(obj)[:8], 'routes': routes(obj)[:8], 'roles': roles(obj)[:8], 'row_ids': sorted(row_ids(obj))[:8], 'card_ids': sorted(card_ids(obj))[:4], 'equation_preview': preview(obj)})

def finalize(pages: dict[str, dict[str, Any]]) -> None:
    for p in pages.values():
        p['tokens'] = dict(p.pop('_tokens').most_common(20)); p['routes'] = dict(p.pop('_routes').most_common(12)); p['constructor_roles'] = dict(p.pop('_roles').most_common(12))
        if p['matched_source_examples'] or p['matched_alignment_records']:
            p['status'] = 'v2_source_grounded'

def render_md(report: Mapping[str, Any]) -> str:
    cov = report.get('coverage') or {}
    lines = ['# MorphWiki Quantum V2 Evidence Index','',f"- Readiness: `{report.get('readiness')}`",f"- V2 root: `{report.get('v2_root')}`",f"- Pages indexed: `{cov.get('pages_total',0)}`",f"- Pages with legacy witnesses: `{cov.get('pages_with_legacy_witnesses',0)}`",f"- Pages with V2 source evidence: `{cov.get('pages_with_v2_source_grounding',0)}`",f"- Pages with V2 row ids: `{cov.get('pages_with_v2_row_ids',0)}`",'', '## Artifacts']
    for k, a in sorted((report.get('artifacts') or {}).items()):
        lines.append(f"- `{k}`: `{a.get('path')}`; readiness `{a.get('readiness')}`")
    h = (report.get('artifacts') or {}).get('hierarchical_language') or {}
    if h.get('language_counts'):
        lines += ['', '## Global Language Counts']
        for k, v in h['language_counts'].items(): lines.append(f"- `{k}`: `{v}`")
    g = ((report.get('artifacts') or {}).get('grammar_rules') or {}).get('recommendation') or {}
    if g:
        lines += ['', '## Grammar Recommendation']
        for k in ['selected_grammar','decision','completion_promotion','three_factor_mdl_gain_over_fiber']:
            if k in g: lines.append(f"- `{k}`: `{g[k]}`")
    lines += ['', '## Page Evidence Examples']
    shown = 0
    for slug, p in sorted((report.get('pages') or {}).items(), key=lambda it: (-int(it[1].get('matched_source_examples',0)), it[0])):
        if p.get('status') != 'v2_source_grounded': continue
        shown += 1; lines.append(f"### {p.get('title')} (`{slug}`)"); lines.append(f"- V2 source examples: `{p.get('matched_source_examples')}`; row ids: `{len(p.get('matched_v2_row_ids') or [])}`")
        for ex in (p.get('source_examples') or [])[:3]: lines.append(f"- {ex.get('equation_preview') or ''}")
        lines.append('')
        if shown >= 10: break
    if not shown:
        lines.append('No page-level V2 source examples were matched. Transfer the source-card alignment JSONL or use pages whose arXiv witnesses overlap the compact source examples.')
    lines += ['', '## Scope', str(report.get('claim_scope') or ''), '']
    return '\n'.join(lines)

def build(args: argparse.Namespace) -> dict[str, Any]:
    root, v2_root = Path(args.root), Path(args.v2_root)
    artifacts = detect(v2_root, {k: getattr(args,k) for k in ['hierarchical_language','symbolic_language','symbolic_full_assignment','grammar_rules','source_language_examples','source_card_alignment','source_card_alignment_jsonl','source_constructor_graph','v2_dag','gamma_bridges','readout_application_coverage','apparatus_basin_a00']})
    meta, id_to_slugs = load_pages(root)
    pages = {s: empty_page(m, args.max_examples_per_page) for s,m in meta.items()}
    if artifacts.get('source_card_alignment_jsonl'):
        for obj in stream_jsonl(Path(artifacts['source_card_alignment_jsonl']), args.max_alignment_rows):
            slugs = set().union(*(id_to_slugs.get(i,set()) for i in collect_ids(obj,16)))
            for slug in slugs: add_match(pages[slug], obj, 'alignment_jsonl', args.max_examples_per_page)
    source = try_json(artifacts.get('source_language_examples'))
    if isinstance(source, Mapping):
        matched = 0
        for obj in example_records(source):
            slugs = set().union(*(id_to_slugs.get(i,set()) for i in collect_ids(obj,16)))
            if not slugs: continue
            matched += 1
            for slug in slugs: add_match(pages[slug], obj, 'source_language_examples', args.max_examples_per_page)
            if args.max_source_example_matches and matched >= args.max_source_example_matches: break
    finalize(pages)
    briefs = {k: brief(v) for k,v in sorted(artifacts.items()) if v.endswith('.json')}
    total = len(pages); with_legacy = sum(1 for p in pages.values() if p['legacy_witness_count']); with_v2 = sum(1 for p in pages.values() if p['status']=='v2_source_grounded'); with_rows = sum(1 for p in pages.values() if p['matched_v2_row_ids'])
    return {'schema_version':1,'report_type':'morphwiki_quantum_v2_evidence_index','readiness':'usable' if briefs and total else 'partial' if briefs else 'blocked','generated_at':datetime.now(timezone.utc).isoformat(),'root':str(root),'v2_root':str(v2_root),'artifacts':briefs,'artifact_paths':artifacts,'coverage':{'pages_total':total,'pages_with_legacy_witnesses':with_legacy,'pages_with_v2_source_grounding':with_v2,'pages_with_v2_row_ids':with_rows,'page_v2_grounding_rate':with_v2/total if total else 0.0,'page_v2_row_rate':with_rows/total if total else 0.0},'pages':pages,'claim_scope':'Evidence adapter from MorphWiki quantum pages to transferred V2 language/source-card artifacts. It supports page-level grounding checks; it is not a public book chapter and not a physical validation result.'}

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', default='discoveries/morphwiki_quantum'); ap.add_argument('--v2-root', default='../tm'); ap.add_argument('--out-json', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index.json'); ap.add_argument('--out-md', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index.md')
    artifact_args = {
        'hierarchical_language': '--hierarchical-language-json',
        'symbolic_language': '--symbolic-language-json',
        'symbolic_full_assignment': '--symbolic-full-assignment-json',
        'grammar_rules': '--grammar-rules-json',
        'source_language_examples': '--source-language-examples-json',
        'source_card_alignment': '--source-card-alignment-json',
        'source_card_alignment_jsonl': '--source-card-alignment-jsonl',
        'source_constructor_graph': '--source-constructor-graph-json',
        'v2_dag': '--v2-dag-json',
        'gamma_bridges': '--gamma-bridges-json',
        'readout_application_coverage': '--readout-application-coverage-json',
        'apparatus_basin_a00': '--apparatus-basin-a00-json',
    }
    for dest, option in artifact_args.items():
        ap.add_argument(option, dest=dest, default='')
    ap.add_argument('--max-alignment-rows', type=int, default=0); ap.add_argument('--max-source-example-matches', type=int, default=0); ap.add_argument('--max-examples-per-page', type=int, default=8)
    args = ap.parse_args(); report = build(args); dump_json(Path(args.out_json), report); Path(args.out_md).parent.mkdir(parents=True, exist_ok=True); Path(args.out_md).write_text(render_md(report), encoding='utf-8')
    print(json.dumps({'json': args.out_json, 'markdown': args.out_md, 'readiness': report['readiness'], 'coverage': report['coverage']}, indent=2, ensure_ascii=False))
if __name__ == '__main__': main()
