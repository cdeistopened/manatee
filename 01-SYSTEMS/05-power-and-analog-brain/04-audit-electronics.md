# Electronics & Analog Circuits

*Due-diligence dossier — Mobula / EVIE-2c (Solaris Cybernetics / Barsoom Engineering). Reverse-engineered from the schematic images, BOM strings, Logo source, and the 2024 PRIME SketchUp previews. Last updated 2026-06-17.*

## What it is (plain language)

The "brain" and nervous system of this robot are not exotic. Strip away the "3rd Generation Prospero Artificial Intelligence" marketing language in `MASTER_CONTROL_AI.md` and what's actually on the bench is two well-known hobby-robotics building blocks bolted together:

1. **An off-the-shelf educational robot controller** — the **MIT "Super Cricket V1.0" (© 2006 Fred G. Martin)**. The schematic `supercx-sch.pdf` is literally Fred Martin's EAGLE file (the title block reads `/Users/fredm/Documents/eagle/supercx/supercx.sch` and `fredm@alum.mit.edu`). It's a PIC-microcontroller board that runs a tiny dialect of the **Logo** programming language ("Cricket Logo"). This is what executes the 6-light-sensor phototaxis code. It is a known, documented, classroom-grade device sold by Gleason Research — not a proprietary AI.

2. **A pile of analog "Braitenberg / BEAM" steering circuits** — `LowellAI.png`, `basicJT1-AI.bmp`, and `VBSXv2schematic.jpg` are three generations of a classic light-following analog circuit lineage. The robot reads light on photodiodes/photocells and steers two thrusters toward the brightest direction. No machine learning, no inference engine, no neural net — just comparators and transistors. The "JT" in the filenames is **not** a Joule Thief; in context it's the inventor's "JT-1" model designation (the JT1 BOM is a *whole-vehicle* parts list — HDPE frame, wind turbine, pumps — not a circuit).

In short: the electronics are real, buildable, and largely *copied from public hobbyist designs*. The achievement here is integration and packaging, not circuit invention. The "AI" claim is the single biggest overstatement in the entire electronics story.

## How it works (the real mechanism, with numbers)

There are **two parallel, redundant control philosophies** in the corpus — a digital one and an analog one — and the documents never fully commit to which actually flies.

### A. The digital path — Super Cricket + Logo phototaxis (the "production" intent)

- **MCU:** The Super Cricket carries **three Microchip PIC16C715** 8-bit microcontrollers (U1, U6, U10 in `supercx-sch.pdf`) — one main, two as a sensor/motor "bus" expander — plus a **24LC32 I²C EEPROM** (U2) for stored programs, a **4 MHz and an 8 MHz crystal**, and a **TFDU4100 IrDA transceiver** (U3) for the "real-time telemetry" link. Power is a **78L05** 5 V regulator (the note on the sheet: *"Use a 78L05 instead of diode to support variable main power supply"*).
- **Motor drivers:** Two **L293D** quad half-bridge driver ICs (U4, U12) drive up to 4 DC motors (MOTOR-A…D) with the usual `74HC32` OR-gate steering logic. Each motor port has an LED + 1 kΩ indicator.
- **Sensors:** Six analog sensor headers (SENSORC…F + two more), feeding the PIC ADC/comparator inputs. These are the `a`–`f` light sensors in the Logo code.
- **The "AI":** `AIsourcecode1.txt` is a complete **Cricket-Logo** program (~78 lines). It is a textbook **reactive Braitenberg vehicle**:
  - `avgread` polls the 6 sensors three times each, averages them, and finds the brightest (`setfinal 1…6`).
  - `lightsensedirection` then drives the two thrusters (`a` / `b`) `thisway`/`thatway` to rotate toward that brightest sensor, with a low-light "sleep" branch (`if 20 > (a+b+c+d+e+f/6) [setfinal 0]` → motors off, `wait 9000`). This is the "Drift & Correct" power-saving strategy named in `MASTER_CONTROL_AI.md`.
  - **Bug worth noting:** every averaging line reads `(x + y + z / 3)` and every comparison reads `a > (b+c+d+e+f/5)` — Logo has no operator precedence rescue here, so only the *last* term is divided. The "average" is mathematically wrong as written. It still *works* as a crude winner-take-all (the raw `a` term dominates), but it is not the average the author thinks it is. This is a real, citable code defect, not a transcription artifact.

