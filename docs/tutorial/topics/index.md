# Physical topic paths

The [main tutorial](../index.md) uses interacting spins to teach one route
from a measured quantity to a closed prediction. Other physical questions
can use the same sequence: specify the state and operation, derive what the
measurement needs, test a changed operation, then connect the calculation to
its source and experimental realization. The equations and discriminating
measurements differ by topic.

| Topic | Starting question | Current path |
| --- | --- | --- |
| [Quantum observable closure](../01_three_views.md) | Which expectations determine one spin's later magnetization? | Complete tutorial and executable four-dimensional calculation |
| [Writable states](memory_dynamics.md) | Which state survives a write and field-free release? | Double-well threshold, barrier and unmeasured-coordinate calculation |
| [Carrier transfer](memory_transfer.md) | Does the same dynamics survive a change of carrier? | Nematic-to-vector map, residual and loop compatibility |
| [Ordered memory](memory_constructor.md) | Which protocol distinguishes retained order from the last write? | Write-order comparison and local realization screen |

The quantum calculation and the first two memory paths run with the
standalone FieldBridge repository installed next to MorphWiki
(`python3 -m pip install -e '../fieldbridge[memory]'`). The ordered-memory
path uses a protocol runner that is not yet public.

## Extend the constructor to another material

A new material is written as a FieldBridge memory specification: one JSON
file with a carrier and drift $F(q;p)$, its parameters, noise, boundary or bath
description, control range and measured observable (FieldBridge tutorial,
Module 2). For gradient dynamics, supply a potential; for a continuous
symmetry, specify the neutral modes used when comparing states.
`fieldbridge/memory/identity.py` defines the `Realization` that a
specification becomes. It separates the operation $\Omega$ from its carrier
$\Xi$ and records the closure $C$, observable $R$, writing protocol $P$ and
parameters $A$. The executable drift and carrier enter the state
calculations. `closure` and the protocol text describe physical conditions,
while the writing field and control sweeps implement specific drives.
Extending the constructor to a new class of materials means implementing its
actual boundaries, input operations and measurement where the existing
solvers need them.

`fieldbridge memory card` then samples stable states, searches for writing
events, tests finite-noise retention and produces a card (Module 7 applies
the sequence to a material from another field). A proposed map to an existing
carrier belongs in `fieldbridge/memory/transfer.py`, where the drifts can be
compared. An experimental design, which checks writing sequences, release,
measurements and controls, belongs in a realization specification for the
protocol runner of the ordered-memory path. The dynamical card and the protocol
report answer different questions; together they identify the next physical
calculation or experiment.
