# Frame, Structure & Amphibious Platform

*Due-diligence dossier — Solaris Cybernetics "Mobula" / EVIE-2c. System: structure, hull, buoyancy, materials, lifting, scaling. Prepared 2026-06-17.*

## What it is (plain language)

Strip away the algae-to-diesel chemistry and the light-seeking controller, and the Mobula is, structurally, a **flat raft built from two big plastic tubes (pontoons) holding up an open frame**. On that frame sits everything else: a clear greenhouse box where algae grows, the cavitation reactor that is supposed to crack the algae into fuel, a wind turbine and solar panel for power, and two small thrusters for steering. It is a catamaran — two hulls, a deck between them — sized so one unit is roughly the footprint of a small bedroom and stands about as tall as a person.

Two design ideas distinguish it from an ordinary pontoon boat. First, **tensegrity**: instead of a heavy welded box-frame, the structure is meant to be a lattice of rigid struts held in place by tensioned cables and rubber bushings, so the whole thing is light and can *flex* with waves rather than fight them. Second, in the newest (2024 "PRIME" / EVIE-2c) design, **amphibious wheels** are added at the ends of the pontoons — the "Manatee" land capability — so the robot can in principle roll itself out of the water onto a beach or pond bank for service instead of needing a crane and a trailer.

The honest framing for an investor: the *concept* of the frame is coherent and draws on real, published engineering (tensegrity for wave-compliant offshore aquaculture is an active research field). But the *artifacts that actually exist* are two freshwater-pond rafts made of PVC and greenhouse film — not an ocean-survivable Sea-State-7 vessel — and the documents that describe the ocean version contain material inconsistencies (HDPE called "fiberglass-reinforced steel," wheels drawn at the wrong scale, sea-state claims with no test behind them). The frame is the *least exotic and most buildable* part of the whole machine — and precisely because of that, it is where the over-claiming is easiest to catch.

## How it works (the real mechanism, with numbers)

**Hull / buoyancy.** Twin pontoons, specified in both the archived docs and the BOM strings as **14-inch PVC sch40 tube with end caps** at prototype/M10 scale (`VBShdl1BOM_strings.txt` lines 36–37: "14inch by 20 PVC sch40 tube / 14inch end caps"), with **100 cubic feet of flotation foam** as backup buoyancy (line 39–40). The polished `.md` docs inflate this to **24-inch pontoons** (`COMPONENT_ASSEMBLY.md`, `MASTER_PARTS_LIST.md`) — a different, larger boat. A 14-in × ~14-ft sealed tube displaces ≈ π(0.583 ft)²(14 ft) ≈ 15 ft³ ≈ 935 lb of fresh water each, so a pair gives ~1,870 lb gross buoyancy before the foam — plausibly adequate for a pond demonstrator carrying a few hundred pounds of frame, panel, pump and a partly-filled 500-gal bladder.

**Primary frame.** BOM calls for **4×4 inch structural HDPE in 10 ft and 20 ft lengths** (`JT1BOM_strings.txt` lines 11–12; `VBShdl1BOM_strings.txt` lines 29–30) plus, in the JT (tetrahedral "Virgo City") variant, the build note "**use 2×2 square tube & hubs, with 1-1/2″ EMT to make the frames … make a prototype using 2″ PVC pipe for the frame & 1″ EMT**" (`SF-1m5x3c.jpg`). So the real frame is a **hub-and-strut space frame**: tubes meeting at multi-way hubs (the `HUB_SYSTEM.md` and the hexagonal hub visible atop each unit in the JT renders), with the triangulated red members forming tetrahedra/octahedra.

**Tensegrity / compliance.** The JT renders explicitly label "**SS cable with springs or flex bushings (typ)**" and "**rubber compression bushing (typ)**" at the strut junctions (`SF-1m5x3.jpg`). This is the load path that matters: the struts take compression, the cables/springs take tension, and the bushings let the frame articulate under wave loading instead of transmitting shock into rigid joints. This is a genuine tensegrity/tensegrity-adjacent approach and is the structurally smartest idea in the whole project.

**Materials reality check (HDPE).** Structural HDPE has a Young's modulus of only ~**800–1,100 MPa**, roughly **1/70th of steel** and far below aluminum or fiberglass. Tensile strength is ~**26–33 MPa**. It is impact-tough and rot/UV/corrosion-proof — ideal for a wet, low-stress pond raft — but it is a **low-stiffness, creep-prone** material. A 4×4 HDPE member spanning 10–20 ft will sag under sustained load (creep) and deflect heavily under wave-induced bending. The frame works *because* it is tensegrity (cables carry the tension HDPE is bad at); a rigid HDPE box-frame at this span would fail serviceability.

