#!/usr/bin/env python3
"""Join quantum topics to source equations through exact V2.1 card alignments.

Topic and relation terms are resolved in the local source context before a
paper is cited. Legacy identifiers remain retrieval leads and cannot establish
source support by themselves.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Iterable

ARXIV_RE = re.compile(r"(?:arxiv:\s*)?(?:(?P<old>[a-z][a-z-]+/[0-9]{7})|(?P<oldflat>[a-z][a-z-]+[0-9]{7})|(?P<new>[0-9]{4}\.[0-9]{4,5}))(?:v[0-9]+)?", re.I)
TOKEN_RE = re.compile(r"(?:Ω|Ξ|Λ|T|Τ|Γ|J|Π)[0-9]{2,3}|(?:A\*?|Α)[0-9]{2}")
ROLES = {"operator_apparatus","real_substrate_geometry","selector","selector_context","closure_constraints","readout_current","protocol_order"}
ROUTES = {"transport_flow","spectral_operator","boundary_weak_form","constraint_closure","discrete_protocol","commutator_incompatibility","unclassified"}
TOPIC_STOP = {
    'quantum', 'theory', 'physics', 'physical', 'mechanics', 'mathematical',
    'formulation', 'introduction', 'applications', 'modern', 'system',
}

CORE_RELATION_CUES = {
    'fermion': ('antisymmetr', 'anticommut', 'pauli', 'fermi-dirac', 'fermi dirac'),
    'gauge_theory': ('covariant derivative', 'field strength', 'gauge potential', 'connection', 'curvature'),
    'quantum_decoherence': ('decoher', 'lindblad', 'master equation', 'reduced density', 'environment'),
    'commutator': ('commutator', 'noncommut', 'lie bracket'),
    'quantum_entanglement': ('entangl', 'schmidt', 'partial trace', 'bell inequality'),
    'renormalization': ('renormalization group', 'beta function', 'running coupling', 'fixed point', 'coarse grain'),
}

CORE_TOPIC_ALIASES = {
    'fermion': ('fermionic',),
    'gauge_theory': ('gauge field', 'gauge symmetry'),
    'quantum_decoherence': ('decoherence', 'decoherent'),
    'commutator': ('commutation relation', 'noncommuting operators'),
    'quantum_entanglement': ('entanglement', 'entangled state'),
    'renormalization': ('renormalisation', 'renormalization group'),
}


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
        'source_cards_jsonl': ['source_equation_cards*full*.jsonl', 'source_equation_cards*.jsonl'],
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
                elif k in {'source_card_alignment', 'source_card_alignment_jsonl'}:
                    def alignment_rank(path: Path) -> tuple[int, int, int, str]:
                        name = path.name.lower()
                        companion = path.with_suffix('.json') if path.suffix == '.jsonl' else path
                        complete = companion.exists() and companion.stat().st_size > 0
                        return (
                            0 if complete else 1,
                            0 if 'v21' in name else 1,
                            0 if 'full' in name else 1,
                            name,
                        )
                    chosen = sorted(found, key=alignment_rank)[0]
                else:
                    # Prefer the corrected V2.1/full-corpus artifact.  File
                    # size is not a quality criterion: the previous rule
                    # systematically selected small pilot outputs.
                    chosen = sorted(
                        found,
                        key=lambda x: (
                            0 if 'v21' in x.name.lower() else 1,
                            0 if 'full' in x.name.lower() else 1,
                            x.name,
                        ),
                    )[0]
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
        terms = {
            token
            for token in re.findall(r'[a-z][a-z0-9-]{2,}', f"{slug.replace('_',' ')} {title.lower()}")
            if token not in TOPIC_STOP
        }
        pages[slug] = {'slug': slug, 'title': title, 'path': str(p), 'legacy_witness_count': len(witnesses), 'legacy_arxiv_ids': sorted(ids), 'topic_terms': sorted(terms)}
        for i in ids:
            id_to_slugs[i].add(slug)
    return pages, id_to_slugs


def normalized_words(value: Any) -> str:
    text = unicodedata.normalize('NFKD', str(value or ''))
    text = ''.join(char for char in text if not unicodedata.combining(char))
    text = text.lower().replace('_', ' ').replace('-', ' ')
    return re.sub(r'[^a-z0-9]+', ' ', text).strip()


def topic_phrases(slug: str, meta: Mapping[str, Any]) -> tuple[str, ...]:
    title = normalized_words(meta.get('title'))
    title_without_parenthesis = normalized_words(
        re.sub(r'\([^)]*\)', ' ', str(meta.get('title') or ''))
    )
    slug_phrase = normalized_words(slug)
    phrases = {value for value in (title, title_without_parenthesis, slug_phrase) if value}
    phrases.update(normalized_words(value) for value in CORE_TOPIC_ALIASES.get(slug, ()))
    return tuple(sorted(phrases, key=lambda value: (-len(value.split()), value)))


def tree_page_branches(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    tree = load_json(path)
    return {
        str(row.get('slug')): str(branch_id)
        for branch_id, branch in (tree.get('branches') or {}).items()
        for row in (branch.get('pages') or [])
        if row.get('slug')
    }


def source_first_topic_candidates(
    pages: Mapping[str, Mapping[str, Any]],
    branches: Mapping[str, str],
    path: Path,
    max_per_page: int,
    aligned_card_ids: set[str] | None = None,
) -> tuple[dict[str, list[tuple[str, dict[str, Any]]]], dict[str, Any]]:
    """Find topic-bearing equation cards before consulting legacy citations."""
    queries: dict[str, tuple[str, ...]] = {}
    anchor_to_slugs: dict[str, set[str]] = defaultdict(set)
    for slug, meta in pages.items():
        if branches.get(slug) == 'annotations':
            continue
        phrases = topic_phrases(slug, meta)
        if not phrases:
            continue
        queries[slug] = phrases
        for phrase in phrases:
            words = phrase.split()
            preferred = [word for word in words if word not in TOPIC_STOP]
            anchor = max(preferred or words, key=len)
            anchor_to_slugs[anchor].add(slug)

    selected: dict[str, list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    per_page: Counter[str] = Counter()
    papers_per_page: dict[str, set[str]] = defaultdict(set)
    cards_seen = 0
    eligible_cards = 0
    for card in stream_jsonl(path, 0):
        cards_seen += 1
        if cards_seen % 1_000_000 == 0:
            print(
                json.dumps(
                    {
                        'event': 'morphwiki_source_first_scan',
                        'cards_seen': cards_seen,
                        'pages_with_candidates': sum(
                            value > 0 for value in per_page.values()
                        ),
                        'candidate_cards': len(selected),
                    }
                ),
                flush=True,
            )
        card_id = str(card.get('equation_card_id') or card.get('card_id') or '')
        if aligned_card_ids is not None and card_id not in aligned_card_ids:
            continue
        equation = str(card.get('canonical_equation') or card.get('raw_equation') or '')
        quality = set(card.get('quality_flags') or [])
        if (
            not card_id
            or not equation.strip()
            or card.get('clean_endpoint') is False
            or ('has_relation' not in quality and quality)
        ):
            continue
        eligible_cards += 1
        section = card.get('section') or {}
        local_context = ' '.join(
            str(value or '')
            for value in (
                section.get('title') if isinstance(section, Mapping) else '',
                card.get('context_before'),
                equation,
                card.get('context_after'),
            )
        )
        normalized = normalized_words(local_context)
        words = set(normalized.split())
        paper_id = str(
            card.get('source_id')
            or card.get('paper_id')
            or card.get('arxiv_id')
            or ''
        )
        candidate_slugs = set().union(
            *(anchor_to_slugs.get(word, set()) for word in words)
        )
        for slug in candidate_slugs:
            if per_page[slug] >= max_per_page:
                continue
            if paper_id and paper_id in papers_per_page[slug]:
                continue
            phrase_hits = [phrase for phrase in queries[slug] if phrase in normalized]
            if not phrase_hits:
                continue
            cue_hits = [
                cue
                for cue in CORE_RELATION_CUES.get(slug, ())
                if normalized_words(cue) in normalized
            ]
            if slug in CORE_RELATION_CUES and not cue_hits:
                continue
            record = {
                'equation_card_id': card_id,
                'source_id': paper_id,
                'paper_id': paper_id,
                'equation_preview': re.sub(r'\s+', ' ', equation).strip()[:520],
                'section_title': section.get('title') if isinstance(section, Mapping) else '',
                'local_context': re.sub(r'\s+', ' ', local_context).strip()[:1600],
                'topic_terms_matched': sorted(phrase_hits),
                'relation_terms_matched': sorted(cue_hits),
                'topic_relevance': 'local_context_match',
                'relation_relevance': (
                    'relation_context_match' if cue_hits else 'topic_equation_match'
                ),
            }
            selected[card_id].append((slug, record))
            per_page[slug] += 1
            if paper_id:
                papers_per_page[slug].add(paper_id)
    return dict(selected), {
        'cards_seen': cards_seen,
        'eligible_cards': eligible_cards,
        'candidate_cards': len(selected),
        'aligned_card_pool': len(aligned_card_ids or ()),
        'pages_with_candidates': sum(value > 0 for value in per_page.values()),
        'candidate_counts_by_page': dict(sorted(per_page.items())),
        'candidate_paper_counts_by_page': {
            slug: len(papers) for slug, papers in sorted(papers_per_page.items())
        },
    }


def align_source_first_candidates(
    pages: dict[str, dict[str, Any]],
    candidates: Mapping[str, list[tuple[str, dict[str, Any]]]],
    path: Path,
    max_examples: int,
) -> dict[str, int]:
    matched_cards: set[str] = set()
    links_seen = 0
    matches = 0
    for alignment in stream_jsonl(path, 0):
        links_seen += 1
        if links_seen % 500_000 == 0:
            print(
                json.dumps(
                    {
                        'event': 'morphwiki_source_first_alignment',
                        'links_seen': links_seen,
                        'matched_candidate_cards': len(matched_cards),
                        'page_card_alignment_matches': matches,
                    }
                ),
                flush=True,
            )
        card_id = str(
            alignment.get('equation_card_id')
            or alignment.get('source_card_id')
            or alignment.get('card_id')
            or ''
        )
        if card_id not in candidates:
            continue
        for slug, card in candidates[card_id]:
            merged = dict(alignment)
            merged.update(card)
            add_match(pages[slug], merged, 'source_first_alignment', max_examples)
            matches += 1
        matched_cards.add(card_id)
    return {
        'alignment_links_seen': links_seen,
        'matched_candidate_cards': len(matched_cards),
        'page_card_alignment_matches': matches,
    }

def empty_page(meta: Mapping[str, Any], max_examples: int) -> dict[str, Any]:
    return {'title': meta.get('title'), 'topic_terms': meta.get('topic_terms',[]), 'legacy_witness_count': meta.get('legacy_witness_count',0), 'legacy_arxiv_ids': meta.get('legacy_arxiv_ids',[]), 'status': 'legacy_witness_only' if meta.get('legacy_witness_count') else 'no_evidence', 'matched_alignment_records': 0, 'matched_source_examples': 0, 'topic_relevant_source_examples': 0, 'matched_v2_row_ids': [], 'matched_source_card_ids': [], 'tokens': {}, 'routes': {}, 'constructor_roles': {}, 'source_examples': [], 'max_examples': max_examples, '_tokens': Counter(), '_routes': Counter(), '_roles': Counter()}

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
    if source in {'source_language_examples', 'source_first_alignment'}:
        page['matched_source_examples'] += 1
    if source == 'alignment_jsonl': page['matched_alignment_records'] += 1
    page['_tokens'].update(tokens(obj)); page['_routes'].update(routes(obj)); page['_roles'].update(roles(obj))
    page['matched_v2_row_ids'] = sorted((set(page['matched_v2_row_ids']) | row_ids(obj)))[:64]
    page['matched_source_card_ids'] = sorted((set(page['matched_source_card_ids']) | card_ids(obj)))[:64]
    example = {
            'source': source,
            'paper_ids': sorted(collect_ids(obj,8)),
            'tokens': tokens(obj)[:8],
            'routes': routes(obj)[:8],
            'roles': roles(obj)[:8],
            'row_ids': sorted(row_ids(obj))[:8],
            'card_ids': sorted(card_ids(obj))[:4],
            'equation_preview': preview(obj),
            'section_title': obj.get('section_title') or '',
            'local_context': obj.get('local_context') or '',
            'topic_terms_matched': obj.get('topic_terms_matched') or [],
            'relation_terms_matched': obj.get('relation_terms_matched') or [],
            'topic_relevance': obj.get('topic_relevance') or 'not_established',
            'relation_relevance': obj.get('relation_relevance') or 'not_established',
        }
    if source == 'source_first_alignment':
        page['source_examples'].insert(0, example)
        page['source_examples'] = page['source_examples'][:max_examples]
    elif len(page['source_examples']) < max_examples:
        page['source_examples'].append(example)


def enrich_with_source_cards(pages: dict[str, dict[str, Any]], path: Path) -> dict[str, int]:
    """Attach local source context to the small set of displayed examples."""
    waiting: dict[str, list[tuple[dict[str, Any], dict[str, Any]]]] = defaultdict(list)
    for page in pages.values():
        for example in page.get('source_examples') or []:
            for card_id in example.get('card_ids') or []:
                waiting[str(card_id)].append((page, example))
    if not waiting:
        return {'requested_cards': 0, 'matched_cards': 0}

    matched = set()
    for card in stream_jsonl(path, 0):
        card_id = str(card.get('equation_card_id') or card.get('card_id') or '')
        if card_id not in waiting:
            continue
        section = card.get('section') or {}
        local_text = ' '.join(
            str(value or '')
            for value in (
                section.get('title') if isinstance(section, Mapping) else '',
                card.get('context_before'),
                card.get('canonical_equation') or card.get('equation'),
                card.get('context_after'),
            )
        )
        local_text = re.sub(r'\s+', ' ', local_text).strip()
        lower = local_text.lower()
        for page, example in waiting[card_id]:
            terms = [str(term).lower() for term in page.get('topic_terms') or []]
            hits = sorted({term for term in terms if term and term in lower})
            example['section_title'] = section.get('title') if isinstance(section, Mapping) else ''
            example['local_context'] = local_text[:1200]
            example['equation_preview'] = re.sub(
                r'\s+', ' ', str(card.get('canonical_equation') or card.get('equation') or '')
            ).strip()[:520]
            example['topic_terms_matched'] = hits
            example['topic_relevance'] = 'local_context_match' if hits else 'not_established'
        matched.add(card_id)
        if len(matched) == len(waiting):
            break
    return {'requested_cards': len(waiting), 'matched_cards': len(matched)}


def finalize(pages: dict[str, dict[str, Any]]) -> None:
    for p in pages.values():
        p['tokens'] = dict(p.pop('_tokens').most_common(20)); p['routes'] = dict(p.pop('_routes').most_common(12)); p['constructor_roles'] = dict(p.pop('_roles').most_common(12))
        relevant = sum(
            1
            for example in p.get('source_examples') or []
            if example.get('topic_relevance') == 'local_context_match'
        )
        p['topic_relevant_source_examples'] = relevant
        if relevant:
            p['status'] = 'v2_source_grounded'
        elif p['matched_source_examples'] or p['matched_alignment_records']:
            p['status'] = 'v2_identifier_linked'

def render_md(report: Mapping[str, Any]) -> str:
    cov = report.get('coverage') or {}
    lines = ['# MorphWiki Quantum V2 Evidence Index','',f"- Readiness: `{report.get('readiness')}`",f"- V2 root: `{report.get('v2_root')}`",f"- Pages indexed: `{cov.get('pages_total',0)}`",f"- Pages with legacy witnesses: `{cov.get('pages_with_legacy_witnesses',0)}`",f"- Pages with identifier-linked V2 candidates: `{cov.get('pages_with_v2_identifier_links',0)}`",f"- Pages with topic-relevant V2 source evidence: `{cov.get('pages_with_v2_source_grounding',0)}`",f"- Pages with V2 row ids: `{cov.get('pages_with_v2_row_ids',0)}`",'', '## Artifacts']
    for k, a in sorted((report.get('artifacts') or {}).items()):
        lines.append(f"- `{k}`: `{a.get('path')}`; readiness `{a.get('readiness')}`")
    scan = report.get('source_first_scan') or {}
    alignment = report.get('source_first_alignment') or {}
    lines += [
        '',
        '## Source-first matching',
        f"- Source cards scanned: `{scan.get('cards_seen', 0)}`",
        f"- Pages with topic-bearing equation candidates: `{scan.get('pages_with_candidates', 0)}`",
        f"- Candidate cards joined to V2 rows: `{alignment.get('matched_candidate_cards', 0)}`",
    ]
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
    artifacts = detect(v2_root, {k: getattr(args,k) for k in ['hierarchical_language','symbolic_language','symbolic_full_assignment','grammar_rules','source_language_examples','source_card_alignment','source_card_alignment_jsonl','source_cards_jsonl','source_constructor_graph','v2_dag','gamma_bridges','readout_application_coverage','apparatus_basin_a00']})
    meta, id_to_slugs = load_pages(root)
    branches = tree_page_branches(Path(args.tree_json)) if args.tree_json else {}
    if branches:
        meta = {slug: page for slug, page in meta.items() if slug in branches}
        id_to_slugs = defaultdict(set)
        for slug, page in meta.items():
            for identifier in page.get('legacy_arxiv_ids') or []:
                id_to_slugs[str(identifier)].add(slug)
    pages = {s: empty_page(m, args.max_examples_per_page) for s,m in meta.items()}
    aligned_card_ids: set[str] = set()
    if artifacts.get('source_card_alignment_jsonl'):
        for obj in stream_jsonl(Path(artifacts['source_card_alignment_jsonl']), args.max_alignment_rows):
            aligned_card_ids.update(card_ids(obj))
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
    source_card_enrichment = {'requested_cards': 0, 'matched_cards': 0}
    source_first_scan = {'cards_seen': 0, 'candidate_cards': 0, 'pages_with_candidates': 0}
    source_first_alignment = {'alignment_links_seen': 0, 'matched_candidate_cards': 0, 'page_card_alignment_matches': 0}
    if artifacts.get('source_cards_jsonl'):
        candidates, source_first_scan = source_first_topic_candidates(
            meta,
            branches,
            Path(artifacts['source_cards_jsonl']),
            args.max_topic_cards_per_page,
            aligned_card_ids,
        )
        if candidates and artifacts.get('source_card_alignment_jsonl'):
            source_first_alignment = align_source_first_candidates(
                pages,
                candidates,
                Path(artifacts['source_card_alignment_jsonl']),
                args.max_examples_per_page,
            )
        elif not candidates:
            source_card_enrichment = enrich_with_source_cards(
                pages, Path(artifacts['source_cards_jsonl'])
            )
    finalize(pages)
    briefs = {k: brief(v) for k,v in sorted(artifacts.items()) if v.endswith('.json')}
    total = len(pages); with_legacy = sum(1 for p in pages.values() if p['legacy_witness_count']); with_v2 = sum(1 for p in pages.values() if p['status']=='v2_source_grounded'); with_links = sum(1 for p in pages.values() if p['status'] in {'v2_source_grounded','v2_identifier_linked'}); with_rows = sum(1 for p in pages.values() if p['matched_v2_row_ids'])
    return {'schema_version':3,'report_type':'morphwiki_quantum_v2_evidence_index','readiness':'usable' if briefs and total else 'partial' if briefs else 'blocked','generated_at':datetime.now(timezone.utc).isoformat(),'root':str(root),'v2_root':str(v2_root),'artifacts':briefs,'artifact_paths':artifacts,'source_card_enrichment':source_card_enrichment,'source_first_scan':source_first_scan,'source_first_alignment':source_first_alignment,'coverage':{'pages_total':total,'pages_with_legacy_witnesses':with_legacy,'pages_with_v2_identifier_links':with_links,'pages_with_v2_source_grounding':with_v2,'pages_with_v2_row_ids':with_rows,'page_v2_identifier_link_rate':with_links/total if total else 0.0,'page_v2_grounding_rate':with_v2/total if total else 0.0,'page_v2_row_rate':with_rows/total if total else 0.0},'pages':pages,'claim_scope':'Equation evidence is selected from topic-bearing local source context and then joined to an exact V2 source-card alignment. Legacy identifiers are retained only as retrieval leads.'}

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', default='discoveries/morphwiki_quantum'); ap.add_argument('--v2-root', default='../tm'); ap.add_argument('--out-json', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index.json'); ap.add_argument('--out-md', default='discoveries/morphwiki_quantum/v2_quantum_evidence_index.md')
    ap.add_argument('--tree-json', default='discoveries/morphwiki_quantum/quantum_mechanism_tree.json')
    artifact_args = {
        'hierarchical_language': '--hierarchical-language-json',
        'symbolic_language': '--symbolic-language-json',
        'symbolic_full_assignment': '--symbolic-full-assignment-json',
        'grammar_rules': '--grammar-rules-json',
        'source_language_examples': '--source-language-examples-json',
        'source_card_alignment': '--source-card-alignment-json',
        'source_card_alignment_jsonl': '--source-card-alignment-jsonl',
        'source_cards_jsonl': '--source-cards-jsonl',
        'source_constructor_graph': '--source-constructor-graph-json',
        'v2_dag': '--v2-dag-json',
        'gamma_bridges': '--gamma-bridges-json',
        'readout_application_coverage': '--readout-application-coverage-json',
        'apparatus_basin_a00': '--apparatus-basin-a00-json',
    }
    for dest, option in artifact_args.items():
        ap.add_argument(option, dest=dest, default='')
    ap.add_argument('--max-alignment-rows', type=int, default=0); ap.add_argument('--max-source-example-matches', type=int, default=0); ap.add_argument('--max-examples-per-page', type=int, default=8)
    ap.add_argument('--max-topic-cards-per-page', type=int, default=32)
    args = ap.parse_args(); report = build(args); dump_json(Path(args.out_json), report); Path(args.out_md).parent.mkdir(parents=True, exist_ok=True); Path(args.out_md).write_text(render_md(report), encoding='utf-8')
    print(json.dumps({'json': args.out_json, 'markdown': args.out_md, 'readiness': report['readiness'], 'coverage': report['coverage']}, indent=2, ensure_ascii=False))
if __name__ == '__main__': main()
