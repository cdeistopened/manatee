# What the record actually says about this machine

_2026-08-06. An audit of every model, photograph, drawing, BOM and video in the archive, run
because the project lead asked to get into the SketchUp files and talk through assembly. Agent-facing
reference. Each claim carries its source; anything inferred is marked as inferred._

---

## The finding that reorganises everything

**The archive does not describe one machine. It describes five, and the 2026 manuals blend them
into a single voice without saying so.**

1. **The 2015/2023 marina raft** — white PVC pipe frame and pontoons, galvanised braced mast,
   small vertical-axis turbine, one bilge pump, an acrylic electronics box. No process train at
   all. `_ARCHIVED/04_Prototype-Testing/2023-Marina-Tests/SAM_0220.JPG`, `SAM_0246.JPG`.
2. **The 2016 pond machine that actually produced paraffin** — annotated by Rudy as *15 watt
   windmill · 15 watt solar panel · 1/10th HP pump*, with a red-lidded bucket and a clear jar as
   the whole separation stage. Riding awash. `~/Downloads/Model-JTfree1NEW/DX5b+notes1.jpg`.
3. **The JT-1 and VBShdl greenhouse cultivation vessels** — a different machine entirely:
   4×4-inch structural HDPE lumber, Northern Greenhouse laminated film, 14-inch × 20-**foot**
   pontoons, trolling motors. `JT1BOM.xls`, `VBShdl1BOM.xls`.
4. **The 2024 SketchUp EVIE-2c** — 6-inch PVC pontoons, a 2-inch schedule-80 PVC frame on 28-inch
   members and 4-way crosses, a Lenz-type vertical-axis rotor, one flexible 100 W panel lying flat
   on the deck, two bilge-pump cartridges slung underneath.
   `~/Downloads/Model-JTfree1NEW/VBShdl-1m5manatee2b1PRIME.skp`.
5. **The 2025 Sarasota machine** — four tubes in two side-by-side pairs banded with worm-drive
   clamps, flat DWV caps, a two-stage mast on a bolted floor flange.
   `~/Downloads/Model-JTfree1NEW/LiftingInstructions.JPG`, City Island, Sarasota.

The "6 vs 14 vs 24 inch pontoon" contradiction that has been treated as a documentation error is
mostly not one. Six inches is the raft. Fourteen inches by twenty feet is the greenhouse vessel's
BOM, read as though it were the raft's. Twenty-four is the polished docs.

---

## The 55-gallon drum has never been built

No photograph anywhere in the corpus shows a 55-gallon drum mounted on a raft. Neither SketchUp
saved view shows one either, and the model's own drum component is an upright blue drum that does
not match the squat cylinder actually sitting at deck centre.

This matters because the drum-as-reactor-and-settler is the organising idea of both 2026 manuals,
of the current homepage ("one drum, three jobs"), and of the kit manifest, which uses the drum as
the shipping crate. It is a 2026 design decision presented as a reading of the record.

Rudy's own process document specifies something else again: four vessels plus a bladder, in
sequence, with the concentration step **on shore in a greenhouse**, not on the raft.
`~/Downloads/Model-JTfree1NEW/9x9HVO process.pdf`.

The buoyancy warning in the manuals is therefore not a spec conflict. It is the gap between what
was built — no reactor, roughly 150–250 lb of payload — and what is documented: a raft carrying a
460 lb full drum that nobody has ever floated. Rudy's own model annotation reads
*"33# net buoyancy per pontoon"*, i.e. 66 lb of reserve.

---

## The machine that worked was thirty times smaller

The only machine with any evidence of producing product ran on about 30 watts of generation and a
1/10 HP pump. The manuals size the energy budget around an AR RMW2G24D at 300 psi and 10 gpm.

