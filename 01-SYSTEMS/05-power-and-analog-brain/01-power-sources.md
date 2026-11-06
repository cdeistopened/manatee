# The Manatee — Power Sources (Wind & Solar)

*Which renewable inputs to fit the Manatee (EVIE-2c), judged under a strict appropriate-technology lens. This document sits alongside the [Electronics Guide](03-ELECTRONICS-GUIDE.md) (which specifies the charge/store/protect circuitry) and the [Bio-Battery Thesis](01-THESIS-bio-battery.md) (which explains why an all-renewable, self-charging machine is the point). Here we choose the panels and turbines that actually feed it.*

**Who this is for:** the same patient off-grid builder — but read through the project's design north star: **"someone in Africa could build and maintain one with our kit."** Every option below is scored on **cheap × durable × fast-to-amortize × locally-repairable**, NOT peak efficiency or sleekness. A rugged, hand-serviceable, fast-payback part beats a fragile high-efficiency one every time. Where a part can be *built locally* from wood, PVC, or scrap, we ship only the irreplaceable core and let the builder make the rest.

---

## 0. The load we are actually feeding (read this first)

Everything downstream is sized by one number, and it is small:

- **Tier-1 daily need: ~120–170 Wh/day** — the pump run as short daily batches, not continuously.
- **The pump** is a small triplex/diaphragm unit, roughly **450–700 W peak**, run in short bursts. Peak watts are buffered by the battery; the *energy* per day is what matters, and it is tiny — a couple of phone-charger-days.
- **The battery** (12 V, 50–100 Ah LiFePO4 ≈ 640–1,280 Wh usable) is the buffer between a spiky source and a spiky load. Both wind and solar only have to *refill the tank* over a day, not track the pump.

**Consequence for this whole document:** the Manatee is a **trickle-charge** machine. It does not need a powerful generator; it needs a *reliable, all-day, low-maintenance* one. This flips the usual "more watts = better" instinct on its head and is exactly why the appropriate-tech lens is the right lens. A 100 W solar panel alone closes this budget with margin. **Wind is a resilience add-on, not a necessity** — the Electronics Guide already drops it from the baseline for good reason (an unloaded turbine overspeeds and cooks itself). So the honest framing throughout: *solar is the workhorse; wind is optional insurance for cloudy/windy sites and for the appropriate-tech story.*

---

## 1. WIND — commercial, cheap-and-durable

### The blunt truth about the cheap end of this market

Small wind is where appropriate-technology romance meets a graveyard of dead hardware. The consensus across off-grid forums (diysolarforum, northernarizona-windandsun) is harsh and worth internalizing: **most sub-$500 Amazon/eBay/Alibaba turbines are junk** — wildly overrated wattage (a "3000 W" unit for $300 is a lie), blades that "barely turn even in winds over 25 km/h," bushings instead of bearings, no real overspeed protection, and mystery-metal that corrodes in a season. Near water and salt-damp air, that failure clock runs faster. Rule of thumb: **divide the advertised watts by 3–5 and assume a 1–3 year life** on anything under ~$200.

That said, a floating raft on a pond has one thing going for it: the load is tiny (~150 Wh/day) and the mast-top mass must stay low for capsize reasons. So we are not shopping for a big machine — we want the *smallest reputable* one, or none.

### Ranked by durability-per-dollar (not watts)

| Rank | Model | Rated | Real-world | ~Price | Honest durability verdict |
|------|-------|-------|-----------|--------|---------------------------|
| **1** | **Primus Wind Power AIR 40** (formerly Southwest Windpower / now Ryse Energy) | 160 W @ 12/24/48 V | The genuine survivor. **>135,000 units sold in 120+ countries**, marine-grade sealed body, built-in microprocessor regulator (internal dump/brake — no separate dump controller needed), 5-yr warranty, US-made. | **$650–900** | The one small turbine with a real 20-yr field record. Marinized, corrosion-resistant, self-braking. Overkill on watts for us, but it is the *only* commercial unit whose durability isn't in question. |
| **2** | **Missouri Wind & Sun / Automaxx 400–600 W kits** | 400–600 W | Mid-tier US sellers with actual support and replaceable parts. Better than no-name, well short of Primus. | $300–500 | Decent bearings, real charge controllers, parts you can re-order. Blades and slip-rings are the wear items. Moderate life (5–10 yr) with maintenance. |
| **3** | **WATEBATH / OSKOPWRC / generic "600–800 W" die-cast kits** | Claimed 600–800 W | The better-built end of the cheap pile: die-cast aluminum bodies, fiberglass-nylon blades, bundled controller. Reviews call build quality "decent for the price." | $120–200 | Realistically ~150–250 W in useful wind and a **1–4 year** life. Buy only if you accept it as a consumable and keep spare blades. The controller is often the first thing to fail. |
| **—** | **Maglev "vertical" tower turbines** (Lbxlhr etc.) | Claimed 400 W–2 kW, "10–15 yr" | Marketed as maintenance-free maglev VAWTs. The maglev/no-yaw story is largely marketing; real output is a fraction of the claim. | $100–300 | **Avoid for a serious build.** Low, unproven output; the "lifespan" claims are not field-verified. Fine as a toy, not as a power source you depend on. |

