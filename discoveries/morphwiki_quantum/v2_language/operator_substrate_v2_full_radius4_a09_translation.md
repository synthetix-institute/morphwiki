# Legacy A09 To Operator/Substrate Translation

- Readiness: `limited_no_current_alignment`
- Decision: `insufficient_current_row_alignment`
- Legacy A09 records: `138`
- Matched current rows: `4`
- Direct row matches: `4`
- Source-alignment matches: `0`

## Translation Test

Hypothesis: old A09 corresponds to operator evidence without substrate support, written operationally as `(Ω, 0)`.

- Operator-high rate: `0.2500`
- Substrate-low rate: `0.5000`
- Operator-without-substrate-support rate: `0.2500`

## Current Coordinate Distributions

### `omega_distribution`
- `Ω06` `Ω:integral`: n=`1`, fraction=`0.2500`
- `Ω00` `Ω:readout_closure_spectral`: n=`1`, fraction=`0.2500`
- `Ω02` `Ω:spectral`: n=`1`, fraction=`0.2500`
- `Ω10` `Ω:spectral_readout_closure`: n=`1`, fraction=`0.2500`

### `xi_distribution`
- `Ξ00` `Ξ:coordinate_field_carrier_selector`: n=`2`, fraction=`0.5000`
- `Ξ05` `Ξ:closure_field_carrier_coordinate`: n=`2`, fraction=`0.5000`

### `alpha_distribution`
- `A00` `A:Ω_readout_closure_spectral-Ξ_diffuse-R_mixed-Γ_lo`: n=`2`, fraction=`0.5000`
- `A04` `A:Ω_readout_closure_spectral-Ξ_closure_field_carrier_coordinate-R_boundary-Γ_lo`: n=`1`, fraction=`0.2500`
- `A07` `A:Ω_spectral_readout_closure-Ξ_selector_hilbert_field_carrier-R_spectral-Γ_lo`: n=`1`, fraction=`0.2500`

## Completion Evidence
- `closure_constraints`: mean=`0.0000`, median=`0.0000`, active_columns=`10`
- `readout_current`: mean=`0.0250`, median=`0.0000`, active_columns=`10`
- `protocol_order`: mean=`0.0000`, median=`0.0000`, active_columns=`8`

## Void Membership
- `operator_void`: `0.5000`
- `substrate_void`: `0.2500`
- `coupling_void`: `0.0000`
- `transition_void`: `0.0000`
- `readout_closure_void`: `0.2500`
- `control_artifact_void`: `0.0000`

## Top `(Ω,0)` Candidates
- `Ω10` `Ω:spectral_readout_closure`: n=`1`, fraction=`1.0000`

## Example Rows

### row `2500`
- Ω label: `21`; Ξ label: `1`; A label: `9`
- energies: operator=`1.4142`, substrate=`1.4142`, control=`2.0156`
- voids: `operator_void, substrate_void, readout_closure_void`

### row `72`
- Ω label: `13`; Ξ label: `13`; A label: `4`
- energies: operator=`1.0000`, substrate=`0.0000`, control=`2.0156`
- voids: ``

### row `1509`
- Ω label: `25`; Ξ label: `13`; A label: `4`
- energies: operator=`0.0000`, substrate=`0.0000`, control=`2.0119`
- voids: ``

### row `1581`
- Ω label: `15`; Ξ label: `1`; A label: `13`
- energies: operator=`1.0000`, substrate=`1.4142`, control=`2.0061`
- voids: `operator_void`

## Scope

Translation audit from legacy A09 witnesses to current operator/substrate coordinates. It tests coordinate landing and operator-without-substrate support; it does not prove that A09 is a physical law, a theorem, or a current atlas cluster.
