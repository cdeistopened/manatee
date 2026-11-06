# Independent Energy-Balance Audit — Mobula / EVIE-2c

*Validation pass for the Solaris Cybernetics / Barsoom "Mobula" due diligence. Role: independent energy-balance auditor. 2026-06-17.*
*Sources read: `LVKNprocess.txt`, `FINANCIAL_SUMMARY.md`, `SCIENCE_BASIS.md`, `SCIENCE-DUE-DILIGENCE.md`, `NEWB E A R -PelagosOceanics(R).md` (2014 business plan), `SC1aecom1report2.md` (AECOM/PACE), `M20 Production-Revenue Estimates.csv`, and the energy/science/entropy dossiers.*

---

## TL;DR (for a technical-but-skeptical reader)

1. **The "47,511 vs 3,150 vs 10 gal/day" mystery is solved, and the prior dossiers misread it.** 47,511 lb/day is **not biomass** — it is the business plan's nameplate figure for **S3 *fuel*** output of one M20 Mobula: `5.62 lb fuel/ft³/day × 8,460 ft³ = 47,545 lb/day`. At the fuel's own measured density (~7.35 lb/gal) that is **~6,460 gal/day**, which the plan rounds/caps to **~10,000 gal per multi-day trip**. The "3,150 gal/day" is an *artifact of the January reviewer's own arithmetic error* (he treated the 47,511 lb as low-grade biomass at 8,400 BTU/lb). And "10 gal/day" is a different object entirely: a single small *land prototype*. So there are not three contradictory production numbers — there is **one wildly optimistic fleet-fuel number, one arithmetic ghost, and one real prototype number**, quoted without labels.

2. **The defensible EROI is positive but nowhere near the headline.** The inventor's 5.34%-cost / **~19:1 EROI** counts only ideal pump-acceleration work. A complete, honest boundary (pump losses + cracking enthalpy + dewatering + the 14-hour LED photoperiod + electrolysis) collapses it. **Best independent estimate: EROI ≈ 5–8:1 *if and only if* growth is sun-driven; EROI < 1 (net-negative) for any unit that runs LED grow-lights as a primary light source.** The whole bet rides on "is the light free?"

3. **The one number that would settle it has never been measured:** a wattmeter on the pump bus + a bomb calorimeter on the fuel output of a single continuous run. The closest real datapoint (AECOM/PACE: 5 gal processed on 37 Wh) is a *remediation/skim* run, not a full conversion, so it cannot be used as the EROI.

---

## 1. The keystone claim, re-derived line by line (`LVKNprocess.txt`)

| Step | Inventor's value | Audit |
|---|---|---|
| Accelerate 1 gal to 100 ft/s | head H = V²/2g = 100²/64.4 = **155.3 ft** | Arithmetic correct. |
| Ideal pump power | hp = Q·H/3960 = 1·155.3/3960 = **0.039 hp** | Correct. |
| At 65% efficiency | 0.039/0.65 ≈ 0.06 hp = **204.84 BTU/gal-pass** | Correct *as pump-shaft work only*. Note: text says "0.039/0.35" (typo) but lands on the right number. |
| Conversion/pass | **3%** | **Unmeasured. The single most load-bearing number in the project.** Basis: a Ball-jar photo showing a ~1/8" layer on 3-5/8" of liquid ("3 percent"). That is a stratification observation, not a per-pass mass balance. |
| Energy/gal *converted* | 204.84 / 0.03 = **6,828 BTU** | Correct *given* 3%/pass. ~33 passes/gal. |
| Output density | **127,000 BTU/gal** | Anchored to a real assay: D240 measured **134,258 BTU/gal**, so 127,000 is conservative. ✓ |
| **Net cost** | 6,828 / 127,000 = **5.34%** → **EROI 18.6:1** | Arithmetically self-consistent; **boundary is drawn at the most favorable possible place.** |

**What the 5.34% boundary silently omits:**
- **Pump/motor real losses** beyond the 65% factor (12 VDC motor + abrasive-slurry duty + tight multi-bore nozzle recirculation).
- **The cracking enthalpy itself** — energy to bring entrained water to supercritical conditions. The inventor argues this is "adiabatic / recovered" (AECOM letter calls cavitation "thermodynamically reversible"). **That is false as stated:** cavitation is the textbook dissipative, entropy-*generating* process. *Some* collapse heat genuinely stays in-fluid and aids the crack (partial recovery is real), but "reversible" is Second-Law-loose marketing.
- **Dewatering / harvest / skimmer pumps.**
- **The 14-hour LED photoperiod** (`SCIENCE_BASIS.md`) — the elephant (Section 3).
- **Electrolysis for the "hydrogenation" step** (process diagram step 2) — ~50 kWh/kg H₂, entirely unbudgeted.

