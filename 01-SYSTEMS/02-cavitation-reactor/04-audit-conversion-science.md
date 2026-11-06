# Science of Conversion (cavitation physics + algae chemistry)

*Due-diligence dossier — Solaris Cybernetics / Barsoom Engineering "Mobula" / EVIE-2c. Focus: does hydrodynamic cavitation actually crack algal biomass into diesel-range hydrocarbons? Drafted 2026-06-17.*

---

## What it is (plain language)

The Mobula is meant to be a self-feeding fuel factory floating on a pond or the ocean. It grows a slurry of pond plants and algae (the "S3 blend": spirulina, azolla, *Gracilaria*, *Lemna minor*/duckweed, and *Wolffia*), concentrates that biomass, and then pumps the wet green slurry at very high speed through a small stainless-steel **"kinetic nozzle."** The claim is that forcing the fluid through this nozzle creates **hydrodynamic cavitation** — clouds of tiny vapor bubbles that form and then violently collapse. Each collapsing bubble is, for a microsecond, a tiny furnace: extremely hot and effectively a vacuum. Behrens' claim is that these micro-furnaces "crack" the long oily molecules in the algae into shorter molecules that fall in the diesel range — no external heat source, no refinery, no chemical catalyst, no methanol.

The headline economic claim is striking: the energy to drive the pump is only about **5.34% of the energy in the fuel that comes out** (~127,000 BTU/gallon), so the machine is wildly energy-positive and pays for its own propulsion and growth lighting with a tiny slice of its output. The robot then steers itself toward light (a Braitenberg-style phototaxis controller, covered in the AI dossier) to keep its algae growing, and stores or offloads the fuel.

The critical thing to understand for investors: **the biology is conventional and credible; the conversion physics is where the entire bet lives.** Growing duckweed and spirulina in a pond is undergraduate-level aquaculture. The contested, load-bearing, and largely unverified claim is that *a single pass through a passive venturi nozzle does the work that the rest of the world does with 300–350 °C reactors at 200+ atmospheres, or with methanol and lye.*

---

## How it works (the real mechanism, with numbers)

The process flow is documented in `PelagosPrcsDgmV2.jpg` and `LVKNprocess.txt` and is internally consistent as a *narrative*:

1. **Grow + concentrate.** Bubblers inject CO₂ and concentrate the biomass to ~6% by weight (`PelagosPrcsDgmV2.jpg` step 1; `SCIENCE_BASIS.md`). Claimed doubling time 90–120 min — optimistic but not impossible for spirulina/duckweed under ideal light.
2. **Cavitation pass #1 (hydrogenation/separation).** Slurry is pumped through a sealed cavitating nozzle that "separates & hydrogenates the lipids" (step 2).
3. **Cavitation pass #2 (thermal depolymerization).** The "hydrogenated lipids" pass through a second cavitating nozzle "to cause Thermal Depolymerization" (step 3).
4. **Recycle.** Waste (CO₂, mineral ash) returns to the growth tank (step 4).
5. **Stratify + store.** Fuel separates by density and is stored (steps 5–6).

### The physics claim, quantified (from `LVKNprocess.txt`)

| Quantity | Claimed value | Notes |
|---|---|---|
| Flow velocity to induce cavitation | 100 ft/s at 150 °F | Used Euler/Bernoulli + Boyle's law (text says "Boyle's" — should be Bernoulli) |
| Energy to accelerate 1 gal to 100 ft/s | 0.06 hp·gal = 204.84 BTU | H = V²/2g = 155.28 ft; hp = Q·H/3960; 65% efficiency |
| Conversion per pass | 3% of fluid | The single most load-bearing number; basis unstated |
| Energy per gallon converted | 204.84 / 0.03 = 6,828 BTU | |
| Output energy density | 127,000 BTU/gal | "Based on lab tests" |
| **Net conversion energy** | **6,828 / 127,000 = 5.34% of output** | The headline efficiency claim |

### The micro-scale claim

