# Buildability — the reactor core (cavitation nozzle and processing train)

Lane: reactor-core. Written 2026-08-11 against the archive as it stands on disk.
Scope: the processing core only — the microbubbler, the eductor, the cavitation nozzle, and the
separator. The raft, frame, pontoons, power and steering are other lanes.

---

## Bottom line

**A competent hobbyist cannot fabricate the reactor core from what exists. Not "with difficulty" —
the archive does not contain enough geometry to make a part, and what it does contain is
self-contradictory by a factor of eleven.**

The core is real in the sense that it was named, drawn, listed on bills of materials, and something
made a floating oily layer in front of witnesses. It is not real in the sense of being specified.
There is exactly **one** original piece of nozzle geometry in the entire archive — a 2008 TurboCAD
sketch — and it is published at three mutually incompatible scales, carries five dimensions of which
three are mis-snapped, has no axial dimension at all, no section view, no depth, no port, no
tolerance, and no surface finish. The 2012 file that the record calls a second, re-drawn production
size is not re-drawn: it is the 2008 sketch squashed 7.5% on one axis and shrunk, so its bores are
ovals.

The good news is genuinely good, and it is bigger than it looks. The gap is **recoverable — but by
re-engineering from open literature, not by recovering Rudy's drawing.** Hydrodynamic-cavitation
orifice reactors for biomass are a live, published, peer-reviewed field with concrete design rules,
and the whole patent estate is expired, so nothing blocks a clean-sheet design. The honest position
for a DIY site is: *here is the machine that ran, here is the inventor's sketch of its core, here is
what the sketch does and does not tell you, and here is a nozzle we designed to published cavitation
practice that you can actually cut.*

**The decision this lane forces: publish the reactor core as an open engineering problem with a
designed-from-literature reference nozzle, or do not publish a reactor core at all.** Publishing
Rudy's drawing as buildable plans would be dishonest and would produce parts that cannot cavitate.

---

## Corrections that lead

Four things the project record currently asserts are wrong. Each one changes a downstream decision,
so they go first.

**1. The nozzle IS claimed in US 7,750,494 — the record says it never was.**

`CLAUDE.md`, `WORKBENCH.md` line 336, and `due-diligence/systems/_validation-ip.md` §3 all state
that the cavitation nozzle was never claimed. Reading the granted patent directly (downloaded from
patentimages, full claim text extracted) shows three claims that recite it:

- Claim 9 and claim 10 — "wherein the catalyzer comprises a cavatition inducing nozzle, wherein the
  optimized solution is forced through said nozzle, causing a portion of the optimized solution to
  reach a Supercritical state…" (the misspelling "cavatition" is the patent's own, twice)
- Claim 19 — the method equivalent: "forcing the optimized solution through a cavitation inducing
  nozzle…"
- FIG. 14 is titled, in the patent's own list of drawings, "a schematic of the algae derived
  hydrocarbon production system 127 and process of the invention **utilizing a cavatation inducing
  nozzle as a catalyzer**."

This does not change the practical conclusion, and in one way it strengthens it — but the reasoning
has to be right, because a buyer's counsel will read the patent. The claims are **purely
functional**: they recite the nozzle by what it does, never by what it is. No bore, no count, no
material, no pressure, no geometry. FIG. 14 draws it as an **empty rectangle labelled 147** in a
block-flow diagram. So the correct statement is not "the nozzle was never claimed" but:

> Both patents are expired, so nothing is enforceable. The nozzle *is* claimed in '494, but only
> functionally — the patent teaches nothing about how to build one, and its only drawing of the
> nozzle is a labelled box. There is nothing to infringe and nothing to learn.

**2. `LVKNprocess.txt` is not an independent engineering note — it is the patent specification.**

The "Thermo-Electric Conversion of Organic Compounds" document that carries the whole physics story
(100 ft/s, 3% per pass, 204.84 BTU, tetra-helical vortex, 15,000 rpm, absolute zero pressure,
1500 °F, 1000 Ångström zone, the 0.04-inch secondary zone) appears **verbatim inside the granted
patent's detailed description**. Same sentences, same numbers. The due-diligence treats it as one
source and the patent as another; they are one document counted twice. Anywhere the record says
"the inventor's derivation is corroborated by the patent," delete that — it is the same text.

The practical consequence: since the patent is expired, that text is public domain. It can be quoted
and republished freely. But quoting it does not make it true, and the physics validation memo
(`due-diligence/systems/_validation-physics.md`) already rules the "absolute zero pressure" and
"stable 15,000 rpm zone" claims impossible. **Being in an issued patent is not evidence.**

