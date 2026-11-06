# Energy Systems (turbine, solar, electrolysis, power & propulsion)

*Due-diligence dossier — Solaris Cybernetics / Barsoom Engineering "Mobula" / EVIE-2c. Prepared 2026-06-17.*
*Scope: power generation, electrolysis/H2, energy storage, station-keeping propulsion, and the whole-system power budget — generation vs. load.*

---

## What it is (plain language)

The Mobula is supposed to be an unmanned floating raft that grows algae and turns it into diesel-like fuel while drifting at sea, with no fuel input and no crew. Everything onboard — the grow lights, the air bubblers, the pumps, the navigation brain, and the thrusters that keep it pointed at the sun — is meant to run entirely on power it harvests from the environment. The energy subsystem is the part that makes or breaks that promise: if the robot can't generate more electricity than it consumes, the whole "self-fueling ocean farm" idea collapses.

The design tries to gather energy four ways at once. A **wind turbine** on a central mast catches the breeze. A **solar panel** (or panels) catches sun. A **thermoelectric (Seebeck) generator** is supposed to scavenge waste heat off the hot fuel-conversion nozzle and turn that temperature difference into a trickle of electricity. And the fuel itself is an energy store — the robot is, in effect, its own battery, banking diesel in a bladder. For short-term electrical buffering it carries a battery bank (the older docs say 48V NiCad; the BOMs and newer renders show capacitors and a small DC battery). Propulsion is deliberately propeller-free: instead of a spinning prop that would foul in seaweed, the robot uses electric trolling-motor thrusters and water jets, plus a passive "whale tail" vane that flaps in the waves for free forward push.

The honest framing for an investor: this is a **multi-source energy-harvesting raft with a very ambitious load list**. The generation hardware is all real, off-the-shelf, and modest (tens to low-hundreds of watts). The load list — 14 hours/day of grow lights over a large area, continuous aeration, a high-pressure cavitation pump, dewatering, and two trolling motors — is large. The central unanswered question of the entire project lives here: **does the power budget close?** The documents assert it does. The numbers, assembled below, say it does not — not without either shrinking the loads by an order of magnitude or growing the generation by one.

---

## How it works (the real mechanism, with numbers)

### Generation hardware (from the bills of materials and renders)

The two BOMs in the corpus are the hardest documented spec for this subsystem:

- **JT-1 BOM** (`JT1BOM_strings.txt`): `400 watt Air-X wind turbine` + `45 watt PV panel` + `1/2hp 12vdc motor` + `300psi x 10gpm 12vdc pump` (a linked AR RMW2G24D pressure-washer pump) + `12vdc pump w/eductor` + `LVKN nozzle` + `500 gallon flexible bladder`.
- **VBShdl-1bM10 BOM** (`VBShdl1BOM_strings.txt`): `45 watt PV panel`, generic `wind turbine`, `Minnkota 55# thrusters`, `12vdc pump w/eductor`, `LVKN nozzle`, `Super Cricket Robotic controller`, `6× SSR-100 DD` solid-state relays, `3 farad capacitor`, `50 amp diode`, `light sensors`, `LED-lamp driver`.

So the baseline generation is roughly **one 400W-nameplate micro wind turbine + one 45W solar panel**, buffered by capacitors and a small DC battery, feeding a 12VDC bus. The Seebeck "630°F vortex heat" generator from `POWER_AND_PROPULSION.md` does not appear in either BOM — it is asserted in the subsystem write-up but not specified as a purchased part.

The **scaled-up render** `SF-1DX4aurora1c.png` (2016) labels a much larger spec: **"PV 600 watts"** and a second source labeled **"VSCV 410 watts"** (a vertical-axis / cross-flow turbine), with the turbine called *"retractable, upgradeable, expandable."* So the project has two generation tiers: a ~445W prototype tier (BOMs) and a ~1,000W+ aspirational tier (the larger SketchUp scenes).

### The "bimodal turbine"

