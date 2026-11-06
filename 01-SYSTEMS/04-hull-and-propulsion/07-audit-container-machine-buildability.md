# The container machine, part by part, as a builder would have to buy it

_2026-08-11. Covers one machine only: the four-pontoon PVC raft assembled inside a shipping
container and photographed fifteen times between April and July 2015. Not the pond machine, not the
55-gallon-drum raft, not the City Island machine, not the 2024 ocean concept._

_Every dimension below is sourced either to the CAD extraction (`cad/out/`) or to a named
photograph and region. Numbers handwritten or typed by the inventor are recorded as his assertions
and are never restated as fact. Where a component cannot be sourced, this document says "unknown —
needs a sourcing pass" rather than estimating._

---

## The answer, up front

**A builder could walk into a hardware store today and buy about a third of this machine with
confidence, roughly another third generically but without any rating, and could not buy the rest at
all.**

What is genuinely buyable, because the archive names it directly: the frame pipe (the pipe prints
its own specification and the photograph is sharp enough to read it), the frame fittings and pontoon
caps (the inventor typed a shopping list into the drawing), the electrical capacitor (its label is
legible), and the fastening consumables.

What is buyable in kind but not in specification: both pump types, the mast and stay tubing, and the
pontoon pipe. A builder can identify the category, walk to the right aisle, and then has to guess
the size or rating, because no rating appears anywhere in the archive.

What cannot be bought at all: the rotor, the masthead collar, the solar panel, the panel's mounting
structure, the electronics enclosure, and every one of the roughly thirty pipe fittings that
actually hold the frame together. Some of these are missing from the drawing entirely; others are in
the drawing as catalogue props, which is worse, because a prop looks like a specification.

**The single most consequential finding is that the drawing's pontoon diameter is a modelling
artefact and is about seventeen per cent undersize.** Anyone sizing buoyancy off the CAD understates
displacement per metre of pontoon by roughly forty-five per cent. Detail under "Pontoons" below.

**The single most useful finding is that the rotor is recoverable after all.** The manifest's squat
rotor is a non-uniformly squashed instance. The component definitions underneath it carry a coherent
full-height design — 48-inch wings on a 1.25-inch shaft — that is much closer to the photographs
than the placed part is. Detail under "Rotor" below.

---

## Three things that govern everything below

### 1. The drawing and the photographs are nine years apart, and nothing ties them together

The CAD is `VBShdl-1m5manatee2b1PRIME.skp`, saved August 2024, and its own text annotation names it
**EVIE-2c**. The photographs are from **April to July 2015**. The two share an architecture — four
PVC pontoon tubes in two touching pairs, a PVC pipe frame, a braced mast, a vertical-axis rotor, two
submersible pumps slung underneath — and the CAD's pairing geometry matches the photographs closely
enough that they are plainly the same design lineage.

But no dimension in the archive links them. No photograph contains a tape measure, a person, or a
dated drawing of the photographed machine. So: **the CAD dimensions the drawn design, and it is an
assumption, not a finding, that they dimension the 2015 machine.** Every "CAD says" line below should
be read that way.

**The 2015 dating is now established three ways**, and the folder name `2023-Marina-Tests` is wrong.
Every frame carries an EXIF creation date in the year 2050 from a Samsung ST66/ST68 whose clock ran
thirty-five years fast. `SAM_0249`, next in the same sequence from the same camera, carries a
corrected file date of 2016-03-06, which forces the 2050 dates back to 2015. And the duplicate of
`SAM_0220` in `~/Downloads/Model-JTfree1NEW/` has a filesystem date of 22 June 2015 against an EXIF
date of 2050-06-22 — same month, same day, thirty-five years apart. This confirms independently what
`panel-identity-20260811.md` established the same day.

### 2. One photograph in heavy use is a different machine

`LiftingInstructions.JPG` is cited throughout `cad-photo-gap-20260807.md` as evidence about "the
machine". It is not this machine. Its background sign reads PERRY W. GILBERT PARK, placing it on
City Island, Sarasota, and `machine-record-audit-20260806.md` already files it as a separate, later
build. Viewed directly, the differences are structural, not cosmetic:

Its mast is large-diameter white PVC stepping into grey plastic flanges; the container machine's is
a slim grey galvanised round tube. Its stays are thin stainless wire rope with swaged eyes; the
container machine's are four rigid galvanised tubes, flattened and bolted at both ends. It carries a
frameless flexible PV laminate with visible finger lines; the container machine carries a small
rigid dark-framed module. It carries a white deck plate with a printed inventory number under its
electronics; the container machine's electronics box sits directly on bare galvanised cross-tubes.
Its joints show purple primer bands and its pontoon pairs are bound with straps.

