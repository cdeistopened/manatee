# The "AI" / Reactive Control System

## What it is (plain language)

The "Prospero AI" that the project documents describe as a "proprietary, patented 3rd Generation Artificial Intelligence" is, in the actual source code, a **roughly 70-line reactive light-following controller** written in a LOGO dialect (the Lego/MicroWorlds Logo family). It is not machine learning, not a neural network, not an inference engine, and not "AI" in any modern sense. It is a textbook **Braitenberg vehicle** — the simplest kind of cybernetic robot, where sensor readings are wired almost directly to motor commands.

The mechanism is honest and elegant in its minimalism: the robot has six light sensors arranged around its body (labeled a through f). Every cycle it reads all six, figures out which direction is brightest, and steers its two thrusters to turn toward that direction. Because algae grow fastest where sunlight is strongest, "swim toward the brightest light" is a reasonable proxy for "swim toward where your cargo will grow best" — and toward open water during the day. That is the entire intelligence: a phototaxis loop, the same behavior a moth or a single-celled alga performs. There is no map, no mission planner, no obstacle model, no learning, and no memory beyond the current sensor frame.

This matters two ways for due diligence. First, the gap between the marketing language ("redundant marine-hardened inference engine," "Drift & Correct strategy," "automated docking," "patented 3rd-generation AI") and the shipped artifact (a single light-seeking LOGO routine with a known arithmetic bug) is large — the prose subsystem docs describe a system that the code does not implement. Second, the actual controller is genuinely sound as a *starting point*: minimal reactive control is the correct, robust, low-power approach for a slow solar drifter, and it is cheap and credible to modernize. The honest framing for investors is: "the navigation 'AI' is a clean Braitenberg phototaxis prototype, not autonomy — and that's fine, because the upgrade path is short and well-understood."

## How it works (the real mechanism, technical)

Source: `AIsourcecode1.txt` (the file is the canonical artifact; the `.md` subsystem docs are aspirational prose, not code).

Two routines:

**`avgread`** — samples and averages the six sensors.
- Declares a 6-element array per sensor (`sa`–`sf`, depth 3) plus globals `a b c d e f final`.
- Reads each sensor three times (`sensora`…`sensorf`), 10 ms apart, into array slots 0/1/2 — a simple 3-sample temporal average to beat wave glint and noise.
- Computes each channel average, e.g. `seta ((aget sa 0) + (aget sa 1) + (aget sa 2) / 3)`.
- Then picks a winning direction by comparing each sensor against the others:
  ```
  if a > (b + c + d + e + f / 5) [setfinal 1]
  if b > (a + c + d + e + f / 5) [setfinal 2]
  ... through f -> setfinal 6
  ```
  `final` (1–6) encodes "sensor a is brightest" … "sensor f is brightest."

**`lightsensedirection`** — the state machine / steering loop.
- Calls `avgread`, then:
  ```
  if 20 > (a + b + c + d + e + f / 6) [setfinal 0]
  ```
  This is the **darkness / night gate**: if overall light is below threshold, set `final 0`.
- `final = 0`: motors off, `wait 9000` (~9 s), recurse. (Deep dark — sleep long.)
- `final = 1`: motors off, `wait 6000`, recurse. (Sensor a = forward/center is brightest → already pointed at the light, so coast and re-check.)
- `final = 2,3,4`: `a, thisway` / `b, thatway` — drive the two thrusters to rotate one way, then enter a tight `loop` that keeps reading until `final` returns to 1 (re-centered on the light), then recurse.
- `final = 5,6`: `a, thatway` / `b, thisway` — rotate the **other** way.

So the behavior is: **average six light sensors → decide which is brightest → rotate toward it until the front sensor (a) is brightest → coast → repeat; if it's dark, sleep.** Power draw is near zero except during correction turns — this is effectively the "Drift & Correct" strategy the prose doc names, just implemented as four lines rather than a planner.

**The operator-precedence bug (load-bearing, real).** In every comparison the author writes `(a + b + c + d + e + f / 6)` intending *the mean of all six*. But in LOGO — as in standard arithmetic and essentially every infix language — **division binds tighter than addition**. The expression actually evaluates as:
```
a + b + c + d + e + (f / 6)
```
i.e. five sensors at full weight plus one-sixth of the sixth. The same bug appears in:
- the night gate (`20 > a+b+c+d+e+f/6`) — threshold is wrong and biased toward whatever sensor sits in the `f` slot;
- all six "brightest" tests (`a > b+c+d+e+f/5` → `a > b+c+d+e+(f/5)`);
- and even the per-channel temporal average (`(aget sa 0)+(aget sa 1)+(aget sa 2)/3` → only the third sample is divided by 3).

