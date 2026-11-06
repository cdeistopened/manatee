# 02 — Kinetic Nozzle Geometry & Jet Eductor Mixing

*Machining dimensions, ceramic insert specifications, and hydraulic jet eductor integration.*

---

## 1. Nozzle Geometry & Orifice Sizing

The kinetic nozzle assembly holds a high-hardness ceramic or tungsten carbide orifice disc inside a standard 316 stainless steel compression tee:

```
                  ◄────────────── 2.50" Length ──────────────►
             ┌───────────────────────────────────────────────────┐
  1/4" NPT   │                                                   │  3/8" Barb
  Inlet ────►│   [ O-Ring ]  [ Ceramic Disc ]  [ Cavitation Zone ]│────► Discharge
 (From Pump) │               (d = 0.030")                        │
             └───────────────────────────────────────────────────┘
```

- **Inlet Thread**: 1/4" or 3/8" Female NPT (rated to 1,000 psi).
- **Orifice Disc**: Alumina Ceramic ($Al_2O_3$, Mohs 9 hardness) or Silicon Carbide ($SiC$). Ceramic provides **20–30× the abrasive lifespan** of 316 stainless steel against diatomaceous algae silica shells.
- **Orifice Diameter ($d$)**: $0.028" \text{ to } 0.035"$ ($0.71–0.89 \text{ mm}$), sized to maintain $250–350 \text{ psi}$ backpressure at a $1.8–2.5 \text{ GPM}$ pump flow rate.

---

## 2. The Jet Eductor Pre-Mixer

To maximize cell concentration prior to the high-pressure pump, a Venturi jet eductor (Rudy's BOM specification: `AZ_Tank_Eductor_2_web.jpg`) entrains secondary concentrated biomass slurry into the primary skimmer flow:

```
Primary Water Feed (From Bilge Pump)
               │
               ▼
   ┌───────────────────────┐
   │ MOTIVE JET NOZZLE     │ Surging Velocity creates Vacuum
   └───────────┬───────────┘
               │
   ◄───────────┴───────────► Secondary Suction (Dense Duckweed-Algae Slurry)
               │
               ▼
   ┌───────────────────────┐
   │ MIXING VENTURI TUBE   │ Homogenized Micro-Emulsion Feed
   └───────────┬───────────┘
               │
               ▼
   To High-Pressure Cavitation Pump
```