**Two attributes that `cad-photo-gap-20260807.md` reports as things "the photographs show" do not
appear on the container machine in any of the fifteen frames: purple PVC primer bands at the glued
joints, and worm-drive hose clamps binding the pontoon pairs.** Both are plainly present at City
Island. The container machine's visible joints are clean white, and its pontoons are carried by
white PVC risers and sockets dropping from the frame, not clamped to each other. This is a
correction, not a contradiction — that document flags the mast and the rigging as build-specific and
simply does not flag the rest.

### 3. There is a scale reference after all, and it is the pipe itself

`panel-identity-20260811.md` concludes that absolute sizes are unrecoverable because "nothing of
known size touches either machine in any frame." That is very nearly right, and one exception
matters a great deal.

**The frame pipe prints its own nominal size, and `SAM_0246` resolves it.** Mirrored and
contrast-stretched, the maroon legend running lengthwise along a deck-level member reads:

> …7200 · 2" PVC TYPE I SCH 40 · NSF-pw · ASTM D 2665 · PVC 1120 · PR 280 PSI @ 23°C · NSF-dwv…

Two-inch Schedule 40 PVC has a standardised outside diameter of 2.375 inches, 60.3 mm, and the 280
psi at 23 °C rating is the published figure for exactly that size and schedule, which corroborates
the reading. So there is a certified-dimension object in physical contact with the machine, in
several frames, and approximate absolute sizing is possible at roughly ±20 per cent for anything
photographed at a similar depth to a frame member.

This is the measuring stick used for the estimates below. It is a rough stick and every number
derived from it is flagged as such.

---

## What the drawing contains, and where it came from

Nineteen machine parts plus a scale figure. **Nine of the nineteen machine parts are third-party
catalogue components, drawn from five distinct catalogue models** — the pontoon tube, the bilge pump
cartridge, the deck pump, the capacitor and the solar panel. Ten are Behrens-drawn.

_A small correction: `CLAUDE.md` records this as "six of the nineteen kept parts". Six is the count
of catalogue **source files**, which includes the scale figure. Counted as parts on the manifest it
is nine of nineteen, because the pontoon component is instanced four times and the bilge pump
cartridge three times._

The drawn envelope, for orientation: overall beam 2.17 m across the outer pontoons, overall length
3.20 m along the pontoons, frame 2.54 m fore-and-aft between rail ends and 2.07 m across, rotor top
1.073 m above the pontoon underside, pump intakes 0.163 m below it.

---

## Part by part

Ordered by how much a builder would suffer from the gap.

### Pontoons — four parts — CATALOGUE PROP, AND THE DIMENSION IS WRONG

**What it is.** Four white PVC tubes in two touching pairs, one pair per side, carrying the whole
machine. Each pair's tubes sit 0.126 m apart on centres with a drawn diameter of 0.132 m, so they
touch, which is exactly what the photographs show.

**CAD says.** 3.1753 m long, 0.1321 m diameter, with a Behrens-drawn end cap on each. Manifest
origin `55+gallon+drum.skp`.

**Where that came from.** The component is the 3D Warehouse "Plastic 55 Gallon Drum", whose native
size in `defs_prime.tsv` is 0.5842 × 0.5842 × 0.9017 m — a real 55-gallon drum, 23 inches across and
35.5 inches tall. To become a pontoon it was laid on its side and scaled to **22.6 per cent on both
cross-section axes and 352 per cent on its length**. That is a non-uniform stretch of a prop, and the
diameter it produced is whatever the stretch happened to land on.

**Which is why the diameter matches no real pipe.** 0.1321 m is 5.20 inches. The standard outside
diameters near it are 4-inch Schedule 40 at 114.3 mm, 5-inch Schedule 40 at 141.3 mm, 6-inch DWV at
159.4 mm and 6-inch Schedule 40 at 168.3 mm. **Nothing is sold at 132 mm.** A builder cannot buy the
drawn pontoon.

**What the photographs show.** A substantially larger white PVC tube. Measured against a frame member
at comparable depth in `SAM_0212`, the pontoon reads about 2.6 times the frame pipe's diameter,
which puts it near 157 mm — within a few millimetres of 6-inch DWV at 159.4 mm. The inventor's own
typed order note in the drawing reads *"14 6" caps"*, pointing the same way independently. So
**6-inch nominal PVC is well supported**, though it is an inference from two soft sources rather than
a legend read off the pontoon itself.

The end cap is a distinct moulded piece and its form is specific: outside diameter slightly larger
than the pipe so there is a hard step ring at the joint, a flat face with a generously rounded rim,
and a small circular boss at the centre. `SAM_0212` region 150–1200 × 2400–3050 is the clearest.
`SAM_0212` also shows a coupling band partway along a pontoon, meaning at least one pontoon is built
from more than one length of pipe joined.