Its feedstock was **duckweed**, not microalgae. Duckweed self-concentrates into a floating mat,
which dissolves the problem WORKBENCH flags as "the likely real hidden invention" — you cannot skim
wax off water at 0.1% solids. `BioMass#.jpg`: *"When this pond is completely covered with duckweed,
as it is most of the summer…"* `ref/DX-5dwPOND.jpg` caption: *"The processor moves around the pond,
collecting duckweed & algae…"*

`ref/DX-5dwPOND.jpg` also carries a dimensioned overall size that appears nowhere in the manuals:
roughly 6 ft 7-5/16 in × 11 ft 3-11/16 in, rotor 10-5/16 in, drawn against a human figure on a
15 ft 2-3/16 in pond.

---

## Firewall exposure sitting in the reference folder

Two files being actively mined for illustration references carry explicit yield claims in Rudy's
own handwriting:

- `DX5b+notes1.jpg` — *"The robot was producing over 1 cup per hour, or 1.33 gallons per day."*
- `BioMass#.jpg` — a duckweed pond holding *"750 gallons of synfuel"* that would *"replace itself
  within 24 hours."*

These are uninstrumented assertions written on photographs of surface scum, and they are almost
these are the project's liability, not Rudy's. Use the geometry; quarantine the captions.

---

## The turbine question is settled: vertical-axis

Four independent records agree, and the one that disagrees is traceable to a spec line rather than
to any model or photograph.

- The SketchUp file contains a component definition named `Lenz wing inner#2`. A Lenz2 is a
  straight-bladed vertical-axis rotor.
- Rudy's own annotated build photo `SAM_0220.JPG` carries a yellow arrow reading
  **VERTICAL WIND TURBINE** pointing at the masthead.
- The pond video shows the same three straight vertical blades.
- `ref/DX-5dwPOND.jpg` shows the identical white-panel vertical rotor.
- `assets-new/wec/evie-ink-c.jpg` — the study the project lead picked — draws it vertical-axis.

**The outliers to retire as geometry references:** `manatee-site/img/manatee-hero.png` and
`manatee-site/img/isomodel.png` show a five-blade horizontal-axis propeller with a tail vane, which
appears in no model and no photograph. `evie-ink-a.jpg` and `evie-ink-b.jpg` are redraws of that
wrong hero and inherit the error. The likely origin is `AS-BUILT-manual.md` line 97 —
*"Wind turbine (optional) | Air-X Marine 400 W 12 V"* — an Air-X being a horizontal-axis marine
turbine. The illustrator drew the bill of materials instead of the machine.

The drawing currently on the design mockup, `design-system/mockups/assets/raft-ink.jpg`, is a later
regeneration and gets the turbine right.

---

## Where the visual records still disagree

- **The drum.** Every line drawing shows a 55-gallon drum lying horizontally in a cradle at deck
  centre. The model shows no drum in its saved view; its drum component is upright. No built
  machine has one.
- **Solar.** Drawings show two large gridded panels cantilevered outboard. The model has one flat
  panel on the deck. The build has one small rigid panel.
- **Mast bracing.** The model and the physical build both use four rigid struts to the frame
  corners — galvanised steel in the build. Every line drawing shows only thin guy cables.
- **Thrusters.** The model hangs two bilge-pump cartridges. The drawings show one.
- **The squat deck-centre cylinder** in the model is unidentified — roughly 3:1 diameter to height,
  with a hexagonal honeycomb texture and a `[Tile_Hexagon_White]` material in the file. Reads as a
  coalescer or filter element. This is the single most valuable thing for geometry extraction to
  resolve.

---

## Real build data recovered from the model's own text annotations

Harder evidence than any drawing, because Rudy typed these into the file himself:

*2" sch 80 x 28"* · *10 2" crosses* · *10 2" caps* · *14 6" caps* · *1-1/2 schedule 40 PVC 90* ·
*3-in x 1.25-in ball valve* · *33# net buoyancy per pontoon* · *"Rigidly attach pipe clamps to
frame. Secure them around pontoon next to shoulders formed by end caps & couplings."* ·
*"Add analog A.I. in phase 2"*

