# V2 Grammar-Rule Learner

- Readiness: `usable`
- Active manifest: `discoveries/operator_substrate_v2_full_active_matrices_manifest.json`
- Edge NPZ: `discoveries/operator_substrate_v2_full_typed_graph_edges.npz`
- Rows sampled: `100000`

## Recommendation

- Selected grammar: `identity_with_completion_fiber`
- Decision: Two primitive spaces with C/R/P as an attached completion fiber.
- C/R/P promotion: `retain_completion_as_attached_fiber`

## Candidate Scores

- `identity_with_completion_fiber`: mdl=`0.308927`, edge_fit=`0.9037`, rank_fraction=`0.8172`, overlap=`0.1493`, completion_signal=`0.9299`
- `identity_multi_fiber`: mdl=`0.333565`, edge_fit=`0.9037`, rank_fraction=`0.8720`, overlap=`0.1493`, completion_signal=`0.9299`
- `three_factor_completion`: mdl=`0.399847`, edge_fit=`0.9037`, rank_fraction=`1.0005`, overlap=`0.1831`, completion_signal=`0.9299`
- `current_two_factor`: mdl=`0.522063`, edge_fit=`0.9067`, rank_fraction=`1.0000`, overlap=`0.1203`, completion_signal=`0.9299`
- `maximal_role_split`: mdl=`0.612744`, edge_fit=`0.9037`, rank_fraction=`1.0601`, overlap=`0.3694`, completion_signal=`0.9299`
- `control_as_primitive_negative_control`: mdl=`0.658022`, edge_fit=`0.9037`, rank_fraction=`1.1792`, overlap=`0.0941`, completion_signal=`0.9299`

## Block Statistics

- `operator_core`: dims=`44`, effective_rank=`18.1591`, zero_rows=`0.2367`, mean_l2=`0.9539`
- `operator_apparatus`: dims=`16`, effective_rank=`8.1237`, zero_rows=`0.4797`, mean_l2=`0.5203`
- `closure_constraints`: dims=`10`, effective_rank=`4.4531`, zero_rows=`0.6931`, mean_l2=`0.3070`
- `readout_current`: dims=`10`, effective_rank=`4.4324`, zero_rows=`0.6080`, mean_l2=`0.3920`
- `protocol_order`: dims=`8`, effective_rank=`3.2715`, zero_rows=`0.9742`, mean_l2=`0.0258`
- `completion_core`: dims=`28`, effective_rank=`10.0535`, zero_rows=`0.4169`, mean_l2=`0.6414`
- `substrate_core`: dims=`28`, effective_rank=`17.4924`, zero_rows=`0.2142`, mean_l2=`0.9682`
- `real_substrate_geometry`: dims=`16`, effective_rank=`9.8983`, zero_rows=`0.3281`, mean_l2=`0.6719`
- `selector_context`: dims=`12`, effective_rank=`7.6158`, zero_rows=`0.4458`, mean_l2=`0.5542`
- `operator_plus_substrate`: dims=`72`, effective_rank=`35.6515`, zero_rows=`0.1014`, mean_l2=`1.4529`
- `control`: dims=`23`, effective_rank=`6.3718`, zero_rows=`0.0000`, mean_l2=`2.0702`
- `equation_shape`: dims=`15`, effective_rank=`9.2529`, zero_rows=`0.0000`, mean_l2=`1.0000`
- `quality`: dims=`8`, effective_rank=`1.4836`, zero_rows=`0.0000`, mean_l2=`1.8119`

## Edge Diagnostics

- `operator_knn`: n=`50000`, op/sub current=`1.0000`, op/sub split=`1.0000`
- `substrate_knn`: n=`50000`, op/sub current=`1.0000`, op/sub split=`1.0000`
- `coupled_operator_substrate`: n=`50000`, op/sub current=`0.9403`, op/sub split=`0.9223`
- `operator_transfer_candidate`: n=`50000`, op/sub current=`1.0000`, op/sub split=`1.0000`
- `substrate_transfer_candidate`: n=`50000`, op/sub current=`1.0000`, op/sub split=`1.0000`
- `control_only_candidate`: n=`50000`, op/sub current=`0.5000`, op/sub split=`0.5000`
- `within_paper_sequence`: n=`50000`, op/sub current=`0.5000`, op/sub split=`0.5000`

## Interpretation

- The learner compares logical grammar structures using measured V2 matrices and typed edges; it does not rename tokens or retrain the language.
- A lower MDL score means a candidate preserves edge evidence with less redundant primitive structure.
- Closure/readout/protocol should remain an attached completion fiber unless a future run shows enough independent topology and MDL gain to promote it.

## Scope

Grammar-rule learner over deterministic V2 evidence matrices and typed edges. It selects a compact logical factorization for the language; it does not prove physical equivalence and does not replace source-card or decoder validation.
