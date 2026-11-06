# The 5.34% Energy-Balance Boundary Trick

*Case-against deep section — Mobula / EVIE-2c (Solaris Cybernetics / Barsoom Engineering). Prepared 2026-06-17 for the engineering review team.*
*Foundation: `01_MASTER_DUE_DILIGENCE_v2.md` §4, `_validation-energy.md`, `_validation-physics.md` #5, `energy.md`, `LVKNprocess.txt`, AECOM/PACE letter (`SC1aecom1report2.md`).*

---

## The one sentence

The headline "5.34% energy cost / ~19:1 EROI" is true arithmetic drawn around a deliberately tiny boundary — it counts **only** the ideal kinetic energy to fling one gallon of water at 100 ft/s, and silently excludes every other energy term in the machine, the largest of which (a 14-hour LED photoperiod) can be **larger than the fuel's entire energy content**. Strip the trick and the *step* is indefensible as a 5% number; but the *system*, if it grows on sunlight instead of LEDs, can still plausibly be EROI > 1. Those two facts must never be quoted in the same breath without the distinction, and the inventor's documents always quote them in the same breath.

---

## 1. Rebuilding the 5.34% line by line

Here is the entire derivation as it appears in `LVKNprocess.txt` (lines 14–32), reproduced and audited term by term. **DOCUMENTED** = lifted verbatim from the source; **INFERRED** = my arithmetic/physics on top; **ASSERTED** = the inventor states it with no measurement.

### Step 1 — The velocity-to-head conversion (Euler / Bernoulli)

> *"To induce cavitation requires a velocity of 100 feet per second if the fluid is at 150 degrees F."* (DOCUMENTED, line 16)
> *"The energy required to accelerate the flow to 100 fps is 0.06 hp/gallon or 204.84 btu. [Eulers Equation: V²/2·g = 100²/2·32.2 = 10000/64.4 = 155.28 ft = H]"* (DOCUMENTED, lines 20–21)

The first move converts a target velocity into a pressure head using the kinetic-head form of Bernoulli's equation (the inventor calls it "Euler's"):

```
H = V² / (2g) = (100 ft/s)² / (2 × 32.2 ft/s²) = 10,000 / 64.4 = 155.3 ft of head
```

**INFERRED verdict: arithmetically correct.** This is the elevation a column of the fluid would have to fall to reach 100 ft/s — i.e., the *ideal* specific energy of the moving water, nothing more. Note what it physically is: the energy to **move** a gallon, not to **transform** it. Already the boundary is set at "kinetic energy of bulk flow."

### Step 2 — Head to pump horsepower

> *"hp = Q·H/3960 = (1gal × 155.28)/3960 = 0.039 hp"* (DOCUMENTED, line 22)

The hydraulic-power rule of thumb `HP = (GPM × head_ft) / 3960` (the 3960 bundles water density and unit conversions) gives:

```
HP = (1 × 155.3) / 3960 = 0.0392 hp   (ideal, 100%-efficient pump)
```

**INFERRED verdict: correct.** 0.039 hp is the *water horsepower* — the energy delivered to the fluid, assuming a perfect pump.

### Step 3 — The efficiency fudge

> *"assume efficiency of 65% = 0.039/0.35 = 0.06 hp"* (DOCUMENTED, line 23)

Here is the first tell. The text **says** 65% efficiency but **divides by 0.35** (which is a 35% efficiency, the reciprocal slip-up) — and yet lands on 0.06, which is what you get dividing by ~0.65:

```
0.039 / 0.65 = 0.060 hp   ✓ (this is what 65% efficiency actually gives)
0.039 / 0.35 = 0.111 hp   ✗ (what the written "÷0.35" would give)
```

So the *number* (0.06 hp) is consistent with 65% efficiency; the *written formula* (÷0.35) is a typo. **INFERRED verdict: the result is right, but the document is internally contradictory** — a documentation-control tell that recurs across the corpus (cf. "306 stainless," "absolute zero pressure"). Crucially, **65% is the only inefficiency the entire balance ever credits.** Everything downstream treats the pump as the sole loss in the system.