**Amphibious wheels ("Manatee").** Visible at both pontoon ends in `VBShdl-1m5manatee2b1PRIME.png` and on every member of the `BEAR Mobula-1 family human scale.jpg` render. Commercial precedent exists and is strong: systems like OCM's BAS-100 use four independently-steered retractable wheels rated to **16 tons**, launching/landing in seas up to ~4 ft. So amphibious capability is *not* science-fiction. The problem is **scale-match**: in the PRIME render the wheels are sized like garden-cart casters relative to a multi-meter pontoon, and there is no documented drive, suspension, retraction, or ground-pressure analysis for soft beach/pond-bank substrate.

**Scaling M10 → M20 → M40.** The family render (`BEAR Mobula-1 family human scale.jpg`) gives the ladder: **m10 = 5 gpd** (gallons/day fuel), **m20 = 1 bpd** (barrel/day), **m40 = 10 bpd**. Buoyancy scales with volume (length³) and *helps* you on scale-up — a 4× longer pontoon displaces ~64× more, easily carrying the heavier rig (square-cube law works *for* floating structures). The trap is the opposite: **bending loads on the frame also grow ~length⁴ while an unchanged strut section's stiffness is fixed**, so the frame members and joints must grow disproportionately, and wave bending moment on a 40 m span in open ocean is a different universe from a 1.5 m pond raft. The jump from "5 gpd pond toy" to "10 bpd ocean harvester" is presented as linear; structurally it is not.

## New-vs-old (what 2024 PRIME / EVIE-2c changed for the frame)

Comparing the older JT/Mobula-1 renders against the 2024 PRIME files:

1. **Pontoon-mounted amphibious wheels added** — the defining "Manatee" change. `VBShdl-1m5manatee2b1PRIME.png` shows wheels at all four pontoon ends; the older `SF-1m5x3*.jpg` JT models sit on bare blue pontoons with no wheels. This converts the platform from "craned in and out" to "self-beaching" in intent.
2. **Tensegrity frame made flatter and more explicit.** PRIME (`VBShdl-1m5manatee2b1PRIME.png`) is a **low, wide, X-braced flat deck** — the red struts form a planar tensegrity table over the twin pontoons, with the growth drum central. This is a departure from the JT line's **stacked tetrahedron/octahedron greenhouse cells** (`SF-1m5x3.jpg`), which were taller and more sculptural. PRIME trades vertical greenhouse volume for a lower center of gravity and a flatter, more transportable package.
3. **Central "growth/processor drum"** consolidated into one cylindrical module at deck center (the grey drum in both PRIME views), versus the JT line's three separate cells (cultivator / processor / battery-rack bays in `SF-1m5x3b.jpg`).
4. **+BimodalTurbine variant** (`VBShdl-1m5manatee2b1PRIME_BimodalTurbine.png`) moves the wind generator from small vertical-axis units perched over each cell to a **single horizontal-axis turbine on a tall central mast**. Structurally this is significant and **under-analyzed**: a mast-mounted HAWT puts a large overturning moment and gyroscopic/yaw load through the deck into the tensegrity frame and raises the CG on a flat, beamy hull — the worst combination for roll stability. No stability or mast-base reinforcement detail is shown.
5. **2025 lifting/rigging instruction** (`LiftingInstructions.JPG`): "**Lift from BOTTOM at corners ONLY**." This is a real, useful handling constraint and confirms the tensegrity reading — you must not hang the structure from its top members (cables/film), only jack/sling it under the pontoon corners where compression members land.

## Evidence & maturity

**Built and photographed (real hardware):**
- **2015 farm-pond prototype** (`lawsofmechcology1.jpg`): a PVC-frame raft floating and *operating* on a pond, with the inventor's own caption: *"The robot was producing over 1 cup per hour, or 1.51 gallons per day … powered by a [1/4]hp pump, powered by a 6-watt solar panel and a 0-watt windmill."* This is the single most honest, most valuable artifact: a self-reported, modest, real output number from a real floating unit.
- **Marina/road test rig** (`LiftingInstructions.JPG`, "Ferry & Gilbert Park"): the PVC catamaran on pavement with solar panel and a wired controller box, with handling instructions. A real, transportable, assembled frame.
- **Full-scale empty frame** (`BEAR test of robot frame.jpg`): a person-height PVC cube space-frame standing in a yard with X-cable bracing — proof the hub-and-cable frame stands up at full scale on land.

