# Small-machine BOM — draft evidence, not a priced bill of materials

_2026-08-07. DRAFT. Nothing here is priced, sourced, or approved. Where a component has no
documented price in the archive, this file says so — it does not estimate one. This document exists
to show what a real bill of materials and price ladder for the small machine would need to contain,
and to be explicit about how much of that is currently missing._

**What "the small machine" means.** the project's ruling, 2026-08-07 (`.board/.resolved/decide-which-machine-sol0010.md`):
publish the 2016 pond build — the only configuration in the archive with photographic evidence of
producing anything. Not the 55-gallon-drum raft (never built), not the 2024 EVIE-2c CAD design
(never built), not the JT-1/VBShdl greenhouse vessels (a different machine entirely).

---

## 1. What the record actually shows

The primary source is `reference-clean/pond-machine-2016-noclaims.jpg` — a cropped, caption-quarantined
copy of Rudy's own annotated photo (source: `~/Downloads/Model-JTfree1NEW/DX5b+notes1.jpg`, per
`machine-record-audit-20260806.md`). I viewed the image directly for this draft. Three red arrows,
in Rudy's own handwriting, label:

- **"15 watt windmill"** — pointing at a small vertical-axis rotor at the top of a mast (three-blade
  profile, consistent with the "Lenz wing" rotor identified in the CAD file per the audit).
- **"1/10th HP pump"** — pointing at a small pump fitting mounted between a red-lidded container and
  a clear jar, at deck level.
  - **This number conflicts with two other due-diligence documents citing what they describe as the
    same photograph.** `due-diligence/systems/energy.md:69` transcribes the caption as *"a 1/100 HP
    pump, powered by a 0-watt solar panel and a 0-watt windmill."* `due-diligence/systems/frame.md:40`
    transcribes it as *"a [1/4]hp pump, powered by a 6-watt solar panel and a 0-watt windmill."* Those
    two due-diligence documents also disagree with each other. The pump size spans a 25× range
    across the three readings (1/100 HP to 1/4 HP), which is a real problem for sourcing — a 1/100 HP
    pump and a 1/4 HP pump are different categories of hardware at very different price points. **This
    has to be resolved by going back to the original file (or a higher-resolution copy of it) before
    any pump is priced.** The "15 W / 15 W / 1/10 HP" reading is the one in `machine-record-audit-20260806.md`
    (the most recent, most carefully cross-checked source) and the one visible on the copy in this
    project's own `reference-clean/` folder, so it is the working assumption below — but it is an
    assumption, not a settled number.
- **"15 watt solar panel"** — pointing at a flat panel mounted low on the frame, partially
  submerged.

Visible in the photograph but not labeled: a white PVC-pipe frame with diagonal corner braces running
up to the mast (the same tensioned-cable-tetrahedron idea used elsewhere in the corpus, but built here
in rigid PVC rather than cable), a red lidded container (looks like a small utility bucket or tote,
not obviously a food-grade pail), a clear plastic jar or jug, and a short section of tubing connecting
the pump to the jar. No visible battery box, charge controller, or wiring enclosure — if the machine
carries any electronics beyond the panel-to-pump connection, it is not visible in this photograph.

**A separate document should not be used for this machine's dimensions.** `manatee-manual/ref/DX-5dwPOND.jpg`
is a SketchUp rendering (a human figure composited in for scale — not a photograph of a real person
standing next to a real machine) showing a different, more elaborate concept: a round floating
platform with a glass pyramid enclosure, twin torpedo-shaped floats, and a machine that converts
duckweed into something labeled "PDRF... stored on board," under a heading "PHASE 1: set up for
S.P.I.S.E." This is a distinct, never-built concept design, not the machine in the 2016 photo. It
should not be blended into this BOM even though `machine-record-audit-20260806.md` groups it with the
2016 machine's evidence — the underlying file is annotated as a design study, not a build record.

**Yield and production numbers on any of these source images are Rudy's own assertions, not
independent measurements, and are not repeated here as fact** — per the project's standing rule
(`CLAUDE.md`, `machine-record-audit-20260806.md` §"Firewall exposure").