Scene names: `FACTORY ASSEMBLE` · `5X5 CORE, MINUS PONTOONS,` · `SOLAR AND WECS`.

Note *14 6" caps* — more caps than a two-pontoon catamaran needs, which is consistent with the
2025 machine's four tubes.

Both files are SketchUp 2024 (24.0.553), author "Rudy B.", units inches. The `+BimodalTurbine`
variant differs from PRIME by exactly one component: `Windtube`, a horizontal split-pipe drag rotor
— a Savonius laid on its side. PRIME is the base design; the Windtube is the variant.

---

## There is no assembly document

Rudy's entire shipped instruction set is one page telling the reader to install SketchUp and
measure the drawing. `~/Downloads/Model-JTfree1NEW/Study Plans Instructions.pdf`.

What exists instead: `ref/photoschematicAssembly1b.jpg` is a **wiring** photo-schematic —
photographs of each real component connected by hand-drawn red and black lines. It is not a
mechanical assembly document, but it is a format worth stealing, because every part in it is a
photograph of the actual part and nothing is inferred.

`LiftingInstructions.JPG` carries one of only two instructions Rudy ever annotated onto a
photograph: **lift from the bottom at the corners only** — never from the cables, the mast or the
panel. Reproduce it verbatim wherever assembly is published.

`AS-BUILT-manual.md` presents itself as reproducing "what was actually built, warts and all." It
does not. It blends the raft's build notes, two greenhouse vessels' BOMs, a misread capacitor label
and a quantity of good original rigging engineering into one voice, marking invented parts
`[MEASURE]` as though they were merely unmeasured rather than unsourced. Anyone publishing assembly
from it inherits that conflation. Cheap fix: mark every step **photographed**, **documented**, or
**reconstructed**.

---

## The nozzle drawings are not manufacturable

`ref/KineticNozzle1.JPG` and `ref/KineticNozzle1BBB.JPG`:

- The front view shows roughly eight **overlapping** circles of at least three diameters.
  Overlapping bores merge into an irregular slot, so this is not a drillable hole pattern.
- No bore diameter, no depth, no through-or-blind indication.
- **No mounting interface anywhere** — no thread, no port, no flange, no inlet. A builder cannot
  attach it to a hose and a shop cannot quote it.
- Title blocks read "306 S.S.", which is not a real stainless grade.
- The two drawings differ in scale by a factor of 11.106. At the small scale the hole spacings
  imply bores finer than the 100–150 mesh filter the improved manual specifies — self-clogging by
  construction, and a misting-pump machine. At the large scale it is a pressure-washer machine.
  These need different pumps, different filters and different power budgets.

The real hardware exists in photograph and bears no resemblance to the drawings: two stainless
pressure chambers with domed ends, swaged compression fittings and hard-plumbed bent tube runs.
`_ARCHIVED/06_Media/Photos/BEAR cavitation nozzle close up.jpg`. The drawings appear to cover only
the orifice insert; the housing that makes it plumbable has never been drawn.

---

## A licensing exposure in the model itself

The SketchUp file carries downloaded 3D Warehouse assets used as scale reference: a Caterpillar
frame, truck seats, mud flaps, a dinghy, a walking figure. Source paths embedded in the file
confirm the provenance.

A naive export drags all of them into any published package. The plans ship under CERN-OHL-S,
CC BY-SA and MIT; 3D Warehouse models carry their own terms that generally do not permit
redistribution. Triage by **keep-list, not delete-list**, before anything is published — including
before any raw push to GitHub.

Genuine machine components present in the file: 55-gallon drum, Mayfair bilge pump cartridge, 12 V
deep-cycle marine battery, vertical immersion sump pump, 15-gallon water barrel, bladder tank,
electrolytic capacitor, PVC elbow, tee and cap.

---

## Safety items that must survive into anything published

- **High-pressure water at the nozzle feed.** No relief valve exists in the as-built, and the
  nozzle has no drawn mounting interface, so whatever fitting a builder improvises is the weakest
  point in a 250–400 psi circuit.