The PRIME thumbnails resolve what "bimodal" means. `VBShdl-1m5manatee2b1PRIME_BimodalTurbine.png` shows a **horizontal-axis rotor (HAWT) mounted crosswise on the top of the central mast** — a propeller-on-a-stick, red blades, above the growth drum. The companion `VBShdl-1m5manatee2b1PRIME.png` (same hull, no turbine fitted) shows the bare mast with a small **flat solar array** near the top. "Bimodal" almost certainly means the mast-top rotor is meant to run in **two flow regimes**: as a **wind** turbine in air and as a **water/tidal** turbine when conditions favor it (or, in the kindest reading, the platform supports either a wind rotor or a submerged current rotor on the same mast/bearing). This is a notable departure from the older docs, which specified a **vertical-axis** turbine (Savonius rotor in `vc310B.txt` Ch. 6; "Vertical Axis Turbine, bird-safe" in `POWER_AND_PROPULSION.md`). PRIME flips to a **horizontal-axis** rotor — losing the omni-directional, no-yaw advantage that was the original VAWT's whole point at sea.

### Electrolysis / H2 for hydrogenation

`Electrolyzer.png` and `Electrolyzer.skp` (2013) document a small upright electrolysis stack. Its role in the energy story is **chemical, not electrical generation**: the fuel pathway (HVO-style / "9x9-HVO," `9x9HVO_process.txt`, `LVKNprocess.txt`) is *hydrous pyrolysis* of algae, and to upgrade raw bio-oil toward a stable, high-cetane diesel you need **hydrogen for hydrogenation/hydrodeoxygenation**. The electrolyzer is the intended onboard H2 source, splitting water with surplus electricity. Critically, **electrolysis is a large electrical sink, not a source** — every gram of H2 made onboard costs ~50–55 kWh/kg at the cell, which must come out of the same 445W generation budget. The corpus contains no energy accounting for the electrolyzer at all.

### Propulsion & station-keeping

- **Thrusters:** two `Minnkota 55#` electric trolling motors (12V). A 55-lb-thrust Minnkota draws ~**50A at 12V ≈ 600W at full**, ~100–250W at moderate continuous thrust. Two of them: 200–1,200W depending on duty.
- **Jet/eductor:** `POWER_AND_PROPULSION.md` claims a "200 GPM centrifugal main pump," "6 vector-controlled jet ports," and **"10,000 lbs total static thrust."** That thrust figure is wildly inconsistent with two 55-lb trolling motors (110 lb combined) and is not supported by any BOM part. Treat the 10,000-lb claim as marketing.
- **Whale tail:** a passive oscillating vane for "free" wave-driven forward motion. Plausible in principle (wave-foil propulsion is real — see Wave Glider), unquantified here.
- **Nav strategy:** "Prospero AI / Drift & Correct" — minimize thruster use by drifting and only correcting occasionally. This is the *right* instinct given the power problem, and is consistent with the established phototaxis controller (steer toward brightest light, run thrusters intermittently).

### The cavitation pump as the dominant electrical load

The fuel conversion runs a **300 psi × 10 gpm pump on a 1/2 hp (~370W) 12VDC motor** (JT-1 BOM). `LVKNprocess.txt` gives the energy theory: accelerating 1 gallon to 100 ft/s costs *0.06 hp·gal (204.84 BTU)*; at 3% conversion per pass, 6,828 BTU in per gallon converted; product = 127,000 BTU/gal; therefore conversion energy = **5.34% of energy produced.** This is the headline energy-balance claim and it is the project's keystone. (Physics critique below.)

---

## New-vs-old (what the 2024 PRIME / EVIE-2c design changed for THIS system)

