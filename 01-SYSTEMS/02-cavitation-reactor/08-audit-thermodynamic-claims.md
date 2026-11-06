# The Literally-False Physics (and the Survivable Version of Each)

**Engagement:** Due diligence — Mobula / EVIE-2c algae-to-diesel ocean robot (Rudy Behrens / Solaris Cybernetics / Barsoom Engineering)
**Section:** Case-against, deep pass on the physics narrative
**Builds on (do not re-derive):** `systems/_validation-physics.md`, `01_MASTER_DUE_DILIGENCE_v2.md` §2/§4/§8e, `03_ADDENDA.md`
**Primary sources dissected:** `corpus/converted/text/LVKNprocess.txt` (the inventor's own "Thermo-Electric Conversion" derivation, L37–53) and `SC1aecom1report2.md` L98 (the AECOM/PACE remediation write-up)

---

## Why this section exists

The validation memo already returned the right verdicts. This section does something narrower and more useful to you, the project lead: it takes the four headline physics phrases that appear on the rig docs and in the AECOM report, and for each one it (a) quotes what it actually says, (b) shows — with the real numbers — *why a hostile physicist demolishes it in under a minute*, and (c) writes the exact honest sentence that survives. The deliverable is a **find-and-replace table** you can hand to anyone writing the website, the pitch, or the patent prosecution. Every false phrase is a credibility landmine. Every one has a true replacement that costs you nothing because the *fuel is still real*.

The governing fact, established elsewhere and assumed here: **a diesel-density, diesel-energy oil genuinely comes out of this process** (ASTM D4052 → 32.71° API; D240 → 134,258 BTU/gal — `BEARfuelTest1.pdf`). Nothing below disputes that. What is false is the *mechanism story* bolted onto the real output. You can throw away 100% of the false physics and lose 0% of the asset. That is the whole argument of this section.

### The real mechanism, in one paragraph (so the corrections make sense)

DOCUMENTED/INFERRED. A pump accelerates warm (~150 °F / ~66 °C) algae slurry through a venturi. Where the flow speeds up, static pressure drops (Bernoulli); when local pressure falls below the liquid's vapor pressure, the liquid *boils cold* and nucleates vapor cavities. The cavities are swept downstream into higher-pressure fluid and **collapse violently**. Each collapse is a near-spherical implosion: the cavity wall accelerates inward, the trapped gas/vapor is compressed almost adiabatically in the final nanoseconds, and for ~100 picoseconds a sub-micron pocket reaches thousands of kelvin and thousands of atmospheres before the shock radiates away and the whole thing is over. Millions of these per second, randomly located, do the chemistry: they disrupt algal cell walls and (the claim) partially crack/decarboxylate lipids toward paraffin. **This mechanism is real, well-studied, and sufficient to explain the output.** Every error below comes from describing this stochastic, picosecond, sub-micron, violently-dissipative event as if it were a *steady, macroscopic, reversible machine*.

The science that bounds it (cited inline below): the **Rayleigh–Plesset equation** governs the cavity radius R(t); **single-bubble sonoluminescence (SBSL)** is the cleanest laboratory realization, with a stably-trapped bubble oscillating between ~5–50 µm and collapsing to a sub-micron minimum, emitting a **<100 ps** flash of light, reaching **~10,000 K** and **gigapascal** interior conditions, with wall accelerations **>10¹¹ g** and a **megabar-class (~10⁴ atm) shock** launched into the surrounding liquid at minimum radius ([Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence); [Weninger/Putterman SL review, NCSU](https://weninger.wordpress.ncsu.edu/files/2022/09/SLreview.pdf); [Brenner/Hilgenfeldt/Lohse, *Modeling SBSL*, arXiv:1407.5531](https://arxiv.org/pdf/1407.5531)).

---

## Claim 1 — "The pressure inside this rotating zone is absolute zero"

### (a) What it says
> "The primary rotation is nearly 15000rpm. **The pressure inside this rotating zone is absolute zero** and the temperature is 1500 degrees F."
> — `LVKNprocess.txt` L43–44 (repeated for the secondary zone, L46: "Its pressure is also absolute zero and its temperature is 630 degrees F")

### (b) Why it is false — the 30-second demolition
This phrase is self-contradicting *in the same sentence*, and a hostile physicist needs only the ideal gas law to kill it:

- **A hot, gas-filled cavity cannot be at zero pressure.** The doc asserts the cavity is at 1500 °F (≈1089 K) **and** at "absolute zero" pressure simultaneously. For any gas, P = nRT/V. If T > 0 and there is *any* gas or vapor in the void (there must be — that gas is what gets hot and does the chemistry), then **P > 0, necessarily.** You cannot have a 1089 K pocket at 0 Pa. The two halves of the sentence are mutually exclusive. (ASSERTED-and-self-refuting.)

- **"Absolute zero pressure" is a category error.** "Absolute zero" is a *temperature* (0 K). Applying it to pressure reveals the phrase is rhetorical, not measured. The real pressure floor is a perfect vacuum (0 Pa) — and a vacuum is *cold and empty*, the opposite of a 1500 °F reacting hot-spot.

- **The actual collapse zone is the highest-pressure region in the whole apparatus, not the lowest.** This is the part that gets the mechanism exactly backwards. Cavitation has two phases: a brief *low-pressure* nucleation (where the cavity is *born*, at pressure ≈ the vapor pressure, ~3 kPa for warm water — low, but emphatically **not zero**) and a violent *high-pressure collapse* (where the chemistry happens). At minimum radius the interior reaches **gigapascals** and the liquid sees a **megabar-class shock (~10⁴ atm)** ([Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence); [Weninger SL review](https://weninger.wordpress.ncsu.edu/files/2022/09/SLreview.pdf)). The doc attaches "absolute zero pressure" to the moment of *maximum* heat — i.e., to the collapse — which is precisely where the pressure spikes to its peak. The number is not just wrong in magnitude; it has the wrong sign of the gradient.

- **It contradicts the inventor's own correct sentence 26 lines earlier.** `LVKNprocess.txt` L17 states the mechanism correctly: cavitation is induced when velocity "reduces the pressure to **less than the vapor pressure** of the fluid." That is the right, defensible, textbook description. Then L43 throws it away for "absolute zero." A reviewer who reads both lines concludes the author *knew the right answer and chose the dramatic one* — which is worse for credibility than not knowing.

### (c) The strongest version that survives
> *"At the venturi throat the flow accelerates and local static pressure momentarily drops **below the fluid's vapor pressure** (~3 kPa at 66 °C), nucleating vapor cavities. These cavities are swept downstream and collapse, generating **transient high-pressure, high-temperature hot-spots** — the regime cavitation research associates with hundreds-to-thousands of atmospheres and shock emission at minimum radius."*

This is true, it is impressive (thousands of atmospheres *is* the headline), and it matches the inventor's own L17. **Cost of switching: zero. The dramatic version was strictly weaker than the truth** — "below vapor pressure, then a megabar collapse" is a *better* story than "absolute zero," and it is real.

**Landmine phrase to delete on sight:** *"absolute zero pressure."* Both instances (L44, L46).

---

## Claim 2 — "Stable 15,000 rpm primary rotation in a 1000-Ångström zone" (+ "2000 rpm secondary zone, 0.04-inch diameter")

### (a) What it says
> "The primary rotation is nearly 15000rpm... this zone is only **1000 Angstroms in diameter**. The flow entrained inside the spiral is rotating at **2000rpm inside a zone 0.04 inches in diameter**."
> — `LVKNprocess.txt` L43–46

### (b) Why it is false — the 30-second demolition
This is the single richest landmine in the corpus, because it pairs **fabricated precision** with a **physical impossibility**. Three independent kills:

**Kill 1 — You cannot have a steady rpm in a structure that exists for picoseconds.**
"rpm" (revolutions *per minute*) is a steady-state rate. A cavitation collapse is a one-shot transient: the cavity exists for microseconds and the energetic collapse/emission lasts **<100 ps** ([Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence); [Camara/Putterman, ASA 2000](https://acoustics.org/pressroom/httpdocs/140th/camara.htm)). Quoting "15,000 rpm" for a feature that lives ~10⁻¹⁰ s is a unit error of staggering size. Run the arithmetic a reviewer will run in their head: 15,000 rpm = 250 rev/s = one revolution every **4 milliseconds**. The hot-spot exists for ~100 ps = 10⁻¹⁰ s. In its entire lifetime the structure could complete **~0.0000025 of a single revolution** — about 0.0009°. It does not "rotate at 15,000 rpm"; it does not complete a measurable fraction of one turn before it is gone. *(Math: 250 rev/s × 100×10⁻¹² s = 2.5×10⁻⁸ rev.)* (INFERRED from documented collapse timescales; the conclusion is not close.)

**Kill 2 — The dimensions are mutually inconsistent and below any instrument on the rig.**
- "1000 Ångströms" = 1000 × 10⁻¹⁰ m = **100 nm = 0.1 µm.** SBSL bubbles collapse to a sub-micron minimum (order ~0.5 µm for a 27 kHz drive; [Weninger SL review](https://weninger.wordpress.ncsu.edu/files/2022/09/SLreview.pdf)), so 0.1 µm is at least *order-of-magnitude plausible* as a collapse minimum — but it is quoted as a **stable rotating "zone diameter,"** which it is not, and which nothing on a 5-gallon bench rig can *measure*. Resolving a 100 nm feature requires electron microscopy or X-ray free-electron-laser imaging (the latter is literally how the 2024 *New J. Phys.* group imaged a collapsing SL bubble — [IOPscience 10.1088/1367-2630/ad295b](https://iopscience.iop.org/article/10.1088/1367-2630/ad295b)). A clamp meter and a thermocouple cannot see it. So the 0.1 µm number is **asserted, not observed** — false precision to four significant figures about something the apparatus is blind to.
- The "0.04-inch (≈1 mm) secondary zone" rotating at "2000 rpm" is **10,000× larger** than the primary "1000 Å" zone. The doc gives no mechanism by which a 100 nm structure and a 1 mm structure coexist as nested steady rotors. They are presented as engineering facts; they are narrative.

**Kill 3 — "Stable / controlled / non-random" contradicts the defining property of cavitation.**
The doc's framing (L40–41) is that the venturi makes the energy distribution "controlled, directed and **non-random**." But cavitation's signature property — stated correctly by the inventor himself two lines earlier (L37–38: "location of individual bubbles **can not be calculated**") — is that it is **stochastic**. Collapse sites are random in space and time; that randomness is intrinsic, not an engineering defect to be tuned away. Claiming a "stable, non-random" rotating nanostructure is claiming you have deterministically tamed a chaotic process at the 100 nm / 100 ps scale with a pump and a nozzle. A reviewer who works in the field will not believe it without high-speed imaging, and there is none.

### (c) The strongest version that survives
> *"A vortex-geometry venturi concentrates turbulent kinetic energy into intense, localized cavitation events rather than spreading it across a flat shock front. Individual collapse sites are inherently stochastic and sub-micron; the design intent is to raise their local intensity, not to create a steady rotating structure."*

That keeps the **engineering insight that may be real** (focus turbulence → more energetic local collapses) and drops every fabricated number. Note what you lose: nothing measured. The 15,000 rpm, the 2000 rpm, the 1000 Å, the 0.04 in are *all* un-instrumented assertions. `KINETIC_NOZZLE.md` §4 concedes as much ("localized temperature claims require high-speed sensor validation") — which is an admission that the geometry is asserted, not measured.

**Landmine phrases to delete on sight:** *"stable 15,000 rpm,"* *"1000 Angstroms in diameter,"* *"2000 rpm... 0.04 inches,"* and the word *"non-random"* as applied to collapse location.

---

## Claim 3 — "Controlled tetra-helical vortex → three vortices → worm-like energy exchange"

### (a) What it says
> "The venturi redirects the energy of cavitation... first into a controlled **tetra-helical vortex**, then compresses the **three vortices** into a rotating flow that also spirals around a center... causing oscillating zones of gas and liquid to exchange energy in a **'worm-like' motion**."
> — `LVKNprocess.txt` L39–48

### (b) Why it is false (or, more precisely, *unfalsifiable* — which is worse)
This is not wrong the way "absolute zero pressure" is wrong; it is **undefined**, which a hostile reviewer treats as a redder flag because it cannot even be tested.

- **"Tetra-helical vortex" is not a term in fluid dynamics.** A helix is a single 3-D curve; "tetra-helical" would imply a four-strand braided helical structure (a geometry borrowed from chemistry/biology — e.g., collagen's triple helix, or "tetrahelix" from Buckminster Fuller's geometry of stacked tetrahedra). It has **no standard hydrodynamic definition**, no governing equation, and no measurement. (ASSERTED — vocabulary borrowed from an unrelated field to sound rigorous.)
- **The count slips inside one sentence.** "Tetra-" (four) helical vortex becomes "the **three** vortices" 1.5 lines later (L39–40). Four → three with no transition. False precision that *contradicts itself* is the tell that this is description-as-decoration, not a derived flow field.
- **"Worm-like motion" / "oscillating zones exchanging energy"** is imagery, not physics. There is no model, no scale, no frequency, no derivation. It paints a picture of energy being *passed back and forth* between zones — which, as Claim 4 shows, is the linguistic seed of the false "energy is recovered" claim.
- **Zero derivation, zero instrumentation.** Nothing on the rig can resolve a vortex structure at the cavitation scale. The entire passage (L37–53) contains not one equation, unlike the *correct* energy paragraph above it (L20–23) which does show its Euler-equation work. The mechanism section abandons the math precisely where the math would expose it.

### (c) The strongest version that survives
> *"The nozzle uses a swirl/vortex geometry to organize the flow so that cavitation is concentrated in a confined region of the stream while the bulk remains in laminar flow."*

If the inventor wants to claim *more* than this, the burden is high-speed imaging or PIV (particle image velocimetry) of the actual flow field. Until then, "tetra-helical" and "three vortices" and "worm-like" are **unsupported vocabulary** and should be cut entirely. Keep "swirl/vortex geometry concentrates cavitation" — that is a normal, defensible thing a nozzle can do.

**Landmine phrases to delete on sight:** *"tetra-helical vortex,"* *"three vortices"* (the self-contradicting count), *"worm-like motion."*

---

## Claim 4 — "An adiabatic (thermodynamically reversible) process... much of the energy used in the conversion is recovered"

### (a) What it says
> "The paraffin is formed by Hydrous Pyrolysis... This is achieved... via controlled, directed cavitation which produces the required pressure and temperatures but is an **adiabatic (thermo-dynamically reversible) process. Thus much of the energy used in the conversion is recovered.**"
> — `SC1aecom1report2.md` L98 (AECOM/PACE remediation write-up, signed Rudolph Behrens, CEO)

### (b) Why it is false — the most sophisticated landmine of the four
This is the one a former API-610/617 pump engineer (which Behrens' CV claims) should know better than to write, and it is the load-bearing falsehood behind the headline EROI. Two distinct errors are fused here:

**Error A — "adiabatic" does not mean "reversible."** These are *different concepts*, and the parenthetical equates them. *Adiabatic* = no heat crosses the boundary (Q = 0). *Reversible* = no entropy generated (ΔS_universe = 0). A process can be adiabatic and **wildly irreversible** — the textbook example is *free expansion* of a gas into a vacuum (adiabatic, Q=0, but entropy increases and no work is recovered). Conflating the two is a first-year-thermodynamics error. (DOCUMENTED conflation; the two terms are not synonyms.)

**Error B — cavitation collapse is the textbook *irreversible* process, and the very features that make it work are the entropy generators.** A reviewer lists them in fifteen seconds:
- **Shock-wave emission.** Each collapse radiates a megabar-class shock into the liquid ([Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence)). Shock waves are *definitionally* irreversible — entropy jumps across the shock front (Rankine–Hugoniot). Energy that leaves as an outgoing shock is gone; it is not "recovered."
- **Sonoluminescence.** The collapse emits broadband UV/visible light ([Weninger SL review](https://weninger.wordpress.ncsu.edu/files/2022/09/SLreview.pdf)). Photons radiated away are energy *lost* from the fluid — the opposite of recovery.
- **Non-adiabatic wall heat conduction.** At the 100 nm / 100 ps scale, the temperature gradient between a ~10,000 K core and ~340 K water is enormous, and the surface-to-volume ratio is extreme. Heat conducts out of the hot-spot fast; the collapse is *not even truly adiabatic* at this scale, let alone reversible.
- **Bond-rearranging chemistry.** The whole point is to *crack/decarboxylate* lipids — to break and remake covalent bonds. Chemical reactions that proceed are spontaneous and entropy-generating; you do not get the activation energy back. If the chemistry were reversible, the paraffin would un-form.

So the mechanism is irreversible *by every channel through which it does useful work.* Calling it "reversible, therefore energy is recovered" is a **Second-Law overclaim of the perpetual-motion family** — it claims the dissipative step is secretly conservative.

**Why this one matters most to the money.** The headline economics — "conversion costs only 5.34% of the fuel's energy, ~19:1 EROI" (`LVKNprocess.txt` L32) — counts *only* ideal pump-acceleration work (204.84 BTU/gal ÷ 0.03). It can ignore everything else *only if* the collapse energy is "recovered." The AECOM "reversible" sentence is the stated justification for that omission. **Falsify "reversible" and you falsify the 5.34% independently of the boundary-drawing critique** — because now the latent heat of vaporizing the cavitating fraction, the shock/acoustic losses, the radiated light, and the recirculation losses are all real, unrecovered costs that the balance dropped. Independent hydrodynamic-cavitation lipid-disruption literature already puts cell-disruption alone at ~13% of biomass energy — ~2.4× the *entire* claimed figure, before any cracking.

### (c) The strongest version that survives
> *"Cavitation delivers the required transient pressure and temperature locally and briefly, so the **bulk slurry is not heated to pyrolysis temperature** — the process avoids the large sensible-heat load of conventional thermal pyrolysis. And because the loop recirculates warm (~66 °C) fluid, **reheat energy between passes is reduced.** The collapse itself is irreversible and dissipative; its energy is not recovered."*

That captures the *genuine* efficiency advantage (you don't bulk-heat the whole batch to 350 °C the way HTL does; the warm loop saves reheat) **without** the false reversibility premise. It is a real and defensible selling point. "Reversible / recovered" must go.

**Landmine phrases to delete on sight:** *"thermodynamically reversible,"* *"much of the energy... is recovered,"* and the equation *"adiabatic (= reversible)."* Keep "adiabatic" **only** if used correctly to mean "the bulk fluid isn't heated" — but given the demonstrated conflation, safest to drop it and say "the bulk fluid is not heated to pyrolysis temperature."

---

## The one claim that is actually CONSERVATIVE — be fair: "1500 °F core temperature"

It would be dishonest to lump this in with the falsehoods. **The 1500 °F figure is defensible and, if anything, *low*.**

- 1500 °F ≈ 1089 K. Peer-reviewed multi-bubble and single-bubble cavitation hot-spots run **~5,000 K to ~12,000 K**, with X-ray and emission studies putting the SL core near **~10,000 K** and gigapascal pressures ([Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence); [Brenner/Hilgenfeldt/Lohse, arXiv:1407.5531](https://arxiv.org/pdf/1407.5531)). Flannigan & Suslick deliberately *tuned* single-bubble emission temperatures across a wide range that bottoms out near ~1,500 **K** — and 1089 K is below even that floor.
- The required cracking/decarboxylation chemistry for hydrous pyrolysis runs in the ~300–600 °C range; the doc's *secondary*-zone figure of 630 °F (≈332 °C) is right in that band, and the 1500 °F primary is comfortably above it.

So the temperature claim is the **one number a physicist would *not* attack** — it is conservative relative to the literature. The honest framing: *"transient hot-spots in collapsing sub-micron cavities reach at least ~1500 °F (and cavitation literature routinely reports far higher, up to ~10,000 K)."* The credibility damage comes entirely from the *geometry and steadiness* claims wrapped around this number (Claims 1–3), not from the number itself.

**One caveat to state plainly:** 1500 °F is a *peak transient in a sub-micron bubble for ~100 ps*, not a bulk temperature the slurry experiences. Quoting it as if the fluid sits at 1500 °F would be misleading; quoting it as a transient hot-spot peak is correct and conservative.

---

## The find-and-replace table (hand this to whoever writes the public copy)

| # | Landmine phrase (delete) | Source | 30-sec kill | Honest replacement (keep) |
|---|--------------------------|--------|-------------|---------------------------|
| 1 | "absolute zero pressure" | LVKN L44, L46 | Hot gas-filled cavity has P=nRT/V>0; collapse is the *high*-pressure phase (megabar shock); "absolute zero" is a temperature | "local pressure drops **below vapor pressure**, nucleating cavities that then collapse at hundreds-to-thousands of atm" |
| 2 | "stable 15,000 rpm" / "1000 Ångströms" / "2000 rpm, 0.04 in" / "non-random" | LVKN L43–46, L41 | No steady rpm in a 100 ps structure (0.0000025 rev per lifetime); 100 nm is below any rig instrument; cavitation is *stochastic* (his own L37) | "a vortex geometry **concentrates** stochastic, sub-micron cavitation events; intensity is the design lever, not a steady rotor" |
| 3 | "tetra-helical vortex" / "three vortices" / "worm-like motion" | LVKN L39–48 | Not a fluid-dynamics term; count slips 4→3 in one sentence; zero derivation/imaging | "a swirl/vortex nozzle geometry concentrates cavitation in a confined region while the bulk stays laminar" |
| 4 | "adiabatic (thermodynamically reversible)... energy is recovered" | AECOM L98 | Adiabatic ≠ reversible (free expansion); collapse is irreversible by *every* working channel (shock, light, conduction, bond chemistry); this is the false basis of 5.34% EROI | "the **bulk fluid is not heated** to pyrolysis temperature, and the warm recirculating loop reduces reheat; the collapse itself is dissipative and not recovered" |
| ✓ | "1500 °F core temperature" — **KEEP** | LVKN L44 | *(none — it's conservative vs ~10,000 K literature)* | "transient sub-micron hot-spots reach **at least** ~1500 °F (literature: up to ~10,000 K)" |

---


Four phrases on these documents are the entire physics liability, and you can excise all four in an afternoon of copy editing without touching the asset:

1. **"Absolute zero pressure"** — delete both instances. It is self-refuting (hot gas can't be at zero pressure) and it points at the *high*-pressure collapse, getting the sign backwards. The inventor already wrote the correct version on line 17 of the same doc; just promote that one.

2. **"Stable 15,000 rpm in a 1000-Å zone"** — this is the worst one, because it is *fabricated precision about a thing the rig cannot measure.* A reviewer does the mental math (one rev every 4 ms vs. a 100-picosecond hot-spot = a quarter of a millionth of a turn before it's gone) and concludes the whole document is decorative rather than measured. Cut every rpm and every Ångström figure; keep "vortex geometry concentrates cavitation."

3. **"Tetra-helical vortex / three vortices / worm-like"** — undefined vocabulary that even contradicts its own count (four becomes three in one sentence). Unfalsifiable claims are *more* damaging than wrong ones because a skeptic can't even engage them — they just walk away. Cut it.

4. **"Adiabatic (thermodynamically reversible) → energy recovered"** — this is the dangerous one, because it's the **stated justification for the 5.34% / 19:1 EROI headline.** It fuses a definitional error (adiabatic ≠ reversible) with a Second-Law overclaim, and it's the load-bearing excuse for ignoring latent heat, shock/light losses, and recirculation in the energy balance. Retiring it doesn't just fix a sentence — it forces the EROI to be re-derived honestly (likely 13–20% cost before lighting, not 5.34%). Keep only "the bulk fluid isn't heated; the warm loop saves reheat."

And the thing to **stop apologizing for: the 1500 °F number is fine.** It's conservative. If anyone defending the project gets nervous about the temperature, that's misplaced — the temperature is the one figure a physicist endorses. The nervousness belongs on the geometry and the reversibility, not the heat.


---

*Sources: [Wikipedia, *Sonoluminescence*](https://en.wikipedia.org/wiki/Sonoluminescence) (flash <100 ps, ~10,000 K, gigapascal/megabar conditions, >10¹¹ g, 5–50 µm bubble range); [Weninger/Putterman SL review (NCSU)](https://weninger.wordpress.ncsu.edu/files/2022/09/SLreview.pdf) (sub-micron emitting radius, shock emission); [Brenner, Hilgenfeldt & Lohse, *Modeling SBSL*, arXiv:1407.5531](https://arxiv.org/pdf/1407.5531) (Rayleigh–Plesset dynamics, hot-spot temperatures); [Camara/Putterman, ASA 2000](https://acoustics.org/pressroom/httpdocs/140th/camara.htm) (picosecond flash timing); [collapse imaged with X-ray FEL, *New J. Phys.* (IOPscience 10.1088/1367-2630/ad295b)](https://iopscience.iop.org/article/10.1088/1367-2630/ad295b) (gigapascal/10,000 K, instrument scale). Primary docs: `corpus/converted/text/LVKNprocess.txt` L17, L37–53; `SC1aecom1report2.md` L98. Builds on `systems/_validation-physics.md` and `01_MASTER_DUE_DILIGENCE_v2.md` §2/§8e.*