The nozzle allegedly redirects cavitation energy from a flat 2-D wavefront into a **tetra-helical vortex** that compresses into three vortices spiraling around a center:
- **Primary rotating zone:** ~15,000 rpm, **1,500 °F**, "absolute zero" pressure, **1,000 Å (0.1 µm) diameter** — ionized/plasma-like.
- **Secondary entrained zone:** ~2,000 rpm, **630 °F**, also "absolute zero" pressure, 0.04 in diameter, non-ionized.
- Energy exchanges between the two in a "worm-like" oscillation; turbulence is focused to one point so the rest of the stream stays laminar.

The nozzle drawing (`KineticNozzle1.JPG`) is a real, dimensioned part: a 4.20-inch-diameter 306-stainless cylinder with a tight cluster of small bores (0.16 in, 0.25 in spacing, 0.73 in) — i.e., a multi-port venturi/orifice plate. This is a *physically buildable object*, and machined hardware exists (see `BEAR cavitation nozzle close up.jpg`).

---

## New-vs-old (what the 2024 PRIME / EVIE-2c design changed for THIS system)

The 2024 SketchUp models (`VBShdl-1m5manatee2b1PRIME.skp`, dated Aug 2024; `...PRIME+BimodalTurbine.skp`, Jul 2024) are the newest artifacts. From the rendered previews (`skp_thumbs/VBShdl-1m5manatee2b1PRIME.png` and `..._BimodalTurbine.png`), labeled **"EVIE-2c"**:

- **The conversion core did NOT change.** The PRIME redesign is an *airframe/platform* change — tensegrity frame on twin blue pontoons, amphibious wheels at the pontoon ends, and a **central growth/processor drum** (visible as the grey cylinder amidships). The kinetic-nozzle conversion subsystem is unchanged from the 2008–2012 `LVKNprocess`/`KineticNozzle1` lineage. No new cavitation geometry, no new energy balance, no new fuel chemistry appears in the 2024 files.
- **Bimodal turbine variant** adds a horizontal-axis turbine on a central mast (`..._BimodalTurbine.png`) — this is a *power-harvesting* change (wind/flow energy to run pumps and lights), not a conversion-chemistry change. It is, however, **thematically aligned with the actual patent** (US 7,750,494 is a wind→hydrocarbon system; see Red Flags), which suggests Behrens may be quietly migrating the energy story toward the thing he actually patented.
- **Net:** For *this* system (cavitation + algae chemistry), the 2024 PRIME work is **packaging, not physics.** The unverified 2008-era conversion claims are carried forward verbatim. Nothing in the new corpus re-tests or re-derives the 3%/pass or 5.34% numbers.

---

## Evidence & maturity

**DOCUMENTED / BUILT:**
- Dimensioned nozzle part drawing in 306 SS (`KineticNozzle1.JPG`, `KINETIC_NOZZLE.md`), plus a DXF/TCW CAD set (`KNdwg/`).
- Physical machined hardware photographed (`BEAR cavitation nozzle close up.jpg` — stainless pressure vessels and fittings on a bench).
- A pyrolizer-separator AutoCAD assembly ("a third-party reference design," `Pyrolizer-Separator-AutoCAD.JPG`) showing pump/motor/nozzle/collection-tank layout — a real bench-rig design.
- A **product** photo: a Ball jar showing a stratified output, labeled "3 percent" with a thin (1/8 in) top layer over 3 5/8 in of green liquid (`BEAR Fuel 3percent.jpg`). This is consistent with — and probably the visual source of — the "3% conversion per pass" claim.

**THE ONE LAB RESULT (read in full):** `BEARfuelTest1.pdf` is a single-page third-party fuel analysis, **"ANALYSIS OF SYNTHETIC FUEL," from "B.E.A.R. GROUP," dated 9/23/2012**, sample designation "BIO DIESEL," sample ID "r.behrens sample." It reports exactly three numbers by ASTM methods:
- **D4052 API Gravity: 32.71° API**
- **D240 Gross Heat of Combustion: 18,254 BTU/lb**
- **D240 Gross Heat of Combustion: 134,258 BTU/gal**

