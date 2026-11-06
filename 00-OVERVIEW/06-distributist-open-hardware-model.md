# The Manatee — A Zero-to-One Proposal

*The single investable document for The Manatee Project. Written for a smart potential co-founder, early investor, or grant funder. Honest by construction: it makes only claims it can defend, and it names the one thing it cannot yet prove.*

---

## The thesis, in one paragraph

The Manatee is a self-charging chemical bio-battery. Free sunlight grows algae in a pond — storing solar energy in living biomass while consuming the pond's surplus nutrients. Sun and wind run a cavitation pump on a small floating raft. The raft breaks the algae open, cleans the water it draws from, and renders a small amount of energy-dense, shelf-stable wax. It trades efficiency for density, duration, and independence: the output holds far more energy per kilogram than a lithium battery, keeps for years without self-discharge, and depends on no grid, no fuel delivery, and no rare-earth supply chain. The business is not the machine. Both underlying patents are expired and in the public domain, so there is nothing to license and nothing to defend. The business is the coordination layer — the open standard, the telemetry network, and the kit — that a distributed fleet of builders orbits. We give the machine away and own the center.

---

## The problem, and the wedge

The hard problem in renewable energy is storage, not generation. Sun and wind are intermittent and often far from where power is needed. Batteries bridge that gap for hours, poorly for days, and not at all for seasons — and they self-discharge, age, and ride a lithium supply chain most of the world cannot access.

The Manatee's lead value is cleaner water. Harmful algae blooms choke ponds, lakes, and slow rivers across the Global South and the rural US. The nutrients that feed those blooms — nitrogen and phosphorus running off farmland — are the same nutrients the Manatee harvests for free. A machine that roams a sick pond, draws in bloom water, and returns cleaner water is valuable on that basis alone, measured with a turbidity reading anyone can take.

The energy is the upside. Every gram of algae the machine breaks open is stored sunlight. What accumulates as wax is a bonus energy reserve — a store you own outright and can burn as heat, light, or cooking fuel whenever you choose. Cleaner water is the wedge that gets the machine into the pond. The stored energy is the reason it stays.

An honest caveat, stated up front: the wax yield is under-indexed here on purpose. Everything past cleaner water is experimental until independently tested. This document sells the proven wedge and treats the energy upside as a hypothesis with a cheap, defined test — not a promise.

---

## The product — the machine in one page

The Manatee is a small floating raft, sized to a single pond, built around four systems.

1. **Hull and propulsion.** A standardized, balanced, low-drag hull — a symmetric catamaran on foam-cored floats — that roams slowly to aerate and treat the whole pond rather than sitting in one corner. Cheap, durable, locally repairable. The one whimsical touch that carries the brand: a googly eye on each pontoon cap.

2. **The cavitation reactor.** A high-pressure pump forces bloom water through a precisely shaped nozzle. The pressure drop triggers hydrodynamic cavitation — collapsing micro-bubbles that break algae cells open. This mechanism is well established in the algae-processing literature; it is not the unknown. The reactor is corrosion-hardened where it must be and owner-serviceable everywhere else.

3. **The separation and storage train.** Broken-open slurry settles; the hydrophobic fraction rises and is skimmed into storage; clarified water returns to the pond below the surface. A passive solar-warmed settler helps the layers break. Biomass must be exported ashore for the water to be genuinely cleaner — a point the design and the protocol both enforce.

4. **The power and control heart.** Solar is the workhorse; one rugged glass panel runs the machine. Wind is an optional add-on where it is justified. The survival loop is a deliberate pure-analog reflex — a discrete comparator that disconnects the pump before the battery is harmed — because nothing critical should depend on firmware that can crash. Digital exists only as an unpluggable **Observer**: a logger that measures energy in, wax out, and turbidity before and after, and phones the numbers home. The Observer is the moat, not the machine.

The kit ships in a 55-gallon drum that is both the reactor vessel and the shipping crate. The corrosion-critical, hard-to-source brains ride inside; the bulky members — floats, frame, mast, panel — are a printed cut-list the builder buys locally.

### Kit tiers

