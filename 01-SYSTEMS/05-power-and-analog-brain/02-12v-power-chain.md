# The Manatee — Electronics Guide

*An open-source wiring manual for the Manatee (EVIE-2c): a solar/wind-powered floating raft that grazes algae off a pond, runs it through a cavitation pump, and returns cleaner water. This guide covers the electrical system only — the frame, floats, drum, and plumbing live in the [IMPROVED Assembly Manual](02-IMPROVED-MANUAL.md).*

**Who this is for:** a patient non-technical builder. If you can wire a light switch, torque a bolt, and follow a numbered list, you can build Tier 1. Every part is a real, in-stock item with a price. Every wire is walked one connection at a time in plain English.

---

## The one big idea: analog is intentional

The Manatee's survival — *charge the battery, don't drain it flat, run the pump when there's power and water* — is a **pure-analog reflex**. There is **no computer** in that loop. Nothing boots up. Nothing runs code. Nothing can crash, freeze, catch a virus, or corrupt a memory card. It is built out of the same dumb, rugged parts as a car's turn signal or a thermostat: a reference chip, a comparator, a relay, a float, a fuse.

This is a deliberate design choice, not a limitation. A machine floating on water, in the sun and rain, for months, cannot depend on a fragile microcontroller for its life. So we build the life-support out of physics that cannot hang.

Digital appears **only as an optional, unpluggable observer** — a passive data-logger (Tier 2) that watches and writes a diary but never touches a switch. You can rip it off the machine, drop it in the pond, and the Manatee keeps cleaning water exactly as before.

### The three tiers

| Tier | What you add | Can the machine run without it? |
|------|--------------|---------------------------------|
| **Tier 1 — Simple** | The complete analog survival reflex: charge → store → don't-over-discharge → run-the-pump-when-power-and-water. Anchored in place (a knot, no motors). Plus the full safety skeleton (fuses, bonding, waterproofing). | This **is** the machine. Everyone builds it. |
| **Tier 2 — The Observer** | A passive digital witness (ESP32 logger + current shunts + water-quality sensors) that measures and reports. Hangs off one plug. | Yes — pull the plug and Tier 1 runs untouched. |
| **Tier 3 — Roaming & options** | The classic BEAM analog "photovore" steering brain (light-seeking), and/or optional wind power and a supercapacitor for a big pump. | Yes — every Tier 3 item is optional and isolated from the survival reflex. |

**Build them in order.** Do not add Tier 2 until Tier 1 runs on its own. Do not add Tier 3 until you have a reason to roam.

### What we deliberately deleted from the original design

The original machine had real, dangerous errors. We fixed them by *deleting* parts, which is the highest form of engineering:

- **No fuses anywhere → FIXED.** A 12-volt battery can shove over a thousand amps into a shorted wire and start a fire on the water. A fuse is now mandatory and is the cheapest life-safety part in the whole build.
- **A contradictory 2200-farad + 3-farad supercapacitor → DELETED.** The numbers never reconciled, and a discharged supercap of that size is a dead short that can arc-weld your battery terminals. The battery buffers our small pump just fine. (It returns only in Tier 3, and only if you fit a big high-inrush motor pump — and only as a safe, factory-balanced module.)
- **A 50-amp blocking diode → DELETED.** The modern charge controller already blocks backflow at night; the diode just wasted power.
- **An unloaded wind turbine → DROPPED from the baseline.** A turbine spinning into an open circuit overspeeds and cooks itself. Solar alone closes our small daily budget. (If you keep wind, a dump-load is mandatory — Tier 3.)
- **Four hot, lossy, polarity-sensitive Fotek solid-state relays → REPLACED** with one sealed marine relay and a logic-level MOSFET. The four SSRs wasted about 5 watts *each* as heat — a third of a 45-watt budget — and failed silently if wired backwards.
- **The survival cutoff buried in charge-controller firmware → PULLED OUT** into a discrete analog circuit. The reflex must be hardware you can trust with every chip on the raft dead or unplugged.

---

# Tier 1 — The Simple Analog Reflex

Everyone builds this. It is the whole machine.

## 1.1 What it does, in plain language

Think of Tier 1 as the machine's **metabolism plus its nervous reflexes** — eat, store, and know when to stop working so you don't starve.

**The power heart (metabolism):**
- The **solar panel** is the mouth: sunlight in, electricity out.
- The **charge controller** is a careful feeder: it spoons energy into the battery at the right rate and stops before it overfills.
- The **battery** is the stomach/fuel tank: it holds today's sunshine so the pump can still run at dusk or under clouds.
- The **main fuse**, bolted right on the battery terminal, is the sacrificial snap-link: if a wire ever rubs through and shorts, the fuse melts in a blink and cuts everything. It is the one part standing between you and an electrical fire on a pond.
- The **low-voltage disconnect (LVD)** is the survival reflex. It is a little voltage-watching switch — like a thermostat, but for battery level. When the battery gets tired, it pulls the plug on the pump so the battery lives to see the next sunrise; when the sun refills the tank, it clicks the pump back on. No computer decides this.

**The pump-switching reflex (nervous system):** thousands of times a second, the machine asks three yes/no questions, wired in series so **all three must be yes** or the pump stays off:

1. **Is the battery charged enough** that running the pump won't hurt it?
2. **Is there daylight power** to spend right now?
3. **Is there actually water/slurry in the drum?** (Never run a high-pressure pump dry — it destroys the seals in minutes.)

Each question is answered by a **comparator** — a balance-beam made of a resistor and a reference chip (see the teaching box below). The three answers are combined into one "yes" that nudges a transistor, which clicks a rugged sealed relay, which feeds the pump. **If any sensing wire breaks, the pump defaults to OFF** — the safe answer.

**The whole loop is one reflex arc:** sun fills the tank → when there's enough charge *and* daylight *and* water, the pump runs → the pump pulls the battery down → the reflex shuts the pump off → the sun refills the tank → repeat. Each on-period is one "batch." The battery itself is the metronome — no timer chip needed.

**Steering, the simple way: tie it up.** The baseline Manatee does not move under its own power. A mushroom anchor on a rope (or a pole pushed into the mud) holds it in place. The wind and the algae bloom drift *to* the raft as much as the raft drifts to them; a pond is small; and the machine's job — suck, cavitate, return cleaner water — works perfectly well sitting still. This has nothing to break, draws zero power, and cannot capsize itself. **If you build only one thing for steering, build a knot.**

## 1.2 Why it's built this way (the honest engineering)

the project's law: the survival loop is a pure-analog reflex with **no microcontroller in the protection path**. The design test is: *"if every clever chip on this raft dies, does the battery still get charged and still refuse to murder itself?"* The answer must be yes.

There is exactly **one** chip we tolerate inside the survival loop, and it's in the safe place:

- **The charge controller.** A modern MPPT ("maximum power point tracking") controller does contain a microcontroller — that's how it squeezes 15–30% more harvest out of the same panel. We keep it because its failure mode is **fail-safe**: a hung charger simply *stops charging*. It physically cannot over-charge or over-discharge the battery — it just quietly stops feeding it, and the machine goes to sleep. If you want literally zero microcontrollers, swap in a dumb PWM controller (a pure analog voltage clamp) and accept 15–30% less harvest. Both are offered below.

The **over-discharge cutoff (the LVD) is deliberately NOT left in the charge controller's firmware.** That would bury the survival reflex inside a config screen. Instead it's a discrete analog circuit (or a proven standalone analog LVD module) — a voltage threshold in hardware. The charge controller's Bluetooth "smarts" become an *optional* observer/timer in Tier 2. Unplug the smart brain and the machine still protects itself.

## 1.3 Teaching box — How a comparator makes a decision with no code

