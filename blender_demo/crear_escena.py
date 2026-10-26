import bpy
import math

# Limpiar escena
bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# Configurar motor de render (Cycles en CPU es muy fiable en modo headless)
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 32
scene.render.resolution_x = 800
scene.render.resolution_y = 600

# 1. Crear un suelo
bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, -1))
floor = bpy.context.active_object
floor_mat = bpy.data.materials.new(name="FloorMat")
floor_mat.use_nodes = True
bsdf_floor = floor_mat.node_tree.nodes.get("Principled BSDF")
if bsdf_floor:
    bsdf_floor.inputs["Base Color"].default_value = (0.1, 0.1, 0.15, 1.0)
    bsdf_floor.inputs["Roughness"].default_value = 0.2
floor.data.materials.append(floor_mat)

# 2. Crear a Suzanne (la mascota de Blender) con modificador Subdivision
bpy.ops.mesh.primitive_monkey_add(location=(0, 0, 0), size=1.5)
monkey = bpy.context.active_object
bpy.ops.object.shade_smooth()

subsurf = monkey.modifiers.new(name="Subdivision", type='SUBSURF')
subsurf.levels = 2
subsurf.render_levels = 2

# Material para Suzanne: dorado metalizado
monkey_mat = bpy.data.materials.new(name="GoldMat")
monkey_mat.use_nodes = True
bsdf_monkey = monkey_mat.node_tree.nodes.get("Principled BSDF")
if bsdf_monkey:
    bsdf_monkey.inputs["Base Color"].default_value = (1.0, 0.76, 0.33, 1.0)
    bsdf_monkey.inputs["Metallic"].default_value = 0.9
    bsdf_monkey.inputs["Roughness"].default_value = 0.2
monkey.data.materials.append(monkey_mat)

# 3. Luces (Key light y Fill/Rim light)
# Key Light (luz calida)
bpy.ops.object.light_add(type='POINT', location=(3, -3, 3))
key_light = bpy.context.active_object
key_light.data.energy = 500
key_light.data.color = (1.0, 0.9, 0.8)

# Rim Light (luz azulada desde atras)
bpy.ops.object.light_add(type='POINT', location=(-3, 2, 2))
rim_light = bpy.context.active_object
rim_light.data.energy = 300
rim_light.data.color = (0.2, 0.6, 1.0)

# 4. Camara apuntando al centro
bpy.ops.object.camera_add(location=(0, -4.5, 1.2), rotation=(math.radians(78), 0, 0))
camera = bpy.context.active_object
scene.camera = camera

# Guardar archivo .blend
blend_path = "blender_demo/ejemplo_suzanne.blend"
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"Archivo .blend guardado en: {blend_path}")

# Renderizar imagen
render_path = "blender_demo/render_suzanne.png"
scene.render.filepath = render_path
bpy.ops.render.render(write_still=True)
print(f"Render guardado en: {render_path}")