| Tier | What it is | Builder's all-in |
|---|---|---|
| **Build-Anywhere** | Free plans and BOM. Atoms only, sourced entirely by the builder. The mission tier — "someone in Africa could build one." | Local materials only |
| **Demonstrator** | Cheapest faithful proof-of-concept kit. Proves cavitation cleans water and renders a little wax, and instruments the question cheaply. | ~$2,600 |
| **Real-Machine** | The version that actually works: right-sized triplex pump, marine-grade rigging, full separation train, honesty instrumentation. | ~$5,100–5,600 |
| **Observer add-on** | The telemetry unit — the fleet-data node. | $199 |

Kit retail: Demonstrator $1,950, Real-Machine $3,950. Prices are real US retail BOM plus a lean ~30% margin.

---

## The business model — distribute the means, own the coordination

The strategy is distributism: put the means of energy production into as many hands as possible. Belloc and Chesterton argued for widely distributed productive property — the family cow, the workshop, the plot of land. The Manatee is a distributist machine for energy. We do not sell energy. We do not own the robots. We arm the builders and steward the center.

You cannot own this technology — it is open, and the patents are expired. So we do not try. In open hardware, the tech is free but the hub is not. Arduino, Prusa, Raspberry Pi, iNaturalist, Wikipedia — each gave the thing away and kept the coordination role. We become **The Manatee Project**: the foundation-style hub the whole fleet orbits.

The moat, ranked:

1. **The telemetry network.** Every Observer unit logs the same numbers — energy in, wax out, turbidity in and out, pond type, climate, configuration — and reports to one public dashboard. That aggregated dataset of *what actually cleans water and banks energy, where* is a network effect no fork can copy: more builders produce more data, which produces a better reference design, which attracts more builders. This is the flywheel.
2. **Reference-design stewardship.** We maintain the canonical known-good plans. Forks orbit the source of truth.
3. **The standard and the trust mark.** We define what "works" means — the Manatee benchmark — and certify builds against it. Whoever owns the measure owns the conversation.
4. **The kit.** Convenient, de-risked sourcing funds the hub, the way an official Arduino funds Arduino.
5. **The community.** Forum, a live map of deployments, docs, events.

Three surfaces, one motion: **free plans go wide, the kit is the premium convenience, Build-Anywhere is the cheapest path for those who source their own atoms.** Revenue comes from kits, foundation and NGO grants, certification licensing of the mark, and data services for serious operators — municipalities and farms that want it done and measured, not DIY'd. None of it requires an exaggerated claim to work.

---

## The market and the buyer

Three buyers, one machine.

- **The Global-South household or village** with a fouling pond, strong sun, and no reliable grid. The design north star is written for this buyer: cheap, durable, fast to amortize, repairable with local materials and hands. This is the appropriate-technology lineage — Hugh Piggott's hand-built turbines, William Kamkwamba's Malawi windmill.
- **The off-grid homestead or remote farm** in the developed world that values autonomy and resilience over cents-per-kilowatt-hour, and already has the free inputs: a sick pond, sunlight, wind, land.
- **The grant or NGO deployment.** Harmful-algae remediation, rural-development, and energy-resilience funders want exactly this: an open, measurable, distributed cleaner-water project with an energy dividend. The Observer makes every unit a data point in a fundable, reportable program.

The buyer is not chasing grid arbitrage. The buyer wants an energy and water asset they fully control.

---

## The economics, done right

The common mistake is to price this machine in watt-hours. That is the wrong lens, because there is no electricity input to pay for. The sun is free. The nutrients are surplus — the pond is paying you to remove them. Round-trip efficiency and EROI are the wrong bar entirely: they matter when you buy the energy going in, and here you do not.

The right frame: **the cost of stored energy is the amortized capital of the machine over its lifetime.** A machine that costs a few thousand dollars and runs for fifteen years on free inputs has a cost of energy set almost entirely by how long it lasts. **Durability is the economics.** This inverts the usual engineering instinct — a rugged, hand-serviceable, fast-payback machine beats a fragile efficient one at every turn. Every part is chosen for cheap × durable × fast-to-amortize × locally-repairable, never for peak efficiency or sleekness.

The energy-density physics is the reason the store is worth making at all. A hydrocarbon wax holds roughly 40 to 100 times more energy per kilogram than a lithium battery, keeps for years with no self-discharge, needs no battery-management system or thermal control, and pours off divisibly to carry anywhere. Even converted back to electricity through a modest generator, a stored hydrocarbon carries many times a battery's energy per kilogram; used directly as heat or light, the full advantage holds. This is general chemistry, not a yield claim.

