# Mobula / EVIE-2c — One-Pager

**Subject:** "Mobula" / "EVIE-2c" algae-to-oil reactor · **Inventor:** Rudy Behrens (Solaris Cybernetics / Barsoom Engineering)
**Condensed:** 2026-07-03, from the full engineering due-diligence pass (see `engineering-assessment.md` and `systems/` for the detail).

**The one honest sentence:** *A chemical-free, solvent-free, transducer-free, solar-powered cavitation reactor that cleans algae-bloom water and recovers a diesel-density oil — third-party-validated at bench scale, one focused round of bench tests from proving its full energy balance, on a buildable floating platform, from a career rotating-equipment engineer.* Not "diesel-from-the-ocean robot" — that framing gets ahead of what's proven so far, and is worth dropping from any pitch until the lab numbers back it up.

---

## What it is

A solar-powered floating reactor that pumps wet algae-bloom slurry through a precisely shaped stainless nozzle. The pressure drop triggers hydrodynamic cavitation — collapsing micro-bubbles create real, extreme hot-spots (textbook sonochemistry) that drive *hydrous pyrolysis*, the same water-mediated chemistry that makes petroleum, in a single pass. No furnace, no catalyst, no solvent, no driven horn. The sun is the energy source; the machine is a solar converter, not a free-energy machine.

## What's already proven by outside labs

- Diesel-density oil, measured by **two accredited labs** (Intertek 2006, BEAR 2012).
- A reactor that treated **5 gallons on 37 watt-hours with no chemicals** and pulled nutrients out of the water (AECOM/PACE).
- A **buildable platform** from a fully-sourced parts list, and a **founder with a checkable engineering record** (Sunoco chief pump engineer, API 610/617 committees, Three Mile Island restart team).

## Where it wins in the market

Against LG Sonic (which kills the bloom and leaves it in the lake — this reactor *harvests* it into wax and removes the nitrogen and phosphorus), against Cavitation Technologies and Hielscher (no solvent, no powered horn), and against the entire survey-drone field (they measure the ocean; this reactor does work on it).

## What's honestly not yet proven

The exact conversion chemistry (does it crack biomass, or extract existing lipid?), the end-to-end energy balance, and open-ocean operation. Each is testable — a GC-MS run, a calorimeter run, and a sunlight-only growth comparison — on the rig that already exists. See `engineering-assessment.md` §4 for the specific tests and what each one would settle.

## The near-term build

Rather than the full ocean platform, the fastest path to a provable, sellable product is the **Tier-1 "Pond-to-Wax" kit** — a tabletop version of the same reactor that runs on pond scum, cleans the water, and produces a wax that's already a finished product (candles) regardless of how the fuel-chemistry questions resolve. Full BOM and build steps in `engineering-assessment.md` §2.


---

# Solaris Cybernetics — Engineering Assessment & Pond-to-Wax Build Plan


---

## 1. Does it work as it says? — best-guess science verdict, claim by claim

*Taking the corpus charitably and finding the version that works. Short answer up top:*

> **The autonomous ocean-diesel-robot framing doesn't hold up as described. A smaller, honest machine underneath it does.** Strip the "ocean robot makes diesel" framing and what remains is real and useful: cavitation genuinely ruptures algae cells and frees their oil, cheaply, with no chemicals, while stripping nutrients from the water. What isn't supported yet is the leap from "frees the oil" to "cracks biomass into finished diesel," and the leap from "a pond raft that trickles wax" to "a Sea-State-7 autonomous ocean robot at 19:1 EROI." The charitable, buildable version right now is a **lipid-extraction + bloom-remediation reactor whose product is wax** — and that version clears its own evidence bar today.

**Keystone 1 — What does the nozzle actually do: crack, extract, or hydrogenate?**
Best guess: **extraction (cell disruption), not cracking, and not hydrogenation.** Hydrodynamic cavitation from a 300-psi pump through a 4-inch nozzle produces collapse hot-spots that are genuinely extreme (sonochemistry confirms ~5,000–12,000 K, hundreds of atmospheres) — but they are sub-micron, nanosecond, and stochastic. The *mass fraction* of slurry that spends enough time-at-temperature to break C–C bonds in a pass or two is tiny. What cavitation is *documented* to do well (peer-reviewed, and already commercialized for microalgae) is **lyse cell walls and release intracellular lipid**. The observed behavior — "paraffin floats up and is skimmed," N and P drop — is exactly the signature of cell-rupture-plus-flotation, not molecular cracking. So the GC-MS will most likely show **intact triglycerides / free fatty acids**, not the C15/C17-from-C16/C18 decarboxylation fingerprint that would prove cracking. The "hydrogenation" story is almost certainly a relabeling artifact: the granted patent claimed an electrolysis→H₂ route, no as-built rig carries an electrolyzer, so there is no hydrogen source. *Worth testing, not banking on yet:* over 30+ recirculating passes on a warm (150 °F) feed, cumulative micro-dosing could partially depolymerize the released lipid — "cracking over many passes," not "single-pass." That's a hypothesis the pass-count assay settles.