**3. The "inventor's own eductor cutaway" is almost certainly a vendor's product illustration.**

`WORKBENCH.md` line 186 tells the project lead, in answer to a direct question, that the eductor is original
and cites "his labelled cutaway `AZ_Tank_Eductor_2_web.jpg`." Four things point the other way:

- **Compatible Components Corp sells a product line literally called "AZ Tank Eductors"**
  (cccmix.com), 0.5 to 2 inch, 304 and 316 stainless, no moving parts, marketed on a 4:1
  circulation-to-feed ratio. The archive filename is `AZ_Tank_Eductor_2_web.jpg` — vendor name,
  product line, image index, and a `_web` suffix typical of a saved web asset.
- The labels on the image — "Feed Inlet," "Induction Port (4)," "Blended Mixture" — are the generic
  nomenclature of a tank mixing eductor, not project-specific language.
- The art is vendor CAD marketing style: gradient-shaded body, gold internals, blue directional
  arrows, drop shadow.
- The same file exists twice under two names — `AZ_Tank_Eductor_2_web.jpg` and `Eductor Pump +
  Cavitation Nozzle schematic.jpg` — and they are **byte-identical** (md5 f90789d4ebd4888efcadde03453bac34).
  `due-diligence/systems/processing.md` line 51 lists them as two separate evidence items, so the
  eductor's evidence base is one file counted twice, and the second filename asserts a nozzle that
  is not in the picture.

Confidence: high, not certain — the definitive check is a reverse-image search or a look at the
vendor's own catalogue art, which is a five-minute job nobody has done.

**This is good news, not bad.** It means the eductor is not a mystery part to reverse-engineer — it
is an off-the-shelf 316 stainless tank mixing eductor available in half-inch to two-inch sizes from
several vendors. Stage 2 of the train is a purchase, not a fabrication. What must change is the
claim that it is Rudy's design, and the removal of the second filename.

**4. The 2024 CAD model contains no processing core at all.**

`due-diligence/systems/processing.md` line 38 states that in the EVIE-2c PRIME design "a cylindrical
processor/growth drum sits low and central between the twin pontoons, slung inside the tensegrity
frame," and calls it a "single drop-in drum module at the platform's center of buoyancy."

The extracted parts manifest (`cad/out/prime/parts_manifest.tsv`, 20 parts) contains: mast stays,
four frame rails, deck cross-members, four pontoon tubes, three bilge-pump cartridges, a wind rotor,
a mast tube, a deck capacitor, a small deck pump, a flat solar panel, a scale figure — and one
unexplained part called `vessel-squat-cylinder`, **0.415 m across by 0.093 m deep**, sitting on the
**aft starboard corner**, not central. `cad-photo-gap-20260807.md` line 354 grades that part "LOW —
not identifiable in the archive." Looking at the rendered thumbnail confirms it: a shallow grey can
resting on one pontoon, about the proportions of a cake tin. It is not a reactor.

Two further absences in the same model: the SketchUp file defines components named "bladder tank#2"
and "15 Gallon Water Barrel", and **neither is placed anywhere in the model** — zero instances. The
only 55-gallon drum in the file is stretched into service as the four pontoon tubes.

So the design that every 3D effort targets has a frame, floats, a mast, a rotor, a panel, and three
bilge pumps, and **no tank, no pump train, no nozzle, no separator, no storage**. The reactor is not
under-detailed in the CAD; it is absent.

---

## What the core is, mechanically

Stripped of the marketing, it is a four-stage recirculating loop. Nothing in it is exotic except
stage 3.

**Stage 1 — Concentrate the algae by flotation.** Fine bubbles are injected at the bottom of a
column; algae attach and rise into a foam that is skimmed off. This is dissolved-air flotation, a
standard water-treatment method. It is the one stage with an unambiguous build photograph:
`Seasteading/_ARCHIVED/06_Media/Photos/BEAR Microbubbler1.jpg` shows four clear PVC columns plumbed
with white PVC and red ball valves inside a hoop greenhouse, one column visibly green, draining to a
blue 55-gallon drum. That rig is real and was built.

There is an unresolved contradiction about how concentrated the feed gets. `9x9HVO_process.txt` says
"more than 6% by weight… a light sensor indicates when it is dense enough." A subsystem document
elsewhere says roughly 30% solids. Those are different feedstocks by a factor of five, and the
difference sets the whole energy balance, because every point of water is water you pay to pump.
Flotation alone plausibly reaches 6%; 30% by flotation alone is not credible without a second
dewatering step.

