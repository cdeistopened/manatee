"""Source-preserving assembly, 100% clean-room parametric CAD replacement, and 316-SS Kinetic Cavitation Nozzle studies. Metres, Z up."""
import bpy, json, math, csv
from pathlib import Path
from mathutils import Vector

D = Path(__file__).resolve().parent
SRC = D.parents[1] / 'out/prime'
manifest = json.loads((SRC / 'parts_manifest.json').read_text())
records = {}
studies = {}
objects = []
source_checks = []
cleanroom_checks = []

SOURCE = 'CAD export: cad/out/prime/parts_manifest.json'
CLEAN_ORIGIN = 'cleanroom-parametric-2026-10-15'
CLEAN_LICENSE = 'CERN-OHL-S-2.0 / CC-BY-SA-4.0'
CLEAN_SOURCE = f'Solaris Clean-Room Parametric CAD ({CLEAN_ORIGIN}) · {CLEAN_LICENSE}'
DXF_NOZZLE_SOURCE = 'Behrens DXF & schematic: dossier/03_cad-and-schematics/kinetic-nozzle/ (KineticNozzle1.DXF, KineticNozzle5gpd.dxf, Eductor_Pump_Cavitation_Nozzle_schematic.jpg)'
PUMP = 'https://www.xylem.com/siteassets/brand/rule/resources/technical-brochure/standard-bilge-pumps-model-number-table.pdf'
TURN = 'https://suncorstainless.com/steel-product/jaw-jaw-turnbuckle/'


def clear():
    global objects
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    objects = []


def mat(name, color, metal=0.0, rough=0.4):
    m = bpy.data.materials.new(name)
    m.diffuse_color = (*color, 1)
    m.use_nodes = True
    p = m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value = (*color, 1)
    p.inputs['Metallic'].default_value = metal
    p.inputs['Roughness'].default_value = rough
    return m


M = {
    'pvc': mat('White PVC', (.8, .83, .78)),
    'metal': mat('Galvanized steel', (.43, .48, .5), .72, .32),
    'ss': mat('Stainless steel 316', (.64, .69, .72), .86, .20),
    'bronze': mat('Cast marine bronze', (.64, .47, .20), .80, .26),
    'black': mat('Black polymer', (.025, .035, .04)),
    'red': mat('Red pump housing', (.65, .035, .035)),
    'blue': mat('Blue strainer / vortex', (.025, .12, .32)),
    'cyan': mat('Cavitation streamline', (.08, .52, .76), .15, .28),
    'rubber': mat('EPDM / flexible hose', (.07, .08, .075)),
    'solar': mat('Monocrystalline PV', (.025, .06, .105), .35, .28),
    'copper': mat('Tinned conductor', (.63, .67, .67), .75),
    'board': mat('PCB substrate', (.03, .24, .12)),
}


def finish(o, m):
    o.data.materials.append(M[m])
    return o


def box(loc, size, m='ss'):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o = bpy.context.object
    o.scale = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    finish(o, m)
    return o


def cyl(loc, r, depth, m='ss', axis=(0, 0, 1), vertices=48):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=r, depth=depth, location=loc)
    o = bpy.context.object
    o.rotation_euler = Vector(axis).to_track_quat('Z', 'Y').to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    finish(o, m)
    for p in o.data.polygons:
        p.use_smooth = len(p.vertices) == 4
    return o


def cone(loc, r1, r2, depth, m='ss', axis=(0, 0, 1), vertices=48):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=r1, radius2=r2, depth=depth, location=loc)
    o = bpy.context.object
    o.rotation_euler = Vector(axis).to_track_quat('Z', 'Y').to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    finish(o, m)
    for p in o.data.polygons:
        p.use_smooth = len(p.vertices) == 4
    return o


def sphere(loc, r, m='pvc', segments=36, rings=18):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=segments, ring_count=rings, radius=r, location=loc)
    o = bpy.context.object
    finish(o, m)
    for p in o.data.polygons:
        p.use_smooth = True
    return o


def tube(loc, ro, ri, length, m='ss', axis=(0, 0, 1), n=64):
    v = []
    f = []
    for z in [-length / 2, length / 2]:
        for r in [ro, ri]:
            v.extend([(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n), z) for i in range(n)])
    for i in range(n):
        j = (i + 1) % n
        f.extend([
            (i, j, 2 * n + j, 2 * n + i),
            (n + j, n + i, 3 * n + i, 3 * n + j),
            (j, i, n + i, n + j),
            (2 * n + i, 2 * n + j, 3 * n + j, 3 * n + i),
        ])
    mesh = bpy.data.meshes.new('Hollow sleeve')
    mesh.from_pydata(v, [], f)
    mesh.update()
    o = bpy.data.objects.new('Hollow sleeve', mesh)
    bpy.context.collection.objects.link(o)
    o.location = loc
    o.rotation_euler = Vector(axis).to_track_quat('Z', 'Y').to_euler()
    bpy.context.view_layer.objects.active = o
    o.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    o.select_set(False)
    finish(o, m)
    return o


def revolve_profile(profile_rz, loc=(0, 0, 0), m='bronze', n=64, angle_deg=360.0):
    """Build a solid of revolution around Z from a closed polygon [(r, z), ...].
    If angle_deg < 360, caps the two cut planes at theta=0 and theta=angle_rad for a clean cutaway."""
    pts = list(profile_rz)
    k = len(pts)
    full = abs(angle_deg - 360.0) < 1e-4
    steps = n if full else n + 1
    ang_max = math.radians(angle_deg)
    v = []
    f = []
    for s in range(steps):
        theta = (2 * math.pi * s / n) if full else (ang_max * s / n)
        ca, sa = math.cos(theta), math.sin(theta)
        for r, z in pts:
            v.append((loc[0] + r * ca, loc[1] + r * sa, loc[2] + z))
    for s in range(n):
        s_next = (s + 1) % n if full else (s + 1)
        base0 = s * k
        base1 = s_next * k
        for i in range(k):
            j = (i + 1) % k
            f.append((base0 + i, base1 + i, base1 + j, base0 + j))
    if not full:
        f.append(tuple(range(k - 1, -1, -1)))
        last_base = n * k
        f.append(tuple(last_base + i for i in range(k)))
    mesh = bpy.data.meshes.new('RevolvedBody')
    mesh.from_pydata(v, [], f)
    mesh.update()
    o = bpy.data.objects.new('RevolvedBody', mesh)
    bpy.context.collection.objects.link(o)
    finish(o, m)
    return o


def path(points, r, m='ss', res=3):
    c = bpy.data.curves.new('Round path', 'CURVE')
    c.dimensions = '3D'
    c.bevel_depth = r
    c.bevel_resolution = res
    s = c.splines.new('POLY')
    s.points.add(len(points) - 1)
    for p, co in zip(s.points, points):
        p.co = (*co, 1)
    o = bpy.data.objects.new('Round path', c)
    bpy.context.collection.objects.link(o)
    o.data.materials.append(M[m])
    bpy.context.view_layer.objects.active = o
    o.select_set(True)
    bpy.ops.object.convert(target='MESH')
    o.select_set(False)
    return bpy.context.object


def strut(p0, p1, r, m='ss', vertices=20):
    v0, v1 = Vector(p0), Vector(p1)
    dv = v1 - v0
    return cyl(tuple((v0 + v1) / 2), r, dv.length, m=m, axis=tuple(dv.normalized()), vertices=vertices)


def torus(loc, major, minor, m='ss', axis=(0, 0, 1)):
    bpy.ops.mesh.primitive_torus_add(major_radius=major, minor_radius=minor, major_segments=48, minor_segments=10, location=loc)
    o = bpy.context.object
    o.rotation_euler = Vector(axis).to_track_quat('Z', 'Y').to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    finish(o, m)
    return o


def bool_diff(target, cutter, name='BoolCut'):
    bpy.context.view_layer.objects.active = target
    mod = target.modifiers.new(name, 'BOOLEAN')
    mod.operation = 'DIFFERENCE'
    mod.solver = 'EXACT'
    mod.object = cutter
    bpy.ops.object.modifier_apply(modifier=mod.name)
    bpy.data.objects.remove(cutter, do_unlink=True)
    return target


def part(pid, label, system, meshes, status, description, connection='', source=SOURCE, quantity=1, source_part=None, origin=None, license_id=None):
    bpy.ops.object.select_all(action='DESELECT')
    for o in meshes:
        o.select_set(True)
    bpy.context.view_layer.objects.active = meshes[0]
    if len(meshes) > 1:
        bpy.ops.object.join()
    o = bpy.context.object
    o.name = pid
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
    o['part_id'] = pid
    o['source_part'] = source_part or pid
    o['evidence_status'] = status
    o['system'] = system
    o['label'] = label
    if origin:
        o['origin'] = origin
    if license_id:
        o['license'] = license_id
    bpy.context.view_layer.update()
    dims = [round(float(v), 5) for v in o.dimensions]
    rec = {
        'id': pid,
        'name': label,
        'system': system,
        'status': status,
        'description': description,
        'connection': connection,
        'source': source,
        'quantity': quantity,
        'dimensions_m': dims,
    }
    if source_part:
        rec['source_part'] = source_part
    if origin:
        rec['origin'] = origin
    if license_id:
        rec['license'] = license_id
    records[pid] = rec
    objects.append(o)
    return o