| Element | Old (2008–2016 docs / BOMs) | New (2024 PRIME / EVIE-2c, .skp + thumbs) | Significance |
|---|---|---|---|
| **Turbine type** | Vertical-axis (Savonius `vc310B.txt`; "VAT bird-safe" `POWER_AND_PROPULSION.md`); "VSCV 410W" cross-flow in `SF-1DX4aurora1c.png` | **Horizontal-axis rotor on mast top** (`..PRIME_BimodalTurbine.png`); "+BimodalTurbine" variant file (`VBShdl-1m5manatee2b1PRIME+BimodalTurbine.skp`, Jul 2024) | Regression for marine use: HAWT needs to yaw into wind and is less tolerant of turbulent, gusty, heeling sea conditions than the original VAWT. "Bimodal" (wind+water on one rotor) is novel but undocumented as to how mode-switching works. |
| **Hull / mounting** | Twin 14" PVC pontoons, flat raft | Twin pontoons **+ tensegrity frame + amphibious wheels at pontoon ends** (`..PRIME.png`) | Wheels add a beach/launch capability (consistent with 2025 `LiftingInstructions.JPG` "lift from bottom at corners only"). Energy cost of amphibious drive is unaddressed — there is no wheel motor in any BOM. |
| **Solar** | 45W single panel (BOMs); "600W PV" aspirational (`SF-1DX4aurora1c.png`) | Small flat array near mast top in PRIME render; flexible "Wing flexible solar" HDPE-mounted in VBShdl BOM | Still tiny relative to load. No panel-area or wattage label on the PRIME thumbnails — can't confirm an upgrade. |
| **Storage** | 48V NiCad bank (`POWER_AND_PROPULSION.md`) | 3-farad capacitor + small 12VDC battery (BOM); capacitors visible in `SF-1DX4aurora1c.png` | A 3F capacitor stores ~0.2 Wh — a smoothing/buffer element, **not** energy storage. NiCad bank is named but never sized. Real overnight storage is undocumented. |
| **Electrolyzer** | Present since 2013 (`Electrolyzer.skp`) | Carried forward; still no energy budget | The H2/hydrogenation load remains entirely unaccounted. |

**Bottom line on new-vs-old:** PRIME/EVIE-2c is mostly a *structural/mechanical* refresh (tensegrity frame, amphibious wheels, mast-mounted HAWT, lifting/rigging instructions). It does **not** resolve any of the energy-balance problems flagged in the 2026-01 prior review, and the VAWT→HAWT switch arguably makes marine wind capture worse.

---

## Evidence & maturity (documented/built/tested vs. asserted)

**Built & physically demonstrated (strongest evidence):**
- The **2015 farm-pond prototype** (`DX5b+notes1.jpg`) is the one piece of real-world energy data. Behrens' own caption: *"This is paraffin floating on the water because the storage tank overflowed… around 2 cups all together. The robot was producing over 1 cup per hour, or 1.33 gallons per day… produced that with a 1/100 HP pump, powered by a 0-watt solar panel and a 0-watt windmill."* The "0-watt" language reads as **the smallest available panel/turbine** (i.e., a token trickle), and the pump is **1/100 hp (~7.5W)** — *fifty times smaller* than the 1/2 hp pump in the JT-1 BOM. So the demonstrated device ran a tiny pump on a tiny trickle of power and produced a tiny amount of waxy paraffin (not finished diesel) in a freshwater pond.
- The **2023 marina test** rig (`LiftingInstructions.JPG`, dated Dec 2025 file) shows a real PVC raft with solar panel, mast/turbine, wired control box — built hardware, lift instructions, but no published energy or fuel output.

**Specified but not shown working:**
- 400W Air-X turbine, 45W panel, 1/2 hp 300psi pump, Minnkota thrusters — all real catalog parts, never shown integrated and power-balanced on water.

**Asserted only (no part, no test):**
- Seebeck generator on the "630°F vortex heat" nozzle (no BOM line, no measured ΔT).
- 10,000 lb static thrust; 200 GPM main pump.
- 48V NiCad bank capacity; overnight energy storage.
- The entire **closed power budget** — there is no document anywhere in the corpus that lists watt-hours generated/day against watt-hours consumed/day.

**Maturity verdict for the energy subsystem: built-untested at small scale; modeled-only at full scale.** A trickle-power device demonstrably made wax. The full-spec energy system (grow-light-bearing, thruster-bearing, electrolyzer-bearing) has never been assembled or measured.

