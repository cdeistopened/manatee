# AGENTS.md — Progressive Disclosure & Epistemic Protocol for AI Agents

Welcome. You are reading an open-hardware engineering and scientific due-diligence repository for **The Manatee** (Solaris Cybernetics / Rudolph "Rudy" Behrens' algae-to-hydrocarbon cavitation reactor and autonomous pond platform).

This repository is structured for **progressive disclosure**: it allows an engineer, scientist, builder, or AI agent to understand the high-level thesis in two minutes, check every assumption against adversarial physics/thermodynamics audits, and trace claims all the way down to primary lab PDFs, handwritten calculations, and parametric 3D CAD.

---

## 1. Epistemic Rules (Read Before Answering Any Question)

The historical archive behind this project spans 22 years (2003–2025) and five distinct company names (`Aeolus Group`, `B.E.A.R. Oceanics`, `Cyanagra`, `Barsoom Engineering`, `Solaris Cybernetics`). In the original inventor documents, genuine engineering breakthroughs and third-party lab results are frequently mixed with unmeasured extrapolations.

**When answering questions or analyzing files in this repo, you MUST enforce three rules:**

### Rule A: Tag Every Claim by Evidence Tier
Never state an unmeasured assertion as an established fact. Classify every technical claim into one of three tiers:
1. **`[DOCUMENTED]`** — Directly supported by an accredited third-party lab report (`04-PRIMARY-EVIDENCE/lab-assays/`), a physical build photograph/video (`04-PRIMARY-EVIDENCE/field-media/`), or a dimensioned CAD/BOM artifact (`03-HARDWARE-CAD/`, `02-BUILD-MANUAL/`).
   - *Examples:* ASTM D4052 density of 28.5°–32.71° API; ASTM D240 heat of combustion of 17,137–18,254 BTU/lb; AECOM/PACE bench remediation of 5 gal on 37 Wh with N/P reduction; Dr. Thomson's 2003 1 MW wind-electrolysis chemical engineering balance.
2. **`[INFERRED]`** — Derived from first-principles physics, peer-reviewed literature, or cross-checking multiple archive files.
   - *Examples:* That cavitation cell-wall disruption requires ~3 MJ/kg dry biomass (~10–20% of output energy, giving a sun-driven EROI of ~5–8:1); that the "3% per pass" figure originated from measuring a 1/8-inch oil layer in a 3-5/8-inch Ball jar (`BEAR_Fuel_3percent_render.jpg`); that duckweed (*Lemna*) root mats provide natural gravity dewatering.
3. **`[ASSERTED / UNMEASURED]`** — Stated in historical pitch decks or process notes without an end-to-end measurement.
   - *Examples:* That single-pass hydrodynamic cavitation chemically *cracks* $\text{C–C}$ bonds into finished diesel distillate (rather than mechanically extracting intracellular lipids/waxes); that conversion consumes only 5.34% of output energy (~19:1 EROI); that cavitation in the nozzle is "thermodynamically reversible / adiabatic" or reaches "absolute zero pressure."

### Rule B: Never Blend the Five Historical Machines
As documented in [`00-OVERVIEW/05-machine-lineage-and-buildability.md`](00-OVERVIEW/05-machine-lineage-and-buildability.md), the archive contains **five different machines**, not one:
1. **The 2003–2006 "Ocean Gypsy" Wind-Electrolysis Ship (`US 7,302,903`):** A 72-foot, 1 MW wind-powered vessel designed to split seawater via electrolysis and capture atmospheric $\text{CO}_2$ via cryogenic distillation to synthesize ethanol/synfuel. Blueprints by NDI Engineering (`04-PRIMARY-EVIDENCE/process-and-naval-drawings/ocean-gypsy-2004-naval-architecture/`); mass balance by Dr. William Thomson (`04-PRIMARY-EVIDENCE/engineering-calcs/`). Never built at full scale.
2. **The 2008–2012 Bench Cavitation Rig (`LVKN` / `B.E.A.R.`):** The stationary high-pressure pump + stainless multi-bore cavitation nozzle rig that produced the 2006 Intertek, 2007 AAL GC-MS, 2008 Ultimate Analysis, and 2012 BEAR fuel samples, plus the AECOM 5-gallon / 37 Wh remediation test.
3. **The 2014–2015 Working Pond Prototype (PA Farm Pond):** A lightweight PVC pontoon raft running on ~15 W wind (vertical-axis Lenz rotor) + ~15 W solar + a 1/10 HP pump with a bucket/jar separator on a duckweed-covered pond. Filmed operating in [`04-PRIMARY-EVIDENCE/field-media/manatee-pond-truesource.mp4`](04-PRIMARY-EVIDENCE/field-media/manatee-pond-truesource.mp4).
4. **The 2015 Container-Built Marina Prototype:** A four-pontoon Schedule-40 PVC raft with a galvanized steel braced mast, Lenz vertical-axis rotor, flexible solar panel, two submerged Rule bilge-pump thrusters, and an acrylic control box (photographed during assembly in April–July 2015; camera EXIF clock was offset by +35 years to 2050).
5. **The 2024–2026 `EVIE-2c` / Clean-Room Manatee Design:** The standardized quad-pontoon symmetric catamaran (`2.26 × 3.20 × 1.24 m`) documented in [`02-BUILD-MANUAL/`](02-BUILD-MANUAL/) and reconstructed procedurally in [`03-HARDWARE-CAD/`](03-HARDWARE-CAD/).

### Rule C: Always Point to the Decisive Bench Test
Whenever a user asks whether a controversial claim works, do not merely argue from theory — cite the specific, low-cost experimental protocol in [`02-BUILD-MANUAL/04-garage-bench-test-protocol.md`](02-BUILD-MANUAL/04-garage-bench-test-protocol.md) (~$100 pressure-washer test) or [`00-OVERVIEW/04-three-unmeasured-keystones.md`](00-OVERVIEW/04-three-unmeasured-keystones.md) (~$500 GC-MS + ASTM D86 distillation curve, wattmeter + D240 calorimetry, and pass-count assay) that settles the question empirically.

---

## 2. Progressive Disclosure Routing Table

| If the user asks about... | Read Tier 1 (`00-OVERVIEW/`) first | Then drill into Tier 2/3 (`01-SYSTEMS/`, `02-BUILD-MANUAL/`) | And verify against Tier 4/5 (`03-HARDWARE-CAD/`, `04-PRIMARY-EVIDENCE/`) |
| :--- | :--- | :--- | :--- |
| **High-level concept, why wax vs. batteries, or overall verdict** | `01-bio-battery-thesis.md`<br>`03-executive-engineering-assessment.md` | `01-SYSTEMS/01-ecology-and-dewatering/` | `04-PRIMARY-EVIDENCE/EVIDENCE-INDEX.md` |
| **Electrolysis, hydrogen, e-fuels, or how the 2003/2006 patents connect to algae** | `02-electrolysis-to-algae-bridge.md`<br>`04-three-unmeasured-keystones.md` | `01-SYSTEMS/02-cavitation-reactor/04-audit-conversion-science.md` | `Dr_William_Thomson_1MW_Wind_Electrolysis_Ethanol_Report_2003.pdf`<br>`PelagosPrcsDgm_V1_Electrolysis.jpg` vs `V2_Cavitation.jpg` |
| **Cavitation nozzle physics, hydrous pyrolysis vs. extraction, or nozzle dimensions** | `04-three-unmeasured-keystones.md` | `01-SYSTEMS/02-cavitation-reactor/01-cavitation-reactor-core.md`<br>`02-nozzle-and-eductor.md`<br>`06-audit-physics-validation.md`<br>`07-audit-reactor-buildability.md` | `03-HARDWARE-CAD/nozzle-dxf/`<br>`03-HARDWARE-CAD/models/kinetic-nozzle.png`<br>`LVKNprocess.txt` |
| **Energy balance (EROI), the 5.34% / 19:1 claim, or the "3% per pass" assumption** | `04-three-unmeasured-keystones.md` | `01-SYSTEMS/03-energy-and-thermodynamics/01-audit-energy-balance.md`<br>`03-audit-energy-validation.md`<br>`04-audit-energy-boundary-math.md` | `LVKNprocess.txt`<br>`AlgaeX_001.jpg`–`AlgaeX_013.jpg` |
| **Algae biology, duckweed (*Lemna*) dewatering, or pond remediation** | `01-bio-battery-thesis.md` | `01-SYSTEMS/01-ecology-and-dewatering/01-three-species-synergy.md`<br>`02-dewatering-breakthrough.md`<br>`03-nutrient-remediation.md` | `Rutgers_John_Kraeuter_Algal_Weight_Lab_Letter_2006.pdf`<br>`S3algaeRecipe.txt` |
| **3D CAD models, parts list, BOM, or physical buildability** | `05-machine-lineage-and-buildability.md` | `01-SYSTEMS/04-hull-and-propulsion/`<br>`02-BUILD-MANUAL/01-bill-of-materials.md`<br>`02-step-by-step-build-manual.md` | `03-HARDWARE-CAD/README.md`<br>`03-HARDWARE-CAD/catalog.json`<br>`02-BUILD-MANUAL/bom-sourced.json` |
| **12V solar/wind power, BEAM phototropism circuit ("Prospero AI"), or wiring** | `03-executive-engineering-assessment.md` | `01-SYSTEMS/05-power-and-analog-brain/` | `02-BUILD-MANUAL/electronics-areas.json` |
| **Fuel test results (API gravity, BTU/lb, GC-MS, Ultimate Analysis)** | `03-executive-engineering-assessment.md` | `02-BUILD-MANUAL/05-lab-assays-and-standards.md` | `04-PRIMARY-EVIDENCE/lab-assays/*` |
