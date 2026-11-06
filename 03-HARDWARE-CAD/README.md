# Manatee Clean-Room Parametric CAD & 316-SS Kinetic Nozzle Studies

All 3D models in this directory are **100% original procedural clean-room CAD builds** created in Blender Python (`build_detail.py`), licensed under **CERN-OHL-S-2.0 / CC-BY-SA-4.0**. All geometry is in metres (`+X` starboard, `+Y` forward, `+Z` up).

## Included 3D Models (`models/`)

1. **`cleanroom.blend` / `cleanroom.glb` / `cleanroom.png`** (`origin = "cleanroom-parametric-2026-10-15"`):
   - 22 selectable groups across all 7 subsystems, matching the `2.26 × 3.20 × 1.24 m` (`[2.2629, 3.2040, 1.2357] m`) machine envelope:
   - **Flotation (`flotation`)**: Four Schedule-40 5-in PVC pontoon tubes (`OD = 0.1321 m`, `length = 3.1753 m`) with domed slip end-caps, coupling shoulders, and 8 stainless band-clamp saddle mounts (`cr-pontoon-clamps`).
   - **Structure (`structure`)**: Fore/aft and port/starboard 53 mm square-section perimeter rails, 4 corner Schedule-80 cross-socket collars (`cr-frame-sockets`), planar X-braced + diamond deck truss (`cr-deck-cross-members`) with central circular mast-step hub, and 0.14 m square mast column (`cr-mast-tube`).
   - **Rigging (`rigging`)**: Inner and outer 4-way diagonal 316-SS mast stay assemblies (`cr-mast-stays-inner`, `cr-mast-stays-outer`) with upper square mast collar rings and inline Suncor-class jaw-jaw turnbuckle bodies.
   - **Propulsion (`propulsion`)**: Port and starboard submerged Rule 2000-class marine bilge thrusters (`cr-bilge-pumps-pair`) at `x = ±0.96 m, y = -0.6428 m, z = -0.0777 m` with slotted blue strainers, white/red motor housings, and aft-directed 29 mm (1-1/8") water-jet discharge nozzles.
   - **Fluid & Cavitation Reactor (`fluid`)**: Central submerged priming cartridge (`cr-bilge-pump-cartridge-centre`), 300-psi 12VDC high-pressure deck feed pump (`cr-pump-deck`), **inline 4-port Venturi Eductor + 4.20-in 316-SS 7-bore Kinetic Cavitation Nozzle (`cr-eductor-nozzle`)**, and aft-starboard separator/decant drum (`cr-vessel-squat-cylinder`).
   - **Power (`power`)**: Forward `2.0655 × 0.5192 m` flexible marine monocrystalline solar array (`cr-solar-panel`) with silver busbars and junction box, plus sealed deck supercapacitor / LiFePO4 buffer module (`cr-capacitor`).
   - **Wind (`wind`)**: Three-wing cycloidal/J-profile **Lenz-2 VAWT rotor & sealed masthead PMG alternator** (`cr-rotor-lenz-masthead`, `z = 0.6756..1.0727 m`).
2. **`kinetic-nozzle.blend` / `kinetic-nozzle.glb` / `kinetic-nozzle.png`**:
   - Parametric 3D engineering study realized directly from the original DXF drawings in `nozzle-dxf/`:
   - `kn-disc-420`: Flagship **4.20-in OD × 4.20-in long 316-SS Kinetic Nozzle Cylinder** (`KineticNozzle1.DXF`, 106.68 mm OD × 106.68 mm length) Boolean-drilled with the 7-bore tetrahedral vortex cluster around the `0.73 in` (18.54 mm) pitch circle (one central `0.25 in` bore, three outer `0.25 in` primary bores at `90°/210°/330°`, and three inner `0.16 in` interstitial bores).
   - `kn-disc-5gpd`: **5-GPD 1.06-in OD × 1.06-in long 316-SS Nozzle Cartridge** (`KineticNozzle5gpd.dxf`, 26.92 mm OD, `0.20 in` pitch circle, `0.06 in` primary and `0.04 in` secondary bores) placed alongside the 4.20-in unit for direct 1:4 scale comparison.
   - `kn-eductor-body`: **180° Cutaway 4-Port Venturi Eductor & Mixing Chamber** (`Eductor_Pump_Cavitation_Nozzle_schematic.jpg`) showing the flanged motive feed inlet, seated 316-SS multi-bore nozzle insert, 4 angled slurry induction ports, and converging-diverging cavitating diffuser.
   - `kn-vortex-guides`: Helical central vortex core and three high-shear cavitation filaments inside the cutaway mixing throat.
3. **Component Detail Studies (`models/`)**:
   - `turnbuckle.blend` / `.glb` / `.png`: 9 selectable groups — barrel, opposed threaded forks, clevis pins/retainers, anchor lug, cable eye, thimble, and swage sleeves ([Suncor S0101-0007](https://suncorstainless.com/steel-product/jaw-jaw-turnbuckle/)).
   - `bilge-pump.blend` / `.glb` / `.png`: 4 groups — inlet strainer, main external housing, discharge barb, and leads (Rule 2000 reference class).
   - `hose-joint.blend` / `.glb` / `.png`: 3 groups — hollow hose, overlapping barb, and worm-drive clamp.

## Rebuilding From Source

```bash
/Applications/Blender.app/Contents/MacOS/Blender --background --factory-startup --python build_detail.py
```