**Why the diameter error matters more than it looks.** Buoyancy goes with the square of the diameter.
Real 159.4 mm against drawn 132.1 mm is a ratio of 1.207, squared to **1.456**. A pontoon of the
photographed size displaces roughly **forty-six per cent more per metre** than the drawn one. Any
freeboard, payload or stability figure computed from the CAD is wrong by that margin, in the
direction of pessimism. Given that the archive already contains a buoyancy dispute — the inventor's
own annotation asserts *"33# net buoyancy per pontoon"*, which is his figure, not a measurement — no
buoyancy number should be published from either source until someone floats one.

**Buyable?** In kind, yes, and probably as 6-inch PVC. **Not at the drawn diameter, ever.**

### Rotor — one part — SQUASHED, BUT RECOVERABLE FROM THE DRAWING'S OWN COMPONENTS

This is the finding that changes what is possible.

**CAD says**, at the manifest level: a vertical-axis rotor 0.645 m across and 0.397 m tall, spanning
z 0.676 to 1.073, 4,378 triangles, origin `behrens`. Height is 0.62 of the swept diameter, which
renders as a squat paddle wheel and is the reason the machine "does not look quite right" in every
render made from it.

**But the placed part is a scaled instance of components that are not squat.** Reading
`defs_prime.tsv` against `nodes_prime.tsv`:

The wing profile, named `Lenz wing inner#2`, is 0.3542 × 0.2149 × 0.0190 m — a bent plate, two
panels meeting along a fold, which is what a Lenz wing actually is and what the photographs show.
`Component#7` and `Component#8` are that profile extruded to **1.1811 m** tall. `Component#5`, the
complete wing assembly with its end plates, is **1.2192 m** tall — forty-eight inches exactly.
`Component#1`, the hub plate, is 0.3048 × 0.3048 × 0.0190 m — twelve inches square, three-quarters
of an inch thick. `Component#6`, the arm plate, is 0.3735 m across and 0.0063 m thick — a quarter of
an inch. And a component simply named `Shaft` is 0.0318 m in diameter and 1.1827 m long: a
**1.25-inch shaft, 46.5 inches long**, matching the wing height to within two millimetres.

That is a coherent, dimensioned, internally consistent rotor design sitting in the file.

**In the assembly it has been squashed.** The wing instances span z 0.682 to 1.067, a height of 0.385
m against a native 1.1811 m — a vertical scale of **0.326**. Horizontally the wing footprint
diagonal drops from 0.414 m native to about 0.315 m placed, a scale of **0.76**. Non-uniform, and
vertically by a factor of more than two relative to horizontal.

**Un-squashed, the design reads far closer to the photographs.** Restoring both axes gives a rotor of
roughly 0.85 m swept diameter and 1.18 m wing height, a height-to-diameter ratio near **1.39**. The
photographs give 1.05 to 1.18. The placed CAD gives 0.62. The native components are the better
guide by a wide margin.

**One difference survives the un-squashing, and it is real.** The CAD puts all six arms in a single
plane at mid-height — two three-arm plates stacked 8 mm apart, which is just plate thickness. The
photographs show **two spiders separated vertically**, at roughly the upper and lower quarters of the
vane, each arm a thin white rod ending in a short right-angle return that clamps the vane near its
leading edge, with the vanes overhanging both spiders. `SAM_0246` region 1800–2750 × 350–1350 is the
sharpest view; `SAM_0224` shows a second rotor assembly leaning against the container door frame,
detached, with the same two-tier arrangement legible.

Below the vanes the photographs show a small dark bearing or generator can, then a reducer stepping
the shaft down into the masthead collar. None of that is in the CAD.

**Buyable?** No. This is a fabricated assembly and always will be. But the **geometry is
recoverable**, which is a much better position than the manifest suggests, and any 3D work should be
built from the component definitions rather than from the placed instance.

### Frame rails — four parts — THE PROFILE IS WRONG, BUT THE PIPE IS IDENTIFIED

**CAD says.** Four plain bars of **0.053 m square section** — 2.5189 m fore-and-aft at x = ±0.89 and
−0.98, 2.0611 m across the beam aft, 2.0856 m across forward. Forty-eight triangles each: a single
extruded stick with no fittings, no joints and no surface.

**What the photographs show.** Round white PVC pipe, and the frame's whole character is in its
joints. `SAM_0245` region 1700–3200 × 2200–3100 carries the vocabulary in one view: a cross fitting
with belled socket hubs stepping visibly proud of the pipe; a stub end left open and unglued with
the bore and its internal shoulder visible straight down the hole; a galvanised strut whose end has
been flattened and drilled, bolted through the fitting with a hex bolt and washer; a barcode sticker;
maroon printed legend; and white nylon zip ties with the tails left uncut. `SAM_0219` adds the short
vertical risers in tees that carry the frame down onto the pontoons, and `SAM_0202` shows the deck
brace assembly laid out flat before fitting.

**The pipe is identified.** 2-inch PVC Type I Schedule 40, ASTM D 2665, PVC 1120, rated 280 psi at
23 °C — read directly off `SAM_0246`, region 1800–3200 × 2750–3200, mirrored. Outside diameter 60.3
mm.