---

## Validation status (what current science says — PLAUSIBLE / DUBIOUS / FALSE)

**Generation claims:**

- **"400W Air-X wind turbine"** → *DUBIOUS as an average power source.* The AIR-X's 400W is a nameplate at ~10–12.5 m/s. Wind power scales with the cube of speed; at a realistic open-water mean of 5–6 m/s the same machine delivers only a small fraction of nameplate — typically tens of watts average, not 400W. AIR-X turbines are also historically known for over-speed/regulation issues and modest real yield in low wind. Plan around **~30–80W average**, not 400W. ([Southwest Windpower AIR-X manual](https://technosun.com/descargas/SOUTHWEST-AIR-X-manual-EN.pdf), [nooutage.com AIR403](https://nooutage.com/air403.htm))
- **"45W solar panel"** → *PLAUSIBLE as spec, marginal as supply.* 45W peak → ~5–7 W average over 24h at sea after marine derating, fouling, and night. Real, but trivially small vs. load.
- **Seebeck on nozzle heat** → *PLAUSIBLE but tiny.* Thermoelectric modules convert at ~5–8% efficiency; a small ΔT scavenger off a nozzle yields watts, maybe low tens of watts at best — a rounding error against the load.
- **"Bimodal" wind+water on one HAWT rotor** → *DUBIOUS.* Air and water differ in density by ~800×; a rotor/airfoil optimized for one is badly matched to the other, and a single generator can't be efficient across both regimes. Switchable wind/current platforms exist as concepts but not as a single shared rotor. Mechanism undocumented.

**The keystone cavitation energy balance:**

