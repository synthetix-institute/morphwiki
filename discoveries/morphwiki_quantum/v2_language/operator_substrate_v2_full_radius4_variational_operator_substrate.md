# Variational Operator/Substrate Audit

- Readiness: `usable`
- Rows: `14523959`
- Edge sample per type: `100000`
- Global action mean: `1.49832`
- Global action sum: `1.04882e+06`

## Action Definition

- Discrete Lagrangian: `L_ij=sum_b w_b ||q_b(j)-q_b(i)||_2^2`
- Connection: `flat identity connection on V2 block coordinates; no road labels enter the action`

## Block Action Fractions

- `real_substrate_geometry`: `0.2424`
- `selector`: `0.2321`
- `operator_apparatus`: `0.2300`
- `closure_constraints`: `0.1441`
- `readout_current`: `0.1362`
- `protocol_order`: `0.0152`

## Noether Generators

- `coupled_operator_substrate`: relative_delta=`0.000948342`, div_l1/action=`0.000957218`, near_symmetry=`True`
- `within_paper_sequence`: relative_delta=`0.290971`, div_l1/action=`0.291764`, near_symmetry=`False`
- `operator_transfer_candidate`: relative_delta=`0.409993`, div_l1/action=`0.410058`, near_symmetry=`False`
- `operator_knn`: relative_delta=`0.432747`, div_l1/action=`0.432835`, near_symmetry=`False`
- `substrate_knn`: relative_delta=`0.559701`, div_l1/action=`0.559735`, near_symmetry=`False`
- `substrate_transfer_candidate`: relative_delta=`0.563686`, div_l1/action=`0.56373`, near_symmetry=`False`

## Edge-Type Action

- `operator_knn`: n=`100000`, mean_L=`1.45949`, sum_L=`145949`
- `substrate_knn`: n=`100000`, mean_L=`1.62216`, sum_L=`162216`
- `coupled_operator_substrate`: n=`100000`, mean_L=`0.00436066`, sum_L=`436.066`
- `operator_transfer_candidate`: n=`100000`, mean_L=`1.5322`, sum_L=`153220`
- `substrate_transfer_candidate`: n=`100000`, mean_L=`1.62944`, sum_L=`162944`
- `within_paper_sequence`: n=`100000`, mean_L=`1.24034`, sum_L=`124034`
- `control_only_candidate`: n=`100000`, mean_L=`3.00023`, sum_L=`300023`
- `sequential_fallback`: n=`0`, mean_L=`0`, sum_L=`0`

## Conclusions

- The Lagrangian is now an explicit quadratic action on typed operator/substrate fields, not a road-label proxy.
- Discrete Noether-current candidates are computed as exact first variations of that action under learned infinitesimal generator fields.
- A conserved current candidate is a generator with small relative first variation and small node-divergence residual, not merely high latent similarity.
- Control/equation-shape channels have zero default action weight and therefore cannot create mechanism currents unless explicitly enabled.

## Scope

Exact discrete variational calculation for the V2 finite-dimensional representation. It is close in form to physical Noether calculus because it uses an action, infinitesimal generator and first variation. It is not a symbolic proof of a continuum physical conservation law unless the source equation action and transformation group are supplied.
