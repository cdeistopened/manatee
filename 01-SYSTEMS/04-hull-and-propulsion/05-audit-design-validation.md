# Design-Evolution Analysis — Mobula → EVIE-2c (2024 "PRIME")

**Analyst lane:** Design-Evolution (2024 PRIME vs legacy)
**Date:** 2026-06-17
**Sources:** SketchUp preview PNGs (PRIME, PRIME+BimodalTurbine, SF-1DX4aurora1c), legacy renders (SF-1m5x3, SF-1m5x3c, BEAR Mobula-1 rendering, BEAR Mobula-1 m20a robot), 2025 LiftingInstructions.JPG, NEW source folder file listing.

---

## The single most important finding

There are **three different vessels** wearing two names, and the design did not "evolve" along one line — it *forked and regressed* depending on which artifact you look at.

1. **The aspirational Mobula (2008–2016):** a sleek translucent manta-ray flying-wing render ("Mobula~1: a revolution in green energy", "Mobula-1 m20a") with a starfish/turbine rotor on top, faired pontoon nacelles, and integrated thrusters. This is *concept art*, not a buildable model — no frame members, no BOM correspondence. The m20a even captions itself "produces One barrel (42 gallons) per day."

2. **The buildable space-frame (2013–2016, "Model JT-1" / SF-1m5x3):** a row of tetrahedral tensegrity cells on twin blue pontoons, vertical-axis (Savonius/Darrieus-style) wind turbines on yellow masts, an "Analog A.I." hex pod, and a labeled algae cell + processor cell. Explicitly annotated as buildable: *"make a prototype using 2" pvc pipe for the frame & 1" EMT."* This is the honest engineering lineage.

3. **The 2024 "PRIME" / EVIE-2c (VBShdl-1m5manatee2b1PRIME):** a *single* flattened tetrahedral/pyramidal frame on twin blue pontoons, with a central grow/processor **drum**, **amphibious wheels** at the pontoon ends, and (in the +BimodalTurbine variant) a **horizontal-axis rotor on a central mast**.

The **2025 LiftingInstructions.JPG is the reality check**: the only physically-existing object is a white-PVC twin-pontoon flat raft with a deck-mounted solar panel, a single vertical mast, and an open electronics box — **no wheels, no turbine, no grow drum, no enclosure.** It sits on pallets at a public park boat ramp ("Ferry 'N Gilbert Park"). PRIME's wheels/turbine/drum are CAD payloads bolted onto a raft that, as built, carries none of them.

> **Investor translation:** "PRIME / EVIE-2c" is a 2024 *drawing*, not a 2024 *machine*. The 2024 changes are paper changes on top of a ~2015–2025 pond raft.

---

## Change-by-change: problem solved vs. new risk added

### 1. Amphibious wheels (NEW in 2024 PRIME)
**What changed:** Caster/cart-style wheels added at all four pontoon ends; absent from every legacy space-frame render and from the 2025 physical raft.
**Problem it claims to solve:** self-beaching / self-launching for unattended harvest, servicing, and hurricane retreat without a crane or crew — a genuine operational pain point for an autonomous coastal robot.
**New risk added:**
- **Scale mismatch.** As drawn the wheels read as cart casters on multi-meter pontoons; no drive motor, no retraction, no suspension, no soft-ground (beach/mud/pond-bank) ground-pressure analysis. On a soft bank a flat-bottomed multi-ton raft on small hard wheels sinks, it doesn't roll.
- **Unpowered & uncontrolled.** The control corpus has zero code or actuators for wheels (consistent with the Electronics/AI lanes). They are unactuated geometry.
- **Drag + fouling penalty.** Permanently-wetted wheels/axles add parasitic drag and a biofouling/corrosion liability for a vessel claimed to run unattended for weeks.
**Verdict:** PLAUSIBLE concept (commercial 16-ton amphibious wheel systems exist, e.g. OCM BAS-100), DUBIOUS as drawn. Net: a real problem addressed with a depicted-not-designed solution that raises CG and adds failure surface.

