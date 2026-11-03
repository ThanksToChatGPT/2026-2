# Registro de Actividades - Snorlax (Blender)

Bitácora de tareas, transformaciones y avances realizados en Blender para el modelado de Snorlax.

---

## Entrada 1 - Paso 1: Preparación y Escala
- **Acción realizada:**
  - **Configuración de vistas y planos de referencia:**
    - Se crearon los objetos Empty de tipo imagen `Ref_Front` (vista frontal para `NumPad 1`, rotación `(90°, 0, 0)`) y `Ref_Side` (vista lateral para `NumPad 3`, rotación `(90°, 0, -90°)`, con el vientre apuntando hacia el eje -Y).
    - Ambos planos se alinearon matemáticamente en el eje Z a `(0, 0, 1.2042 m)` con un `empty_display_size` de 3.0252 m, logrando que los pies de Snorlax queden exactamente en Z = 0.00 m y la punta de las orejas en Z = 2.10 m.
    - Se configuró opacidad al 70% con `DOUBLE_SIDED` y visualización en vistas ortográficas y perspectiva.
  - **Cubo de referencia de dimensiones oficiales:**
    - Se configuró el cubo de referencia con 2.10 m en Z (2.10 x 2.10 x 2.10 m), con su base en Z = 0.00 m y su parte superior en Z = 2.10 m, envolviendo exactamente los límites del modelo de referencia.
    - Se renombró a `Cubo_Referencia_2.1m`.
    - Se aplicaron todas las transformaciones (`Ctrl + A > All Transforms`), dejando la posición en `(0, 0, 0)`, rotación `(0, 0, 0)` y escala en `(1.0, 1.0, 1.0)`.
  - **Comprobación de normales:**
    - Se normalizaron y recalcularon las caras hacia el exterior (`normals_make_consistent(inside=False)`).
    - Se activó *Face Orientation* en los overlays del viewport (`space.overlay.show_face_orientation = True`), comprobando que todas las caras se visualizan en color azul uniforme.
  - **Guardado:** Se persistieron todos los cambios en `Snorlax.blend`.
- **Estado de la escena:**
  - Total objetos: 5 (`Cubo_Referencia_2.1m`, `Ref_Front`, `Ref_Side`, `Light`, `Camera`)
  - Modo activo: `OBJECT`
  - Orientación de normales: Verificada (Azul)

---