**Independent anchor:** peer-reviewed hydrodynamic-cavitation lipid-disruption work puts cell-disruption energy at **~3 MJ/kg ≈ ~13% of biomass energy** — ~2.4× the inventor's 5.34%, and that's *just the disruption step*, before lighting. So the honest cavitation-only cost is **~10–20% of output (EROI 5–10:1)**, not 5%.

---

## 2. Production-number reconciliation (the credibility wound, resolved)

**The numbers, traced to source:**

| Figure | Source | What it actually is |
|---|---|---|
| **5.62 lb/ft³/day** | 2014 business plan; `ENVIRONMENTAL_CONTROL.md` | Claimed **fuel** yield per ft³ of growth chamber |
| **8,460 ft³** | 2014 business plan | M20 Mobula growth-chamber volume |
| **47,511 lb/day** | `NEWB E A R` plan + `SCIENCE-DUE-DILIGENCE.md` | = 5.62 × 8,460 ≈ 47,545. **Nameplate S3 *fuel* mass/day.** (×0.85 utilization ≈ 40,400 lb/day) |
| **~10,000 gal/trip** | 2014 plan | 47,511 lb ÷ ~7.35 lb/gal ≈ 6,460 gal/day → "up to 10,000 gal" over a **1–3 day trip**. Internally consistent with 47,511 lb/day. |
| **3,150 gal/day** | `SCIENCE-DUE-DILIGENCE.md` (Jan 2026) | **Reviewer artifact.** He treated 47,511 lb as *biomass* @ 8,400 BTU/lb → 399 M BTU ÷ 127,000 = 3,150. This double-counts a conversion that already happened. **Do not propagate this number.** |
| **10 gal/day** | Kickstarter / land unit | A *single small land prototype*, not a Mobula. ~130× below the fleet-unit figure because it is a different machine at a different scale. |
| **160 gal/mo (~5 gal/day)** | `FINANCIAL_SUMMARY.md` "conservative" | Prototype-class unit. |
| **172–225 gal/day** | `M20 Production-Revenue Estimates.csv` | Mid-tier spreadsheet model (volume × %algae × doubling). Between prototype and the 6,460 figure. |

**Diagnosis (corrects the entropy dossier):** the spread is **mixed denominators *and* one propagated arithmetic error**, not fabrication of any single number. The biology, not the reactor, is the real throttle: at a realistic 1–3% photosynthetic efficiency and area-limited growth, **the low end (single unit, low-tens-of-gallons/day) is the only physically defensible anchor.** The 5.62 lb-fuel/ft³/day yield requires the disputed 90–120 min doubling and is ~12–90× above demonstrated photobioreactor performance — so the 47,511 lb/day fuel figure is best read as a **theoretical ceiling, not a throughput.**

> **One-line fix for the deck:** state every production number against a single basis — *"X gal/day for a named unit of Y ft³ at Z% utilization, sun-driven."* Until then, every downstream financial ($32.1M Yr-3 revenue, 57% EBITDA) is unanchored.

---

## 3. The decisive variable: is the light free?

The entire EROI verdict pivots on whether photosynthesis is **solar** (free, Second-Law-clean — the sun is the entropy source) or **LED-supplemented** (a grid/onboard electrical load that competes with everything).

`SCIENCE_BASIS.md` specifies a **simulated 14-hour day using high-spectrum LEDs**. Cost of that, at standard horticultural density:

| Grow area | LED density | 14 h load | As energy |
|---|---|---|---|
| 100 ft² | 20 W/ft² | 28 kWh/day | 0.10 M BTU/day |
| 150 ft² | 40 W/ft² | 84 kWh/day | 0.29 M BTU/day |

A **10 gal/day** prototype's fuel output is only **1.27 M BTU/day**. So LED lighting alone is **8–23% of fuel energy** at that scale — and for any smaller/denser tank unit, **LED lighting can exceed the fuel's energy content, flipping EROI below 1.**

**Resolution:** on the *open ocean*, growth should be ~100% solar through the Lexan dome, and 14 h LED supplementation is fantasy (no generation budget supports it — see §4). On *land/tank* prototypes, LEDs likely dominate and the system is plausibly net-negative. **The EROI is therefore not one number — it is two regimes**, and the documents never say which one any given figure belongs to.

---

## 4. Generation vs. load — does the autonomous power budget close? (NO)

From the BOMs: **~400W nameplate turbine + 45W panel.** Realistic marine average:
- Turbine at 5–6 m/s mean (vs 10–12.5 m/s nameplate; wind power ∝ V³): **~30–80 W avg.**
- 45W panel after marine derating + night: **~5–7 W avg.**
- Seebeck nozzle-heat scavenger (~5–8% TEG efficiency): **watts, a rounding error.**
- **Total generation ≈ 50–150 W avg ≈ 2–3.6 kWh/day.**