**Stage 2 — Pressurize with an eductor and a pump.** An eductor is a venturi with no moving parts:
a fast motive jet drags surrounding fluid in through side ports and mixes it. Off-the-shelf part
(see correction 3). The pump is the only line item in any bill of materials with a real link:
`JT1BOM_strings.txt` names an **AR RMW2G24D, 300 psi at 10 gpm, 12 VDC**, with a pwoutlet.com URL —
a vertical pressure-washer pump.

**Stage 3 — Push it through the nozzle.** This is the invention and the subject of everything below.

**Stage 4 — Let the oil float off and decant it.** No distillation, no heat. The converted material
floats; fresh slurry pumped in raises the water level and pushes the floating layer over into a
collection bladder; an S-shaped tube with a below-surface inlet returns green water to the growth
tanks. Described plainly in `9x9HVO_process.txt`. Mechanically this is gravity separation plus
displacement decanting, which is about as simple as separation gets.

---

## The nozzle: every scrap of geometry the archive contains

There is one original drawing. Everything else is a copy, a render, or a caption.

Original files, all in `~/Downloads/Model-JTfree1NEW/KNdwg/` (mirrored to
`Personal/Seasteading/_ARCHIVED/01_Robot-Technology/CAD/` and, as JPGs, to
`Personal/ventures/solaris-cybernetics/manatee-manual/ref/`):

- `KineticNozzle1.DXF` — 122,794 bytes, file-dated 13 Dec 2008. AutoCAD 2007 exchange format,
  authored in TurboCAD. 72 lines, 9 circles, 5 dimensions, a title block reading "Kinetic Nozzle"
  and "306 S.S."
- `KineticNozzle1.TCW` — the TurboCAD source of the same, 12 Dec 2008.
- `KineticNozzle1.JPG` — a render of the above, dimensions shown in inches.
- `KineticNozzle1BBB.JPG` — the identical drawing rendered with a different unit scale.
- `KineticNozzle5gpd.DXF` and `.TCW` — 4 Mar 2012. Same title block, same "306 S.S."
- `CanardProcessFlow.JPG` — the plumbing schematic tying pump, nozzle and two tanks together.
- `Pyrolizer-Separator-AutoCAD.DWG` / `.JPG` — the separator general-arrangement, title-blocked
  **a third-party reference design**. Under project rules this is IP-quarantined; do not copy it.

That is the complete set. There is **no photograph anywhere in the archive of a machined cavitation
nozzle.** The file `BEAR cavitation nozzle close up.jpg` — which the due-diligence cites as physical
proof — shows two small polished stainless pressure vessels with domed ends, quarter-inch compression
fittings and bent stainless tube, sitting on OSB with wood blocks under them and a handwritten note
beside them. They are vessels with tube ports. Nothing in the photograph is a multi-bore nozzle, and
nothing in it is dimensioned or labelled. It is evidence that Rudy fabricated stainless plumbing. It
is not evidence of the nozzle.

### What the 2008 drawing actually shows, measured from the vector file

Reading the DXF geometry directly rather than the render, the front view contains a body circle and
eight inner circles:

- Body — 4.1912 in diameter (the drawing calls it 4.20 in)
- One inner circle 0.7422 in diameter, roughly concentric (the drawing calls it 0.73 in)
- One hole at the centre, 0.2418 in
- Three outer holes, 0.2682 / 0.2473 / 0.2418 in, on radii of 0.3499 / 0.3859 / 0.3883 in
- Three inner holes, 0.1710 / 0.1710 / 0.1499 in, on radii of 0.1594 / 0.1765 / 0.1888 in

So the part is **seven bores in two triads around a central bore**, not the "one central plus three
surrounding" tetrahedral cluster the due-diligence describes. That matters for flow area by about a
third.

Checking the dimension entities' snap points settles a question the manuals hedge on: the callouts
are **hole diameters, not hole spacings**. The 0.25 in dimension runs from x=3.45828 to x=3.71274 at
constant y — the left and right edges of the top hole. The 0.16 in dimension likewise spans the
lower-left small hole. `manatee-manual/00-GROUNDING.md` line 23 reads them as "orifice spacings";
that is wrong and it changes the computed flow area by roughly a factor of two.

### Why it is a sketch and not a drawing

Three measurements say this was placed by eye, not constructed:

- The three holes nominally called 0.25 in are drawn at 0.2418, 0.2473 and 0.2682 — a **10.9% spread**
  across supposedly identical features. The three called 0.16 in are drawn at 0.1499, 0.1710 and
  0.1710 — a **14.0% spread**.
