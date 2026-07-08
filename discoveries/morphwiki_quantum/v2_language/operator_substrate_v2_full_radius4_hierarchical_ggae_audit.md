# Operator/Substrate Hierarchical GGAE Audit

- Readiness: `usable`
- Rows used: `14523959`
- Edge auxiliary features: `True`

## Latent Neighbourhood Preservation

- `operator_to_z_operator`: mean `0.5829`, median `0.7000`, rows `10000`
- `substrate_to_z_substrate`: mean `0.6666`, median `0.8000`, rows `10000`
- `operator_plus_substrate_to_z_product`: mean `0.5265`, median `0.5000`, rows `10000`

## Hierarchical Edge Decoder

- Level 1 accuracy: `0.9135`
- Level 2 accuracy: `0.8011`
- Level 3 accuracy: `0.5412`
- Mechanism Level 2 accuracy: `0.8120`
- Mechanism Level 3 accuracy: `0.5082`
- Transfer subtype accuracy: `0.4235`
- Transfer-strength MSE: `0.0082`
- Transfer-strength correlation: `0.9241`

## Per Edge Type

- `operator_knn`: n=`8192`, L1=`1.000`, L2=`0.922`, L3=`0.137`, strength_mse=`0.008`
- `substrate_knn`: n=`8192`, L1=`0.988`, L2=`0.865`, L3=`0.795`, strength_mse=`0.013`
- `coupled_operator_substrate`: n=`8192`, L1=`1.000`, L2=`0.999`, L3=`1.000`, strength_mse=`0.000`
- `operator_transfer_candidate`: n=`8192`, L1=`1.000`, L2=`0.941`, L3=`0.803`, strength_mse=`0.008`
- `substrate_transfer_candidate`: n=`8192`, L1=`0.986`, L2=`0.884`, L3=`0.043`, strength_mse=`0.013`
- `within_paper_sequence`: n=`8192`, L1=`0.726`, L2=`0.263`, L3=`0.271`, strength_mse=`0.006`
- `control_only_candidate`: n=`8192`, L1=`0.695`, L2=`0.736`, L3=`0.739`, strength_mse=`0.009`

## Conclusions

- Mechanism/control separation is stable.
- The parent road taxonomy is stable: coupled, operator-near and substrate-near are separable.
- KNN-vs-transfer remains the harder distinction; use Level 2 roads as the primary manuscript claim and Level 3 as a measured subtype.
- The continuous transfer-strength target is learned from operator/substrate mismatch evidence.
- Use this fixed-sample audit, not stochastic epoch validation alone, when comparing hierarchical runs.

## Scope

Fixed-sample audit of a hierarchical two-stream operator/substrate graph autoencoder. It tests parent-road and transfer-subtype separability; it does not prove physical equivalence.