## Entrada 2 - Paso 2: Blockout (Bloqueo Inicial)
- **Fecha y Hora:** 2026-11-01 21:25 (COT / UTC-5)
- **Acción realizada:**
  - **Organización y Visibilidad:** Se configuró el cubo de escala `Cubo` en modo de visualización de aristas (`display_type = 'WIRE'`) para permitir la visibilidad completa del modelo y las imágenes de referencia ortográficas sin estorbar el bloqueo.
  - **Construcción de Volúmenes Separados (Blockout):**
    - `Snorlax_Cuerpo_Cabeza`: Malla estructurada 100% en cuadriláteros (*quads*) sobre el semieje $+X$, acoplada a los contornos frontal y lateral de la referencia. Se modeló la silueta en forma de pera: base amplia ($Z = 0.16\text{ m}$ a $0.35\text{ m}$), ensanchamiento máximo del abdomen en $Z \approx 0.75\text{ m}$ (ancho $1.76\text{ m}$, profundidad $1.40\text{ m}$ con vientre prominente hacia $-Y$), transición de cuello casi imperceptible en $Z \approx 1.48\text{ m}$, cabeza redondeada con pómulos anchos ($Z \approx 1.60\text{ m}$) y coronilla en $Z = 1.88\text{ m}$.
    - `Snorlax_Orejas`: Primitiva piramidal de 4 lados orientada hacia afuera a $\sim 45^\circ$, conectando en la base superior de la cabeza en $Z = 1.76\text{ m}$ y alcanzando el vértice en $Z = 2.10\text{ m}$ en concordancia con el límite del cubo de escala.
    - `Snorlax_Brazos`: Geometría cilíndrica de 8 segmentos a lo largo de una curva anatómica con hombro ($Z = 1.28\text{ m}$), codo orientado hacia afuera y adelante ($Z = 0.98\text{ m}$, envergadura $2.29\text{ m}$), y muñeca/mano curvada descansando sobre la parte baja del abdomen ($Z = 0.71\text{ m}$).
    - `Snorlax_Pies`: Cuerpos esféricos escalados ($X = 0.38\text{ m}$, $Y = 0.64\text{ m}$, $Z = 0.18\text{ m}$) con base totalmente plana apoyada sobre el plano de tierra ($Z = 0.00\text{ m}$), centrados en $X = \pm 0.68\text{ m}$.
    - `Snorlax_Garras_Manos`: 5 garras cónicas por mano distribuidas a lo largo del arco frontal de la mano ($Z \approx 0.70\text{ m}$), afiladas y curvadas hacia adentro.
    - `Snorlax_Garras_Pies`: 3 conos afilados por pie orientados hacia adelante y abajo en el extremo frontal del pie ($Z \approx 0.03\text{ m}$).
    - `Snorlax_Colmillos`: 2 conos afilados en las comisuras inferiores de la boca ($Z \approx 1.66\text{ m}$ a $1.75\text{ m}$), orientados hacia arriba y ligeramente hacia afuera.
  - **Modificadores y Transformaciones:**
    - Se aplicó el modificador **Mirror** en el eje $X$ con **Clipping** activado en todos los componentes para garantizar simetría bilateral limpia y soldadura estricta en el plano central $X=0$.
    - Se aplicaron todas las transformaciones (`Ctrl + A > All Transforms`) en cada objeto, dejando sus orígenes en `(0, 0, 0)` y escala en `(1.0, 1.0, 1.0)`.
    - Se asignó modificador **Subdivision Surface** (nivel 1 en viewport, 2 en render) y sombreado suave (**Shade Smooth**) al cuerpo, orejas, brazos y pies. Las garras y colmillos se conservaron con sombreado plano (**Shade Flat**) para preservar bordes nítidos.
  - **Materiales Base de Previsualización:**
    - Se crearon y asignaron materiales basados en nodos Principled BSDF: `Mat_Piel_Principal` (azul verdoso oscuro `#1B3B4B`), `Mat_Crema` (tono crema `#EAD8B1`) y `Mat_Garras_Dientes` (blanco hueso `#FDFBF7`).
  - **Persistencia:** Guardado del archivo [Snorlax.blend](file:///c:/Users/Computador/2026-2/Computacion%20visual/Snorlax/Snorlax.blend).

---

### Guía de Herramientas de Blender para la Creación Manual del Modelo

Para recrear manualmente este paso dentro de la interfaz de Blender, el artista 3D debe emplear las siguientes herramientas, atajos y modificadores:

| Fase / Tarea | Herramienta en Blender | Atajo de Teclado | Descripción de Uso |
|---|---|---|---|
| **Navegación y Vistas** | Vista Frontal / Lateral / Superior | `NumPad 1` / `NumPad 3` / `NumPad 7` | Alinear el viewport con las imágenes de referencia para calcar las siluetas ortográficas. |
| **Modo Rayos X** | X-Ray Toggle | `Alt + Z` | Permitir ver a través de las mallas y seleccionar vértices ocultos mientras se visualiza la imagen de referencia. |
| **Adición de Primitivas** | Add Mesh | `Shift + A > Mesh` | Insertar las primitivas base: *Cube* / *UV Sphere* (Cuerpo), *Cone* con 4 lados (Orejas), *Cylinder* (Brazos), *Cone* (Garras/Colmillos). |
| **Modo Edición** | Edit Mode Toggle | `Tab` | Alternar entre Object Mode y Edit Mode para transformar geometría. |
| **Selección de Componentes** | Vértices / Bordes / Caras | `1` / `2` / `3` (teclado superior) | Cambiar el modo de selección para manipular anillos de aristas o caras individuales. |
| **Corte de Simetría** | Loop Cut and Slide | `Ctrl + R` | Insertar un bucle central en el eje $X=0$. Luego seleccionar la mitad izquierda ($X < 0$) y borrar con `X > Vertices`. |
| **Modificador Mirror** | Mirror Modifier | Menú *Modifiers* > *Mirror* | Activar simetría en eje $X$. **Imprescindible activar la casilla `Clipping`** para que los vértices centrales no se separen ni crucen el eje de simetría. |
| **Modelado de Silueta (Pera)** | Loop Cut + Proportional Editing | `Ctrl + R` + `O` | Añadir 10 a 14 bucles horizontales a lo largo del torso. Con `O` (Proportional Editing en modo *Smooth*), mover (`G`) y escalar (`S` o `S + Shift + Z`) para engordar el abdomen hacia adelante (`G + Y`) y estrechar el cuello. |
| **Extrusión de Brazos** | Extrude Region | `E` | Extruir un círculo cilíndrico desde el hombro siguiendo la trayectoria del brazo hacia el codo, antebrazo y mano, rotando (`R`) y escalando (`S`) en cada sección. |
| **Aplanado de Base de Pies** | Flatten to Floor | `S + Z + 0` | En Edit Mode, seleccionar los vértices de la parte inferior de la esfera del pie y presionar `S`, luego `Z`, luego `0` para proyectarlos planos en $Z = 0.00\text{ m}$. |
| **Alineación y Orientación** | Rotate / Scale / Move | `R` / `S` / `G` | Rotar las orejas $45^\circ$ hacia afuera (`R + Y`), orientar los colmillos hacia arriba y curvar las garras hacia el centro. |
| **Aplicación de Transformaciones** | Apply All Transforms | `Ctrl + A > All Transforms` | **Obligatorio tras rotar o mover objetos en Object Mode** antes de usar Mirror o Subdivision, restableciendo origen a `(0,0,0)` y escala a `(1,1,1)`. |
| **Suavizado y Subdivisión** | Subdivision Surface | `Ctrl + 1` o `Ctrl + 2` | Añadir modificador de subdivisión Catmull-Clark para suavizar las formas orgánicas. Clic derecho en la malla > **Shade Smooth**. Para las garras, mantener **Shade Flat**. |

- **Estado de la escena:**
  - Total objetos: 12 (1 cámara, 1 luz, 2 empties de referencia, 1 cubo guía en wireframe, 7 mallas del blockout de Snorlax).
  - Componentes del modelo: `Snorlax_Cuerpo_Cabeza`, `Snorlax_Orejas`, `Snorlax_Brazos`, `Snorlax_Pies`, `Snorlax_Garras_Manos`, `Snorlax_Garras_Pies`, `Snorlax_Colmillos`.
  - Modo activo: `OBJECT`
  - Orientación de normales: Verificada (Azul)

---

## Entrada 3 - Corrección y Calibración Fina del Blockout
- **Fecha y Hora:** 2026-11-01 21:40 (COT / UTC-5)
- **Diagnóstico y Corrección de Discrepancias:**
  1. **Orejas:** En el intento inicial las puntas se habían situado en $X = \pm 0.52\text{ m}$, sobresaliendo en exceso de la cabeza. Se recalibraron exactamente a $X = \pm 0.36\text{ m}$, $Y = 0.04\text{ m}$, $Z = 2.08\text{ m}$, con una base ancha asentada sobre los laterales superiores del cráneo coincidiendo con la referencia.
  2. **Cabeza y Cuello:** Se eliminó la hendidura artificial del cuello que creaba un aspecto de muñeco de nieve. Se reconstruyó la transición continua en forma de pera orgánica sin estrangulamiento ($R_x \approx 0.50\text{ m}$ continuo entre cuello y mejillas), con pómulos anchos y coronilla con una leve depresión central en $Z = 1.91\text{ m}$ entre orejas.
  3. **Brazos y Manos:** Los brazos se habían curvado hacia el frente del vientre. Se corrigió su trayectoria para que desciendan rectos a lo largo de los flancos laterales del cuerpo ($Y \approx 0.00\text{ m}$ constante), alcanzando la envergadura de codos en $X \approx 1.14\text{ m}$ y rematando en manos redondeadas a los lados con sus 5 garras apuntando hacia abajo/adentro en $Z \approx 0.68\text{ m}$.
  4. **Pies:** Estaban desplazados hacia afuera ($X = 0.68\text{ m}$); se reposicionaron en $X = \pm 0.52\text{ m}$ (amplitud $X \in [0.25\text{ m}, 0.79\text{ m}]$) asentados bajo la curva inferior del vientre y planos sobre el suelo en $Z = 0.00\text{ m}$, con 3 garras frontales por pie.
  5. **Colmillos:** Se ajustó su posición a las comisuras bucales exactas en $X = \pm 0.13\text{ m}$ (en vez de $0.22\text{ m}$), apuntando hacia arriba desde $Z = 1.67\text{ m}$ hasta $1.74\text{ m}$.
- **Acción realizada:**
  - Regeneración completa de los 7 volúmenes anatómicos con los bucles acoplados pixel a pixel a las siluetas ortográficas frontal y lateral.
  - Modificador **Mirror** con `Clipping` activo en todos los elementos.
  - Aplicación de todas las transformaciones (`All Transforms`) dejando orígenes limpios en `(0, 0, 0)`.
  - Guardado en [Snorlax.blend](file:///c:/Users/Computador/2026-2/Computacion%20visual/Snorlax/Snorlax.blend).
- **Estado de la escena:**
  - Total objetos: 12 (1 cámara, 1 luz, 2 empties de referencia, 1 cubo guía en wireframe, 7 mallas de bloqueo corregidas).
  - Silueta: Calibrada y acoplada a las vistas ortográficas de referencia.

---

## Entrada 4 - Ajuste de Contracción por Subdivisión (Ears, Arms, Feet & Silhouette)
- **Fecha y Hora:** 2026-11-01 21:45 (COT / UTC-5)
- **Diagnóstico del problema:**
  - Al activar el modificador *Subdivision Surface* (Catmull-Clark), las primitivas de baja resolución sufrían contracción geométrica:
    1. Las orejas perdían casi $20\text{ cm}$ de altura en su cúspide, quedando como pequeños muñones redondeados por debajo de la coronilla.
    2. Los brazos se adelgazaban excesivamente, perdiendo el volumen macizo que llena la silueta de la referencia.
    3. La base del vientre quedaba estrecha respecto a la postura pesada de Snorlax.
    4. Los pies se encogían hacia adentro en lugar de asomar lateralmente bajo el abdomen con sus 3 dedos.
- **Acciones Correctivas:**
  - **Orejas reforzadas:** Se introdujeron bucles de soporte intermedios en $Z = 2.06\text{ m}$ y $Z = 1.95\text{ m}$ para anclar la punta piramidal, garantizando que tras la subdivisión el vértice evaluado alcance exactamente $Z = 2.08\text{ m} \approx 2.10\text{ m}$ y $X = \pm 0.365\text{ m}$, coincidiendo plenamente con el contorno de la referencia.
  - **Brazos y Garras:** Se compensó el radio anatómico del brazo (hombro a codo con radio de $0.22\text{ m}$ a $0.25\text{ m}$), alcanzando el codo en $X \approx 1.02\text{ m}$ y reubicando las 5 garras en el borde exterior inferior de la mano en $X \in [0.80\text{ m}, 1.06\text{ m}]$.
  - **Cuerpo y Vientre:** Se aumentó la amplitud del paunch abdominal ($R_x = 0.90\text{ m}$, profundidad $1.46\text{ m}$) para que tras subdividirse mantenga el volumen completo de la silueta morada.
  - **Pies Exteriores:** Se reubicó el centro de cada pie a $X = \pm 0.62\text{ m}$ con amplitud $X \in [0.38\text{ m}, 0.86\text{ m}]$, sobresaliendo con firmeza bajo el abdomen y apoyados planos en $Z = 0.00\text{ m}$ con 3 garras frontales ($X = 0.50, 0.64, 0.78\text{ m}$).
- **Persistencia:** Guardado en [Snorlax.blend](file:///c:/Users/Computador/2026-2/Computacion%20visual/Snorlax/Snorlax.blend).
- **Estado de la escena:**
  - Total objetos: 12.
  - Verificación en viewport: Malla coincidente con los límites del cubo de 2.10 m y la ilustración de referencia.