### 2. Bimodal turbine — HAWT on a central mast (NEW variant in 2024)
**What changed:** The legacy honest model used **vertical-axis** turbines (omni-directional, no yaw, low CG, marine-friendly). The Mobula concept art used a top-mounted starfish rotor. The 2024 +BimodalTurbine variant regresses to a **horizontal-axis rotor on a tall central mast**, claimed to harvest *both* wind and water ("bimodal").
**Problem it claims to solve:** higher per-unit energy capture and dual-medium harvesting (wind when surfaced, current when the rotor dips/submerges) to close the power deficit.
**New risk added:**
- **Physics of "bimodal."** Air and water differ ~800× in density; one rotor + one generator cannot be efficient across both, and **no mode-switching mechanism is documented anywhere.** The word "bimodal" is doing the work a mechanism should.
- **Stability regression.** A tall mast-top rotor on a flat, beamy, shallow-draft hull is the textbook way to capsize a demonstrator. Raising CG directly contradicts the marine logic of the vertical-axis predecessor it replaced.
- **Yaw + gyroscopic loads** on a pitching/rolling raft — a HAWT needs to face the wind; a VAWT doesn't. This is a step backward in marine suitability.
**Verdict:** REGRESSION. The 2024 change trades a marine-appropriate VAWT for a less-suitable HAWT and adds an undocumented "bimodal" claim. The only generation hardware that ever physically existed is the modest deck setup in the 2025 photo — neither turbine type is built.

### 3. "EVIE-2c" naming (NEW in 2024)
**What changed:** The 2024 previews are titled **"EVIE-2c"**; legacy artifacts are "Mobula-1 / m20a", "Model JT-1", "SF-1m5x3", "Manatee 2b". The filename itself — `VBShdl-1m5manatee2b1PRIME` — stacks four generations of naming (VBS hull + 1m5 + manatee2b + PRIME).
**Problem it claims to solve:** a cleaner consumer/product brand ("EVIE") and a version signal ("2c") over an accreting pile of internal codenames.
**New risk added:**
- **Continuity confusion.** Three names (Mobula, EVIE-2c, Manatee/JT) for vessels that are *not the same boat* makes diligence harder and lets the polished render borrow credibility from the buildable model and vice-versa.
- **No corresponding spec reset.** A new product name with no new BOM, no new power budget, no new control code, and no test data is branding ahead of engineering — the same pattern as "3rd-Gen Prospero AI" over a Braitenberg loop.
**Verdict:** Cosmetic. Harmless if disclosed; a credibility landmine if "EVIE-2c (2024)" is presented as a new *machine* rather than a re-skinned *drawing*.

### 4. Tensegrity refinement — many cells → one flat frame (CHANGED in 2024)
**What changed:** Legacy SF-1m5x3 is a **chain of full tetrahedral cells** (algae cell + processor cell + AI pod, each a complete tetrahedron) — tall, modular, visibly tensegrity (red struts, "SS cable with springs", "rubber compression bushing (typ)"). PRIME collapses this into a **single, flattened pyramidal frame** spanning the two pontoons with the payload (drum) slung underneath.
**Problem it claims to solve:** lower profile (lower CG, less windage), simpler single-bay structure, easier to lift ("Lift from BOTTOM at corners only" — consistent with tensegrity load paths), and a flat deck for solar.
**New risk added:**
- **Loss of the modular scaling story.** The legacy "add a cell" architecture made M10→M40 scaling legible; the single flat frame doesn't obviously tile, yet the docs still claim linear gpd→bpd scaling. Wave bending moment grows far faster than the fuel-output ladder; the flattened frame hides rather than solves this.
- **Tensegrity not acknowledged in the prose.** The frame *only works* as a tension-stabilized structure (HDPE modulus ~1/70 steel, creep-prone), but the polished doc calls the primary frame "Fiberglass-reinforced Steel" — an incoherent material that isn't what the BOM (HDPE) or the renders (cable/strut tensegrity) show.
**Verdict:** PLAUSIBLE and arguably an improvement for a demonstrator (lower CG, simpler, liftable) — but it quietly discards the one feature (modular cells) that made scale-up intelligible, and the documentation still misstates the material. Mixed.

