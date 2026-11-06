# Primary Evidence Index & Provenance Guide

This directory holds the primary historical lab reports, chemical engineering calculations, process schematics, naval architecture blueprints, and field media from Rudolph ("Rudy") Behrens' archive (`Aeolus Group` / `B.E.A.R. Oceanics` / `Solaris Cybernetics`, 2003–2016).

Every file below is indexed with its **date**, **author/lab**, **what it documents**, and **what it does NOT prove** (its epistemic boundary).

---

## 1. Third-Party Laboratory Assays (`lab-assays/`)

| File | Date | Lab / Author | What It Documents (`[DOCUMENTED]`) | Epistemic Boundary (What It Does NOT Prove) |
| :--- | :---: | :--- | :--- | :--- |
| [`Intertek_Caleb_Brett_ASTM_D4052_D240_Assay_Report_2006.pdf`](lab-assays/Intertek_Caleb_Brett_ASTM_D4052_D240_Assay_Report_2006.pdf) | May 2006 | **Intertek Caleb Brett** (Accredited petroleum testing lab) | Certifies a submitted bio-fuel sample at **28.5° API gravity** (ASTM D4052) and **17,137 BTU/lb / 126,197 BTU/gal** (39.9 MJ/kg, ASTM D240). | Sample was submitted by the inventor (chain of custody from raw algae to vial was not witnessed by Intertek). D4052/D240 measure density and heat of combustion only, not molecular composition. |
| [`Atlantic_Analytical_Lab_GCMS_Combustion_Report_2007.pdf`](lab-assays/Atlantic_Analytical_Lab_GCMS_Combustion_Report_2007.pdf) | Mar 23, 2007 | **Atlantic Analytical Laboratory** (AAL #2827, Ralph J. Ciotti, for *The Aeolus Group LLC*) | Thermo-oxidative combustion characterization at 700°F in air via **GC-TCD/FID, GC-SCD, and GC/MS**: **99.01% w/w sample weight loss**, **0.09% w/w ash residue**, **128 ppb v/v total sulfur** ($\text{H}_2\text{S} = 28\text{ ppb}$, $\text{COS} = 100\text{ ppb}$), plus headspace combustion/pyrolysis fragments ($\text{C}_3\text{–C}_{11}$ unsaturated methyl esters, alkenes, aromatics). | Analyzes the *gaseous effluent after heating at 700°F in air* (thermo-oxidative stress), not a direct liquid-phase GC-MS or ASTM D86 boiling curve of the unburned oil. Note the presence of $\text{C}_3\text{–C}_{11}$ methyl esters of mono-unsaturated carboxylic acids in the recovered fraction. |
| [`Bio_Fuel_Ultimate_Analysis_Test_2008.pdf`](lab-assays/Bio_Fuel_Ultimate_Analysis_Test_2008.pdf) | Oct 2008 | **Independent Analytical Lab** | Elemental / ultimate analysis (Carbon, Hydrogen, Nitrogen, Sulfur, Ash, and Heating Value) of submitted biofuel sample. | Same chain-of-custody boundary: certifies the physical properties of the submitted sample, not the closed-loop energy input required to make it. |
| [`Rutgers_John_Kraeuter_Algal_Weight_Lab_Letter_2006.pdf`](lab-assays/Rutgers_John_Kraeuter_Algal_Weight_Lab_Letter_2006.pdf) | Sep 2006 | **Dr. John N. Kraeuter** (Rutgers University, Haskin Shellfish Research Laboratory) | Independent laboratory drying and gravimetric dry-weight measurement of algal biomass samples provided by Behrens. | Validates biomass sample concentration/dry weight; does not test the cavitation nozzle or fuel conversion. |

*(Note: A fifth third-party assay, the **Sept 23, 2012 B.E.A.R. Group Synthetic Fuel Analysis**, is transcribed and analyzed in full in [`../02-BUILD-MANUAL/05-lab-assays-and-standards.md`](../02-BUILD-MANUAL/05-lab-assays-and-standards.md) and [`../01-SYSTEMS/02-cavitation-reactor/04-audit-conversion-science.md`](../01-SYSTEMS/02-cavitation-reactor/04-audit-conversion-science.md): **ASTM D4052 = 32.71° API**, **ASTM D240 = 18,254 BTU/lb / 134,258 BTU/gal**. Note that the words "BIO DIESEL" on that form are the submitter's sample label, not a lab speciation finding.)*

---

## 2. Engineering Calculations & Process Notes (`engineering-calcs/`)

| File | Date | Author | What It Documents | Key Engineering Takeaway |
| :--- | :---: | :--- | :--- | :--- |
| [`Dr_William_Thomson_1MW_Wind_Electrolysis_Ethanol_Report_2003.pdf`](engineering-calcs/Dr_William_Thomson_1MW_Wind_Electrolysis_Ethanol_Report_2003.pdf) | Dec 4, 2003 | **Prof. William J. Thomson** (PhD Chemical Engineer, commissioned by B.E.A.R.) | Formal 6-page chemical engineering mass-and-energy balance for Behrens' original 1 MW offshore wind-turbine + water electrolyzer + cryogenic $\text{CO}_2$ air separator + 800 psig catalytic reactor (`US 7,302,903`). | **The smoking gun for why the project pivoted to algae:** Cryogenic $\text{CO}_2$ separation consumed **884.6 kW (88.5%)** of the 1 MW wind turbine, leaving only **115 kW (11.5%)** for the Stuart Energy electrolyzer. Worse, thermodynamic equilibrium at 800 psig / 374°C yielded **60% methane gas ($\text{CH}_4$)** and only ~4 gal/day of actual alcohol. |
| [`LVKNprocess.txt`](engineering-calcs/LVKNprocess.txt) & [`LVKN_low_velocity_kinetic_nozzle_process.pdf`](engineering-calcs/LVKN_low_velocity_kinetic_nozzle_process.pdf) | Nov 2008 | **Rudolph Behrens** | The core derivation of the **"5.34% conversion energy cost"** claim: Euler/Bernoulli acceleration of 1 gal to $100\text{ ft/s}$ at $150^\circ\text{F}$ ($0.06\text{ hp}\cdot\text{gal} = 204.84\text{ BTU}$) divided by an assumed **3% conversion per pass** ($6,828\text{ BTU/gal}$) against $127,000\text{ BTU/gal}$ output. | Arithmetically self-consistent, but rests on an unmeasured **3%/pass** assumption and omits multi-pass recirculation losses, dewatering, and reaction enthalpy. See [`../00-OVERVIEW/04-three-unmeasured-keystones.md`](../00-OVERVIEW/04-three-unmeasured-keystones.md). |
| [`9x9HVO_process.txt`](engineering-calcs/9x9HVO_process.txt) & [`Hydrous_Pyrolysis_System_summary.pdf`](engineering-calcs/Hydrous_Pyrolysis_System_summary.pdf) | Nov 2008 | **Rudolph Behrens** | Describes the 2-tank growth/concentration loop (venturi $\text{CO}_2$ aeration to >6% solids), 300-psi pump + cavitating nozzle hydrous pyrolysis, gravimetric stratification, displacement into a collection bladder, and anaerobic decomposition of residual biomass for $\text{CO}_2$ recycle. | Shows that concentration to ~6% solids happens *before* the high-pressure cavitation loop, and separation is passive gravity stratification + water-level displacement. |
| [`S3algaeRecipe.txt`](engineering-calcs/S3algaeRecipe.txt) | ~2010 | **Rudolph Behrens** | Lists the "S3" polyculture blend: *Spirulina*, *Azolla*, *Gracilaria*, *Lemna minor* (duckweed), and *Wolffia*. | Precursor to the 3-species freshwater polyculture (microalgae + *Lemna* duckweed + microbial biofilm) analyzed in [`../01-SYSTEMS/01-ecology-and-dewatering/`](../01-SYSTEMS/01-ecology-and-dewatering/). |
| [`9rules_living_machines_design_principles.pdf`](engineering-calcs/9rules_living_machines_design_principles.pdf) | May 2012 | **Rudolph Behrens** (adapting John Todd's *Living Machines*) | Ecological engineering precepts governing multi-species aquatic bioreactors (microbial reservoirs, mineral diversity, light gradients, trophic exchange). | Explains why the pond/bioreactor uses a polyculture rather than a sterile monoculture photobioreactor. |
| [`handwritten-calcs/AlgaeX_001.jpg`](engineering-calcs/handwritten-calcs/) – `AlgaeX_013.jpg` | 2008–2012 | **Rudolph Behrens** | 13 pages of scanned handwritten engineering notes, pump curves, buoyancy sizing, and cavitation calculations. | Primary-source record of the inventor's sizing math. |

---

## 3. Process Diagrams & Historical Naval Architecture (`process-and-naval-drawings/`)

| File | Date | What It Shows | Why It Matters |
| :--- | :---: | :--- | :--- |
| [`PelagosPrcsDgm_V1_Electrolysis.jpg`](process-and-naval-drawings/PelagosPrcsDgm_V1_Electrolysis.jpg) | ~2008 | **Version 1 of the Pelagos Process Diagram.** Step 2 reads: *"An electric current ruptures the cell walls and make H2"* (electrolysis), followed by Step 3: *"The hydrogenated lipids are passed through a cavitating nozzle."* | Documents the transitional bridge between the 2006 electrolysis patent (`US 7,750,494`) and the later cavitation-only design. |
| [`PelagosPrcsDgm_V2_Cavitation.jpg`](process-and-naval-drawings/PelagosPrcsDgm_V2_Cavitation.jpg) | ~2010 | **Version 2 of the Pelagos Process Diagram.** Step 2 swaps out electrolysis for *"A cavitating nozzle separates & hydrogenates the lipids,"* while Step 3 still calls them *"the hydrogenated lipids."* | Shows how the "hydrogenation" terminology survived into the cavitation-only era after the physical electrolyzer was removed from the BOM. |
| [`BEAR_Fuel_3percent_render.jpg`](process-and-naval-drawings/BEAR_Fuel_3percent_render.jpg) | ~2010 | Photograph/graphic of a Ball jar containing 3-5/8 inches of green liquid topped by a 1/8-inch floating layer labeled **"3 percent"**. | Visual origin of the load-bearing "3% conversion per pass" assumption ($0.125 / 3.625 \approx 3.4\%$). |
| [`BEAR_cavitation_nozzle_close_up.jpg`](process-and-naval-drawings/BEAR_cavitation_nozzle_close_up.jpg) | ~2011 | Photograph of the physical machined stainless-steel cavitation vessels, swaged compression fittings, and hard-plumbed tubing on a workbench. | Confirms that physical stainless cavitation hardware was machined and plumbed at bench scale. |
| [`ocean-gypsy-2004-naval-architecture/`](process-and-naval-drawings/ocean-gypsy-2004-naval-architecture/) | 2004 | 6 naval architecture blueprints and general specifications by **NDI Engineering** (`NDI 1157-001`) for the 2004 *Ocean Gypsy* wind-electrolysis ship. | Professional naval engineering package from the 2004 `US 7,302,903` seawater-electrolysis era. |

---

## 4. Field Media (`field-media/`)

| File | Date | Provenance & Description |
| :--- | :---: | :--- |
| [`manatee-pond-truesource.mp4`](field-media/manatee-pond-truesource.mp4) | 2014 | **26.6-second continuous handheld video (640×360)** filmed at a Pennsylvania farm pond. Shows the working PVC pontoon prototype floating on muddy pond water with its vertical-axis Lenz turbine spinning in the wind, solar panel on the right, and red-lidded separation jar, clear electronics box, and silver pump in the center. |
| [`pond-machine-2015-noclaims.jpg`](field-media/pond-machine-2015-noclaims.jpg) | Dec 2015 | Photograph of the small working pond prototype (~15 W wind rotor, ~15 W solar panel, 1/10 HP pump, bucket + jar separator) with the inventor's unverified yield captions cropped out. |
| [`duckweed-pond-noclaims.jpg`](field-media/duckweed-pond-noclaims.jpg) | 2015 | Photograph of the dense *Lemna minor* (duckweed) surface mat on the test pond (uncaptioned). |
| [`dome-and-greenhouse/`](field-media/dome-and-greenhouse/) | 2009–2012 | **17 genuine construction and operation photographs** of the timber geodesic dome erection, indoor algae pond inside the dome, and commercial greenhouse paddlewheel raceway tanks. |