> **The balance-beam that thinks.**
>
> Every yes/no decision in the reflex is made by a **comparator**. Picture a see-saw (a balance beam):
>
> - On one pan you place a fixed **yardstick weight** — a rock-steady 2.5-volt reference from a chip called a **TL431** (about 40 cents). This voltage does not move, even as the battery sags or the temperature swings.
> - On the other pan you place a small, honest **fraction** of whatever you're measuring — a slice of the battery voltage, or the voltage from a light sensor, made with two resistors (a "divider").
>
> Whichever pan is heavier, the see-saw **slams all the way to that side** — fully ON or fully OFF, never halfway. That slam *is* the whole decision. There is no code, no program, nothing to crash. It's a resistor and a reference.
>
> **The hysteresis trick.** A plain see-saw *flutters* madly when the two pans are nearly equal — which would make the pump chatter on-off-on-off many times a second and burn out the relay. So we add one small feedback resistor that acts like a **notch the see-saw clicks into**. Once it tips ON, it won't tip back OFF until the battery drops noticeably lower — and vice-versa. This notch is what turns the machine into a **batch processor for free**: the pump switches on at (roughly) 12.4 V, runs and pulls the battery down to ~11.7 V, shuts off, the panel refills it, and it runs again.
>
> **Building an AND-gate out of nothing.** The comparators have "open-collector" outputs, meaning each one can only pull a shared wire *down* to off — never force it up. Tie all of them to one wire with a single "pull-up" resistor, and that wire only goes high (pump allowed) when *every* comparator lets go. That is a three-input AND gate built from one resistor. The float switch (a dumb plastic bob that rises with the water) sits in series in that same wire, adding the third condition.
>
> **The most important upgrade over the original.** The original builder's "AI inference engine" was, physically, a hand-soldered board with a single trim-pot comparing the sensor against a bare slice of the *drifting* battery bus — so its threshold wandered with the very thing it was trying to measure. Adding the stable TL431 yardstick and the hysteresis notch is the single biggest correction to the "brain."

## 1.4 Tier 1 consolidated parts list

Prices are rough US retail for one demonstrator. **UNKNOWN** = measure/decide on your unit; do not invent.

### The power heart (charge, store, protect)

| Part | Spec / notes | Qty | Cost |
|------|--------------|-----|------|
| **Solar panel**, 12 V nominal, rigid mono | Baseline 45 W (~120–170 Wh/day); **100 W recommended** for real margin (~300–400 Wh/day). MC4 leads. | 1 | $60–110 |
| **Charge controller — MPPT** (Victron SmartSolar 75/15) | 75 V PV max, 15 A. +15–30% harvest, reverse-polarity + night-blocking built in, LiFePO4/AGM presets. Its firmware LVD is **NOT** used for the survival cutoff. | 1 | ~$110 |
| *Alt:* **dumb PWM controller** (Morningstar SunSaver / Victron BlueSolar PWM) | Zero-microcontroller substitute. Costs 15–30% harvest. Same fail-safe (stops charging). | 0–1 | $20–40 |
| **Battery — 12 V LiFePO4 with internal BMS** (LiTime/Ampere Time 50–100 Ah) — *recommended* | 50 Ah ≈ 640 Wh usable, ~2 days autonomy. BMS = hardware over/under-voltage + over-current backstop; pick a model with **low-temp charge cutoff**. | 1 | $150–300 |
| *Alt:* **Group 24/27 AGM marine battery** | Cheaper, cold-tolerant, extra weight = useful low ballast. **No BMS** (so the analog LVD is doubly essential); never take below ~50%. | 0–1 | $130–200 |
| **Main terminal fuse** — Blue Sea MRBF + holder, on the battery **+** post | Baseline **30 A** (small pump ~5 A + margin, protects 10 AWG). 60 A only with a big motor pump + 6 AWG wire. Fuse matches the **wire**, not just the load. | 1 | $20–30 |
| **Battery main disconnect switch** (Blue Sea m-Series) | On/off isolator downstream of the fuse; kills the whole bus for service/transport. ≥100 A. | 1 | $15–25 |
| **Analog low-voltage disconnect (LVD)** — comparator module (LM393 + relay/MOSFET, adjustable) *or* discrete build (LM393 + TL431 + P-MOSFET) | Pure analog, no firmware. LiFePO4: cut ~12.0 V, reconnect ~13.0 V. AGM: cut ~11.5 V, reconnect ~12.6 V. ~100–500 ms debounce so pump-start sag doesn't false-trip. **This is the survival reflex.** | 1 | $15–30 (module) / ~$8 (discrete) |
| **Positive distribution feed** (fused block / stud) | Switched positive → feeds LVD input. | 1 | $10–20 |
| **Negative bus bar** (single-point ground) | All module negatives land here. Prevents ground loops. | 1 | $10–15 |
| **Wire & connectors** — tinned marine wire, MC4s, ring terminals, heat-shrink, PV disconnect/breaker | PV leads 10 AWG; battery + LVD legs 10 AWG (6 AWG if 60 A fuse). | 1 set | $40–70 |

### The pump-switching reflex board

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| REF1 | **TL431ACLP** shunt voltage reference (TO-92) | The stable 2.5 V "yardstick" all comparators judge against. | 1 | $0.40 |
| U1 | **LM393P** dual comparator (DIP-8) | Open-collector outputs (enables the wired-AND). | 1 | $0.50 |
| RV1 | **Bourns 3296** 25-turn trimpot, 10k | Field-calibrate the battery on/off thresholds. | 1 | $1.50 |
| CDS1 | **GL5528 CdS photocell** (or a small pilot PV cell) | The daylight sensor. A pilot PV cell ties "daytime" to "the panel is actually generating" — more honest. | 1 | $0.50 |
| Q1 | **IRLZ44N** logic-level MOSFET (TO-220) | Drives the relay coil; no heatsink. | 1 | $1.00 |
| K1 | **Sealed 40 A SPDT marine relay** (Song Chuan / Panasonic CB1-class) | Switches the pump. Replaces the 4× Fotek SSRs — no standing heat, no polarity trap. | 1 | $6.00 |
| SW-FLOAT | **Vertical float switch, normally-open, 12 V** (marine bilge float) | At the drum's minimum safe suction level. Wired fail-safe (open = pump blocked). | 1 | $15.00 |
| D-FB / D-PUMP | **1N5822 Schottky** (3 A) ×2 | One across the relay coil, one across the pump — kills inductive kickback. | 2 | $0.60 |
| D-RP | **SB560 Schottky** (5 A) | Reverse-polarity block on the board's supply. | 1 | $0.50 |
| R-SET | 1% metal-film resistors (39k, 10k, 680k, 2.2k, 4.7k, 10k, 1M, 10k, 100k) | Dividers, hysteresis, bias, wired-AND pull-up, gate drive. | 1 set | $2.00 |
| C-SET | Ceramic 100nF ×2 + electrolytic 10µF | Filtering + decoupling (stops noise false-tripping). | 1 set | $1.00 |
| F1 | **2 A inline blade fuse** + holder | Protects the reflex board's own supply tap. | 1 | $3.00 |
| F2 | **Pump-branch fuse** (blade or ANL), sized to the LOAD | ~10 A for a diaphragm demo pump; ~30 A ANL if feeding a big BLDC controller. | 1 | $5.00 |
| PCB1 | Perfboard + screw terminals + MG Chemicals 422B conformal coat | Coat both sides; screw terminals for field service. | 1 | $10.00 |