- The outer triad is not on a 120° pattern. The three angular gaps measure **107.8°, 125.0° and
  127.2°**. Their bolt-circle radii differ by 11%.
- Three of the five dimensions are mis-snapped. The 4.20 in body dimension's two extension-line
  origins differ in y by 0.33 in, which a true diameter dimension cannot. The 0.73 in dimension runs
  from the *centre* of the top hole to the *bottom edge* of the inner circle, so it measures nothing
  in particular and lands within 0.01 in of the inner circle's diameter by luck.

None of the seven bores carries a "3 PLACES" or "TYP" note, so a machinist has no instruction to
regularise them, and the drawn geometry does not agree with the callouts.

### The three-scale problem

The same geometry is published at three different sizes, with nothing anywhere saying which is real.

- `KineticNozzle1.JPG` — body 4.20 in, holes 0.25 and 0.16, feature 0.73
- `KineticNozzle1BBB.JPG` — body 0.3782 in, holes 0.02225 and 0.01424, feature 0.0649
- `KineticNozzle5gpd.DXF` — body 1.06 in, holes 0.06 and 0.04, feature 0.20

The BBB render is the 2008 drawing at **1/11.1 scale**; every callout scales at 11.24 to 11.25 within
rounding. The 2012 "5gpd" file is the same drawing again, at about **1/3.98**.

Here the record is wrong in a way that matters commercially. `03_ADDENDA.md` lines 472–521 argue at
length that `KineticNozzle5gpd` is a genuinely re-drawn second production size — "real engineering
work on a discrete second size," giving "the Tier-2 bench-loop kit and the razor-blade
replacement-cartridge offer a real, drawn second SKU." The reasoning was that the 2012 file contains
"0 CIRCLEs, built from 51 LINEs." That is a parser artifact: the 2012 file's round features are
stored as **ELLIPSE** entities, which the addendum's extraction did not count.

Normalising both files to their body diameter, all nine features match to fifteen decimal places in
y and in radius, and differ in x by exactly one constant — **0.925184**. In plain terms: somebody
selected the 2008 drawing, scaled it to 27.18% in one direction and 25.15% in the other, and saved
it. It is a photocopy with a squash, not a redesign.

Two consequences. First, there is no second SKU; the kit catalogue and the replacement-cartridge
story rest on one geometry, not two. Second, and worse for anyone trying to build it: **the 2012
part's bores are not round.** They are ellipses 7.5% out of true, and the "1.06 in" body callout is
measured across the squashed axis, so the body as drawn is 1.054 in one way and 1.139 in the other.
A machinist cutting the 2012 file literally would produce an oval part with oval holes.

### What the drawing does not specify, at all

The right-hand view is a rectangle 4.21 in wide and 3.73 in tall, with a group of horizontal lines
across the lower third. It carries **one** dimension — the 4.20 in width, repeated from the front
view. There is no height dimension and no section.

Therefore the following are absent from the record entirely, and every one of them is load-bearing
for whether the part cavitates:

- **Overall length / body height.** Undimensioned. Scaled off the drawing it is about 3.73 in, which
  is a measurement of a picture, not a spec.
- **Bore depth, and whether the bores are through-holes or blind.** Nothing.
- **The axial profile of each bore** — this is the entire hydrodynamic function. Straight cylinder?
  Convergent cone? Convergent-divergent? Inlet chamfer angle? Exit expansion half-angle? Nothing.
  In published cavitation practice the throat length-to-diameter ratio and the plate thickness are
  the parameters that decide whether you get cavitation inception, a stable cavity cloud, or just a
  pressure drop.
- **Inlet and outlet identification.** Which face does flow enter? The drawing does not say, and the
  seven-bore pattern is not symmetric, so it is not obvious.
- **The 0.7422 in inner circle's meaning.** Counterbore? Plenum? Bore-circle construction line?
  Unlabelled.
- **How it mounts.** No thread, no port, no flange, no O-ring groove, no wrench flat, no hose
  connection. A 4.2-inch stainless cylinder with holes in it is not a plumbable component.
- **Material.** The title block says "306 S.S." There is no AISI 306. It is almost certainly a typo
  for 316, which is what you would want, but it is an uncorrected typo carried on both files across
  four years.
- **Surface finish.** Absent, and it is not cosmetic here — cavitation erosion initiates at surface
  defects, and bore finish is a first-order variable in nozzle service life.
- **Tolerances.** None anywhere.
- **Erosion allowance or service life.** No test data of any kind. The subsystem note
  `Seasteading/_ARCHIVED/01_Robot-Technology/Subsystems/KINETIC_NOZZLE.md` lists pitting as a known
  risk and offers no numbers.