**A discrepancy worth carrying.** The inventor's own typed annotation in the drawing reads *"2" sch
80 x 28""*, and it sits at z = 0.675, up near the masthead rather than at deck level. The photographed
frame pipe is Schedule 40. Schedule 80 in 2-inch has the same outside diameter but a much thicker
wall, so the two are interchangeable in the fittings and different in weight and cost. The note may
describe the mast rather than the frame. Unresolved.

**What the CAD cannot give a builder.** Every fitting. The drawing has no tee, no cross, no elbow, no
coupling, no cap, no riser and no saddle, so the 2.52 m and 2.06 m figures are spans between
fitting centres, not cut lengths. Socket depth alone moves each cut by an inch or more per end. The
only fitting information anywhere in the archive is the inventor's typed order note — *"10 2"
crosses · 10 2" caps · 14 6" caps"* — which is a shopping list, not a schedule.

**Buyable?** The pipe, yes, with confidence. The fittings, in kind, from the order note. The cut
lengths, no.

### Mast — one part — DRAWN AT ROUGHLY FIVE TIMES ITS PHOTOGRAPHED SIZE

**CAD says.** One member, 0.14 m square section, from z 0.036 to 0.879.

**What the photographs show.** A slim round grey galvanised tube. Against the 2-inch frame pipe in
`SAM_0246` it reads as considerably smaller than the frame pipe, so of order 25 to 35 mm — plausibly
electrical conduit or fence rail. A 140 mm square section is wrong in shape and wrong in size by
something like a factor of five.

The file's own `Shaft` component, 31.8 mm in diameter, is a far better match to what is in the
photographs than the part actually placed as the mast.

**Buyable?** In kind — galvanised round tube. Not in size. Diameter, wall and grade are unknown —
needs a sourcing pass.

### Masthead collar — NOT IN THE DRAWING AT ALL

The CAD has nothing between the mast top at z 0.879 and the rotor bottom at z 0.676, and the stays
stop at 0.615. The photographs show a distinct and prominent component there.

A white cylindrical drum roughly two and a half times the mast diameter and about as tall as it is
wide, with a stepped rim at its top and a recessed dark opening where the upper shaft emerges. **Four
small flat square metal brackets are bolted to its side face, one bolt each**, and all four stays land
on those. `SAM_0220` region 1950–2600 × 900–1350 shows two brackets and the stepped top clearly;
`SAM_0211` and `SAM_0224` show the four-stay convergence from a distance.

It appears to be assembled from PVC fittings, but which fittings is not determinable from these
photographs.

**This is the visual anchor of the entire upper machine and the drawing does not have it.** Any render
built from the CAD ends the mast in nothing.

**Buyable?** Unknown — needs a sourcing pass, and probably a fabrication drawing rather than a
purchase.

### Mast stays — two parts — DRAWN AS A GEOMETRY THAT WAS NOT BUILT

**CAD says.** Two nested sets, each four diagonals plus a square ring. Outer 1.9203 × 1.5925 × 0.4527
m reaching a collar at z 0.615; inner 0.16 m smaller and 0.013 m lower. The inner set is loose faces
at the model root rather than a group, which is the drawing's weakest construction.

**What the photographs show.** **Four** rigid grey galvanised round tubes, uniform diameter, no taper,
no joint along their length, running from the four frame corners up to the collar at roughly 35 to 40
degrees below horizontal, each end flattened and bolted. They are compression struts. There is no
second set, and no square ring appears at stay height in any frame.

What does exist lower down is a set of horizontal galvanised tubes crossing the deck, and the CAD's
second stay set and its rings most plausibly stand in for those.

**Buyable?** In kind. Diameter, wall, grade and every fastener are unknown — needs a sourcing pass.

### Deck cross-members — one part — THE CAD'S DESCRIPTION MISREADS THE HUB

**CAD says.** 136 triangles across 1.635 × 1.645 × 0.127 m at deck level, described in the manifest as
a perimeter diamond, an X-brace, and a round hub disc the mast steps onto.

**What the photographs show**, and `SAM_0202` is decisive because the assembly was photographed flat
on the container floor on 2015-05-15 before it was fitted: grey galvanised round tubes forming an
X-brace, converging on **a white PVC socket fitting** at the centre. Region 1700–2600 × 1400–2400
shows the socket open and facing up, with its internal shoulder visible down the bore, and the
galvanised tubes bolted radially around its outside through flattened, drilled ends. A second white
PVC fitting sits below it. Tube ends elsewhere are left open.

So the "round hub disc the mast steps onto" is in fact **a pipe socket the mast drops into**, with the
braces bolted round its outside. Different part, different fabrication, and a builder told "disc"
would build the wrong thing.

