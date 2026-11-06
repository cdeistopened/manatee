# 03 — Reaction Propulsion & Roaming Dynamics

*How the submerged cavitation discharge doubles as an un-cloggable waterjet thruster to roam and aerate the entire pond.*

---

## 1. Dual-Purpose Fluid Jet Propulsion

Instead of a dedicated trolling motor or propeller that constantly fouls on surface vegetation, the Manatee uses **reaction thrust** from its own pump discharge:

```
[ Surface Skimmer Intake ] ──► [ 12V Diaphragm Pump ] ──► [ Cavitation Nozzle ]
                                                                   │
                                                                   ▼
                                                       [ Submerged Jet Discharge ]
                                                                   │
                                                                   ▼
                                                       Thrust Force F = ṁ · v_exit
                                                       (Pushes Robot Forward)
```

$$\text{Thrust Force } F = \dot{m} \cdot v_{\text{exit}} = \rho \cdot Q \cdot \left(\frac{Q}{A_{\text{nozzle}}}\right)$$

- **Volumetric Flow Rate ($Q$)**: $3.0 \text{ GPM} \approx 0.000189 \text{ m}^3\text{/s}$
- **Discharge Orifice ($d = 3/8" \approx 0.0095 \text{ m}$)**: $A = 7.09 \times 10^{-5} \text{ m}^2$
- **Exit Velocity ($v_{\text{exit}}$)**: $\approx 2.67 \text{ m/s}$
- **Net Reaction Thrust ($F$)**: $\approx \mathbf{0.51 \text{ Newtons}}$

In calm water, $0.5 \text{ N}$ of continuous thrust easily overcomes the hull's low skin friction ($C_d \approx 0.04$), moving the vessel at a slow, continuous grazing velocity of **$0.15 \text{ to } 0.35 \text{ knots}$ ($0.08–0.18 \text{ m/s}$)**.

---

## 2. Roaming & Benthic Aeration Benefits

1. **Continuous Surface Sweeping**: Slow grazing allows the surface skimmer to harvest new patches of duckweed and microalgae without outrunning the biomass intake rate.
2. **Benthic Aeration**: The downward-angled discharge jet pushes cavitated, oxygenated surface water into the stagnant deeper layers of the pond, preventing thermal stratification and stimulating aerobic decomposition of bottom muck.
3. **Zero Fouling**: Because the jet is a pressurized output tube without spinning exposed blades, pond weeds and duckweed flow harmlessly past the hull.