---

## 2. Component list — sourcing status

| Component | Evidence | Sourcing status |
|---|---|---|
| Vertical-axis wind rotor, ~15 W | Photo annotation, "15 watt windmill" | **Unpriced — needs a sourcing pass.** No brand, model, or vendor documented anywhere in the archive. A small VAWT in this wattage class exists as a commodity/hobbyist product, but nothing in this project ties the photo to a specific part. |
| Solar panel, ~15 W, flat-mount | Photo annotation, "15 watt solar panel" | **Unpriced — needs a sourcing pass.** Same gap: no model number anywhere in the corpus for a panel this size. (The corpus does document a 100 W flat panel and a 305 W SunPower panel — both belong to the 2024 EVIE-2c CAD machine, not this one; see `cad/out/prime/parts_manifest.tsv` row `solar-panel`.) |
| Pump — nominal 1/10 HP (see §1 caveat: sourced range 1/100–1/4 HP across conflicting readings) | Photo annotation, contested across three sources | **Unpriced — needs a sourcing pass, and needs the HP question resolved first.** No pump brand/model documented for this specific unit anywhere in the archive. |
| Bucket / container (red lid, visible in photo) | Photo, unlabeled | **Unpriced — needs a sourcing pass.** Not clearly identifiable as a specific product from the photo (could be a generic tote, pail, or storage tub). The 55-gallon-drum BOMs elsewhere in the corpus price food-grade HDPE drums (`04-KIT-MANIFEST.md:153`, `~$180–230`; corrected in `mvp-launch-and-backlog-20260724.md:72` to `~$127`) — those prices are for a different, much larger vessel and do not transfer to whatever container is actually in this photo. |
| Jar (clear, visible in photo) | Photo, unlabeled | **Unpriced.** Likely a commodity glass or plastic jar; no size or model documented. |
| PVC pipe frame + pontoons | Photo, visible geometry | **Unpriced — needs both a sourcing pass and a dimensioning pass.** The photo shows a rigid PVC frame with corner-brace struts to a central mast. No pipe diameter, wall schedule, or cut length is documented for this specific configuration. (Pontoon diameter is separately unresolved across the *big*-machine documents — 6 in build notes vs. 14 in BOM strings vs. 24 in polished docs, per `04-KIT-MANIFEST.md:126` — and that contradiction has never been resolved for this small machine either, since no one has measured or re-derived a diameter sized to this machine's much lighter payload.) |
| Mast + corner-brace hardware | Photo, visible geometry | **Unpriced.** Fittings, clamps, and brace material are visible but not itemized anywhere. |
| Tubing / fittings (pump-to-jar) | Photo, partially visible | **Unpriced.** A short length of tubing and at least one barbed or threaded fitting are visible; nothing further is documented. |
| Battery, charge controller, wiring | No documentation found | **Not established as present.** No battery box or controller is visible in the reference photograph, and nothing in the corpus specifies electronics for this specific configuration. Before pricing anything electrical for this machine, confirm whether it ran on direct panel/turbine power with no storage, or whether an enclosure exists that simply isn't visible in this one photo. |
| Cavitation nozzle | Not evidenced for this machine | **Do not include.** Every documented nozzle spec, BOM line, and price in the corpus belongs to the big/drum machine's process train. The 2016 pond machine's separation stage, per the record, is the bucket and jar — there is no evidence it used a pressurized nozzle at all. |

---

## 3. What the existing $1,950 figure was actually for, and why it doesn't transfer

`manatee-manual/04-KIT-MANIFEST.md` prices a **"Demonstrator kit"** at **$1,950** and a **"Real
Machine"** kit at **$3,950**. Both are built up from a bill of materials that assumes:

- a 55-gallon HDPE reactor/settling drum (`04-KIT-MANIFEST.md:70`, `~$99`, or `:153`, `$180–230`);
- a triplex plunger pump and 24–48 V BLDC motor driving 250–400 psi through a stainless kinetic
  nozzle with ceramic orifice inserts;
- a 15-gallon translucent HDPE settling barrel;
- drum penetration fittings, gooseneck vents, and a drum cradle;
- rigging and frame sized to a catamaran hull carrying that drum's ~460 lb full weight.

None of that bill of materials describes the 2016 machine. The $1,950 and $3,950 figures are real
retail research for a different, much larger machine — they are not a starting point to discount or
scale down; they would need to be rebuilt from a completely different parts list.

**`WORKBENCH.md:72` already states this plainly**: *"the price ladder ($1,950 demonstrator is wrong
for a 1/10 HP machine)... need re-speccing."* This document is the first pass at that re-speccing,
and it stops at "here is the list and what's missing" rather than producing a number, per the
instruction not to invent prices.

