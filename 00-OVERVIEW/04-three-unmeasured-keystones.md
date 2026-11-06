# The Three Never-Measured Keystones + the "3% per pass" Assumption

*Case-against deep dive — Solaris Cybernetics / Barsoom "Mobula" / EVIE-2c. Drafted 2026-06-17 by the independent due-diligence desk for the engineering review team. Builds on `01_MASTER_DUE_DILIGENCE_v2.md` §2/§4/§8, `systems/_validation-physics.md`, `systems/_validation-energy.md`, and `systems/science.md`. Does not re-derive what those establish; this extends them into the single sharpest frame: **the whole economic thesis rests on three numbers that have never been measured on the same machine in the same run, and one of those three is then divided into everything.**)*


---

## The one-paragraph version

Three things have to be true for the Mobula to be worth anything as a *fuel* machine rather than a pond-cleaning gadget: (1) the nozzle must **convert** biomass to fuel by a real mechanism — cracking, not just squeezing oil out of cells, and not a relabeled version of an electrolysis route the hardware can no longer perform; (2) the **EROI** must exceed 1 by a comfortable margin (the deck says 19:1); and (3) the output must be a real **diesel-grade distillate**, not merely "an oil of diesel-like density." **None of the three has ever been closed by an end-to-end measurement on the current rig.** Worse, the entire production and economics stack is built by *dividing pump energy by a single number — "3% conversion per pass" — that the inventor never measured.* It is an eyeball estimate off a photograph of a Ball jar. Below I show where that 3% comes from, show that it propagates multiplicatively into every dollar of projected revenue, and specify the exact instrument readings (GC-MS + ASTM D86; metered pass-count assay; wattmeter + bomb calorimeter) that would convert each keystone from ASSERTED to a number — and what each FAIL downgrades the project to.

---

## Keystone 1 — The conversion MECHANISM (crack vs. extract vs. the vestigial electrolysis/hydrogenation route)

### What is claimed

**ASSERTED** (`science.md`, `LVKNprocess.txt`, `PelagosPrcsDgmV2.jpg`): a single/double pass through a passive 316-SS multi-bore venturi causes hydrodynamic cavitation whose collapse hot-spots **"thermally depolymerize"** — i.e. *crack* — long-chain algal lipids into shorter, diesel-range hydrocarbons. No external heat, no catalyst, no methanol, no refinery. The AECOM/PACE cover letter (`SC1aecom1report2.md`, signed R. Behrens, CEO) sharpens the name: *"The paraffin is formed by **Hydrous Pyrolysis** … achieved … via controlled, directed cavitation … but is an **adiabatic (thermo-dynamically reversible) process**."*

### Why "crack vs. extract" is the whole ballgame

These are two categorically different machines wearing one description:

- **Cracking / hydrous pyrolysis** (the breakthrough claim): cavitation chemically *breaks* C–C bonds, shortening C16–C18 fatty chains into C10–C17 alkanes. If real, this is a catalyst-free, single-step replacement for the refinery, worth licensing for a great deal of money.
- **Extraction / cell disruption** (the mundane reality the literature supports): cavitation merely *ruptures the algal cell wall* and releases the lipid that was already inside. The "fuel" is then just raw algal oil — energetic, diesel-*density*, but not a diesel distillate and not a new molecule. This is a modest, real, already-commercialized niche (see literature below). It is **not** a breakthrough.

The 2012 BEAR assay (`BEARfuelTest1.pdf`) **cannot tell these two apart**, because it ran only D4052 (density) and D240 (heat of combustion). **DOCUMENTED:** 32.71° API, 134,258 BTU/gal. **A bomb calorimeter reports ~18,000 BTU/lb for cracked diesel, raw algal oil, crude, and a veg-oil/solvent blend alike** — all are hydrocarbons of similar energy density. The assay proves an *oil exists*; it is silent on *how it was made*. That silence is the entire unmeasured keystone.

### The third possibility the prior dossiers surface — the vestigial electrolysis/hydrogenation route

This is the sharpest finding in `01_MASTER_DUE_DILIGENCE_v2.md` §8e/§8 (Addenda) and it deserves elevation here. **DOCUMENTED:** two saved revisions of the process diagram differ *only* at Step 2:

- **V1:** "an electric current ruptures the cell walls and make[s] H₂" — i.e. **electrolysis**.
- **V2:** "a cavitating nozzle … separating & **hydrogenating** the lipids" — electrolysis silently swapped out for the nozzle.

