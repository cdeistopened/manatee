# 02 — Hull Architecture & Pontoon Sizing

*Hydrodynamic balance, displacement calculations, and construction of the standardized 4-pontoon catamaran hull.*

---

## 1. Hull Configuration: Symmetric Catamaran

The Manatee utilizes a quad-pontoon catamaran layout (two parallel pairs) to maximize roll stability and provide a stable central deck platform for the fluid processing equipment and wind rotor mast:

```
        ◄──────────────────── 2.26 m Length ────────────────────►
 ┌───────────────────────────────────────────────────────────────────┐
 │ PONTOON A1 (Outer Left) 4" PVC                                    │
 └───────────────────────────────────────────────────────────────────┘
 ┌───────────────────────────────────────────────────────────────────┐
 │ PONTOON A2 (Inner Left) 4" PVC                                    │
 └───────────────────────────────────────────────────────────────────┘
      │                                                         │
      │ ◄────────── Central Processing Deck & Pump ──────────►  │
      │                                                         │
 ┌───────────────────────────────────────────────────────────────────┐
 │ PONTOON B2 (Inner Right) 4" PVC                                   │
 └───────────────────────────────────────────────────────────────────┘
 ┌───────────────────────────────────────────────────────────────────┐
 │ PONTOON B1 (Outer Right) 4" PVC                                   │
 └───────────────────────────────────────────────────────────────────┘
```

---

## 2. Buoyancy & Displacement Sizing

### A. Total Dry Machine Mass
- Frame & Hardware: $14.5 \text{ kg}$
- Pontoons (4 × 4" PVC × 2.26m): $18.2 \text{ kg}$
- Diaphragm Pump & Motor: $4.8 \text{ kg}$
- Battery Buffer (12V 20Ah LiFePO4): $2.8 \text{ kg}$
- Solar Module (50W–100W): $6.2 \text{ kg}$
- Wind Rotor Mast & Hub: $5.5 \text{ kg}$
- Reactor Nozzle, Manifold & Hoses: $3.8 \text{ kg}$
- Concentrated Product Payload (Max): $15.0 \text{ kg}$
- **Total Operational Wet Mass**: $\approx \mathbf{70.8 \text{ kg}}$

### B. Displacement Capacity
For four 4" (nominal outer diameter $D = 0.1143 \text{ m}$) PVC pipes of length $L = 2.26 \text{ m}$:
$$\text{Total Submerged Volume} = 4 \times \pi \times \left(\frac{0.1143}{2}\right)^2 \times 2.26 = 4 \times 0.01026 \times 2.26 = 0.0927 \text{ m}^3$$
$$\text{Total Buoyancy Force} = 0.0927 \text{ m}^3 \times 1,000 \text{ kg/m}^3 = \mathbf{92.7 \text{ kg}}$$

- **Operating Draft**: At $70.8 \text{ kg}$ total load, the hull operates at **$76\%$ displacement depth** (~3.4" waterline), leaving 1"–1.5" freeboard to prevent deck swamping in chop.
- **For larger capacity (55-gal drum variant)**: Standard 6" PVC pipe provides **$208.5 \text{ kg}$** total buoyancy force, allowing up to $130 \text{ kg}$ of stored wax payload.