**Commercial recommendation:** if a buyer insists on a bought turbine, the honest answer is **Primus AIR 40 or nothing** — it is the only one that satisfies "durable × locally-repairable (sealed, few parts, global spares)." But at $650–900 it dwarfs the entire rest of the Manatee's power kit to feed a 150 Wh/day load solar already covers. That economic absurdity is precisely what pushes the *right* answer toward the DIY route below.

---

## 2. WIND — the handmade / DIY route (the appropriate-tech heart)

This is where the north star actually lives. The lineage is real and load-bearing: **Hugh Piggott** (Scoraig, Scotland) has spent 40+ years refining a hand-built **axial-flux permanent-magnet (AFPM)** turbine specifically so that a non-specialist with scrap metal and hand tools can build a durable machine. **Wind Empowerment** — a global federation of NGOs — teaches the Piggott build across the Global South precisely because it is repairable in a village. And **William Kamkwamba** ("The Boy Who Harnessed the Wind") built a working windmill in Malawi at 14 from a bicycle dynamo, blue-gum poles, and scrapyard parts — the proof-of-concept for the entire "anyone can build one" thesis. This is the culture the Manatee should plug into, not the Amazon marketplace.

### 2a. The Piggott axial-flux PMG turbine — the gold standard

**What it is:** neodymium magnets resin-cast onto two steel rotor discs, spinning either side of a hand-wound copper-coil stator also set in resin. Rectified to DC for battery charging. No gearbox. The main bearing is **a scrap-car front wheel hub**; much of the steel is reclaimed; the blades are **hand-carved from wood**.

- **The manual:** *A Wind Turbine Recipe Book* by Hugh Piggott — a 65-page open plan covering **six sizes** (rotor diameters ~1.2 m up to ~4.8 m) for 12/24/48 V. **~US$23 posted**, ~$5 Kindle, or a free/cheap metric PDF. The single best ~$23 the kit could point a builder to.
- **Cost to build (small ~1.2–1.8 m "2F" size, right for us):** roughly **$150–400** in materials if buying magnets/wire new, far less with scrap steel and a junkyard hub. Wind Empowerment workshops routinely build these for a few hundred dollars.
- **Output:** the small sizes make on the order of **100–400 W in good wind** — *comfortably more than the Manatee's whole daily budget in a few breezy hours.* We would deliberately build the **smallest** size to keep mast-top mass (and capsize moment) down.
- **Durability:** this is the headline. Piggott's design is "well respected across the globe for its durability, simplicity and adaptability." No gearbox to strip, no electronics in the generator, bearings and blades are the only wear parts — **both village-replaceable.** A well-built one runs for a decade-plus. This is the *most* durable-and-repairable option in this entire document, commercial units included.
- **Buildability by a non-specialist:** moderate. It needs basic welding, coil-winding patience, and resin casting — a weekend workshop skill, not an engineering degree. This is exactly the skill Wind Empowerment transfers in a 1–2 week course. **It is buildable by a determined amateur; it is not plug-and-play.**

**What the kit would SHIP vs. what's built locally:**

