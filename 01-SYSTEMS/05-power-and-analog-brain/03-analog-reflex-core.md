# 03 — Analog Reflex Core & Unpluggable Observer

*The survival control architecture: why the machine's critical operational loop is pure analog reflex, and digital microcontrollers exist only as an optional observer.*

---

## 1. The Core Philosophy: Analog Survival Loop

Digital microcontrollers (Arduino, ESP32, Raspberry Pi) are vulnerable to moisture ingress, software hangs, voltage brownouts, and firmware corruption. If an off-grid machine relies on software to avoid drowning its battery or burning its motor, it will eventually fail.

The Manatee separates control into two strictly isolated tiers:
1. **Tier 1: Analog Reflex Core (The Unbreakable Brain)**:
   - Built entirely from discrete analog components (comparators, Zener diodes, relays, and BEAM phototropism circuits).
   - Functions autonomously without software, clock signals, or boot cycles.
   - Handles low-voltage disconnect (LVD), over-current protection, and automatic sun-seeking roaming.
2. **Tier 2: The Unpluggable Observer (Digital Telemetry)**:
   - An optional ESP32 / LoRa module that monitors voltage, current, GPS, and water clarity.
   - **Completely isolated from the power control loop**: if the observer is unplugged, soaked in water, or smashed, the machine continues running without interruption.

```
                      12V SOLAR PANEL / BATTERY
                                  │
                                  ▼
┌──────────────────────────────────────────────────────────────────┐
│ TIER 1: ANALOG REFLEX CORE (Zero Software / Hardware Hardened)   │
│ • LM393 Comparator Voltage Monitor                              │
│ • Hard Low-Voltage Cutoff Relay (< 11.8V disconnect, > 12.8V on) │
│ • Dual Cadmium-Sulfide (CdS) BEAM Phototropism Steering Circuit │
└─────────────────────────────────┬────────────────────────────────┘
                                  │
                                  ▼
                         [ 12V DIAPHRAGM PUMP ]
                                  │
                                  │ (Passive Optoisolated Tap)
                                  ▼
┌──────────────────────────────────────────────────────────────────┐
│ TIER 2: UNPLUGGABLE OBSERVER (Optional Telemetry / LoRa)         │
│ • ESP32 / INA219 Current Sensor / GPS Tracker                    │
│ • Transmits daily yield and water quality to home base           │
│ • *Can be pulled out or destroyed with zero effect on machine*   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 2. BEAM Analog Phototropism (Sun Seeking)

The vessel naturally steers toward the brightest, most productive algae blooms using a dual-photodiode BEAM circuit:
- Two CdS photoresistors angled left and right detect sunlight gradient.
- The analog comparator biases a small auxiliary trim jet or rudder flap toward the sunniest patch of the pond, ensuring maximum solar charging and peak photosynthetic biomass intake.
