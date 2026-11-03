# Guía de Modelado: Snorlax en Blender (Paso a Paso)

Esta guía detalla el flujo de trabajo estándar en Blender para modelar, texturizar, posar y renderizar a **Snorlax** con calidad profesional.

---

## 1. Preparación y Escala

1. **Configuración de vistas y referencias:**
   - En la vista frontal (`NumPad 1`), importa la imagen ortográfica: `Shift + A > Image > Reference`.
   - En la vista lateral (`NumPad 3`), repite el proceso y alinea ambos planos en el eje Z.
2. **Dimensiones:**
   - Snorlax mide oficialmente **2.10 m** de altura. Coloca un cubo de referencia de 2.1 m en Z.
   - Aplica transformaciones inmediatamente: `Ctrl + A > All Transforms`.
3. **Comprobación de normales:**
   - Activa *Face Orientation* en el menú de superposiciones (*Overlays*) para asegurar que todas las caras apunten hacia afuera (color azul).

---

## 2. Blockout (Bloqueo Inicial)

Trabaja con volúmenes separados usando modificador **Mirror** (`Clipping` activado):

- **Cuerpo y cabeza:** Empieza con una *UV Sphere* o un cubo subdividido. Ajusta la silueta en forma de pera (base muy amplia, cintura baja, cuello casi inexistente que funde directamente con la cabeza).
- **Orejas:** Primitivas cónicas o piramidales de 4 lados, orientadas hacia afuera en un ángulo aproximado de 45°.
- **Brazos y manos:** Cilindros con ligera curvatura hacia adelante y extremos redondeados.
- **Pies:** Esferas escaladas y aplanadas en la base.
- **Garras y colmillos:** Objetos separados (conos afilados con ligera curva) para mantener bordes nítidos.

---

## 3. Esculpido y Fusión Orgánica

1. **Fusión de volúmenes:**
   - Une el torso con los brazos mediante el modificador **Boolean** (modo *Union*) o usa **Voxel Remesh** (`Ctrl + R` en *Sculpt Mode*) con un tamaño de vóxel moderado (~0.02 - 0.03 m).
2. **Pinceles principales:**
   - **Smooth (`Shift`):** Suaviza las costuras de unión entre extremidades y tronco.
   - **Inflate:** Aumenta el volumen de la papada, los rollos abdominales y la base del cuerpo.
   - **Grab / Elastic Deform:** Ajusta la silueta general para capturar la postura relajada y pesada.
3. **Detalles faciales:**
   - Dibuja la hendidura de los ojos y la boca con el pincel **Draw Sharp** o **Crease**.

---

## 4. Retopología y Topología Limpia

Si esculpiste en alta densidad, genera una malla limpia basada 100% en quads (cuadriláteros):

- **Bucles clave (Edge Loops):**
  - Alrededor de los ojos y la boca.
  - Alrededor del perímetro del vientre crema (esto facilitará separar materiales o pintar texturas).
  - Anillos concéntricos en las articulaciones de hombros y piernas.
- **Modificadores finales:**
  - Aplica un modificador **Subdivision Surface** en nivel 2 (`Ctrl + 2`).
  - Clic derecho sobre la malla > **Shade Smooth**.

---

## 5. Costuras (Seams) y Desplegado UV

1. Entra en *Edit Mode* (`Tab`), selecciona las aristas de corte y pulsa `Right Click > Mark Seam`.
2. **Puntos de corte recomendados:**
   - Línea dorsal central: desde la nuca hasta la base del coxis.
   - Perímetro inferior de los pies (isla separada para la planta).
   - Anillos de corte en la base de las orejas y brazos.
3. **Desplegado:**
   - Selecciona todo (`A`) y pulsa `U > Unwrap`.
   - En el *UV Editor*, ve a `UV > Pack Islands` asegurando un margen de separación (*Margin* ~0.005) para evitar sangrado de textura.

---

## 6. Sombreado y Materiales (Shader Setup)

Configura el material en el **Shader Editor** utilizando el nodo **Principled BSDF**:

### Piel Principal (Azul verdoso oscuro)
- **Base Color:** `#1B3B4B` (ajustable a gusto).
- **Subsurface Weight:** `0.05 - 0.1` (le otorga suavidad orgánica).
- **Subsurface Radius:** `[1.0, 0.2, 0.1]` (dispersión cálida/rojiza).
- **Roughness:** `0.65 - 0.75` (superficie mate sin brillos reflectantes duros).

### Vientre y Rostro (Tono Crema)
- **Base Color:** `#F3E5AB` o `#EAD8B1`.
- **Subsurface Weight:** `0.08`.
- **Roughness:** `0.60`.

### Garras y Dientes
- **Base Color:** Blanco hueso/marfil (`#FDFBF7`).
- **Roughness:** `0.30 - 0.40`.

---

## 7. Posa, Iluminación y Render

1. **Rigging básico:**
   - Añade una armadura simple con huesos para columna, cabeza, brazos y pies.
   - Emparenta la malla: `Ctrl + P > With Automatic Weights`.
   - Alternativa rápida: usa el pincel **Pose** directamente en *Sculpt Mode*.
2. **Esquema de iluminación (3 Puntos):**
   - **Key Light:** Área grande lateral para sombras suaves.
   - **Fill Light:** Intensidad baja en el lado opuesto para levantar sombras profundas.
   - **Rim Light (Contraluz):** Detrás de Snorlax, con mayor potencia, para recortar su silueta oscura contra el fondo.
3. **Ajustes de Render:**
   - Motor: **Cycles**.
   - Denoising: **OpenImageDenoise** activado.
   - Color Management: **AgX** o **Filmic** con contraste medio-alto.