### The flow arithmetic — and the one thing it does resolve

Taking the callouts as diameters and the geometry as seven bores (four at the larger size, three at
the smaller), total open area works out to:

- 4.20 in body — 0.2567 in², or 165.6 mm²
- 1.06 in body — 0.0151 in², or 9.73 mm²
- 0.3782 in body — 0.0020 in², or 1.31 mm²

The inventor's own requirement is 100 ft/s (30.5 m/s) through the bores. Flow needed to hit that:

- 4.20 in body — **80 US gpm**
- 1.06 in body — **4.7 US gpm**
- 0.3782 in body — **0.63 US gpm**

Now compare against the only two pumps specified anywhere in the archive. The AR RMW2G24D from
`JT1BOM_strings.txt` is 10 gpm. The `BOM1BB1m5.csv` for the pond-class machine names a **Medog 12 V
DC, 1.35 gpm, 116 psi diaphragm pump**. Running each pump into each nozzle:

- 4.20 in body on the 10 gpm pump gives **12 ft/s** — an eighth of what is needed. It cannot cavitate.
  On the 1.35 gpm pump it gives 2 ft/s.
- 1.06 in body on the 10 gpm pump gives 213 ft/s at full flow, and hits exactly 100 ft/s when
  throttled to 4.7 gpm — comfortably inside the pump's envelope.
- 0.3782 in body on the 1.35 gpm pump gives 213 ft/s; it hits 100 ft/s at 0.63 gpm.

Pressure required for 100 ft/s across an orifice is 67 psi ideal, about **105 psi** at a realistic
discharge coefficient of 0.8 and about **175 psi** at 0.62, before line losses. So the "300 psi"
figure in the process text is not an overclaim — it is a reasonable working pressure with margin.
And the cavitation number at 100 ft/s, 150 °F feed and atmospheric downstream comes out at **0.16**,
which is well inside the cavitating regime (below about 1). *The velocity and pressure story holds.
It is the geometry that does not.*

This gives one useful reconstruction, and it should be labelled as a reconstruction, because the
archive nowhere states it: **the 1.06 in nozzle is the only one of the three scales that pairs with
a pump in any bill of materials, and the 2012 nozzle file and the 2012-era JT-1 bill of materials
are contemporaries.** That is circumstantial, not documented. Treat it as the best working hypothesis
for which scale Rudy meant, and confirm it with him rather than publishing it as fact.

*Every number in this section is computed here from the vector geometry and the bills of materials.
None of it appears in the archive. Any of it could be wrong if the callouts are not diameters or the
hole count is not seven — both of which I read off the file rather than off a note.*

---

## The separator and the rest of the train

**The separator drawing is the best engineering document in the archive and cannot be used.**
`Pyrolizer-Separator-AutoCAD.JPG` is a clean, fully-labelled general arrangement: a "Kinetic Nozzle"
block feeding five parallel stainless tubes into a plenum, then a collection tank, with a motor and
pump on a common base plate and a scale bar around five feet. Its title block reads Project Name:
from three named Ceres IP assets and this is exactly the downstream-process subject matter most
likely to sit inside them. **Do not copy it, do not trace it, do not publish it.**

Worth noting what it shows about the nozzle anyway, since it is the only other depiction: the
"Kinetic Nozzle" there is a rectangular manifold block feeding **five** parallel tubes. That is not
the 4.2-inch seven-bore cylinder in the DXF. So even inside the archive, "kinetic nozzle" names at
least two physically different things.

**The separator itself needs no invention.** Gravity stratification plus displacement decanting is
buildable from a vented drum, a floating skimmer, baffles and a sight tube — which is exactly what
`manatee-manual/02-IMPROVED-MANUAL.md` §8 already specifies, in detail, competently. That manual is
the strongest engineering document the project has produced and its process section is honest: it
right-sizes the pump, replaces the unknown-bore nozzle with a holder taking known-bore carbide
inserts, adds a relief valve, and says plainly at line 71 that the "actual nozzle bore diameter and
orifice count on any original part" must be measured. It got there without knowing what I have just
measured, and nothing I found contradicts it.

---

## The evidence artifacts, re-graded

The processing dossier's evidence table grades several items higher than the files support. Handling
these correctly is a liability question, not a pedantry question.

**The AECOM/PACE result is not a lab report.** `SC1aecom1report2.md` is a Solaris Cybernetics
company document on company letterhead with a phone number and website, written in the first person,
signed "Rudolph Behrens, CEO." It describes results and says the PACE analysis is "attached." **The
attachment is not in the archive.** The body of the document is where the "adiabatic
(thermo-dynamically reversible)… much of the energy used in the conversion is recovered" claim comes
from — a Second-Law overclaim, per `_validation-physics.md` §7. So the strongest single artifact in
the corpus is, as filed, a company-authored summary of a third-party report nobody has. Getting the
raw PACE sheet is the single cheapest credibility upgrade available.