### The safety skeleton (fusing · bonding · waterproofing) — mandatory at every tier

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| FDB | **Blue Sea 5025 ST-Blade** fused distribution block + common negative bus | 6 branch circuits, one fuse per branch. | 1 | $30 |
| FUSE-B | ATO/ATC blade fuse assortment (3/5/7.5/10/15/20 A) | One per branch, sized to LOAD. | 1 kit | $10 |
| ENCL | **IP66 polycarbonate enclosure** (~200×150×100 mm), gasketed | Mount above the splash line. IP66 (not IP67 — a higher rating just traps condensation). | 1 | $28–40 |
| GLAND | **Nylon IP68 cable glands** (M12–M20) + blanking plugs | One cable per gland; enter on the **LOW** face. Plug unused holes. | 10-pk | $10–15 |
| BRV | **Gore PolyVent** pressure-equalizing breather, M12 | On the **TOP** face. Lets the box breathe so it doesn't rain inside overnight. | 1 | $6–10 |
| COAT | **MG Chemicals 422B** acrylic conformal coating | Both sides of every board. | 1 | $18 |
| HS / TERM | Adhesive-lined heat-shrink (3:1) + tinned ring/blade terminals | Every crimp and splice. | 1 kit | $27 |
| WIRE-BG | Tinned marine battery cable, 6 AWG (red + black) | Main feed + main negative. | ~10 ft | $30 |
| DGREASE | Dielectric grease | On every terminal — blocks corrosion. | 1 | $8 |
| ANODE | **Magnesium sacrificial anode (FRESHWATER)** + SS strap | Bolt to frame below waterline. **NOT zinc** (zinc passivates in fresh water). | 1 | $15–25 |
| ISOWASH | Nylon shoulder washers / isolation bushing kit | Galvanic isolation at every aluminum-to-stainless joint. | 1 kit | $12 |
| BBOX | Vented marine battery box + strap | Contains + vents any fault off-gassing; mounts battery low as ballast. | 1 | $20–30 |

### Steering — baseline (station-keeping)

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| MOOR | Mushroom anchor (8–15 lb) + nylon rode + stainless swivel + bridle to two forward pad-eyes | Size to ~1.5× wind load on the raft's sail area; bridle from **both** forward lift-eyes so it weathervanes bow-to-wind. | 1 set | $30–70 |
| SPUD | *Alt:* fiberglass push-pole + PVC guide sleeve on frame | Best in <6 ft, soft-bottom ponds; raft rises/falls with level but can't drift. | 0–1 | $40–90 |

## 1.5 Tier 1 wiring — one connection at a time

Read this like a recipe. Build the power heart first, then the reflex board, then join them. Every wire is tinned marine wire; every crimp gets glue-lined heat-shrink.

### A. The charge-and-store path

1. **Battery + post → main fuse.** Bolt the MRBF terminal fuse **directly onto the battery positive post**. No wire in between. *Nothing unfused ever leaves the battery.* Call the fuse's output the **fused-positive node (FP)**.
2. **FP → charge controller BATT+.** 10 AWG red. Wire this *before* the panel — the controller needs to see the battery first.
3. **Battery − post → negative bus bar.** 6 AWG black. This is your single-point ground. (In Tier 2 this leg routes through the shunt first.)
4. **Charge controller BATT− → negative bus bar.** 10 AWG black.
5. **Panel + (MC4) → charge controller PV+.** 10 AWG red, through the optional PV disconnect/breaker. **Connect the panel LAST**, after the controller already sees the battery.
6. **Panel − (MC4) → charge controller PV−.** 10 AWG black. Confirm polarity with a meter in sunlight before you mate the MC4s.
7. Set the controller's charge profile to match your battery chemistry (LiFePO4 or AGM). Confirm it reports "charging."

*(No blocking diode. The controller blocks night reverse-current itself.)*

### B. The protected load feed (the LVD reflex)

8. **FP → main disconnect switch (SW) input.** 10 AWG red. The same fused node feeds both the charger and the load side.
9. **SW output → positive distribution (BUS+).** 10 AWG red. Opening this switch kills the whole load bus for service.
10. **BUS+ → LVD input (IN).** 10 AWG red. The LVD both *watches* this node's voltage and *passes* its current.
11. **LVD ground/reference → negative bus bar.** 16 AWG black. The LVD's balance-beam must share the system ground to read battery voltage correctly.
12. **LVD output (OUT) → LOAD-BUS+.** 10 AWG red. **This node is the boundary** between "protected power" and "the pump reflex." Everything downstream is over-discharge-safe.

Set the LVD thresholds for your chemistry (LiFePO4 ~12.0 V cut / ~13.0 V reconnect; AGM ~11.5 V / ~12.6 V). Add ~100–500 ms debounce so pump inrush sag doesn't false-trip it.

### C. The pump-switching reflex board

Build and bench-test this board on a variable bench supply *before* it ever touches the raft.

