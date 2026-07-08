# V2 Operator/Substrate DAG Audit

- Readiness: `usable`
- Rows: `14523959`
- Directed DAG edges: `1118304`
- Lateral/transfer edges excluded from DAG: `5397436`

## Interpretation

- The V2 DAG should be read as a constructor-completion audit, not as the whole V2 typed graph.
- Operator/substrate transfer edges are roads across views; by default they are not causal DAG edges.
- The DAG tests whether typed mechanisms become more complete along selected product-graph roads.
- The terminal layer is a high-completion constructor state, not a subject hierarchy.

## Layer Counts

- Layer 0: `1452315` (0.100)
- Layer 1: `3008721` (0.207)
- Layer 2: `4860461` (0.335)
- Layer 3: `3995724` (0.275)
- Layer 4: `1174186` (0.081)
- Layer 5: `32552` (0.002)

## Edge Orientation

- `operator_knn`: directed `419967`, lateral `580033`, reversed `221977`
- `substrate_knn`: directed `645210`, lateral `354790`, reversed `327501`
- `coupled_operator_substrate`: directed `18`, lateral `265722`, reversed `16`
- `operator_transfer_candidate`: directed `0`, lateral `1000000`, reversed `0`
- `substrate_transfer_candidate`: directed `0`, lateral `1000000`, reversed `0`
- `control_only_candidate`: directed `0`, lateral `0`, reversed `0`
- `within_paper_sequence`: directed `53109`, lateral `196891`, reversed `0`

## Scope

Graph-theoretic audit over V2 evidence features and typed graph edges. Directed edges are monotone constructor-completion candidates, not proof of physical causality.