- **Cyanotoxin aerosol.** Absent from every document in the corpus, including both 2026 manuals. A
  cavitating jet lysing a cyanobacterial bloom releases and aerosolises intracellular microcystins,
  and running in bloom water is the machine's whole purpose. Lysed cells put toxin into solution
  rather than removing it.
- **Mast under tension** — applies only to the cable-rigged route, which is the one with no
  photographic evidence of ever being built.
- **Lifting a full drum** — about 460 lb. Rudy's own instruction, verbatim, at the point of use.
- **Capsize.** The 2016 pond photograph shows the working machine riding awash with a mast-top
  turbine. There is no stability analysis anywhere in the corpus. A dockside inclining test is the
  cheapest de-risk in the build.
- **Electrical fire.** No fusing anywhere in the as-built rig; the electronics sit in an open food
  tub. Blue Sea 5175 at 30 A — not 5177, which is 50 A. Turnbuckles jaw-and-jaw 316, not
  hook-and-eye.

---

## Sources

Workflow run `wf_67bb7353-a3b`, four parallel agents over the SketchUp extracts, the Seasteading
archive, `~/Downloads/Model-JTfree1NEW/`, the scroll-world repository and the current web
landscape. Per-agent transcripts and full evidence in that run's journal.


---

# Can the Manatee ship real build plans? Verdict, 2026-08-11

## The answer

No — not today, and not for the machine anyone would want to build. A followable build package is achievable for the 2015 container machine (the four-pontoon raft assembled at the shipping container) at roughly eight to twelve working days of writing, but every one of those days is blocked behind a single thing nobody has done in eleven years: putting a tape measure on the hardware. The reactor — the cavitation nozzle the whole project is named for — cannot be specified from what exists, at any effort level, and that is the finding that decides what this project is.

Confidence: high on all three. Nine independent investigations reached the same conclusion this week, and three separate simulated builders each stopped at step one.

## What I would do

Stop producing documents. Spend one day on two actions instead: half a day with a tape measure against a surviving machine, and one hour on the phone with Rudy Behrens with a prepared list of questions. Publish nothing until both are done. Then write the container machine up as what the evidence actually supports — a solar-and-wind instrument raft with a builder-run float test in place of every performance number — and carry the pond machine alongside it purely as proof that a machine of this family floated and turned. Treat the reactor as a separate, clean-sheet engineering project funded and scheduled on its own, never as part of a build package.

The reason is sequencing, not caution. The measurement and the phone call take one day between them and they unblock roughly eight of the twelve remaining days. Every document written before them produces numbers that will be thrown away. The archive now runs to something on the order of half a million words about a machine on which no dimension has ever been measured; that ratio is the problem, and one more report does not improve it.

## The core cannot be specified

The part that makes the Manatee interesting does not exist in buildable form anywhere, and it never has.

The whole original record of the cavitation nozzle — the component supposed to break algae cells open — is one freehand sketch drawn in 2008, published at three different sizes that disagree with each other by eleven to one. It carries no length, no cross-section, no hole depth, no hole shape, no inlet or outlet identification, no thread or port so it could be plumbed into anything, no tolerance, and a material callout for a stainless grade that does not exist. Holes meant to be identical are drawn eleven to fourteen per cent apart, and a pattern that should sit at even 120-degree spacing measures 108, 125 and 127 degrees. The 2012 "production" file is not a second design either — it is that same drawing squashed unevenly, so its holes are ovals and a shop following it literally would cut an oval part.

Worse, the size the project leads with is physically impossible on its own equipment. To reach the water speed the inventor himself states, that nozzle needs about 80 gallons per minute; the largest pump named in any parts list in the archive delivers 10.