Consequence: the controller still *works* as a rough light-follower (the dominant terms are real sensor sums, so the brightest direction usually still wins), but the thresholds are skewed and the `f`/back sensor is structurally under-weighted. It is a real, reproducible defect — exactly the kind of thing that proves the code was written and (lightly) run, but never code-reviewed or unit-tested. The fix is one set of parentheses per line: `((a + b + c + d + e + f) / 6)`.

**The hardware it maps to.** `LowellAI.png` (the analog board) and `photoschematicAssembly1b.jpg` (the bench build) show the physical realization of this same idea, and reveal that two parallel control philosophies exist in the corpus:
- **Analog Braitenberg board** (`LowellAI.png`): two photodiode + 1381 voltage-supervisor + 2N3906/2N3904 transistor channels driving two motors, with a 100K pot, a green "sensing diode," and a 680K/0.22µF "tetra-helical"-style center network. This is a *purely analog* light-seeking vehicle — no microcontroller at all. It is the hardware twin of the LOGO routine: cross-coupled light-to-motor steering.
- **Bench assembly** (`photoschematicAssembly1b.jpg`): a solar panel, a "2200 WATTS" supercap/"low-ESR" module, a 16×2 LCD, a diaphragm pump, **solid-state relays (Fotek SSR-25/40 DA)**, a busbar, and a **hand-soldered perfboard with a trim-pot** — a relay-driven power/process controller, not a navigation computer. This is consistent with a real but very early breadboard-grade prototype.

Numbers that are actually in the code: 6 sensors; 3 temporal samples × 10 ms; night-gate threshold = 20 (units unspecified ADC counts); sleep waits of 9000 and 6000 (≈9 s, 6 s); correction re-check `wait 300` (≈0.3 s). These are the only quantitative facts the "AI" provides.

## New-vs-old (what the 2024 PRIME / EVIE-2c design changed for THIS system)

Evidence: `VBShdl-1m5manatee2b1PRIME.png`, `VBShdl-1m5manatee2b1PRIME_BimodalTurbine.png` (SketchUp previews), `Circuits/photoschematicAssembly1b.jpg`, `Circuits/LowellAI.png` (all dated within the 2022–2024 NEW model folder).

The PRIME / EVIE-2c rev is a **mechanical and power-architecture redesign, not a control-system redesign.** For the "AI" specifically:

1. **No change to the controller logic.** The same two-thruster, light-seeking paradigm survives. The model name embeds it: `manatee2b` — **"2b" is the Braitenberg vehicle 2b designation** (crossed, excitatory sensor-to-motor wiring = "aggression," steers *toward* the source). The naming confirms the design intent is still a Braitenberg phototaxis vehicle.
2. **Two thrusters → likely differential drive at the pontoon ends.** The PRIME hull is now twin pontoons on a tensegrity frame with a central growth/processor drum. The previews show **amphibious wheels at the pontoon ends** — a new actuator the old LOGO code does not address. The existing `a, thisway / b, thatway` two-actuator steering can drive a differential pontoon-thruster pair directly, but the wheels (beaching/haul-out) are unhandled by any code in the corpus.
3. **`+BimodalTurbine` variant adds a horizontal-axis turbine on a central mast.** This is a new power/sensing element (wind or flow harvesting) that would require at minimum a charge-state input and a furl/stow control — neither exists in the LOGO routine. It widens the gap between "what the hull can do" and "what the controller knows about."
4. **Power controller, not brain, is what got built out.** The `photoschematicAssembly1b` bench board (solar → 2200W supercap module → SSR-switched pump + LCD + perfboard) is the PRIME-era control hardware that actually exists. It is a **homeostatic power/process switcher** (run the pump, read a level, show status) — exactly the "homeostatic control" the prose doc claims — but it has **no GPS, no IMU, no compass, no radio, and no microcontroller-grade autonomy**. The "navigation AI" and the "process controller" are two separate, both-primitive systems.

Net: PRIME/EVIE-2c made the *vehicle* more ambitious (amphibious, turbine-augmented, tensegrity) while the *control intelligence* stayed at the 2015-era Braitenberg level. The new mechanical capabilities (wheels, turbine, docking) have **no corresponding control code** — they are CAD-only.

## Evidence & maturity