Both versions keep Step 3 verbatim: "the **hydrogenated lipids** are passed through a cavitating nozzle." So the *word* "hydrogenated" survived the edit even though the only thing that could supply hydrogen — the electrolyzer — was deleted. **INFERRED (high confidence):** the cavitation-"hydrogenation" story is a **later relabeling** of an originally electrolysis-based route. This matters for three reasons:

1. **The granted patent describes the deleted route, not the surviving one.** US 7,750,494 (Behrens) claims an electrolyzer → reverse-water-gas-shift → methanation hydrocarbon system — i.e. it covers the *electrolysis* branch, **not** a cavitation lipid-cracker (`_validation-physics.md` red-flag; `science.md` Claim 6). The IP and the as-built hardware point at different machines.
2. **Neither as-built BOM carries an electrolyzer** (`01_MASTER` §8). The current hardware *cannot* perform the route the patent protects.
3. **Hydrogenation needs a hydrogen source and a catalyst.** In a passive nozzle there is neither. "Hydrogenated lipids" in Step 3 is therefore either (a) chemically meaningless as written, or (b) a fossil of the electrolysis design. `science.md` red-flag #7 flags exactly this: *"Where does the H₂ come from in a passive nozzle? Unexplained."*

### What the peer-reviewed literature does — and does NOT — support

I went to the primary literature to ground "does hydrodynamic cavitation crack biomass." The picture is unusually clean, and it cuts against the breakthrough claim while *partly rescuing* a narrower one.

**What the literature DOES support:**