**Load (conservative):** grow lights 28–84 kWh/day *alone*, + 370W cavitation pump (~8.9 kWh/day continuous) + 2× Minnkota thrusters + bubblers + electrolyzer.

**Gap ≈ 10–30×.** The autonomous *electrical* budget does not close by an order of magnitude. The only reason the 2015 prototype "worked": it ran a **~7.5 W (1/100 hp) pump**, a token panel/turbine, **sunlight not LED**, in freshwater, producing wax slowly. The hard loads were never run.

---

## 5. Independent EROI estimate (with assumptions stated)

| Boundary | Cost as % of fuel energy | EROI | Verdict |
|---|---|---|---|
| Inventor (pump-accel only, 3%/pass) | 5.34% | **18.6:1** | Optimistic; favorable boundary |
| + real pump losses + cracking enthalpy | ~10–13% | **8–10:1** | Plausible, sun-driven |
| + dewatering + controls + pass losses | ~13–20% | **5–8:1** | **My central estimate, sun-driven** |
| + 14 h LED photoperiod (tank/land unit) | 50–110%+ | **<1:1** | Net-negative |
| + onboard electrolysis (hydrogenation) | adds large term | worse | Unbudgeted |

**Stated EROI for the deck:** **~5–8:1, contingent on sun-driven growth and a closed-loop bench measurement that has never been performed.** Not a free-energy claim — the sun pays the chemical-energy bill — but the headline 19:1 is **~3× too rosy.** The system is *probably* energy-positive at order-of-magnitude (the diesel-grade output + the 37 Wh/5 gal datapoint both point positive), but "probably positive" is the honest ceiling of the current evidence.

**Why the AECOM datapoint is NOT the EROI:** `SC1aecom1report2.md` reports 5 gal processed on **37 Wh** (= 126 BTU total, ~25 BTU/gal-throughput) — *lower* than even one pump pass (204.84 BTU/gal), confirming it was a **low-pass remediation/skim** (paraffin recovery + N/P reduction), not full conversion of 5 gal *into* fuel. It validates that the reactor runs cheaply and makes paraffin with no additives — genuinely the strongest physical evidence in the corpus — but it does not close the conversion EROI.

---

## 6. Break-even fuel price

Unit cost = **$38,545** (M20, `FINANCIAL_SUMMARY.md`). Capex amortized over 5 yr = $7,709/yr; opex at the inventor's claimed $0.60/gal:

| Output regime | gal/yr | Break-even price |
|---|---|---|
| **5 gal/day** (conservative prototype, 160 gal/mo) | 1,825 | **~$4.82/gal** |
| **172 gal/day** (M20 CSV mid) | 62,780 | **~$0.72/gal** |
| **225 gal/day** (M20 CSV high) | 82,125 | **~$0.69/gal** |

**Reading:** the plan's "$0.60/gal all-in" and "$2.25/gal sale" economics **only work at the high-throughput (hundreds of gal/day) regime** — i.e., the regime that depends on the unverified 5.62 lb/ft³/day yield and sun-driven growth. **At the only demonstrated output (≈5 gal/day) the unit needs ~$4.82/gal just to break even on capex+opex** — above the assumed $2.25 sale price, so the prototype-class machine **loses money per gallon.** The venture is viable *if* the biology scales as claimed and *if* light is free; both are unproven. (Note: even the favorable break-evens exclude marine O&M, nozzle erosion/replacement — the nozzle is a *consumable* under cavitation pitting — insurance, USCG/ABS, and hub logistics.)

---

## Key numbers (for the structured digest)

- 47,511 lb/day = 5.62 lb fuel/ft³ × 8,460 ft³ → it is **fuel**, not biomass (corrects prior reading)
- ~10,000 gal/trip ≈ 6,460 gal/day × 1.5-day trip → internally consistent with 47,511 lb/day
- "3,150 gal/day" = January-reviewer arithmetic artifact (47,511 lb mis-treated as biomass @8,400 BTU/lb)
- Inventor EROI 18.6:1 (5.34% cost); independent honest EROI ≈ 5–8:1 (sun-driven); <1:1 if LED-driven
- AECOM/PACE: 5 gal on 37 Wh (= ~25 BTU/gal) — remediation, not full-conversion EROI
- Generation ~50–150 W avg (2–3.6 kWh/day) vs LED load 28–84 kWh/day → power budget 10–30× short
- Break-even: ~$4.82/gal at 5 gal/day; ~$0.69–0.72/gal at 172–225 gal/day; sale price $2.25/gal
- Measured fuel: 134,258 BTU/gal (D240), 32.71° API — diesel-range density & heating value ✓