### B. The analog path — three generations of BEAM/Braitenberg steering

This is the lineage the filenames track, oldest to newest:

- **`basicJT1-AI.bmp` (2012, "JT-1"):** A pure-analog **solar BEAM photovore**. It has a **Basic Stamp socket** (J1, BS3…BS14 lines) but the steering intelligence is analog: two **CdS photocells (CdS1/CdS2)** into a **TLC27L2 dual op-amp** (U1A/U1B) configured as a comparator pair (Fwd/Rev outputs), an **MC34164** voltage supervisor (VR1) gating a solar "store-and-dump" engine into a **1000–2000 µF** reservoir cap (C1), and **discrete transistor H-bridges** (Q1–Q17: 2N3904/2N3906-class NPN/PNP pairs) driving "MOTOR" and "MOTOR SERVO." Everything is rail-labeled "Solar." This is the Solarbotics/Mark-Tilden cookbook, near-verbatim.
- **`LowellAI.png` (the cleanest, fully-specified analog board):** A symmetric two-channel phototaxis circuit with a **published BOM right on the image**: 2× **1381** (the canonical Solarbotics CMOS voltage-trigger), 2× photodiodes, 2× **2N3906** + 2× **2N3904**, 2× 2.2 kΩ, 2× motors, 1× 100 kΩ pot, 1× solar cell, optional 0.22 µF / 680 kΩ. A **4700 µF** reservoir cap. The two `1381`/transistor-pair channels act as left/right "solar engines," each fired by its own photodiode — the classic dual-engine photovore. Clean, real, ~$15 of parts.
- **`VBSXv2schematic.jpg` (2019, "VBSX v2"):** The most ambitious analog board — a **Tilden "Nervous Net" (Nv) microcore walking machine** re-skinned for a boat. Hand-drawn, color-blocked into: *Phototropism Oscillator/Threshold*, *Tactile Sensor Conditioning* (left/right "Tact" bump inputs), a 4-neuron *Microcore Core Walking Loop*, a *Turning* block, and **Front/Rear motor** outputs. `BasicJT2-AI.JPG` is the matching clean redraw: a **74HC14/74HC125**-based Nv microcore ("MicroCore" with Nv1–Nv4 delay stages, 0.1 µF + 3M/10M timing), a **photo bridge** (2N3906/2N3904 + PD1/PD2 "Bright Sensor"), and **PN2907/PN2222/2N3906 discrete H-bridges** with 1N4148 flyback diodes for FRONT and REAR motors, plus a "Reversing Mux" and a "Halt" gate. This is a CMOS-logic BEAM nervous net — again, a known public topology (Tilden Nv nets, Wilf Rigter–style), not original silicon.

### C. The actual 2015 pond prototype wiring (`photoschematicAssembly1b.jpg`)

The real-world photo-assembly is cruder than any schematic above and is the best evidence of what was *built*: a **2200 µF "Ultimate Power" supercap**, a **45 W solar panel**, a **16×2 LCD voltmeter module**, a generic **12 V LCD charge controller** (the small green-boxed sub-schematic, an off-the-shelf 12 V battery charger/solar regulator), a **bus-bar distribution block**, **four Fotek SSR-40DD solid-state relays** (DC-DC, exactly the "SCR relays" in the VBShdl BOM), a **12 V diaphragm pump**, two **air-horn/annunciators**, a 12 V battery, and a **perfboard processor board** with a trim-pot. So the *deployed* control was: solar → charge controller → battery/supercap → SSRs switching thrusters/pump, with a perfboard doing the logic. The elegant CMOS nervous-net boards above appear to be **design studies, not the thing that floated.**