What this PDF actually proves and does **not** prove is the crux of the whole due diligence:
- It is a **calorimetry + density** report only. D240 measures how much heat a sample releases when burned; D4052 measures density. **Neither identifies the molecules.** A bomb calorimeter will happily report ~18,000 BTU/lb for diesel, for raw algal oil, for crude, or for a vegetable-oil/solvent mix — they're all hydrocarbons of similar energy density.
- 32.71° API ≈ 0.862 g/mL — that is in the range of **petroleum diesel (≈30–39° API)**, but it is *also* in the range of many bio-oils and blends. It tells you the sample is an oil of roughly diesel density; it does **not** tell you it was made by cavitation, nor that it is a diesel-range *distillate*.
- **134,258 BTU/gal measured** vs. **127,000 BTU/gal asserted** in the process doc — close, so the asserted figure is at least anchored to this one real test.
- **Critically absent:** no cetane number (D613), no distillation curve / boiling range (D86), no viscosity (D445), no flash point, no GC/GC-MS speciation, no sulfur, no cloud/pour point, no FAME content (EN 14103). These are exactly the tests that would distinguish "real diesel-range hydrocarbon fuel made by cracking" from "an oily layer of similar energy density." The project's own `SCIENCE_BASIS.md` admits this: it lists "ASTM Fuel Testing… density, viscosity, and cetane number" as a *future research gap*.

**Maturity verdict: built-untested.** Real hardware and one real-but-thin lab report exist; the *mechanism* (cavitation cracks lipids into diesel-range hydrocarbons) and the *energy balance* (5.34%) have never been independently demonstrated. The 2015 pond prototype (`BioMass#.jpg`) and 2023 marina test verify a floating platform and algae growth, not fuel conversion.

**Note on `IllustratedPhotosymthesis.pdf`:** this is **not original research** — it is a verbatim reprint of a 2007 NSTA *Science and Children* "Science 101" article ("How does photosynthesis work?" by Bill Robertson). It is grade-school background, not evidence for any Mobula claim. Its presence in the corpus should not be read as supporting documentation.

---

## Validation status (per claim)

