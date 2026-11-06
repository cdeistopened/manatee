# The Unit Economics — It Loses Money Per Gallon at Real Scale

*Case-against deep dive #6. Solaris Cybernetics / Barsoom "Mobula / EVIE-2c" due diligence.*
*Builds on §4 (economics) and §4a/§4b (mass-balance) of `01_MASTER_DUE_DILIGENCE_v2.md` and the EROI work in `_validation-energy.md`. 2026-06-17.*

> **One-sentence thesis:** The only physical output anyone has ever measured is ~1.3–1.5 gal/day of paraffin wax in a freshwater pond, and at that output the machine needs roughly **$4.82/gal just to break even** against a **$2.25/gal** target sale price — so it **loses about $2.57 on every gallon it actually makes.** The attractive economics ($0.60/gal, $32.1M Yr-3 revenue, 57% EBITDA) exist **only** in a hundreds-to-thousands-of-gallons-per-day regime that has never been demonstrated and that the corpus itself cannot describe without contradicting itself by up to ~6,600×.

---

## 0. What this section adds to the master report

The master (§4, §4a, §4b) and the energy audit (`_validation-energy.md`) already established the headline: ~$4.82/gal break-even, the 6,600× mass-balance spread, and the EROI regime split. This section does three things they did not:

1. **Reconstructs the $4.82/gal from the actual line items** in `FINANCIAL_SUMMARY.md` and the M20 BOM — and shows where it is conservative (it is) and where the *real* number is higher (it is, materially).
2. **Reframes the whole business off the fuel price.** The fuel-sale model is structurally dead at demonstrated scale. But there is a real, price-independent business hiding underneath — **remediation paid per gallon of water treated, plus a paraffin byproduct, plus nutrient credits** — and that business does NOT need the contested cavitation-cracking physics or the unproven biology to pencil. That reframing is the most valuable thing in this document.
3. **Gives the project lead one number that decides go/no-go**, and states it three times so it cannot be missed.

Everything is labeled **DOCUMENTED** (in the corpus or a third-party source), **INFERRED** (a derivation from documented inputs, shown), or **ASSERTED** (inventor-only, never measured).

---

## 1. The denominator problem: what does this thing actually make?

You cannot do unit economics until you fix the denominator — gallons per day. The corpus offers **five** numbers for what reads as one product line, spanning ~6,600×.

| Figure | Value | Source | Status |
|---|---|---|---|
| Third-party-MEASURED reality | **~1.3–1.5 gal/day** paraffin, freshwater pond | 2015 raft; `DX5b+notes1.jpg`; AECOM bench reconfig | **DOCUMENTED** (only measured output) |
| "Conservative" prototype | **~160 gal/mo ≈ 5.3 gal/day** | `FINANCIAL_SUMMARY.md` L25; `M20_Revenue_Projected.csv` (4,800 gal/mo... see below) | ASSERTED |
| Land demonstrator | **"up to 10 gal/day"** | `SCIENCE-DUE-DILIGENCE.md` L91 | ASSERTED |
| M20 spreadsheet (high) | **225.6 gal/day** ($203K/yr) | `M20 Production-Revenue Estimates.csv` | ASSERTED (self-contradictory — §1a) |
| M20 spreadsheet (low) | **160 gal/day** (4,800 gal/mo, $164K/yr) | `M20_Revenue_Projected.csv` | ASSERTED (self-contradictory — §1a) |
| "Energy-equivalent" / nameplate | **~3,150 gal/day** (artifact) → **~6,460 gal/day** (fuel reading) | `SCIENCE-DUE-DILIGENCE.md` L97–98; `_validation-energy.md` §2 | RETIRED — model artifact |
| Business-plan target | **~10,000 gal/trip** | `FINANCIAL_SUMMARY.md` L25 | ASSERTED |