The tubes are the same material and apparent diameter as the mast stays, so in any drawing they
belong to one line family — which the CAD, treating one as a grouped diamond and the other as loose
faces, does not suggest.

**Buyable?** In kind. No sizes.

### Solar panel — one part — CATALOGUE PROP; SIZE UNRECOVERABLE; INTENT NOW KNOWN

`panel-identity-20260811.md` settled the main question the same day and its conclusions hold: the CAD
part is `sun_power305_single_crystalline`, a real catalogue module of native size 1.5593 × 1.0460 ×
0.0460 m, placed at 2.0655 × 0.5192 × 0.0069 m — stretched 1.33× in length, halved in width and
flattened to a seventh in thickness. Non-uniform on all three axes, dragged edge-to-edge across the
bow rail. Its dimensions carry no information. The container machine carries a rigid dark-framed
module and no deck board; the City Island machine carries a flexible laminate and a plate.

**Two things to add.**

**First, the inventor stated his intent in the drawing, and nobody had read it.**
`cad/out/annotations_prime.tsv` carries a text annotation at (1.0071, 1.0215, 0.1614) — which is the
corner of the solar panel instance — reading:

> flexible 100watt PV panel

That is his assertion, not a measurement, and it is not restated as fact anywhere. But it does
resolve what the block was standing in for. The 2024 drawing intends a flexible 100 W laminate. The
SunPower rigid module is a placeholder for it, and the 2015 machine in the photographs carries
neither — it carries a small rigid framed module. Three different articles across the record. The
`panel-identity` pass listed "annotations in the .skp scenes" as the highest-value thing that would
raise its confidence; this is that thing, and it points at the drawing's intent rather than at the
photographed panel's size.

**Second, an approximate size for the photographed panel is now available**, using the 2-inch pipe as
the stick. In `SAM_0225` the panel lies flat across two frame tubes at essentially the same depth as
its supports. Its long edge measures between 6.9 and 7.7 times the frame pipe's outside diameter,
depending on which support is used as the reference, giving **roughly 0.42 to 0.47 m**. Call it
**about 0.4 m on the long edge, certainly under 0.6 m**, ±25 per cent. The short edge is heavily
foreshortened and is not recoverable this way. For orientation only: a panel of that footprint is in
the size class sold as a small trickle or marine panel, an order of magnitude smaller in area than a
305 W module. **No wattage is asserted** — there is no nameplate in any frame.

**Buyable?** No. Not from the drawing, not from the photographs.

### Solar panel mounting — NOT IN THE DRAWING AT ALL

The panel does not simply lie on the frame. `SAM_0225`, region 850–2350 × 1900–2900, shows a
dedicated outboard shelf built for it: a large white PVC 90-degree elbow turning outboard off the
deck frame, a run outboard of the pontoon, and two short open stub ends standing up to carry the
panel, with the panel held down by a single white zip tie over a tube at its near-right corner. A
coiled black lead sits on the far edge.

**None of that structure exists in the CAD**, which simply floats a slab at deck height. It is several
fittings and two pipe cuts, and it is load-bearing and cantilevered.

### Bilge pumps, the fitted pair — one part — CATALOGUE PROP, POSITION GOOD, SPEC ABSENT

**CAD says.** One part holding both cartridges, spanning x −1.10 to +1.04 at y ≈ −0.64, reaching down
to z −0.163, so one pump under each outer pontoon toward the aft end. Origin `Bilge Pump
Cartridge2.skp`; the component is named `Mayfair Bilge Pump Cartridge`, native size 0.0795 × 0.0632 ×
0.0999 m — a plausible real cartridge size, unlike most of the props in this file.

**Positions agree with the photographs.** This is the one catalogue part whose placement is not in
dispute.

**What the photographs show**, `SAM_0220` region 300–900 × 2400–3100 being clearest: a dark red
strainer skirt at the bottom, a cylindrical cage of fine vertical comb ribs with a smooth band above
them, snapping onto a white cylindrical body; a horizontal parting seam and a small rectangular latch
tab on the body; a barcode label; and above it a stepped hose barb feeding up into a white PVC
reducer and then into the frame. `SAM_0212` shows a third pump standing loose on the container floor
on its own PVC riser, not yet fitted.

**Buyable?** In kind, easily — this is the standard cartridge-in-base submersible bilge pump sold by
several marine brands. **Flow rate, voltage draw and thread size are all unknown — needs a sourcing
pass.** The component's name points at a real brand family, but the drawing's use of a catalogue model
is not evidence that the photographed pump is that brand, and no label is legible.

### Bilge pump, the third one at the deck centre — one part — CONFIRMED STRAY IMPORT, DROP IT

`cad-photo-gap-20260807.md` recommended dropping this on the reasonable grounds that no photograph
shows a pump at the deck centre and that it intersects the mast. **The node table now confirms it
outright.**