**The 2012 fuel assay is a spreadsheet printout.** `BEARfuelTest1.pdf` is one page reading "Sheet1"
at the top and "Page 1" at the bottom — an Excel print. It carries **no laboratory name, no
letterhead, no report number, no accreditation, no analyst signature, and no chain of custody.**
"Drawn By: Submitted Samples" means the client supplied the sample. It reports three numbers: D4052
API gravity 32.71°, D240 gross heat of combustion 18,254 BTU/lb and 134,258 BTU/gal, on a sample the
client designated "BIO DIESEL." The numbers may be perfectly genuine; the artifact cannot establish
that they are. And as `science.md` and `_validation-physics.md` both note, density and calorimetry
identify no molecule at all — they cannot distinguish cracked hydrocarbon from raw algal oil.

**`KINETIC_NOZZLE.md` is a later synthesis, not primary evidence.** It sits in
`Seasteading/_ARCHIVED/01_Robot-Technology/Subsystems/` and reads as a written-up summary: it asserts
patent protection that is functionally void, repeats "306 Stainless Steel," and closes by directing
the reader to "`06_Media/Photos/KineticNozzle1.JPG` for high-resolution physical documentation" — a
file that is a line drawing, not a photograph, and is not at that path. Anywhere the record cites it
as a source, the underlying source is the patent text.

**One image, two filenames, counted twice** — see correction 3.

**One further IP note:** `9rules[1].txt` in the converted corpus is John Todd's "Nine Principles for
Designing Living Machines," third-party authorship. It is fine as background reading and must not be
republished as project content.

---

## Could a competent hobbyist fabricate this core?

Taking the stages one at a time, because the answer differs sharply by stage.

**Stage 1, the flotation concentrator — YES, today.** Clear PVC columns, an air pump, a diffuser, a
skimmer. Standard practice, photographed as built, nothing proprietary. A competent hobbyist could
reproduce the microbubbler from the photograph and a water-treatment textbook.

**Stage 2, the eductor and pump — YES, today, by purchase.** Both are catalogue parts. The eductor is
an off-the-shelf 316 stainless tank mixing eductor. The pump is a named model with a live product
class. No fabrication required.

**Stage 3, the cavitation nozzle — NO.** Not from this archive. A machinist handed
`KineticNozzle1.DXF` would have to ask, before touching a bar of stainless:

1. Which of the three scales do I cut? (The archive does not say, and they differ 11:1.)
2. How long is the part? (Undimensioned.)
3. How deep are the holes, and do they go through? (Unstated.)
4. Are the holes straight bores, or tapered, and at what angles? (Unstated — and this is the part
   that decides whether it works.)
5. Which end is the inlet? (Unstated.)
6. Are the holes really different sizes, or is that drafting scatter? (The geometry and the callouts
   disagree; nothing resolves it.)
7. How does it connect to a hose? (No port, no thread, no flange anywhere.)
8. 306 or 316? (306 does not exist.)

Every one of those is a stop-work question. None is answerable from the archive. And the flow
arithmetic adds a ninth: the largest and most-cited scale needs 80 gpm, and the biggest pump in any
bill of materials delivers 10.

**Stage 4, the separator — YES, today.** Gravity, a drum, a weir, a skimmer, patience. Already
specified competently in the improved manual.

**So: three of four stages are buildable now. The fourth — the one the whole thing is named for —
is not.**

---

## What exactly is missing, and where each piece is recoverable from

Ordered by what unblocks the most.

**Recoverable from Rudy, and only from Rudy:**

- Which scale is the real one, and whether a physical nozzle still exists. If one survives, a
  caliper, a pin gauge set and a bore scope close the entire geometry gap in an afternoon. This is by
  far the highest-value question to ask him, and it is a five-minute phone call.
- The bore profile: straight, tapered, or stepped, and the entry angle. Nothing in the archive
  records it.
- Which pump actually ran on which machine. The pond machine's photo annotation says "1/10th HP
  pump," `BOM1BB1m5.csv` names a 1.35 gpm / 116 psi Medog diaphragm pump, `JT1BOM_strings.txt` names
  a 10 gpm / 300 psi AR pressure-washer pump, and `small-machine-bom-draft-20260807.md` §1 documents
  that internal project sources disagree across a 25× range on the pond machine's pump alone. Pump
  and nozzle are one design decision; neither can be settled without the other.