### Step 4 — Horsepower to BTU per gallon-pass

> *"0.06 hp/gallon or 204.84 btu … 1hp = 2544 BTU"* (DOCUMENTED, lines 20, 27)

```
0.06 hp × ? = 204.84 BTU
```

This only works if the "hp" is implicitly **hp·hour** (the inventor is treating one gallon-pass as taking one hour of that power, or equivalently folding a time basis into the constant). Using 1 hp·h = 2544 BTU:

```
0.0805 hp × 2544 = 204.8 BTU   →  back-solving, the figure assumes ~0.0805 hp·h, not 0.06
```

**INFERRED verdict: the unit chain is muddy** — 0.06 hp does not become 204.84 BTU without a hidden hp-hour time basis that is never stated. The number 204.84 BTU/gal-pass is best read as "the asserted shaft energy to drive one gallon through the venturi once." Treat 204.84 BTU/gal-pass as the inventor's stake in the ground; it is **the most favorable possible reading** of the pump work and we will grant it for the rest of the audit.

### Step 5 — The 3%-per-pass divisor (the load-bearing assumption)

> *"Each pass through the venturi converts 3% of the fluid. … Therefore it requires 204.84/0.03 or 6828 btu."* (DOCUMENTED, lines 26, 28)

```
204.84 BTU/gal-pass ÷ 0.03 conversion/pass = 6,828 BTU per gallon fully converted
```

This says: because each pass only converts 3% of the fluid, you must run ~33 passes (1/0.03 ≈ 33.3) to convert a whole gallon, so multiply the per-pass pump energy by 33.

**ASSERTED verdict: this 3% is the single most load-bearing number in the entire project, and it has never been measured.** Per `_validation-physics.md` #4, its only basis is a Ball-jar photograph showing a ~1/8″ layer of product on ~3-5/8″ of liquid (≈3% by depth) — a *stratification observation*, not a per-pass mass balance, not a GC yield, not a pass count. The whole EROI hangs on it, and it cuts **both ways**: if true conversion is lower than 3%/pass (entirely plausible for a stochastic cavitation process), the divisor grows and the energy cost rises proportionally. At 1%/pass the cost **triples**.

### Step 6 — Versus the output heating value

> *"Based on lab tests, the resulting fluid contains 127,000 btu/gallon. Thus the venturi reduces the conversion energy requirement to 5.34% of the energy produced."* (DOCUMENTED, lines 30–32)

```
6,828 BTU in / 127,000 BTU out = 0.05376 = 5.34%
→  EROI = 127,000 / 6,828 = 18.6 : 1
```

**INFERRED verdict: arithmetic is self-consistent, and the 127,000 is real and conservative.** The 2012 ASTM D240 assay (`BEARfuelTest1.pdf`) measured **134,258 BTU/gal**; 127,000 understates the measured output by ~5%, so the *denominator* is the one honest, lab-anchored number in the whole chain. The problem is entirely in the *numerator*.

### What the 5.34% boundary actually encloses

| Term included in 6,828 BTU | Term excluded |
|---|---|
| Ideal kinetic energy to accelerate water to 100 ft/s | Latent heat to actually vaporize/cavitate the fluid |
| A single 65% pump-efficiency factor | Real 12 VDC motor + drive + recirculation losses |
| (nothing else) | Dewatering / DAF / harvest |
| | Controls, sensors, bubblers, parasitics |
| | Electrolysis for the hydrogenation step |
| | **The 14-hour LED photoperiod (the elephant)** |

The boundary is drawn **exactly at the edge of the pump shaft and nowhere else.** That is the trick. It is not arithmetic fraud — every number inside the box is roughly right — it is **boundary fraud**: the box is drawn around the one term that is small and excludes the terms that are large.

---

## 2. Enumerating every omitted term (order-of-magnitude)

To put all terms on one ruler, the reference quantity is **one gallon of finished fuel = 127,000 BTU out.** Below, each omitted energy term is expressed as BTU per gallon of fuel and as a percentage of that 127,000. (1 kWh = 3,412 BTU; water = 8.34 lb/gal; latent heat of vaporization ≈ 970 BTU/lb; sources cited in §7.)