Neither machine that was actually built has a processing core on it. Fifteen photographs of the container machine and the CAD model show a raft carrying two submersible bilge pumps, one small 12-volt diaphragm pump with both of its hose ports bare — no hose, no fitting, no clamp on either — a car-audio capacitor storing about a twentieth of a watt-hour, and a household plastic parts-organiser box. No tank, no nozzle, no separator, no filter, no valve, no gauge, no instrument. The inventor's own red arrows label the two bilge pumps as thrusters and label the plastic organiser box with the words "artificial intelligence." The pond machine is the same: a pump, a hose, a jar and a lidded tub.


Confidence: high. This was checked directly against original-resolution photographs and the raw drawing files, not taken from prior summaries.

## What is genuinely established

The good work here is real, and it is a short list.

One certified dimension now exists. The frame pipe prints its own specification along its length and it is legible in one photograph: 2-inch PVC, Type I, Schedule 40, with a pressure rating that independently corroborates the reading. That is a standard 60.3 mm outside diameter physically touching the machine — the first object of known size in the entire record, and it overturns an earlier conclusion that nothing of known size ever touched it.

The dating is fixed. The container machine was built April to July 2015, not 2023; the camera's clock ran 35 years fast and a duplicate file dated by the filesystem settles it. The folder name is wrong and should be corrected wherever it is cited.

A build chronology exists — seven photographic sessions across three months, structure first and deck equipment last. That is rare in hobbyist open hardware, though fifteen frames is a chronology and not a step-by-step sequence.

One document is publishable nearly as it stands: the electronics guide, which is a general marine 12-volt practice manual wearing a Manatee cover — fusing, grounding, enclosure and corrosion practice that applies to any small machine on any water.

And the honesty apparatus is unusual and correct in intent. Most projects in this space would have shipped the fuel numbers.

## What is genuinely missing

For the container machine: the size of the pontoons, cut lengths for every frame member, a list of the pipe fittings that join them, the construction of the collar at the masthead that carries the entire wind rotor load, the identity of whatever generator sits inside that collar, every single bolt on the machine, the solar panel's size and rating, both pumps' flow ratings, and any test at all that would tell a builder whether the finished machine works.

The pontoon gap is the expensive one. The CAD's diameter is an artefact — a downloaded 55-gallon drum model squashed and stretched, and no manufacturer sells pipe at that size. Three separate attempts to read the real size off photographs returned 120 mm, 157 mm and 177 mm. Across that spread the four tubes carry somewhere between roughly 50 and 150 pounds of usable payload, against equipment weighing on the order of 100 pounds. At the top of the range the raft works with margin; at the bottom it will not float its own gear. Confidence in the 6-inch hypothesis: moderate, and moderate is not good enough to publish.

The CAD cannot fill any of these gaps, and the reason matters. It draws the frame as a square section matching the pipe's inside diameter rather than a round pipe at its outside diameter. It contains not one tee, cross, elbow, coupling, cap or riser, so nothing accounts for how deep a pipe seats into a fitting — which moves every cut by more than an inch per end. It is not symmetric about its own centreline: one pontoon pair sits 80 mm further out than the other, the two cross rails differ by 24 mm, and within each pair the tubes overlap by 6 mm. It defines a rotor shaft and never places it. It is a massing sketch made after the fact and cannot be dimensioned off at any point.

The pond machine has no absolute dimension at all and no route to one: both photographic scale methods were tried quantitatively this week and both are degenerate, meaning a one-pixel reading error swings the answer by more than the answer is worth. But its shape is fully legible, so one answer to "what pipe did you use" converts a dozen already-measured proportions into real dimensions in an afternoon.

Confidence on the missing list: high. Confidence that measurement closes most of it: moderate to high, conditional on hardware surviving.

## Publishing a document versus somebody building it

About one third of published open-source hardware carries enough documentation for an outsider to replicate it, per a study of 76 products across agriculture, machine tools, transport and energy. The default outcome for a package shipping a CAD model, a photo gallery and good prose is that nobody builds it — which is exactly the shape of what exists here. The packages that do get built share one high-leverage artifact, and it is not the drawings: a jig, mould or template that takes precision out of the builder's hands, paired with a parts list naming where each item is bought and for how much. The water filter design with over two million builds ships a steel mould; the small wind turbine design with build counts in the thousands ships four jigs and a plain statement of which dimensions are critical and which are merely nominal. The Manatee has neither.

