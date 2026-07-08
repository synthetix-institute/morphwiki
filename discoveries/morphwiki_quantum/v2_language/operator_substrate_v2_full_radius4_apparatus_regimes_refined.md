# Refined V2 Apparatus Regime Audit

- Readiness: `usable`
- Rows assigned: `14523959`
- Original A tokens: `18`
- Refined A tokens: `19`
- Split parents: `1`

## Conclusions

- A is treated as a conditional apparatus state, not a primitive atom.
- Only oversized/high-entropy parents are split; stable small regimes are preserved.
- Refined labels are written as a separate artifact and do not overwrite the learned symbolic language.

## Parent Decisions

### `A00` support `6151464` fraction `0.4235`
- decision: `kept`
- reason: candidate splits failed support, silhouette, or entropy-reduction gates
- parent entropy: `0.5862769986828571`

### `A01` support `1157760` fraction `0.0797`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.4314031161454075`

### `A02` support `1104645` fraction `0.0761`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.47052160616891164`

### `A03` support `1054640` fraction `0.0726`
- decision: `split`
- reason: large/high-entropy parent passed child support and entropy gates
- parent entropy: `0.5782253313522459`
- accepted children: `2`; entropy reduction `0.045802002536709956`; silhouette `0.12000563740730286`; min child fraction `0.21550671319123113`
  - `A03.00`: support `227282`, fraction `0.216`, A03:Ω_ω03-Ξ_ξ04-R_unclassified
  - `A03.01`: support `827358`, fraction `0.784`, A03:Ω_ω03-Ξ_ξ01-R_unclassified

### `A04` support `866698` fraction `0.0597`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.4558724659132579`

### `A05` support `785279` fraction `0.0541`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5104776563750671`

### `A06` support `659591` fraction `0.0454`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5249529913048815`

### `A07` support `537584` fraction `0.0370`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5509094710792963`

### `A08` support `503973` fraction `0.0347`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.4982579056275609`

### `A09` support `389797` fraction `0.0268`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5850439214870322`

### `A10` support `295950` fraction `0.0204`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.711095278730678`

### `A11` support `246763` fraction `0.0170`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.4277605188139247`

### `A12` support `236455` fraction `0.0163`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5199889699858435`

### `A13` support `232938` fraction `0.0160`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.6791156009328745`

### `A14` support `143926` fraction `0.0099`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.27396654412694005`

### `A15` support `53252` fraction `0.0037`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.7331053884149485`

### `A16` support `51680` fraction `0.0036`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.4613326905549991`

### `A17` support `51564` fraction `0.0036`
- decision: `kept`
- reason: below split thresholds
- parent entropy: `0.5091000777822174`

## Scope

Second-stage refinement of V2 A apparatus regimes using fixed Ω/Ξ assignments, route evidence and operator/substrate product features. This tests whether broad A basins can be subdivided; it does not prove exact physical mechanism classification.