### (a) Latent heat to actually cavitate

Cavitation means flashing a fraction of the water to vapor. The inventor's own narrative says cavities form and collapse; forming them costs the **latent heat of vaporization**, ~970 BTU/lb of water vaporized (2.26 MJ/kg). Even if only the converted 3%/pass fraction is vaporized and most collapse heat is recovered in-fluid, consider the order of magnitude:

```
If 3% of 8.34 lb/gal is vaporized per pass and NOT recovered:
  0.03 × 8.34 lb × 970 BTU/lb = 243 BTU/gal-pass
```

That is **larger than the 204.84 BTU/gal-pass pump term the whole balance is built on.** The inventor's escape hatch is "the process is adiabatic / reversible, so this energy is recovered" (the AECOM claim, demolished in §5). To the extent collapse heat genuinely stays in the warm recirculating slurry, *partial* recovery is real and this term shrinks — but it is **never zero**, and it is **never accounted.** Honest allowance: **2–8% of output** depending on recovery fraction. **INFERRED.**

### (b) Real pump + motor + drive inefficiency

The balance credits one 65% pump-efficiency factor. The actual drivetrain is a **1/2 hp 12 VDC motor** driving a **300 psi × 10 gpm pressure-washer pump** (JT-1 BOM) pushing **abrasive algae slurry** through a tight multi-bore cavitating nozzle, recirculated ~33 times. Realistic wire-to-water efficiency of a small 12 VDC motor + pump under abrasive duty is **35–50%**, not 65%, and the recirculation plumbing adds friction losses on every one of the ~33 passes that the model sets to zero.

```
Correcting 65% → 45% raises the pump term:
  204.84 × (0.65/0.45) = 296 BTU/gal-pass
  ÷ 0.03 = 9,860 BTU/gal  (vs 6,828)  →  +24% to the numerator on its own
```

Honest allowance: the pump term alone is likely **7–8% of output**, not 5.34%, before any other term. **INFERRED.**

### (c) Dewatering / DAF / harvest

Before slurry enters the nozzle it must be concentrated from a dilute pond/ocean suspension (algae grow at ~0.5–2 g/L) to something processable. Mechanical harvesting — dissolved air flotation, flocculation, centrifugation — costs **1–8 kWh/m³** of processed water (peer-reviewed range, §7), or roughly **0.3–2 kWh per kg dry biomass.** Per gallon of fuel:

```
Even at the low end, concentrating the water for ~1 gal fuel:
  ~1 kWh/m³ × (water volume per gal fuel) — order 1,000s of BTU/gal
  1 kWh = 3,412 BTU = 2.7% of 127,000 just for the cheapest single dewatering step
```

Honest allowance: **3–10% of output**, highly dependent on starting concentration. The AECOM test sidestepped this by using *already-bloomed* dense algae and "a simple filter" (`SC1aecom1report2.md` line 100) — i.e., it deleted the dewatering term rather than measuring it. **INFERRED / DOCUMENTED omission.**

### (d) Controls, bubblers, sensors, parasitics

The VBShdl BOM lists a Super Cricket controller, 6× SSR-100 relays, light sensors, an LED-lamp driver, aerators/bubblers. Continuous aeration of a photobioreactor alone runs **0.5–2 kWh/m³/day** in the literature. These are small per gallon but **non-zero and continuous (24h)**, unlike the pump. Honest allowance: **1–4% of output.** **INFERRED.**

### (e) The deleted electrolysis / hydrogenation step

The fuel pathway (`9x9HVO_process.txt`, "HVO-style" hydrotreating) requires **hydrogen** to upgrade raw bio-oil to stable diesel — that is what the onboard `Electrolyzer.skp` is for. Electrolysis costs **50–55 kWh/kg H₂** in practice (39.4 kWh/kg is the thermodynamic floor; §7). HVO/hydrotreating consumes very roughly **~0.03–0.05 kg H₂ per kg of oil upgraded**:

