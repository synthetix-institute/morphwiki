# Operator/Substrate Two-Stream GGAE Audit

- Readiness: `usable`
- Rows used: `14523959`
- Checkpoint: `results/operator_substrate_v2_full_radius4_twostream_ggae/operator_substrate_twostream_ggae.pt`

## Latent Neighbourhood Preservation

- `operator_to_z_operator`: mean overlap `0.5791`, median `0.7000`, rows `10000`
- `substrate_to_z_substrate`: mean overlap `0.6390`, median `0.8000`, rows `10000`
- `operator_plus_substrate_to_z_product`: mean overlap `0.5698`, median `0.6000`, rows `10000`

## Edge Decoder

- Mean positive edge accuracy: `0.5332`
- Mean transfer edge accuracy: `0.7071`

## Edge-Type Confusion

- `operator_knn`: n=`8192`, acc=`0.2654`, target_prob=`0.4242`, predictions: operator_transfer_candidate=5629; operator_knn=2174; within_paper_sequence=172; no_edge_or_control=113
- `substrate_knn`: n=`8192`, acc=`0.3291`, target_prob=`0.4911`, predictions: substrate_transfer_candidate=5427; substrate_knn=2696; coupled_operator_substrate=59; within_paper_sequence=5
- `coupled_operator_substrate`: n=`8192`, acc=`0.8159`, target_prob=`0.7630`, predictions: coupled_operator_substrate=6684; substrate_knn=521; operator_knn=445; operator_transfer_candidate=235
- `operator_transfer_candidate`: n=`8192`, acc=`0.7402`, target_prob=`0.5553`, predictions: operator_transfer_candidate=6064; operator_knn=1849; within_paper_sequence=136; no_edge_or_control=105
- `substrate_transfer_candidate`: n=`8192`, acc=`0.6740`, target_prob=`0.5049`, predictions: substrate_transfer_candidate=5521; substrate_knn=2657; within_paper_sequence=7; coupled_operator_substrate=7
- `within_paper_sequence`: n=`8192`, acc=`0.3749`, target_prob=`0.4075`, predictions: no_edge_or_control=4724; within_paper_sequence=3071; operator_transfer_candidate=115; operator_knn=93
- `control_only_candidate`: n=`8192`, acc=`0.9352`, target_prob=`0.8470`, predictions: no_edge_or_control=7661; within_paper_sequence=435; operator_transfer_candidate=31; substrate_knn=26

## Conclusions

- The operator latent preserves nontrivial local operator neighbourhood structure.
- The substrate latent preserves nontrivial local substrate neighbourhood structure.
- The edge decoder separates positive mechanism edge classes above a trivial-collapse regime.
- Transfer edge classes are partially separable and should be retained as typed roads.
- Control-only edges are mostly recognized as non-mechanism/control edges.
- Use these diagnostics as the acceptance gate before scaling the two-stream GGAE beyond the 100k V2 sample.

## Scope

Audit of a bounded two-stream operator/substrate graph autoencoder. It tests latent neighbourhood preservation and typed edge separability; it does not prove physical equivalence.