| Ship in the kit (the irreplaceable core) | Build/source locally (the bulk & the tower) |
|---|---|
| **Neodymium magnets** (the one part you cannot make or easily buy in a village) | **Blades** — hand-carved from local wood (Piggott's plans) |
| **Enameled copper magnet wire** for the coils | **Rotor/stator steel discs & frame** — reclaimed/cut locally |
| **Rectifier bridge + dump-load controller + dump resistor** (see §2d — mandatory) | **Main bearing** — scrap-car wheel hub |
| **The Recipe Book** (or our condensed build sheet) | **Tower/mast** — local pipe, wood pole, or guyed scaffold (Kamkwamba used blue-gum poles) |
| Resin/casting epoxy (shelf-stable, hard to source remotely) | **Tail vane & furling** — sheet metal + the plans |

This split *is* the appropriate-tech thesis in hardware form: ship the atoms that are genuinely scarce and unmakeable locally (magnets, magnet wire, power electronics), and let sunlight, scrap, and a machete do the rest.

### 2b. Savonius vertical-axis from a 55-gallon drum (ties to our drum!)

The poetic option: the Manatee already has a **55-gallon drum** in its BOM, and the classic beginner wind project is a **Savonius VAWT cut from a 55-gallon drum** — split the cylinder lengthwise, offset the halves by a radius, cap with end plates, run a shaft through bearings. **~$100–250 in materials**, buildable from scrap with a jigsaw and drill, self-starting from any wind direction (no yaw), slow-turning and low-stress so it "doesn't go fast enough to fly apart" — inherently safe and durable.

**The honest catch — and it is fatal for direct generation:** a drum Savonius is a **torque** machine, not a **speed** machine. Its bare rotor turns far too slowly (and its Cp/aerodynamic efficiency is low, ~15%) to spin a PMG alternator directly — you'd need a gear/pulley step-up (3–10×), which adds friction, a wear point, and complexity that undercuts the whole "nothing to break" appeal. Raw electrical output of naive builds is often cited at a near-useless **1–10 W**.

**Verdict:** the Savonius is a **wonderful teaching build and a beautiful brand tie-in** (drum → turbine → same machine), but it is **not a serious charging source** for the Manatee without a step-up drive we don't want on a floating raft. Keep it as an optional "Tier-3 experiment / educational module," not the recommended generator. If someone wants VAWT charging, they should belt it up to the same Piggott-style PMG — at which point they've done most of the Piggott work anyway.

### 2c. PVC-blade turbines (the "poor-man's blades")

A common Global-South shortcut is carving turbine blades from a **large-diameter PVC pipe** cut lengthwise into airfoil-ish sections — near-free, weatherproof, and workable with a hacksaw and rasp. They pair naturally with a scrap-motor or PMG generator. **Honest assessment:** PVC blades work and are cheap, but they're aerodynamically crude (lower efficiency than carved wood), can go brittle under prolonged UV, and flex/deform at higher rpm. They are a fine **stopgap / first-build** blade, but Piggott's **carved-wood** blades are more durable and efficient for a machine you want to last years. Ship neither — blades are the *definitional* local-build part; just point to both methods in the plans.

### 2d. The non-negotiable safety rule for ANY wind option

Repeating the Electronics Guide because it kills turbines and starts fires: **a turbine must NEVER spin into an open circuit.** Unloaded, it overspeeds and destroys itself (and adds capsize-inducing mast-top mass). Any wind fit therefore *requires*, in the kit: **turbine → rectifier (if 3-phase AC) → diversion/dump-load controller → dump resistor bank** sized to absorb full output when the battery is full. The Primus AIR 40 has this braking built in; a DIY Piggott build does **not** and must ship with the dump electronics. This is the one place wind adds real electronic complexity over solar.

---

## 3. RECOMMENDATION — should the kit include a turbine?

**Recommendation: the kit does NOT include a whole turbine. It offers an optional "Wind Pack" of the irreplaceable core, and points the builder at the Piggott plans.** Reasoning, scored on the four axes:

1. **Amortization:** A whole commercial turbine (Primus $650–900) costs **more than the entire rest of the power kit combined**, to feed a load solar already covers. That fails "fast-to-amortize" badly. A **Wind Pack** (magnets + magnet wire + rectifier + dump controller + dump resistor + build sheet) is perhaps **$60–150** — and the builder adds only local scrap and labor. That amortizes fast because most of the cost is converted into free local materials and sweat.
2. **Durability:** A locally-built Piggott turbine, with village-replaceable blades and bearings and no gearbox, is *more* durable-in-context than a sealed commercial unit whose one failed proprietary part strands it. Local repairability **is** durability in the Global South.
3. **Buildability:** Shipping the scarce atoms (magnets, wire, power electronics) and letting the builder make blades/hub/tower/frame is the exact model Wind Empowerment has proven works with non-specialists.
4. **Optionality:** Solar alone closes the budget. Wind should never be a single point of failure or a mandatory cost. Making it an **optional pack** keeps the base kit cheap and lets windy/cloudy sites add resilience.

**Concrete spec — the optional "Manatee Wind Pack":**
- Neodymium magnet set (sized for the smallest Piggott rotor)
- Enameled copper magnet wire (coil quantity)
- Bridge rectifier + **dump-load controller + dump resistor bank** (the safety-critical, un-improvisable bit)
- Casting epoxy (shelf-stable)
- Condensed Manatee-specific build sheet + link to *A Wind Turbine Recipe Book*
- **Explicitly NOT shipped:** blades (carve wood/PVC locally), frame/discs (reclaimed steel), bearing (scrap hub), tower (local pole/pipe)

This is the purest expression of the north star: **ship the ~$100 of atoms a village can't make; let the village make the rest.** For a buyer who just wants it to work with zero fabrication, the fallback is "buy a Primus AIR 40" — sold as the premium, no-build option, not the default.

---

## 4. SOLAR — cheap and durable over efficient (the workhorse)

Solar is the Manatee's primary and, honestly, sufficient source. The good news: **PV is now so cheap that the appropriate-tech and the economic answers converge** — you do not need to sacrifice durability to hit a low price.

### What the Manatee actually needs

- **Baseline: one 100 W 12 V panel.** The Electronics Guide's baseline is 45 W (~120–170 Wh/day — closes the budget only marginally, in daylight, as a batch process) but **recommends 100 W** (~300–400 Wh/day) for real margin against clouds and dawn/dusk. **Fit 100 W.** It's the single highest-leverage upgrade in the whole electrical system and costs ~$60–110.
- That is *one panel.* The Manatee is not a house; there is no panel array to optimize. Which means the efficiency-vs-durability tradeoff is almost moot — a 100 W panel is a 100 W panel whether it's 18% or 21% efficient; on a raft with room to spare, **buy the rugged cheap one.**

### Cheap and durable beats efficient — the honest tradeoff

- **New panel $/W (2026):** polycrystalline ~**$0.25/W**, value-mono **$0.30–0.50/W**. A new 100 W rigid panel lands around **$60–110**. Poly is slightly cheaper and slightly less efficient per area — irrelevant here where area isn't constrained. **Poly or value-mono, rigid, glass-front, aluminum-framed** is the durable-cheap sweet spot: 20–25 year life, IEC-rated, corrosion-resistant frame.
- **Used / salvage panels:** decommissioned utility/residential panels sell for as little as **~$0.12/W** (and older 200–250 W units are near-worthless on the resale market → cheap to acquire). A salvaged panel with 15+ years of remaining life is the **cheapest durable watt on earth** and squarely on-thesis: rescue a "waste" panel, bank free sun. Caveat: inspect for delamination, cracked cells, and corroded junction boxes — a cracked panel is a slow failure, not a bargain.
- **What to AVOID:** cheap **flexible/ETFE "marine" panels.** They *look* right for a boat, but they delaminate, hot-spot, and yellow within 2–5 years — the classic "fragile premium" trap. A rugged $70 rigid glass panel that lasts 20 years beats a $120 flexible one that dies in three. Rigid glass, always. (Mount it to shed water and take spray; it's already the most weather-hardened part of the machine.)

**Solar recommendation:** **one 100 W rigid poly (or value-mono, or salvaged) glass-framed 12 V panel, ~$60–110 new or ~$15–40 salvaged.** Do not chase efficiency or "marine" flex panels. This single choice, plus the MPPT controller already in the Electronics Guide, is the entire required generation system. Everything wind is optional on top.

---

## 5. AMORTIZATION VIEW (approximate — for a resilience buyer, not grid arbitrage)

Framed honestly per the Bio-Battery Thesis: **this is not a cents-per-kWh play** — round-trip efficiency is low and PV+battery banks more sun per m². The payback that matters is *independence and stored, dispatchable energy you fully own*, charged from free surplus (sun + a sick pond's nutrients). With that framing:

**Approximate power-kit cost (the generation + store + protect subset):**

| Item | Approx cost |
|---|---|
| 100 W rigid panel (new) — or ~$15–40 salvaged | **$60–110** |
| MPPT charge controller (Victron 75/15) | ~$110 |
| 12 V 50 Ah LiFePO4 battery (the buffer/store) | $150–300 |
| Fuse + disconnect + LVD + wiring + safety skeleton | ~$150–250 |
| **Solar-only power kit subtotal** | **≈ $470–770** |
| *Optional Wind Pack (magnets/wire/rectifier/dump) + local build* | *+$60–150 atoms + scrap/labor* |
| *Optional whole Primus AIR 40 instead* | *+$650–900* |

**How fast does the banked energy pay it back?** Frame it as *stored dispatchable energy owned*, not dollars saved:

- The generation *hardware* (100 W panel) is a **rounding error** — ~$60–110 — and harvests **~0.3–0.4 kWh/day** of electrical energy essentially forever. In pure electricity terms the panel pays for itself in energy value within a season or two; that's not the interesting number.
- The *interesting* amortization is the **bio-battery**: the panel + pump spend ~150 Wh/day to run the reactor, which (thesis, **UNPROVEN pending the ~$100 bench test**) banks algae oil/wax at **~10,000–12,000 Wh/kg raw thermal** — a store that **doesn't self-discharge, needs no BMS, and keeps for years.** If the yield closes, the machine converts a near-free panel + free nutrients into a **shelf-stable energy reserve** whose *value per kg dwarfs the battery it would take to store the same energy* (~15–25× a Li-ion pack after conversion losses; ~40–100× for direct heat/light/cooking).
- **Independence framing:** for the off-grid homestead or remote community, the payback isn't grid arbitrage — it's *never hauling fuel again.* The power kit is a **one-time ~$500–800 purchase** (most of it the battery and safety wiring, not the generation) that turns sunlight, wind, and a sick pond into a barrel of energy you own and burn on your schedule. Against the recurring cost and supply-chain dependence of hauling diesel or maintaining a big battery bank, that amortizes not in cents-per-kWh but in **autonomy per dollar** — which is the only metric the resilience buyer actually cares about.

*All figures approximate (2026 US retail); the bio-battery yield that anchors the deep amortization story remains the one unproven number, resolvable by the ~$100 oil-out-per-Wh-in bench test flagged in the thesis.*

---

## Summary of recommendations

| Question | Answer |
|---|---|
| **Primary source?** | **One 100 W rigid glass 12 V panel** (poly, value-mono, or salvaged). ~$60–110 new. Rugged-cheap beats efficient. Avoid flexible/marine panels. |
| **Include a whole turbine in the base kit?** | **No.** Solar closes the ~150 Wh/day budget alone; a whole turbine costs more than the rest of the kit. |
| **Best commercial turbine if a buyer wants one?** | **Primus AIR 40** (~$650–900) — the only small turbine with a real durability record; self-braking. Sold as the premium no-build option. |
| **The appropriate-tech turbine answer?** | **Optional "Wind Pack": ship magnets + magnet wire + rectifier + dump controller + build sheet (~$60–150); builder makes blades/hub/frame/tower locally** from the Piggott *Recipe Book* ($23). Most durable & repairable option in context. |
| **The drum Savonius?** | Beautiful brand tie-in and teaching build, but too slow-turning to charge directly — **educational module, not a generator.** |
| **Any wind = ?** | Mandatory dump-load controller + resistor. Never spin a turbine open-circuit. |

---

*Sources: [Primus AIR 40 (Practical Preppers)](https://practicalpreppers.com/product/air-40-turbine/), [Primus AIR 40 (Solacity)](https://www.solacity.com/product/primus-air-40/); [small-wind scam discussion (DIY Solar Forum)](https://diysolarforum.com/threads/small-wind-turbines-no-longer-worth-it.16527/), [northernarizona-windandsun forum](https://forum.solar-electric.com/discussion/3638/small-windpower-a-scam-survey-says-so/p2); [Piggott Turbine (Wind Empowerment)](https://windempowerment.org/research-and-devlopment/small-wind-systems/the-piggott-turbine/), [A Wind Turbine Recipe Book (Scoraig)](https://scoraigwind.co.uk/a-wind-turbine-recipe-book/); [55-Gallon Drum Turbine (Instructables)](https://www.instructables.com/55-Gallon-Drum-Turbine/), [Savonius VAWT technical guide (NovaFuture)](https://novafuture.org/data-sheets/clean-energy/wind-turbines/complete-technical-guide-to-vertical-axis-savonius-wind-turbines/); [Solar cost per watt 2026 (Solar.com)](https://www.solar.com/learn/solar-panel-cost/), [used panel pricing (Sunhub)](https://www.sunhub.com/blog/solar-panel-price-per-watt/).*