The existing manuals cannot be edited into service, and the reason is not the drum contamination everyone has been chasing. They document a machine that was never built: a two-pontoon catamaran with cable rigging and a 55-gallon reactor drum, appearing in no photograph anywhere. The file named as an as-built record is not one — that term means measured off the finished article, and any builder discovers it is not by counting pontoons in the folder next door. Four in every photograph, two in the manual. That single word will cost more credibility than any yield claim, because a builder who catches one false completeness claim stops believing the parts you got right. The manuals also fail their own arithmetic in five separate places, all caught by the project's own reviews. Salvage has to be extraction, not repair.

## What it would take, in order

This is sequenced. Items later in the list produce disposable work if started first.

Needs Rudy Behrens, or needs hardware — one day, and it gates everything:

Establish first whether any machine physically survives. One photograph in the archive is dated December 2025 with its camera data stripped, two and a half years newer than anything else, and shows a four-pontoon machine of the same family sitting on wooden pallets. If that machine exists, half a day with a tape measure and calipers closes the pontoon diameter, the frame cut lengths, the mast and stay tube sizes, every bolt, the panel dimensions and the rotor sweep — more than every remaining document task combined.

Then one hour on the phone, with these questions prepared: what pipe size are the pontoons and the frame; what is inside the masthead collar; are the frame joints glued or dry-fitted and lashed; how are the pontoons clamped to the frame; does the 2024 drawing describe the 2015 machine at all; which of the three nozzle sizes was the real part and does one still exist; and can the raw laboratory sheets behind the two credibility documents be obtained. Every one is a five-minute answer from him and unrecoverable from the archive.

Needs the owner — decisions, not work:

Whether to publish at all, given that the buildable object is a raft with a pump on it. Whether to fund the reactor as its own engineering project. The licence declaration for hardware, documentation and software, named separately — noting that nine of the nineteen parts in the CAD model are third-party catalogue downloads, so that model is not the project's to relicense. Who staffs a support channel, since every package in the benchmark with a real build record has a person answering. And a ruling on whether the word "fuel" may appear in public copy for the wax: the site draft and the manual flatly contradict each other on that point, and the reasoning used to route around the firewall is written down in the same folder.

An agent can do alone, unblocked, starting now — about four days total:

Quarantine the four homepage mockups and one system page that lead with a fuel-grade headline and print two laboratory figures as hero numbers. They are the newest files in the manual tree and sit inside the folder that would be pushed to a repository. Half a day.

Extract the five safety findings that exist only as review commentary on the two manuals slated for retirement — toxin release and aerosol from a pressure jet, high-pressure injection injury, vapour from pour foam, and launch, recovery and drowning risk. Three of the five apply unchanged to whichever machine gets published, and retiring those manuals first would delete the only safety guidance in the corpus. Half a day, and it must happen before any file is moved.

Correct the documents that import features of a later, different machine into descriptions of the 2015 one, and the panel document whose central conclusion the pipe legend now falsifies. Rename or re-crop the pond reference image whose filename promises no claims while three of the inventor's captions remain burned into the pixels, since eight documents point at that path. Correct the pond machine's date from 2016 to December 2015 — which makes the two machines contemporaries and easier to present side by side. One day.

Write the honesty page: which machine is which, what the record shows, what was never tested. The one artifact the archive is fully equipped for. One day.

Write the commissioning test: freeboard measured at four corners with a tape, a leak check after an hour afloat, pump output timed into a bucket, rotor cut-in observed against a handheld anemometer. Thresholds derived from the design and labelled as design intent, never as measured history. One day, and the best return on effort in the whole package — it replaces every asserted number with one the builder produces himself.

