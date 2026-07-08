# V2 Readout/Application Coverage Audit

- Readiness: `usable`
- Active manifest: `discoveries/operator_substrate_v2_full_active_matrices_manifest.json`
- Source cards: `discoveries/source_equation_cards_full.jsonl`

## Matrix Evidence

- Matrix readiness: `usable`
- `operator_apparatus`: active_dims=`16`, nonzero_row_rate=`0.52133`, mean_energy=`0.5213299989700317`
- `closure_constraints`: active_dims=`10`, nonzero_row_rate=`0.30551`, mean_energy=`0.305510014295578`
- `readout_current`: active_dims=`10`, nonzero_row_rate=`0.395155`, mean_energy=`0.39515501260757446`
- `protocol_order`: active_dims=`8`, nonzero_row_rate=`0.02682`, mean_energy=`0.026820000261068344`

## Source-Card Evidence

- Card readiness: `usable`
- Cards scanned: `500000`
- Readout role rate: `0.25733`
- Protocol role rate: `0.071022`
- Application context counts: `{'biology_application': 145995, 'measurement_application': 80671, 'material_application': 32149, 'chemistry_application': 11615}`

## Conclusion

- Readout and protocol channels are present in the active operator-core matrix; they were not pruned away.
- Application-like readout labels are sparse; application/realization should not be treated as well learned without source-card or knowledge-graph support.
- Source cards can provide the missing human-readable realization/readout context above the V2 endpoint fingerprints.

## Scope

Coverage audit for V2 readout/protocol/application evidence. It tests extraction coverage and sparsity; it does not validate equation reconstruction or physical mechanisms.