**The reconciled, defensible band (INFERRED, from standard algal-lipid mass balance on the plan's own 47,511 lb/day biomass):**

```
10% lipid:  47,511 lb × 0.10 × 0.98 / 7.3 lb/gal  ≈   638 gal/day
20% lipid:  47,511 lb × 0.20 × 0.98 / 7.3         ≈ 1,276 gal/day
50% lipid:  47,511 lb × 0.50 × 0.98 / 7.3         ≈ 3,189 gal/day
```

So **~640–1,280 gal/day at a realistic 10–20% lipid fraction** is the defensible *theoretical-ceiling* number for a full M20 — **IF** the biology grows as claimed (the disputed 90–120 min doubling, ~12–90× above demonstrated photobioreactor performance) and **IF** the light is free (see EROI regime split, §3). Neither is proven. Read ~640–1,280 gal/day as the best case the physics permits, **not** as a throughput.

**The honest two-anchor framing for the cost model:**
- **Demonstrated denominator: ~1.5 gal/day** (the only measured number).
- **Best-case ceiling denominator: ~640–1,280 gal/day** (defensible mass balance, two big unproven IFs).
- Everything between (5, 10, 160, 225) is an asserted middle the corpus cannot anchor.

### §1a — The M20 contradicts *itself* by 41% on the same unit, same day

Two saved M20 revenue models disagree on the identical machine:

- `M20 Production-Revenue Estimates.csv`: `volume 3,600 ft³ → 26,928 gal → ×1,615.7 (%algae) → ×95.2 (%biomass) → ×2.37 (doubling) = **225.6 gal/day**`, at **$2.50/gal** → $203K/yr.
- `M20_Revenue_Projected.csv`: hard-codes **4,800 gal/mo = 160 gal/day** at an implied **$2.85/gal** ($13,680 / 4,800) → $164K/yr.

The high number is driven entirely by an **unlabeled multiplier `2.37`** in the cell `gal/day = 95.2 × 2.37`. That `2.37` carries no units and no citation — it appears to be an undocumented "doubling" assumption, and it is the single most leveraged number in the entire financial model: change it and revenue moves one-for-one. **A business whose top-line is a one-cell, unlabeled multiplier is not a business; it is a spreadsheet.** (DOCUMENTED: both CSVs read directly.)

**What this means for the denominator:** even if you grant the M20 scale, you cannot tell whether the unit makes 160 or 225 gal/day, and the price floats between $2.50 and $2.85. The model is unanchored at both the volume and the price axis simultaneously.

---

## 2. Rebuilding the $4.82/gal break-even from the actual line items

The master cites ~$4.82/gal at 5 gal/day. Here is where it comes from, derived from `FINANCIAL_SUMMARY.md` and the M20 BOM in `M20_Revenue_Projected.csv` — and where the real number is worse.

### 2.1 The capital stack (DOCUMENTED, from the BOM)

The M20 "Construction Budget" totals **$38,544.96**, built from real catalog line items:

| Category | Cost | Key items (from BOM) |
|---|---|---|
| Pontoons | $4,738 | 24" PVC tubes, end caps, HDPE rod, flotation foam |
| Frame | $10,167 | fiberglass matting, 4×4 EMT, clear resin, HDPE sheet |
| Primary systems (power/thrust) | $7,580 | $4,800 wind generator, capacitors, $400 PV, 2× $850 thrusters, battery |
| A.I. / control | $400 | CPU, sensors |
| Refinery (generator/skimmer/digester) | $1,660 | skimmer, 6× pump+eductor, $600 digester, heaters, ICgen |
| **Total parts** | **$24,545** | |
| Tools & molds (non-recurring) | $5,000 | |
| Labor | $9,000 | 120 hr × $75 |
| **TOTAL UNIT COST** | **$38,545** | |

This is the only capex figure the corpus supports for a "commercial-grade" unit. (The `FINANCIAL_SUMMARY.md` rollup of $38,545 matches the BOM to the dollar — the one internally consistent number in the financials.)

### 2.2 The cost stack at 5 gal/day (INFERRED — reproducing the master's $4.82)

Capex amortized straight-line over a 5-year life, plus the inventor's own claimed $0.60/gal all-in opex:

```
Capex:   $38,545 / 5 yr                    = $7,709 / yr
Output:  5 gal/day × 365                   = 1,825 gal/yr
Capex per gallon:  $7,709 / 1,825          = $4.22 / gal
Opex (inventor's claim):                   = $0.60 / gal
─────────────────────────────────────────────────────
BREAK-EVEN:                                ≈ $4.82 / gal
```

**That is the $4.82.** It is `$4.22 capex + $0.60 opex`. Against a **$2.25/gal** sale price (`FINANCIAL_SUMMARY.md` L26, "minimum market index"), the unit **loses ~$2.57 on every gallon.** Revenue at 5 gal/day is `1,825 × $2.25 = $4,106/yr` against `$7,709` of capex amortization alone — it does not even cover the depreciation, let alone opex. (INFERRED; arithmetic shown.)

### 2.3 Why $4.82 is the *optimistic* break-even — five costs it omits

The $4.82 is built on the inventor's own inputs and is therefore charitable. The real demonstrated-scale break-even is higher because the model omits:

1. **The nozzle is a consumable, not a fixture.** Cavitation pitting erodes 316-SS; the master/Masters review put replacement at **6–18 months**. At 1.06" "5-gpd" SKU machining cost, that is a recurring capex line the $0.60/gal opex does not carry. (DOCUMENTED risk; INFERRED cost.)
2. **The opex floor of $0.60/gal is itself ASSERTED and never measured** — it predates any closed-loop test and excludes marine O&M, biofouling cleaning, and haul-out.
3. **EROI risk on lighting.** If the unit runs the spec **14-hr LED photoperiod** (`SCIENCE_BASIS.md`), the energy audit shows LED load is 8–110%+ of fuel energy — meaning at small scale you may be **buying more grid electricity than the fuel is worth**, an opex item nowhere in the $0.60. (DOCUMENTED spec; INFERRED cost.)
4. **Insurance, USCG/ABS registration for an uncrewed vessel, and hub/logistics** — flagged in `FINANCIAL_SUMMARY.md` §4 as a "strategic risk" but never priced.
5. **Capacity factor < 100%.** The 5 gal/day assumes continuous operation; seasonal algae density (the plan's #1 named risk) and weather downtime cut effective gallons, raising per-gallon capex.

**Bounded conclusion:** the *defensible* demonstrated-scale break-even is **at least $4.82/gal and realistically $6–8/gal** once nozzle replacement, marine O&M, and any LED draw are carried. Either way it is **2–3.5× the $2.25 target.** The master's $4.82 is a floor, not a midpoint.

### 2.4 Where the attractive economics live — and why they're unreachable today

Run the same capex+opex math at the high-throughput regime:

| Output regime | gal/yr | Capex/gal (5-yr) | + $0.60 opex | Break-even | vs $2.25 target |
|---|---|---|---|---|---|
| **1.5 gal/day** (measured) | 548 | $14.07 | — | **~$14.67/gal** | loses ~$12.42/gal |
| **5 gal/day** (conservative) | 1,825 | $4.22 | $0.60 | **~$4.82/gal** | loses ~$2.57/gal |
| **160 gal/day** (M20 low) | 58,400 | $0.13 | $0.60 | **~$0.73/gal** | **profits ~$1.52/gal** |
| **225 gal/day** (M20 high) | 82,125 | $0.09 | $0.60 | **~$0.69/gal** | **profits ~$1.56/gal** |
| **640 gal/day** (10% lipid ceiling) | 233,600 | $0.03 | $0.60 | **~$0.63/gal** | profits ~$1.62/gal |

(INFERRED; same $38,545 capex / 5-yr / $0.60 opex applied across regimes.)

**The economics flip from catastrophic to attractive somewhere between 5 and 160 gal/day** — a ~30× throughput gap from anything demonstrated. The entire investment thesis is a bet that you can cross that gap. The break-even is hyperbolic in output: at 1.5 gal/day the *capex alone* is ~$14/gal; the curve only bends below $2.25 once you are producing tens of gallons per day. **Note the trap:** even the favorable break-evens still assume the unmeasured $0.60 opex and exclude nozzle replacement and marine O&M, so the real profitable-regime margin is thinner than the table shows. But the *shape* of the conclusion is robust: this is a scale business or it is nothing, and scale is exactly what has never been shown.

---

## 3. The two-regime EROI tax on the fuel model (why scale alone may not save it)

Even if the biology scaled to 640–1,280 gal/day, the fuel model carries a second, independent risk the cost table above ignores: **the energy to run it.** Per `_validation-energy.md`:

- **Sun-driven growth:** honest EROI ≈ **5–8:1** (not the headline 18.6:1, which is ~3× too rosy and rests on the false "adiabatic/thermodynamically reversible" premise). Energy-positive. The fuel model *can* work.
- **LED-supplemented growth:** EROI **< 1** — net-negative. The 14-hr LED photoperiod alone is 8–110%+ of fuel energy, and the onboard generation budget (50–150 W avg) is **10–30× short** of the LED + pump + thruster load.

So the fuel business has **two gates, not one**: (a) cross the ~30× throughput gap, AND (b) do it on sunlight alone. Miss either and the fuel doesn't pencil. The cost stack in §2 is the *capital* problem; the EROI is the *operating-energy* problem. They are independent, and both must be cleared for "ocean diesel" to be a business. **This is why the fuel framing is the wrong framing.** (DOCUMENTED + INFERRED, per energy audit.)

---

## 4. The reframe: there IS a real business — and it doesn't care about the fuel price

Here is the most important move in this entire document. **Stop selling fuel. Sell remediation.** The fuel price ($2.25 vs $4.82) is the wrong axis because the strongest third-party datapoint in the whole corpus is not a fuel assay — it is a *remediation* result:

> **AECOM/PACE Labs (DOCUMENTED, third-party):** 5 gallons of Florida pond algae treated on **37 Wh**, no chemicals, paraffin formed, **nitrogen and phosphorus reduced.**

That datapoint says nothing about EROI (37 Wh / 5 gal ≈ 25 BTU/gal, *less* than one pump pass — it was a low-pass skim, not a full conversion). But it is *exactly* the proof you need for a **paid-water-treatment** business, where revenue is **per gallon of water cleaned**, and the paraffin and nutrient removal are *byproducts that lower your net cost* rather than the product you live or die on.

### 4.1 Three independent, price-independent revenue lines

**Line 1 — Remediation paid per gallon of water treated (the anchor).**
Municipalities and utilities already spend enormous sums fighting harmful algae blooms (HABs): EWG documents **$1.1B+ across 85 U.S. locations since 2010**, with **12 cities spending ~$289M on drinking-water treatment alone** ([EWG](https://www.ewg.org/research/high-cost-of-algae-blooms)). This is a budget that exists *today*, paid by buyers who are *already paying*, regardless of any fuel price. The named NJ-local comparable, **LG Sonic**, generated **~$87,800/yr in documented savings with a ~1.8-yr ROI** at one NJ reservoir (master §5) — but it *suppresses the bloom in place*, leaving biomass and nutrients in the water. Behrens' device **removes** the bloom into recoverable paraffin and pulls N and P out. **That is a categorically better remediation product, and it is sold on a budget that doesn't blink at fuel prices.** (DOCUMENTED market size; INFERRED positioning.)

**Line 2 — Paraffin byproduct (a cost offset, not a profit center).**
Bulk paraffin/slack wax runs **~$0.54–0.68/lb** in the US ([businessanalytiq](https://businessanalytiq.com/procurementanalytics/index/paraffin-wax-price-index/); North America ~$1.23/kg early 2025). At ~7.3 lb/gal, a gallon of paraffin is worth **~$3.94–4.96 as wax** — *higher than its value as $2.25 diesel.* This is the single most overlooked number in the corpus: **the wax is worth more sold as wax than burned as fuel.** It will never be a large business (the volumes are small), but as a byproduct credit it materially offsets remediation opex — and the honest "renewable candle from cleaned-up water" story (Behrens' own FAQ close) is true and chargeable. (DOCUMENTED wax price; INFERRED comparison.)

**Line 3 — Nutrient credits (an option, not a line you can underwrite).**
Water-quality trading markets pay for N and P removal in "pounds equivalent" ([PA DEP](https://www.pa.gov/agencies/dep/programs-and-services/water/clean-water/nutrient-credit-trading); [EPA](https://www.epa.gov/system/files/documents/2025-01/tools-part3-water-quality-trading.pdf)). The AECOM result already shows N and P reduction, so the mechanism qualifies in principle. **But:** these markets are thin, bilaterally negotiated, geographically fragmented (Chesapeake Bay, PA, VA), prices are unpublished and volatile, and credits in some programs expire annually. Treat nutrient credits as **upside optionality in the right watershed**, never as a load-bearing revenue line in a base-case model. (DOCUMENTED market exists; price ASSERTED-unknowable.)

### 4.2 Why the remediation business survives everything that kills the fuel business

| Killer of the fuel business | Does it kill remediation? |
|---|---|
| Cavitation-cracking physics unproven (crack vs extract vs hydrogenate) | **No.** Remediation needs the nozzle to *remove biomass + cut N/P*, which AECOM already showed. Cracking is irrelevant. |
| EROI < 1 under LED | **Mostly no.** Remediation is a *skim* (37 Wh / 5 gal); it doesn't run the heavy conversion energy budget. |
| Biology doesn't scale to 640+ gal/day | **No.** You're paid per gallon of *water* treated, not per gallon of *fuel* made. |
| Fuel price $2.25 < break-even $4.82 | **No.** Remediation revenue is set by the customer's treatment budget, not by diesel. |
| Mass-balance contradiction (6,600×) | **No.** The contradiction is entirely in *fuel-yield* figures; treated-water throughput is a different, cleaner denominator. |
| Title clouds / off-point patent | Partially — still a real legal problem, but the AECOM-anchored, correctly-scoped *new* remediation IP is the cleanest path (master §7B path 1). |

**The remediation business is the part of this venture that does not depend on a single one of the contested claims.** It is also the part with the only genuine third-party datapoint. That is not a coincidence — it is the signal.

---

## 5. The number that decides go/no-go

the project lead asked for the one number. Here it is, stated three ways so it cannot be missed.

> ## **Demonstrated-scale break-even ≈ $4.82/gal vs a $2.25/gal target — the unit loses ~$2.57 on every gallon it has ever actually produced.**

**Restated as the decision:** the fuel business is a bet that you can multiply demonstrated output by **~30–100×** (from 1.5–5 gal/day to 160–640+ gal/day) **AND** do it on free sunlight. Until a single closed-loop run proves *both* — a metered pump-bus wattmeter + D240 calorimetry at a stated gal/day under solar-only growth (the master's ~$4k Phase 1–4b) — every dollar of the **$32.1M Yr-3 / 57% EBITDA** model rests on the least-defensible figure in the corpus (the unlabeled `2.37` multiplier and the retired 3,150/10,000-gal artifacts).

**Restated as go/no-go:**
- **No-go on the fuel/"ocean diesel" thesis** at any price, today. It loses money per gallon at the only scale that exists, the scale where it wins has never been shown, and even at scale it carries an independent EROI gate it may fail.
- **Conditional-go on the remediation thesis** — paid per gallon of water treated, paraffin and nutrient removal as byproduct credits — because that business is anchored by the one real third-party result (AECOM), is priced off the customer's existing HAB budget rather than the diesel index, and survives every failure mode that kills the fuel model.

The cheapest way to convert this from opinion to decision is the master's Phase 2 test (~$2–4k): **one wattmeter + one calorimeter on one continuous run.** If you are going to spend any money on this, spend that money first. If the EROI comes back < 1 or the gal/day can't be pushed, the fuel question is closed and only the remediation question remains open.

---



1. **The fuel business is, on today's evidence, a money-loser per gallon — and your equity is attached to the patent, not the paraffin.** At the only output ever measured (~1.5 gal/day) the machine needs ~$14.67/gal to break even; even at the "conservative" 5 gal/day it needs ~$4.82/gal against a $2.25 target. The good economics ($0.69–0.73/gal) require 160–225+ gal/day, a 30–45× jump nobody has shown, gated on top of a separate sunlight-only EROI requirement. **Do not let anyone pitch the $32.1M/57%-EBITDA model without first showing one metered, calorimetered, solar-only run.** That number is built on a single unlabeled `2.37` spreadsheet cell.

2. **The real business is remediation, and it ignores the fuel price entirely.** Cities are already spending $1.1B+ on algae blooms. You get paid per gallon of *water* cleaned; the paraffin (worth *more* as wax than as diesel — ~$4/gal vs $2.25) and the N/P removal are cost-offsetting byproducts and optional nutrient credits. This business is anchored by the only real third-party datapoint you have (AECOM: 5 gal on 37 Wh, paraffin formed, N/P cut) and it survives every single thing that kills the fuel story — unproven physics, EROI risk, biology that won't scale, the mass-balance contradiction. **If there is a defensible venture here, it is "chemical-free HAB remediation that turns the bloom into wax," not "ocean diesel robot."**

3. **The one number that decides it: ~$4.82/gal break-even vs $2.25/gal target.** Spend the ~$2–4k on the wattmeter-plus-calorimeter run before anything else. If EROI ≥ 1 under solar-only growth *and* the throughput can be pushed toward the hundreds, the fuel thesis reopens. If not, the fuel thesis is dead and you redeploy the entire pitch onto remediation — where the economics never depended on the fuel price in the first place. Given your equity position, get an independent analyst to co-sign whichever way the calorimeter reads.

**Sources for external anchors:**
- [EWG — The High Cost of Algae Blooms in U.S. Waters](https://www.ewg.org/research/high-cost-of-algae-blooms) ($1.1B+ since 2010; $289M drinking-water treatment)
- [businessanalytiq — Paraffin wax price index](https://businessanalytiq.com/procurementanalytics/index/paraffin-wax-price-index/) (~$0.54–0.68/lb bulk US)
- [PA DEP — Nutrient Credit Trading](https://www.pa.gov/agencies/dep/programs-and-services/water/clean-water/nutrient-credit-trading) and [EPA — Water Quality Trading](https://www.epa.gov/system/files/documents/2025-01/tools-part3-water-quality-trading.pdf) (nutrient-credit market structure)