def export(study, label, note, cam_dir=(1.2, -1.6, 1.0), ortho_mult=1.8):
    scene = bpy.context.scene
    scene.unit_settings.system = 'METRIC'
    scene.unit_settings.scale_length = 1
    bpy.ops.object.select_all(action='DESELECT')
    for o in objects:
        o.select_set(True)
    bpy.ops.export_scene.gltf(filepath=str(D / f'{study}.glb'), use_selection=True, export_format='GLB', export_extras=True)
    ids = [o.name for o in objects]
    studies[study] = {'name': label, 'note': note, 'parts': ids}
    bpy.context.view_layer.update()
    pts = [o.matrix_world @ Vector(c) for o in objects for c in o.bound_box]
    lo = Vector([min(p[i] for p in pts) for i in range(3)])
    hi = Vector([max(p[i] for p in pts) for i in range(3)])
    center = (lo + hi) / 2
    span = max(hi - lo)
    bpy.ops.object.camera_add(location=center + Vector(cam_dir) * span)
    cam = bpy.context.object
    cam.rotation_euler = (center - cam.location).to_track_quat('-Z', 'Y').to_euler()
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = span * ortho_mult
    cam.data.clip_start = .0001
    scene.camera = cam
    for loc, power in [((1, -2, 3), 90), ((-2, -1, 2), 65), ((1, 3, 2), 100)]:
        bpy.ops.object.light_add(type='AREA', location=center + Vector(loc) * span)
        o = bpy.context.object
        o.data.energy = power * span * span
        o.data.size = span * 2
        o.rotation_euler = (center - o.location).to_track_quat('-Z', 'Y').to_euler()
    scene.world.color = (.6, .6, .6)
    scene.render.engine = 'CYCLES'
    scene.cycles.samples = 24
    scene.render.resolution_x = 1200
    scene.render.resolution_y = 900
    scene.render.resolution_percentage = 100
    scene.render.film_transparent = True
    scene.render.image_settings.file_format = 'PNG'
    scene['study_note'] = note
    scene['catalog'] = json.dumps({i: records[i] for i in ids})
    bpy.ops.wm.save_as_mainfile(filepath=str(D / f'{study}.blend'))
    scene.render.filepath = str(D / f'{study}.png')
    bpy.ops.render.render(write_still=True)


# ==============================================================================
# STUDY 1: CLEAN-ROOM PARAMETRIC MANATEE ASSEMBLY (ZERO catalogue placeholder GEOMETRY)
# ==============================================================================
clear()


def build_clean_pontoon(pid, source_name, label, cx, cy, cz):
    length = 3.1753
    r_max = 0.1321 / 2.0  # 0.06605 m (cap & coupling OD)
    r_pipe = 0.0630       # 5-in Schedule-40 PVC nominal OD
    y_min = cy - length / 2.0
    y_max = cy + length / 2.0
    meshes = [
        cyl((cx, cy, cz), r_pipe, length - 2 * r_max, 'pvc', axis=(0, 1, 0), vertices=48),
        # Slip end-cap skirts & domed ends
        cyl((cx, y_min + r_max + 0.045, cz), r_max, 0.090, 'pvc', axis=(0, 1, 0), vertices=48),
        cyl((cx, y_max - r_max - 0.045, cz), r_max, 0.090, 'pvc', axis=(0, 1, 0), vertices=48),
        sphere((cx, y_min + r_max, cz), r_max, 'pvc', segments=48, rings=20),
        sphere((cx, y_max - r_max, cz), r_max, 'pvc', segments=48, rings=20),
        # Schedule-40 coupling shoulders adjacent to frame clamp stations
        cyl((cx, -0.635, cz), r_max, 0.075, 'pvc', axis=(0, 1, 0), vertices=48),
        cyl((cx, 0.790, cz), r_max, 0.075, 'pvc', axis=(0, 1, 0), vertices=48),
    ]
    return part(
        pid, label, 'flotation', meshes, 'Clean-room parametric',
        '100% original procedural Schedule-40 PVC pontoon tube (132.1 mm cap OD, 3.175 m overall length) with domed slip end-caps and coupling shoulders. Replaces stretched catalogue placeholder 55+gallon+drum.skp.',
        'Clamped to the fore and aft cross-rails by 316-SS band-clamp saddle brackets bearing against the coupling shoulders.',
        source=CLEAN_SOURCE, quantity=1, source_part=source_name, origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
    )


build_clean_pontoon('cr-pontoon-port-outer', 'pontoon-port-outer', 'Clean-room PVC pontoon · port outer', -1.0603, 0.0382, 0.0705)
build_clean_pontoon('cr-pontoon-port-inner', 'pontoon-port-inner', 'Clean-room PVC pontoon · port inner', -0.9340, 0.0382, 0.0705)
build_clean_pontoon('cr-pontoon-starboard-inner', 'pontoon-starboard-inner', 'Clean-room PVC pontoon · starboard inner', 0.8538, 0.0668, 0.0661)
build_clean_pontoon('cr-pontoon-starboard-outer', 'pontoon-starboard-outer', 'Clean-room PVC pontoon · starboard outer', 0.9801, 0.0668, 0.0661)

clamp_meshes = []
for px, pz in [(-1.0603, 0.0705), (-0.9340, 0.0705), (0.8538, 0.0661), (0.9801, 0.0661)]:
    r_c = 0.06605
    for yy in [-0.7099, 0.8652]:
        clamp_meshes.extend([
            tube((px, yy, pz), r_c + 0.0025, r_c + 0.0005, 0.016, 'ss', axis=(0, 1, 0)),
            box((px, yy, pz + r_c + 0.006), (0.036, 0.024, 0.012), 'rubber'),
            box((px, yy, pz + r_c + 0.016), (0.042, 0.022, 0.012), 'ss'),
            cyl((px, yy, pz + r_c + 0.016), 0.0032, 0.048, 'ss', axis=(1, 0, 0), vertices=20),
        ])