Write the tools-and-skills page: PVC cutting and solvent welding, drilling, flattening and drilling thin-wall conduit, shearing and bending light sheet, basic 12-volt wiring. No lathe, no welding, no machining. Half a day.

Blocked behind the measurement — seven to nine days:

Derive the fitting schedule and cut lengths from the joint configuration in the photographs against published socket depths for the now-certified 2-inch pipe. Draw the fabricated parts that have no drawing. Redraw the rotor as a fresh design, labelled as a design and not as a record of what was built. Run a genuine sourcing pass at the real pipe size. Roughly one third of the parts list is writable today; the rest is not.

## What cannot be closed

The nozzle geometry, from this archive, at any effort. It is a clean-sheet engineering project drawn from published cavitation research, not an archaeology problem — that literature is live and concrete, and one recent open-access study gives a fully specified plate geometry, inlet pressures and throat velocities, plus a finding that plate thickness significantly affects whether cavitation starts at all, which is precisely the dimension the 2008 sketch omits. Both patents being expired means nothing blocks a clean design. But it needs a bench and a budget, and it does not belong in a raft's build package.

A tolerance statement and a jig package. Needs an engineering judgment that is not in the archive, cannot be inferred from photographs, and requires the inventor or a competent mechanical reviewer to sign it.

Any measured performance figure for either machine — buoyancy, freeboard, flow, power, throughput, runtime. Nothing was ever measured. The only buoyancy number in existence is the inventor's handwritten assertion of 33 pounds net per pontoon, which is his claim, is drawn against a pontoon size that is itself wrong, and back-solves to a pipe smaller than anyone claims. Four times that figure is 132 pounds against roughly 100 pounds of the machine's own equipment — so on his own number the raft is near its limit carrying nothing but itself. A dockside float test the builder repeats is the only honest route.

A step-by-step photographic build sequence for the pond machine. Its assembly was never photographed; all four of its records show a finished machine. The substitutes are a video of a new build, or CAD drawings explicitly labelled as reconstructions.

Whether either machine ever produced anything. The 26-second video proves the raft floated and the rotor turned. It does not show the pump running and does not show anything produced — no flow, no plume, no discharge, no meter, no gauge — and the energy arithmetic permits tens of minutes of pumping a day at most, and only with electrical storage that appears in no photograph. That is a bench question; publishing cannot answer it.

Whether the 2024 drawing describes the 2015 machine at all. The two share an architecture, the files are nine years apart, and no measurement links them. Only the inventor can settle it — and if the answer is no, every dimension in that model describes a design nobody built.

Confidence on this section: high, with one exception. The claim that the nozzle is unrecoverable rests on the archive being complete; if a physical nozzle survives, calipers and a bore scope close the whole geometry gap in an afternoon. That possibility is the first question for Rudy.

## The website

Good news first, and it corrects the brief: nothing is live. solariscybernetics.com currently serves a registrar parking page (checked directly, 2026-08-11). The dead "Get the plans" button, the retired machine descriptions and the fuel-grade mockups all sit in undeployed drafts on disk. There is no public exposure to fix, only a deployment to not perform.

So: do not deploy, and make the drafts safe to leave lying around. Hold the domain on the parking page, or point it at a one-screen holding page saying what the project is with an email address — no claims, no plans button. Quarantine the mockups today, before any repository exists, since they would be pushed along with everything else. Remove the dead plans button rather than leaving it for a future deploy to inherit. Fix the draft's own description, which says two pontoons where the photographs show four and one prototype where at least two exist. And correct the video caption, which names a year and a place the file's camera data contradicts.

The instinct behind the draft — that the homepage is the offer, not the investigation — is right, and it is also what makes the fuel headline dangerous. An offer page carrying a claim with no measurement behind it is the exposure. The replacement is not a softer claim; it is the commissioning test. Publish the procedure, publish the thresholds as design intent, and let each builder produce the number himself. Both reference packages in the benchmark do exactly this, each with a plain disclaimer of what its machine does not do, and neither lost builders for it.