### 5. Central grow/processor drum (CHANGED in 2024)
**What changed:** Legacy split functions into separate transparent cells (a visible algae-growth cell + a separate processor cell with the cavitation hardware). PRIME consolidates into a **single central cylindrical drum** slung at the frame's center of the deck.
**Problem it claims to solve:** consolidation — one pressure-rated vessel for grow + dewater + cavitation reduces plumbing, joints, and leak paths, and centers mass low and amidships (good for trim).
**New risk added:**
- **Black-boxes the process.** The legacy cells at least *showed* distinct unit operations (grow vs. crack). A single sealed drum makes the already-contested chemistry (3%/pass cavitation cracking, "HVO" with no catalyst/H2 in the BOM) impossible to inspect or instrument — exactly the wrong direction when the core conversion physics is the unvalidated keystone.
- **Loss of grow-area.** A drum has far less illuminated surface/volume than the flat-panel grow cell it replaces; for a system already ~10–30× short on grow-light power and reliant on optimistic (12–90×) growth rates, shrinking photic area worsens the biology case.
- **Single point of failure.** Combining grow, harvest, and reaction in one vessel means one fouling/erosion event (cavitation erodes the stainless nozzle — inventor concedes it) takes the whole loop down; no redundancy.
**Verdict:** PLAUSIBLE for packaging/trim, DUBIOUS for the actual mission. Consolidation helps the naval architecture and hurts the (already weak) bio + process-transparency case.

---

## Net judgment: are the 2024 changes improvements?

| Change | Problem solved | Improvement? | Dominant risk |
|---|---|---|---|
| Amphibious wheels | self-beaching/service | **Concept yes, execution no** | scale-mismatched, unpowered, would sink on soft bank |
| Bimodal HAWT turbine | more/dual-medium energy | **Regression** | raises CG (capsize), no mode-switch, ~800× density gap |
| EVIE-2c naming | product brand | **Cosmetic** | continuity confusion, branding ahead of engineering |
| Flat single tensegrity frame | lower CG, liftable, simple | **Mixed (net slight +)** | discards modular scaling; material still misstated |
| Central grow/processor drum | packaging, trim | **Mixed (net −)** | black-boxes contested chemistry; less photic area; SPOF |

**Two improvements are real and demonstrator-appropriate** (lower-CG flat frame; centered low payload mass) — *until* the +BimodalTurbine variant re-raises CG and undoes the benefit. **The rest add operational ambition (wheels, dual-medium turbine, sealed reactor) with no matching engineering, no power-electronics, no control code, and no test data.** The mechanics drew checks the electronics and physics can't cash — a pattern every other lane in this dossier independently reports.

**The decisive evidence is chronological:** between the 2016 buildable space-frame and the 2024 PRIME CAD, *eight years passed and the only thing that physically materialized* is the 2025 flat PVC raft with a solar panel and a mast — no wheels, no turbine, no drum. The 2024 "evolution" happened entirely in SketchUp.

---

## What would change this verdict (cheap, decisive asks)
1. A **power budget** that includes the PRIME-era loads (wheels drive, electrolyzer, drum lighting) — currently absent everywhere.
2. A **stability sheet** (GM, CG, roll period) for the +BimodalTurbine mast configuration — the single most likely capsize mode.
3. **Photos of any PRIME feature physically built** — a wheel, the drum, the HAWT. To date the camera only ever sees the flat raft.
4. A **mode-switching description** for the "bimodal" turbine, or honest reversion to the marine-correct VAWT.
5. One **continuity diagram** mapping Mobula ↔ EVIE-2c ↔ JT/Manatee so buyers know which boat exists.