part(
    'cr-pontoon-clamps', '316-SS pontoon band-clamp saddle mounts (8×)', 'flotation', clamp_meshes,
    'Clean-room parametric',
    'Eight 316-SS worm-drive band clamps with EPDM elastomer saddles securing the four PVC pontoons to the fore and aft cross-rails next to the coupling shoulders.',
    'Saddle bolts pass into the underside of the cross-rails; axial thrust is reacted against the PVC coupling shoulders.',
    source=CLEAN_SOURCE, quantity=8, source_part='pontoon-clamps', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# Structure: 4 square-section rails, 4 corner cross-socket collars, planar X-braced + diamond deck truss, and central square mast tube
part(
    'cr-frame-rail-cross-aft', 'Aft structural cross-rail', 'structure',
    [box((-0.0217, -0.7099, 0.1354), (2.0611, 0.0530, 0.0530), 'pvc')],
    'Clean-room parametric',
    'Clean-room 53 mm square-section UV-stabilized PVC/HDPE aft cross-beam spanning 2.061 m across all four pontoons at y = -0.7099 m.',
    'Engages port and starboard corner cross-socket collars and carries the eight aft pontoon band clamps.',
    source=CLEAN_SOURCE, quantity=1, source_part='frame-rail-cross-aft', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)
part(
    'cr-frame-rail-cross-forward', 'Forward structural cross-rail', 'structure',
    [box((-0.0289, 0.8652, 0.1358), (2.0856, 0.0530, 0.0530), 'pvc')],
    'Clean-room parametric',
    'Clean-room 53 mm square-section UV-stabilized PVC/HDPE forward cross-beam spanning 2.086 m at y = +0.8652 m.',
    'Engages forward corner cross-socket collars and supports the aft edge of the marine solar array.',
    source=CLEAN_SOURCE, quantity=1, source_part='frame-rail-cross-forward', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)
part(
    'cr-frame-rail-long-port', 'Port longitudinal frame rail', 'structure',
    [box((-0.9823, 0.0616, 0.1221), (0.0530, 2.5189, 0.0530), 'pvc')],
    'Clean-room parametric',
    'Clean-room 53 mm square-section longitudinal rail running 2.519 m fore-and-aft between the port inner and outer pontoons at x = -0.9823 m.',
    'Pinned through corner cross-sockets; provides mounting deck for the high-pressure feed pump and supercapacitor buffer.',
    source=CLEAN_SOURCE, quantity=1, source_part='frame-rail-long-port', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)
part(
    'cr-frame-rail-long-starboard', 'Starboard longitudinal frame rail', 'structure',
    [box((0.8913, 0.0443, 0.1225), (0.0530, 2.5189, 0.0530), 'pvc')],
    'Clean-room parametric',
    'Clean-room 53 mm square-section longitudinal rail running 2.519 m fore-and-aft between the starboard pontoons at x = +0.8913 m.',
    'Pinned through corner cross-sockets; supports the aft-starboard Pyrolizer-Separator & DAF drum.',
    source=CLEAN_SOURCE, quantity=1, source_part='frame-rail-long-starboard', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

socket_meshes = []
for sx in [-0.9823, 0.8913]:
    for sy in [-0.7099, 0.8652]:
        socket_meshes.extend([
            box((sx, sy, 0.1355), (0.115, 0.065, 0.065), 'pvc'),
            box((sx, sy, 0.1223), (0.065, 0.115, 0.065), 'pvc'),
            cyl((sx, sy, 0.129), 0.005, 0.088, 'ss', axis=(0, 0, 1), vertices=20),
        ])
part(
    'cr-frame-sockets', 'Corner cross-socket collars (4×)', 'structure', socket_meshes,
    'Clean-room parametric',
    'Four heavy-duty Schedule-80 PVC/HDPE cross-socket collars with 316-SS vertical thru-bolts locking the longitudinal and cross rails at all four perimeter intersections.',
    'Thru-bolts also anchor the lower clevis lugs for the outer diagonal mast stays.',
    source=CLEAN_SOURCE, quantity=4, source_part='frame-sockets', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

deck_meshes = [
    # Central mast step hub disc & stiffening ring at z = 0.0357..0.065
    cyl((-0.0098, 0.0993, 0.0457), 0.145, 0.020, 'pvc', vertices=48),
    tube((-0.0098, 0.0993, 0.058), 0.145, 0.115, 0.016, 'metal', n=48),
    # X-brace diagonal tension/compression chords from mast step to inner frame corners
    strut((-0.0098, 0.0993, 0.050), (-0.806, -0.737, 0.150), 0.0125, 'pvc'),
    strut((-0.0098, 0.0993, 0.050), (0.804, -0.737, 0.150), 0.0125, 'pvc'),
    strut((-0.0098, 0.0993, 0.050), (0.804, 0.883, 0.150), 0.0125, 'pvc'),
    strut((-0.0098, 0.0993, 0.050), (-0.806, 0.883, 0.150), 0.0125, 'pvc'),
    # Planar diamond truss chords connecting rail midpoints
    strut((-0.806, 0.073, 0.135), (-0.001, -0.737, 0.135), 0.012, 'pvc'),
    strut((-0.001, -0.737, 0.135), (0.804, 0.073, 0.135), 0.012, 'pvc'),
    strut((0.804, 0.073, 0.135), (-0.001, 0.883, 0.135), 0.012, 'pvc'),
    strut((-0.001, 0.883, 0.135), (-0.806, 0.073, 0.135), 0.012, 'pvc'),
    # Corner gusset pads preserving exact manifest envelope [-0.8183..0.8168, -0.7496..0.8957, 0.0357..0.1623]
    box((-0.8063, -0.7376, 0.1503), (0.024, 0.024, 0.024), 'metal'),
    box((0.8048, 0.8837, 0.1503), (0.024, 0.024, 0.024), 'metal'),
]
part(
    'cr-deck-cross-members', 'Planar X-braced & diamond deck truss with mast step hub', 'structure', deck_meshes,
    'Clean-room parametric',
    'Clean-room structural deck truss combining an inscribed diamond frame, four inclined X-brace chords, and the lower circular mast-step hub disc (z = 0.0357..0.1623 m).',
    'Reacts mast step compression and lateral rigging loads into the four perimeter rails.',
    source=CLEAN_SOURCE, quantity=1, source_part='deck-cross-members', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

mast_meshes = [
    box((-0.0098, 0.0993, 0.4575), (0.1397, 0.1397, 0.8436), 'pvc'),
    box((-0.0098, 0.0993, 0.052), (0.158, 0.158, 0.028), 'metal'),
    box((-0.0098, 0.0993, 0.865), (0.152, 0.152, 0.024), 'metal'),
]
part(
    'cr-mast-tube', 'Central square mast column (0.14 m section)', 'structure', mast_meshes,
    'Clean-room parametric',
    'Clean-room 139.7 mm square-section vertical composite/PVC mast column rising from the deck step hub (z = 0.0357 m) to the masthead alternator mount (z = 0.8793 m).',
    'Base flange bolts to the central deck hub; upper collar carries the Lenz-2 VAWT rotor and inner/outer stay rings.',
    source=CLEAN_SOURCE, quantity=1, source_part='mast-tube', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)


# Rigging: Inner and outer diagonal tensegrity mast stay sets with upper/lower collar rings and inline jaw-jaw turnbuckles
def build_stay_set(pid, source_name, label, x_min, x_max, y_min, y_max, z_low, z_high, r_collar):
    cx, cy = -0.0098, 0.0993
    meshes = [
        # Upper square mast collar ring
        box((cx, cy - r_collar, z_high - 0.006), (2 * r_collar + 0.016, 0.014, 0.012), 'metal'),
        box((cx, cy + r_collar, z_high - 0.006), (2 * r_collar + 0.016, 0.014, 0.012), 'metal'),
        box((cx - r_collar, cy, z_high - 0.006), (0.014, 2 * r_collar + 0.016, 0.012), 'metal'),
        box((cx + r_collar, cy, z_high - 0.006), (0.014, 2 * r_collar + 0.016, 0.012), 'metal'),
    ]
    corners = [
        ((x_min + 0.006, y_min + 0.006, z_low + 0.006), (cx - r_collar, cy - r_collar, z_high - 0.006)),
        ((x_max - 0.006, y_min + 0.006, z_low + 0.006), (cx + r_collar, cy - r_collar, z_high - 0.006)),
        ((x_max - 0.006, y_max - 0.006, z_low + 0.006), (cx + r_collar, cy + r_collar, z_high - 0.006)),
        ((x_min + 0.006, y_max - 0.006, z_low + 0.006), (cx - r_collar, cy + r_collar, z_high - 0.006)),
    ]
    for p0, p1 in corners:
        v0, v1 = Vector(p0), Vector(p1)
        dv = v1 - v0
        u = dv.normalized()
        tb_mid = v0 + u * 0.14
        meshes.extend([
            strut(p0, p1, 0.006, 'metal', vertices=16),
            # Inline Suncor-class 316-SS jaw-jaw turnbuckle body & clevis forks at lower end
            cyl(tuple(tb_mid), 0.010, 0.095, 'ss', axis=tuple(u), vertices=20),
            box(tuple(v0 + u * 0.055), (0.018, 0.018, 0.022), 'ss'),
            box(tuple(p0), (0.012, 0.012, 0.012), 'ss'),
        ])
    return part(
        pid, label, 'rigging', meshes, 'Clean-room parametric',
        f'Clean-room four-way diagonal 316-SS mast stay assembly ({source_name}) with welded upper mast collar ring and inline Suncor-class jaw-jaw turnbuckle tensioners at the four deck corners.',
        'Upper collar bolts around the 0.14 m mast column; lower clevis forks pin to the frame corner lugs.',
        source=CLEAN_SOURCE, quantity=1, source_part=source_name, origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
    )


build_stay_set('cr-mast-stays-inner', 'mast-stays-inner', 'Inner diagonal mast stays & turnbuckles', -0.8183, 0.7744, -0.6967, 0.8957, 0.1492, 0.6019, 0.082)
build_stay_set('cr-mast-stays-outer', 'mast-stays-outer', 'Outer diagonal mast stays & turnbuckles', -0.9874, 0.9328, -0.7216, 0.8708, 0.1627, 0.6154, 0.092)

# Propulsion: Port and starboard clean-room Rule 2000-class marine bilge thrusters
thruster_meshes = []
for tx in [-0.997, 0.941]:
    ty = -0.6428
    # Strainer base z = -0.163..-0.125, white wet housing z = -0.125..-0.040, red motor cap z = -0.040..-0.010, mount up to +0.0076
    thruster_meshes.extend([
        cyl((tx, ty, -0.144), 0.056, 0.038, 'blue', vertices=36),
        tube((tx, ty, -0.144), 0.060, 0.053, 0.034, 'blue', n=36),
        cyl((tx, ty, -0.082), 0.052, 0.085, 'pvc', vertices=36),
        cyl((tx, ty, -0.025), 0.052, 0.030, 'red', vertices=36),
        # Aft-directed 1-1/8" (29 mm) propulsion water-jet nozzle (y = -0.8081..-0.695)
        tube((tx, -0.751, -0.120), 0.016, 0.012, 0.114, 'pvc', axis=(0, 1, 0), n=32),
        # Forward hydrodynamic intake fairing & stainless hanger bracket up to z = +0.0076
        cone((tx, -0.535, -0.100), 0.046, 0.014, 0.115, 'black', axis=(0, 1, 0), vertices=28),
        box((tx, ty, -0.002), (0.198, 0.040, 0.019), 'ss'),
    ])
part(
    'cr-bilge-pumps-pair', 'Clean-room Rule 2000-class marine bilge thrusters (pair)', 'propulsion', thruster_meshes,
    'Clean-room parametric',
    'Clean-room port and starboard submerged 2000-GPH centrifugal marine bilge thrusters at x = ±0.96 m, y = -0.6428 m, z = -0.0777 m with slotted blue ABS strainers, sealed white/red motor housings, and aft-directed 29 mm water-jet discharge nozzles. Replaces catalogue placeholder Bilge Pump Cartridge2.skp.',
    'Suspended beneath the aft frame cross-rail on 316-SS hanger brackets; differential thrust steers the vessel.',
    source=CLEAN_SOURCE, quantity=2, source_part='bilge-pumps-pair', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# Fluid & Cavitation Reactor system:
# 1. Central submerged intake pump (bilge-pump-cartridge-centre)
centre_pump_meshes = [
    cyl((0.0, -0.0016, 0.016), 0.0316, 0.032, 'blue', vertices=32),
    cyl((0.0, -0.0016, 0.056), 0.0290, 0.048, 'black', vertices=32),
    cyl((0.0, -0.0016, 0.0899), 0.0290, 0.020, 'red', vertices=32),
    tube((0.022, -0.0016, 0.026), 0.011, 0.008, 0.035, 'pvc', axis=(1, 0, 0), n=24),
]
part(
    'cr-bilge-pump-cartridge-centre', 'Central intake & priming bilge cartridge', 'fluid', centre_pump_meshes,
    'Clean-room parametric',
    'Clean-room central low-pressure priming/slurry lift pump at (0, -0.0016, 0.050 m) with slotted strainer base and 12VDC sealed cartridge. Replaces catalogue placeholder Bilge Pump Cartridge2.skp.',
    'Draws surface algae harvest slurry into the 4-port Venturi eductor induction manifold.',
    source=CLEAN_SOURCE, quantity=1, source_part='bilge-pump-cartridge-centre', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# 2. Deck high-pressure feed pump (pump-deck, AR RMW2G24D 300-psi 12VDC diaphragm/plunger pump)
deck_pump_meshes = [
    # Vibration-isolating baseplate (z = 0.1506..0.160)
    box((-0.7833, 0.2217, 0.1556), (0.0716, 0.1399, 0.010), 'rubber'),
    # 12VDC motor cylinder (y = 0.165..0.245)
    cyl((-0.7833, 0.205, 0.192), 0.033, 0.082, 'black', axis=(0, 1, 0), vertices=32),
    # Cast bronze/brass 300-psi triplex plunger manifold head (y = 0.245..0.2916)
    box((-0.7833, 0.268, 0.194), (0.068, 0.046, 0.058), 'bronze'),
    # Top unloader / pressure regulator valve reaching z = 0.2285
    cyl((-0.7833, 0.268, 0.220), 0.014, 0.017, 'ss', vertices=24),
    # High-pressure outlet & suction fittings
    tube((-0.755, 0.268, 0.194), 0.010, 0.006, 0.024, 'ss', axis=(1, 0, 0), n=24),
]
part(
    'cr-pump-deck', 'High-pressure motive feed pump (300-psi 12VDC)', 'fluid', deck_pump_meshes,
    'Clean-room parametric',
    'Clean-room 300-psi 12VDC positive-displacement plunger/diaphragm feed pump at (-0.7833, 0.2217, 0.1896 m) with cast bronze manifold head and unloader valve. Replaces catalogue placeholder Pumpe.skp.',
    'Delivers high-pressure motive water stream to the 316-SS 7-bore Kinetic Cavitation Nozzle inside the inline Venturi eductor.',
    source=CLEAN_SOURCE, quantity=1, source_part='pump-deck', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# 3. Inline 4-port Venturi Eductor + 4.20-in 316-SS 7-bore Kinetic Cavitation Nozzle cartridge (cr-eductor-nozzle)
eductor_loc = (0.12, -0.7099, 0.198)
ed_nozzle = cyl((eductor_loc[0] - 0.055, eductor_loc[1], eductor_loc[2]), 0.05334, 0.10668, 'ss', axis=(1, 0, 0), vertices=48)
# Drill the 7-bore cluster along X axis in the installed 4.20-in 316-SS nozzle
for br, bang, bdia in [(0.0, 0.0, 0.00635)] + [(0.009271, a, 0.00635) for a in (90, 210, 330)] + [(0.004445, a, 0.004064) for a in (90, 210, 330)]:
    rad = math.radians(bang)
    by = eductor_loc[1] + br * math.cos(rad)
    bz = eductor_loc[2] + br * math.sin(rad)
    cutter = cyl((eductor_loc[0] - 0.055, by, bz), bdia / 2.0, 0.12, 'ss', axis=(1, 0, 0), vertices=20)
    bool_diff(ed_nozzle, cutter, 'NozzleBore')

eductor_meshes = [
    ed_nozzle,
    # Bronze 4-port induction manifold collar & converging-diverging Venturi diffuser
    cone((eductor_loc[0] + 0.045, eductor_loc[1], eductor_loc[2]), 0.058, 0.032, 0.095, 'bronze', axis=(1, 0, 0), vertices=36),
    cone((eductor_loc[0] + 0.125, eductor_loc[1], eductor_loc[2]), 0.032, 0.046, 0.065, 'bronze', axis=(1, 0, 0), vertices=36),
    # 4 angled induction ports around the suction chamber
    cyl((eductor_loc[0] + 0.010, eductor_loc[1] - 0.055, eductor_loc[2]), 0.014, 0.045, 'bronze', axis=(0.4, -0.9, 0), vertices=20),
    cyl((eductor_loc[0] + 0.010, eductor_loc[1] + 0.055, eductor_loc[2]), 0.014, 0.045, 'bronze', axis=(0.4, 0.9, 0), vertices=20),
    cyl((eductor_loc[0] + 0.010, eductor_loc[1], eductor_loc[2] + 0.055), 0.014, 0.045, 'bronze', axis=(0.4, 0, 0.9), vertices=20),
    cyl((eductor_loc[0] + 0.010, eductor_loc[1], eductor_loc[2] - 0.055), 0.014, 0.045, 'bronze', axis=(0.4, 0, -0.9), vertices=20),
    # Motive feed line from cr-pump-deck, induction line from centre pump, and discharge line to separator drum
    path([(-0.745, 0.268, 0.194), (-0.62, -0.25, 0.185), (-0.42, -0.7099, 0.198), (eductor_loc[0] - 0.11, eductor_loc[1], eductor_loc[2])], 0.009, 'rubber'),
    path([(0.022, -0.0016, 0.026), (0.04, -0.35, 0.12), (eductor_loc[0] + 0.010, eductor_loc[1] + 0.065, eductor_loc[2])], 0.010, 'rubber'),
    path([(eductor_loc[0] + 0.158, eductor_loc[1], eductor_loc[2]), (0.52, -0.82, 0.188), (0.735, -1.046, 0.178)], 0.014, 'rubber'),
]
part(
    'cr-eductor-nozzle', 'Inline 4-port Venturi Eductor & 4.20-in 316-SS Kinetic Cavitation Nozzle', 'fluid', eductor_meshes,
    'Clean-room parametric',
    'Behrens core IP: 4.20-in OD × 4.20-in 316-SS 7-bore tetrahedral Kinetic Cavitation Nozzle seated inside a 4-port bronze Venturi Eductor on the aft fluid bridge between the high-pressure deck pump and separator drum.',
    'High-pressure motive water from pump-deck accelerates through the 7 bores (0.25" & 0.16" jets on 0.73" pitch circle), entraining algae/paraffin slurry via the 4 induction ports and lysing cells by hydrodynamic acoustic cavitation.',
    source=DXF_NOZZLE_SOURCE, quantity=1, source_part='cr-eductor-nozzle', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# 4. Pyrolizer-Separator & DAF Drum (vessel-squat-cylinder)
vessel_meshes = [
    tube((0.9264, -1.0460, 0.1740), 0.20765, 0.192, 0.0933, 'pvc', n=64),
    cyl((0.9264, -1.0460, 0.1330), 0.20765, 0.011, 'pvc', vertices=64),
    tube((0.9264, -1.0460, 0.1820), 0.135, 0.128, 0.068, 'ss', n=48),
    # Tangential feed inlet boss, paraffin decant port, and bottom clarified water return stub
    cyl((0.735, -1.0460, 0.1780), 0.018, 0.036, 'ss', axis=(1, 0, 0), vertices=24),
    cyl((0.9264, -0.855, 0.1950), 0.014, 0.034, 'bronze', axis=(0, 1, 0), vertices=24),
    cyl((0.9264, -1.235, 0.1500), 0.016, 0.034, 'pvc', axis=(0, 1, 0), vertices=24),
]
part(
    'cr-vessel-squat-cylinder', 'Pyrolizer-Separator & DAF decant drum', 'fluid', vessel_meshes,
    'Clean-room parametric',
    'Clean-room 415.3 mm OD × 93.3 mm cyclonic dissolved-air-flotation (DAF) & lipid/paraffin decant vessel at the aft-starboard corner (0.9264, -1.0460, 0.1740 m) with internal stainless weir baffle, tangential cavitated-slurry feed boss, upper lipid/paraffin skim port, and clarified water return port.',
    'Receives lysed multiphase mixture from cr-eductor-nozzle; separates buoyant lipid/paraffin fraction over the internal weir.',
    source=CLEAN_SOURCE, quantity=1, source_part='vessel-squat-cylinder', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# Power: Clean-room flexible marine monocrystalline solar array & sealed supercapacitor / LiFePO4 buffer module
solar_meshes = [
    box((-0.0399, 1.1179, 0.1632), (2.0655, 0.5192, 0.0034), 'pvc'),
    box((-0.0399, 1.1179, 0.1662), (2.0350, 0.4950, 0.0028), 'solar'),
    # Silver tinned-copper busbars & top weatherproof junction box within exact z = 0.1614..0.1683 envelope
    box((-0.0399, 1.00, 0.1678), (1.98, 0.008, 0.0008), 'copper'),
    box((-0.0399, 1.23, 0.1678), (1.98, 0.008, 0.0008), 'copper'),
    box((-0.65, 0.91, 0.1665), (0.095, 0.065, 0.0036), 'black'),
]
part(
    'cr-solar-panel', 'Clean-room flexible marine monocrystalline PV array (100 W)', 'power', solar_meshes,
    'Clean-room parametric',
    'Clean-room 2.0655 × 0.5192 m ETFE-laminated flexible marine monocrystalline solar array at (-0.0399, 1.1179, 0.1649 m) with white polymer backing, busbar grid, and sealed junction box. Replaces catalogue placeholder sun_power305 placeholder.',
    'Mounted across the forward pontoon deck ahead of the forward cross-rail; feeds the supercapacitor/LiFePO4 buffer module.',
    source=CLEAN_SOURCE, quantity=1, source_part='solar-panel', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

cap_meshes = [
    cyl((-0.7735, 0.5625, 0.1921), 0.0320, 0.175, 'ss', axis=(0, 1, 0), vertices=36),
    cyl((-0.7735, 0.4710, 0.1921), 0.0320, 0.020, 'black', axis=(0, 1, 0), vertices=36),
    cyl((-0.7735, 0.6540, 0.1921), 0.0320, 0.020, 'black', axis=(0, 1, 0), vertices=36),
    # Waterproof PG9 terminal cable glands at aft end
    cyl((-0.785, 0.464, 0.1921), 0.006, 0.006, 'copper', axis=(0, 1, 0), vertices=16),
    cyl((-0.762, 0.464, 0.1921), 0.006, 0.006, 'copper', axis=(0, 1, 0), vertices=16),
]
part(
    'cr-capacitor', 'Sealed marine supercapacitor / LiFePO4 buffer module', 'power', cap_meshes,
    'Clean-room parametric',
    'Clean-room 64.0 × 203.1 × 64.0 mm brushed-stainless energy buffer module at (-0.7735, 0.5625, 0.1921 m) with sealed polymer end-caps and waterproof cable glands. Replaces catalogue placeholder Elec_capacitor.skp.',
    'Buffers solar & Lenz-2 VAWT generator output to handle high-current pulse loads from the 300-psi cavitation feed pump.',
    source=CLEAN_SOURCE, quantity=1, source_part='capacitor', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# Wind: Clean-room 3-wing Lenz-2 VAWT rotor & sealed masthead PMG alternator housing
rx, ry, rz = -0.0136, 0.1687, 0.8742
r_lenz = 0.252
wing_r = 0.0705
z_bot, z_top = 0.6756, 1.0727
h_lenz = z_top - z_bot  # 0.3971 m
rotor_meshes = [
    # Central rotor hub tube & sealed masthead permanent-magnet generator (PMG) drum
    cyl((rx, ry, rz), 0.028, h_lenz, 'ss', vertices=32),
    cyl((rx, ry, z_bot + 0.055), 0.078, 0.095, 'metal', vertices=36),
]
for i in range(3):
    ang = math.radians(i * 120.0 + 30.0)
    wx = rx + r_lenz * math.cos(ang)
    wy = ry + r_lenz * math.sin(ang)
    t_ang = ang + math.pi / 2.0
    # Upper and lower radial spoke arms
    rotor_meshes.append(strut((rx, ry, z_bot + 0.065), (wx, wy, z_bot + 0.065), 0.0085, 'ss'))
    rotor_meshes.append(strut((rx, ry, z_top - 0.065), (wx, wy, z_top - 0.065), 0.0085, 'ss'))
    # Lenz-2 vertical airfoil wing: cylindrical leading-edge cup + tangential cambered trailing blade
    rotor_meshes.append(tube((wx, wy, rz), wing_r, wing_r - 0.006, h_lenz, 'metal', n=36))
    bx = wx - wing_r * 0.65 * math.cos(t_ang)
    by = wy - wing_r * 0.65 * math.sin(t_ang)
    blade = box((bx, by, rz), (0.006, wing_r * 1.45, h_lenz), 'metal')
    blade.rotation_euler = (0, 0, t_ang - math.pi / 2.0 - 0.22)
    bpy.context.view_layer.objects.active = blade
    blade.select_set(True)
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    blade.select_set(False)
    rotor_meshes.append(blade)

part(
    'cr-rotor-lenz-masthead', 'Clean-room 3-wing Lenz-2 VAWT rotor & masthead PMG alternator', 'wind', rotor_meshes,
    'Clean-room parametric',
    'Clean-room vertical-axis wind turbine (VAWT) at (-0.0136, 0.1687, 0.8742 m, z = 0.6756..1.0727 m) with three cycloidal/J-profile Lenz-2 wings on six radial spoke arms around a central hub and sealed permanent-magnet alternator housing.',
    'Couples directly to the masthead PMG shaft to trickle-charge the deck supercapacitor/LiFePO4 buffer day and night.',
    source=CLEAN_SOURCE, quantity=1, source_part='rotor-lenz-masthead', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

bpy.context.view_layer.update()
cr_pts = [o.matrix_world @ Vector(c) for o in objects for c in o.bound_box]
cr_lo = [round(min(p[i] for p in cr_pts), 4) for i in range(3)]
cr_hi = [round(max(p[i] for p in cr_pts), 4) for i in range(3)]
cr_size = [round(cr_hi[i] - cr_lo[i], 4) for i in range(3)]
for o in objects:
    cleanroom_checks.append({
        'id': o.name,
        'source_part': o['source_part'],
        'origin': o['origin'],
        'license': o['license'],
        'third_party': False,
        'dimensions_m': records[o.name]['dimensions_m'],
        'vertices': len(o.data.vertices),
    })

export(
    'cleanroom',
    'Manatee · 100% clean-room parametric CAD',
    '100% original procedural CAD replacement (CERN-OHL-S-2.0 / CC-BY-SA-4.0) resolving sol0075. Zero catalogue placeholder meshes. Includes all 7 systems and the inline 316-SS 7-bore Kinetic Cavitation Nozzle & 4-port Venturi Eductor.'
)


# ==============================================================================
# STUDY 2: 316-SS HYDRODYNAMIC CAVITATION NOZZLE & 4-PORT VENTURI EDUCTOR
# ==============================================================================
clear()


def build_drilled_nozzle(pid, label, cx, cy, cz, od_in, len_in, pitch_d_in, pri_d_in, sec_d_in, sec_r_in, desc):
    od = od_in * 0.0254
    length = len_in * 0.0254
    r_outer = od / 2.0
    r_pitch = (pitch_d_in * 0.0254) / 2.0
    r_pri = (pri_d_in * 0.0254) / 2.0
    r_sec = (sec_d_in * 0.0254) / 2.0
    r_inner = sec_r_in * 0.0254
    # Oriented with bore axis along Y so the 7-bore face looks straight toward the front-right ortho camera
    body = cyl((cx, cy, cz), r_outer, length, 'ss', axis=(0, 1, 0), vertices=64)
    bores = [(0.0, 0.0, r_pri)]
    for ang_deg in (90.0, 210.0, 330.0):
        a = math.radians(ang_deg)
        bores.append((r_pitch * math.cos(a), r_pitch * math.sin(a), r_pri))
        bores.append((r_inner * math.cos(a), r_inner * math.sin(a), r_sec))
    for bx, bz, br in bores:
        cutter = cyl((cx + bx, cy, cz + bz), br, length * 1.15, 'ss', axis=(0, 1, 0), vertices=28)
        bool_diff(body, cutter, 'KineticBore')
    # Pitch-circle witness groove ring on front face (-Y) for visual inspection of the 0.73" / 0.20" layout
    ring = torus((cx, cy - length / 2.0, cz), r_pitch, max(0.00035, r_outer * 0.008), 'copper', axis=(0, 1, 0))
    return part(
        pid, label, 'fluid', [body, ring], 'Clean-room parametric', desc,
        'Seats inside the converging motive inlet of the 4-port Venturi Eductor; high-velocity jets generate collapsing vapour cavities downstream.',
        source=DXF_NOZZLE_SOURCE, quantity=1, source_part=pid, origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
    )


# Part 1: Flagship 4.20-in OD × 4.20-in 316-SS Kinetic Nozzle Cylinder (KineticNozzle1.DXF)
build_drilled_nozzle(
    'kn-disc-420',
    '4.20-in 316-SS 7-Bore Kinetic Cavitation Nozzle (KineticNozzle1.DXF)',
    cx=-0.105, cy=0.0, cz=0.0,
    od_in=4.20, len_in=4.20, pitch_d_in=0.73, pri_d_in=0.25, sec_d_in=0.16, sec_r_in=0.175,
    desc='Exact 3D realization of KineticNozzle1.DXF & KineticNozzle1BBB.JPG (labeled "306 S.S." / 316 stainless steel): 4.20 in (106.68 mm) OD × 4.20 in (106.68 mm) cylinder Boolean-drilled with the 7-bore tetrahedral vortex cluster around the 0.73 in (18.54 mm) pitch circle — one central 0.25 in (6.35 mm) bore, three outer 0.25 in primary bores at 90°/210°/330°, and three interstitial 0.16 in (4.06 mm) secondary bores.'
)

# Part 2: 5-GPD 1.06-in OD × 1.06-in 316-SS Nozzle Cartridge (KineticNozzle5gpd.dxf)
build_drilled_nozzle(
    'kn-disc-5gpd',
    '5-GPD 1.06-in 316-SS Kinetic Nozzle Cartridge (KineticNozzle5gpd.dxf)',
    cx=-0.195, cy=-0.025, cz=-0.0399,
    od_in=1.06, len_in=1.06, pitch_d_in=0.20, pri_d_in=0.06, sec_d_in=0.04, sec_r_in=0.048,
    desc='Exact 3D realization of KineticNozzle5gpd.dxf: 1.06 in (26.92 mm) OD × 1.06 in (26.92 mm) 316-SS bench/pilot 5-GPD cavitation cartridge with 0.20 in (5.08 mm) pitch circle, four 0.06 in (1.52 mm) primary bores, and three 0.04 in (1.02 mm) secondary bores, shown alongside the 4.20-in full-scale unit for 1:4 scale comparison.'
)

# Part 3: Cutaway (180° section) 4-Port Venturi Eductor & Mixing Chamber (Eductor_Pump_Cavitation_Nozzle_schematic.jpg)
ed_x = 0.075
# Revolved 180° cutaway (angle 0..180° -> back +Y half retained, front -Y half open to camera!)
outer_wall_profile = [
    (0.030, -0.105), (0.064, -0.105), (0.064, -0.093), (0.044, -0.093),
    (0.044, -0.065), (0.076, -0.040), (0.076, 0.005),  (0.062, 0.045),
    (0.042, 0.082),  (0.056, 0.130),  (0.044, 0.130),  (0.031, 0.082),
    (0.048, 0.045),  (0.062, 0.005),  (0.062, -0.032), (0.030, -0.058),
]
ed_shell = revolve_profile(outer_wall_profile, loc=(ed_x, 0.0, 0.0), m='bronze', n=48, angle_deg=180.0)

# Seated 180°-sectioned 316-SS kinetic nozzle insert inside the motive throat (z = -0.060..-0.002)
nozzle_insert_profile = [
    (0.004, -0.060), (0.030, -0.060), (0.030, -0.025), (0.038, -0.025),
    (0.038, -0.002), (0.004, -0.002),
]
ed_insert = revolve_profile(nozzle_insert_profile, loc=(ed_x, 0.0, 0.0), m='ss', n=48, angle_deg=180.0)
# Outer 7-bore ring on the seated insert
for ang_deg in (30.0, 90.0, 150.0):
    a = math.radians(ang_deg)
    cutter = cyl((ed_x + 0.011 * math.cos(a), 0.011 * math.sin(a), -0.031), 0.0032, 0.070, 'ss', axis=(0, 0, 1), vertices=20)
    bool_diff(ed_insert, cutter, 'SeatedBore')

# 4 angled induction ports around the lower plenary chamber (at 35°, 145°, 215°, 325°; rear two intact, front stubs visible)
ind_ports = []
for ang_deg in (35.0, 145.0):
    a = math.radians(ang_deg)
    px = ed_x + 0.068 * math.cos(a)
    py = 0.068 * math.sin(a)
    ind_ports.append(tube((px, py, -0.028), 0.016, 0.010, 0.042, 'bronze', axis=(-0.65 * math.cos(a), -0.65 * math.sin(a), 0.75), n=28))

part(
    'kn-eductor-body',
    'Cutaway 4-Port Venturi Eductor & Cavitation Mixing Chamber',
    'fluid', [ed_shell, ed_insert] + ind_ports, 'Clean-room parametric',
    '180° cutaway engineering model of Rudy Behrens\' 4-Port Venturi Eductor & Cavitation Nozzle schematic (Eductor_Pump_Cavitation_Nozzle_schematic.jpg). Shows the bottom flanged high-pressure motive feed inlet, the seated 316-SS multi-bore kinetic nozzle insert, the four angled low-pressure induction ports, the converging acoustic-cavitation mixing chamber, and the diverging Venturi discharge diffuser.',
    'Motive jet exits the 316-SS nozzle at high velocity into the converging chamber, pulling secondary slurry through the four angled induction ports and collapsing cavitation microbubbles in the throat.',
    source=DXF_NOZZLE_SOURCE, quantity=1, source_part='kn-eductor-body', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

# Part 4: Helical streamlines & cavitation collapse zone callout geometry in the downstream mixing chamber
core_helix = []
for i in range(121):
    t = i / 120.0
    zz = -0.002 + t * 0.130
    env_r = 0.018 * (1.0 - 0.35 * math.sin(math.pi * t))
    ang = 2.0 * math.pi * 3.5 * t
    core_helix.append((ed_x + env_r * math.cos(ang), env_r * math.sin(ang), zz))

vortex_meshes = [
    path(core_helix, 0.0026, 'blue', res=3),
    cone((ed_x, 0.0, 0.134), 0.007, 0.0005, 0.016, 'blue', axis=(0, 0, 1), vertices=20),
]
for k in range(3):
    phase = k * (2.0 * math.pi / 3.0)
    shear_pts = []
    for i in range(91):
        t = i / 90.0
        zz = -0.018 + t * 0.138
        rr = 0.042 * (1.0 - 0.45 * t) + 0.0025 * math.sin(2.0 * math.pi * 8.0 * t)
        ang = phase + 2.0 * math.pi * 1.6 * t
        shear_pts.append((ed_x + rr * math.cos(ang), rr * math.sin(ang), zz))
    vortex_meshes.append(path(shear_pts, 0.0016, 'cyan', res=2))

part(
    'kn-vortex-guides',
    'Helical Vortex Core & Acoustic Cavitation Shear Streamlines',
    'fluid', vortex_meshes, 'Clean-room parametric',
    'Illustrative 3D flow-field geometry inside the cutaway mixing chamber: central helical vortex core (blue) generated by the tetrahedral 7-bore cluster, surrounded by three high-frequency acoustic-cavitation shear filaments (cyan) rising from the four induction ports into the Venturi throat.',
    'Visualizes the hydrodynamic shear and microbubble implosion zone that lyses algae cell walls and emulsifies/cracks heavy hydrocarbons.',
    source=DXF_NOZZLE_SOURCE, quantity=1, source_part='kn-vortex-guides', origin=CLEAN_ORIGIN, license_id=CLEAN_LICENSE
)

export(
    'kinetic-nozzle',
    '316-SS Kinetic Cavitation Nozzle & 4-Port Eductor',
    'Parametric 3D engineering study from KineticNozzle1.DXF (4.20 in OD × 4.20 in, 7 bores on 0.73 in pitch circle), KineticNozzle5gpd.dxf (1.06 in 5-GPD cartridge), and Eductor_Pump_Cavitation_Nozzle_schematic.jpg (180° cutaway 4-port Venturi eductor with helical vortex streamlines).',
    cam_dir=(0.9, -1.75, 0.65),
    ortho_mult=1.55
)


# ==============================================================================
# STUDY 3: SOURCE-PRESERVING ASSEMBLY (ORIGINAL 19 GROUPS + 12 PLACEMENT STUDIES)
# ==============================================================================
clear()
for p in manifest['parts']:
    if p['class'] != 'machine':
        continue
    name = p['part']
    verts = []
    faces = []
    for l in (SRC / 'parts' / f'{name}.obj').read_text().splitlines():
        if l.startswith('v '):
            verts.append(tuple(map(float, l.split()[1:4])))
        elif l.startswith('f '):
            faces.append([int(s.split('/')[0]) - 1 for s in l.split()[1:]])
    mesh = bpy.data.meshes.new(name)
    mesh.from_pydata(verts, [], faces)
    mesh.update()
    o = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(o)
    system = 'structure'
    material = 'pvc'
    desc = 'Shape and position retained from the SketchUp export. Dimensions describe the drawing, not a verified manufactured part.'
    connection = 'Joint hardware and fits need confirmation.'
    status = 'Source geometry'
    if 'pontoon' in name:
        system = 'flotation'
        desc += ' Four individual tubes, arranged in two pairs. Catalogue drum geometry was stretched into tubes; nominal pipe size is unresolved.'
        connection = 'Source annotation calls for frame-fixed pipe clamps next to cap/coupling shoulders.'
    elif 'stays' in name:
        system = 'rigging'
        material = 'metal'
        desc += ' These are wide brace-like strips in the drawing; whether each is a rigid brace or cable must be resolved.'
        connection = 'End fasteners are not resolved in the export. Do not substitute cables without confirming the load path.'
    elif 'bilge-pumps' in name:
        system = 'propulsion'
        material = 'black'
        desc = 'Two bare catalogue cartridges in one source group. Charlie confirms propulsion uses large off-the-shelf marine bilge pumps. Make/model and complete-pump versus cartridge conversion are unresolved.'
        connection = 'Mounts, discharge direction, wet inlet clearance and wiring route need confirmation.'
        status = 'Pump identity needed'
    elif 'bilge-pump-cartridge' in name:
        system = 'fluid'
        material = 'black'
        desc = 'Central bilge cartridge exists in the drawing; exact model and fluid duty unconfirmed.'
        connection = 'Inlet/outlet plumbing is absent from the source.'
    elif 'pump-deck' in name:
        system = 'fluid'
        material = 'metal'
        desc = 'Generic catalogue Pumpe.skp placeholder, not an identified process pump.'
        connection = 'Do not infer flow direction or hose route from this placeholder.'
        status = 'Pump identity needed'
    elif 'vessel' in name:
        system = 'fluid'
        material = 'pvc'
        desc = 'Shallow source cylinder. Function is unresolved; it is not evidence of a 55-gallon reactor.'
        connection = 'No confirmed feed, return or drain ports.'
        status = 'Function unresolved'
    elif 'solar' in name:
        system = 'power'
        material = 'solar'
        desc = 'Source panel is a non-uniformly stretched SunPower catalogue model. Its 2.066 × 0.519 m footprint is a placeholder, not a real panel specification. Annotation says flexible 100 W.'
        connection = 'Actual panel dimensions, mounting holes and cable exit need identification.'
        status = 'Scaled placeholder'
    elif 'capacitor' in name:
        system = 'power'
        material = 'metal'
        desc = 'Catalogue capacitor present in drawing. Electrical rating and actual wiring unverified.'
        connection = 'Terminals are not sufficient evidence of an electrical circuit.'
        status = 'Electrical identity needed'
    elif 'rotor' in name:
        system = 'wind'
        material = 'metal'
        desc = 'Three-wing Lenz-type rotor geometry retained. This represents the rotor, not a verified generator assembly.'
        connection = 'Bearing stack, shaft coupler and generator attachment are not detailed.'
    finish(o, material)
    part(name, name.replace('-', ' ').capitalize(), system, [o], status, desc, connection, source=SOURCE + '; origin: ' + p.get('origin', 'unknown'), quantity=2 if name == 'bilge-pumps-pair' else 1)
    bpy.context.view_layer.update()
    error = max(abs(float(o.dimensions[i]) - p['size_m'][i]) for i in range(3))
    assert error < .002, (name, error)
    source_checks.append({'id': name, 'max_envelope_error_m': error, 'vertices': len(o.data.vertices)})

for p in manifest['parts']:
    if not p['part'].startswith('pontoon'):
        continue
    x, y, z = p['centre_m']
    r = p['size_m'][0] / 2
    for end, yy in [('aft', -.7099), ('forward', .8652)]:
        meshes = [
            tube((x, yy, z), r + .0025, r + .0006, .012, 'ss', axis=(0, 1, 0)),
            box((x, yy, z + r + .008), (.027, .018, .014)),
            cyl((x, yy, z + r + .009), .003, .031, axis=(1, 0, 0)),
            box((x, yy, z + r + .021), (.019, .015, .012), 'black'),
        ]
        part(
            'clamp-' + p['part'] + '-' + end,
            'Pontoon band clamp · ' + p['part'].replace('pontoon-', '') + ' ' + end,
            'flotation', meshes, 'Placement study',
            'Clamp band around source tube, worm housing and mounting saddle. Generic dimensions; band orientation is illustrative.',
            'Generic mounting saddle shown near the source frame. The source has overlapping pipe envelopes; bracket geometry, liner and axial stops require a close-up.',
            'CAD annotation: Rigidly attach pipe clamps to frame… next to shoulders formed by end caps & couplings.'
        )

for x in [-.9823, .8913]:
    for y in [-.7099, .8652]:
        meshes = [
            tube((x, y, .134), .0315, .0265, .105, 'pvc', axis=(1, 0, 0)),
            tube((x, y, .124), .0315, .0265, .105, 'pvc', axis=(0, 1, 0)),
        ]
        part(
            f'frame-socket-{x}-{y}', 'Frame cross socket', 'structure', meshes, 'Placement study',
            'Generic socket envelope around the two intersecting source rails. Socket bores remain visible; this is not a fitting SKU.',
            'Confirm cross versus tee arrangement, real pipe outside diameter, and insertion depths. Do not use for fabrication.'
        )
export('assembly', 'Manatee · detailed source study', '19 source groups retained. White pipe materials corrected. Twelve removable clamp/socket placement studies added; dimensions and connections are not an as-built certification.')

# ==============================================================================
# STUDY 4: TURNBUCKLE & CABLE CONNECTION
# ==============================================================================
clear()
body = .0889
pinspan = .19
pinr = .005588 / 2
gap = .009652
part('tb-body', 'Turnbuckle barrel', 'rigging', [tube((0, 0, 0), .004826, .00325, body)], 'Manufacturer dimensions', 'Closed barrel: nominal 3.50 in length and 0.38 in diameter, based on Suncor S0101-0007.', 'Opposed right- and left-hand 1/4 in UNC studs engage this barrel. Internal thread form is simplified.', TURN)
for side, sign in [('upper', 1), ('lower', -1)]:
    z = sign * pinspan / 2
    meshes = [cyl((0, 0, sign * .057), .003175, .05), box((0, 0, sign * .079), (.014, .014, .01))]
    for xx in [-gap / 2 - .002, gap / 2 + .002]:
        meshes.append(box((xx, 0, sign * .09), (.004, .013, .03)))
    for o in meshes[2:]:
        cutter = cyl((o.location.x, 0, z), pinr + .0002, .015, axis=(1, 0, 0))
        bool_diff(o, cutter, 'Clevis pin clearance')
    pts = []
    for i in range(401):
        t = i / 400
        zz = sign * (.035 + t * .035)
        a = 2 * math.pi * (.035 / .00127) * t
        pts.append((.0031 * math.cos(a), .0031 * math.sin(a), zz))
    meshes.append(path(pts, .00022))
    part('tb-stud-' + side, side.capitalize() + ' threaded fork', 'rigging', meshes, 'Manufacturer envelope', 'Nominal 1/4 in UNC stud and fork. Jaw opening and pin size from manufacturer; transition profiles are simplified.', 'Fork cheeks flank the eye; pin passes through all three. Operating pin span shown at 190 mm, within published open/closed range.', TURN)
    meshes = [cyl((0, 0, z), pinr, .025, axis=(1, 0, 0)), cyl((-.014, 0, z), .004, .002, axis=(1, 0, 0)), torus((.014, 0, z), .003, .0006, axis=(0, 1, 0))]
    part('tb-pin-' + side, side.capitalize() + ' clevis pin & retaining ring', 'rigging', meshes, 'Connection study', 'Removable cross-pin through the fork and mating eye. Retaining ring is schematic; retention detail must match the selected product.', 'Pin carries the eye load; the threaded stud does not screw into the cable.', TURN)
anchor = box((0, 0, -.112), (.005, .022, .052))
cut = cyl((0, 0, -pinspan / 2), pinr + .0002, .02, axis=(1, 0, 0))
bool_diff(anchor, cut, 'Anchor hole')
part('tb-anchor', 'Anchor lug with pin hole', 'rigging', [anchor], 'Connection study', 'A drilled 5 mm plate illustrates a mating anchor. Not identified on the Manatee.', 'Its base attachment and backing structure remain unresolved; this plate is not installed in the source model.')
eye = [(0, .006 * math.sin(2 * math.pi * i / 64), .106 + .013 * math.cos(2 * math.pi * i / 64)) for i in range(65)]
part('cable-thimble', 'Cable-eye thimble', 'rigging', [path(eye, .0012)], 'Connection study', 'Protective thimble form at the upper clevis. Profile simplified.', 'Upper pin crosses the hollow eye. Actual thimble groove and wire diameter must be matched.')
wire = [(0, .008 * math.sin(2 * math.pi * i / 64), .106 + .015 * math.cos(2 * math.pi * i / 64)) for i in range(65)]
meshes = [path(wire, .0015875), cyl((0, -.003, .18), .0015875, .13, 'metal'), cyl((0, .003, .147), .0015875, .06, 'metal')]
part('cable-eye', '1/8 in cable eye & tail', 'rigging', meshes, 'Connection study', '1/8 in cable drawn as a smooth centreline envelope; strand construction is not reproduced.', 'Return tail and standing run meet the eye. End termination type must be confirmed from the actual machine.')
part('cable-sleeves', 'Example swage sleeves', 'rigging', [box((0, 0, z), (.007, .01, .01)) for z in [.135, .155]], 'Connection study', 'Example swaged termination, not an assertion that the raft uses swages.', 'Confirm swage versus clips versus a swageless fitting; hardware and tooling must match the cable.')
export('turnbuckle', 'Turnbuckle & cable connection', 'Bench study, not installed on the raft. Suncor 1/4 in jaw–jaw envelope, visible threads and pinned eye; generic anchor and cable termination. Connection type still needs confirmation.')

# ==============================================================================
# STUDY 5: LARGE BILGE PUMP REFERENCE STUDY
# ==============================================================================
clear()
part('pump-strainer', 'Removable slotted inlet strainer', 'propulsion', [cyl((0, 0, .004), .054, .008, 'blue')] + [box((.05 * math.cos(i * math.pi / 16), .05 * math.sin(i * math.pi / 16), .023), (.004, .004, .031), 'blue') for i in range(32)] + [tube((0, 0, .037), .054, .049, .005, 'blue')], 'Representative part', 'Slotted inlet cage and removable base, based on the form of a large marine bilge pump.', 'Water must reach the inlet slots. Mounting-hole locations and service-release mechanism are not specified.', PUMP)
wet_shell = tube((0, 0, .051), .047, .036, .024, 'pvc')
cut = cyl((0, -.043, .05), .0115, .09, axis=(0, 1, 0))
bool_diff(wet_shell, cut, 'Open outlet into lower wet chamber')
part('pump-motor', 'Motor housing & lower wet chamber', 'propulsion', [wet_shell, cyl((0, 0, .0935), .047, .061, 'pvc'), cyl((0, 0, .138), .047, .028, 'red')], 'Manufacturer envelope', 'Rule 2000 / 10-6UL reference class: 152 mm tall, 108 mm wide. This is a size study, not identification of the actual Manatee pump.', 'Outlet opens into an illustrative lower wet chamber, separate from the upper motor envelope. Impeller and shaft seal are not reconstructed.', PUMP)
meshes = [tube((0, -.056, .05), .0145, .0115, .055, 'pvc', axis=(0, 1, 0))]
for yy in [-.065, -.073, -.08]:
    meshes.append(tube((0, yy, .05), .0155, .0115, .003, 'pvc', axis=(0, 1, 0)))
part('pump-discharge', 'Open discharge hose barb', 'propulsion', meshes, 'Representative part', 'Nominal 1-1/8 in (29 mm) hose connection, using the manufacturer hose size. Barb profile/position are illustrative.', 'A complete pump pushes water through this outlet. A cartridge/propeller conversion would be a different assembly.', PUMP)
part('pump-leads', 'Sealed power-lead exit', 'propulsion', [path([(x, .033, .146), (x, .05, .165), (x, .07, .18), (x, .08, .21)], .0018, m) for x, m in [(-.003, 'red'), (.003, 'black')]], 'Connection study', 'Two insulated leads leave the housing. Lead gauge, gland geometry and circuit protection depend on the actual pump.', 'Splices and disconnects belong outside the submerged connection zone unless specifically rated; exact route is pending.')
export('bilge-pump', 'Large bilge pump · reference study', 'Complete 2000 GPH-class pump envelope, not a chosen thruster. Inlet cage, sealed motor, open hose outlet and two leads. Awaiting actual pump identity and propulsion arrangement.')

# ==============================================================================
# STUDY 6: HOSE, BARB & BAND CLAMP
# ==============================================================================
clear()
part('hose', 'Hose with visible bore', 'fluid', [tube((0, 0, 0), .0185, .0145, .13, 'rubber', axis=(0, 1, 0))], 'Connection study', 'Short flexible hose at nominal 29 mm bore. Generic wall thickness.', 'This illustrates a joint only; no route or pressure rating is assigned to the raft.')
part('hose-barb', 'Barbed spigot with open bore', 'fluid', [tube((0, .069, 0), .0145, .011, .08, 'pvc', axis=(0, 1, 0))] + [tube((0, yy, 0), .0155, .011, .003, 'pvc', axis=(0, 1, 0)) for yy in [.036, .043, .05, .057]], 'Connection study', 'Hose overlaps the ridged spigot. Mating bore is visible; wall profiles are illustrative.', 'Barb OD fits inside the nominal hose bore, with local interference at the ridges. Exact fitting standard and material depend on the chosen pump.')
part('hose-clamp', 'Worm-drive band, housing & screw', 'fluid', [tube((0, .047, 0), .020, .0185, .009), box((.019, .047, 0), (.013, .016, .012)), cyl((.019, .047, 0), .003, .02, axis=(0, 1, 0))], 'Connection study', 'Band sits over the hose above the inserted barb. Worm housing and screw are individually shaped.', 'Clamp type/count/torque must follow the selected hose and fitting. No high-pressure suitability is implied.')
export('hose-joint', 'Hose, barb & band clamp', 'Bench study of a physically overlapping hose/barb/clamp connection. Generic geometry, not a specified fluid circuit or pressure-rated joint.')

systems = [
    {'id': 'flotation', 'name': 'Flotation & attachments', 'note': 'Clean-room study uses 100% procedural Schedule-40 PVC pontoon tubes and 8 stainless band-clamp saddles; source study retains the four stretched catalogue tubes.'},
    {'id': 'structure', 'name': 'Pipe frame & mast', 'note': '53 mm square-section perimeter rails, four corner cross-sockets, planar X-braced + diamond deck truss, and 0.14 m central square mast column.'},
    {'id': 'rigging', 'name': 'Braces, rigging & connectors', 'note': 'Inner and outer diagonal mast stay sets with upper mast collar rings and inline Suncor-class 316-SS jaw-jaw turnbuckles.'},
    {'id': 'propulsion', 'name': 'Bilge-pump propulsion', 'note': 'Port and starboard submerged Rule 2000-class marine bilge thrusters with slotted strainers and aft 29 mm water-jet discharge nozzles.'},
    {'id': 'fluid', 'name': 'Intake, cavitation nozzle & separator', 'note': 'Central priming pump, 300-psi deck feed pump, inline 4-port Venturi Eductor with 4.20-in 316-SS 7-bore Kinetic Cavitation Nozzle, and aft-starboard Pyrolizer-Separator / DAF drum.'},
    {'id': 'power', 'name': 'Solar, storage & controls', 'note': 'Forward 2.066 × 0.519 m flexible marine monocrystalline PV array and sealed deck supercapacitor / LiFePO4 buffer module.'},
    {'id': 'wind', 'name': 'Rotor & generator', 'note': 'Three-wing cycloidal/J-profile Lenz-2 VAWT rotor on six radial spoke arms driving a sealed masthead PMG alternator.'},
]
questions = [
    {'id': 'P01', 'text': 'What is the thruster pump make/model/GPH, and does it retain the complete pump housing or drive an exposed propeller?', 'system': 'propulsion'},
    {'id': 'R01', 'text': 'Which stays are rigid metal braces and which are wire? Where do turnbuckles attach, and are their ends hook/eye/jaw?', 'system': 'rigging'},
    {'id': 'F01', 'text': 'What are the actual pontoon/frame outside diameters and socket fittings? Source part scales conflict with annotations.', 'system': 'structure'},
    {'id': 'E01', 'text': 'Which solar panel, storage device and control enclosure belong on this version? The drawn PV slab is distorted catalogue geometry.', 'system': 'power'},
    {'id': 'W01', 'text': 'Confirm operating pressure and orifice wear tolerance for the 4.20-in vs 1.06-in 316-SS 7-bore Kinetic Cavitation Nozzle and 4-port Venturi Eductor.', 'system': 'fluid'},
    {'id': 'G01', 'text': 'How does the rotor shaft connect to the generator and bearing/mast assembly?', 'system': 'wind'},
]

(D / 'catalog.json').write_text(json.dumps({
    'version': '2026-10-15-detail-2-cleanroom',
    'license': CLEAN_LICENSE,
    'origin': CLEAN_ORIGIN,
    'systems': systems,
    'studies': studies,
    'parts': records,
    'questions': questions,
}, indent=2))

with (D / 'parts-list.csv').open('w') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'System', 'Qty shown', 'Evidence', 'Description', 'Connection', 'Source'])
    for p in records.values():
        writer.writerow([p[k] for k in ['id', 'name', 'system', 'quantity', 'status', 'description', 'connection', 'source']])

(D / 'verification.json').write_text(json.dumps({
    'version': '2026-10-15-detail-2-cleanroom',
    'cleanroom_origin': CLEAN_ORIGIN,
    'cleanroom_license': CLEAN_LICENSE,
    'cleanroom_zero_3d_warehouse': all(not c['third_party'] for c in cleanroom_checks),
    'cleanroom_envelope_m': {'bbox_min_m': cr_lo, 'bbox_max_m': cr_hi, 'size_m': cr_size, 'target_size_m': manifest['machine']['size_m']},
    'cleanroom_groups': len(cleanroom_checks),
    'cleanroom_checks': cleanroom_checks,
    'kinetic_nozzle_groups': len(studies['kinetic-nozzle']['parts']),
    'source_groups': len(source_checks),
    'source_checks': source_checks,
    'assembly_groups': len(studies['assembly']['parts']),
    'study_groups': {k: len(v['parts']) for k, v in studies.items()},
    'all_part_ids_unique': len(records) == sum(len(v['parts']) for v in studies.values()),
    'units': 'metres',
    'open_questions': len(questions),
    'note': 'cleanroom and kinetic-nozzle studies are 100% procedural clean-room CAD (CERN-OHL-S-2.0 / CC-BY-SA-4.0) with zero catalogue placeholder meshes. Source assembly retained separately for provenance comparison.',
}, indent=2))

print('DETAIL BUILT', len(records), 'groups across', len(studies), 'studies; cleanroom size =', cr_size)