13. **LOAD-BUS+ → F1 (2 A) → D-RP → board rail (VBAT).** The reverse-polarity diode protects the whole board.
14. **VBAT → 2.2k resistor → TL431 cathode; TL431 anode → ground; 100nF cathode→ground.** This makes the steady **2.5 V reference (REF)**. *Bench check: REF must read 2.48–2.51 V and NOT move as you sweep the supply 11–14 V.*
15. **Battery comparator (question 1 — "charged enough?"):** VBAT → 39k → node **BDIV**; BDIV → 10k + trimpot RV1 → ground. BDIV → LM393 pin 3; REF → LM393 pin 2. Add the **680k hysteresis** resistor from output (pin 1) back to BDIV. Trim RV1 for ~ON 12.4 V / OFF 11.7–12.0 V. *Verify the gap is at least ~0.5 V or the relay will chatter.*
16. **Daylight comparator (question 2 — "sun up?"):** VBAT → CdS cell → node **LDIV**; LDIV → 10k → ground. LDIV → LM393 pin 5; REF → pin 6. Add the **1M hysteresis** from output (pin 7) back to LDIV. *Bench check: cover the sensor → output goes low (blocked); shine light → releases. Unplug the sensor → reads dark → pump off (fail-safe).*
17. **The wired-AND:** tie pin 1 and pin 7 together to node **N**; fit ONE **4.7k pull-up** from VBAT to N. N goes high only when battery is high AND it's light.
18. **Float switch (question 3 — "water present?"):** N → SW-FLOAT (normally-open) → 10k → node **GATE**; add a **100k GATE→ground** pull-down. *Wire it so an OPEN float (broken wire, dry drum) leaves the gate DOWN = pump OFF. Test by disconnecting the float.*
19. **GATE → Q1 gate.** When enabled, the gate sits near 10.9 V — hard ON for the MOSFET.
20. **Q1 drain → K1 relay coil (low side); VBAT → K1 coil (high side).** Fit **D-FB (1N5822)** across the coil, cathode to VBAT. (Mandatory flyback.)
21. **The pump power path (separate from the board supply):** Battery + → F2 (pump fuse) → K1 common terminal. K1 normally-open → PUMP+ (or the pump controller's ENABLE input — see caution). Pump − → negative bus. Fit **D-PUMP** across the pump (or an RC snubber across the K1 contacts if K1 directly switches a DC motor line).

> **Caution — DC switching:** if the pump is a big brushless (BLDC) motor, prefer switching the controller's low-current **ENABLE** line, not the raw motor DC. A 40 A automotive relay is rated for 12–24 V; switching a 48 V DC motor risks contact arcing. DC arcs don't self-extinguish like AC.

### D. Anchor it

22. Shackle the mushroom anchor to a bridle led from **both** forward frame pad-eyes so the raft weathervanes bow-to-wind. Confirm it holds position in the expected wind. **Done — no motors.**

## 1.6 Tier 1 build order (checklist)

1. Mount the battery **low and central** in a vented, strapped box (deliberate anti-capsize ballast).
2. Bolt the main fuse on the battery + post — **before any wire leaves it.**
3. Mount the charge controller high in the enclosure; wire **battery-first**, set the chemistry profile.
4. Connect the panel; confirm charging. (No blocking diode.)
5. Install the analog LVD between BUS+ and LOAD-BUS+; set thresholds; tie its ground to BUS−.
6. Build the negative bus as a single star point.
7. Build and bench-test the reflex board; confirm all three fail-safe defaults (battery low → off, dark → off, float open → off).
8. Confirm the deletions: **no** supercap, **no** blocking diode on the baseline.
9. Fuse every branch off the distribution block, sized to its load.
10. Galvanic isolation + one **magnesium** anode below the waterline.
11. Mount the IP66 box above the splash line: glands **down** with drip loops, breather on **top**, unused holes plugged.
12. Conformal-coat all boards; tinned wire + glue-lined heat-shrink + dielectric grease throughout; no submerged splices.
13. **Commission:** prove every fuse is present and correctly rated before energizing, then rain/splash-test the closed box.

## 1.7 Tier 1 safety

- **Fusing (life-safety #1):** main MRBF fuse on the battery + post before any wire leaves it, sized to the wire it protects; one blade fuse per branch, sized to its load. A 12 V LiFePO4/AGM bus sources hundreds-to-thousands of fault amps into a short — this is the fire-on-water scenario, and the original had **zero** fuses.
- **Fail-safe sensing:** every sensing wire is oriented so a break defaults the pump OFF (battery divider open → reads low → off; light sensor open → reads dark → off; float open/dry → gate down → off). Verify all three by disconnection during commissioning.
- **Inductive suppression:** Schottky flyback across the relay coil AND the pump motor; RC snubber across the contacts if switching DC motor power directly.
- **Dry-run protection:** the float interlock exists specifically to stop the high-pressure pump running dry (seal destruction in minutes).
- **12 V is not a shock hazard** — even soaking wet, 12 V DC is below the human shock threshold. The real dangers on the water are **fire** and **corrosion**, not electrocution. Spend your safety budget accordingly (fuses + waterproofing), not on phantom shock risk.
- **Bonding = floating DC, not chassis-return.** Keep both battery terminals off the metal frame entirely. Then a single wire chafing to the frame does nothing — it takes two independent faults to pass frame current. Handle dissimilar-metal corrosion mechanically: nylon isolation washers at every aluminum-to-stainless joint + one magnesium anode.
- **Waterproofing:** IP66 box above the splash line, glands low, breather high, drip loop on every entry, conformal-coated boards. Water ingress is the top failure mode for a floating box.
- **Battery venting:** AGM/lead-acid off-gas hydrogen — vented box only, never sealed; no spark source (fuse/relay) inside the battery box. LiFePO4 doesn't off-gas but must still be strapped hard.
- **LiFePO4 cold-charge:** charging LiFePO4 below 0 °C permanently damages cells — use a BMS with low-temp cutoff, or choose AGM for freezing ponds.
- **Polarity + sequence:** confirm panel polarity with a meter; wire the controller battery-first, PV last.

## 1.8 Tier 1 honest notes

- **The one microcontroller (moderate-high confidence):** an MPPT controller genuinely contains a chip. We keep it because its failure is fail-safe. If you want zero chips, the PWM swap is honest and offered, at 15–30% less harvest. What we will *not* do is let the survival cutoff live in firmware.
- **Power budget is tight (high confidence):** at 45 W the baseline closes only marginally, in daylight, as an intermittent batch process. **Recommend 100 W** for real margin. Do not expect continuous solar operation — the Tier 2 shunt will prove the actual daily balance instead of us arguing it.
- **LVD on LiFePO4 (known limitation):** LiFePO4's discharge curve is nearly flat, so a voltage-threshold LVD is a *coarse* fuel gauge on lithium. It's still the correct robust reflex (no firmware, no calibration drift); precise state-of-charge belongs to the Tier 2 coulomb-counting shunt.
- **The "daylight" signal is a proxy.** A CdS cell reads brightness, a fair proxy for "sun is up," but it can be fooled by cloud-shadow flicker (hence the hysteresis). A pilot PV cell tied to actual panel output is the more honest choice.
- **Exact thresholds must be measured on your unit.** The 12.4 V / 11.7 V numbers come from the chosen resistor values and a first-order calculation. Set them empirically with the trimpot. Confidence is HIGH on the method, MODERATE on the exact numbers.
- **What we did NOT invent:** we did not assign a purpose to the two air-horn annunciators (their function is genuinely **UNKNOWN** in the source corpus — alarm? bird deterrent?). Confirm intent before wiring them always-armed. We also did not fix the pump's exact current until you confirm whether it's a diaphragm demo pump or a 500–700 W BLDC — that sets the pump fuse (F2) and relay rating.

---

# Tier 2 — The Observer (passive logger + telemetry)

Optional. Add only after Tier 1 runs on its own.

## 2.1 What it does, in plain language

The survival brain is a heart that beats on its own. **The Observer is a fitness watch strapped onto that heart.**

It watches — battery volts and amps, how much sun came in versus how much the pump used, how cloudy the water is going **in** versus coming **out** (the honest proof the pond got cleaner), pond temperature, drum level, and how many grams of wax piled up — and it writes every reading into a diary on a memory card once a minute. It can also text that diary home over Wi-Fi, a little long-range radio, or a cell connection.

**The one rule that makes it safe: the watch never touches the steering wheel.** It cannot turn the pump on or off, cannot cut the battery, cannot do anything but look and write. It sips power through its own tiny fuse, so if the watch itself shorts out, only its own little fuse blows and the heart never feels it. And it hangs on **a single plug** — pull that one connector and the whole digital watch is gone while the machine keeps running. That is what "unpluggable observer" means: you can rip it off, drop it in the pond, let its firmware freeze, and the Manatee does not care.

## 2.2 Why it's built this way — four hard isolations

Microcontrollers crash, SD cards corrupt, firmware hangs, boards flood. So the ESP32 is bolted on strictly as a **witness**, enforced by four physical isolations:

1. **Power isolation** — the Observer draws its supply through its **own 1 A fuse** into its **own buck converter**. A dead short anywhere in the digital domain blows only that 1 A fuse; the main bus is untouched. Its draw (~0.3–0.8 W) is a rounding error on the budget.
2. **Sense isolation** — every electrical measurement is a **read**. Battery/PV/pump current is measured across **permanent passive shunts** (dumb milliohm resistors that live in the harness forever and essentially never fail open). The chips only read the tiny voltage drop. Remove the digital side and the shunts still carry current normally.
3. **No actuation authority** — the ESP32 has **zero wires** into the pump relay, the LVD, or any survival actuator. It can log "the pump is running" but it can never *make* the pump run. This is the bright line between an observer and a controller, enforced in copper, not code.
4. **Physical unpluggability** — the entire digital domain hangs off **one keyed connector** (fused +12 V, ground, and the sense/sensor leads). Unplug it and you drop cleanly from Tier 2 to Tier 1.

**Why instrument at all?** The venture's entire honesty firewall turns on two *measured* numbers: **watt-hours in vs. grams of product out**, and **turbidity in vs. turbidity out**. The Observer is how you measure them permanently, cheaply, on every run — and how you standardize that measurement across a fleet so the data becomes the moat (see the Telemetry Protocol section). But measuring a claim must never endanger the machine making the claim — hence a witness, not a controller.

**Why external shunts instead of a clip-on Hall sensor?** At DC, cheap Hall sensors are noisy and drift; true non-invasive DC clamps cost $20–40 each. Kelvin-tapped passive shunts read to under 1% for a few dollars. **Why a separate ADS1115 ADC for the turbidity sensors?** The ESP32's own analog input is noisy and unusable while Wi-Fi is on — and water quality is the reading we least want to get wrong.

## 2.3 Tier 2 consolidated parts list

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| OBS-MCU | **ESP32-WROOM-32** dev board | Logger + phone dashboard + store-and-forward. | 1 | $8–12 |
| OBS-BUCK | **12 V→5 V buck** (MP1584/LM2596) | The Observer's sole power interface to the machine. | 1 | $2–4 |
| OBS-FUSE | **1 A ATC fuse** + inline holder | On the +12 V tap. Isolates the entire digital domain. | 1 | $3 |
| OBS-CONN | **Keyed 8–12 pos disconnect** (Phoenix/JST) | Single-plug removal of the whole digital domain. | 1 | $3–5 |
| SH-PV / SH-BAT / SH-PMP | **Permanent passive shunts** (2 mΩ) *or* reuse INA226 onboard shunt | In series with PV+, battery−, pump branch. Stay in the harness forever. | 3 | $2–6 total |
| INA-PV / INA-BAT / INA-PMP | **INA226** current/power monitor (I²C) | Reads V and I across each shunt. Addresses 0x40/0x41/0x44. The energy-balance instrument. | 3 | $4 ea |
| OBS-ADC | **ADS1115** 4-ch 16-bit I²C ADC | Clean reads for the two turbidity sensors. Addr 0x48. | 1 | $4 |
| TURB-IN / TURB-OUT | **DFRobot Gravity turbidity sensor** (SEN0189-class) | IN at the pond intake, OUT at the clarified return. *in − out = the "cleaner water" proof.* Needs a 2:3 divider; fouls (recalibrate monthly). | 2 | $10 ea |
| OBS-TMP | **DS18B20** waterproof 1-wire temp probe | pond_temp_c; 4.7k pullup. | 1 | $5 |
| OBS-LVL | **JSN-SR04T** waterproof ultrasonic (or eTape/pressure) | drum level. Echo pin needs a divider to 3.3 V. | 1 | $8 |
| OBS-RTC | **DS3231** real-time clock + coin cell | Accurate UTC timestamps offline. | 1 | $4 |
| OBS-SD | **microSD SPI breakout** + 8–32 GB industrial card | Primary log store (~1,440 rows/day). | 1 | $5 + $6 |
| OBS-LOAD *(opt)* | **HX711** ADC + 5–20 kg load cell | Under the storage can → grams of product out. Deck mass, not a lab assay. | 0–1 | $8 |
| OBS-FLOW *(opt)* | **YF-S201** Hall flow sensor | On the return line → L/min and volume. Else derive from pump runtime. | 0–1 | $8 |
| OBS-GPS *(opt, T3)* | **u-blox NEO-M8N** GPS | Logs roaming vs. station-keeping drift; doubles as anti-theft. | 0–1 | $15 |
| OBS-LORA *(opt)* | **RFM95W (SX1276)** LoRa + shore gateway | ~24-byte packets to shore; best where there's no Wi-Fi. | 0–1 | $15 + gateway |
| OBS-CELL *(opt)* | **SIMCom SIM7000** LTE-M/NB-IoT + IoT SIM | Remote ponds; POST every 15 min. | 0–1 | $25 + SIM |
| OBS-ENCL | Small IP65 box or connectorized carrier inside the main IP66 box | Only dry electronics inside; water sensors on rated cable outside. | 1 | $8–15 |

*(If you bought a Victron SmartShunt for Tier 1's battery monitoring, read it over its VE.Direct UART and skip INA-BAT.)*

## 2.4 Tier 2 wiring — one connection at a time

1. **Battery + bus (post-main-fuse) → 1 A fuse → buck Vin+.** 18 AWG red. The *only* power the Observer draws — its own fuse means a digital short blows only this 1 A.
2. **Negative bus → buck Vin− / Observer common ground.** 18 AWG black. **Star ground:** the Observer ties to the machine's negative at exactly ONE point.
3. **Buck 5 V → ESP32 VIN + the 5 V sensor rail** (turbidity, ultrasonic, flow, load cell). The ESP32's onboard regulator makes 3.3 V for the logic sensors.
4. **SH-PV (in the PV+ line) → INA-PV IN+/IN−** (twisted 24 AWG sense pair). Shunt is permanent; the INA only reads across it.
5. **PV+ node → INA-PV Vbus** (read-only voltage tap). → pv_v, pv_w, wh_in accumulator.
6. **SH-BAT (battery − path) → INA-BAT IN+/IN−; battery + node → INA-BAT Vbus.** Signed current (+charge / −load).
7. **SH-PMP (pump branch) → INA-PMP IN+/IN−.** pump_w; integrates to wh_out. Never a control wire.
8. **ESP32 SDA (GPIO21) / SCL (GPIO22) → all three INAs, the ADS1115, and the RTC** (shared I²C, 4.7k pullups to 3.3 V). Distinct addresses: 0x40/0x41/0x44/0x48/0x68.
9. **TURB-IN / TURB-OUT signals → ADS1115 A0 / A1** (each via a 2:3 divider). *in − out = the cleaner-water signal.*
10. **DS18B20 data → GPIO4** (4.7k pullup). Probe hangs in the pond; gland low, drip loop.
11. **JSN-SR04T Trig → a GPIO; Echo → GPIO via a divider** (Echo is 5 V).
12. **microSD SPI (MOSI/MISO/SCK/CS) → ESP32 VSPI GPIOs (23/19/18/5).** The source-of-truth log.
13. *(opt)* **HX711 → GPIOs; load cell → HX711.** grams of product out.
14. *(opt)* **Flow signal → an interrupt GPIO** (via divider). *(opt)* **GPS TX/RX/PPS → UART2.** *(opt)* **LoRa/cell → SPI/UART on their own local supply cap, inside the fused Observer domain.**
15. **OBS-CONN keyed connector carries fused +12 V, ground, all shunt-sense pairs, and water-sensor leads across ONE plug.** Unplug it → the entire digital domain is gone; the shunts stay in-circuit and keep passing current.
16. **Pump-state input:** *inferred from the measured pump current only.* The Observer has **NO wire** to the pump relay or LVD. Zero actuation authority.

## 2.5 Tier 2 build order (checklist)

1. **Confirm the analog machine runs WITHOUT the Observer first.** If it can't, fix Tier 1 before adding the witness.
2. Install the three permanent passive shunts in the harness (they belong to the power wiring — they stay whether or not the Observer exists). **Kelvin-tap the sense leads at the shunt body**, not out on the power lugs.
3. Build the Observer on a connectorized carrier; fuse its +12 V tap at 1 A; bring ground to the single star point.
4. Wire the I²C bus; power up on the bench; run an I²C scan and confirm every chip answers. Set the RTC to UTC. *(Two INAs at the same address is the classic bug — strap the address pins deliberately.)*
5. Mount and calibrate the water sensors; zero the turbidity pair in clear water; tare the load cell empty. **Divide every 5 V sensor output before it hits a 3.3 V input.**
6. Flash the logger firmware: sample the INAs at a few Hz, integrate watt-hours continuously, write a 60 s row to SD, write a daily JSON rollup at local midnight. *Open/flush/close the SD file safely — a yanked card mid-write corrupts the log.*
7. Set `config_id` from the exact build manifest (pump model, nozzle bore, panel watts, battery Ah/chemistry, filtration). Re-stamp it whenever you change hardware.
8. Choose and wire **one** transport tier (offline / Wi-Fi / LoRa / cellular). All buffer to SD when offline.
9. **Prove unpluggability — the acceptance test:** with the machine running, pull the OBS-CONN connector; confirm the pump, charging, and LVD carry on unchanged; re-plug and confirm logging resumes and backfills. *This test is the whole design contract.*

## 2.6 Tier 2 safety

- **One fuse, one ground.** The Observer's dedicated 1 A fuse guarantees a flooded/shorted logger blows only its own fuse. A single star-ground tie prevents a ground loop that would both corrupt the current reading (the venture's key number) and create a sneak fault path.
- **No control authority is itself a safety property.** The Observer physically cannot energize a load or defeat the LVD, so a firmware bug or a hostile telemetry payload can't drain the battery or deadhead the pump. The bright line is enforced in copper.
- **Waterproofing:** dry electronics in IP65/IP66 with conformal coat, glands low, breather high, drip loops. Only water-rated sensors go outside on marine cable; antennas exit through gasketed bulkhead connectors, never a drilled hole.
- **Stay clear of the high-pressure fluid.** The Observer touches only 12 V and sensor-level signals — never the 250–400 psi cavitation leg. Any pressure sensing uses sensors rated well above line pressure; the logger only reads their low-voltage output.
- **Calibration as safety-of-data.** An uncalibrated turbidity or current channel gives confident *wrong* numbers — the most dangerous failure for an honesty-firewall venture. Monthly clean-and-recalibrate of the turbidity pair and a periodic current-zero check are mandatory, logged.

## 2.7 Tier 2 honest notes

- **What this honestly is:** a Tier-2 bolt-on *witness*. It measures and reports; it never controls. If anyone frames the ESP32 as the "brain" or "AI," that's an overclaim — it's a data logger.
- **Turbidity is a proxy**, not a species assay and not a nutrient (N/P) test. It fouls and drifts — good for a clear directional "water left cleaner" signal, not a lab result. Pair it with occasional grab-sample lab tests for the real claim.
- **Product mass** (load cell) is cumulative mass on a moving deck — honest as a trend, noisy from raft motion, and it's "grams of skimmed material," not "grams of fuel."
- **State-of-charge is an estimate** (coulomb-count drifts; needs periodic full-charge resync). Report battery voltage and integrated watt-hours as the primary truths, SoC as derived.

---

# Tier 3 — Roaming (BEAM steering) and options

Everything here is optional and isolated from the survival reflex. **The recommendation is still to anchor** (Tier 1). Build Tier 3 only when you have a reason to roam or a specific hardware need.

## 3.1 Steering, the clever way: the BEAM photovore

### What it does, in plain language

Give the raft a **nervous system made of light** — no computer, no code. This is the BEAM "photovore," a 1980s style of "living" robot.

Picture two eyes (two photodiodes) on the front, one left, one right. If more light hits the right eye, a little circuit nudges the raft to turn right — so it crawls toward the brightest patch of water. The turning rhythm comes from a ring of cheap logic chips wired to charge and discharge capacitors in a loop, like a row of metronomes handing a pulse around a circle forever. That pulse train, steered left or right by the eyes, drives the motors. It is a **reflex, not a decision**: light in, motion out, the way a moth flies at a lamp.

**The honest catch:** "brightest water" is only a rough stand-in for "most algae." A moth also flies at the moon; this raft will happily steer toward sun-glare or a white dock instead of a green bloom. Light-seeking finds blooms *sometimes*, by luck, but it **does not see algae** — it sees luminance. This is why we ban any "AI seeks cyanobacteria" framing: it is a public-domain phototrope, no machine learning, no inference.

**One more honest thing:** the tiny transistor motors on the original BEAM board are pager-motor sized — fine for a toy in your hand, far too weak to shove a 200-plus-pound raft. So if you roam, the light-brain still makes the left/right decision, but it hands that decision to **real muscle**: proper 12-volt thrusters switched by a power chip, the way a tiny light switch controls a big floodlight.

### Why it's built this way

Steering is where "analog is intentional" is easiest to honor by simply *not steering*. Gravity, wind, and the pond's own circulation move a bloom around a small basin; the reactor doesn't care where it sits. Station-keeping delivers ~90% of the value at ~1% of the risk and cost, with zero failure surface. Every motor, prop, and thruster wire can flood, foul, entangle, draw current the panel can't spare, and — worst case — apply a side force that helps capsize a beamy hull.

When roaming *is* wanted, the BEAM photovore is the right brain precisely because it is **not** a computer — a pure reflex with nothing to crash, drawing microamps in its logic core. It can be unplugged mid-pond and the machine keeps cleaning water.

We keep the heritage circuit faithful (two-photodiode bright-sensor bridge → "Nv-neuron" microcore ring oscillator → reversing tri-state gates → H-bridges) but correct it at exactly **one seam**: the original sub-1-amp discrete H-bridge can't move a raft, so the 4.5 V BEAM logic makes the decision and a **power H-bridge module drives real thrusters**. Brains stay tiny and analog; muscle is separate, fused, opto-isolated, and power-appropriate.

### Tier 3 steering parts list

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| BEAM_PCB | Perfboard/PCB for the photovore | Conformal-coat after test. | 1 | $5–15 |
| BATT (logic) | 3× AA holder + cells = **4.5 V logic rail** | **Isolated** from the 12 V power bus. | 1 | $5 |
| DPOL | 1N34A germanium diode (or 1N5817 Schottky) | Reverse-polarity block on the 4.5 V rail. | 1 | $0.50 |
| SW | SPST toggle | ON/OFF for the steering brain only — pulling it stops roaming without touching the reactor. | 1 | $2 |
| U14 | **74HC14** hex Schmitt-trigger inverter | The Nv-neuron substrate + power-on-reset. Schmitt hysteresis makes the ring oscillate. | 1–2 | $0.50 ea |
| U125 | **74HC125** quad tri-state buffer | Reversing MUX + Halt gates. | 1–2 | $0.60 ea |
| PD | **Photodiodes (BPW34 class)** — the two eyes | Reverse-biased; shade-hooded and forward-canted to compare left-vs-right water brightness. | 2 | $2 ea |
| Q3906 / Q3904 | 2N3906 PNP ×4 / 2N3904 NPN ×1 | Bright-sensor differential bridge + bias drivers. | 5 | ~$0.50 |
| QP2907 / QP2222 | PN2907 PNP ×4 / PN2222 NPN ×4 | **BENCH/DEMO ONLY** heritage H-bridges (<1 A — pager motors, to prove the logic). | 8 | ~$1.20 |
| D4148 | 1N4148 signal diodes | Microcore asymmetry diodes + demo-motor catches. | 6 | $0.30 |
| RES / CAP | 3M, 10M, 100K, 10K, 1K resistors; 0.1µF ×4, 0.001µF, 1µF caps | 3M/10M set the turn cadence (seconds-scale); 1µF+10M is the power-on reset. | sets | ~$13 |
| MOTOR_DEMO | 2× small DC gearmotors | Bench proof only. | 2 | $12 |
| **THRUST** | 2× **12 V thrusters** — bilge-cartridge jet (Rule 500–800 GPH housing) or small trolling motor | FRONT + REAR. **Sizing UNKNOWN** — must close the power budget *and* actually turn the loaded hull; likely 3–30 A each. | 0–2 | $40–150 ea |
| **DRV** | 2× **power H-bridge module** — DRV8871 (~3.6 A, small thrusters) or BTS7960 (~43 A, trolling-motor class) | The correction: real muscle between the 4.5 V logic and the 12 V thrusters. | 0–2 | $6–15 ea |
| LVL | Optocoupler (or logic-level MOSFET) level shifter | Translates 4.5 V logic to the driver AND galvanically isolates the 12 V muscle from the analog brain. | 1 set | $2 |
| FUSE | 2× inline ATC fuse + holder on each thruster feed | Sized to thruster stall/running current, off the fused block. | 2 | $6 |
| FLY | 1N5822 Schottky flyback across each 12 V thruster | Inductive-kickback catch on the power motors. | 2 | $1 |

### Tier 3 steering wiring — one connection at a time

**The isolated 4.5 V brain:**
1. **4.5 V battery + → SW → DPOL → VCC rail.** All 74HCxx chips and the bridge run off this isolated rail.
2. **VCC → 1µF → ground; VCC → 10M → U14a input; U14a input → the 1µF junction.** This RC power-on-reset issues a clean start pulse so the microcore self-starts into oscillation.
3. **4.5 V battery − → logic ground rail** (single-point; ties to the 12 V power ground **only** through the driver's isolation reference).

**The two eyes (bright-sensor bridge):**
4. **VCC → 1K → each Q3906 emitter** (left eye and right eye).
5. **Each Q3906 collector → 100K + its photodiode cathode node.** Left and right photocurrent branches.
6. **Both photodiode anodes → Q3904 collector (bridge tail); Q3904 emitter → ground.** The imbalance between left and right photocurrent is the steering error signal.
7. **Bridge imbalance node → U125b buffer input; 10M feedback U125b in→out; 0.001µF in→ground.** The 1nF slows the eye so glints and ripples don't jitter the steering.
8. **U125b output → U14b → microcore bias node.** The eyes skew the ring's left/right symmetry — the actual turn command.

**The microcore ring (the "walking loop"):**
9. Wire four (or six) 74HC14 inverters in a ring, each stage's output → **0.1µF → next stage's input**, with a **3M or 10M timing resistor to ground** at each input. Insert 1N4148 asymmetry diodes at two stages to give the walk a direction. Close the ring (last output → first input). This free-running oscillator is the turn cadence.

**Bench-prove with toy muscle first:**
10. Route the microcore taps through the **U125 reversing-MUX** (tri-state enables pick FRONT/REAR and polarity). Ensure the CW and CCW enables for a given bridge are **mutually exclusive** — both high is a commanded shoot-through.
11. Build the PN2907/PN2222 H-bridges (base resistors + 1N4148 catches), hang two pager motors, and confirm: shade the left eye → the model turns toward light. *This validates the entire logic chain cheaply before any thruster money is spent.*

**Swap toy muscle for real muscle (the water rig):**
12. **Tap the four MUX logic lines (FRONT-CW/CCW, REAR-CW/CCW) → LVL optocoupler inputs.**
13. **LVL outputs → DRV (power H-bridge) IN1/IN2**, front and rear.
14. **12 V bus (fused block) → ATC fuse → DRV VM** (sized to thruster stall current).
15. **DRV OUT1/OUT2 → thruster + 1N5822 flyback**, each channel on its own fuse and flyback.
16. **Keep the 4.5 V analog ground separate from the 12 V power ground — join only through the driver's isolated reference.** A motor-side transient must never reach the microcore.

### Tier 3 steering build order (checklist)

1. **Default decision: anchor, don't steer** (Tier 1). If the pond is small and the bloom drifts to the raft, you're done — skip the rest.
2. Breadboard the microcore ring on a 4.5 V bench supply; scope it; confirm clean free-running oscillation. *(If it won't oscillate, you probably substituted a non-Schmitt inverter for the 74HC14, or the timing R/C is off by 10×.)*
3. Build and null the bright-sensor bridge; hood and forward-cant the eyes; under even light trim to zero turn; shade one eye and confirm the correct swing.
4. Add the reversing MUX + Halt gates; verify shading left biases one way, right the other.
5. Bench-prove steering with the toy H-bridges + pager motors. *(Warm transistors = shoot-through; add base resistors / brief dead-time.)*
6. Swap toy muscle for real muscle via opto-isolated power H-bridges.
7. Power, fuse, and flyback the thrusters; mount them **low and symmetric** so the thrust line passes near the center of buoyancy; do the inclining test with both thrusters at full opposing thrust.
8. Conformal-coat, enclose, wet-test toward a lamp — then **prove the unpluggable property**: pull the steering ON/OFF switch and confirm the reactor keeps cleaning water.
9. **Honesty check on the water:** run it toward an actual bloom vs. open sunlit water and record how often "brightest" equals "most algae." Log thruster watt-hours against the shunt. Decide from data whether roaming earns its power and complexity over the anchor. Reverting to station-keeping is a valid, honest outcome — not a failure.

## 3.2 Other Tier 3 options (from the power heart)

These live in the charge/storage area but are Tier-3 optional. They are listed here so the whole "optional" layer is in one place.

| Ref | Part | Spec / notes | Qty | Cost |
|-----|------|--------------|-----|------|
| WIND+DUMP | Small 12 V wind turbine + rectifier (if AC) + **diversion/dump-load controller** + dump resistor bank | **Turbine NEVER runs unloaded** (open-circuit overspeed destroys it and raises capsize risk from mast-top mass). Dump resistor sized to absorb full turbine output. Dropped from baseline — solar alone closes the budget. | 0–1 | $60+ turbine + $60 controller + $20 resistor |
| SC | **Factory-balanced 16 V supercap module** (Eaton XLM/XLR) + pre-charge resistor (10–47 Ω, 5–10 W) | ONLY if a high-inrush brushed-motor pump is fitted. First connection MUST go through the pre-charge resistor (a discharged bank is a dead short that arc-welds terminals), then bypass. Replaces the deleted 2200 F / 3 F parts. | 0–1 | ~$60 + $2 |
| FUSE-MIDI | Blue Sea MIDI/AMI fuse holder + fuse | 30–60 A on its own holder for a thruster or big BLDC pump — **NOT** the little blade block. Rating UNKNOWN until sized. | 0–2 | $18 ea |

**Wind wiring (if kept):** turbine leads → rectifier (if 3-phase AC) → dump controller charge output → the fused battery node (FP); the dump controller senses BUS+/BUS− and shunts surplus to the dump resistor bank once the battery is full. **The dump terminal → dump resistor connection is mandatory** — the turbine is never open-circuit.

**Supercap wiring (if kept):** module +/− → BUS+ / BUS− **through the pre-charge resistor on first connect only**; bypass once charged.

## 3.3 Tier 3 safety

- **Fuse every thruster feed** at the distribution block (own MIDI/ANL holder, sized to stall current) with a Schottky flyback across each motor. A stalled or shorted thruster next to water is a fire and shock path.
- **Power/brain isolation:** the 4.5 V analog nervous system and the 12 V muscle share **no direct ground** — they meet only through the optocoupler's isolated reference, so a motor transient can never reach the microcore or the survival reflex.
- **Shoot-through:** verify mutually-exclusive CW/CCW drive; use base resistors / brief dead-time on any discrete H-bridge; prefer a power H-bridge IC with built-in cross-conduction protection on the water rig.
- **Capsize from steering forces:** mount thrusters low with the thrust line near the center of buoyancy; repeat the dockside inclining test with both thrusters at full opposing thrust. Steering side-load is a capsize contributor the original never considered.
- **Entanglement:** screen or duct any prop; keep the anchor rode clear of the intake and return.
- **Wind (if kept):** never energize the turbine without its dump load connected.
- **Fail-safe default:** the ON/OFF switch and the Halt gate must both leave the raft dead-in-the-water (anchored) when steering is cut — never in a runaway single-thruster turn.
- **Supercap arc-weld:** a discharged supercap module is a dead short; first connection through a pre-charge resistor, never directly.

## 3.4 Tier 3 honest notes

- **Light-seeking is a weak proxy for bloom-seeking** — the load-bearing caveat. Sun glint, a white dock, sky reflection, and open bright water all fool it. Treat roaming as "wander toward bright water," not "hunt the bloom," and expect it to steer wrong a meaningful fraction of the time. Confidence that station-keeping is the right baseline: **HIGH**.
- **The heritage discrete H-bridge is demonstrator-scale** (sub-1-amp, pager motors). It genuinely cannot move a 200-plus-pound raft. The board is the correct *brain*; the muscle must be a separate power stage.
- **Steering is entirely unproven on water.** By the teardown's own evidence, the BEAM board in this corpus never flew — the pond rig actually used a trim-pot perfboard and sat put. Roaming also busts the power budget: the 45 W panel makes ~120–170 Wh/day, and continuous thruster duty plausibly overruns that by a wide, **UNKNOWN** margin (thruster sizing is itself unresolved). Confidence that the BEAM logic can be made to oscillate and steer toy motors on a bench: **HIGH**. Confidence that roaming meaningfully improves harvest over an anchor within the power budget: **LOW**.
- **Recommendation:** build the knot. Build the BEAM board only as a Tier-3 experiment, gated on bench proof and an honest on-water light-vs-bloom test, and keep it fully unpluggable from the survival reflex.

---

# The Telemetry Protocol (the strategic moat)

*This is why Tier 2 exists. The defensible asset is NOT the open-source hardware — anyone can clone an ESP32 and a shunt. It's the **standardized, comparable dataset** that a fleet of rafts reports to a central hub, keyed to exactly which build produced it. That fleet-learning loop — "which nozzle bore / pump size / panel watt config actually closes the energy balance and cleans water fastest, across many real ponds" — is what a hardware cloner cannot copy. Standardize the schema now; version it; never silently change a field's units.*

## Fields (per 60 s row; units explicit; * = optional sensor)

| Field | Unit / notes |
|-------|--------------|
| `schema_version` | int — bump on any change |
| `device_id` | str — per-raft UUID, permanent |
| `config_id` | str — hash of the build manifest (pump model, nozzle bore, insert type, panel W, battery Ah/chem, filtration) |
| `fw_version` | str |
| `ts_utc` | ISO8601 (RTC/GPS/NTP disciplined) |
| `uptime_s` | int |
| `batt_v` | V (0.01) |
| `batt_i` | A, signed (+charge / −load) |
| `batt_soc_pct` | % (derived, low-confidence) |
| `pv_v`, `pv_i`, `pv_w` | V / A / W |
| `wh_in_cum`, `wh_in_60s` | Wh — PV harvest accumulator + interval |
| `pump_state` | 0/1 — **inferred from pump current, NOT commanded** |
| `pump_i`, `pump_w` | A / W |
| `pump_runtime_cum_s` | int |
| `wh_out_cum`, `wh_out_60s` | Wh — load accumulator + interval |
| `flow_lpm`* , `vol_pumped_cum_l`* | L/min, L |
| `turbidity_in_ntu`, `turbidity_out_ntu` | NTU |
| `turbidity_delta_ntu` | NTU (in − out) — the honest "cleaner water" signal |
| `pond_temp_c` | °C |
| `drum_level_cm` | cm (or %) |
| `product_mass_g_cum`* , `product_mass_60s_g`* | g (load cell) |
| `gps_lat`, `gps_lon`, `gps_fix`* | T3 roaming / drift / anti-theft |
| `heading_deg`* , `drift_m`* | T3 station-keeping vs. photovore |
| `lvd_flag` | 0/1 — LVD observed active |
| `fault_flags` | bitmask — sensor-fault / SD-fault / net-fault bits |

## Sample cadence

- **Electrical (INA226):** integrate continuously at 4–10 Hz; log a 60 s row + 60 s Wh intervals.
- **Water quality / level / temp / product mass:** 60 s.
- **GPS:** 300 s, or event-driven on movement.
- **Events (extra rows):** pump start/stop, LVD trip, network connect, SD-swap, calibration.
- **Daily rollup (local solar midnight):** `wh_in_day`, `wh_out_day`, `energy_balance_ratio = wh_in/wh_out`, `pump_runtime_day`, `product_g_day`, mean `turbidity_delta`, mean `pond_temp`. **This daily row is the fleet's headline record.**

## Local storage (source of truth)

- SD CSV, one file per day (`YYYYMMDD.csv`) — ~1,440 rows/day, negligible.
- Daily JSON rollup file.
- Flash ring buffer (last ~hours) as an SD-failure backup.
- Unsent-queue file for store-and-forward.

## Transport (ranked; all fall back to offline; SD is always authoritative)

1. **OFFLINE (baseline, zero infra):** ESP32 SoftAP hosts a captive dashboard; a phone connects to view live or download the CSV — or you just pull the card.
2. **Wi-Fi STA → HTTPS POST** to the hub `/ingest` with a device token, batched rows, when a pond access point is in range.
3. **LoRa → shore gateway:** compact ~24-byte binary packet (short device_id, ts, batt_v, wh_in_60s, wh_out_60s, turb_in, turb_out, product_g, flags) every 5 min; best for Wi-Fi-less ponds.
4. **Cellular LTE-M/NB-IoT:** POST every 15 min for remote ponds.

Envelope: `{schema_version, device_id, config_id, fw_version, rows:[...]}`. Offline → queue to SD, backfill on reconnect, **de-dupe idempotently** at the hub by `device_id + ts`. Never let a failed network call stall logging — telemetry is best-effort; the SD log is the truth.

## Hub / public dashboard

Aggregate every raft's daily `energy_balance_ratio` and `turbidity_delta`, sliced by `config_id`, into a growing public proof surface — the credible, third-party-checkable answer to "does it clean water?" and "does the energy balance close?" across many ponds and configs.

## Deliberately out of scope for Tier 2

**Any path from the logger to an actuator.** If a future tier wants observed data to influence steering or duty cycle, that becomes a *separate, clearly-gated controller* with its own fusing and fail-safe — it does not get bolted onto this witness. Keeping actuation out is exactly what lets the Observer be freely unplugged, drowned, or crashed with zero risk to the machine.

---

# Appendix — the honesty firewall (public-facing framing)

Carried from the grounding docs; applies to anything this electrical system is described as doing:

- **Lead value = cleaner water.** The wax/oil is an under-indexed **bonus**, "experimental until independently tested."
- **No** gal/day throughput. **No** "diesel / engine fuel." **No** "patented AI." **No** "red tide" / "Sea State 7" / species-selective sensing.
- The steering is a **public-domain analog BEAM/Braitenberg phototrope** — it seeks light (a proxy for surface blooms), not algae. No machine learning, no inference engine.
- The ESP32 Observer is a **data logger**, not a brain.

## Open UNKNOWNS in the electrical system (measure/confirm — do not invent)

| Item | Where it bites | How to resolve |
|------|----------------|----------------|
| Pump type & current (diaphragm demo vs. 500–700 W BLDC) | Sets the pump fuse (F2), relay/contactor rating, and whether a supercap is ever needed | Confirm the fluid-side pump choice |
| Air-horn annunciators' purpose (alarm? bird deterrent?) | Whether to wire them always-armed | Confirm intent before arming |
| Exact LVD on/off thresholds | Battery protection + batch cadence | Set empirically on a bench supply with the trimpot |
| Thruster sizing (if roaming) | Power budget + capsize moment + fuse rating | Size to close the budget and actually turn the loaded hull; measure watt-hours against the shunt |
| Real daily energy balance | Whether the machine runs continuously or only in batches | Measured by the Tier 2 shunt on every run |
| Main-fuse rating | 30 A baseline (10 AWG) vs. 60 A (6 AWG) if a big pump shares the bus | Sum the actual peak load before finalizing |

---

*This guide covers electronics only. Frame, floats, drum, nozzle, and plumbing are in [02-IMPROVED-MANUAL.md](02-IMPROVED-MANUAL.md); the first-hand engineering read of the models and circuits is in [00-GROUNDING.md](00-GROUNDING.md).*