- **"Cavitation reaches 1500°F / 12,000 K"** → *PLAUSIBLE as transient physics.* Peer-reviewed sonoluminescence work confirms collapsing cavitation bubbles momentarily reach ~5,000–12,000 K and ~300–500 bar. ([Sonoluminescence — Wikipedia](https://en.wikipedia.org/wiki/Sonoluminescence); [Cavitation bubble temperature minireview, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8960979/))
- **"Stable 15,000 rpm zone at absolute-zero pressure, 1500°F, 1000 Å diameter"** → *FALSE as described.* The extreme conditions in cavitation are **picosecond-duration, sub-micron, stochastic collapse events** — not a steady-state rotating reactor you can hold at "15,000 rpm." **"Absolute zero pressure" is physically meaningless** (the floor is hard vacuum, 0 Pa; pressure can't go below it). The "tetra-helical vortex / worm-like energy exchange" narrative is unfalsifiable hand-waving, not a measured flow field.
- **"3% conversion per pass; net cost 5.34% of energy produced; 127,000 BTU/gal"** → *DUBIOUS-to-FALSE (extraordinary claim, no independent data).* This is effectively a claim of cheap, continuous, **net-energy-positive** fuel synthesis from cavitation. There is **no peer-reviewed evidence** that hydrodynamic cavitation produces net-positive liquid fuel; cavitation is used industrially for *mixing, emulsification, and pre-treatment* (e.g., biodiesel transesterification intensification), where it **saves a little process energy on an already-energetic feed** — it does not manufacture energy. The 5.34% figure also conveniently counts **only** the pump-acceleration energy and ignores: the latent heat to raise the entrained water to supercritical conditions, pump and motor inefficiency at 12VDC, the grow-light energy that produced the biomass, dewatering, and electrolysis for upgrading. Energy-balance is drawn around the most favorable boundary. The 127,000 BTU/gal product is also **paraffin/raw bio-oil**, per the prototype caption — not finished 127k-BTU diesel.

**Power budget (the decisive test):**

- **LED grow lights, 14 h/day** → *DUBIOUS that renewables can power them.* Standard horticultural LED density is **20–40 W/ft²**. Even a modest **100–150 ft² growth area → 2,000–6,000W of lighting**, for 14h/day = **28–84 kWh/day**. Algae photobioreactors targeting useful PPFD (200–600+ µmol/m²/s) need comparable or higher irradiance. ([LED Grow Lights Depot — watts/ft²](https://www.ledgrowlightsdepot.com/blogs/blog/16326275-how-many-led-watts-are-required-per-square-foot-of-grow-space))
- **Generation total:** 400W turbine (~30–80W real) + 45W panel (~5–7W avg) + Seebeck (~tens of W) ≈ **~50–150W average, call it ~2–3.6 kWh/day.**
- **Load total (conservative):** grow lights 28–84 kWh/day **alone**, before bubblers, dewatering, the 370W cavitation pump (~8.9 kWh/day if continuous), nav, and 2× Minnkota thrusters (each ~0.6 kWh per hour of moderate use).

**The gap is roughly 10× to 30×.** Generation supplies single-digit kWh/day; the lit-grow-chamber load alone is tens of kWh/day. **The power budget does not close by about an order of magnitude.** This is the single most important finding in the energy dossier and it is consistent with the prior review's "physically unverified" verdict.

> The only way the documented prototype "worked" is that it *didn't run the hard loads*: the 2015 device used a ~7.5W pump, a token panel/turbine, **sunlight (not LED) for growth**, and produced wax slowly. Scale the loads up to the EVIE-2c spec and the generation has to scale ~10–30× — which the renders gesture at ("600W PV," "expandable" turbine) but never deliver.

---

## Red flags & open questions

1. **No power budget exists anywhere in the corpus.** For an energy-autonomous robot, the absence of a single generated-vs-consumed watt-hour table is the central red flag.
2. **Grow-light load vs. generation is ~10–30× short.** Either the grow area is far smaller than implied, or the robot must rely on **ambient sunlight through the Lexan dome** (in which case 14h LED supplementation is fantasy at sea), or generation must grow by an order of magnitude.
3. **"Absolute zero pressure" and "stable 15,000 rpm cavitation zone" are physically wrong.** The underlying transient cavitation physics is real; the steady-state reactor described is not. This wording will fail any expert technical review instantly.
4. **5.34% energy cost is a boundary-drawing trick** — it omits latent heat, motor/pump losses, lighting, and upgrading. The honest system-level energy return is unmeasured and likely far less favorable.
5. **VAWT→HAWT regression.** PRIME's mast-top horizontal rotor is worse for omni-directional, gusty marine wind than the original vertical-axis design. The "bimodal" wind+water claim has no described switching mechanism.
6. **Electrolyzer is a hidden load, never budgeted.** Onboard H2 for hydrogenation is energy-expensive (~50 kWh/kg H2) and competes directly with the already-deficient budget.
7. **Storage is undersized/undefined.** A 3F capacitor is a buffer (~0.2 Wh), not storage. The 48V NiCad bank is named but never sized. Overnight operation (lights off, thrusters drifting) is unmodeled.
8. **Thrust inconsistency.** "10,000 lb static thrust" vs. two 55-lb Minnkota motors (110 lb) — a ~90× discrepancy that undermines confidence in all stated specs.
9. **Prototype output is paraffin/wax, not diesel** — and was produced in **freshwater**, not seawater (salt, biofouling, and corrosion are unaddressed in the energy/propulsion hardware).

---

## Concrete improvements (buildable upgrades + cheap de-risking experiments)

**Cheap experiments that settle the big questions for <$2k each:**

1. **Bench the cavitation pump's real energy balance.** Run the JT-1 spec pump (AR RMW2G24D, 300psi×10gpm) on a measured wattmeter through the LVKN nozzle with an S3 algae slurry. Measure: kWh in, mass of hydrocarbon out, HHV of product (bomb calorimeter). One afternoon. This either validates or kills the 5.34% claim with a number. **Highest-leverage test in the whole project.**
2. **Instrument the 2023 marina rig.** Add a $30 INA226 power-logger on the 12V bus and a pyranometer + anemometer. Log generation vs. load for one week. Produces the missing power budget directly.
3. **Measure the Seebeck output.** Clamp a TEG module to the running nozzle, log watts at the real ΔT. Confirms or deletes that source.

**Buildable upgrades that actually move the budget:**

4. **Replace 14h LED grow with sunlight-primary growth.** At sea the only sane lighting strategy is **maximize transparent surface area and grow on daylight**, using LEDs only as a small night-trim — or drop night-lighting entirely and accept slower doubling. This is the single biggest load-killer.
5. **Go big and flexible on PV.** Pontoon-deck and dome-skin flexible monocrystalline film could realistically host 600–1,200W of panel on a 12–15 ft platform — matching the aspirational "600W PV" label and 5–10×-ing the real generation. PV is the only source here that scales cleanly with the robot's surface area.
6. **Right-size storage.** Swap the capacitor/NiCad story for a sized LiFePO4 bank (marine-tolerant, deep-cycle) explicitly sized to carry the overnight drift + dawn restart. State the kWh.
7. **Keep the VAWT.** Revert PRIME to a vertical-axis rotor (or a Savonius/Darrieus hybrid) for no-yaw, gust-tolerant marine wind — the original instinct was correct.
8. **Embrace "drift-and-correct" hard.** Duty-cycle the thrusters to near-zero (true Wave-Glider-style station-keeping on the passive whale-tail foil) so propulsion stops competing with the fuel pump for the budget.
9. **Defer onboard electrolysis.** Upgrade/hydrogenate fuel at port where grid H2 is cheap, rather than carrying the electrolysis load at sea. Makes the at-sea budget close far more easily.

---

## Kit/license angle (what's sellable / licensable, and why)

**The cleanest sellable products are the parts that are real, cheap, and don't depend on the unproven cavitation physics:**

- **"Energy-harvesting research raft" kit.** The documented PVC-pontoon + tensegrity-frame + 45W solar + micro-turbine + 12V controller + Minnkota-thruster platform is a genuinely buildable, education-friendly autonomous surface vehicle. Sold as a STEM / maker / ocean-sensing platform (decoupled from the fuel claims), it has a real market — and it matches Behrens' own Virgo City "hands-on biosphere for schools" framing (`vc310B.txt`). The BOMs already exist; this is a near-ready kit.
- **The phototaxis solar-seeking control board** (Super Cricket / LOGO controller + 6 light sensors + SSR thruster drivers) is a tidy, licensable "solar-tracking autonomous boat brain" module on its own.
- **The "bimodal" mast** as a configurable wind-OR-current generation mount is patentable/licensable **if** the switching mechanism is actually designed and demonstrated.

**The 2022 patent-license template** (`2022PatentLicenseEditableGENERAL...`) is already structured for exactly this: a **non-exclusive, worldwide, royalty-on-gross-sales** license on the "Patented Portion" (the cavitation nozzle / LVKN conversion). That is the IP Behrens most wants to monetize — but it is also the **least validated** piece. **Recommendation:** license/sell the *raft + control + harvesting kit* now (built, honest, low-risk), and gate any license of the **cavitation conversion IP** behind the bench energy-balance test (#1 above). Selling the fuel-physics license before that number exists would expose buyers — and the agency's credibility — to the one claim most likely to be false.

---

*Files cited: `JT1BOM_strings.txt`, `VBShdl1BOM_strings.txt`, `LVKNprocess.txt`, `9x9HVO_process.txt`, `POWER_AND_PROPULSION.md`, `ENVIRONMENTAL_CONTROL.md`, `vc310B.txt`, `2022PatentLicenseEditableGENERALforPACKAGE.txt`, `DX5b+notes1.jpg` (2015 prototype), `LiftingInstructions.JPG` (2023/2025 rig), `SF-1DX4aurora1c.png`, `VBShdl-1m5manatee2b1PRIME.png`, `VBShdl-1m5manatee2b1PRIME_BimodalTurbine.png`, `Electrolyzer.png`. Web validation: Southwest Windpower AIR-X manual; Sonoluminescence (Wikipedia) + cavitation-temperature minireview (PMC8960979); LED Grow Lights Depot watts/ft².*
