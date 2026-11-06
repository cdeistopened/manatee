# Processing Unit (HVO processor, 9x9, pyrolizer-separator, eductor/cavitation hardware)

*Due-diligence dossier — Solaris Cybernetics / Barsoom Engineering "Mobula" / EVIE-2c. Prepared 2026-06-17.*
*Scope: the physical processing train only. The cavitation physics (energy balance, 1500°F / "absolute zero" claims) is treated in a separate physics dossier; here we assess the **hardware** — materials, flow rates, module geometry, and how the pieces connect.*

---

## What it is (plain language)

The Processing Unit is the onboard "refinery" that turns wet algae soup into a storable, oily fuel — without a furnace, without added chemicals, and without drying the algae first. That last point is the whole pitch. Conventional algae-to-fuel either dries the biomass (huge energy cost) or extracts lipids with solvents (huge chemical cost). Behrens' bet is that you can crack the organic molecules **inside the water**, using nothing but a high-pressure pump pushing the slurry through a specially shaped nozzle. The nozzle makes the water cavitate — form and collapse vacuum bubbles — and the inventor claims each bubble collapse briefly reaches the pressure and temperature of a tiny chemical reactor. A few percent of the slurry converts to hydrocarbons each pass; the oil floats, gets skimmed, and the rest recirculates.

Mechanically the train is four stages bolted in series: (1) a **microbubbler / dewaterer** that floats the algae into a foam and skims it to roughly 6% solids (the drawings cite 6% by weight; a subsystem doc claims up to ~30% solids / 70% water removed — the two numbers disagree and matter, see Red Flags); (2) an **eductor pump** that draws the concentrated slurry in and pressurizes it; (3) the **kinetic / cavitation nozzle** — the patented core, a stainless cylinder with a tight cluster of holes that accelerate the flow to ~100 ft/s and trigger controlled cavitation; and (4) a **pyrolizer-separator** tank where converted oil ("paraffin") stratifies to the top, is displaced into a collection bladder, and the un-converted water/biomass sinks and is sent through the nozzle again. The labels drift across documents — "HVO processor," "9x9 HVO processor," "H-D-R process," "LVKN nozzle," "Pelagos process," "Canard process flow" — but they describe variants of this same loop.

It is best understood as a **recirculating loop, not a single-pass reactor**. Nothing is fully converted in one go; the system grinds the same batch around the loop, peeling off a few percent of oil each cycle, until a layer accumulates and is decanted. That design choice is what lets a small pump do the work of a big high-pressure HTL vessel — at the cost of throughput. The flagship unit is small: a "5 gpd" (gallons-per-day) class device, fed by a 300 psi / 10 gpm pressure-washer pump, with the products held in a flexible bladder.

---

## How it works (mechanism, with numbers)

**Stage 1 — Microbubbler / dewatering (dissolved-air flotation).** Fine bubbles are injected at the bottom of a column; algae cells attach to the bubbles and rise into a foam fraction at the surface, which is mechanically skimmed (protein-skimmer style). This is textbook **dissolved-air flotation (DAF)** — a standard, well-understood harvesting method. The prototype photo `BEAR Microbubbler1.jpg` shows clear PVC columns with one column visibly green (algae) draining into a blue 55-gal drum — a real, built bench rig. The process prose targets **>6% solids** ("a light sensor indicates when it is dense enough"); the `BIOMASS_PROCESSING.md` subsystem doc instead claims **~30% moisture / 30% solids**. These are very different feedstocks. 6% is consistent with DAF on dilute algae; 30% solids by flotation alone is not realistic without a second dewatering step.

**Stage 2 — Eductor pump.** An eductor (jet/venturi pump, no moving parts in the wetted path) uses a motive jet to entrain and pressurize the slurry. The archived photo `AZ_Tank_Eductor_2_web.jpg` is the inventor's own cutaway: "Feed Inlet," four "Induction Ports," and a "Blended Mixture" outlet — a multi-port venturi/eductor that mixes and accelerates the stream. The bill of materials (`JT1BOM_strings.txt`) names a concrete part: a **300 psi × 10 gpm 12 VDC pressure-washer pump** (AR RMW2G24D) feeding the "LVKN nozzle." So the pressurization hardware is COTS and cheap.