**Documented (BOM / parts, internally consistent at prototype scale):**
- `JT1BOM_strings.txt` and `VBShdl1BOM_strings.txt`: real, specific, sourced parts (4×4 HDPE, 14″ PVC pontoons, Northern Greenhouse laminated film + NH mounting strips, 100 CF flotation foam, Minnkota 55# thrusters, 500-gal bladder, named vendor URLs). This reads like a genuine maker BOM, not vaporware.

**Asserted only (no test, and inflated relative to the hardware):**
- "**Sea State 7 survivability**," "24″ pontoons," "**Fiberglass-reinforced Steel** primary frame" (`COMPONENT_ASSEMBLY.md`). Sea State 7 = 6–9 m waves; nothing in the evidence base has seen open water, let alone a storm. The material descriptor is internally contradictory.
- The **M40 ocean harvester** (`HUB_SYSTEM.md`: "transfers 24 tons of synthetic fuel … in 1–2 hours") exists only as renders.
- Amphibious wheel **drive/retraction/ground-pressure** — asserted by depiction, zero engineering shown.

**Maturity verdict: built-untested.** A real freshwater pond demonstrator exists and ran; the ocean-going, amphibious, tensegrity vessel described in the docs and 2024 renders is **modeled-only** with no structural test, no stability calc, and no sea trial.

## Validation status

| Claim | Verdict | Basis |
|---|---|---|
| Tensegrity frame is appropriate for a wave-compliant floating structure | **PLAUSIBLE (well-supported)** | Active research field — FEA studies of tensegrity for offshore aquaculture confirm high strength-to-mass and wave compliance are exactly tensegrity's strengths. The *concept* is sound engineering, not crank. |
| HDPE + cable/bushing frame is buildable and durable in water | **PLAUSIBLE** | HDPE is rot/UV/corrosion-proof and impact-tough; cables carry the tension HDPE can't. Right material for a low-stress wet frame. |
| A rigid 4×4 HDPE frame would be structurally adequate | **DUBIOUS** | HDPE modulus ~1/70 of steel, creep-prone. Only works *as tensegrity*; a stiff HDPE box-frame would sag/creep. The docs don't acknowledge this — the tensegrity is doing silent heavy lifting. |
| "Fiberglass-reinforced Steel" primary frame | **FALSE / incoherent** | The BOM says HDPE. "Fiberglass-reinforced steel" is not a real material; the polished doc is wrong. |
| Amphibious self-beaching ("Manatee") is feasible in principle | **PLAUSIBLE** | Commercial 16-ton-rated amphibious wheel systems exist (OCM BAS-100) and beach in ~4 ft seas. |
| The wheels as drawn on PRIME will work | **DUBIOUS** | Scale-mismatched (cart-caster-sized on multi-meter pontoons); no drive/retraction/suspension/soft-ground analysis. Render, not design. |
| Sea State 7 survivability | **DUBIOUS→FALSE (unsupported)** | SS7 = 6–9 m seas. No sea trial, no hull-girder/slamming calc, no class society review. Asserted, never tested; flat beamy hull + tall turbine mast is poor for it. |
| Square-cube favors scale-up buoyancy (M10→M40) | **PLAUSIBLE (the easy half)** | Displacement scales length³ — buoyancy is *not* the binding constraint on scale-up. |
| Linear performance scaling M10→M40 | **DUBIOUS** | Wave bending moment and frame loads scale far faster than the linear gpd→bpd ladder implies; structure/joints must grow disproportionately. Not modeled. |
| "Lift from bottom at corners only" | **PLAUSIBLE / correct** | Consistent with tensegrity load paths — sling under compression members, never the cables/film. Good real-world instruction. |

## Red flags & open questions

1. **Two different boats wear the same name.** The BOMs and photos describe a ~14″-PVC-pontoon pond raft producing ~1.5 gal/day; the `.md` dossier describes a 24″-pontoon, Sea-State-7, steel-frame ocean vessel. An investor must be told *which one exists* (the small one) and which is a render (the big one).
2. **Material misstatement.** "Fiberglass-reinforced Steel" for an HDPE frame is either a careless error or marketing inflation. Either way it undermines the document's credibility on materials.
3. **No stability analysis anywhere** — no GM/metacentric height, no roll period, no CG. The +BimodalTurbine mast *raises* CG on a flat hull; this is the most likely thing to capsize a demonstrator and it is completely unaddressed.
4. **Amphibious wheels are depicted, not designed.** No motor, no drive train, no retraction mechanism, no ground-pressure/flotation-on-soft-mud numbers. On a pond bank the wheels would likely sink.
5. **Sea State 7 is a wild claim** for a structure that has never left a freshwater pond. This single phrase will torpedo credibility with any marine engineer; recommend deleting it from all materials until a tank test exists.
6. **Scaling is asserted as linear** and isn't. The M40 is the product story but the structural feasibility gap from M10 to M40 is the largest unquantified risk.
7. **HDPE creep over the years-long ocean deployment** the business model assumes is unaddressed — sustained-load deflection in a structural polymer is a real long-duration failure mode.
8. **"Tyrell Schreber / deus ex machina" business card** (`SCNJ1drt2.jpg`) — a Blade-Runner in-joke as the listed CTO. Charming, but it signals a hobbyist/art-project register that sophisticated buyers will read as a credibility risk on the engineering claims.

## Concrete improvements (buildable, de-risking)

**Cheap experiments first (weeks, <$5k):**
1. **Inclining test on the existing pond raft.** Hang known weights at known offsets, measure heel, back out GM and CG. One afternoon, a tape measure and dumbbells; immediately tells you whether the +BimodalTurbine mast is survivable. *Single highest-value, lowest-cost de-risk in the whole project.*
2. **HDPE strut deflection/creep bench test.** Simply-support a 4×4 HDPE member over its real span, hang the design load, measure deflection at 1 hr / 1 day / 1 week. Quantifies the creep risk with a bucket of water and a dial gauge.
3. **Amphibious wheel ground-pressure check.** Park the loaded prototype on the wheels on grass/mud; measure sink-in and the force to roll it. Either the wheels work on soft ground or they don't — settle it empirically before designing a drive.
4. **Wave-flex log.** Put an IMU/accelerometer on the deck during a windy day on the pond; record real frame articulation and shock at the bushings. Validates the tensegrity-compliance assumption with a $30 sensor.

**Design upgrades:**
5. **Replace "Sea State 7" with a tested rating.** State only what's been demonstrated ("operates in protected freshwater; designed for up to Sea State X *pending tank test*"). Credibility over bravado.
6. **Lower the turbine.** For the bimodal variant, prefer the older distributed vertical-axis turbines (low CG) or a deck-level ducted unit over a tall mast HAWT, until a stability test clears the mast.
7. **Engineer the wheel scale.** Size wheels for actual ground pressure on soft mud (wide, low-pressure pneumatic or tracked), add a real retraction so they don't add drag afloat, and publish the load rating.
8. **Correct and reconcile the BOM/docs** into one source of truth at one scale (M10), with correct material names (HDPE, modulus, creep allowance) and an explicit "ocean version is conceptual" label.
9. **Joint/hub FEA.** The hubs are where a tensegrity frame lives or dies. A modest FEA pass on the worst-case hub under wave bending is the gate before any open-water claim.

## Kit/license angle

The frame is the **most sellable, least risky** slice of the whole invention — precisely because it's mundramatic and real.

- **"Tensegrity pond-platform kit" (build-kit, near-term).** The hub-and-strut HDPE/PVC tensegrity frame + pontoon + greenhouse-film enclosure, decoupled from the contested cavitation chemistry, is a genuinely buildable maker product: a floating, self-powered, wave-compliant instrument/grow platform. Sell it as the *chassis* (frame + pontoons + hubs + cable/bushing set + lifting rig + assembly guide) — the BOMs already exist (`*BOM_strings.txt`) and the hub system, lifting instructions, and full-scale frame photo prove it assembles. This is the honest "the platform works, the fuel is R&D" product.
- **Amphibious-skid add-on.** Once the wheel scale is engineered and tested, the self-beaching "Manatee" undercarriage is a differentiated, license-able module for *any* small floating platform (aquaculture sensors, research buoys), not just this robot.
- **Tensegrity-frame IP / license.** The specific flat-deck tensegrity + flex-bushing + "lift-from-corners" geometry is the defensible structural know-how. The 2022 patent-license template + a clean, *corrected* structural spec (with the inclining/creep test data above) is the licensable asset. **Do not license or sell on the Sea-State-7 / ocean-harvester story** until a tank test exists — the frame's saleability depends on *under*-claiming relative to today's documents.

*Bottom line: the structure is the part of the Mobula most likely to survive contact with a skeptical engineer — if and only if the marketing is dialed back to match the hardware that actually exists (a real, modest, freshwater tensegrity raft) and the inclining/creep/ground-pressure tests above are run to replace assertion with data.*