```
0.04 kg H₂/kg oil × 52 kWh/kg H₂ = 2.1 kWh/kg oil
  fuel ≈ 7.35 lb/gal = 3.33 kg/gal
  2.1 kWh/kg × 3.33 kg = 7.0 kWh/gal = 23,900 BTU/gal = 18.8% of output
```

If the process truly hydrogenates onboard, **the electrolysis term alone (~19% of output) is larger than the entire claimed 5.34% balance**, and it is **completely absent** from `LVKNprocess.txt`. Either the process does not actually hydrogenate (and the "diesel" is raw cracked/extracted lipid — the provenance problem in `_validation-physics.md` #6), or it does and the energy balance is off by a factor of ~4 from this term alone. Honest allowance: **0% if hydrogenation is skipped, ~15–20% if it is real.** **INFERRED / DOCUMENTED omission.**

### (f) The dominant term — the 14-hour LED photoperiod

`SCIENCE_BASIS.md` specifies a **simulated 14-hour day using high-spectrum LEDs.** Horticultural LED density is **20–40 W/ft²** (§7). The energy to *grow* the algae is the energy that becomes the fuel's chemical content — if it comes from LEDs, it must be counted; if it comes from the sun, it is free. This is the whole ballgame.

```
Modest 150 ft² lit growth area at 40 W/ft² for 14 h:
  150 × 40 = 6,000 W = 6 kW × 14 h = 84 kWh/day = 287 M BTU/day

A 10 gal/day prototype produces only:
  10 gal × 127,000 BTU = 1.27 M BTU/day

LED energy as % of fuel energy:
  Even 100 ft² at 20 W/ft²: 2 kW × 14 h = 28 kWh/day = 95,500 BTU
    per gal at 10 gal/day = 9,550 BTU/gal = 7.5% of output (best case)
  At 150 ft²/40 W: 84 kWh/day = 286,600 BTU ÷ 10 gal = 28,660 BTU/gal = 22.6% of output
  At smaller/denser tank units: LED energy EXCEEDS 127,000 BTU/gal → EROI < 1
```

**Honest allowance: 8% to >100% of output, depending entirely on whether the light is solar or electric.** This single omitted term can be **20× the size of the term the balance actually counts.** **DOCUMENTED omission of an asserted (`SCIENCE_BASIS.md`) load.**

### The omission ledger

| Omitted term | BTU/gal (order) | % of 127,000 output |
|---|---|---|
| (a) Latent heat to cavitate (net of recovery) | 2,500–10,000 | 2–8% |
| (b) Real pump/motor losses beyond the 65% credit | +3,000 over baseline | raises pump term to 7–8% |
| (c) Dewatering / DAF / harvest | 3,800–13,000 | 3–10% |
| (d) Controls / bubblers / parasitics | 1,300–5,000 | 1–4% |
| (e) Electrolysis (if hydrogenation real) | 0 or ~24,000 | 0% or 15–20% |
| (f) **14-h LED photoperiod** | 9,500 to **>127,000** | **8% to >100%** |
| **Inventor's counted term (pump only)** | **6,828** | **5.34%** |

Read the table top to bottom: the inventor counted the *smallest* line and the one labeled "the elephant" is the *largest*, and can be larger than the entire output.

---

## 3. The honest EROI range

The master report states **13–20% of output (EROI ≈ 5–8:1), sun-driven.** I **defend and slightly refine** that, splitting it explicitly by the only variable that matters — the light source.

### Sun-driven regime (open ocean, growth through the Lexan dome)

Sum the non-lighting terms (lighting is free; the sun is the entropy source):

```
Pump (corrected, b):        ~8%
Latent heat net (a):        ~4%
Dewatering (c):             ~5%
Controls/parasitics (d):    ~2%
Electrolysis (e):           0% if no hydrogenation; +18% if real
                            -----
Subtotal, no hydrogenation: ~19% of output   →  EROI ≈ 5.3 : 1
Subtotal, with hydrogenation: ~37%            →  EROI ≈ 2.7 : 1
```

**Refined central estimate: EROI ≈ 5–8:1 if no onboard hydrogenation and growth is solar; ≈ 2.5–3:1 if onboard electrolysis is real.** This **confirms the master's 13–20% band** for the no-hydrogenation case and **extends it downward** for the hydrogenation case the master under-weighted. Either way the headline 18.6:1 is **~3× to ~7× too rosy.**

The honest independent cross-check from `_validation-energy.md` holds: peer-reviewed **hydrodynamic-cavitation lipid-disruption work puts cell disruption alone at ~3 MJ/kg ≈ ~13% of biomass energy** — already ~2.4× the inventor's 5.34%, and that is *only* the disruption step. So even a literature floor refuses to credit 5.34%.

### LED-driven regime (land/tank prototype)

Add term (f). At any realistic LED density the lighting term is 8% to >100% of output by itself:

```
Best case (100 ft², 20 W/ft², 10 gal/day): +7.5% → total ~26% → EROI ≈ 3.8:1
Typical (150 ft², 40 W/ft²):               +22.6% → total ~41% → EROI ≈ 2.4:1
Dense small tank:                          LED alone > output → EROI < 1 (NET-NEGATIVE)
```

**The flip is real and arithmetic.** For a compact, densely-lit tank unit, the grow lights consume more electricity than the fuel will ever release. Such a unit is a **net energy sink** — it destroys energy to make fuel.

### The EROI is not one number — it is two regimes

| Regime | What pays for the light | Honest EROI |
|---|---|---|
| Open ocean, solar through dome, no onboard H₂ | The sun (free) | **~5–8:1** |
| Open ocean, solar, with onboard electrolysis | Sun + a big electrical sink | **~2.5–3:1** |
| Land/tank, LED-grown | The grid / onboard generation | **~1–4:1, often < 1 (net-negative)** |

The documents **never label which regime a given figure belongs to.** That ambiguity is the heart of the trick.

---

## 4. Onboard generation vs. load — the budget is 10–30× short

Even granting sun-driven growth, the *electrical* loads (pump, thrusters, controls, and any LED supplementation) must be met by onboard generation. They are not. From the BOMs:

**Generation (nameplate vs. realistic marine average):**

```
400 W Air-X wind turbine: nameplate at 10–12.5 m/s.
  Wind power ∝ V³. At a realistic open-water mean of 5–6 m/s:
  (5.5/11)³ = 0.125 → ~12.5% of nameplate ≈ 50 W, derated to ~30–80 W avg.
45 W PV panel: marine derating + fouling + night → ~5–7 W avg.
Seebeck nozzle TEG (~5–8% eff): watts — a rounding error.
─────────────────────────────────────────────
Total realistic generation ≈ 50–150 W avg ≈ 1.2–3.6 kWh/day.
```

**Load (continuous):**

```
370 W cavitation pump, continuous:  ~8.9 kWh/day  ← already 2.5–7× total generation
2× Minnkota 55# thrusters, intermittent: 0.2–1.2 kW when on
Bubblers, controls, sensors:        ~0.5–2 kWh/day
LED grow (if used):                 28–84 kWh/day  ← 8–70× total generation
Electrolyzer (if used):             large
─────────────────────────────────────────────
Load (pump alone): ~8.9 kWh/day vs ~2.4 kWh/day generation = 3.7× short
Load (with LED):   30–90 kWh/day vs ~2.4 kWh/day generation = 12–37× short
```

**The autonomous electrical budget does not close by an order of magnitude — 10–30× — and the pump alone overruns generation ~4×.** The only reason the 2015 farm-pond prototype "worked" (`DX5b+notes1.jpg`): it ran a **~7.5 W (1/100 hp) pump** — *fifty times smaller* than the BOM's 1/2 hp pump — on a token panel/turbine, in **sunlight not LED**, in **freshwater**, producing wax slowly. The hard loads were never run simultaneously. **The closed power budget exists nowhere in the corpus** (per `energy.md` red flag #1). For an "energy-autonomous" robot, the absence of a single generated-vs-consumed watt-hour table is itself the finding.

---

## 5. Why "adiabatic / thermodynamically reversible / energy recovered" is false

The AECOM/PACE letter (`SC1aecom1report2.md`, line 98) states:

> *"The paraffin is formed by Hydrous Pyrolysis. … This is achieved … via controlled, directed cavitation which produces the required pressure and temperatures but is an **adiabatic (thermo-dynamically reversible) process. Thus much of the energy used in the conversion is recovered.**"* (DOCUMENTED)

This sentence is the linchpin that lets the inventor *delete* the latent-heat term (a), and it is wrong on two distinct counts.

**(1) "Adiabatic" and "reversible" are not synonyms — the letter conflates them.** Adiabatic means *no heat crosses the boundary* (Q = 0). Reversible means *no entropy is generated* (ΔS_universe = 0). A process can be adiabatic and wildly irreversible — a hand grenade in a sealed vacuum chamber is adiabatic and about as far from reversible as physics gets. Cavitation collapse is exactly that: it may be locally adiabatic (the collapse is too fast for heat to conduct away in picoseconds), but it is **violently irreversible.**

**(2) Cavitation collapse is the textbook entropy-generating, dissipative event.** A collapsing bubble emits a **shock wave** (acoustic energy radiated away and dissipated as heat), **broadband light** (sonoluminescence — energy leaving as photons), and drives **chemical bond-breaking** (radical formation). Each of these is an irreversible export of organized energy into disorder. The peer-reviewed cavitation literature (`_validation-physics.md` #2/#7: arXiv 2412.05471; PMC7786618; PMC8960979) describes collapse zones reaching ~5,000–15,000 K and emitting megabar-class shocks — the signature of a maximally dissipative process, not a reversible one. **You cannot run a cavitation cycle backward and recover the shock wave and the UV flash.** By the Second Law, the work required to create the cavity is **never** fully recovered when it collapses; the difference is exported as entropy.

**What survives:** *partial in-fluid heat recovery* is genuinely real and defensible. The collapse heat that stays in the warm recirculating slurry reduces the energy needed to keep the fluid at 150 °F — a real, modest saving. That is the kernel of truth the letter inflates into "thermodynamically reversible." The honest statement is: *"some collapse heat is retained in the working fluid, partially offsetting reheat losses."* The dishonest statement is the one in the letter: *"thermodynamically reversible, thus much of the energy is recovered,"* which is used to zero out the cavitation enthalpy entirely.

**Why this matters for the boundary trick:** the "reversible" claim is precisely the rhetorical device that lets term (a) — latent heat to cavitate, ~2–8% of output — vanish from the 5.34% balance. It is not a measurement; it is a Second-Law-loose assertion doing load-bearing work in the economics.

---

## 6. The crisp distinction the project lead can wield


> **The STEP-level claim is indefensible. The SYSTEM-level claim can survive.**
>
> - **"The cavitation conversion costs only 5.34% of the fuel's energy (EROI 19:1)"** is a *boundary trick* — it counts only ideal pump-acceleration work and omits latent heat, real pump losses, dewatering, parasitics, electrolysis, and (dominantly) the LED photoperiod. The honest step-plus-balance-of-plant cost is **~13–37% of output (EROI ~3–8:1)**, and the "adiabatic/reversible" justification for the omission violates the Second Law. **Do not defend 5.34%.**
> - **"The whole farm is net-energy-positive"** can still be **true**, because the real energy source is **the sun** — algae build the lipid from sunlight, not from the nozzle. The nozzle is a *processor*, not a *generator*. A sun-driven Mobula that grows on daylight through its dome and skips onboard electrolysis is plausibly **EROI ≈ 5–8:1** — genuinely energy-positive, just nowhere near 19:1.
> - **The trap to refuse:** any document or pitch that quotes "5.34% / 19:1" as evidence the *system* is efficient. That number describes one term inside a process that has at least six energy terms; presenting it as the system EROI is the error. And any unit that runs **LED grow-lights** as a primary light source is plausibly **net-negative** — it makes fuel by destroying more energy than the fuel contains.

In one line for a buyer or partner: **"The fuel is real and diesel-grade; the sun-driven system can be energy-positive; but the 5.34% figure is a boundary artifact that omits the largest loads, and it must be replaced by a measured wattmeter-in/calorimeter-out EROI on one continuous run before any of the economics can be trusted."**

The one experiment that ends the argument (from `_validation-physics.md`): a **wattmeter on the pump bus + a bomb calorimeter on the output of one continuous batch run.** ~$1,500, one afternoon. It has never been done. Until it is, 5.34% is a derivation, not a measurement — and the derivation is drawn around the wrong box.

---

## 7. Sources

- Latent heat of vaporization of water ≈ 2.26 MJ/kg ≈ 970 BTU/lb; specific heat and phase-change energy: [Engineering Toolbox — Water Properties: Vaporization Heat vs. Temperature](https://www.engineeringtoolbox.com/water-properties-d_1573.html); [Geosciences LibreTexts 3.3 Latent Heat](https://geo.libretexts.org/Bookshelves/Meteorology_and_Climate_Science/Atmospheric_Processes_and_Phenomena/03:_Thermodynamics/3.03:_Latent_Heat).
- Electrolysis of water: 39.4 kWh/kg H₂ theoretical (100%), 50–55 kWh/kg practical: [Electrolysis of water — Wikipedia](https://en.wikipedia.org/wiki/Electrolysis_of_water); [WEF — Seawater electrolysis: here are the numbers](https://www.weforum.org/stories/2023/09/seawater-electrolysis-a-hydrogen-revolution-or-technological-dead-end-here-are-the-numbers/); [Carbon Commentary — rules of thumb of the hydrogen economy](https://www.carboncommentary.com/blog/2021/6/11/some-rules-of-thumb-of-the-hydrogen-economy).
- Microalgae harvesting/dewatering energy: centrifugation 1–8 kWh/m³, flocculation 0.1–6.7 kWh/m³, flotation 0.015–7.6 kWh/m³; ~0.1–0.7 kWh/kg closed systems: [Techno-economic evaluation of microalgae harvesting and dewatering systems — ScienceDirect (Algal Research, 2018)](https://www.sciencedirect.com/science/article/pii/S2211926417306677); [Harvesting of microalgae by centrifugation for biodiesel production: A review — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2211926420302642).
- LED horticultural density 20–40 W/ft²: [LED Grow Lights Depot — watts per square foot](https://www.ledgrowlightsdepot.com/blogs/blog/16326275-how-many-led-watts-are-required-per-square-foot-of-grow-space).
- Cavitation temperatures / irreversibility / shock+sonoluminescence: [Sonoluminescence — Wikipedia](https://en.wikipedia.org/wiki/Sonoluminescence); [Cavitation-bubble-temperature minireview — PMC8960979](https://pmc.ncbi.nlm.nih.gov/articles/PMC8960979/).
- Wind power ∝ V³ and AIR-X real-world derating: [Southwest Windpower AIR-X manual](https://technosun.com/descargas/SOUTHWEST-AIR-X-manual-EN.pdf).
- Primary corpus: `LVKNprocess.txt`, `SC1aecom1report2.md` (AECOM/PACE), `BEARfuelTest1.pdf` (2012 ASTM assay), `SCIENCE_BASIS.md`, JT-1 and VBShdl BOMs, `9x9HVO_process.txt`, `Electrolyzer.skp`.

---


You can be the harshest critic in the room about the **5.34% figure** and still protect the asset you hold equity in — *if* you keep the step/system distinction surgically clean. Three things to internalize:

1. **Never let "5.34% / 19:1" be quoted as the system EROI.** It is the cost of one term (ideal pump work) inside a six-term process, and it leans on an "adiabatic/reversible" claim that violates the Second Law to delete a term roughly its own size. The defensible system number is **EROI ≈ 5–8:1, sun-driven, no onboard electrolysis** — energy-positive, just 3–7× less rosy than the headline. Put *that* in any deck; it is honest and still attractive.

2. **The light source is the whole ballgame.** A Mobula that grows on **daylight through the dome** can be genuinely energy-positive. A unit that runs a **14-hour LED photoperiod** can consume more electricity in grow-lights than its fuel will ever release — a net energy sink. Every production and economic number in the corpus is unanchored until someone states which regime it belongs to. Demand that label before you defend any figure.

