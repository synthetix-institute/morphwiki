# Quantum Book Content Preservation Audit

- Readiness: `usable`
- Topics in the mechanism map: `146`
- Dedicated topic sections: `146`
- Topic words: `57048`
- Topic-specific physical treatments: `62`
- Branch-level topic maps: `67`
- Topic-word retention: `0.897`
- Equation blocks: `158`
- TeX topics with displayed equations: `123`
- PDF pages: `292`
- PDF-page retention: `0.939`
- Source-grounded topics: `6`
- Original-paper topics (separate from corpus alignment): `15`
- Original-paper display records: `16`
- Identifier-linked candidates: `135`

## Checks

- `topic_count`: **passed**
- `all_topics_mapped_in_tex`: **passed**
- `all_topics_have_dedicated_sections`: **passed**
- `all_derivation_pages_present`: **passed**
- `derivation_manifest_matches_tree`: **passed**
- `topic_specific_depth`: **passed**
- `all_physics_topics_have_equations`: **passed**
- `all_physics_topics_have_equations_in_tex`: **passed**
- `canonical_arxiv_links`: **passed**
- `original_display_links_preserved`: **passed**
- `original_source_coverage`: **passed**
- `mechanisms_before_roles_and_closure`: **passed**
- `no_unsupported_grounding_status`: **passed**
- `topic_words`: **passed**
- `topic_word_retention`: **passed**
- `equation_blocks`: **passed**
- `equation_block_retention`: **passed**
- `pdf_pages`: **passed**
- `pdf_page_retention`: **passed**
- `source_equations_only_when_grounded`: **passed**
- `source_grounding`: **passed**
- `source_summary_consistent`: **passed**
- `no_wikipedia_scaffold`: **passed**
- `no_unverified_topic_page_links`: **passed**
- `no_internal_pipeline_language`: **passed**

## Scope
Build-integrity audit. It requires equation-bearing content for physical topics while keeping historical and interpretive entries free of invented equations; it does not validate the physics of individual pages.

incomplete: topic-specific treatments and physical-role overviews remain distinct; build checks are not physics verification