| Claim / element | Status | Source |
|---|---|---|
| LOGO phototaxis controller exists | **DOCUMENTED (code)** | `AIsourcecode1.txt` |
| Operator-precedence bug present | **DOCUMENTED / reproducible** | `AIsourcecode1.txt` lines 6, 65–76 |
| Analog Braitenberg board designed | **DOCUMENTED (schematic)** | `LowellAI.png` |
| Bench power/process prototype built | **BUILT (photo of real hardware)** | `photoschematicAssembly1b.jpg` |
| 2023 marina test of a physical unit | **BUILT + partially tested** | `04_Prototype-Testing/2023-Marina-Tests/*.jpg` |
| "3rd-gen patented inference engine," redundant processors | **ASSERTED, unsupported** | `MASTER_CONTROL_AI.md` (prose only) |
| Autonomous Hub→High-Seas navigation, automated docking | **ASSERTED, no code/hardware** | `MASTER_CONTROL_AI.md`, `OPERATIONS_CONTROL_CENTER.md` |
| Mesh fleet comms, satellite link, Rutgers COOL / NOAA buoy integration | **ASSERTED, no code/hardware** | `COMMUNICATIONS.md` |
| Manned 24/7 OCC with tele-presence override | **ASSERTED (future concept)** | `OPERATIONS_CONTROL_CENTER.md` |

**Maturity verdict for this system: built-untested.** The light-seeking controller and analog board are real designs and a related power-control prototype was physically built and wet-tested at a marina (2023), but there is **no evidence the LOGO navigation code was ever run on the water, no closed-loop autonomy test, no telemetry log, and no validation of the controller against waves, current, or fouled sensors.** Everything above "follow the light / run the pump" is prose.

## Validation status

- **"It's a Braitenberg phototaxis vehicle, not AI."** — **PLAUSIBLE → effectively CONFIRMED.** The code is a direct implementation of Braitenberg Vehicle 2b (Valentino Braitenberg, *Vehicles: Experiments in Synthetic Psychology*, MIT Press, 1984). The model filename `manatee2b` and the crossed analog wiring in `LowellAI.png` corroborate the intent. This is well-understood, sound, robust minimal control.
- **Operator-precedence bug (`f / 6` not `(sum)/6`).** — **CONFIRMED / FALSE-as-written.** LOGO, like standard arithmetic and every common infix language, evaluates `/` before `+`. The averages and thresholds are mathematically wrong as written. Not fatal to the "find the brightest sensor" behavior, but the thresholds and the back-sensor weighting are off. One-parenthesis fix.
- **"Redundant marine-hardened inference engine / 3rd-generation AI."** — **DUBIOUS / unsupported.** No inference code, no model, no redundant-processor design anywhere in the corpus. The only real compute is a hand-soldered perfboard with a trim-pot and SSRs. Treat as marketing.
- **"Autonomous navigation Hub → Mid-Atlantic Bight + automated docking."** — **DUBIOUS.** Open-ocean autonomous navigation requires, at minimum, GPS/GNSS, a heading reference (compass/IMU), sea-state-robust state estimation, and collision avoidance. None are present. Phototaxis alone cannot navigate to a named offshore coordinate or dock precisely. Achievable in principle with off-the-shelf marine autonomy (see below) but **not demonstrated and not in the code.**
- **"Mesh fleet comms + satellite + live Rutgers COOL / NOAA buoy integration."** — **DUBIOUS as built; PLAUSIBLE as roadmap.** Each piece is a standard, buyable capability (Iridium/Starlink, LoRa mesh, public NOAA/COOL feeds), but there is zero implementation evidence — no radios in the schematic, no comms code.
- **Three-sample 10 ms temporal averaging to reject wave glint.** — **PLAUSIBLE and sensible** as a noise filter, though 30 ms total is short relative to wave/glint timescales (often 0.5–5 s); a longer or median filter would be better.

## Red flags & open questions

1. **Marketing-vs-artifact gap is the headline risk.** Every `.md` subsystem doc describes a system one to two orders of magnitude more capable than the code/hardware that exists. An investor reading only the prose would badly misjudge maturity. The build-kit/license story must lead with the *real* artifact.
2. **The shipped code has an uncorrected arithmetic bug** in every averaging/threshold line. Proves it was never reviewed or unit-tested. (Easy fix; cited here as a maturity signal, not a dealbreaker.)
3. **Two un-reconciled control stacks.** A microcontroller-free analog board (`LowellAI.png`) *and* a LOGO software routine *and* an SSR/perfboard power controller all coexist. Which is the intended production controller? Unknown. No integration diagram ties navigation + power + comms together.
4. **New PRIME hardware has no control code.** Amphibious wheels, the bimodal turbine, and docking are CAD-only; nothing in the corpus actuates or senses them.
5. **No state estimation at all.** No GPS, IMU, compass, current/heading sensing. A pure light-follower in a 3–5 kt tidal current can be swept backward while "correctly" facing the sun. Open-ocean station-keeping is unaddressed.
6. **Sensor failure modes unhandled.** Biofouling, bird droppings, salt film, or a stuck-bright sensor would hijack the phototaxis with no fault detection. For a months-at-sea algae platform this is a first-order reliability problem.
7. **"Patented 3rd-generation AI" claim** — needs the actual patent/application number to verify; nothing in this system's files supports a patent on the control logic (a Braitenberg vehicle is 40-year-old prior art and not novel).
8. **LOGO is a dead end as a runtime.** No marine-grade LOGO interpreter ships on real hardware. The code is a *specification of behavior*, not a deployable program. It must be ported.