---

## 4. What a price ladder needs before it can be honest

In order, the actual blocking steps:

1. **Resolve the pump-HP contradiction** (§1). Three sources give three different numbers spanning
   25×. This has to be settled — ideally by finding a higher-resolution copy of the source photograph,
   or asking Rudy directly — before any pump can be selected, let alone priced.
2. **Identify or measure the actual container(s)** — the bucket and jar visible in the photo have no
   documented make, model, or size. A rough size estimate from the photo (relative to the pump and
   frame) could narrow the search, but that is a sourcing task, not something to guess a price for
   here.
3. **Settle the frame dimensions.** No pipe diameter or cut length is documented for this specific
   small machine. The big-machine pontoon-diameter dispute (6 in / 14 in / 24 in) is a warning sign,
   not a source to copy from — this machine needs its own measurement or a scaled re-derivation from
   the photo against a known reference object (the pump, the jar, or a hand/arm if one appears in an
   unlabeled photo).
4. **Confirm or rule out electronics.** If there's no battery or controller, the price ladder is
   shorter and the "power & electronics" system page collapses to two line items (panel, turbine). If
   there is one, it needs to be found in the archive or treated as a genuine unknown.
5. **Price each component independently** once 1–4 are resolved, using current retail sourcing (the
   same discipline already applied to the big-machine BOM in `04-KIT-MANIFEST.md`, which does cite
   real vendor SKUs and prices for its own — different — parts list).
6. **Then, and only then, build the ladder** — a demonstrator/kit/plans tier structure can reuse the
   existing four-tier shape (`Build anywhere` / `Observer add-on` / a physical-kit tier / a
   complete-machine tier), but every dollar figure in it needs to come from the small machine's own
   sourced parts, not a discount off the drum machine's numbers.

Until step 1 is resolved, nothing downstream of it can be priced honestly — a bill of materials for a
1/100 HP pump and one for a 1/4 HP pump are not close enough to average.

---

## 5. Sources

- `reference-clean/pond-machine-2016-noclaims.jpg` — viewed directly for this draft; captions
  quarantined, geometry kept, per standing project rule.
- `machine-record-audit-20260806.md` — the cross-checked evidence base; establishes the 2016 machine
  as the only one with any evidence of producing output, and the 15 W / 15 W / 1/10 HP reading.
- `due-diligence/systems/energy.md:69`, `due-diligence/systems/frame.md:40` — conflicting
  transcriptions of what each describes as the same source photograph's caption.
- `manatee-manual/04-KIT-MANIFEST.md` — the big-machine kit pricing ($1,950 / $3,950 / $199) and its
  underlying parts list.
- `manatee-manual/ref/DX-5dwPOND.jpg` — viewed directly; a distinct concept rendering, flagged here so
  it is not mistaken for evidence about the 2016 machine's dimensions.
- `cad/out/prime/parts_manifest.tsv` — confirms the 100 W / 305 W panel and bilge-pump-cartridge parts
  belong to the 2024 EVIE-2c CAD export, not this machine.
- `WORKBENCH.md:69-73`, `.board/.resolved/decide-which-machine-sol0010.md` — the ruling this document
  works from.
