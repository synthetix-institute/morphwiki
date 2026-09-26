# Find a writable state

The [spin example](../08_quantum_construction.md) asks which coordinates are
needed to predict a measured signal. A memory experiment adds a temporal
question: after an input is removed, which physical state carries its effect
into a later measurement? The answer requires a writing operation, dynamics
during release and a measurement that distinguishes the resulting states.

## Derive a write threshold

Let $s$ be a scalar material coordinate, $\epsilon$ a control parameter and
$h(t)$ an applied writing field. A simple overdamped model is

```math
\dot s=\epsilon s-s^3+h(t).
```

At $\epsilon>0$ and $h=0$, the stable states are
$s_\pm=\pm\sqrt{\epsilon}$. The field-free potential
$V_0(s)=s^4/4-\epsilon s^2/2$ has a barrier
$\epsilon^2/4$ between them. Writing with a positive field changes the
potential to $V_0(s)-hs$ and tilts the
potential until the negative well disappears. At that point both the drift
and its derivative vanish:

```math
\epsilon s-s^3+h=0,\qquad \epsilon-3s^2=0
\quad\Longrightarrow\quad
h_c=\frac{2\epsilon^{3/2}}{3\sqrt{3}}.
```

For $\epsilon=1$, the predicted barrier is $0.25$ and the threshold is
$h_c\simeq0.385$. After the field is removed, the selected well persists
until noise drives a transition across the barrier. A measurement of the sign
of $s$ measures the stored bit.

```mermaid
flowchart LR
    P["Prepare a well"] --> W["Apply h beyond the write threshold"]
    W --> F["Remove h; evolve in the double well"]
    F --> R["Measure the sign of s"]
```

With FieldBridge installed next to MorphWiki
(`python3 -m pip install -e '../fieldbridge[memory]'`), run from the
MorphWiki root:

```bash
python3 -B -m fieldbridge memory card ../fieldbridge/examples/memory/pitchfork.json \
  --quick --out-dir build/tutorial_pitchfork_memory
```

The run writes `card.json`, `card.md` and `card.png`. In `card.json`,
`card.states.count` is 2, `card.barrier.barrier` is approximately 0.25 and
`card.threshold` is approximately 0.385. The analytic calculation establishes
these values for this model; the code also checks them through sampled
states and numerical continuation. `--quick` reduces the number of
trajectories and skips the swept-write check.

The model is the specification `examples/memory/pitchfork.json` in
FieldBridge. In `fieldbridge/memory/`, `analysis.py` finds stable states and
barriers, `construct.py` locates write points, and `discovery.py` assembles
the results into a card.

## Construct the same local write in a reaction

The autocatalytic reaction model in the same library has concentration $x$,
reservoir-controlled parameters $a,b$ and a fixed rate coefficient $k_3$:

```math
\dot x=-x^3+ax^2-k_3x+b.
```

At each fixed parameter choice, shifting to $s=x-a/3$ exposes the terms
that distinguish this reaction from the symmetric double well:

```math
\dot s=-s^3+\left(\frac{a^2}{3}-k_3\right)s
 +\left(b+\frac{2a^3}{27}-\frac{ak_3}{3}\right).
```

The final bracket biases one state over the other. Setting
$b=ak_3/3-2a^3/27$ removes that bias. The critical value
$a_c=\sqrt{3k_3}$ also makes the linear coefficient vanish: this is the
cusp where the local write changes from a one-sided fold to a symmetric
choice. Moving $a$ through $a_c$ while adjusting $b$ along the zero-bias
curve varies the linear coefficient through zero. For an actual time-dependent
sweep, the moving coordinate adds $-\dot a/3$ to $\dot s$; the writing
protocol must account for that drive as well.

`construct.py` locates the folds numerically and uses the second parameter
to cancel their quadratic asymmetry. The reaction calculation runs with
`../fieldbridge/examples/memory/schlogl.json` in place of `pitchfork.json`;
`fieldbridge memory design` solves for the parameter setting that restores the
symmetric write (FieldBridge tutorial, Module 5).
The analytic shift explains why tuning both reservoir parameters is needed.

## Keep the state that the measurement needs

The scalar model stores one bit, but a measured coordinate may conceal the
state that carries earlier inputs. Let $x$ be a measured population
difference and $z$ an unmeasured imbalance, with relaxation rates
$a_x,a_z>0$ and couplings $b,c$:

```math
\dot x=-a_xx+bz,\qquad \dot z=cx-a_zz.
```

Eliminating $z$ gives

```math
\dot x(t)=-a_xx(t)+be^{-a_zt}z(0)
 +bc\int_0^t e^{-a_z(t-u)}x(u)\,du.
```

The term proportional to $z(0)$ carries the unmeasured preparation. The
integral carries feedback through the unmeasured coordinate. Even at $c=0$,
two samples with the same $x(0)$ can have different later $x(t)$ when their
$z(0)$ values differ and $b\ne0$. Preparation and measurement therefore
determine which reduced coordinates suffice for prediction. FieldBridge's
`examples/memory/compartments.json` specifies a three-compartment version of
this model; its card has a single state, with memory only in the unmeasured
coordinate (FieldBridge tutorial, Module 7).

The [carrier-transfer module](memory_transfer.md) tests whether a writable
state survives a change of carrier. The [protocol module](memory_constructor.md)
asks whether an experimental sequence retains more than its final input.

**Exercise.** At $\epsilon=4$, calculate the barrier and writing threshold
from the equations above. Which quantity controls long retention, and which
sets the deterministic field required to remove a well?

[Material topic paths](index.md) · [Main tutorial](../index.md)
