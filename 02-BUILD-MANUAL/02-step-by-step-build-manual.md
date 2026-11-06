# The Manatee (EVIE-2c) — IMPROVED DIY Assembly Manual

*A buildable solar/wind-powered floating raft that harvests harmful pond algae by hydrodynamic cavitation, cleans the water, and yields a waxy lipid residue as a bonus. This is the **IMPROVED** edition: same machine, same function, re-engineered for reliability, safety, lower cost, and — above all — the ability to **measure whether it actually works**. The faithful **AS-BUILT** edition is a separate document; read it if you want the original design verbatim.*

**Stance:** optimistic skeptic. The core idea is sound — cavitation lyses algae cells (documented in the algae-lipid literature) and the lead deliverable is **cleaner water**. The oil/wax is an under-indexed, unproven-at-yield **bonus**, suitable for shore-side candle rendering. This manual makes **no** claim of gal/day throughput, no "diesel/engine fuel," and no "patented AI." The steering brain is a public-domain BEAM/Braitenberg analog phototrope, not machine learning.

**Honesty rules baked into this build:**
- Lead value = cleaner water. Wax/candles = bonus, "experimental until independently tested."
- Every UNKNOWN spec is marked **UNKNOWN / measure on your unit** — nothing is invented.
- The one number the whole venture turns on — **watt-hours in vs. grams of oil out** — is now measured on every run by permanently installed instrumentation, not asserted.

---

## What changed from the original, and why

| # | Subsystem | AS-BUILT | IMPROVED | Why it matters |
|---|-----------|----------|----------|----------------|
| 1 | Flotation | Two 10-ft × 6-in sealed PVC pipes, partially foam-filled (~300 lb pair buoyancy) | Two **foam-cored HDPE dock floats** sized to a **2× payload reserve** (or 12-in HDPE filled solid) | 6-in pipes cannot float a working reactor drum. Dock floats are inherently unsinkable, UV-stable, no glued seam to leak. |
| 2 | Frame | Furniture-grade PVC + steel-cable tensegrity; PVC mast as sole compression strut | **Bolted 6061-T6 aluminum ladder frame** (tensegrity kept as an optional *hardened* route in aluminum + 316 cable) | PVC creeps under sustained preload and embrittles under UV; furniture-grade fittings aren't structurally rated. Aluminum is stiffer, ratable, bolts together. |
| 3 | Stability | No stability analysis; mast-top turbine raises CG on a beamy hull | **Battery mounted low as ballast, min beam spec, removable turbine, $0 dockside inclining test** | Capsize is the most likely demonstrator failure and was completely unaddressed. |
| 4 | Cavitation pump | AR RMW2G24D run at "300 psi × 10 gpm" (~1.3 kW mech / ~2.5 kW elec) | **Small triplex plunger pump, ~1.5–2.5 gpm @ 250–400 psi** on a 24–48 V BLDC motor (~450–700 W) | Cavitation is set by throat velocity + downstream pressure, not gpm. Holding pressure while cutting flow ~5× cuts power ~5× — turns an impossible continuous claim into an honest solar-charged **batch** process. |
| 5 | Nozzle | Custom micro-drilled 316 body, unknown bore, whole part is a $150–600 consumable | **316L holder + pressed tungsten-carbide orifice inserts** of known bore | Carbide resists cavitation erosion ~10–50×; a defined bore fixes orifice area (so pressure/flow become predictable); consumable drops to a $15–40 insert. |
| 6 | Clog defense | Single coarse strainer | **Two-stage: coarse basket + 100–150 mesh backflushable screen w/ ΔP gauge** | Micro-bore clogging is the single most likely field failure. Mesh finer than the smallest bore guarantees nothing that passes can lodge. |
| 7 | HP safety | No pressure relief | **Unloader / relief valve** set below hose rating, bypass to drum | Prevents a blocked nozzle from bursting the line; bypass doubles as in-drum mixing. |
| 8 | Instrumentation | LCD voltmeter only; metering borrowed once at commissioning | **Permanent MPPT harvest log + coulomb-counting shunt + HP pressure/flow/watt meters** | Retires the "no power budget exists" flag by *measuring* Wh-in vs. oil-out every run. |
| 9 | Charge control | Generic 12 V PWM controller | **MPPT controller** (Victron SmartSolar 75/15) with programmable load output + LVD | +15–30% harvest from the same panel; free timer + low-voltage-disconnect duty cycling; built-in reverse-polarity protection. |
| 10 | Surge buffer | Unknown-config 2200 F ultracap + a separate 3 F cap (contradictory, arc-weld hazard) | **Deleted on the baseline** (battery buffers the small pump); balanced 16 V module only if a high-inrush motor pump is fitted | Removes an undocumented hazard and ends the ultracap-vs-3F contradiction. |
| 11 | Load switching | 4× Fotek SSR-40 DD (polarity-sensitive, hot, lossy) | **Sealed 40 A automotive/marine relays** (or logic-level MOSFET modules) + Schottky flyback | ~5 W wasted continuously per SSR at 4 A matters on a 45 W budget; sealed relays are marine, cheaper, cooler. |
| 12 | Fusing | None anywhere | **Main terminal fuse (MRBF) + fused distribution block, one fuse per branch** | A 12 V lead-acid/LiFePO4 bus can source fire-starting fault current. Cheapest life-safety fix in the build. |
| 13 | Waterproofing | None (open box, bare perfboard) | **IP66 enclosure, conformal coat, marine glands, drip loops, breather vent** | "Marine-hardened" was unsupported. Water ingress is the top failure mode for a floating box. |
| 14 | Steering brain | Two un-reconciled stacks (BEAM board + discontinued MIT Super Cricket w/ code bug) | **One chosen path: BEAM analog phototrope**; Super Cricket dropped; ESP32 optional for real telemetry | Ends ambiguity, kills the ~$150 obsolete PIC path and the false ~1 m IrDA "telemetry" claim. |
| 15 | Wind turbine | Air-X 400 W, no rectifier/MPPT/dump-load in any schematic | **Dropped from baseline** (solar alone closes the trickle budget); if kept, a **diversion-load controller is mandatory** | Poor value on a low-wind pond; a turbine must never run unloaded. |
| 16 | Oil decant | Fixed weir, hand-timed displacement decanting | **Self-leveling floating weir skimmer** + sight-glass level/interface gauge | A ~1/8-in floating layer can't be reliably decanted over a fixed lip on a raft that moves. |
| 17 | Separation stability | Bare open free surface (gravity separation on a moving raft) | **Internal anti-slosh baffles + skimmer stilling shroud + skim-only-when-calm** | Gravity separation needs a still surface; a moving raft re-mixes the layer. |
| 18 | Emulsion / settling | Ambiguous 15-gal barrel, no de-emulsification | **Defined clear-sided coalescer/settler** (corrugated-plate media) + passive solar warming | Cavitation can throw a stable emulsion; a coalescing pack breaks it with no heat/power. |
| 19 | Final storage | Fully unspecified bladder (capacity, material, ports UNKNOWN) | **Spec'd hydrocarbon-rated TPU bladder OR cheap inert HDPE jerricans** | Removes every UNKNOWN and the swell/leach failure of a plain water bladder. |
| 20 | Documentation | Drawing says "306 S.S." (a nonexistent grade); 6 oz vs 4 oz foam conflict | **316L specified throughout; conflicts resolved or measured** | Correctness. AISI 306 doesn't exist. |