## New-vs-old (what 2024 PRIME / EVIE-2c changed for the electronics)

The PRIME previews (`VBShdl-1m5manatee2b1PRIME.png`, `..._BimodalTurbine.png`, `9x9-HVOprocessor.png`, `Electrolyzer.png`) are **mechanical CAD only — they contain no new circuit content.** What changed at the *system* level, and what it implies for electronics:

- **Amphibious wheels** at the pontoon ends (visible in the EVIE-2c preview) imply **2 added drive actuators** beyond the 2 marine thrusters. The Super Cricket already supports 4 motors (MOTOR-A…D via two L293Ds), so the controller is, conveniently, already sized for "two thrusters + two wheels." No schematic was drawn for the wheel drive, however — it's an unfilled gap.
- **`+BimodalTurbine` variant** (horizontal-axis turbine on the central mast) adds a **generator input** to the power bus — i.e., wind charging in addition to the 45 W PV. The VBShdl BOM already lists a "wind turbine" / "400 watt Air-X" so the electrical intent predates PRIME, but no MPPT/rectifier/charge-controller schematic exists for it.
- **`Electrolyzer.png` / `9x9-HVOprocessor.png`** imply **new high-current DC loads** (electrolysis, process heaters/pumps). These would need real power electronics (current-limited supplies, bus protection) that **do not appear anywhere in the circuit folder.** This is the largest new electrical gap the 2024 design opens.
- **Net:** PRIME is a *mechanical* re-architecture (tensegrity frame, drum, wheels, turbine). The electronics dossier did **not** advance to match it. The newest *actual circuit* is still the 2019 VBSX v2 / BasicJT2 nervous net; the 2024 model has more electrical requirements and **fewer** matching schematics than the 2019 model. The "v1→v2 (VBSX) board evolution" the brief asks about is real and is the analog BEAM lineage above; there is **no v3/PRIME board.**

## Evidence & maturity

| Artifact | What it proves | Maturity |
|---|---|---|
| `supercx-sch.pdf` | Digital controller is MIT Super Cricket V1.0 (Fred Martin, 2006), PIC16C715×3 + L293D | **Documented, third-party, real** — but not original |
| `AIsourcecode1.txt` | Complete reactive Logo phototaxis program (with an averaging bug) | **Built/runnable** as Cricket-Logo; trivial Braitenberg behavior |
| `LowellAI.png` | Fully-specified analog photovore w/ on-image BOM (1381, 2N3904/06) | **Buildable as drawn** (~$15 BOM); standard BEAM |
| `basicJT1-AI.bmp`, `VBSXv2schematic.jpg`, `BasicJT2-AI.JPG` | Three generations of BEAM/Nv-net steering boards | **Design studies**; hand-drawn → clean-redraw; no test data |
| `photoschematicAssembly1b.jpg` | Actual 2015 pond wiring: 45W PV, charge controller, 4× SSR-40DD, supercap, perfboard | **Physically built** — this is the real deployed electronics |
| PRIME `.skp` previews | Mechanical only | **CAD-only**, no circuit content |
| `MASTER_CONTROL_AI.md` | "Prospero 3rd-Gen AI," "inference engine," "patented" | **Asserted, unsupported** — contradicted by the actual schematics |

**Bottom line on maturity:** the digital controller is *built-untested* at the integration level (the chip is real and proven; nobody has shown the full 6-sensor + 4-motor + telemetry stack running on water). The analog boards are *modeled-only* (schematics, no scope traces, no bench logs). The 2015 SSR/perfboard rig is the only *built+tested* electronics, and it's the least sophisticated.

## Validation status (per claim)