And the value is dual at every turn. The machine produces cleaner water *and* a stored-energy reserve from the same pass. Even if the energy economics stayed thin, the remediation value stands alone. That dual return is what makes the amortized-capital math forgiving: you are buying two outputs with one durable asset fed by free inputs.

---

## The central unknown, and how we de-risk it

One number decides everything past cleaner water: **how much usable wax accumulates per unit of energy the pump spends, and whether a season of sun banks a reserve worth having.** The mechanism — cavitation breaks algae cells open — is proven. The yield on this machine has never been measured. Everything downstream of that number is, until measured, a hypothesis.

The de-risking is deliberately cheap and staged.

**Stage one — the ~$100 garage bench test.** A consumer pressure washer is a cavitating high-pressure pump. Plug it into a $20 energy meter, recirculate a thick algae slurry through its jet, let the batch settle, and weigh what floats. Read turbidity before and after with a printed Secchi card. That afternoon answers three questions: does a wax layer form and break clean, how much per unit of energy, and does the water measurably clear. Use store-bought Chlorella or Spirulina for the bench so the yield question is isolated from any toxin-handling question. A hidden but likely-decisive sub-experiment rides alongside: cheap concentration. Bloom water is almost entirely water; you cannot skim wax off it until you thicken the slurry ten to a thousand fold. Whoever makes cheap, low-energy concentration work holds the real invention. The bench tests four cheap methods — gravity settling, food-grade flocculant, dissolved-air flotation, and coalescing media — and finds which combination reaches a workable solids fraction.

**Stage two — the ~$4,000 instrumented gate, firewalled.** Any claim about wax as fuel — energy content, energy balance, chemistry — waits behind an independent lab test on the existing rig: gas chromatography, standard fuel assays, calorimetry, and a metered batch. Until that gate is passed by an outside lab, no fuel claim is made in any money conversation. This firewall is deliberate and non-negotiable. The bench test decides whether the $4,000 test is even worth running; a bench pass de-risks the capital, a bench fail saves it.

The point of the staging: spend $100 before $4,000, and make no claim you have not independently earned.

---

## Why open-source wins here

You cannot license an expired patent. Both underlying patents are in the public domain, and the nozzle was never claimed — so there is almost nothing to infringe and nothing to protect. The instinct to build a defensible IP moat here is a dead end by construction.

Open-source is not a concession, then; it is the winning move. What is genuinely hard to fork is the coordination role and the aggregated telemetry — network effects and trust, not law. An open repo maximizes builders; every builder is a data node; the dataset compounds into a yield map no competitor has. The design self-improves each release from real fleet telemetry — a self-learning system where the learning is the fleet's, run through our hub. Licenses: hardware under CERN-OHL-S, docs under CC BY-SA 4.0, firmware under MIT. We win by being indispensable to a movement we did not have to manufacture, which is the most durable moat there is.

---

## The ask, and the path


**What the next 6 to 12 months need:**

1. **Run the ~$100 bench test.** The single highest-leverage act available. It converts the central unknown from assertion to a number, in an afternoon, for the cost of a nice dinner. Everything else is gated on it.
2. **Resolve the physical design.** Lock the standardized balanced hull and the slow-roaming propulsion method, then finalize the Real-Machine spec around them.
3. **Publish the hub.** The open repo, the Observer protocol and one-line data schema, and a live results dashboard — seeded with the bench data and one to three pilot builds. The dashboard is the product; ship it before the fleet exists and let the empty map be the invitation.
4. **Seed the first fleet.** Get plans in front of thousands through the site and the whimsy; a fraction build. Every build is a telemetry node, not a cost.
5. **Gate the rest.** Clear the patent-assignment title cloud with Delaware and IP counsel, and fund the ~$4,000 lab trio, before any sale, license, or fuel claim. These are legal and documentation fixes, not science fixes.

**What a funder or co-founder is buying:** not a promise of cheap fuel, which we refuse to make. A proven cleaner-water wedge, a defensible density-and-independence energy thesis with a $100 test standing between hypothesis and number, and a coordination-layer business that wins by owning the standard and the data instead of an IP no one can hold. The next hundred dollars buys the clarity that decides the next hundred thousand.

---