- Whether the pond machine had a nozzle at all. Looking closely at
  `reference-clean/pond-machine-2016-noclaims.jpg`, the fluid circuit is a small diaphragm pump, a
  short amber flexible hose, a grey hose looping down into a clear tub through a white plastic
  fitting, and a red-lidded container. **No stainless nozzle body is visible, and the annotation does
  not mark one** — it marks the windmill, the solar panel and the pump only. `small-machine-bom-draft-20260807.md`
  line 76 already reaches the same conclusion independently and says do not include a nozzle in that
  machine's bill of materials. If the machine that demonstrably ran had no nozzle, that is the single
  most important fact in this lane and it is one question away.
- The raw PACE laboratory sheet behind `SC1aecom1report2.md`.

**Recoverable from the patents: nothing useful.** I read both. '494 claims the nozzle functionally in
claims 9, 10 and 19, describes it in prose lifted from `LVKNprocess.txt`, and draws it as an empty
box in FIG. 14. '903 is the earlier, narrower wind-to-synfuel vessel. Neither contains a dimension, a
bore count, a material, or a profile. The patents settle the freedom-to-operate question and
contribute nothing to buildability.

**Recoverable from open literature: the whole design, cleanly.** This is the finding that changes the
plan. Orifice-plate hydrodynamic cavitation for biomass is an active, published field with concrete,
reproducible design rules — the gap is a re-engineering job, not a research project.

The most directly useful reference found: Roy, Rudra, Muhandiram and Roshid, "Numerical modelling and
experimental validation of an orifice plate-based hydrodynamic cavitation process for improving the
biomass pretreatment," *Biotechnology Reports* 48 (2025) e00925 — open access, CFD plus experimental
validation. Its optimised geometry: **nine holes of 2.0 mm through a 4 mm plate** (thickness-to-diameter
ratio 0.16), inlet pressures of 1.4 to 1.9 bar, throat velocity 23.4 to 25.3 m/s, cavitation numbers
0.31 to 0.93, running 2% by weight biomass at 0.8 mm particle size. Plate thickness is reported as
significantly influencing cavitation inception — which is precisely the dimension Rudy's drawing
omits. Total open area of that plate is 28.3 mm².

Set that beside the Behrens geometry and the convergence is striking: nine 2 mm holes versus seven
holes of 4 to 6.4 mm; 77 to 83 ft/s throat velocity versus the claimed 100 ft/s; 20 to 28 psi versus
105 to 175 psi. **Same family of device, same operating regime, one of them measured and published.**
The older standard design reference is Gogate and Pandit, "Engineering design methods for cavitation
reactors II: hydrodynamic cavitation" (AIChE Journal, 2000), which gives the orifice-plate design
methodology in general form.

Design-around constraints stay as the project already has them: avoid the live cavitation patents
(ODU 8,778,035, CVAT, Hielscher) and do not copy the a third-party reference design drawing. Note from `03_ADDENDA.md` that
Hielscher's process is **acoustic** cavitation driven by a mains-powered ultrasonic horn and is
usually solvent-coupled — architecturally a different machine from a passive hydrodynamic orifice, so
the design space here is genuinely open.

**Recoverable only from a bench:**

- The nozzle's real service life under cavitation erosion. Zero data exists. Run one nozzle
  continuously and borescope the bores at 24, 72 and 168 hours. This is cheap, it is just time, and
  it is the number the consumable-cartridge business model depends on.
- Whether the output is cracked hydrocarbon or merely extracted lipid. A GC-MS plus a distillation
  curve settles it for a few hundred dollars, and `_validation-physics.md` and `03_ADDENDA.md`
  already specify the three-way test correctly.
- The actual energy in versus oil out on a closed loop. Never measured. A watt-meter and a scale.

---

## Recommended path for this lane

1. **Ask Rudy the geometry questions before anything else is built or written.** Does a physical
   nozzle survive; which scale is real; are the bores straight or tapered; which end is the inlet;
   did the pond machine have a nozzle at all. Five questions, one call, and they collapse most of
   this document.
2. **Publish the 2008 drawing as an artifact, never as plans.** It is genuinely interesting — a
   handmade 2008 TurboCAD sketch of a seven-bore cavitation nozzle by a career pump engineer — and it
   belongs on an honest site with its scale ambiguity stated openly. Label it: *the inventor's
   original sketch, published at three incompatible scales, with no axial dimensions; here is what we
   measured off the file; here is what it does not tell you.* That is a better story than a fake spec
   and it invites exactly the audience the project wants.
