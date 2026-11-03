---
name: blender
description: >-
  Guía para trabajar en Blender mediante el MCP de Blender (ejecución de scripts bpy,
  inspección de escena, capturas de vista) y registrar obligatoriamente cada acción
  realizada en registros.md dentro de la carpeta.
---

# Skill: Blender (MCP y Registro de Actividades)

Esta skill define el protocolo de trabajo para las tareas de modelado 3D, materiales, iluminación y renderizado en Blender para el proyecto.

## 1. Uso Obligatorio del MCP de Blender

Se tienen las herramientas del MCP:
- **`execute_blender_code`**: Ejecución de código Python con `bpy` (creación de geometrías, transformaciones, modificadores, configuración de nodos y materiales).
- **`get_scene_info`**: Inspección del estado actual de la escena (conteo de objetos, jerarquías, dimensiones, modo).
- **`look`**: Captura visual del viewport o renderizado para verificar proporciones y resultados.
- **`get_addon_status`**: Verificación de conectividad con la sesión activa de Blender.

### Buenas Prácticas con la API `bpy`:
- Buscar nodos de sombreado por tipo (`BSDF_PRINCIPLED`), nunca por nombre localizado.
- Aplicar transformaciones (`bpy.ops.object.transform_apply`) al rotar o escalar antes de usar modificadores orgánicos (*Mirror*, *Subdivision*, *Remesh*).
- Guardar los cambios en el archivo `.blend` periódicamente (`bpy.ops.wm.save_mainfile()`).

## 2. Registro Obligatorio en `registros.md`

Tras cada intervención o avance relevante en Blender, documentar de forma clara y concisa en `Snorlax/registros.md`:
- **Fecha y Hora**: Momento de la intervención.
- **Acción realizada**: Descripción de los cambios (mallas creadas, modificadores aplicados, materiales configurados, etc.).
- **Estado de la escena**: Resumen del estado actual