Its instance bounding box in `nodes_prime.tsv` is −0.040 to +0.040, −0.033 to +0.030, 0.000 to 0.100.
Its component's native size in `defs_prime.tsv` is 0.0795 × 0.0632 × 0.0999. **The instance is the
native size to within a tenth of a millimetre, unrotated, centred on the world origin.** That is
precisely and only what an unplaced import looks like — dropped in at 1:1 at (0,0,0) and never moved.

**Drop it.** No judgement call remains.

### Capacitor — one part — CATALOGUE PROP, BUT THE REAL ARTICLE IS NOW FULLY IDENTIFIED

**CAD says.** 0.064 × 0.2031 × 0.064 m at (−0.77, +0.56, 0.19), inboard of the port rail just above
deck level. Origin `Elec_capacitor.skp`, native size 0.4 × 0.4 × 1.2692 m — a 400 mm diameter,
1.27 m tall industrial power capacitor, scaled uniformly to 0.16× to fit the deck. Uniform scaling,
at least, but a wrong-category object.

**What the photographs show**, and `SAM_0248` and `SAM_0249` are close enough to read the label:

A chrome mirror-finish cylinder with a tribal-flame graphic and a yellow-gold script mark, held in
**clear acrylic saddle brackets** and zip-tied **on top of an outer longitudinal rail** — not inboard on
the deck as drawn. Its top face carries two chrome terminal posts with hex nuts, a red battery-clamp
lead and a black lead, and **a three-digit red LED numeric display**. Around the base, legible in
`SAM_0249` region 1238–2188 × 2822–4089, the body is printed:

> 2 FARAD POWER CAP · Designed in Florida

**This is a 12-volt car-audio power capacitor** — the "stiffening cap" sold to smooth current draw on
large amplifiers. The yellow script brand mark is not resolvable to a name at this resolution and no
brand is asserted here. It is, straightforwardly, **the most identifiable single component on the
machine** and the easiest thing on this list for a builder to buy.

**Diameter reads larger than the drawn 64 mm** — nearer 100 mm against the 2-inch pipe it is strapped
to — though the mounting angle makes that soft.

**One consequence worth stating plainly, because it guards a claim.** A 2 farad capacitor at 12 volts
stores ½CV², which is 144 joules — about 0.04 watt-hours, and the usable fraction between 12 V and
10 V is a third of that. **It is not energy storage in any operational sense**, and no photograph of
this machine shows a battery. Whatever the deck electronics do, they are not being run off this. Any
copy describing the capacitor as the machine's power store would be wrong on arithmetic alone.

**Buyable?** Yes, and cheaply. Nothing else on this machine is this easy.

### Deck pump — one part — CATALOGUE PROP OF THE WRONG CATEGORY

**CAD says.** 0.0716 × 0.1399 × 0.0779 m on the deck at (−0.78, +0.22, 0.19). Origin `Pumpe.skp`,
whose native size is **4.3399 × 8.4804 × 4.7204 m** — a large industrial machine, almost certainly an
import in the wrong units. It has been scaled **uniformly by 0.0165**, roughly one sixtieth, so the
drawing carries a proportionally faithful rendering of an industrial centrifugal pump, complete with
cooling fins, bolted end bell and mesh fan guard, at the size of a fist.

**What the photographs show** is a different class of object entirely. `SAM_0246` region 1200–2000 ×
2600–3100 is sharp: a **black moulded diaphragm pump head**, square in profile, with screws around its
face and two barbed ports; a **red round pressure-adjustment cap** on the side; a **green printed band**
at the head-to-motor joint; then a plain silvery-white motor can with a small label window; red and
black leads; and a black plastic mounting foot. It is zip-tied to a frame rail. No fins, no fan
guard, no end bell.

This is the common 12-volt diaphragm demand pump of the RV, marine and agricultural-sprayer world.

**Buyable?** In kind, easily. **Flow, pressure and duty are unknown — needs a sourcing pass**, and this
matters more than for most parts, because the whole cavitation-nozzle question turns on what pressure
and flow the machine could actually deliver. The CAD contributes nothing: it depicts a machine-shop
object where the real one is a hardware-store object.

### Electronics enclosure — NOT IN THE DRAWING AT ALL

The largest object on the deck after the panel, present in every assembled frame, and the CAD has
nothing for it.

`SAM_0220` region 1950–2800 × 1700–2100 shows it plainly: a **clear polycarbonate compartmented case**,
roughly a hand-span across and a few fingers deep, its lid divided into a grid of about a dozen
rectangular lidded compartments — the form sold as a tackle or craft organiser. Electronics and
coloured wiring are visible inside. **It sits directly on the grey galvanised deck cross-tubes**, held
by small metal straps. There is no white plate under it on this machine.

The inventor's yellow annotation on `SAM_0220` labels this box ARTIFICIAL INTELLIGENCE. That
annotation exists and is recorded here as existing; nothing about its contents is established by any
document or photograph in the archive.