**Stage 3 — Kinetic / cavitation nozzle (the patented core).** `KineticNozzle1.JPG` and `KineticNozzle1BBB.JPG` are the same part drawn at two scales — a ~4.2 in (or sub-half-inch in the "BBB" variant) **316-class stainless cylinder** with a **tetrahedral cluster of small bores** (one central + three surrounding, dimensions ~0.16/0.25 in or ~0.014/0.022 in). The drawing title block reads **"306 S.S."** — there is no AISI 306 stainless; this is almost certainly a typo for **316** (the marine-grade austenitic stainless you'd actually want here). The geometry is the physical embodiment of the patent's claim: accelerate flow to ~100 ft/s, drop local pressure below vapor pressure (Bernoulli/"Boyle's law" in the source text), and nucleate cavitation. The inventor's model says the imploding bubbles route their energy into a "tetra-helical vortex" — a primary core ~1000 Å across at ~15,000 rpm, nominally 1500°F and "absolute zero" pressure, with a secondary 0.04-in zone at ~630°F. **A few percent (claimed 3%) of the slurry is cracked per pass** via "hydrous pyrolysis" (= hydrothermal cracking in the bubble). *These temperature/pressure numbers are the physics dossier's job; mechanically, the relevant fact is that this is a tiny, replaceable, machinable stainless part.*

**Stage 4 — Pyrolizer-separator.** `Pyrolizer-Separator-AutoCAD.JPG` ("Project Name: a third-party reference design," a third-party reference design) is the cleanest engineering drawing in the set: a horizontal pressure vessel labeled **Kinetic Nozzle → S.S. tube → plenum → collection tank**, driven by a **motor + pump** on a common baseplate, ~5 ft scale bar. Converted oil floats; the prose describes injecting fresh slurry to raise the water level and **displace the floating hydrocarbon layer into a collection bladder**, while an "S-shaped" sub-surface return tube sends chlorophyll-laden water back to the growth tanks. So separation is **gravimetric stratification + displacement decanting**, not distillation. `CanardProcessFlow.JPG` is the dimensioned plumbing schematic tying pump → nozzle → two tanks together.

**The "HVO" / "9x9" framing.** "HVO" (hydrotreated vegetable oil) normally means catalytic hydrotreating with H₂ over a metal catalyst at 300–400°C — this system has **no catalyst and no external H₂ supply**, so calling the output "HVO" is marketing borrowed from a different process. Note the internal contradiction worth flagging: the SketchUp `PelagosPrcsDgm.jpg` (V1) says stage 2 ruptures cell walls with an **electric current to "make H2,"** while `PelagosPrcsDgmV2.jpg` revises the same caption to a **cavitating nozzle** "hydrogenating the lipids." The "9x9" appears to be a 9-module-square production array concept (`9x9-HVOprocessor.png` thumbnail + `BioMekAlpha9x9a.jpg`) — i.e., gang many small 5-gpd loops to reach commercial volume, rather than build one big reactor. That is a sensible scaling philosophy for a process whose unit economics live in a cheap, replicated nozzle.

**Throughput reality.** A 5-gpd unit at 3%/pass means the fuel rate is set by pump duty cycle and recirculation, not by a big reactor. The AECOM/PACE third-party test (below) ran **5-gallon samples on 37 watt-hours** with no additives and no waste stream — a genuine, if tiny, external data point.

---

## New-vs-old (what the 2024 PRIME / EVIE-2c design changed for THIS system)

The 2024 "PRIME" SketchUp (`VBShdl-1m5manatee2b1PRIME.png`, labeled **EVIE-2c**) and its `+BimodalTurbine` variant re-house the same processing train inside a new platform, with three changes that matter to the Processing Unit specifically:

- **The processor became a discrete central drum.** In both EVIE-2c previews a **cylindrical processor/growth drum sits low and central between the twin pontoons**, slung inside the tensegrity frame. In the older `9x9-HVOprocessor.png` and the a third-party reference design drawing the processing gear is a horizontal skid bolted to a baseplate. The PRIME design packages the loop as a **single drop-in drum module** at the platform's center of buoyancy — better weight distribution at sea and a cleaner "one module" unit for the 9×9 ganging story. (DOCUMENTED in the thumbnails; the internal plumbing of the drum is INFERRED to be the same eductor→nozzle→separator loop, not separately drawn in the new set.)
- **Amphibious wheels at the pontoon ends.** EVIE-2c adds wheels — implying the unit is meant to **self-beach to off-load fuel/paraffin** rather than rely solely on a port "fuel transfer hub" (cf. `BEAR Mobula m40 with fuel transfer hub.jpg`). For the processing train this changes the **off-load interface** (the bladder decant point) but not the conversion hardware.
- **`+BimodalTurbine` adds a horizontal-axis turbine on a central mast** (`VBShdl-...PRIME_BimodalTurbine.png`). This is a **power-supply change**, not a process change: the old JT-1 BOM powered the pump from a 400 W Air-X wind turbine + 45 W PV + 1/2 hp 12 VDC motor. The bimodal turbine (wind + water) is a bigger, steadier energy source for the same ~300 psi pump. It matters because the entire viability of the loop rests on the pump's parasitic load being small relative to fuel output — more reliable harvest power de-risks the duty cycle, but does nothing to validate the 3%/pass conversion claim.

What did **not** change: the core is still the **316-stainless cavitation nozzle + eductor + gravity separator** recirculating loop. The 2024 work is repackaging and power, not a new conversion mechanism.

---

## Evidence & maturity

| Claim / component | Evidence | Status |
|---|---|---|
| Microbubbler / DAF dewatering | `BEAR Microbubbler1.jpg`, `microbubbler 2/3/4.jpg` — built clear-column rig with green algae column | **BUILT** (bench) |
| Eductor / multi-port venturi | `AZ_Tank_Eductor_2_web.jpg` cutaway; `Eductor Pump + Cavitation Nozzle schematic.jpg`; BOM names AR RMW2G24D pump | **BUILT + specced** |
| Cavitation nozzle (316 SS, tetra-hole) | `KineticNozzle1.JPG` + `...BBB.JPG` dimensioned drawings; `BEAR cavitation nozzle close up.jpg` shows machined stainless vessels on a workbench | **BUILT** (physical parts photographed) |
| Pyrolizer-separator vessel | `Pyrolizer-Separator-AutoCAD.JPG` (a third-party reference design, fully labeled GA drawing) | **DESIGNED** (drawing; no build photo of this exact vessel) |
| Recirculating 3%/pass conversion | `9x9HVO_process.txt`, `LVKNprocess.txt`, `KINETIC_NOZZLE.md` | **ASSERTED** (inventor math, not independently measured) |
| Third-party output validation | `SC1aecom1report2.md` — AECOM (Jensen Beach FL) test, PACE Labs analysis: 5-gal samples, **37 Wh**, no additives, paraffin formed, N&P reduced in water | **TESTED (3rd-party)** — strongest single data point |
| Fuel characterization | `BEARfuelTest1.pdf`, `BEAR Fuel 3percent.jpg`, `curve_350UM950_81178.jpg` | **PARTIAL** (needs read of the PDF for ASTM-grade data) |
| Patent | US 7,750,494 B1, Behrens, "Systems and vessels for producing hydrocarbons and/or water, and methods for same" — confirmed real | **GRANTED** |
| EVIE-2c PRIME repackaging | `VBShdl-1m5manatee2b1PRIME(_BimodalTurbine).png` | **CAD-ONLY** (2024) |

Overall maturity for THIS subsystem: **built + bench-tested at 5-gal scale, third-party-witnessed for output existence (paraffin) and energy input (37 Wh), but never independently validated for conversion rate, fuel quality, or continuous marine operation.** The 2024 PRIME repackaging is CAD-only.

---

## Validation status (what current science says)

- **Cavitation as a real route to hydrothermal cracking — PLAUSIBLE (mechanism), DUBIOUS (claimed magnitudes).** Bona-fide HTL of wet algae works at **300–350°C and 2,000–3,000 psi (subcritical water)**, producing bio-crude at **HHV ~33.8–36.9 MJ/kg** ([PNNL/DOE](https://www.energy.gov/eere/bioenergy/articles/whole-algae-hydrothermal-liquefaction-technology-pathway), [Springer 2024](https://link.springer.com/article/10.1007/s42452-024-05911-4)). The inventor's ~127,000 BTU/gal output is **in the right neighborhood** for an oily product. Hydrodynamic-cavitation *intensification* of biomass/HTL is an active research area, so "cavitation helps crack wet organics" is not crank science. What is unproven is that a 300-psi pressure-washer pump driving a 4-inch nozzle delivers, in transient microscopic zones, the *integrated* energy a 3,000-psi heated HTL vessel delivers in bulk. The "absolute zero pressure / 1500°F / 1000 Å" figures are the physics dossier's to adjudicate; mechanically they are **not measurable with the sensors on this rig**, which the inventor concedes ("localized temperature claims require high-speed sensor validation," `KINETIC_NOZZLE.md`).
- **Cavitation erosion of the stainless nozzle — PLAUSIBLE and a real liability.** The literature is unambiguous: controlled cavitation pits and fatigues stainless steel, with erosion concentrated ~200 µm downstream of an orifice; harder surfaces resist better ([ScienceDirect S1350630705001792](https://www.sciencedirect.com/science/article/abs/pii/S1350630705001792), [Frontiers 2022](https://www.frontiersin.org/journals/mechanical-engineering/articles/10.3389/fmech.2022.869165/full)). The very effect that (claimed) cracks the lipids will eat the nozzle. The inventor lists this risk himself. This makes the nozzle a **consumable wear part** — which is bad for "maintenance-free autonomy" but *good* for a kit/replacement-part business.
- **"316 (not 306) stainless" choice — PLAUSIBLE/CORRECT.** No AISI 306 grade exists; 316 is the right marine austenitic choice. Treat "306" as a documentation error to correct, not a red flag about competence.
- **"HVO" label — DUBIOUS terminology.** Real HVO requires a catalyst + external H₂ ([HVO process literature]). This system has neither, so the output is an HTL-type bio-crude / paraffin, **not** HVO. The product is real; the name oversells its grade.
- **AECOM/PACE third-party test — PLAUSIBLE and load-bearing.** An independent facility (AECOM Jensen Beach) and an accredited lab (PACE) reportedly witnessed 5-gal runs producing paraffin with N/P reduction at 37 Wh input. This is the **single most credible artifact** in the whole corpus and deserves to be obtained in full (the `.md` is a summary, not the raw PACE report). If the raw lab sheet exists and matches, the de-water + cavitation + separate train moves from "asserted" toward "verified."
- **DAF microbubbler dewatering — PLAUSIBLE/STANDARD.** Flotation harvesting of algae is established; nothing exotic here.

---

## Red flags & open questions

1. **Solids-content contradiction (6% vs 30%).** The process prose and the subsystem doc disagree by 5×. This sets the entire energy balance — more water per pass = more parasitic pumping for less fuel. **Which is the real feed concentration into the nozzle?**
2. **Conversion rate never independently measured.** "3% per pass" is inventor math (`LVKNprocess.txt` derives it, doesn't measure it). The AECOM test proves *paraffin forms*, not *at what rate or yield per unit energy at the loop level*. Open: what is the measured **gal fuel / gal slurry** and **energy-return-on-energy-invested** for a full recirculating run?
3. **"HVO" / catalyst / H₂ confusion.** Docs variously claim H₂ is generated electrically (V1 diagram), that lipids are "hydrogenated" (V2 diagram), and that output is "HVO." With no catalyst and no H₂ feed in the BOM, the chemistry story is inconsistent. **Where does the hydrogen come from, if at all?**
4. **Nozzle erosion vs. autonomy.** A cavitation nozzle is a wear item; the whole product premise is months of unattended marine operation. **What is the measured nozzle service life (hours to bore-geometry drift) in salt water?** No erosion-test data is in the corpus.
5. **Fuel quality unknown.** `BEARfuelTest1.pdf` is unread here. Is the paraffin/"diesel" within any ASTM spec (cetane, cloud point, oxygen content)? HTL bio-crude is typically 5–20 wt% oxygen and needs upgrading — does theirs?
6. **Scale gap.** Everything physical is 5-gal / 5-gpd bench scale. The "9×9" and the EVIE-2c drum are concepts. **No continuous, multi-day, full-loop run at the unit's design rate is documented.**
7. **PRIME drum internals not drawn.** The 2024 EVIE-2c shows a central processor drum but no internal GA — we infer it's the same loop. **Confirm the drum actually packages eductor + nozzle + separator, or whether it's a placeholder solid.**
8. **Two process diagrams, two mechanisms.** V1 (electric cell-rupture + H₂) vs V2 (cavitation nozzle) — the inventor changed his own story between renders. Which is current for EVIE-2c?

---

## Concrete improvements (buildable upgrades + cheap de-risking experiments)

**Cheap experiments to de-risk (in order of leverage):**
1. **Closed-loop yield + energy test (the single most important number).** Run a known mass of 6% slurry around the loop for N passes on a metered DC supply (the rig already has a 12 VDC pump). Measure grams of paraffin out vs watt-hours in. This converts "3%/pass" from claim to data and produces the EROI investors actually want. ~1 day, ~$0 new hardware.
2. **Nozzle erosion run.** Operate one 316 nozzle continuously in salt water, pull and micrometer/borescope the bores at 24/72/168 h. Establishes service life and the replacement-part cadence (which is also the kit revenue model). Cheap, just time.
3. **Pull the raw PACE/AECOM lab report** and the `BEARfuelTest1.pdf`, get the paraffin sent for a one-off ASTM D975 / oxygen-content panel (~$300–800). Decides whether the output is "diesel," "diesel precursor," or "wax."
4. **Resolve the solids spec** by measuring DAF output solids directly with a moisture balance.

**Buildable upgrades:**
5. **Make the nozzle a hardened, swappable cartridge** — tungsten-carbide or boronized-316 insert in a quick-change holder. Turns the erosion liability into a clean consumable and a sellable spare.
6. **Instrument the nozzle** with a high-frequency pressure transducer + thermocouple downstream to actually bound (not assert) the local conditions — directly answers the physics dossier and the inventor's own stated validation gap.
7. **Add a second dewatering stage** (e.g., hydrocyclone or settling weir) if the real feed is 6% — getting to ~15–20% solids before the nozzle is exactly what HTL economics want and cuts parasitic pumping.
8. **Standardize the "module"** — package eductor + nozzle + separator as one flanged 5-gpd cartridge with documented interfaces, so the 9×9 array is literally "bolt N modules to a manifold." This is the productization step that makes both the kit and the EVIE-2c drum real.

---

## Kit / license angle

This subsystem is the **most sellable and most licensable** part of the whole invention, precisely because it is small, COTS-adjacent, and patent-anchored.

- **Licensable IP:** US 7,750,494 B1 (granted, Behrens) covers the cavitation/venturi conversion. The corpus already ships a **2022 editable patent-license template** offering a **non-exclusive, field-limited license at 3% of gross sales** (`Study_Plans_Instructions.txt`). That is a ready-made, low-friction licensing instrument — the diligence task is verifying the patent's term/maintenance status and claim scope, not drafting a deal from scratch.
- **Kit-able hardware:** the entire train is buildable from a documented BOM — a ~$200–400 pressure-washer pump (AR RMW2G24D class), a machined 316 stainless nozzle (a CNC turning job from the dimensioned `KineticNozzle1` drawings), an eductor, a PVC DAF column, and a flexible bladder. A **"5-gpd algae-to-paraffin bench kit"** is a credible maker/research SKU: sell the machined nozzle + assembly drawings + the closed-loop test protocol, license the patent on top for any commercial use.
- **The recurring-revenue wedge is the nozzle itself.** Because cavitation erodes it, the nozzle is a **consumable** — a razor/razor-blade model. Sell the kit once; sell hardened replacement cartridges forever; collect 3% on anyone who commercializes.
- **What's NOT kit-ready:** the EVIE-2c marine platform, autonomy, and continuous-operation claims. The defensible, immediately sellable product is the **bench processing module** (de-water → eductor → cavitation nozzle → separator), decoupled from the boat. That is the unit to validate (experiment #1 above), package (upgrade #8), and sell first.