3. **Design a reference nozzle from published practice and ship that as the buildable part.** Start
   from the Roy et al. plate geometry, scale the open area to whatever pump the kit specifies, and
   publish it with a full drawing: bore count, diameter, plate thickness, entry chamfer, exit
   geometry, material, finish, tolerance, port thread. Say plainly that it is our design informed by
   published cavitation research and by Rudy's sketch, not a reproduction of his part. Both patents
   being expired means nothing prevents this.
4. **Adopt the improved manual's holder-plus-insert architecture as the reference design.**
   `manatee-manual/02-IMPROVED-MANUAL.md` already specifies a 316L holder carrying known-bore inserts
   with a quick-change fitting. That solves the unknown-bore problem, the erosion problem and the
   consumable-part business model in one move, and it is honest because the insert bore is a number
   we chose and can defend.
5. **Fix the four corrections above at source** — in `CLAUDE.md`, `WORKBENCH.md` line 336 and 186,
   `due-diligence/systems/_validation-ip.md` §3, `due-diligence/systems/processing.md` lines 24, 38,
   51–53, `03_ADDENDA.md` lines 472–521, and `manatee-manual/00-GROUNDING.md` line 23 — before any of
   them gets copied into site copy.
6. **Do not put a reactor in any 3D render until the geometry question is answered.** The CAD has no
   reactor; inventing one for a render would put a fabricated part in front of the public under a
   project whose whole discipline is not doing that.

---

## Claims that must never appear on the site, from this lane

Beyond the project's standing bans (Sea State 7, 10,000 lb thrust, patented AI, 19:1 EROI, ocean
diesel, diesel-grade fuel, 10 gal/day, any fuel yield number):

- **"Patented cavitation nozzle."** Both patents are expired. The claim is functional and teaches
  nothing. Say "the original patents are expired and in the public domain" and leave it there.
- **"Machine-ready CAD" / "CNC-ready DXF" / "toolpath-grade."** The file imports into CAM. What comes
  out is a sketch with 11 to 14% dimensional scatter, no axial geometry and no ports. Calling it
  machine-ready would send someone's money to a shop for a part that cannot be assembled.
- **"Two nozzle sizes" / "a second SKU."** There is one geometry, anisotropically scaled.
- **"Third-party validated" without qualification.** The lab sheet has no laboratory on it and the
  AECOM document is company-authored with its attachment missing.
- **Anything asserting the 1500 °F core, absolute zero pressure, 15,000 rpm, the 1000 Ångström zone,
  or the tetra-helical vortex.** These are the inventor's assertions, they are in the patent, and
  being in a patent is not evidence. Two of them are ruled physically impossible in the project's own
  validation memo.
- **"3% conversion per pass."** Never measured. It is a number in a document, divided into everything
  downstream of it.

---

*Sources read for this lane: `due-diligence/systems/processing.md`, `science.md`,
`_validation-physics.md`, `_validation-ip.md`; `03_ADDENDA.md`; `due-diligence/corpus/converted/text/`
(`LVKNprocess.txt`, `9x9HVO_process.txt`, `JT1BOM_strings.txt`, `VBShdl1BOM_strings.txt`,
`S3algaeRecipe.txt`, `9rules[1].txt`, `vc310B.txt`); `Seasteading/_ARCHIVED/01_Robot-Technology/`
(`KINETIC_NOZZLE.md`, `KNdwg/` DXF vector geometry parsed directly), `04_Prototype-Testing/Lab-Results/`
(`SC1aecom1report2.md`, `BEARfuelTest1.pdf`), `03_Business/Financials/BOM1BB1m5.csv`,
`06_Media/Photos/` (microbubbler, eductor, "cavitation nozzle close up"), `04_Prototype-Testing/2023-Marina-Tests/`
(all 15 container-machine photographs, which are from 2015 — the camera clock ran 35 years fast);
`manatee-manual/00-GROUNDING.md`, `02-IMPROVED-MANUAL.md`, `04-KIT-MANIFEST.md`;
`cad/out/prime/` and `cad/out/bimodal/` parts manifests and definition tables;
`reference-clean/pond-machine-2016-noclaims.jpg`; `small-machine-bom-draft-20260807.md`;
`cad-photo-gap-20260807.md`; `WORKBENCH.md`. External: full text and claims of US 7,750,494 B1
downloaded from patentimages; US 7,302,903 B1 status; Compatible Components Corp AZ Tank Eductor
product line; Roy et al. 2025, Biotechnology Reports 48 e00925; Gogate and Pandit, AIChE Journal 2000.*