**Keystone 2 — Is the energy balance real (the 5.34% / 19:1 EROI)?**
Best guess: **the conversion step is genuinely cheap and net-positive; the headline number is ~2–4× too optimistic; and the *system* EROI is only positive if you grow on sunlight.** The AECOM datapoint — 37 Wh to process 5 gallons, ~25 BTU/gal of electrical input — is real and points to a low-energy process, because you are *releasing already-made oil*, not synthesizing energy (the sun did that). But 5.34% rests on a premise — that cavitation is "adiabatic / thermodynamically reversible" so the energy is "recovered" — that doesn't hold up. Cavitation is a textbook *dissipative, entropy-generating* process; that's why it makes heat, light, noise, and erosion. A more honest reactor-boundary cost is more like **10–20% of the output energy** — still net-positive. The real EROI risk is the **14-hour LED grow-light**: at any real grow area that load is tens of kWh/day and dwarfs generation, flipping system EROI below 1. *This is why the honest product grows on ambient sunlight* (which a pond or a parish courtyard does for free) and drops the lit-ocean-robot entirely. So: **works as "a cheap way to get oil out of sun-grown algae." Doesn't yet work as "19:1 free energy" — that number needs the lab to confirm or correct.**

**Keystone 3 — Does it make diesel?**
Best guess: **not yet demonstrated — it makes a diesel-*density*, diesel-*heating-value* oil/wax that is almost certainly not a diesel-spec distillate.** The one real fuel assay (BEAR 2012: 32.71° API, 134,258 BTU/gal) measures density and heat of combustion only — both satisfied by *any* hydrocarbon of that class, including raw algal oil and wax. No cetane number, no distillation curve, no oxygen content. HTL-type bio-crude is typically 5–20 wt% oxygen and *requires* catalytic upgrading the whole field agrees on; this rig has no catalyst and no H₂. Best expectation: the product is a **waxy paraffin / bio-crude**, high pour point, not engine-ready as-is. **That's actually the strong pivot** — as a *wax* it's already a finished, saleable product (candles), so the outcome is good either way: paraffin → traditional candle, triglyceride → "botanical wax" candle. The only claim that doesn't hold up yet is "diesel."

**Keystone 4 — Does the ocean robot work as designed?**
Best guess: **not as specified.** The power budget looks ~10–30× short for a lit, thruster-driven, electrolyzer-bearing, self-navigating open-ocean vessel. The demonstrated device (2015) worked precisely because it ran none of the hard loads: a 7.5 W pump, sunlight (not LED) growth, a freshwater pond, ~1.3 gal/day of wax. "Sea State 7 / 10,000 lb thrust" specs describe hardware that currently exists only in SketchUp. **The version that works today:** a small, mostly-passive, **sunlight-grown pond or nearshore raft** — or simpler still, a **land-based bench unit** beside the pond. Drop the autonomy and the ocean load for now; keep the reactor, and the ocean vision stays the long-term "someday" — it just isn't the thing to build or sell first.

**What this means for the build.** Every genuinely-supported piece survives this reframe: cavitation cell-disruption (real), chemical-free lipid release (real), bloom-water N/P removal (AECOM-validated), a diesel-density oily product (lab-measured), a buildable COTS rig (BOM exists below), a consumable-nozzle razor/razor-blade model (erosion is real → recurring revenue). The parts that don't hold up yet are marketing claims about the finished machine, not the machine itself — every one of them is testable, cheaply, on the bench.

---

## 2. Tier-1 "Pond-to-Wax" demonstrator kit — spec, BOM, build, and what it proves

**What it is.** A tabletop recirculating loop that takes free pond scum (or a spirulina culture), concentrates it by dissolved-air flotation, pumps it through the cavitation nozzle, and skims the released oil/wax — while metering the watt-hours in and the grams of wax out. It is simultaneously (a) a product demonstrator, (b) the rig that could run the lab-grade tests (GC-MS, calorimetry, pass-count — see §3), and (c) something a maker/university buyer would purchase outright. **It deliberately exercises only the proven step** (lipid release + remediation), not the unproven cracking step.

