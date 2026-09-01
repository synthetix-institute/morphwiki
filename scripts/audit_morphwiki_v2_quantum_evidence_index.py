#!/usr/bin/env python3
"""Audit the MorphWiki quantum V2 evidence index."""
from __future__ import annotations
import argparse, json
from collections import Counter
from pathlib import Path
from typing import Any, Mapping

def load_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as f: return json.load(f)
def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(data, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
def tree_slugs(tree: Mapping[str, Any]) -> set[str]:
    out=set()
    for b in (tree.get('branches') or {}).values():
        for p in b.get('pages') or []:
            if p.get('slug'): out.add(str(p['slug']))
    return out
def build(args: argparse.Namespace) -> dict[str, Any]:
    idx=load_json(Path(args.index)); pages=idx.get('pages') or {}; tree=load_json(Path(args.tree)) if args.tree and Path(args.tree).exists() else {}; slugs=tree_slugs(tree) if isinstance(tree, Mapping) else set()
    statuses=Counter(str(p.get('status')) for p in pages.values()); toks=Counter(); roles=Counter(); routes=Counter()
    for p in pages.values(): toks.update(p.get('tokens') or {}); roles.update(p.get('constructor_roles') or {}); routes.update(p.get('routes') or {})
    no_v2=[s for s,p in pages.items() if p.get('status')!='v2_source_grounded']
    grounded=sum(p.get('status')=='v2_source_grounded' for p in pages.values())
    missing_tree=sorted(slugs-set(pages))
    readiness='usable' if pages and grounded and not missing_tree else 'blocked'
    return {'schema_version':1,'report_type':'morphwiki_quantum_v2_evidence_index_audit','readiness':readiness,'index':args.index,'tree':args.tree,'coverage':idx.get('coverage') or {},'status_counts':dict(statuses),'tree_pages_missing_from_index':missing_tree[:50],'pages_without_v2_source_grounding_count':len(no_v2),'pages_without_v2_source_grounding_examples':no_v2[:40],'top_tokens':toks.most_common(30),'top_constructor_roles':roles.most_common(20),'top_routes':routes.most_common(20),'conclusions':['Publish only equation witnesses confirmed by topic-level source-card alignment.','Identifier-linked candidates remain retrieval leads until their local equation context matches the topic.','A zero-grounding index is incomplete and cannot support public source citations.'],'claim_scope':'Audit of the MorphWiki V2 evidence adapter. It measures grounding coverage and token/role support; it does not validate equation derivations.'}
def md(r: Mapping[str, Any]) -> str:
    c=r.get('coverage') or {}; lines=['# MorphWiki Quantum V2 Evidence Index Audit','',f"- Readiness: `{r.get('readiness')}`",f"- Pages total: `{c.get('pages_total',0)}`",f"- Pages with V2 source grounding: `{c.get('pages_with_v2_source_grounding',0)}`",f"- Pages with V2 row ids: `{c.get('pages_with_v2_row_ids',0)}`",'', '## Status Counts']
    for k,v in sorted((r.get('status_counts') or {}).items()): lines.append(f"- `{k}`: `{v}`")
    lines += ['', '## Top Constructor Roles']; lines += [f"- `{k}`: `{v}`" for k,v in r.get('top_constructor_roles') or []]
    lines += ['', '## Top Routes']; lines += [f"- `{k}`: `{v}`" for k,v in r.get('top_routes') or []]
    if r.get('pages_without_v2_source_grounding_examples'):
        lines += ['', '## Pages Still Needing V2 Source Grounding']; lines += [f"- `{s}`" for s in r['pages_without_v2_source_grounding_examples'][:30]]
    lines += ['', '## Conclusions']; lines += [f"- {x}" for x in r.get('conclusions') or []]; lines += ['', '## Scope', str(r.get('claim_scope') or ''), '']
    return '\n'.join(lines)
def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--index', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index.json'); ap.add_argument('--tree', default='discoveries/morphwiki_quantum/quantum_mechanism_tree.json'); ap.add_argument('--out-json', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index_audit.json'); ap.add_argument('--out-md', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index_audit.md'); args=ap.parse_args(); r=build(args); dump_json(Path(args.out_json), r); Path(args.out_md).parent.mkdir(parents=True, exist_ok=True); Path(args.out_md).write_text(md(r), encoding='utf-8'); print(json.dumps({'json':args.out_json,'markdown':args.out_md,'readiness':r['readiness']}, indent=2))
if __name__ == '__main__': main()