- **"3rd-Generation Prospero Artificial Intelligence / inference engine / patented AI"** — **FALSE (as described).** The code is a reactive Braitenberg phototaxis loop in Cricket Logo running on a 2006 MIT educational board. There is no learning, no inference, no model. Calling it "AI" in 2026 is, at best, 1990s-era usage; the patent claim is unsubstantiated in the corpus. ([Fred Martin / Handy Cricket](https://www.cs.uml.edu/~fredm/handyboard.com/cricket.html))
- **"Redundant marine-hardened computer processors"** — **PLAUSIBLE in intent, DUBIOUS in fact.** The Super Cricket does carry 3 PICs, but they are not redundant fault-tolerant processors — they're a main + 2 bus expanders on one board. "Marine-hardened" is unsupported; the parts are standard 5 V DIP/SOIC silicon with no conformal-coat or sealing evidence.
- **6-sensor phototaxis steering works** — **PLAUSIBLE.** The Logo logic and the analog photovore boards are both legitimate, well-trodden ways to steer toward light. The averaging bug degrades but does not break the winner-take-all behavior.
- **Solar + (optional wind) charging into supercap/battery, SSR-switched loads** — **PLAUSIBLE and partly BUILT.** The 2015 rig demonstrably did this. Fotek SSR-40DD DC-DC relays switching 12 V thrusters is mundane and correct. ([Solarbotics BEAM solar engines](http://solarbotics.net/library/circuits/se.html))
- **The analog BEAM boards are original IP** — **FALSE.** `1381` voltage triggers, 2N3904/06 solar engines, TLC27L2 comparator photovores, and 74HC14 Nv microcores are all canonical, published Solarbotics / Tilden / Rigter circuits. ([Solarbotics schematics](http://robomaniac.solarbotics.net/schematics.html))
- **The 2024 PRIME electronics are designed** — **FALSE / DUBIOUS.** No PRIME-era schematic exists; the electrolyzer, process heaters, wheel drives, and turbine generator are CAD payloads with no matching power-electronics design.

## Red flags & open questions

1. **The "AI" is the headline and it's the weakest claim.** Any technical reviewer who opens `supercx-sch.pdf` sees `fredm@alum.mit.edu` and `THE SUPER CRICKET V1.0 (C) 2006`. Selling a 2006 classroom board's reactive Logo loop as proprietary "3rd-Gen AI" is a credibility landmine. **Reframe before anyone technical sees it.**
2. **No power budget.** A 45 W PV (and an optional turbine) must run two 55 lb-thrust trolling thrusters, a 300 psi pump, electrolysis, and heaters. Nowhere in the electronics corpus is there a load table, battery sizing, or duty-cycle math. The "Drift & Correct" sleep loop hints they knew power was tight — but it's never quantified.
3. **The averaging bug** in `AIsourcecode1.txt` is real and shippable-as-is only because the behavior is forgiving. It signals the code was never carefully reviewed.
4. **Schematic ≠ built.** The sophisticated CMOS nervous-net boards (VBSX v2 / BasicJT2) have zero test evidence. The thing that was actually built is the crude SSR/perfboard rig. The dossier conflates the two.
5. **No PRIME-era electronics at all.** The 2024 mechanical redesign added electrical loads (electrolyzer, wheels, turbine) with no corresponding circuit work. The electronics are a generation behind the mechanics.
6. **"JT" ambiguity** — worth stating plainly so investors aren't told it's a Joule Thief energy-harvester. It's the JT-1 *vehicle* model code. The energy-harvesting story lives in the BEAM solar-engine caps, not a JT.
7. **Telemetry is IrDA (TFDU4100)** — line-of-sight, ~1 m, ~115 kbps. That is not an over-the-horizon "real-time telemetry to Operations Control Center" link for a mid-Atlantic vessel. The comms claim and the actual part are incompatible.

## Concrete improvements (buildable, de-risking)

1. **Re-platform the controller honestly and cheaply.** Replace the 2006 Super Cricket with a single **ESP32** (or RP2040 + LoRa). You get: 6× ADC for the light sensors, PWM motor control, real Wi-Fi/LoRa telemetry (kilometers, not 1 m IrDA), watchdog, OTA updates, and a $6 BOM. Port the Logo phototaxis loop to ~40 lines of MicroPython/C. **This single swap fixes the "AI," the comms, and the redundancy claims at once** and gives a defensible modern story.
2. **Fix the averaging bug** (parenthesize the sums) — 10-minute change, and re-derive the low-light threshold with real photodiode data.
3. **Keep the analog board as a "limp-home" safety layer.** The BEAM photovore (`LowellAI.png`) is genuinely useful as a *dead-simple, no-firmware* fallback that steers toward open sky/light if the MCU hangs. Market it as designed-in redundancy (which is honest) rather than "AI."
4. **Build the missing power-electronics tier:** a proper **MPPT solar+wind charge controller**, a fused/monitored DC bus, and current-limited drivers for the electrolyzer/heater. This is the real 2024 gap. Off-the-shelf marine MPPT + a Victron-style BMV shunt closes most of it.
5. **Cheap de-risk experiment ($300, one weekend):** wire one thruster + 6 light sensors to an ESP32 in a tote of water, log sensor/thrust/current to SD, and publish a 2-minute video of it steering toward a lamp with a live power graph. That single artifact converts "modeled-only" to "built+tested" for the control loop and is the highest-leverage credibility move available.
6. **Instrument the supercap/battery** (the 2015 rig already had an LCD voltmeter) — add a $15 INA226 current/voltage logger so the next pond test produces the power-budget data the corpus is missing.

## Kit/license angle

There is a **legitimate, sellable kit here — once it's renamed away from "AI."**

- **"Light-Following Marine Robot Brain" kit (sellable now):** ESP32 + 6 photodiode front-ends + dual H-bridge + MPPT charge input + the (corrected) phototaxis firmware, sold as a soldering/learning kit with the BEAM analog board as the "no-code redundancy" module. The `LowellAI.png` BOM is already ~$15; a complete kit lands at a **$60–120 retail** sweet spot. This is squarely in the Solarbotics / Adafruit-CRICKIT / educational-robotics market that already exists and sells.
- **The analog BEAM boards (`LowellAI`, `BasicJT2`) are individually kit-able** as classic photovore solder kits — but **they cannot be licensed as IP**, because they are public-domain Solarbotics/Tilden circuits. Sell them as kits, never license them as inventions.
- **Not licensable:** the Super Cricket (Fred Martin's copyright), the BEAM circuits (public), and the "Prospero AI" (a name over off-the-shelf parts). The licensable electronics IP in this corpus is **effectively zero today.** What's licensable is the *integrated vessel system* (mechanics + process), not the control board.
- **Strategic recommendation:** sell the build-kit (real, buildable, modest margin), and base any IP license on the *cavitation reactor + algae process*, not the electronics. The honest electronics pitch is "rugged, redundant, $60 of proven parts" — which is a *strength* for a buyer who feared exotic unobtanium, and a *liability* only if it's oversold as AI.

---
*Sources: [Fred Martin / MIT Cricket](https://www.cs.uml.edu/~fredm/handyboard.com/cricket.html), [Solarbotics BEAM solar engines](http://solarbotics.net/library/circuits/se.html), [Solarbotics schematics library](http://robomaniac.solarbotics.net/schematics.html). Primary artifacts: supercx-sch.pdf, AIsourcecode1.txt, LowellAI.png, basicJT1-AI.bmp, VBSXv2schematic.jpg, BasicJT2-AI.JPG, photoschematicAssembly1b.jpg, MASTER_CONTROL_AI.md, VBShdl1BOM_strings.txt, PRIME .skp previews.*