## Concrete improvements (buildable upgrades + cheap de-risking experiments)

**Tier 0 — trivially correct the existing design (hours):**
- Fix the precedence: `((a + b + c + d + e + f) / 6)` and `((s0 + s1 + s2) / 3)` in all eight lines. Re-bench against `LowellAI`-style sensor inputs to confirm the brightest-direction decision is unchanged but thresholds are now correct.
- Add a stuck-sensor sanity check: reject any channel that reads pinned-max for N cycles.

**Tier 1 — port to a real microcontroller (days, ~$50–150 BOM):**
- Re-implement the exact same six-sensor phototaxis on an **ESP32 or RP2040 (or Arduino-class)**. Same behavior, but now with watchdog, logging, OTA update, and PWM thruster control instead of bang-bang. This alone converts "LOGO spec" into a deployable, demonstrable controller and is the single highest-leverage step.
- Drive the two pontoon thrusters as differential drive; add a furl/stow output for the turbine and a wheel-disable interlock so the PRIME mechanicals are at least addressable.

**Tier 2 — add minimal state estimation / sensor fusion (weeks, ~$100–300):**
- Add **GPS + 9-DOF IMU/compass** and a simple complementary or Kalman filter. Now the robot knows heading and position, can hold a waypoint, and can compensate for current — turning "follow the light" into "go to a coordinate while biasing toward light/algae optimum." This is the credible version of the "autonomous Hub→High-Seas" claim.
- Fuse the existing light array as a *bias term* on a waypoint controller rather than the sole input. Best of both: robust autonomy + algae-growth optimization.

**Tier 3 — comms + mission layer (weeks–months):**
- Off-the-shelf **LoRa (fleet/near-shore) + Iridium/Starlink (offshore)** for telemetry; ingest public **NOAA buoy + Rutgers COOL** feeds shoreside for routing, exactly as the prose doc imagines — but actually wired.
- **Optional, honestly-scoped LLM/edge-ML layer for *mission planning only* (not control):** an LLM at the shoreside OCC that reads telemetry + weather and proposes harvest routes / return-to-hub timing, which a human approves and the deterministic onboard controller executes. Keep ML out of the safety-critical inner loop. This is where the word "AI" can be used truthfully.

**Cheapest high-value experiment:** put the Tier-1 ESP32 port in a tank or pond with a moving lamp and log that it tracks the light through wave-chop noise. A single afternoon test turns the entire "AI" claim from asserted to demonstrated.

## Kit/license angle

The control system is the **most sellable, lowest-risk piece of the whole project**, precisely because it is small, honest, and easy to make real:

- **"Braitenberg light-seeking marine robot" build-kit / STEM kit.** The analog `LowellAI` board (photodiodes + 1381 + 2N3906/3904 + two motors) is a genuinely charming, teachable, ~$30–60 BOM educational kit: a self-contained phototaxis robot with no code required. This is a clean, shippable product on its own and a credible top-of-funnel for the larger vision. It is also *defensible to sell* because it does exactly what it claims.
- **ESP32 phototaxis controller reference design + firmware (Tier 1 above)** as the "starter brain" kit for the EVIE/Mobula platform — open the path from hobby kit to the real solar drifter. Licensable as a hardware reference + MIT/dual-licensed firmware.
- **What is NOT licensable as novel IP:** the control *logic* itself. A Braitenberg 2b vehicle is 1984 prior art; the phototaxis algorithm is unpatentable. Any "patented AI" license language should be scrubbed — the licensable value is the **integrated platform** (hull + power + growth drum + control), the brand, and the build-kit packaging, not the steering algorithm.
- **License template caution:** the editable 2022 patent-license template should not assert patent coverage over the navigation/control method. Position the IP around the cavitation reactor and the platform integration; treat the controller as an open, teachable, kit-friendly subsystem that *adds* credibility rather than overclaiming it.