**What the demonstrator proves (and doesn't).**
- *Proves:* the loop runs on a small metered power draw; pond water goes in dirty and comes out clearer (visible N/P/turbidity drop); an oily/waxy layer accumulates and skims; you can weigh it, melt it, and pour a candle. This is a complete, honest value chain a person can watch.
- *Doesn't prove on its own (needs a proper lab pass):* that the wax is "diesel," the true EROI, or the per-pass conversion rate. Those are GC-MS / calorimeter / pass-count tests the same rig can feed.

**BOM.** Part specs (pump model, pressures, nozzle geometry) are sourced from the corpus (`JT1BOM_strings.txt`, `KineticNozzle1.JPG`). **Prices below are current-market estimates — verify at purchase.**

| # | Part | Spec / source | Est. cost (verify) | Notes |
|---|------|---------------|--------------------|-------|
| 1 | High-pressure pump | AR RMW2G24D class, 300 psi × 10 gpm (BOM-sourced) | **$180–260** | The exact BOM part; AR North America pressure-washer pump. A cheaper 12VDC diaphragm pump works for a first bench pass. |
| 2 | Cavitation nozzle | 316 SS, multi-bore, CNC-turned from `KineticNozzle1` DXF (corpus has the drawing) | **$150–400** | One-off machining. "306 SS" in the original drawing is a typo → spec **316**. This is the consumable; make two. |
| 3 | DAF column + bubbler | Sched-40 clear PVC column + aquarium air pump / protein-skimmer | **$60–140** | Standard dissolved-air flotation. Concentrates scum to ~6% solids before the nozzle. |
| 4 | Separator / collection | Food-grade bucket or 5-gal bladder + skimmer weir | **$25–60** | Gravimetric stratification + displacement decant (per corpus). Bench version = a clear bucket. |
| 5 | Plumbing + fittings | Hose, clamps, check valve, tee, ball valves | **$50–100** | — |
| 6 | Power meter | DC clamp meter or INA226 logger (bench: Kill-A-Watt on the AC side) | **$15–35** | The EROI instrument. Cheapest, highest-leverage part. |
| 7 | Feedstock | Free pond scum, or spirulina starter culture | **$0–25** | Free nuisance input keeps the whole thing cheap. |
| 8 | Candle finishing | Double boiler, cotton wicks, molds, thermometer | **$40–80** | Turns wax into the sellable product. |
| | **Total** | | **~$520–1,100** | Bench-scale, one-time. Nozzle is the recurring consumable. |

**Build steps (half a day once parts are in hand).**
1. Assemble the DAF column; run pond scum + bubbler until a green foam concentrates at the top; skim to the feed tank (~6% solids).
2. Plumb feed tank → pump → nozzle → separator → return line back to feed tank (closed loop).
3. Put the power meter on the pump. Zero it. Note feed mass.
4. Run the loop; every N passes, skim the floating wax layer and log grams out vs. watt-hours in.
5. Melt the skimmed wax, pour a candle. Photograph the cleared water beside the starting scum.
6. *(Optional, when ready)* Send a wax sample + a recorded run's numbers to a lab for GC-MS / D86 / calorimetry — see §3.

**What NOT to do in the build:** don't run LED grow-lights (grow on sunlight — it's the honest EROI story); don't add methanol/solvent/catalyst (chemical-free is the whole differentiator); don't call the output "diesel" or "paraffin" on anything public until GC-MS says so — call it "algae-derived wax."

---

## 3. Honest label language (what can be truthfully claimed before a lab confirms more)

The rule of thumb: **claim only cleaned water, cell-released algae oil, and a wax you can hold.** Nothing about diesel, EROI, or fuel grade until a lab confirms it — that's what keeps every claim on solid ground.

**Safe to say today (documented or self-evident):**
- "Made from a nuisance algae bloom — cleaned out of the water it grew in."
- "Chemical-free and solvent-free: the oil is released by pressure alone, no hexane, no lye, no heat source."
- "Renewable algae-derived wax." / "A candle from cleaned-up water."
- "Removes nitrogen and phosphorus from the water" *(AECOM/PACE-validated at bench scale — say "bench-scale validated" if pressed).*
- "Solar-grown." (True if grown on sunlight.)

**Hold off until GC-MS confirms (and some, maybe never):**
- "Paraffin" on a label → say **"algae-derived wax"** until the chemistry is typed.
- "Diesel," "biofuel," "fuel-grade," any BTU/EROI number, "carbon-negative."
- "Patented" — the patents behind this project are expired and don't cover the cavitation nozzle specifically (see `systems/science.md` and `systems/_validation-physics.md` for the detail).
- "Ocean," "autonomous," "AI," "Sea State 7," "19:1" — those describe the long-term vision, not the current, testable machine.

**The value ladder (why small is profitable):**
free pond scum → cleaned water (a paid remediation service) → algae wax (~$0.50–0.68/lb, *unconfirmed estimate*) → artisan candles ($25–50/lb retail, *market estimate*). The margin lives in the candle, not the gallon.

---

## 4. Recommended next tests (the cheapest things that answer the open questions)

These are the three lab tests that would turn "best guess" into "known," using the Tier-1 rig above:

- **GC-MS + ASTM D86 (~$500):** the fuel-vs-wax answer. Three outcomes — genuine cracking (a real breakthrough, less likely per the analysis above), intact lipid/extraction (a real, modest, sellable product — the likely outcome), or a hydrogenation ghost (rules out the fuel story). Either way, this settles what to call the product.
- **Wattmeter + D240 calorimetry on one continuous solar-grown run (~$2–4k):** the real energy return on investment (EROI), measured rather than estimated.
- **Metered pass-count assay (~$1k):** turns the never-measured "3% conversion per pass" claim into an actual curve.

None of this requires anything beyond the bench rig in §2 and a lab that can run standard fuel-chemistry assays.

---

*Bottom line: the ocean-diesel-robot claim, as originally framed, doesn't hold up yet — but a smaller, honest version works today, and that version (cleaned water + algae wax + candles) is robust to every open science question because it never depended on the answers. The three lab tests above are the cheapest way to convert "best guess" into a number.*