**Design philosophy of the improved edition:** *right-size, measure, protect, and delete.* The single highest-leverage change is right-sizing the cavitation pump (change #4) — it cascades into a smaller motor, longer runtime, higher usable duty cycle, and less erosion. Everything else either measures a previously-asserted claim, protects against the two catastrophic failures (electrical fire, water ingress), or deletes an undocumented/redundant part.

---

## Table of contents
1. [Introduction & how to use this manual](#1-introduction)
2. [Safety](#2-safety)
3. [Tools](#3-tools)
4. [Bill of materials + total cost](#4-bill-of-materials)
5. [Subsystem A — Frame & Flotation](#5-subsystem-a--frame--flotation)
6. [Subsystem B — Fluid & Process (cavitation)](#6-subsystem-b--fluid--process-cavitation)
7. [Subsystem C — Power & Electronics](#7-subsystem-c--power--electronics)
8. [Subsystem D — Storage & Separation](#8-subsystem-d--storage--separation)
9. [Commissioning — the instrumented proof run](#9-commissioning)
10. [Appendix](#10-appendix)

---

## 1. Introduction

The Manatee is a twin-hull catamaran raft. Two slender pontoons carry a stiff deck holding a folding solar array, an (optional, removable) mast-top wind turbine, a 55-gallon reactor/settling drum at the center of buoyancy, and a dry electronics box. It drifts toward the brightest water (a cheap proxy for a surface algae bloom), draws slurry into the drum, concentrates it, and drives it through a multi-jet cavitation nozzle. Cavitation lyses the algae cells; a few percent of organics crack to a floating oil/wax per pass; the light fraction is skimmed to storage and the rest recirculates. Chlorophyll-laden water returns to the pond through a sub-surface tube. **The water leaves cleaner. The wax is a bonus you render into candles ashore.**

### How this manual is structured
Each subsystem section gives: what changed and why, a numbered build sequence, and the parts specific to it. **Where the builder can choose between the improved part and the original**, both are shown and labeled *Route A (improved, recommended)* vs *Route B (keep the original character)*. The manual never forces you off the original concept — it just makes the reliable path the default.

### Two builder decisions to make before you start
1. **Flotation route:** dock floats (recommended) vs. round HDPE pipe (keeps the classic tube look). See §5.
2. **Frame route:** bolted aluminum ladder frame (recommended) vs. *hardened tensegrity* (aluminum members + 316 cable, keeps the tetrahedron signature). See §5.

Everything downstream (drum, plumbing, electronics) is identical regardless of those two choices.

### What is still UNKNOWN and must be measured on your unit
- Actual nozzle **bore diameter and orifice count** on any original part (Route B nozzle) — measure it. On the improved route you buy inserts of a **known** bore.
- **Feed concentration:** process prose says >6% solids; a subsystem doc says ~30%. These disagree ~5×. **Resolve by moisture-balance measurement** at commissioning.
- **Payload weight** (drum fill level, panel weight, battery group) — measure and sum before sizing floats (§5, Step 1).
- **Air-horn annunciators' purpose** — unstated in the source corpus (alarm? bird deterrent?). Confirm intent before wiring them always-armed.

---

## 2. Safety

- **Electrical fire:** a 12 V lead-acid/LiFePO4 bus can source hundreds of amps into a fault. **A main fuse and per-branch fuses are mandatory** (they were absent in the original). Do not energize without them.
- **High-pressure fluid:** the nozzle-feed leg runs at 250–400 psi. Use only pressure-rated hose, and fit the **unloader/relief valve** before first pressurization. A blocked nozzle without relief can burst a line.
- **Ultracapacitor arc-weld:** if you fit the optional high-inrush ultracap module, a discharged 2200 F+ cap looks like a dead short — **pre-charge through a resistor** or it will arc/weld terminals.
- **Two-part pour foam (Route B pipe hulls only):** exothermic and expands hard. Mix small batches, pour in staged lifts, wear gloves and eye protection.
- **Capsize:** a mast-top turbine on a beamy, lightly-loaded hull is the classic tip-over. **Do the dockside inclining test (§9) before deployment.** Make the turbine removable for high-wind days.
- **Vessels are vented, never sealed:** the drum and settling vessel are lidded and vented (gooseneck + screen). The cavitation loop and any decomposition CO₂ need a vent path. **Do not seal them against pressure.**
- **Galvanic corrosion:** isolate every aluminum-to-stainless interface with nylon washers/bushings and anti-seize.
- **Cavitation erosion:** the nozzle is a **wear/consumable part**. Plan a quick-change fitting and inspect it on schedule.

---

## 3. Tools

**Fabrication & assembly**
- Cordless drill + bits; hole-saw set (for drum penetrations and float mounts)
- Metal-cutting saw or chop saw (aluminum tube); PVC cutter; hacksaw
- Sockets/wrenches, torque wrench (for cable clips and structural bolts), Allen keys
- Deburring tool, files, sandpaper
- Tape measure, square, level, marker
- Rivet gun or bolt kit; crimper for ring terminals
- Wire cutters / angle grinder (cable), cable-clip tool

**Electrical**
- Soldering iron; heat-shrink/heat gun
- Multimeter; clamp meter (or rely on the installed SmartShunt)
- Oscilloscope (only if building the BEAM steering board — to verify the microcore oscillates)
- Smartphone (VictronConnect app for the MPPT + shunt)

**Fluid / commissioning**
- Borescope + micrometer (nozzle erosion inspection)
- **Moisture balance** or drying-oven method (to measure feed solids — resolves the 6% vs 30% conflict)
- Graduated cylinder, kitchen/lab scale, stopwatch
- Bucket, water source for leak/level tests

**Route-B-only**
- Sledge is **not** used (the original's sledge-seating of caps is dropped — it crazes joints). PVC primer + cement with proper cure instead.

---

## 4. Bill of materials

Costs are rough, US retail, for a single demonstrator. Where a line is route-dependent or optional, it is marked. **UNKNOWN** = spec must be measured on your unit; do not invent.

### A — Frame & Flotation

| Part | Qty | Route | Rough cost | Notes |
|------|-----|-------|-----------|-------|
| Foam-cored HDPE dock floats (~24×72×16 in, ~600 lb ea) | 2 (or 3) | A (rec.) | $300–500 pair | Size to ≥2× payload. Unsinkable, UV-stable, molded bolt flanges. |
| 12-in HDPE pipe (10 ft) + gasketed/fused caps | 2 + 4 | B alt | $200–450 | Only if keeping round-tube hulls. Fill solid with foam. |
| 2-lb pour foam | 0 / ~2 gal per hull | B only | $0 / ~$120 | Deleted on dock-float route; fill hulls **solid** on pipe route. |
| 6061-T6 aluminum square tube, 2×2 in × 0.125 in wall | ~40–60 ft | A (rec.) | $120–300 | Frame cross-beams + perimeter + center bay. Measure to your beam. |
| 6061-T6 aluminum tube, 2 in (mast) | ~6 ft | both | $25–40 | Dimensioned; set in a bolted base flange. |
| Mast base flange/socket (+ threaded adjuster on Route B) | 1 | both | $15–30 | Removable mast; adjuster sets tensegrity preload to torque. |
| 316 SS structural bolts/nuts/washers + nylon isolation washers + anti-seize | ~40–60 sets | both | $40–70 | Galvanic isolation at every Al/SS interface. |
| 1/8-in 7×19 **316 stainless** cable | ~50 ft | B only | $40–60 | Tensegrity route only. Corrosion-proof in a pond. |
| 1/8-in 316 thimbles + clips (or swageless terminals) | clips 16–24 / terminals 8–12 | B only | $25–100 | Dimensioned terminations (see §5, Step 6). |
| 6-in turnbuckles (316 or hot-dip galv) | 4 | B only | $40–60 | Upper-half tensioners; deleted on Route A. |
| 12 V marine battery box (vented) + straps | 1 | both | $20–40 | Mounts battery **low** as ballast. |
| 316 SS lifting eyes / pad-eyes | 4 | both | $20–40 | Frame-corner lift points ("lift only here"). |
| 6-in domed PVC caps or foam nose cones (cosmetic) + googly eyes | 2 + eyes | both | $20–40 | Manatee face on forward float ends. **Not on the drum.** |
| PVC primer + cement (cosmetic caps only) | as needed | both | ~$15 | Primer THEN cement, proper cure. No sledge-seating. |

### B — Fluid & Process

| Part | Qty | Rough cost | Notes |
|------|-----|-----------|-------|
| HP feed pump — small triplex plunger (AR RKA / Comet FDX class), ~1.5–2.5 gpm @ 250–400 psi | 1 | $130–200 | Replaces RMW2G24D. Confirm delivered P/Q on the rig. |
| Nozzle drive motor — 24–48 V BLDC, ~500–750 W, + coupling/belt | 1 | $120–250 | Needs matching controller (see §7). 24/48 V bus preferred at this power. |
| Tungsten-carbide orifice inserts (waterblast grade), known bore 0.012–0.020 in | 3–4 + spares | $15–40 ea | Defined bore; ~10–50× erosion life over 316. The new razor-blade consumable. |
| Kinetic Nozzle holder — 316L, drilled/tapped for pressed inserts + quick-change coupling | 1 | $100–200 | 316**L**, not the drawing's nonexistent "306". |
| Backflushable screen filter, 100–150 mesh, + differential-pressure gauge | 1 | $65–90 + $25 | Mesh opening < smallest orifice bore. Primary anti-clog defense. |
| Coarse basket strainer (intake) | 1 | ~$20 | First-stage debris capture at the pond. |
| Unloader / pressure-relief valve (pressure-washer type) | 1 | $25–50 | Set below hose rating; bypass to drum. Safety + anti-deadhead + mixing. |
| Inline flow meter (paddlewheel/turbine) + HP pressure gauge + DC watt-meter | 1 set | $75–125 | Permanent instrumentation — every run yields data. |
| Intake / transfer bilge pump (Rule/Mayfair cartridge, 500–800 GPH) | 1 | $25–45 | Low-pressure lift into the drum. GPH: UNKNOWN, match drum turnover. |
| Eductor / venturi (Mazzei 1078/1583 class) | 1 | $30–80 | Aerate/entrain + blend/float toward >6% solids. Sizing: UNKNOWN. |
| UV-stabilized / black 55-gal HDPE drum (open-head, bolt-ring lid) | 1 | $60–130 | Reactor + separator in one. Lidded & vented, **not** pressure-rated. |
| High-pressure hose (3000 psi) + low-pressure hose, barbs, ball valves, tees, check valves | 1 set | $50–120 | Only the nozzle-feed leg must be HP-rated. Runs: UNKNOWN. |
| ~~Circulation / immersion sump pump~~ | 0 (DELETED) | −$40 to −$90 | Removed; unloader bypass + eductor handle in-drum recirculation. |

### C — Power & Electronics

| Part | Qty | Rough cost | Notes |
|------|-----|-----------|-------|
| 45 W 12 V solar panel | 1 | $60–90 | Primary generation. ~120–170 Wh/day realistic. |
| MPPT charge controller — Victron SmartSolar 75/15 | 1 | ~$110 | Replaces PWM. Bluetooth harvest log + programmable load output + LVD + reverse-polarity protection. |
| Battery monitor w/ shunt — Victron SmartShunt 500A (or INA226 module) | 1 | $120 (or ~$15) | Coulomb-counting Wh in/out — the missing power-budget instrument. |
| Battery — 12 V 50 Ah (AGM baseline, or LiFePO4 w/ BMS) | 1 | $130 / $200–250 | Sized for ~2 days autonomy at trickle-rig load. LiFePO4 lighter + BMS safety. |
| Main terminal fuse — Blue Sea MRBF 60 A | 1 | ~$25 | On battery positive post. Size to actual peak load if a big pump is used. |
| Fused distribution block — Blue Sea ST-Blade 6-circuit + negative bus bar | 1 | $30 + $15 | Per-branch fusing. |
| Sealed automotive/marine relays 40 A SPDT (or logic-level MOSFET modules) | 3–4 | ~$6 ea | Replace SSR-40 DD. Near-zero drop, sealed, no heatsink. |
| Schottky flyback diodes — 1N5822 | 3–4 | ~$1 total | One across each inductive load. |
| IP66 enclosure + marine cable glands + Gore breather vent | 1 set | $25 + $10 + $5 | Waterproofing package. |
| Conformal coating — MG Chemicals 422B | 1 | ~$18 | Coat all PCBs. |
| BEAM analog phototrope parts (74HC14, 74HC125, PN2907/PN2222/2N3906, 1N4148, photodiodes, R/C) | 1 board | $15–25 | Steering brain, if thrusters fitted. Public-domain topology. |
| FRONT/REAR thrusters (Minn Kota-class or small 12 V) | 0–2 | UNKNOWN | Only if steering is fitted; sizing to close budget = UNKNOWN. |
| OPTIONAL: 16 V balanced ultracap module (Eaton XLM/XLR) + pre-charge resistor | 0–1 | ~$60 | Only if a high-inrush 1/2-hp motor pump is fitted. |
| OPTIONAL: ESP32 dev board (real Wi-Fi/BLE telemetry) | 0–1 | ~$10 | Replaces obsolete Super Cricket + false IrDA "telemetry". |
| OPTIONAL: small 12 V wind turbine + **diversion/dump-load controller** | 0–1 | $60+ turbine + $60 controller | Dropped from baseline. If kept, dump-load is **mandatory** (never run unloaded). |
| ~~Generic PWM controller, 50A blocking diode, 2200F ultracap, 3F cap, 4× SSR-40, MIT Super Cricket~~ | 0 | −$150+ | Deleted/superseded on the baseline. |

### D — Storage & Separation

| Part | Qty | Rough cost | Notes |
|------|-----|-----------|-------|
| Floating weir surface skimmer head (self-leveling) | 1 | $30–60 | Replaces fixed decant weir. Feeds transfer-pump suction. |
| Internal anti-slosh baffle(s) + skimmer stilling shroud (HDPE) | 1 set | $25–40 | Damps slosh; gives the skimmer a calm pool. |
| Coalescing media pack (corrugated OWS plates / coalescing media) | 1 | $40–80 | Passive, no-power de-emulsification. |
| 15-gal intermediate vessel (clear-sided coalescer/settler, flat-black exterior) | 1 | $40–70 | Defined role: coalesce + settle; bottom drain to S-return. |
| Clear sight-tube level/interface gauge (UV-shielded) | 1 | $15–25 | See the level AND the oil/water interface. |
| Low sidewall bulkhead ball valve (S-return take-off + drain, screened) | 1 | $10–15 | Draws clarified water; doubles as cleanout. |
| Sub-surface "S"-shaped return tube (~1 in Sch-40 PVC + 2 elbows) | 1 | $15–25 | Returns chlorophyll water; inlet below the oil layer. |
| Gooseneck vent + insect/debris screen | 2 | $8–12 | One on drum, one on settling vessel. Lidded & vented, never sealed. |
| Final storage: hydrocarbon-rated TPU bladder (15–25 gal) **OR** 2× 6.5-gal HDPE jerricans + quick-connect tap | 1 set | $350–600 / $60–100 | Removes the UNKNOWN. Jerricans = cheap inert DIY default. |
| Inline suction strainer (protects transfer pump) | 1 | $10–20 | Keeps wax lumps/debris out of the pump. |
| 12 V diaphragm/RV transfer pump — hydrocarbon-compatible (Santoprene/Viton) wetted parts | 1 | $50–130 | Transfer/off-load only. **Never** on the HP loop. |
| Drum penetration fittings (Uniseal / threaded PVC bulkhead, 1–2 in) | 6–8 | $30–80 | Nozzle return, feed, S-return valve, skim line, sight-tube, vent. |
| Flat-black paint (passive solar warming of settler) | 1 | $5–10 | Speeds stratification, zero power. |

### Cost roll-up (single demonstrator, baseline configuration)

| Subsystem | Low | High |
|-----------|-----|------|
| A — Frame & Flotation (Route A dock floats + aluminum frame) | ~$580 | ~$1,050 |
| B — Fluid & Process | ~$700 | ~$1,150 |
| C — Power & Electronics (baseline: solar-only, no thrusters/wind/ultracap) | ~$560 | ~$780 |
| D — Storage & Separation (jerrican route) | ~$340 | ~$630 |
| **TOTAL (baseline)** | **~$2,180** | **~$3,610** |

**Notes on the total:**
- **Baseline** = solar-only power, no wind turbine, no steering thrusters, no ultracap, jerrican storage, dock-float + aluminum-frame routes. This is the honest "prove-it-works" configuration.
- **Add-ons:** wind turbine + dump-load (+$120), steering thrusters + BEAM board (thruster cost UNKNOWN), TPU bladder instead of jerricans (+$300–540), high-inrush ultracap (+$60), ESP32 telemetry (+$10).
- **Route B (tensegrity + pipe hulls)** shifts A downward on materials but adds foam and labor; net roughly comparable.
- Figures exclude tools, shipping, and machine-shop setup for the nozzle holder (one-off CNC of the 316L holder is included in its $100–200 line; expect the low end at quantity).

---

## 5. Subsystem A — Frame & Flotation

**Function (unchanged):** two slender hulls carrying a stiff deck for the solar array, mast turbine, and central reactor drum; "lift only from the bottom" handling; the manatee face on the forward hull ends.

**What changed:** flotation sized to a real payload with 2× reserve using inherently-unsinkable foam-cored floats; a bolted aluminum ladder frame replaces the creep/UV-prone PVC tensegrity (tensegrity kept as a hardened aluminum+316 option); every cable/clip/mast dimension specified; and — the one thing the original never mentioned — stability is de-risked with low-mounted battery ballast, a minimum-beam rule, a removable turbine, and a free dockside inclining test.

### Build sequence

**Step 1 — Fix the payload budget first (do the buoyancy math).**
Before buying anything, tally the real deck load:
- Reactor drum + **design fill level** — a 55-gal drum at ~40 gal water is ~355 lb incl. drum. **Do not plan to run it full (~460 lb) on light hulls.** *(Fill level = measure/decide on your unit.)*
- Solar array — *measure the actual panel; ~30–50 lb typical (UNKNOWN).*
- Mast + wind turbine — ~15–25 lb.
- 12 V marine battery — ~55 lb.
- Supercap/relays/pumps/wiring — ~30 lb.
- Frame + mast + hardware — ~60–90 lb.

Sum = your **payload budget** (rough working figure ~500–600 lb; mark the drum fill, panel weight, and battery group as *measure-on-your-unit*).
**Required pair displacement = 2 × payload.** Required float volume (ft³) = **2 × payload_lb / 62.4** (fresh water = 62.4 lb/ft³).

**Step 2 — Select and lay out the floats.**
- **Route A (recommended):** two foam-cored HDPE dock floats whose combined buoyancy ≥ 2× payload (e.g., two ~24×72×16 in floats ≈ 1,200 lb pair for a ~600 lb budget; add a third float or upsize if the drum runs fuller).
- **Route B (round-tube look):** cut two 10-ft lengths of 12-in HDPE, fill each **solid** with 2-lb foam in ~5 staged lifts (control exotherm), gasket/fuse both end caps.
- Set hull centerline spacing (**beam**) to at least ~5 ft for 10-ft-class hulls (min beam ≈ hull length / 2) for stability.

**Step 3 — Cut and drill the aluminum ladder frame.**
Cut two spanwise cross-beams + a perimeter from 2×2 in × 0.125 in wall 6061-T6 tube (~40–60 ft total; measure to your beam and hull length). Lay out and drill for 5/16 or 3/8 in 316 SS bolts at the float flanges and all frame joints. Deburr every cut and hole.
*Route B (hardened tensegrity):* build the frame perimeter and cross members in the same aluminum tube but leave the cable pad-eye points; proceed to Step 6 for rigging.

**Step 4 — Bolt the frame to the floats with galvanic isolation.**
Bolt the cross-beams down through the dock-float molded flanges (or through-bolt with backing plates on the pipe route). Use nylon washers / isolation bushings and anti-seize at **every** aluminum-to-stainless interface. Torque per bolt spec; the frame should be rigid before any payload goes on.

**Step 5 — Set the mast in a bolted base.**
Bolt a base flange/socket at frame center; set the 2-in aluminum mast in it. On Route A the mast only carries the solar array + turbine (no preload role). On Route B, add a threaded adjuster at the base and proceed to Step 6.

**Step 6 — (Route B tensegrity only) Rig cables to spec.**
Keep the tetrahedron: cut 1/8-in 7×19 **316 SS** for the four lower and four upper legs. Terminate **every** eye:
- Thimble, **turnback 3-1/4 in**, **two 316 clips**, first clip **one saddle-width** from the thimble, clip spacing **~3/4 in**, each nut to **4.5 ft-lb**, **saddle on the live/standing part** ("never saddle a dead horse").
- Equalize the lower X by measured diagonals; then tension the four upper turnbuckles **in opposing pairs, a little at a time**, so the mast stays centered.
- **RE-TORQUE all clips after first tensioning.**
- (Full-strength no-tool alternative: swageless mechanical terminals — Hayn Hi-Mod / Suncor.)
Skip this entire step on Route A.

**Step 7 — Mount the battery low as ballast.**
Fasten the 12 V deep-cycle battery on the frame **low and central**, near the waterline between the hulls, in a vented marine battery box, strapped down. This is deliberate ballast — it lowers CG for free.

**Step 8 — Cradle the drum and mount the deck payload.**
Bolt the drum cradle in the center bay; strap the 55-gal drum in it at deck center (lowest practical position). Mount the folding solar array on the frame and the **removable** wind turbine on the mast top. Route wiring clear of lifting points.

**Step 9 — Bolt on lifting eyes and set the handling rule.**
Bolt four 316 SS lifting eyes to the frame corners over the float mounts. Label them: **LIFT ONLY HERE — never from cables, mast, or solar panel.**

**Step 10 — Dockside inclining test (before launch — see §9).**
Do not skip. This is the cheapest capsize de-risk in the whole build.

**Step 11 — Add the manatee face.**
Bolt two 6-in domed PVC caps (or foam nose cones) as **cosmetic** fairings to the forward float ends; mount the googly eyes there. Keep them off the reactor drum.

---

## 6. Subsystem B — Fluid & Process (cavitation)

**Function (unchanged):** draw pond/algae slurry, concentrate it, drive it through a multi-jet cavitation nozzle into the 55-gal drum, decant the floating oil/wax to storage, recirculate the rest.

**What changed:** the cavitation pump is right-sized for low flow at adequate pressure (the keystone move — cuts hydraulic power ~5× and makes solar-charged batch operation physically honest); the micro-drilled 316 nozzle becomes a 316L holder carrying known-bore tungsten-carbide inserts (kills erosion, cost, and the unknown-bore problem at once); two-stage backflushable filtration attacks the top field-failure (clogging); an unloader valve makes the HP leg safe; permanent gauges turn every run into data; and the redundant circulation pump is deleted.

**The physics, honestly:** cavitation intensity is governed by throat velocity and downstream pressure (the cavitation number), **not** by gpm. Holding ~250–400 psi while dropping to ~1.5–2.5 gpm cuts hydraulic power roughly 5×. To hit the stated ~100 ft/s at an orifice, ideal ΔP ≈ ½ρv² ≈ 67 psi; with a real discharge coefficient (~0.6–0.8) plus line losses, ~150–300 psi — so the process text's 300 psi is physically reasonable. The mechanism (cell lysis + intensified hydrothermal cracking) is real and documented; what is unproven is the *rate* on a small solar budget. **Lead value stays cleaner water; oil/wax is an experimental bonus. No gal/day.**

### Build sequence

**Step 1 — Mount and plumb the reactor drum with weir + bottom drain.**
Set the UV-stabilized/black 55-gal HDPE drum low and central between the hulls. Cut/fit bulkhead fittings for: raw-water intake, HP nozzle feed, cavitation return (**below** the liquid surface), the unloader bypass return, the "S"-shaped sub-surface chlorophyll-water return, an **adjustable overflow skimmer weir** to storage, and a **bottom ball-valve sludge drain**. Seal every penetration with marine sealant.
*Caution:* a leak on the decant port loses product; a leak on the feed port is a high-pressure hazard.

**Step 2 — Install intake + two-stage filtration.**
Mount the 12 V bilge/transfer cartridge (Rule/Mayfair) to lift pond water + surface algae into the drum through a **coarse basket strainer**. Downstream of the drum draw, before the HP pump, install a **100–150 mesh backflushable screen filter whose mesh opening is smaller than the smallest orifice bore**, with a differential-pressure gauge across it.
*Caution:* this is the single most important defense against orifice clogging — the top field failure. Backflush when ΔP rises.

**Step 3 — Fit the eductor for concentration (DAF) + mixing.**
Plumb the Mazzei-class eductor into the recirculation leg so it entrains gas and floats/concentrates the algae toward the **>6%-solids** target. Feed it from the **unloader bypass** so it keeps mixing while the pump idles between batches. A turbidity/light sensor gates when the slurry is dense enough.
*Caution:* **measure actual solids with a moisture balance** — the 6% vs 30% spec conflict must be resolved by measurement, and it sets the whole energy balance.

**Step 4 — Install the right-sized HP feed pump + unloader + instrumentation.**
Mount the small triplex plunger pump and its 24–48 V BLDC motor on the baseplate. Suction from the concentrated-slurry draw (through the fine filter); discharge via pressure-rated hose to the nozzle. Fit the **unloader/relief valve set below the hose rating**, bypassing back to the drum. Install a pressure gauge, inline flow meter, and DC watt-meter **permanently**.
*Caution:* do **not** trust any BOM caption (the "300 psi × 10 gpm 12 VDC" figure doesn't cleanly match real pumps) — read true pressure/flow off the gauges. Undersized pressure = no cavitation; oversized pump = blown budget.

**Step 5 — Install the Kinetic Nozzle with carbide inserts + quick-change fitting.**
Press 3–4 known-bore tungsten-carbide inserts into the 316L holder in the original triangular cluster geometry (one central bore + three surrounding). Thread the holder into the HP leg via a **quick-change coupling** so it discharges **below** the liquid surface. Orient the jet **away** from the drum wall (erosion) and the skimmer/weir zone (re-mixing).
*Caution:* the nozzle is a wear part — cavitation erosion concentrates ~200 µm downstream of the bores. Quick-change lets you pull and inspect it (§9).

**Step 6 — Set the passive separation / decant path.**
Route the "S"-shaped sub-surface tube to return chlorophyll-laden water low/out. Set the **adjustable skimmer weir** so only the floating oil/wax layer overflows to storage — injecting fresh slurry raises the level and the weir passively skims the top. Add a check valve on the storage line.
*(Detailed separation build is in §8 — this step just leaves the ports and the weir ready.)*

**Step 7 — Install the transfer/off-load pump + storage.**
Plumb the 12 V diaphragm/RV pump (~45–55 psi, hydrocarbon-compatible wetted parts) for decant/off-load into the bladder/jerricans. **This pump is transfer-only — keep it strictly OFF the high-pressure loop.**
*Note:* the separate immersion circulation pump is **DELETED** — the unloader bypass handles in-drum recirculation.

**Step 8 — Commission: instrumented closed-loop test (see §9).**
Because the gauges, flow meter, and watt-meter are permanent, every run logs grams oil/wax out vs. Wh in and reads true nozzle pressure/flow directly. Borescope the carbide inserts on schedule to build the erosion service-life curve. **This is the number the whole venture turns on — do not skip.**

---

## 7. Subsystem C — Power & Electronics

**Function (unchanged):** harvest solar, buffer surge, switch the pump + annunciators, steer toward light, instrument the bus.

**What changed:** the two things the corpus most conspicuously lacked — **measurement and protection** — are added. An MPPT controller + coulomb-counting shunt produce a real logged energy balance (retiring the "no power budget" flag) while squeezing 15–30% more from the same panel. Fusing and a sealed enclosure address the two catastrophic failures (fire, water ingress) for pennies. Sealed relays/MOSFETs replace the hot, lossy, polarity-sensitive DC SSRs. The undocumented ultracap is deleted from the baseline. One steering path (BEAM analog) is chosen; the discontinued, buggy MIT Super Cricket is dropped. The unjustified 400 W wind turbine is dropped from baseline.

**Honest framing:** the electronics are a **strength precisely because they are cheap, proven, and un-exotic** — a liability only if oversold as AI. The steering is a public-domain BEAM/Braitenberg analog phototrope. No machine learning, no inference engine, no "3rd-generation Prospero AI."

**Power-budget reality:** generation ~120–170 Wh/day (45 W PV). Baseline load (small duty-cycled pump, no thrusters/lights/electrolyzer) **closes marginally in daylight**. Full-spec load (1/2-hp pump + thrusters + grow-lighting + electrolyzer) does **not** close — it misses by ~10–30×. The improved rig operates as an **intermittent solar-charged batch process**, and the shunt now proves the actual number instead of arguing about it.

### Build sequence

**Step 1 — Mount the sealed enclosure and fused distribution.**
Mount an IP66 junction box **above the splash line**. Inside, install the fused distribution block (Blue Sea ST-Blade) as the switched positive bus and a negative bus bar. Fit a Gore breather vent at the **top** of the box; drill gland holes **low** on a side wall. Bond all module negatives to the negative bar (single-point ground).

**Step 2 — Fit the main battery fuse and battery.**
Install the 12 V 50 Ah battery (AGM baseline or LiFePO4 w/ BMS). Put the MRBF 60 A terminal fuse **directly on the battery positive post** before any wire leaves it. Route battery + through the fuse to the MPPT battery terminal; battery − to the negative bus.

**Step 3 — Wire PV → MPPT (battery-first sequence).**
With the MPPT already connected to the battery (Step 2), confirm panel polarity in sunlight with a meter, then connect the 45 W panel to the MPPT PV terminals. **No external blocking diode needed** — the MPPT has reverse-polarity protection. Pair VictronConnect over Bluetooth; confirm it is harvesting and logging Wh.

**Step 4 — Install the battery monitor / shunt.**
Insert the SmartShunt (or INA226 module) in the battery **negative** path so ALL current in/out passes through it. This is the power-budget instrument: it logs Wh consumed vs. the MPPT's Wh harvested. Keep the old 16×2 LCD voltmeter across the bus as a glance display.

**Step 5 — (High-inrush option only) Add a balanced ultracap module.**
Skip for the diaphragm-pump baseline — the battery buffers inrush. Only if a 1/2-hp motor pump is fitted: connect a **factory-balanced 16 V ultracap module** across the bus **through a current-limiting pre-charge resistor** for the first connection (a discharged module is a dead short and will arc-weld terminals), then bypass the resistor once charged.

**Step 6 — Mount the load switches.**
Mount sealed 40 A automotive/marine relays (or logic-level MOSFET modules) for the pump and each annunciator. Feed each load's positive from a **fused branch**; put a 1N5822 Schottky flyback diode across every inductive load (pump motor, horns). No heatsinking or polarity fuss like the old DC SSRs.

**Step 7 — Wire the loads through the switches.**
Route the 12 V pump and the two annunciators from their switch outputs back to the negative bus, each on its own correctly-sized branch fuse (size to the **load**, not the wire max).
*Caution:* the air-horn annunciators' purpose is **unconfirmed** in the corpus (alarm? bird deterrent?) — confirm intent before wiring them always-armed.

**Step 8 — Configure duty cycling from the MPPT load output.**
Drive the pump relay/MOSFET coil from the MPPT's **programmable load output**. Set day/night + a **low-voltage-disconnect** threshold in VictronConnect so the pump runs on the intended schedule and never over-discharges the battery. This replaces the bare trim-pot perfboard.

**Step 9 — (Steering variant) Build the BEAM analog phototrope.**
If steering thrusters are fitted, build the board: 4.5 V rail, two-photodiode Bright Sensor bridge (2N3906/2N3904), 74HC14 Nv microcore (0.1 µF + 3 M/10 M timing), 74HC125 reversing/halt gates, PN2907/PN2222 H-bridges with 1N4148 flyback to FRONT/REAR thrusters. **Bench-verify on a scope** that the microcore oscillates and the bridges reverse cleanly before water. Skip the Super Cricket entirely; if telemetry is wanted, use an ESP32 instead.

**Step 10 — Seal, bench-test, then wet-test with the logger (see §9).**
Conformal-coat all boards, close and gland the enclosure, add **drip loops** on every entry. Bench-test, then wet-test in a tote/pond and read the SmartShunt: record Wh harvested vs. Wh consumed to prove or disprove the day's energy balance.

---

## 8. Subsystem D — Storage & Separation

**Function (unchanged):** the 55-gal drum is both the recirculating cavitation reactor and the gravity separator; the light oil/wax fraction floats, is skimmed to storage, and the rest recirculates; chlorophyll water returns via the sub-surface S-tube; a settling vessel buffers the product; storage is off-loaded ashore. **The recovered material is a waxy lipid residue — not diesel, not "HVO." Candle rendering is a shore-side after-step.**

**What changed:** the two fragile assumptions in the original — that a thin (~1/8 in) floating layer decants cleanly over a **fixed** weir by displacement, and that the free surface is **still** enough for gravity to work on a moving raft — are both fixed. A self-leveling floating skimmer removes dependence on knife-edge level control; internal baffles + a stilling shroud give the skimmer a calm pool despite motion; a passive coalescing pack in the (now clearly-defined) settling vessel breaks the cavitation emulsion with no heat/power; a sight-glass makes the interface visible; and the fully-unspecified bladder becomes a spec'd part.

### Build sequence

**Step 1 — Prep the 55-gal drum as reactor/separator with defined penetrations.**
Start with a clean open-head UV-stabilized HDPE drum. Lay out and cut penetrations for: (a) nozzle recirculation RETURN (low or wall-directed, never jetting up through the surface), (b) fresh-biomass FEED, (c) a **low sidewall bulkhead VALVE** feeding the sub-surface S-return from the clarified mid-low zone (screened intake), (d) the floating-skimmer skim line, (e) a **UV-shielded clear sight-tube** level/interface gauge (two fittings, top and bottom), and (f) a **gooseneck VENT**. Install Uniseals or threaded PVC bulkhead fittings.
*Caution:* port elevations are UNKNOWN / measure on your unit — the sight tube now lets you set and verify them empirically. Set the decant/skim zone at the top liquid line; the S-tube inlet well below it.

**Step 2 — Install internal anti-slosh baffle and skimmer stilling shroud.**
Fit one or two HDPE baffle plates (or a slotted center tube) to damp bulk sloshing, and build a **stilling shroud** — a short open-top cylinder/sleeve — around the zone where the floating skimmer will sit, so the skim pool stays locally calm while the raft moves. Keep baffles removable or perforated near the bottom for cleanout/drainage.
*Caution:* do **not** fully partition the drum — the recirculation loop must still circulate around the baffle.

**Step 3 — Fit the floating weir skimmer and the sub-surface S-return.**
Mount an off-the-shelf floating weir/surface skimmer head inside the stilling shroud so its intake self-levels at the surface; plumb it to the transfer-pump suction. Separately assemble the ~1-in Sch-40 PVC "S" return off the low bulkhead valve so return water is drawn from the clarified zone and sent back toward the pond/growth side.
*Caution:* verify the skimmer float travels freely and cannot jam against the shroud wall; confirm the S-return intake is screened. If the S-inlet is too high it will siphon off your product oil — keep it clearly sub-surface.

**Step 4 — Plumb the recirculation return from the cavitation nozzle.**
Connect the nozzle discharge into the drum's nozzle-return penetration so treated slurry re-enters the same drum. Confirm the HP pump suction pulls from **LOW** in the drum (heavier un-converted water). Aim the return low or against the wall so it does not re-emulsify the floating layer.

**Step 5 — Set and secure the drum at the center of buoyancy.**
Lower the drum into the frame, centered and low between the hulls; strap/cradle it so it cannot shift underway.
*Caution:* a 55-gal drum is ~460 lb full and dominates raft trim — verify flotation and level after loading (and remember the payload-budget rule from §5: don't run it full on light hulls). An off-center or high drum makes the raft tippy and worsens sloshing.

**Step 6 — Build the intermediate coalescer/settling vessel.**
Set up the ~15-gal vessel as a **passive coalescer**: install a corrugated-plate or coalescing-media pack inside, a bottom water-drain routed back to the S-return, and a top take-off for the coalesced oil/wax to final storage. Paint the exterior flat black and site it in sun for **passive warming** (warmer wax is less viscous and separates faster — free, zero added draw). UV-shield any clear sections; fit its own gooseneck vent.
*Caution:* coalescing media needs periodic cleaning — make the pack removable. Keep solar warming **mild** — excessive gain can soften/stress HDPE.

**Step 7 — Mount final storage and the transfer pump.**
Fix the final storage — a hydrocarbon-rated TPU bladder OR two 6.5-gal HDPE jerricans with a quick-connect off-load tap. Wire in the 12 V diaphragm/RV pump (hydrocarbon-compatible Santoprene/Viton wetted parts) with an inline strainer on its suction. Plumb: **skimmer → pump → coalescer vessel → final storage**; ball valves isolate each leg.
*Caution:* a centrifugal bilge pump will not reliably move semi-solid wax or self-prime — use the diaphragm pump for the oil/wax leg. Do not use a plain water bladder for a lipid product (it can swell/leach).

**Step 8 — Leak-test, level-test, and dry-run the skim in motion (see §9).**
Fill the drum with water, check every penetration, confirm the raft floats level, verify the sight tube reads correctly, run a skim cycle in calm water, then agitate/rock the raft and confirm the baffle + shroud keep water out of the skim path. Gate skimming to calm/moored windows if motion still carries water. Time how long a still surface takes to stratify and how much the coalescer improves it — this is the key unproven step; bench-validate before field use.

---

## 9. Commissioning

Commissioning is not a formality here — it is where the machine's central claims get **measured**. Do these in order.

### 9.1 Dockside inclining test (stability — before anything floats loaded)
1. With everything mounted, float the raft at the dock.
2. Hang a plumb bob from the mast.
3. Place a known weight (e.g., 25 lb) at a **measured** offset from centerline; record the heel angle.
4. Remove it and confirm the raft **self-rights**.
5. Confirm freeboard is near **half the float height** at working load, and heel under load stays **under ~10°**.
6. If it heels too far or floats too low: widen the beam, add a float, or lower the mast/turbine **before** deploying.
*Cost: $0 (plumb bob + a known weight). This catches a tippy hull on the trailer instead of in the pond.*

### 9.2 Electrical bench power-up
1. Confirm bus voltage on the LCD **and** in VictronConnect.
2. Confirm the MPPT **load output cycles the pump** on/off on schedule and cuts off at the **low-voltage-disconnect** threshold.
3. If the BEAM steering board is fitted, confirm it steers thrusters toward a lamp (after the scope check in §7 Step 9).
4. Verify every branch fuse and the main fuse are in place. **Do not proceed without fusing.**

### 9.3 Leak / level / skim-in-motion test (fluid, on water)
1. Fill the drum with water; check every penetration for leaks.
2. Confirm the raft floats level; verify the sight tube reads correctly.
3. Run a skim cycle in **calm** water — confirm the floating skimmer pulls only the top film to the coalescer while the S-return bleeds clarified water back.
4. **Rock the raft** — confirm the baffle + stilling shroud keep water out of the skim path. If motion still carries water, gate skimming to calm/moored windows.

### 9.4 The instrumented proof run (the number the venture turns on)
1. Measure feed solids with a **moisture balance** — **resolve the 6% vs 30% conflict by measurement.**
2. Run a **known mass** of measured-solids slurry around the loop for **N passes** on a metered supply.
3. Because the gauges/flow meter/watt-meter are permanent, log continuously:
   - **Wh in** (pump circuit) vs. **grams of oil/wax out** (skimmed, weighed).
   - True **nozzle pressure and flow** (read off the gauges — never the BOM caption).
   - **Water-quality delta:** turbidity, and if possible N/P reduction (the honest lead value).
4. Pull and **borescope/micrometer the carbide inserts at 24 / 72 / 168 h** to build the erosion service-life curve.
5. Report results honestly: **cleaner water first**; oil/wax yield as an experimental datum, **no gal/day extrapolation.**

*What "success" looks like at this stage:* measurable turbidity/nutrient reduction (the deliverable), a positive but modest oil/wax mass per batch (the bonus), a known insert service life (the consumable-kit economics), and a logged daily energy balance that shows what duty cycle the 45 W panel actually supports.

---

## 10. Appendix

### 10.1 Key dimensions and specs (with honesty markers)
- **Bus:** 12 VDC nominal (24/48 V preferred for the BLDC pump motor — needs its own controller).
- **PV:** 45 W nameplate (~120–170 Wh/day realistic after derating).
- **Battery:** 12 V 50 Ah (AGM or LiFePO4) — ~2 days autonomy at trickle-rig load.
- **Cavitation pump:** ~1.5–2.5 gpm @ 250–400 psi (confirm delivered P/Q on the rig — **do not trust any BOM caption**).
- **Nozzle:** triangular cluster (one central + three surrounding bores) reproduced with carbide inserts of **known** bore (0.012–0.020 in class). *Original-part bore diameter, body length, wall thickness, orifice through-length: UNKNOWN on the source drawings — measure the physical part if replicating Route B.*
- **Drum:** 55-gal HDPE, ~23 in dia × ~34 in tall; lidded and **vented, not pressure-rated**.
- **Settling vessel:** ~15-gal, ~14.5 in dia × ~27 in tall, repurposed as a clear-sided coalescer/settler.
- **Cable (Route B):** 1/8-in 7×19 316 SS; terminations = thimble + 2 clips + 3-1/4 in turnback + ~3/4 in spacing + 4.5 ft-lb + re-torque.
- **Beam:** ≥ hull length / 2 (≥ ~5 ft for 10-ft hulls).
- **Buoyancy rule:** required float volume (ft³) = 2 × payload_lb / 62.4.
- **Oil-layer reference:** the "BEAR Fuel 3%" jar shows a ~1/8-in top layer over ~3-5/8 in of green liquid — the floating fraction per batch is thin, so the skimmer must ride right at the surface (hence the self-leveling weir).

### 10.2 UNKNOWNS to measure on your unit (do not invent)
| Item | Where | How to resolve |
|------|-------|----------------|
| Drum design fill level | §5 Step 1 | Decide + measure; sets payload budget |
| Solar panel weight | §5 Step 1 | Weigh the actual panel |
| Feed solids concentration (6% vs 30%) | §6 Step 3, §9.4 | Moisture balance |
| Nozzle bore diameter (Route B original) | §6 Step 5 | Micrometer the physical part |
| Intake pump GPH | BOM B | Match to drum turnover |
| Eductor sizing | BOM B | Size to slurry flow |
| Hose/line runs | BOM B | Measure the built layout |
| Thruster sizing (if steering fitted) | BOM C | Size to close the power budget |
| Air-horn annunciator purpose | §7 Step 7 | Confirm intent before arming |
| Bladder capacity/material/ports | BOM D | Spec to product volume; use hydrocarbon-rated |

### 10.3 Honest claims firewall (public-facing framing)
- **Lead value = cleaner water** (cell lysis + N/P reduction).
- Wax/candles = **under-indexed bonus**, "experimental until independently tested." Candle rendering is a **shore-side after-step** — no melting/molding gear on the raft.
- **No** gal/day throughput. **No** "diesel / engine fuel." **No** "patented AI" — the steering is a public-domain analog BEAM phototrope. **No** "red tide" / "Sea State 7" / species-selective sensing (it seeks light, a proxy for surface blooms).
- The recovered material is a **waxy lipid residue**, not a fuel. Do not label stored product a fuel.

### 10.4 IP caution
- Both Behrens patents (US 7,302,903; 7,750,494) are **expired/public domain** and never claimed the nozzle geometry — little to infringe on the nozzle itself.
- The **a third-party reference design pyrolizer-separator AutoCAD** is a third-party (a third-party reference design) drawing — **do not reproduce it.** Design the separator around it (this manual does — the coalescer/skimmer packaging here is independent).
- If replicating live cavitation art, design around active patents (ODU 8,778,035, CVAT, Hielscher).

### 10.5 Maintenance schedule (improved rig)
| Interval | Task |
|----------|------|
| Each run | Log Wh in vs. oil-out (SmartShunt); read nozzle P/Q; check ΔP across the fine filter (backflush if high). |
| 24 / 72 / 168 h (commissioning) | Borescope/micrometer the carbide inserts; record erosion. |
| Weekly (field) | Clean coarse strainer + inline suction strainer; wipe the floating skimmer; drain settled biomass via the bottom valve. |
| Monthly | Inspect carbide inserts; re-torque frame bolts; check galvanic-isolation washers; inspect conformal coat + glands for water ingress. |
| Seasonal | Replace carbide inserts as the erosion curve dictates; clean coalescer media; inspect cable terminations (Route B) and re-torque. |

### 10.6 Route A vs Route B quick reference
| Decision | Route A (improved default) | Route B (keeps original character) |
|----------|----------------------------|-------------------------------------|
| Hulls | Foam-cored HDPE dock floats | 12-in HDPE pipe filled **solid** with foam |
| Frame | Bolted 6061-T6 aluminum ladder | Hardened tensegrity (aluminum members + 316 cable + turnbuckles) |
| Mast | Structural only, bolted base | Sole compression strut, base preload adjuster |
| Nozzle | 316L holder + carbide inserts | (still recommended over micro-drilled 316; if replicating the original, measure the bore) |
| Storage | HDPE jerricans (cheap, inert) | TPU hydrocarbon bladder (collapses as it empties) |

---

*End of IMPROVED manual. For the faithful original design, see the AS-BUILT edition. For the first-hand engineering read of the models, drawings, and circuits, see `00-GROUNDING.md`.*