**Buyable?** In kind — it is a stock plastic organiser box. Which one is unknown, and it is not
weatherproof.

### Squat deck cylinder — one part — UNIDENTIFIED, AND ONE INFERENCE ABOUT IT IS WEAK

**CAD says.** An open-topped twelve-sided cylinder 0.4153 m across and 0.0933 m deep on the frame at
the aft starboard corner. Ninety-two triangles. Origin `behrens`, so this is his own geometry rather
than a prop.

**What the photographs show.** Nothing that matches. `SAM_0246` shows a small white open-topped socket
near the mast base of roughly one pipe diameter — an order too small — and a white barrel standing on
the container floor behind the machine, which is not attached to anything.

**A caution on a prior inference.** `machine-record-audit-20260806.md` reads this part as "a coalescer
or filter element" on the basis of a hexagonal honeycomb texture and a `[Tile_Hexagon_White]` material
name in the file. That is a **material assignment, not geometry**, and a stock hexagon-tile texture is
exactly what an unassigned surface picks up. The inference should be held loosely; nothing in the
geometry, the photographs or the annotations supports a filter reading.

**Buyable?** No. Unidentified. Recommend drawing it as a plain open pan or omitting it, and inventing
no detail either way.

### Scale figure — not a machine part

A flat 1.785 m two-dimensional cut-out standing 2.2 m off to port, from `2D_Man_Walking_Dusty.skp`,
exported separately and never in the machine mesh. It must never be lit or shaded as a solid.

---

## Everything visible in the photographs that the drawing does not contain

Gathered, in order of how much a builder would miss them.

**The pipe fittings — the whole joinery of the machine.** Belled-socket tees and four-way crosses,
90-degree elbows, couplings, caps, short vertical risers, and open unglued stub ends left proud by
roughly a hand's width with the bore and internal shoulder visible. The CAD is four extruded sticks
and a diamond; the built frame is perhaps thirty fittings. The inventor's order note gives counts for
three of them and nothing else.

**The masthead collar and its four bolted brackets.** Described above. The CAD ends the mast in
nothing.

**The rotor's lower gear.** A small dark bearing or generator can beneath the vanes, then a white tube
stepping down through a reducer into the collar, with a small flange and bearing plate between.

**The electronics enclosure.** Described above.

**The panel's outboard mounting shelf.** Described above.

**The wiring harness.** Red and black cable runs zip-tied along every rail, looping between panel,
box, capacitor and pumps, with tails left hanging, plus a copper braided lead near the capacitor
visible in `SAM_0248` and `SAM_0249`. Not a part, but leaving it out is what makes a render look like
a render.

**The fastening and marking vocabulary.** White nylon zip ties everywhere with the tails uncut;
barcode and inventory stickers on pipe and pumps; the maroon printed specification legend running
lengthwise on every frame member; galvanised struts bolted through flattened, drilled ends into
saddles on the pipe.

**A large white PVC cone or reducer** at the forward port area, joining a large pipe to a smaller one.
What it does is not determinable from these photographs and is not asserted here. `SAM_0220`,
`SAM_0246`.

**And one thing that is NOT part of this machine, despite appearances.** A thick white board with a
rebated edge lies on the container floor in `SAM_0220`, `SAM_0221`, `SAM_0224` and `SAM_0225`. It is
board stock in the workshop. It is never fitted to the raft in any of the fifteen frames, and the
deck plate that does exist on the City Island machine is a different machine's part.

---

## Everything the drawing contains that the photographs do not

The third bilge pump at the deck centre — confirmed stray import, drop it.

The squat deck cylinder — unidentified; may belong to a build that was never photographed.

The second, inner set of mast stays and both stay rings — no ring appears at stay height in any
frame; these most plausibly stand in for the deck-level galvanised cross tubes, which are drawn
separately anyway.

The full-beam solar slab — a stretched catalogue module, standing in for what the inventor's own
annotation calls a flexible 100 W panel, on a machine that carries a small rigid framed module.

---

## The build sequence, recovered from the photograph dates

There is no assembly document in the archive — the inventor's entire shipped instruction set is one
page telling the reader to install SketchUp and measure the drawing. The photograph sequence is a
partial substitute, and it has not been used as one before. Corrected dates:

**28 April 2015** — two pontoon tubes on roller stands in an otherwise empty container. Nothing else
built. `SAM_0196`.

**15 May 2015** — the deck brace assembly laid out flat on the container floor: PVC perimeter,
galvanised X-brace, central socket hub. Assembled as a sub-assembly before anything was joined to it.
`SAM_0202`.

**25 May 2015** — frame, pontoons, mast, stays and collar standing on trestles. Structure complete;
no deck equipment. `SAM_0203`.

**4 June 2015** — same, further along, deck cross tubes fitted. `SAM_0211`, `SAM_0212`.