- **HC is established for microalgal cell disruption and lipid extraction.** Multiple peer-reviewed studies report HC disrupting wet microalgae and releasing lipid, with disruption energy as low as **~3 MJ/kg — ~10× more efficient than sonication** ([Lee & Han, *J. Appl. Phycology* 2014](https://link.springer.com/article/10.1007/s10811-014-0483-3)), lipid yields of **25.9–99.0%** across 500–10,000 kJ/kg specific energy, and full-process figures of **~33 MJ/kg dry biomass** vs. 529 MJ/kg for high-pressure homogenization ([CEC-600-2019-015](https://www.energy.ca.gov/sites/default/files/2021-05/CEC-600-2019-015.pdf)). So cavitation *does* break algae open and release oil cheaply. **This is the "extraction" half — and it is real.**
- **HC is established as an *intensifier* of catalyzed biodiesel synthesis.** Gogate, Pandit, Mohod, Maddikeri et al. repeatedly show HC orifice/venturi reactors cut transesterification time from ~90 min (stirred) to ~20 min at >90% FAME yield ([ScienceDirect HC-biodiesel review S2666086521000916](https://www.sciencedirect.com/science/article/pii/S2666086521000916); [Springer microalgae HC-biodiesel](https://link.springer.com/article/10.1007/s11356-022-20474-w)). **But in every one of these the chemistry is still oil + alcohol + catalyst → FAME.** Cavitation is the *mixer*, not the reaction.
- **HC can assist hydrocarbon cracking/viscosity reduction — with a hydrogen donor and/or catalyst, on already-petroleum heavy oil.** The heavy-oil-upgrading literature ([*Ultrason. Sonochem.* review, PMID 31450381](https://pubmed.ncbi.nlm.nih.gov/31450381/); [RSC Adv. C8RA08087A](https://pubs.rsc.org/en/content/articlehtml/2019/ra/c8ra08087a)) shows cavitation reducing heavy-oil viscosity ~20–39% **only when tetralin/gasoline (a H-donor) or metal nanoparticles are added.** Collapse hot-spots "may activate dispersed metal nanoparticles, catalyzing cracking **or hydrogenation**." Note the word: the *real* cracking literature needs a hydrogen donor — which is precisely the deleted electrolysis branch.

**What the literature does NOT support — and this is decisive:**

> **There is no peer-reviewed precedent for catalyst-free, alcohol-free, H-donor-free hydrodynamic cavitation converting *whole wet biomass* into *finished diesel-range hydrocarbons* in a single or recirculating pass.** The cracking that the literature documents is (a) on petroleum feedstock, not biomass, and (b) requires an added hydrogen donor or catalyst. The biomass work that the literature documents is extraction and disruption, *not* cracking. The Mobula claim sits in the empty cell of that matrix.

The established route for *wet* algae remains **Hydrothermal Liquefaction (HTL): 300–350 °C, 5–22 MPa (~50–220 atm), 15–60 min residence**, yielding ~45–50 wt% biocrude that *still* needs catalytic hydrotreating before it's a fuel ([Springer HTL review](https://link.springer.com/article/10.1007/s12155-023-10615-5); [OSTI](https://www.osti.gov/servlets/purl/1848720)). HTL works because the *entire bulk* is held at supercritical-ish conditions for *minutes*. Behrens proposes to beat it with *transient sub-micron hot-spots* in a *single pass* with *no bulk heating* and *no upgrading step*. The literature does not forbid surprise — but it offers zero support, and the burden of proof sits squarely on an unrun experiment.

### A genuine counterweight (so this is honest, not a hit piece)

The AECOM/PACE result is real and is the strongest physical evidence in the corpus: **5 gallons of field algae processed on 37 Wh, no chemical additives, producing paraffin + N/P-reduced water** (`SC1aecom1report2.md`). Behrens' own framing — **"Hydrous Pyrolysis"** — is, notably, the *correct scientific term* for low-temperature water-mediated cracking (Lewan/USGS), and is more defensible than "thermal depolymerization." So the mechanism is not crank physics; it is an *under-evidenced* version of a real phenomenon. But two caveats gut its use as proof of the *fuel* claim: (a) AECOM was a **remediation/skim run**, not a full conversion — at ~25 BTU/gal-throughput it is *below even one pump pass* (204.84 BTU/gal), so almost no conversion energy went in (`_validation-energy.md` §5); and (b) "adiabatic (thermodynamically reversible)" is a **Second-Law error** — cavitation is the textbook dissipative, entropy-generating process; partial in-fluid heat recovery is real, "reversible" is marketing (`_validation-physics.md` #7).

### How you measure it, and what PASS/FAIL looks like

**Instrument: GC-MS + ASTM D86 distillation curve on the existing jar of product (~$300–800, one fuels lab, one afternoon).** Read it as a **three-way discriminator** (this is the v2 sharpening — not the binary the v1 framing implied):

| Outcome | GC-MS / D86 signature | Verdict | Downgrades to |
|---|---|---|---|
| **(a) Cracking** | Paraffinic n-alkane distribution shifted ~1 carbon *below* source fatty-acid chains (C15/C17 from C16/C18 — the **decarboxylation fingerprint**); no intact triglycerides/FAME; D86 boils in the C10–C22 diesel window | **PASS — the breakthrough is real** | Nothing. License the conversion IP (on correctly-scoped, unclouded title). |
| **(b) Extraction** | Intact triglycerides / FAME / unbroken long chains; D86 boils high/broad, not a diesel cut | **FAIL (mechanism)** | **"A solvent-free, catalyst-free algal-lipid extraction + HAB-remediation nozzle."** A real, modest niche (vs. CVAT/Hielscher/LG Sonic) — but **not** a fuel breakthrough; the 5.34%/19:1 story dies. |
| **(c) Hydrogenation signature** | Saturated/hydrogenated profile inconsistent with passive-nozzle inputs — betraying the deleted electrolysis route or an undisclosed H-source | **FAIL (provenance)** | **An undisclosed-process machine.** Triggers the patent-scope problem (494 covers electrolysis) and a representations-and-warranties landmine. |


---

## Keystone 2 — EROI (energy return on investment)

### What is claimed

**ASSERTED** (`LVKNprocess.txt` lines 20–32): net conversion energy = **5.34% of output → EROI ≈ 18.6:1**. Derivation (arithmetically self-consistent, audited line-by-line in `_validation-energy.md` §1): 204.84 BTU/gal pump-acceleration work ÷ 0.03 (the 3%/pass) = 6,828 BTU/gal converted; ÷ 127,000 BTU/gal output = 5.34%.

### Why the number is drawn at the most favorable possible boundary

The 5.34% counts **only ideal pump-shaft work to accelerate fluid to 100 ft/s.** It silently omits, by construction (full list in `_validation-physics.md` #5 and `_validation-energy.md` §1):

- Real pump/motor/recirculation losses beyond the credited 65% (12 VDC motor, abrasive-slurry duty, tight multi-bore nozzle, ~33 recirculation passes per gallon).
- The **cracking enthalpy itself** — energy to bring entrained water to supercritical conditions — hand-waved away as "adiabatic/reversible" (a Second-Law error; see Keystone 1).
- Dewatering / harvest / skimmer pumps.
- **The 14-hour LED photoperiod** (`SCIENCE_BASIS.md`) — the term that can flip EROI *negative*.
- **Electrolysis for the "hydrogenation" step** — ~50 kWh/kg H₂, entirely unbudgeted.

**Independent anchor (literature):** HC cell-disruption alone runs **~3 MJ/kg ≈ ~13% of the ~29 MJ/kg biomass energy** ([Lee & Han 2014](https://link.springer.com/article/10.1007/s10811-014-0483-3); CEC-600-2019-015) — already **~2.4× the inventor's 5.34%, for the disruption step *before* any cracking.** The honest cavitation-only cost is **~10–20% of output (EROI 5–10:1)**, not 5%.

### The decisive fork: is the light free?

`_validation-energy.md` §3 establishes the pivot, and it belongs here: EROI is **two regimes, not one number.**

- **Sun-driven (open ocean, light through the Lexan dome):** the sun pays the chemical-energy bill; EROI **~5–8:1** is defensible. Not free energy — solar energy, correctly attributed.
- **LED-supplemented (land/tank prototype):** 14 h of grow-lights = **28–84 kWh/day**, against a 10-gal/day unit's **1.27 M BTU/day** output → LED is **8–23% of fuel energy at best, and exceeds it for denser tanks → EROI < 1, net-negative.**

And the autonomous power budget **does not close**: generation ~50–150 W avg (2–3.6 kWh/day) vs. LED load alone 28–84 kWh/day → **10–30× short** (`_validation-energy.md` §4). The documents never label which regime any given figure belongs to.

### How you measure it, and what PASS/FAIL looks like

**Instrument: a wattmeter/power-logger on the pump bus (~$200) + a bomb calorimeter (ASTM D240) on the output of *one continuous batch* run on the existing 5-gal rig.** EROI = (gal × 134,258 BTU) ÷ (measured Wh-in × 3.412). This single measurement is the entire ballgame and **has never been done.** Co-gate it with a **$0-marginal-cost solar-only-vs-LED growth A/B** (`01_MASTER` §1), because lighting — not the pump — is the term that flips the sign.

| Outcome | Verdict | Downgrades to |
|---|---|---|
| Closed-loop EROI **> ~3:1 under solar-only growth** | **PASS** | Nothing — energy thesis survives (though headline 19:1 stays ~3× too rosy). |
| EROI **1–3:1** | Marginal | A thin-margin remediation device, not a fuel business; economics rest on paraffin byproduct, not energy arbitrage. |
| EROI **< 1** (any LED-primary unit, or pump losses worse than modeled) | **FAIL** | **A net-energy-negative novelty / pond-cleaner.** The "ocean diesel" story is dead; only the remediation + paraffin value remains. |


---

## Keystone 3 — Final FUEL GRADE

### What is claimed

**ASSERTED:** the output is diesel / "BIO DIESEL" (sample label on `BEARfuelTest1.pdf`), ~127,000–134,258 BTU/gal, suitable to run an engine and power the robot's own propulsion and growth lighting "with a tiny slice of its output" (`science.md`).

### What is actually DOCUMENTED vs. ASSERTED

**DOCUMENTED (the entire evidentiary basis for "diesel"):**
- D4052 API Gravity: **32.71° API** (≈ 0.862 g/mL — *in* the petroleum-diesel band of ~30–39° API, but *also* in the band of many bio-oils and blends).
- D240 Gross Heat of Combustion: **18,254 BTU/lb / 134,258 BTU/gal** (diesel/HTL-biocrude range).

**CRITICALLY ABSENT — the exact tests that define a fuel** (`science.md` Evidence; `SCIENCE_BASIS.md` admits these as a future gap):
- No **GC-MS speciation** (what molecules?)
- No **ASTM D86 distillation curve** (boiling range — is it actually a diesel cut?)
- No **cetane number** (D613 — will it ignite in a diesel engine?)
- No viscosity (D445), flash point (D93), sulfur, cloud/pour point, **FAME content** (EN 14103).

**INFERRED:** D240 + D4052 establish *"an oil of diesel-like density and heating value."* They are **physically incapable** of establishing *"a diesel-range distillate"* or *"cavitation provenance."* "It's diesel" is **ASSERTED**; "it's a diesel-density, diesel-energy oil" is **DOCUMENTED**. The gap between those two sentences is the third unmeasured keystone — and note it is settled by the **same GC-MS + D86 run** as Keystone 1. Mechanism and grade are one experiment.

### How you measure it, and what PASS/FAIL looks like

**Instrument: GC-MS + ASTM D86 distillation curve (the Keystone-1 run), plus the missing ASTM panel — cetane D613, viscosity D445, flash D93, FAME EN 14103 (~$1–2k total).**

| Outcome | Verdict | Downgrades to |
|---|---|---|
| D86 boils in the diesel window (≈180–360 °C), cetane ≥ ~40, low FAME | **PASS** | A defensible **fuel spec** — sellable as diesel/renewable diesel. |
| Boils as a heavy bio-oil / high FAME / fails cetane | **FAIL (grade)** | **"A diesel-density oil / paraffin / candle feedstock."** Market it as paraffin for pond-remediation ("renewable candle from cleaned-up water") — **never** "diesel," no ASTM/engine/marine claims (`01_MASTER` §-Kit). |


---

## The load-bearing assumption: "3% conversion per pass"

This is the number the whole project is divided by. It deserves its own dissection.

### Exactly where it comes from

**DOCUMENTED — `LVKNprocess.txt`, line 26, in full:**

> *"Each pass through the venturi converts 3% of the fluid."*

That is the entire derivation. **There is no measurement, no citation, no mass balance, no per-pass assay, no error bar.** It is stated as a given and then immediately divided into the energy budget (line 28: "Therefore it requires 204.84/0.03 or 6828 btu").

**Where the 3% actually originates (INFERRED, high confidence):** the corpus contains a product photo — `BEAR Fuel 3percent.jpg` — a **Ball jar showing a thin ~1/8-inch top layer floating on 3-5/8 inches of green liquid, labeled "3 percent"** (`science.md` Evidence; `_validation-energy.md` §1). 0.125 in ÷ ~3.7 in ≈ 3.4%. **The "3% per pass" number is an eyeball reading of the height of a floating layer in a jar.**

This is a **stratification observation, not a per-pass mass balance.** It conflates three different things:

1. **A static separation ratio** (how much floats after settling) with
2. **A per-pass conversion rate** (how much *new* fuel each trip through the nozzle makes), with
3. **A loop-level yield** (total fuel ÷ total biomass over all passes).

A jar photo can, at most, weakly support #1. The energy balance needs #2 — measured at the recirculating-loop level. **#2 has never been measured.** And #1 ≠ #2: a 3% floating layer could be the *accumulated* product of dozens of passes (consistent with low per-pass conversion), or could be lipid that was *already present* and merely *released* (extraction, not conversion — Keystone 1 again). The photo cannot distinguish these, and neither can anyone reading it.

### How the 3% multiplies into every dollar

The 3% is not a side assumption — it is a **denominator that scales the entire stack.** Trace it:

```
Energy per gallon CONVERTED   = 204.84 BTU (pump work per pass) ÷ 0.03
                              = 6,828 BTU/gal        ← implies ~33 passes/gal
Net conversion energy cost    = 6,828 ÷ 127,000 (output) = 5.34%   ← EROI 18.6:1
```

- **If the true per-pass conversion is 1% instead of 3%** (entirely plausible for a low-single-digit passive process — `_validation-physics.md` #4 explicitly notes "single-pass conversion is low"), then passes/gal triples to ~100, pump energy/gal triples to **20,484 BTU**, net cost rises to **~16%**, and **EROI falls from 18.6:1 to ~6:1** — before lighting. A 3×-optimistic 3% turns the headline EROI into the *central honest estimate*, which is the tell that the headline was tuned to the most favorable input.
- **If conversion is 0.3%**, EROI drops to **~1.9:1** on pump work alone — and any LED load pushes it net-negative.
- Conversely, the optimism compounds the *other* way on **throughput**: the production model (`M20 Production-Revenue Estimates.csv`, the 47,511 lb/day nameplate, the $32.1M Yr-3 revenue, 57% EBITDA in `FINANCIAL_SUMMARY.md`) all assume the recirculating loop *clears* biomass fast enough to hit volume. If per-pass conversion is 3× lower, the loop must run 3× longer per gallon, **cutting daily fuel output by ~3×** for the same pump duty — directly deflating every revenue line. **The 3% sits underneath both the EROI numerator-side *and* the throughput/revenue side.** One unmeasured eyeball estimate is the keystone of the keystone.

### How you measure it, and what PASS/FAIL looks like

**Instrument: a metered, closed-loop pass-count assay on the existing rig — ideally the 1.06-inch "5-gpd" bench bore that near-matches the ~1.5 gal/day reality (`01_MASTER` §-table).** Charge a known mass of feedstock; run the loop; **assay product fraction after 1, 2, 5, 10, 33 passes** (GC-MS or simple gravimetric + the Keystone-1 speciation). Mass-balance input vs. output. This is the experiment the jar photo *should have been.*

| Outcome | Verdict | Effect |
|---|---|---|
| Per-pass conversion ≈ 3% **and** rising cumulative yield is genuine *new* fuel (not released lipid) | **PASS** | The economic stack's denominator is validated; EROI/throughput math stands (subject to Keystones 1–2). |
| Per-pass conversion measurably **< 3%** | **FAIL (degree)** | EROI and daily output both deflate proportionally; re-run all economics with the measured number. |
| "Conversion" is flat across passes / matches released lipid | **FAIL (kind)** | It's **extraction/stratification, not conversion** — collapses to Keystone-1 outcome (b); the "3% per pass" was never a conversion rate at all. |


---


Strip everything to its load-bearing core:

1. **Three keystones, three never-measured claims, one lab visit.** Mechanism (Keystone 1) and grade (Keystone 3) are settled by the *same* **GC-MS + ASTM D86** run (~$500–2k). EROI (Keystone 2) needs a **wattmeter + bomb calorimeter on one continuous batch**. The "3%/pass" needs a **metered pass-count assay.** All three can run on the existing rig in roughly one afternoon for under ~$4k total. **Until they do, the fuel thesis is entirely ASSERTED.** What is DOCUMENTED is narrower and real: an oil of diesel density/energy exists, and the nozzle cheaply remediates algae and makes paraffin (AECOM).

2. **The 3% is the keystone of the keystones — and it is a jar photo.** "Each pass converts 3% of the fluid" has no measurement behind it; it traces to a 1/8-inch floating layer in `BEAR Fuel 3percent.jpg`. It is then *divided into* the EROI numerator and *multiplied through* the throughput/revenue model. A 3×-optimistic 3% alone drops EROI from 18.6:1 to ~6:1 and daily output by ~3×. **No number downstream of it can be trusted until it is metered.**

3. **The literature is honest and it is not on the breakthrough's side — yet.** HC genuinely disrupts algae and extracts lipid (~3 MJ/kg) and genuinely intensifies *catalyzed* biodiesel. HC can crack *petroleum heavy oil* — but only with an added **hydrogen donor or catalyst.** There is **no peer-reviewed precedent** for catalyst-free, H-donor-free cavitation cracking whole wet biomass into finished diesel. The Mobula claim lives in the empty cell of that matrix. That is not proof of failure — it is proof that the burden of evidence is unmet and rests entirely on an unrun experiment.


---

*Sources cited inline: [Lee & Han, J. Appl. Phycology 2014 — HC microalgal disruption ~3 MJ/kg](https://link.springer.com/article/10.1007/s10811-014-0483-3); [CEC-600-2019-015 — HC vs HPH disruption energy](https://www.energy.ca.gov/sites/default/files/2021-05/CEC-600-2019-015.pdf); [ScienceDirect S2666086521000916 — HC biodiesel intensification review](https://www.sciencedirect.com/science/article/pii/S2666086521000916); [Springer s11356-022-20474-w — HC microalgae biodiesel](https://link.springer.com/article/10.1007/s11356-022-20474-w); [Ultrason. Sonochem. PMID 31450381 — cavitation heavy-oil upgrading review](https://pubmed.ncbi.nlm.nih.gov/31450381/); [RSC Adv. C8RA08087A — cavitating-jet viscosity reduction w/ H-donor](https://pubs.rsc.org/en/content/articlehtml/2019/ra/c8ra08087a); [Springer s12155-023-10615-5 — algae HTL global review](https://link.springer.com/article/10.1007/s12155-023-10615-5); [OSTI 1848720 — microalgae HTL biofuels](https://www.osti.gov/servlets/purl/1848720). Primary corpus: LVKNprocess.txt, BEARfuelTest1.pdf, SC1aecom1report2.md (AECOM/PACE), BEAR Fuel 3percent.jpg, PelagosPrcsDgmV2.jpg, US 7,750,494. Prior dossiers: 01_MASTER_DUE_DILIGENCE_v2.md, _validation-physics.md, _validation-energy.md, science.md.*