**Claim 1 — Hydrodynamic cavitation can be used to make biodiesel. → PLAUSIBLE (but not the way claimed).**
The peer-reviewed literature (Gogate & Pandit and successors) is clear and substantial: hydrodynamic cavitation via orifice/venturi reactors **intensifies transesterification** — it emulsifies oil + methanol so the catalytic reaction to FAME runs faster and at >90% yield with less catalyst/energy. This is real and commercialized-adjacent. **But in every one of these studies the chemistry is still transesterification (oil + alcohol + catalyst → biodiesel + glycerol).** Cavitation is the *mixer/intensifier*, not the *reaction*. Behrens claims something categorically different: catalyst-free, alcohol-free **molecular cracking/depolymerization** of whole biomass by cavitation alone. That is **not** what the cited literature supports.
Sources: [ScienceDirect HC review](https://www.sciencedirect.com/science/article/pii/S2666086521000916); [Springer — HC-assisted microalgae biodiesel](https://link.springer.com/article/10.1007/s11356-022-20474-w).

**Claim 2 — Cavitation bubble collapse reaches extreme temperature/pressure. → PLAUSIBLE in spirit, DUBIOUS in the specific numbers.**
Sonochemistry (Suslick) confirms collapsing-bubble hot spots of **~5,000 K (≈8,500 °F), ~1,000 atm, with >10¹⁰ K/s heating/cooling**. So a 1,500 °F (≈1,090 K) hot-spot claim is, if anything, *conservative* relative to acoustic cavitation — that part is not crazy. **However:** (a) "absolute zero pressure" is physically meaningless — the interior of a collapsing bubble is at *enormous* pressure (~1,000 atm), not zero; the author appears to be conflating the *pre-collapse* vapor-cavity (low pressure) with the *collapse* (high pressure). (b) Specific figures like "15,000 rpm," "1,000 Å zone," "tetra-helical vortex," and "2,000 rpm secondary" are presented with false precision and **no derivation or measurement** — they read as narrative, not physics. (c) The hot spot lasts nanoseconds over sub-micron volumes; whether enough *mass* spends enough *time* there to crack 3% of the bulk flow per pass is exactly the unproven leap. The project's own risk note concedes "localized temperature claims require high-speed sensor validation."
Sources: [Suslick — Sonoluminescence & Sonochemistry](https://suslick.scs.illinois.edu/documents/ap.encycl.physscitech2001.pdf); [Suslick — Hot-spot conditions](https://suslick.scs.illinois.edu/documents/natoasi.conditions.rv1.pdf).

**Claim 3 — Cavitation alone thermally depolymerizes algal biomass into diesel-range hydrocarbons. → DUBIOUS / UNVERIFIED.**
The established thermochemical route for *wet* algae is **Hydrothermal Liquefaction (HTL)**: 300–350 °C, 5–22 MPa (≈50–220 atm), ~15–60 min residence, yielding ~45–50 wt% biocrude that **still requires catalytic upgrading** (hydrotreating) before it is a finished fuel. HTL works because the *entire bulk slurry* is held at supercritical-ish conditions for minutes. Behrens proposes to get an equivalent or better result from *transient sub-micron hot spots* in a *single pass* with *no bulk heating* — and to produce finished fuel directly, skipping the upgrading step the entire field requires. There is **no peer-reviewed precedent** for single-pass cavitation converting whole biomass to finished diesel. This is the claim most likely to be false as stated.
Sources: [Springer — Global perspective on HTL of algae](https://link.springer.com/article/10.1007/s12155-023-10615-5); [OSTI — Microalgae to biofuels via HTL](https://www.osti.gov/servlets/purl/1848720).

**Claim 4 — Net energy cost is 5.34% of output. → DUBIOUS.**
The 5.34% figure is arithmetically self-consistent *given* the 3%/pass conversion and the 204.84 BTU/gal pump energy. But it rests entirely on the **unproven 3%/pass** number and **ignores**: pumping losses across a tight multi-bore nozzle (real venturi/orifice HC rigs run at high inlet pressures and have substantial recirculation energy), the energy to grow/concentrate/dry biomass, multiple passes (the process flow shows *at least two* cavitation stages), and CO₂/lighting overhead. Real HC-biodiesel rigs report energy *intensification* vs. stirred tanks — not a 19:1 energy-return-on-investment from a passive nozzle. EROI claims this high without a closed-loop demonstration are a classic over-unity red flag.

**Claim 5 — The fuel is diesel (the BEAR lab test). → The test shows an oil of diesel-like density and heating value; it does NOT show diesel-range hydrocarbons or cavitation provenance. → PARTIALLY SUPPORTED / INSUFFICIENT.** (See Evidence section.)

**Claim 6 — Protected under US Patent 7,750,494. → MISLEADING / FALSE as applied to this mechanism.**
`KINETIC_NOZZLE.md` states the nozzle is "protected under US Patent 7,750,494." The actual patent (Behrens, Rudolph) is titled **"Systems and vessels for producing hydrocarbons and/or water, and methods for same"** and describes a **wind-turbine → electrolyzer → reverse water-gas-shift → methanation** (essentially Fischer-Tropsch-style) system making hydrocarbons from *air, water, and wind energy* — **not** a cavitation nozzle that cracks algal lipids. The cavitation-cracking mechanism does not appear to be the subject of that patent. The 2024 "+BimodalTurbine" variant is conspicuously closer to what the patent actually covers. This mismatch needs to be resolved before any IP/licensing representation is made.
Source: [Google Patents US7750494B1](https://patents.google.com/patent/US7750494).

---

## Red flags & open questions

1. **The one lab test can't distinguish the hypothesis from the null.** D240 + D4052 measure energy and density — both satisfied by *any* oil. Without GC-MS, a distillation curve, and cetane, "BIO DIESEL, r.behrens sample" could be cracked fuel, raw algal lipid, or a solvent/oil blend. This is the single biggest gap.
2. **"Absolute zero pressure"** in the collapse zone is physically wrong and signals the author is narrating intuition, not solving the thermodynamics. Same for "tetra-helical vortex" precision with no math.
3. **Patent mismatch (Claim 6).** The cited patent is a wind-to-hydrocarbon system, not a cavitation cracker. Citing 7,750,494 as covering the "kinetic nozzle IP" overstates what that patent actually protects — worth correcting in the documentation before it's used in any licensing or marketing material.
4. **Mechanism conflicts with the entire wet-algae conversion field.** Everyone else needs either HTL (minutes at 300+ °C / 200 atm bulk) or transesterification (alcohol + catalyst). Single-pass passive-nozzle cracking has no precedent.
5. **EROI ~19:1 from a passive nozzle** has the shape of an over-unity claim; the energy accounting omits real costs (multi-pass, growth, concentration, lighting, recirculation).
6. **The 2024 PRIME work re-skinned the platform without re-testing the core.** A decade of CAD iteration on the *frame* while the load-bearing *conversion* claim sits on one 2012 calorimetry sheet.
7. **"Hydrogenated lipids" (process step 2)** — hydrogenation needs a hydrogen source and a catalyst. Where does the H₂ come from in a passive nozzle? Unexplained.
8. **Open questions:** What is the actual conversion-vs-passes curve? Does output composition match diesel by GC-MS? What inlet pressure does the nozzle need, and what is the true wire-to-fuel EROI on a closed loop? Is there *any* finished fuel that ran an engine?

---

## Concrete improvements (buildable upgrades + cheap de-risking experiments)

These are ordered cheapest-first; the first three could be done for low four figures and would settle the central question.

1. **GC-MS + distillation curve on the existing jar of product (~$300–800).** This is the decisive, cheap test. If the carbon-number distribution sits in the C10–C22 diesel window, the cracking story gains real credibility. If it looks like intact triglycerides/FAME or a solvent blend, the cracking claim collapses. *Do this before anything else.*
2. **Add the missing ASTM panel: cetane (D613), viscosity (D445), flash point (D93), FAME content (EN 14103).** Together with #1 this converts "an oil of diesel-like density" into a defensible fuel spec — and is exactly what `SCIENCE_BASIS.md` already flags as the gap.
3. **Single-variable conversion-vs-passes experiment.** Run the same feedstock through the nozzle 1, 2, 5, 10 times; assay product fraction each pass. This directly tests the "3% per pass" claim and reveals whether conversion is real cracking or just emulsification/stratification artifact. Mass-balance the input and output (this is what "3 percent" in the jar photo *should* have been).
4. **Instrument the nozzle.** High-speed imaging + a hydrophone + inlet/outlet pressure and temperature logging to confirm cavitation is actually occurring and to bound the real hot-spot conditions (the project itself calls for "high-speed sensor validation").
5. **Reframe honestly as cavitation-*assisted* conversion.** The defensible, literature-backed product is **HC-intensified transesterification** of the algal lipid fraction (add methanol + a cheap catalyst at the nozzle). That is a real, sellable process improvement with published >90% yields. Cavitation-as-cracker can stay as the moonshot, clearly labeled unproven.
6. **Decouple the energy story.** Adopt the 2024 BimodalTurbine to honestly power pumps/lights from wind/flow rather than claiming the conversion itself is near-free. This also aligns the build with the actual patent.

---

## Kit / license angle

**What is genuinely sellable today (low technical risk):**
- **The floating algae-growth + concentration platform.** Twin-pontoon tensegrity frame, CO₂ bubblers, phototaxis steering, growth drum — the EVIE-2c airframe. This is a buildable **"autonomous pond-algae harvester" kit**: BOM exists (`JT1BOM.xls`), CAD exists (PRIME .skp set), lifting/rigging instructions exist (2025). Sell it as an aquaculture/bioremediation rig ("bio-battery" that pulls N/P/CO₂ from runoff) — claims that are *true and demonstrable* without touching the fuel controversy.
- **The kinetic-nozzle as an HC mixing/intensification cartridge.** A dimensioned 306-SS multi-bore venturi is a real part. Sold honestly as a **cavitation intensifier** for transesterification or for general emulsification/mixing, it stands on solid published ground.
- **"Study Plans" / build-kit + the editable 2022 patent-license template.** The corpus already contains a study-plans instruction PDF and a general license template — the scaffolding for a kit-plus-license business is in place.

**What must NOT be sold or licensed as-is:**
- The **"cavitation cracks algae into finished diesel at 5.34% energy cost"** claim. It is unverified, conflicts with the literature, and is not what patent 7,750,494 actually covers. Licensing IP on that basis is legal and reputational exposure. **De-risk it with experiments #1–#3 first; if GC-MS confirms diesel-range hydrocarbons, the value of the kit-and-license business goes up by an order of magnitude.**

**Bottom line for a technical-but-skeptical buyer:** the platform and the nozzle are real and sellable now; the conversion miracle is one cheap GC-MS away from being either the most valuable thing here or a polite footnote. Spend the $800 before you spend anything else.