**11 June 2015** — capacitor and electronics box fitted. The panel is off the machine, standing on the
container floor. `SAM_0219`.

**22 June 2015** — panel fitted, rotor on, machine complete. This is the session at which the inventor
added his yellow annotations. `SAM_0220`, `SAM_0221`, `SAM_0224`, `SAM_0225`.

**8 July 2015** — final close-up detail photographs of the capacitor, the pumps and the deck.
`SAM_0245` through `SAM_0249`.

**Structure first, deck equipment last, and the pontoon tubes were prepared before anything else.**
That ordering is itself useful to publish, and it is directly evidenced rather than reconstructed.

---

## The buy list, honestly graded

**Buy with confidence, sourced from the record itself:**

2-inch PVC Type I Schedule 40 pipe, ASTM D 2665 / PVC 1120 — read off the pipe in `SAM_0246`.

2-inch PVC four-way crosses, ten off, and 2-inch PVC caps, ten off — from the inventor's typed order
note in the drawing.

6-inch PVC caps, fourteen off — same note.

A 2 farad 12 V car-audio power capacitor with digital voltage display — label read directly in
`SAM_0249`.

White nylon cable ties, in quantity — visible in every frame.

**Buy in kind, rating unknown, needs a sourcing pass:**

6-inch PVC pipe for the pontoons — supported by the cap count and by a measured diameter ratio of
about 2.6 against the frame pipe, not read off the pontoon itself.

Two 12 V submersible cartridge bilge pumps — form confirmed, flow rate and fittings unknown.

One 12 V diaphragm demand pump — form confirmed, flow and pressure unknown, and this is the one whose
rating most affects everything downstream.

Galvanised round tube for four mast stays and the deck cross braces — diameter, wall and grade
unknown.

Galvanised round tube for the mast — same, and the drawing is no help at all here.

Bolts, washers and saddles throughout — no fastener is specified anywhere in the archive.

A clear compartmented plastic organiser box for the electronics — form confirmed, and it is not
weatherproof.

**Cannot be bought; must be fabricated or redesigned:**

The rotor, in full — but its geometry is recoverable from the component definitions.

The masthead collar and its four brackets.

The solar panel — size unrecoverable; the drawing's intent and the photographed article disagree.

The panel's outboard mounting shelf — several fittings and two cuts, none dimensioned.

The squat deck cylinder — unidentified; recommend omitting.

Every cut length in the frame — the drawing gives spans between fitting centres, and socket depths
are unknown.

---

## What would close the biggest gaps, in order of value

**A tape measure in one photograph.** Any single frame with a rule or a person in contact with the
machine collapses most of the ±20 per cent uncertainty at once. Failing that, a higher-resolution
scan of any frame where the pontoon's own printed legend is legible would settle the pontoon
diameter directly rather than by ratio.

**The back of the solar panel.** `SAM_0219` shows it leaning off the machine, so the reverse face was
photographable at that session. A model number settles size and rating together.

**Nameplates on either pump.** Both are photographed at close range; neither label resolves. A
sharper original, if one exists, would settle both.

**The fitting schedule.** The order note gives three counts. A complete fitting list and a set of cut
lengths would turn this from a photograph album into a build package, and it is the single largest
piece of missing work.

**Whether the 2024 drawing dimensions the 2015 machine.** Nothing establishes this. If it does not,
every CAD dimension in this document describes a design that was never built, and the photographs
become the only record of the machine that was.

---

## Sources

CAD extraction: `cad/out/prime/parts_manifest.tsv`, `cad/out/defs_prime.tsv`,
`cad/out/nodes_prime.tsv`, `cad/out/annotations_prime.tsv`, `cad/out/prime/part-renders/`.

Photographs, all viewed directly at full resolution:
`Personal/Seasteading/_ARCHIVED/04_Prototype-Testing/2023-Marina-Tests/SAM_0196`, `_0202`, `_0203`,
`_0211`, `_0212`, `_0219`, `_0220`, `_0221`, `_0224`, `_0225`, `_0245`, `_0246`, `_0247`, `_0248`,
`_0249`. Comparison frame, a different machine: `~/Downloads/Model-JTfree1NEW/LiftingInstructions.JPG`.

Prior work built on and, in two places, corrected: `machine-record-audit-20260806.md`,
`cad-photo-gap-20260807.md`, `panel-identity-20260811.md`, `CLAUDE.md`.

Annotations present on the source photographs, recorded so their existence is on file and repeated as
fact nowhere: `SAM_0220` carries yellow captions labelling a vertical wind turbine, a solar panel, a
capacitor, a pump, a thruster, a high-pressure nozzle pack and an artificial-intelligence component.
The drawing carries typed annotations naming EVIE-2c, a flexible 100 W PV panel, a net buoyancy
figure per pontoon, a pipe-clamp instruction, an order list and a note about adding analog A.I. in a
second phase. All are the inventor's own assertions.
