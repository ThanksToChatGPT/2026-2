# Especificación de Requerimientos de Software (ERS)

**Proyecto:** Agregador de Moda, Comparador de Precios y Creador de Outfits  
**Materia:** Ingeniería de Software II  
**Fuente Base:** [Historias de Usuario](./Historias_de_Usuario.md) (77 Historias de Usuario distribuidas en 9 Épicas)  
**Versión:** 1.0  
**Fecha:** 2026-09-29  

---

## 1. Introducción y Alcance del Sistema

### 1.1 Propósito
El presente documento define la especificación formal de los **Requerimientos Funcionales (RF)** y **Requerimientos No Funcionales (RNF)** para la plataforma de agregación de prendas de vestir, recomendación personalizada, comparación de precios en pesos colombianos (COP) y ensamblador visual de conjuntos (*Outfit Builder*).

### 1.2 Actores del Sistema
- **Visitante (Guest):** Usuario no registrado que navega, busca y aplica filtros en el catálogo de prendas sin persistencia de datos.
- **Usuario Registrado (User):** Usuario autenticado que gestiona su perfil, configura preferencias de estilo y presupuesto, arma y almacena outfits personalizados, guarda favoritos y genera listas de compra.
- **Administrador (Admin):** Usuario con privilegios de gestión sobre las fuentes de datos (tiendas), ejecución y monitoreo de procesos de extracción (*scraping*), moderación de catálogo, resolución de reportes de inconsistencias y visualización de analíticas.
- **Sistema Externo (Tiendas de Comercio Electrónico):** Plataformas web de las tiendas de moda desde las cuales se extraen los catálogos y a las cuales se redirige al usuario final para la compra.

---

## 2. Requerimientos Funcionales (RF)

Los requerimientos funcionales se encuentran categorizados por los módulos derivados de las épicas del proyecto, clasificados bajo la metodología **MoSCoW** (Must, Should, Could, Would) y trazados directamente a las Historias de Usuario correspondientes.

```
Leyenda de Prioridad MoSCoW:
- [MUST]   : Requisito obligatorio / crítico para el MVP.
- [SHOULD] : Requisito importante de alta prioridad.
- [COULD]  : Requisito deseable si hay recursos disponibles.
- [WOULD]  : Requisito postergable para futuras versiones.
```

---

### Módulo 1: Cuentas, Autenticación y Perfil de Usuario

#### RF-01: Registro de cuenta local
- **Código:** RF-01
- **Trazabilidad:** US-1
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir a nuevos usuarios registrarse mediante correo electrónico válido y contraseña segura. Debe validar que el correo no esté registrado previamente y que la contraseña cumpla con las políticas de seguridad.
- **Entradas:** Correo electrónico, contraseña, confirmación de contraseña.
- **Salidas:** Cuenta creada con confirmación y redirección a sesión activa o inicio de sesión.

#### RF-02: Autenticación y gestión de sesiones
- **Código:** RF-02
- **Trazabilidad:** US-2
- **Prioridad:** MUST
- **Descripción:** El sistema debe autenticar las credenciales del usuario (correo y contraseña) para iniciar sesión de forma segura y permitir el cierre explícito de la sesión en cualquier momento, destruyendo los tokens o sesiones activas. Ante credenciales incorrectas, debe emitir un mensaje de error descriptivo sin comprometer la seguridad.
- **Entradas:** Correo electrónico, contraseña.
- **Salidas:** Token de sesión/sesión iniciada con acceso al perfil, o mensaje de error.

#### RF-03: Autenticación federada con Google
- **Código:** RF-03
- **Trazabilidad:** US-3
- **Prioridad:** COULD
- **Descripción:** El sistema debe ofrecer la opción de iniciar sesión o registrarse utilizando una cuenta de Google mediante el protocolo OAuth 2.0 / OpenID Connect, vinculando automáticamente la identidad del usuario.
- **Entradas:** Token de identidad emitido por el proveedor Google.
- **Salidas:** Sesión iniciada y cuenta de usuario sincronizada/creada.

#### RF-04: Recuperación de contraseña por correo electrónico
- **Código:** RF-04
- **Trazabilidad:** US-4
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir solicitar el restablecimiento de contraseña mediante el envío de un enlace único temporal al correo electrónico registrado. Dicho enlace debe contar con un tiempo de expiración programado.
- **Entradas:** Correo electrónico registrado.
- **Salidas:** Envío de correo con enlace de recuperación criptográficamente seguro con tiempo de vida limitado.

#### RF-05: Modificación de datos del perfil
- **Código:** RF-05
- **Trazabilidad:** US-5
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir al usuario autenticado visualizar y editar sus datos personales básicos (nombre completo, correo electrónico, país y tallas predeterminadas) y reflejar los cambios de inmediato.
- **Entradas:** Nombre, correo, país, medidas/tallas estándar.
- **Salidas:** Registro de usuario actualizado en base de datos e interfaz refrescada.

#### RF-06: Eliminación definitiva de cuenta y datos personales
- **Código:** RF-06
- **Trazabilidad:** US-6
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir al usuario solicitar la eliminación permanente de su cuenta, exigiendo una confirmación explícita previa y ejecutando el borrado de sus datos personales, preferencias y conjuntos guardados conforme al derecho de supresión.
- **Entradas:** Confirmación explícita del usuario (reautenticación o diálogo de confirmación).
- **Salidas:** Eliminación de los registros personales y cierre de sesión definitivo.

#### RF-07: Navegación y búsqueda sin cuenta (Modo Visitante)
- **Código:** RF-07
- **Trazabilidad:** US-7
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir a usuarios no autenticados explorar el catálogo, buscar prendas y aplicar filtros. Si el visitante intenta guardar favoritos o crear outfits persistentes, el sistema debe solicitar el registro o inicio de sesión.
- **Entradas:** Interacciones de búsqueda del visitante.
- **Salidas:** Resultados visibles en modo solo lectura; advertencia o modal de registro ante acciones que requieran persistencia.

---

### Módulo 2: Configuración y Gestión de Preferencias de Estilo

#### RF-08: Asistente guiado de configuración inicial (Onboarding)
- **Código:** RF-08
- **Trazabilidad:** US-8
- **Prioridad:** SHOULD
- **Descripción:** Al iniciar sesión por primera vez, el sistema debe presentar un asistente guiado paso a paso para configurar preferencias clave (marcas, colores, tallas, presupuesto). El usuario debe tener la opción de omitir el asistente y completarlo posteriormente.
- **Entradas:** Respuestas del usuario en el formulario guiado o acción de omitir (*Skip*).
- **Salidas:** Preferencias iniciales almacenadas o redirección directa al catálogo principal.

#### RF-09: Selección y priorización de marcas favoritas
- **Código:** RF-09
- **Trazabilidad:** US-9
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir al usuario seleccionar una o múltiples marcas de su preferencia desde un listado y ponderar los resultados de búsqueda para presentar dichas marcas en las primeras posiciones.
- **Entradas:** Lista de identificadores de marcas seleccionadas.
- **Salidas:** Preferencias guardadas y reordenamiento de relevancia en búsquedas.

#### RF-10: Selección de colores favoritos
- **Código:** RF-10
- **Trazabilidad:** US-10
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir elegir una paleta de colores preferidos mediante una interfaz visual o lista de tonos, almacenándolos en el perfil para ajustar sugerencias cromáticas.
- **Entradas:** Selección de colores/códigos cromáticos.
- **Salidas:** Lista de colores preferidos asociada al perfil.

#### RF-11: Definición de rango de precios preferente
- **Código:** RF-11
- **Trazabilidad:** US-11
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir al usuario establecer un valor de precio mínimo y máximo por prenda, restringiendo o priorizando los productos mostrados dentro de dicho intervalo.
- **Entradas:** Valor numérico de precio mínimo y máximo en COP.
- **Salidas:** Rango de precios almacenado y aplicado en consultas.

#### RF-12: Registro de tallas por categoría de prenda
- **Código:** RF-12
- **Trazabilidad:** US-12
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe almacenar las tallas habituales del usuario discriminadas por categoría: prendas superiores (top), prendas inferiores (bottom) y calzado (shoes), facilitando el prefiltrado de productos con stock en dichas medidas.
- **Entradas:** Tallas seleccionadas por tipo de prenda (ej. Superior: M, Inferior: 32, Calzado: 40).
- **Salidas:** Perfil de tallas del usuario actualizado.

#### RF-13: Preferencia de corte y silueta (Fit)
- **Código:** RF-13
- **Trazabilidad:** US-13
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir al usuario seleccionar uno o más tipos de ajuste o silueta deseada (*oversized*, *slim*, *regular*, etc.) para ser utilizados en los filtros de recomendación.
- **Entradas:** Tipos de ajuste seleccionados.
- **Salidas:** Criterios de corte asociados al perfil del usuario.

#### RF-14: Configuración de presupuesto máximo por outfit
- **Código:** RF-14
- **Trazabilidad:** US-14
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir fijar un límite presupuestal global para la composición de un outfit completo, disparando alertas cuando la suma de las prendas del conjunto supere dicho monto.
- **Entradas:** Monto máximo de presupuesto en COP.
- **Salidas:** Presupuesto tope registrado y utilizado por el verificador del constructor de outfits.

#### RF-15: Actualización dinámica de preferencias
- **Código:** RF-15
- **Trazabilidad:** US-15
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir consultar y modificar las preferencias en cualquier momento desde el módulo de configuración, actualizando de forma inmediata las recomendaciones y ponderaciones mostradas al usuario.
- **Entradas:** Nuevos valores de preferencias.
- **Salidas:** Persistencia inmediata y recálculo reactivo de sugerencias.

#### RF-16: Restablecimiento de preferencias a valores por defecto
- **Código:** RF-16
- **Trazabilidad:** US-16
- **Prioridad:** COULD
- **Descripción:** El sistema debe proveer una opción para limpiar y reiniciar todas las preferencias guardadas a su estado inicial, solicitando confirmación previa al usuario.
- **Entradas:** Acción de reseteo y confirmación.
- **Salidas:** Vaciado de preferencias del usuario en base de datos.

#### RF-17: Visualización resumida de preferencias
- **Código:** RF-17
- **Trazabilidad:** US-17
- **Prioridad:** MUST
- **Descripción:** El sistema debe mostrar en el perfil del usuario un panel unificado con el resumen consolidado de todas sus preferencias activas (marcas, colores, tallas, presupuesto y cortes).
- **Entradas:** Solicitud de visualización de perfil.
- **Salidas:** Vista consolidada de parámetros de preferencia.

---

### Módulo 3: Búsqueda, Filtrado y Exploración del Catálogo

#### RF-18: Búsqueda textual libre de prendas
- **Código:** RF-18
- **Trazabilidad:** US-18
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir realizar búsquedas mediante texto libre (ej. *"pantalón cargo negro"*), comparando las palabras clave contra títulos, marcas, categorías y descripciones de las prendas.
- **Entradas:** Cadena de texto ingresada en la barra de búsqueda.
- **Salidas:** Listado de productos coincidentes ordenados por relevancia.

#### RF-19: Agregación y visualización multitienda
- **Código:** RF-19
- **Trazabilidad:** US-19
- **Prioridad:** MUST
- **Descripción:** El sistema debe mostrar en una única interfaz de resultados productos provenientes de dos o más tiendas externas diferentes, mostrando en cada tarjeta de producto el logo o nombre visible del comercio de procedencia.
- **Entradas:** Parámetros de búsqueda o catálogo general.
- **Salidas:** Listado unificado multitienda con metadata de origen.

#### RF-20: Filtrado por rango de precios
- **Código:** RF-20
- **Trazabilidad:** US-20
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir acotar los resultados de búsqueda mediante controles deslizantes (*slider*) o entradas numéricas de precio mínimo y máximo en COP.
- **Entradas:** Rango numérico [precio_min, precio_max].
- **Salidas:** Catálogo filtrado en tiempo real según el rango estipulado.

#### RF-21: Filtrado multiselección por marca
- **Código:** RF-21
- **Trazabilidad:** US-21
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir filtrar los resultados seleccionando una o múltiples marcas específicas de manera simultánea.
- **Entradas:** Conjunto de marcas seleccionadas.
- **Salidas:** Productos pertenecientes exclusivamente a las marcas indicadas.

#### RF-22: Filtrado por color
- **Código:** RF-22
- **Trazabilidad:** US-22
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir filtrar las prendas según uno o varios colores estándar homologados en el catálogo.
- **Entradas:** Colores seleccionados en la barra de filtros.
- **Salidas:** Productos cuyo atributo de color coincida con la selección.

#### RF-23: Filtrado por talla y disponibilidad
- **Código:** RF-23
- **Trazabilidad:** US-23
- **Prioridad:** MUST
- **Descripción:** El sistema debe filtrar el catálogo mostrando únicamente aquellas prendas que cuenten con stock confirmado en la talla seleccionada.
- **Entradas:** Talla(s) requerida(s).
- **Salidas:** Productos con disponibilidad activa en dicha talla.

#### RF-24: Filtrado jerárquico por categoría de prenda
- **Código:** RF-24
- **Trazabilidad:** US-24
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir filtrar por categoría principal (superior, inferior, calzado, accesorios) y por subcategorías específicas (chaqueta, buzo, camiseta, jeans, bermudas, etc.).
- **Entradas:** Categoría o subcategoría seleccionada.
- **Salidas:** Prendas clasificadas bajo la taxonomía elegida.

#### RF-25: Filtrado por material textil
- **Código:** RF-25
- **Trazabilidad:** US-25
- **Prioridad:** COULD
- **Descripción:** El sistema debe permitir filtrar prendas según su composición de material (ej. algodón, denim, lino, poliéster) siempre que dicha información se encuentre disponible en los metadatos de la tienda fuente.
- **Entradas:** Material seleccionado.
- **Salidas:** Productos confeccionados con el material especificado.

#### RF-26: Filtrado por tienda externa
- **Código:** RF-26
- **Trazabilidad:** US-26
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir incluir o excluir de la búsqueda una o más tiendas específicas a elección del usuario.
- **Entradas:** Tiendas seleccionadas / desmarcadas.
- **Salidas:** Resultados filtrados según el origen comercial.

#### RF-27: Ordenamiento de resultados
- **Código:** RF-27
- **Trazabilidad:** US-27
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir reordenar los resultados de búsqueda por criterios de precio ascendente (menor a mayor), precio descendente (mayor a menor) y relevancia.
- **Entradas:** Criterio de orden seleccionado.
- **Salidas:** Lista de productos reordenada de acuerdo con el criterio.

#### RF-28: Limpieza global de filtros
- **Código:** RF-28
- **Trazabilidad:** US-28
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe proveer una acción de un solo clic (*Limpiar filtros*) que restablezca todos los filtros aplicados a sus valores predeterminados sin reiniciar el término de búsqueda base.
- **Entradas:** Clic en botón "Limpiar filtros".
- **Salidas:** Estado de filtros reiniciado y catálogo actualizado.

#### RF-29: Personalización y ponderación de resultados según perfil
- **Código:** RF-29
- **Trazabilidad:** US-29
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe ponderar y priorizar en los primeros lugares de la búsqueda los productos que coincidan con las marcas, colores, tallas y rango de precios del usuario autenticado, permitiendo habilitar o deshabilitar dicha personalización mediante un conmutador (*toggle*).
- **Entradas:** Estado del conmutador de personalización y preferencias del usuario.
- **Salidas:** Resultados reordenados por ponderación personalizada o catálogo neutral estándar.

#### RF-30: Historial y eliminación de búsquedas recientes
- **Código:** RF-30
- **Trazabilidad:** US-30
- **Prioridad:** COULD
- **Descripción:** El sistema debe registrar las últimas búsquedas efectuadas por el usuario, desplegándolas al enfocar la barra de búsqueda y permitiendo al usuario eliminar elementos individuales de dicho historial.
- **Entradas:** Consultas anteriores; acción de borrado de elemento.
- **Salidas:** Menú desplegable con términos recientes e historial actualizado.

#### RF-31: Gestión de estado vacío (Zero-results feedback)
- **Código:** RF-31
- **Trazabilidad:** US-31
- **Prioridad:** SHOULD
- **Descripción:** Cuando una combinación de búsqueda o filtros no arroje resultados, el sistema debe presentar un mensaje amigable indicando la ausencia de coincidencias y ofreciendo sugerencias contextuales (relajar filtros, verificar ortografía o explorar productos populares).
- **Entradas:** Búsqueda con cero coincidencias.
- **Salidas:** Vista informativa de estado vacío con recomendaciones de acción.

#### RF-32: Paginación y carga diferida (Infinite Scroll / Pagination)
- **Código:** RF-32
- **Trazabilidad:** US-32
- **Prioridad:** MUST
- **Descripción:** El sistema debe cargar los productos por lotes utilizando paginación o carga diferida por desplazamiento continuo (*infinite scroll*), evitando el bloqueo de la interfaz y optimizando el consumo de red y memoria.
- **Entradas:** Evento de cambio de página o desplazamiento hacia el final de la lista.
- **Salidas:** Lote subsiguiente de productos renderizado eficientemente.

---

### Módulo 4: Detalle de Producto, Recomendaciones y Redirección

#### RF-33: Consulta de ficha técnica de producto
- **Código:** RF-33
- **Trazabilidad:** US-33
- **Prioridad:** MUST
- **Descripción:** El sistema debe presentar una vista detallada del producto con nombre, fotografías de alta calidad, precio en COP, marca, material, color, tabla de tallas y comercio de origen.
- **Entradas:** Identificador único del producto.
- **Salidas:** Ficha técnica completa del producto renderizada.

#### RF-34: Galería interactiva de fotografías
- **Código:** RF-34
- **Trazabilidad:** US-34
- **Prioridad:** MUST
- **Descripción:** La página de detalle de producto debe exhibir un visor o carrusel de fotografías del producto provistas por la tienda externa, permitiendo navegar entre las distintas tomas disponibles.
- **Entradas:** Interacción con el carrusel/miniaturas.
- **Salidas:** Imagen activa ampliada en el visor.

#### RF-35: Consulta de disponibilidad de tallas
- **Código:** RF-35
- **Trazabilidad:** US-35
- **Prioridad:** MUST
- **Descripción:** El sistema debe diferenciar visualmente en la ficha de producto aquellas tallas que cuentan con existencias activas frente a las agotadas (mediante sombreado o deshabilitación).
- **Entradas:** Estado de inventario del producto.
- **Salidas:** Matriz visual de tallas con indicación de disponibilidad.

#### RF-36: Agrupación y visualización de productos similares
- **Código:** RF-36
- **Trazabilidad:** US-36
- **Prioridad:** WOULD
- **Descripción:** El sistema debe identificar y agrupar productos con atributos visuales y funcionales similares (mismo tipo, color y corte) para facilitar su contraste en una sección dedicada.
- **Entradas:** Atributos del producto en visualización.
- **Salidas:** Carrusel o lista de productos catalogados como similares.

#### RF-37: Sección de recomendaciones contextuales ("También te podría gustar")
- **Código:** RF-37
- **Trazabilidad:** US-37
- **Prioridad:** WOULD
- **Descripción:** El sistema debe computar y desplegar una sección de productos complementarios o sugeridos con base en la prenda actual y el perfil de preferencias del usuario.
- **Entradas:** Prenda visualizada y preferencias del usuario.
- **Salidas:** Bloque de productos sugeridos.

#### RF-38: Redirección externa con enlace de compra directa
- **Código:** RF-38
- **Trazabilidad:** US-38
- **Prioridad:** MUST
- **Descripción:** El sistema debe proveer un botón de enlace directo al sitio web de la tienda propietaria del producto, abriéndose en una nueva pestaña del navegador para que el usuario concrete la transacción.
- **Entradas:** Clic en "Ir a la tienda" o "Comprar en [Tienda]".
- **Salidas:** Apertura de la URL original del producto en pestaña externa (`target="_blank"`).

#### RF-39: Visualización de fecha de última sincronización
- **Código:** RF-39
- **Trazabilidad:** US-39
- **Prioridad:** COULD
- **Descripción:** El sistema debe indicar explícitamente en la ficha del producto la fecha y hora del último escaneo o actualización de precio y stock registrado por el sistema.
- **Entradas:** Timestamp de sincronización del producto.
- **Salidas:** Etiqueta visible *"Actualizado el: DD/MM/AAAA HH:MM"*.

#### RF-40: Reporte de inconsistencias de producto
- **Código:** RF-40
- **Trazabilidad:** US-40
- **Prioridad:** WOULD
- **Descripción:** El sistema debe disponer de un formulario que permita al usuario reportar incidencias sobre un producto (enlace roto, precio discordante, imagen errónea o producto descontinuado).
- **Entradas:** Motivo del reporte y comentario opcional del usuario.
- **Salidas:** Incidencia registrada en la base de datos de administración con estado pendiente.

---

### Módulo 5: Comparador de Precios y Productos

#### RF-41: Distintivo visual del menor precio
- **Código:** RF-41
- **Trazabilidad:** US-41
- **Prioridad:** COULD
- **Descripción:** Cuando un mismo producto o modelo equivalente se encuentre disponible en diferentes tiendas, el sistema debe resaltar visualmente mediante una insignia (*badge*) o color distintivo la oferta con el precio más bajo.
- **Entradas:** Comparación de precios de productos homólogos.
- **Salidas:** Insignia destacada *"Mejor Precio"* en la opción más económica.

#### RF-42: Cuadro comparativo lado a lado (Side-by-side)
- **Código:** RF-42
- **Trazabilidad:** US-42
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir seleccionar dos o más prendas y contrastarlas en una tabla comparativa matricial que evalúe atributos como precio, tienda, marca, material, color, tallas disponibles y valoración.
- **Entradas:** Selección de productos a comparar (2 a 4 prendas).
- **Salidas:** Vista tabular comparativa organizada por filas de atributos.

#### RF-43: Estandarización de formato monetario en Pesos Colombianos (COP)
- **Código:** RF-43
- **Trazabilidad:** US-43
- **Prioridad:** MUST
- **Descripción:** El sistema debe mostrar la totalidad de los precios y totales calculados en Pesos Colombianos (COP) utilizando el formato numérico estándar (ej. `$ 150.000 COP`), sin ambigüedad de divisas.
- **Entradas:** Montos brutos de las tiendas.
- **Salidas:** Cadenas monetarias formateadas homogéneamente en toda la aplicación.

---

### Módulo 6: Constructor de Outfits (Outfit Builder)

#### RF-44: Inicialización de nuevo outfit
- **Código:** RF-44
- **Trazabilidad:** US-44
- **Prioridad:** MUST
- **Descripción:** El sistema debe proveer una vista de trabajo interactiva (*canvas* / ensamblador) en blanco donde el usuario pueda estructurar un nuevo conjunto desde cero.
- **Entradas:** Acción "Crear nuevo outfit".
- **Salidas:** Espacio de trabajo vacío inicializado con ranuras (*slots*) preparadas.

#### RF-45: Asignación de prenda superior (Top slot)
- **Código:** RF-45
- **Trazabilidad:** US-45
- **Prioridad:** MUST
- **Descripción:** El ensamblador debe disponer de una ranura destinada a prendas superiores (camisetas, camisas, buzos, chaquetas), permitiendo ubicar una prenda de dicha categoría.
- **Entradas:** Selección de prenda de categoría superior.
- **Salidas:** Prenda posicionada en el slot superior del outfit activo.

#### RF-46: Asignación de prenda inferior (Bottom slot)
- **Código:** RF-46
- **Trazabilidad:** US-46
- **Prioridad:** MUST
- **Descripción:** El ensamblador debe disponer de una ranura destinada a prendas inferiores (jeans, pantalones, pantalonetas, faldas), permitiendo vincular una prenda de dicha categoría.
- **Entradas:** Selección de prenda de categoría inferior.
- **Salidas:** Prenda posicionada en el slot inferior del outfit activo.

#### RF-47: Asignación de calzado (Shoes slot)
- **Código:** RF-47
- **Trazabilidad:** US-47
- **Prioridad:** MUST
- **Descripción:** El ensamblador debe disponer de una ranura destinada a calzado (tenis, botas, zapatos formales, sandalias), permitiendo vincular un par de calzado.
- **Entradas:** Selección de prenda de categoría calzado.
- **Salidas:** Calzado posicionado en el slot correspondiente.

#### RF-48: Asignación de accesorios opcionales (Accessories slots)
- **Código:** RF-48
- **Trazabilidad:** US-48
- **Prioridad:** COULD
- **Descripción:** El sistema debe permitir añadir uno o más accesorios opcionales (gorras, gafas, bolsos, relojes) sin que su ausencia invalide o impida guardar el outfit.
- **Entradas:** Selección de uno o más accesorios.
- **Salidas:** Accesorios incorporados en ranuras complementarias.

#### RF-49: Sustitución contextual de piezas
- **Código:** RF-49
- **Trazabilidad:** US-49
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir pulsar la opción "Cambiar" sobre cualquier ranura ocupada del outfit para desplegar un selector con prendas alternativas de la misma categoría y sustituirla con un solo clic.
- **Entradas:** Selección de pieza alternativa.
- **Salidas:** Ranura actualizada con la nueva prenda sin perder el resto del conjunto.

#### RF-50: Actualización reactiva en tiempo real del lienzo
- **Código:** RF-50
- **Trazabilidad:** US-50
- **Prioridad:** MUST
- **Descripción:** El sistema debe reflejar cualquier cambio, sustitución o adición de prendas de manera inmediata y reactiva en la interfaz visual, sin recargar la página web.
- **Entradas:** Eventos de cambio en el estado del outfit.
- **Salidas:** Re-renderizado instantáneo de la composición visual.

#### RF-51: Remoción de prendas individuales
- **Código:** RF-51
- **Trazabilidad:** US-51
- **Prioridad:** SHOULD
- **Descripción:** El usuario debe poder remover cualquier prenda individual del outfit pulsando un botón de eliminación, dejando la ranura respectiva en estado vacío.
- **Entradas:** Clic en botón "Quitar" de la ranura.
- **Salidas:** Ranura liberada y totales recalculados.

#### RF-52: Adición de productos al outfit desde el catálogo
- **Código:** RF-52
- **Trazabilidad:** US-52
- **Prioridad:** MUST
- **Descripción:** Cada tarjeta de producto en el catálogo y en la ficha de detalle debe contar con un botón "Agregar al outfit", permitiendo insertar directamente la prenda en la ranura correspondiente según su categoría.
- **Entradas:** Clic en "Agregar al outfit".
- **Salidas:** Prenda agregada al canvas y notificación de confirmación al usuario.

#### RF-53: Cálculo dinámico del precio total del outfit
- **Código:** RF-53
- **Trazabilidad:** US-53
- **Prioridad:** MUST
- **Descripción:** El sistema debe recalcular y mostrar automáticamente la sumatoria de los precios de todas las prendas que componen el outfit activo cada vez que se agregue, modifique o elimine un elemento.
- **Entradas:** Lista de prendas activas con sus precios individuales.
- **Salidas:** Monto total consolidado en COP visible en el constructor.

#### RF-54: Alerta visual de exceso de presupuesto
- **Código:** RF-54
- **Trazabilidad:** US-54
- **Prioridad:** MUST
- **Descripción:** Cuando el costo total acumulado del outfit supere el presupuesto máximo configurado por el usuario, el sistema debe emitir un indicador de advertencia visual no bloqueante (color ámbar/rojo con diferencia del monto excedido).
- **Entradas:** Costo total del outfit > Presupuesto máximo del usuario.
- **Salidas:** Mensaje de alerta visual destacando el sobrecosto.

#### RF-55: Desglose de tiendas y precios por componente
- **Código:** RF-55
- **Trazabilidad:** US-55
- **Prioridad:** MUST
- **Descripción:** El constructor debe proveer un panel de desglose donde se listen cada una de las prendas que conforman el outfit, indicando su nombre, tienda externa proveedora y precio individual.
- **Entradas:** Estado actual del outfit armado.
- **Salidas:** Listado detallado de ítems, precios y tiendas.

#### RF-56: Control de historial de cambios (Deshacer / Rehacer)
- **Código:** RF-56
- **Trazabilidad:** US-56
- **Prioridad:** WOULD
- **Descripción:** El constructor de outfits debe almacenar una pila de estados que permita al usuario deshacer (*Undo*) o rehacer (*Redo*) las últimas modificaciones realizadas sobre el lienzo.
- **Entradas:** Clic en botones Deshacer/Rehacer o atajos de teclado asociados.
- **Salidas:** Reversión o restauración del estado inmediatamente anterior del outfit.

#### RF-57: Bloqueo de prendas en el lienzo (Lock slot)
- **Código:** RF-57
- **Trazabilidad:** US-57
- **Prioridad:** WOULD
- **Descripción:** El usuario debe poder bloquear una o varias piezas mediante un icono de candado para que permanezcan inalteradas mientras explora cambios automáticos o aleatorios en las ranuras restantes.
- **Entradas:** Activación/desactivación del estado de bloqueo en una ranura.
- **Salidas:** Ranura protegida contra reemplazos accidentales o globales.

#### RF-58: Asistente consultivo de compatibilidad y estilo
- **Código:** RF-58
- **Trazabilidad:** US-58
- **Prioridad:** WOULD
- **Descripción:** El sistema debe evaluar reglas heurísticas básicas de armonía cromática y compatibilidad de corte entre las prendas del conjunto, emitiendo sugerencias o advertencias de estilo informativas que no impidan al usuario guardar o conservar su elección.
- **Entradas:** Conjunto de atributos de color y corte de las piezas del outfit.
- **Salidas:** Consejos breves de estilo visibles en pantalla sin efecto restrictivo.

---

### Módulo 7: Visualización y Composición del Outfit

#### RF-59: Composición visual unificada
- **Código:** RF-59
- **Trazabilidad:** US-59
- **Prioridad:** MUST
- **Descripción:** El sistema debe generar un renderizado gráfico integrado que ubique armónicamente las imágenes de las prendas (top superior, pantalón en el medio, calzado en la base y accesorios en laterales) en una única composición visual.
- **Entradas:** Imágenes transparentes/recortadas de las prendas del outfit.
- **Salidas:** Canvas visual compuesto coherente.

#### RF-60: Proyección en silueta o maniquí virtual
- **Código:** RF-60
- **Trazabilidad:** US-60
- **Prioridad:** WOULD
- **Descripción:** El sistema debe permitir superponer las prendas del outfit sobre una silueta de maniquí bidimensional o tridimensional para ofrecer una apreciación cercana a la figura corporal.
- **Entradas:** Selección del modo de visualización de maniquí.
- **Salidas:** Renderizado de prendas alineadas sobre la silueta virtual.

#### RF-61: Control de zoom e inspección de detalles
- **Código:** RF-61
- **Trazabilidad:** US-61
- **Prioridad:** WOULD
- **Descripción:** La vista de visualización del outfit debe contar con controles de acercamiento (*zoom in*), alejamiento (*zoom out*) y encuadre para inspeccionar texturas y acabados de las prendas.
- **Entradas:** Interacción con controles de zoom o rueda del ratón.
- **Salidas:** Escala visual ajustada del lienzo.

#### RF-62: Alternancia entre modos de visualización
- **Código:** RF-62
- **Trazabilidad:** US-62
- **Prioridad:** WOULD
- **Descripción:** El sistema debe permitir alternar dinámicamente entre el modo de composición plana (*flat-lay*), vista en maniquí y vista avatar, conservando en todo momento las prendas seleccionadas sin perder el progreso.
- **Entradas:** Selección del modo de visualización.
- **Salidas:** Transición visual de la interfaz manteniendo el estado del modelo de datos.

---

### Módulo 8: Almacenamiento, Listas de Deseos y Compra

#### RF-63: Gestión de productos favoritos (Wishlist)
- **Código:** RF-63
- **Trazabilidad:** US-63
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir a los usuarios autenticados marcar o desmarcar prendas individuales como favoritas mediante un icono de corazón, almacenándolas en una lista de deseos accesible desde su perfil.
- **Entradas:** Clic en icono de favorito sobre un producto.
- **Salidas:** Producto añadido o eliminado de la lista de favoritos del usuario.

#### RF-64: Guardado persistente de outfits con nombre
- **Código:** RF-64
- **Trazabilidad:** US-64
- **Prioridad:** MUST
- **Descripción:** El sistema debe permitir guardar un outfit completo asignándole un nombre identificador (ej. *"Look Oficina Verano"*), almacenando la configuración en la base de datos asociada a la cuenta del usuario.
- **Entradas:** Nombre asignado y conjunto de IDs de prendas del outfit.
- **Salidas:** Outfit persistido en la sección "Mis Outfits".

#### RF-65: Edición y eliminación de outfits guardados
- **Código:** RF-65
- **Trazabilidad:** US-65
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir al usuario renombrar, modificar las prendas o eliminar definitivamente cualquiera de sus outfits guardados previamente.
- **Entradas:** Acción de edición o eliminación sobre un outfit existente.
- **Salidas:** Registro de outfit modificado o suprimido en base de datos.

#### RF-66: Organización de outfits en colecciones
- **Código:** RF-66
- **Trazabilidad:** US-66
- **Prioridad:** WOULD
- **Descripción:** El sistema debe permitir agrupar outfits guardados dentro de colecciones o carpetas temáticas personalizadas (ej. *"Universidad"*, *"Eventos Formales"*, *"Gimnasio"*).
- **Entradas:** Nombre de la colección y asignación de outfits.
- **Salidas:** Estructura jerárquica de colecciones reflejada en el perfil.

#### RF-67: Duplicación de outfits existentes
- **Código:** RF-67
- **Trazabilidad:** US-67
- **Prioridad:** WOULD
- **Descripción:** El sistema debe permitir clonar un outfit guardado para generar una copia editable independiente sin alterar la versión original.
- **Entradas:** Acción "Duplicar" sobre un outfit guardado.
- **Salidas:** Nuevo registro de outfit clonado con sufijo *(Copia)*.

#### RF-68: Redirección individual de compra por prenda del outfit
- **Código:** RF-68
- **Trazabilidad:** US-68
- **Prioridad:** MUST
- **Descripción:** En la vista del outfit guardado o en el desglose final, cada prenda debe contar con un botón "Comprar" que redirija directamente a la URL de compra en la tienda correspondiente.
- **Entradas:** Clic en "Comprar" de una prenda específica.
- **Salidas:** Redirección a la tienda externa específica del producto seleccionado.

#### RF-69: Exportación de lista de compras consolidada
- **Código:** RF-69
- **Trazabilidad:** US-69
- **Prioridad:** SHOULD
- **Descripción:** El sistema debe permitir exportar la lista de compras del outfit (nombre de prendas, tiendas, precios individuales, precio total y enlaces de compra) en formato descargable PDF o copiarla como texto plano al portapapeles.
- **Entradas:** Clic en "Exportar lista de compras" y selección de formato (PDF / Portapapeles).
- **Salidas:** Archivo PDF generado o texto formateado copiado.

---

### Módulo 9: Administración, Recolección y Gobierno de Datos

#### RF-70: Gestión administrativa de tiendas (CRUD Tiendas)
- **Código:** RF-70
- **Trazabilidad:** US-70
- **Prioridad:** MUST
- **Descripción:** El panel de administración debe permitir crear, consultar, actualizar, activar o pausar las tiendas externas asociadas a los procesos de recolección de catálogo.
- **Entradas:** Datos de la tienda (nombre, URL base, logo, selector/adaptador de scraping, estado).
- **Salidas:** Tienda registrada o modificada en el catálogo administrativo.

#### RF-71: Motor automatizado de extracción de productos (Scraping)
- **Código:** RF-71
- **Trazabilidad:** US-71
- **Prioridad:** MUST
- **Descripción:** El sistema debe ejecutar procesos de extracción automática de datos desde las tiendas activas, recopilando títulos, descripciones, precios en COP, imágenes, tallas, colores y enlaces de compra para alimentar la base de datos central.
- **Entradas:** URLs y esquemas de extracción de las tiendas activas.
- **Salidas:** Lote de productos parseados y almacenados en la base de datos.

#### RF-72: Programación periódica de recolección de datos
- **Código:** RF-72
- **Trazabilidad:** US-72
- **Prioridad:** COULD
- **Descripción:** El sistema debe contar con un planificador de tareas (*cron scheduler*) configurable por el administrador para disparar la extracción periódica (ej. cada 24 horas) en horarios de bajo tráfico.
- **Entradas:** Expresión cron o frecuencia temporal configurada.
- **Salidas:** Ejecución automática del pipeline de extracción según cronograma.

#### RF-73: Consola y registro de auditoría de sincronizaciones (Logs)
- **Código:** RF-73
- **Trazabilidad:** US-73
- **Prioridad:** WOULD
- **Descripción:** El sistema debe registrar un historial detallado de cada ejecución de scraping, reportando marca temporal, tienda procesada, estado (éxito/fallo), número de productos insertados/actualizados y detalle de excepciones.
- **Entradas:** Eventos generados durante el ciclo de recolección.
- **Salidas:** Panel de auditoría de logs con filtros por fecha, tienda y severidad de error.

#### RF-74: Estandarización y normalización ontológica de datos
- **Código:** RF-74
- **Trazabilidad:** US-74
- **Prioridad:** MUST
- **Descripción:** El sistema debe procesar los datos extraídos de diversas tiendas mediante reglas de normalización que unifiquen nombres de colores dispares a una paleta canónica, homologuen tallas heterogéneas (ej. S / Small / 36) y asignen categorías estándar.
- **Entradas:** Registros crudos provenientes de las tiendas externas.
- **Salidas:** Registros estandarizados y saneados aptos para filtros universales.

#### RF-75: Gestión y resolución de reportes de usuarios
- **Código:** RF-75
- **Trazabilidad:** US-75
- **Prioridad:** WOULD
- **Descripción:** El panel de administración debe presentar la bandeja de incidencias reportadas por los usuarios (RF-40), permitiendo a los administradores cambiar su estado (*Abierto*, *En revisión*, *Resuelto*, *Descartado*) e ingresar notas de seguimiento.
- **Entradas:** Interacción del administrador con la bandeja de incidencias.
- **Salidas:** Estado de reporte actualizado en base de datos.

#### RF-76: Moderación y edición manual de productos
- **Código:** RF-76
- **Trazabilidad:** US-76
- **Prioridad:** SHOULD
- **Descripción:** El administrador debe tener la potestad de editar manualmente campos erróneos de cualquier producto del catálogo o despublicarlo/ocultarlo inmediatamente de las búsquedas públicas.
- **Entradas:** Datos modificados o acción de ocultar (*hide/unpublish*).
- **Salidas:** Producto actualizado o excluido de los resultados públicos.

#### RF-77: Tablero de métricas operativas y estadísticas
- **Código:** RF-77
- **Trazabilidad:** US-77
- **Prioridad:** WOULD
- **Descripción:** El sistema debe suministrar un panel de analíticas básicas para el administrador que grafique el total de usuarios registrados, búsquedas más frecuentes, marcas populares y prendas más visualizadas o añadidas a outfits.
- **Entradas:** Datos de actividad y telemetría de la aplicación.
- **Salidas:** Dashboard interactivo con gráficos e indicadores clave de rendimiento (KPIs).

---

## 3. Requerimientos No Funcionales (RNF) según ISO/IEC 25010

Los requerimientos no funcionales definen los atributos de calidad, restricciones técnicas y estándares de cumplimiento del sistema, clasificados bajo el modelo de calidad de software **ISO/IEC 25010**.

---

### 3.1 Rendimiento y Eficiencia (Performance Efficiency)

#### RNF-01: Tiempo de respuesta en búsquedas y filtrados
- **Categoría:** Rendimiento (Comportamiento temporal)
- **Descripción:** Las consultas de búsqueda de texto libre y la aplicación de filtros combinados deben retornar los resultados en un tiempo máximo de **1.5 segundos** en el percentil 95 (P95) bajo condiciones normales de carga sobre un catálogo de al menos 50.000 prendas.
- **Métrica:** Latencia del endpoint `GET /api/v1/products/search` ≤ 1.5 s en P95.

#### RNF-02: Latencia de interacción en el Outfit Builder
- **Categoría:** Rendimiento (Capacidad de respuesta en cliente)
- **Descripción:** La adición, reemplazo o remoción de una prenda en el lienzo del *Outfit Builder*, así como el recálculo del precio total acumulado, debe reflejarse en la interfaz en un tiempo inferior a **200 milisegundos**.
- **Métrica:** Tiempo de re-renderizado en el DOM de la aplicación cliente ≤ 200 ms.

#### RNF-03: Optimización y entrega de recursos multimedia
- **Categoría:** Rendimiento (Utilización de recursos)
- **Descripción:** Las imágenes de catálogo deben ser comprimidas y servidas en formatos modernos optimizados para la web (WebP o AVIF), con un peso objetivo inferior a **150 KB** por fotografía estándar, utilizando técnicas de carga perezosa (*lazy loading*) y red de distribución de contenidos (CDN).
- **Métrica:** Tamaño promedio de imagen ≤ 150 KB; puntuación Google Lighthouse Performance ≥ 85/100 en versión móvil y escritorio.

#### RNF-04: Capacidad de concurrencia y escalabilidad
- **Categoría:** Rendimiento (Capacidad)
- **Descripción:** El backend del sistema debe soportar un mínimo de **500 usuarios concurrentes activos** navegando y realizando consultas simultáneas sin que la tasa de error supere el 0.1% ni los tiempos de respuesta se degraden en más de un 20%.
- **Métrica:** 500 conexiones simultáneas sostenidas con error rate < 0.1%.

---

### 3.2 Seguridad (Security)

#### RNF-05: Cifrado de comunicaciones en tránsito
- **Categoría:** Seguridad (Confidencialidad)
- **Descripción:** Todo el tráfico entre clientes web/móviles y los servidores del sistema, así como las comunicaciones entre microservicios o procesos de backend, debe realizarse obligatoriamente sobre el protocolo **HTTPS** con cifrado **TLS 1.3** (o TLS 1.2 como versión mínima permitida).
- **Métrica:** Certificado SSL/TLS válido de 2048 bits; redirección forzada de HTTP a HTTPS con cabecera HSTS activa.

#### RNF-06: Almacenamiento seguro de credenciales
- **Categoría:** Seguridad (Integridad y Confidencialidad)
- **Descripción:** Las contraseñas de los usuarios nunca deben almacenarse en texto plano. Deben ser procesadas mediante funciones hash criptográficas robustas con sal (*salt*) aleatorio por usuario, empleando **Argon2id** o **bcrypt** con un factor de trabajo (*work factor*) mínimo de 12.
- **Métrica:** Algoritmo bcrypt (cost ≥ 12) o Argon2id verificado en auditorías de persistencia.

#### RNF-07: Control de acceso y gestión de sesiones
- **Categoría:** Seguridad (Autenticación y Autorización)
- **Descripción:** La autenticación en la API debe implementarse mediante tokens **JWT** (*JSON Web Tokens*) firmados con algoritmos asimétricos (RS256) o HMAC-SHA256 con tiempo de expiración corto (máximo 15 minutos), acompañados de *Refresh Tokens* revocables almacenados en cookies seguras con banderas `HttpOnly`, `Secure` y `SameSite=Strict`. Debe implementarse control de acceso basado en roles (**RBAC**) para separar estrictamente las funciones de usuario y administrador.
- **Métrica:** Ausencia de tokens expuestos en `localStorage`; expiración estricta de access tokens ≤ 15 min.

#### RNF-08: Mitigación de vulnerabilidades OWASP Top 10
- **Categoría:** Seguridad (Resistencia a ataques)
- **Descripción:** El sistema debe implementar salvaguardas explícitas contra ataques comunes: consultas parametrizadas contra Inyección SQL (SQLi), sanitización estricta de entradas y Content Security Policy (CSP) contra Cross-Site Scripting (XSS), validación de tokens contra Cross-Site Request Forgery (CSRF), y limitador de tasa (*Rate Limiting*) de 60 peticiones/minuto por dirección IP en endpoints públicos y máximo 5 intentos fallidos consecutivos de inicio de sesión antes de bloqueo temporal de 15 minutos.
- **Métrica:** Escaneos automatizados de seguridad (SAST/DAST) con cero vulnerabilidades críticas o altas no remediadas.

---

### 3.3 Usabilidad y Accesibilidad (Usability)

#### RNF-09: Diseño adaptable y multidispositivo (Responsive Web Design)
- **Categoría:** Usabilidad (Operabilidad)
- **Descripción:** La interfaz gráfica de usuario debe adaptarse fluidamente a diferentes factores de forma y resoluciones de pantalla, ofreciendo soporte verificado desde dispositivos móviles compactos (viewport de 360 px de ancho) hasta monitores de escritorio de alta resolución (Full HD / 4K).
- **Métrica:** 100% de los flujos críticos (búsqueda, outfit builder, perfil) operables sin desbordamiento horizontal en resoluciones entre 360px y 3840px.

#### RNF-10: Cumplimiento de accesibilidad web (WCAG 2.1 AA)
- **Categoría:** Usabilidad (Accesibilidad)
- **Descripción:** La plataforma debe cumplir con las pautas de accesibilidad para el contenido web **WCAG 2.1 Nivel AA**, garantizando un contraste cromático mínimo de 4.5:1 para texto normal, navegación completa mediante teclado y atributos semánticos `ARIA` para lectores de pantalla.
- **Métrica:** Puntuación de Accesibilidad en Google Lighthouse ≥ 90/100; validación con herramientas Axe Core sin infracciones de nivel crítico.

#### RNF-11: Claridad de retroalimentación y manejo de errores
- **Categoría:** Usabilidad (Protección contra errores de usuario)
- **Descripción:** Todo error o excepción en la aplicación debe traducirse en un mensaje descriptivo en lenguaje natural y comprensible en español, evitando la exposición de trazas de código (*stack traces*) o tecnicismos al usuario final, e indicando la acción sugerida para subsanarlo.
- **Métrica:** 100% de los mensajes de error validados según guía de estilo de usuario; cero fugas de información interna en respuestas HTTP.

---

### 3.4 Fiabilidad y Disponibilidad (Reliability)

#### RNF-12: Disponibilidad del servicio (Uptime)
- **Categoría:** Fiabilidad (Disponibilidad)
- **Descripción:** La plataforma web y sus servicios de API para usuarios finales deben mantener una disponibilidad mínima mensual del **99.5%** (permitiendo un tiempo máximo de indisponibilidad no planificada inferior a 3.6 horas por mes), excluyendo ventanas de mantenimiento previamente notificadas.
- **Métrica:** SLA de disponibilidad mensual ≥ 99.5% medido mediante monitores sintéticos externos (ej. UptimeRobot, Pingdom).

#### RNF-13: Aislamiento y resiliencia ante fallos externos
- **Categoría:** Fiabilidad (Tolerancia a fallos)
- **Descripción:** La caída, lentitud o bloqueo de las operaciones de scraping sobre una tienda externa específica no debe interrumpir el funcionamiento del resto de la plataforma ni degradar las búsquedas sobre los datos previamente recolectados. Los workers de extracción deben implementar reintentos con retroceso exponencial (*exponential backoff*) y disyuntores (*circuit breakers*).
- **Métrica:** Aislamiento de procesos de scraping en colas asíncronas independientes; disponibilidad del catálogo estático persistido = 100% ante fallas del extractor.

#### RNF-14: Política de respaldo y recuperación de desastres (Backup & Recovery)
- **Categoría:** Fiabilidad (Capacidad de recuperación)
- **Descripción:** El sistema debe ejecutar copias de seguridad automáticas diarias de la base de datos relacional y configuraciones críticas. El objetivo de punto de recuperación (**RPO**) no debe exceder las **24 horas** y el objetivo de tiempo de recuperación (**RTO**) debe ser inferior a **2 horas**.
- **Métrica:** RPO ≤ 24 horas; RTO ≤ 2 horas en pruebas semestrales de restauración.

---

### 3.5 Mantenibilidad y Calidad de Código (Maintainability)

#### RNF-15: Arquitectura modular y desacoplada
- **Categoría:** Mantenibilidad (Modularidad)
- **Descripción:** El sistema debe construirse siguiendo un patrón arquitectónico modular desacoplado (Frontend SPA, Backend API RESTful, Módulo de Scraping independiente y Base de Datos), garantizando que las modificaciones en los adaptadores de scraping no alteren la capa de presentación ni la lógica de negocio de usuarios.
- **Métrica:** Bajo acoplamiento y alta cohesión comprobable en la estructura de paquetes; componentes de scraping aislados mediante interfaces polimórficas por tienda.

#### RNF-16: Documentación técnica estandarizada de APIs
- **Categoría:** Mantenibilidad (Modificabilidad)
- **Descripción:** La totalidad de los endpoints del backend deben encontrarse documentados formalmente bajo la especificación **OpenAPI 3.0** (Swagger), suministrando una interfaz interactiva donde se detallen rutas, métodos HTTP, esquemas de entrada, códigos de estado y respuestas de ejemplo.
- **Métrica:** Cobertura del 100% de rutas en `swagger.json` o interfaz Swagger UI actualizada automáticamente en cada despliegue.

#### RNF-17: Cobertura de pruebas automatizadas
- **Categoría:** Mantenibilidad (Capacidad de ser probado / Testability)
- **Descripción:** El código fuente debe contar con suites de pruebas unitarias y de integración automáticas en el pipeline de Integración Continua (CI), alcanzando una cobertura de código mínima del **70%** sobre los módulos de lógica de negocio, autenticación, normalización y cálculo de precios.
- **Métrica:** Cobertura de pruebas calculada por herramientas de reporte (ej. Jest, PyTest, JaCoCo) ≥ 70%.

---

### 3.6 Compatibilidad e Interoperabilidad (Compatibility)

#### RNF-18: Compatibilidad multiplataforma de navegadores
- **Categoría:** Compatibilidad (Coexistencia e Interoperabilidad)
- **Descripción:** La plataforma web debe funcionar correctamente y de manera consistente en las últimas dos versiones mayores de los navegadores web predominantes: Google Chrome, Mozilla Firefox, Apple Safari y Microsoft Edge, tanto en sistemas operativos de escritorio (Windows, macOS, Linux) como móviles (Android, iOS).
- **Métrica:** Ejecución sin fallos críticos en la matriz de compatibilidad de navegadores mediante pruebas automatizadas cross-browser.

#### RNF-19: Formato estandarizado de intercambio de datos
- **Categoría:** Compatibilidad (Interoperabilidad)
- **Descripción:** La comunicación entre cliente y servidor debe emplear exclusivamente el formato estándar **JSON** (*JavaScript Object Notation*) con codificación de caracteres **UTF-8**, cumpliendo con convenciones RESTful estándar para verbos HTTP y códigos de estado.
- **Métrica:** 100% de payloads de petición y respuesta en formato `application/json; charset=utf-8`.

---

### 3.7 Portabilidad (Portability)

#### RNF-20: Contenerización y despliegue agnóstico
- **Categoría:** Portabilidad (Adaptabilidad e Instalabilidad)
- **Descripción:** Todos los componentes de la solución (servicios web, workers de extracción, bases de datos y balanceadores) deben estar empaquetados en contenedores estándar **Docker**, gestionados mediante archivos `docker-compose.yml` o manifiestos para orquestadores, permitiendo el despliegue homogéneo en entornos locales de desarrollo, pruebas y producción en la nube.
- **Métrica:** Capacidad de levantar la suite completa del entorno mediante un comando único (`docker compose up`) en menos de 5 minutos en un entorno configurado.

---

### 3.8 Cumplimiento Legal y Privacidad (Compliance & Privacy)

#### RNF-21: Protección de datos personales (Habeas Data / Ley 1581 de 2012)
- **Categoría:** Cumplimiento (Privacidad)
- **Descripción:** Dado que el sistema maneja precios en Pesos Colombianos (COP) y atiende usuarios locales e internacionales, debe dar estricto cumplimiento al Régimen General de Protección de Datos Personales en Colombia (**Ley 1581 de 2012**) y principios equivalentes de GDPR, requiriendo autorización expresa previa para el tratamiento de datos personales, disponiendo de una Política de Tratamiento de Información visible y permitiendo la actualización, rectificación y supresión de datos a solicitud del titular (RF-05, RF-06).
- **Métrica:** Registro auditable de consentimientos de términos y política de privacidad al momento del registro; mecanismos funcionales de baja de cuenta.

#### RNF-22: Extracción ética de datos y directivas de robots
- **Categoría:** Cumplimiento (Regulación comercial y ética)
- **Descripción:** Los procesos automáticos de recolección de catálogo deben respetar las políticas de concurrencia y no saturación de los servidores objetivo (incorporando retardos deliberados entre peticiones), identificarse mediante una cabecera `User-Agent` descriptiva institucional, no recolectar datos protegidos por autenticación privada sin autorización y desplegar en la plataforma advertencias claras de que las marcas e imágenes pertenecen a sus respectivos comercios afiliados o terceros.
- **Métrica:** Configuración de rate-limit en workers de scraping con retardo mínimo de 500 ms entre peticiones a un mismo dominio; presencia de disclaimer legal en el pie de página de la aplicación.

---

## 4. Matriz de Trazabilidad: Historias de Usuario vs. Requerimientos Funcionales

| Épica | Historia de Usuario (US) | Prioridad US | Requerimiento Funcional (RF) | Prioridad RF |
| :--- | :--- | :---: | :--- | :---: |
| **Epic 1. Account and Profile** | US-1: Create an account | MUST | RF-01: Registro de cuenta local | MUST |
| | US-2: Log in and log out | MUST | RF-02: Autenticación y gestión de sesiones | MUST |
| | US-3: Sign in with Google | COULD | RF-03: Autenticación federada con Google | COULD |
| | US-4: Recover password by email | SHOULD | RF-04: Recuperación de contraseña por correo | SHOULD |
| | US-5: Edit my profile | SHOULD | RF-05: Modificación de datos del perfil | SHOULD |
| | US-6: Delete my account and data | SHOULD | RF-06: Eliminación definitiva de cuenta y datos | SHOULD |
| | US-7: Search without an account | SHOULD | RF-07: Navegación y búsqueda sin cuenta (Visitante) | SHOULD |
| **Epic 2. User Preferences** | US-8: Setup guide for new users | SHOULD | RF-08: Asistente guiado de configuración inicial | SHOULD |
| | US-9: Select liked brands | SHOULD | RF-09: Selección y priorización de marcas favoritas | SHOULD |
| | US-10: Choose favorite colors | SHOULD | RF-10: Selección de colores favoritos | SHOULD |
| | US-11: Set price range | MUST | RF-11: Definición de rango de precios preferente | MUST |
| | US-12: Save my sizes | SHOULD | RF-12: Registro de tallas por categoría de prenda | SHOULD |
| | US-13: Choose fit preference | SHOULD | RF-13: Preferencia de corte y silueta (Fit) | SHOULD |
| | US-14: Set maximum budget | MUST | RF-14: Configuración de presupuesto máximo | MUST |
| | US-15: Edit preferences anytime | MUST | RF-15: Actualización dinámica de preferencias | MUST |
| | US-16: Reset preferences | COULD | RF-16: Restablecimiento de preferencias por defecto | COULD |
| | US-17: View preferences summary | MUST | RF-17: Visualización resumida de preferencias | MUST |
| **Epic 3. Search and Filtering** | US-18: Search clothing by text | MUST | RF-18: Búsqueda textual libre de prendas | MUST |
| | US-19: See results from many stores | MUST | RF-19: Agregación y visualización multitienda | MUST |
| | US-20: Filter by price | MUST | RF-20: Filtrado por rango de precios | MUST |
| | US-21: Filter by brand | MUST | RF-21: Filtrado multiselección por marca | MUST |
| | US-22: Filter by color | MUST | RF-22: Filtrado por color | MUST |
| | US-23: Filter by size | MUST | RF-23: Filtrado por talla y disponibilidad | MUST |
| | US-24: Filter by clothing type | MUST | RF-24: Filtrado jerárquico por categoría | MUST |
| | US-25: Filter by material | COULD | RF-25: Filtrado por material textil | COULD |
| | US-26: Filter by store | MUST | RF-26: Filtrado por tienda externa | MUST |
| | US-27: Sort results by price | MUST | RF-27: Ordenamiento de resultados | MUST |
| | US-28: Clear all filters | SHOULD | RF-28: Limpieza global de filtros | SHOULD |
| | US-29: Personalize results | SHOULD | RF-29: Personalización y ponderación de resultados | SHOULD |
| | US-30: View recent searches | COULD | RF-30: Historial y eliminación de búsquedas | COULD |
| | US-31: No-results message | SHOULD | RF-31: Gestión de estado vacío (Zero-results) | SHOULD |
| | US-32: Pagination or infinite scroll | MUST | RF-32: Paginación y carga diferida | MUST |
| **Epic 4. Product Details** | US-33: Open product page | MUST | RF-33: Consulta de ficha técnica de producto | MUST |
| | US-34: See product photos | MUST | RF-34: Galería interactiva de fotografías | MUST |
| | US-35: See available sizes | MUST | RF-35: Consulta de disponibilidad de tallas | MUST |
| | US-36: Group similar products | WOULD | RF-36: Agrupación de productos similares | WOULD |
| | US-37: "You may also like" section | WOULD | RF-37: Recomendaciones ("También te podría gustar") | WOULD |
| | US-38: Link to store page | MUST | RF-38: Redirección externa con enlace de compra | MUST |
| | US-39: See last price update | COULD | RF-39: Visualización de fecha de sincronización | COULD |
| | US-40: Report a wrong product | WOULD | RF-40: Reporte de inconsistencias de producto | WOULD |
| **Epic 5. Price Comparison** | US-41: Highlight cheapest option | COULD | RF-41: Distintivo visual del menor precio | COULD |
| | US-42: Compare products side by side | MUST | RF-42: Cuadro comparativo lado a lado | MUST |
| | US-43: Show prices in COP | MUST | RF-43: Estandarización de formato en COP | MUST |
| **Epic 6. Outfit Builder** | US-44: Start a new outfit | MUST | RF-44: Inicialización de nuevo outfit | MUST |
| | US-45: Add a top to the outfit | MUST | RF-45: Asignación de prenda superior (Top) | MUST |
| | US-46: Add a bottom to the outfit | MUST | RF-46: Asignación de prenda inferior (Bottom) | MUST |
| | US-47: Add shoes to the outfit | MUST | RF-47: Asignación de calzado (Shoes) | MUST |
| | US-48: Add accessories | COULD | RF-48: Asignación de accesorios opcionales | COULD |
| | US-49: Replace a piece | MUST | RF-49: Sustitución contextual de piezas | MUST |
| | US-50: Live outfit update | MUST | RF-50: Actualización reactiva en tiempo real | MUST |
| | US-51: Remove a piece | SHOULD | RF-51: Remoción de prendas individuales | SHOULD |
| | US-52: Add products from search | MUST | RF-52: Adición de productos desde catálogo | MUST |
| | US-53: See outfit total price | MUST | RF-53: Cálculo dinámico de precio total | MUST |
| | US-54: Over-budget warning | MUST | RF-54: Alerta visual de exceso de presupuesto | MUST |
| | US-55: See the store of each piece | MUST | RF-55: Desglose de tiendas y precios por pieza | MUST |
| | US-56: Undo and redo changes | WOULD | RF-56: Control de historial (Deshacer/Rehacer) | WOULD |
| | US-57: Lock a piece | WOULD | RF-57: Bloqueo de prendas en el lienzo (Lock) | WOULD |
| | US-58: Style mismatch tips | WOULD | RF-58: Asistente consultivo de estilo | WOULD |
| **Epic 7. Outfit Visualization** | US-59: Visual outfit composition | MUST | RF-59: Composición visual unificada | MUST |
| | US-60: Virtual mannequin view | WOULD | RF-60: Proyección en maniquí virtual | WOULD |
| | US-61: Zoom in on the outfit | WOULD | RF-61: Control de zoom e inspección | WOULD |
| | US-62: Switch visualization modes | WOULD | RF-62: Alternancia entre modos de visualización | WOULD |
| **Epic 8. Saved Items & Sharing** | US-63: Save favorite products | SHOULD | RF-63: Gestión de productos favoritos (Wishlist) | SHOULD |
| | US-64: Save outfits with a name | MUST | RF-64: Guardado persistente de outfits con nombre | MUST |
| | US-65: Edit or delete saved outfits | SHOULD | RF-65: Edición y eliminación de outfits | SHOULD |
| | US-66: Outfit collections | WOULD | RF-66: Organización en colecciones temáticas | WOULD |
| | US-67: Duplicate a saved outfit | WOULD | RF-67: Duplicación de outfits existentes | WOULD |
| | US-68: Buy each piece in its store | MUST | RF-68: Redirección individual de compra | MUST |
| | US-69: Export shopping list | SHOULD | RF-69: Exportación de lista de compras | SHOULD |
| **Epic 9. Admin & Data Mgmt** | US-70: Manage stores | MUST | RF-70: Gestión administrativa de tiendas (CRUD) | MUST |
| | US-71: Collect products automatically | MUST | RF-71: Motor automatizado de extracción | MUST |
| | US-72: Schedule data collection | COULD | RF-72: Programación periódica de recolección | COULD |
| | US-73: View collection logs | WOULD | RF-73: Consola y registro de auditoría (Logs) | WOULD |
| | US-74: Standardize product data | MUST | RF-74: Estandarización y normalización ontológica | MUST |
| | US-75: Review user reports | WOULD | RF-75: Gestión y resolución de reportes | WOULD |
| | US-76: Edit or hide a product | SHOULD | RF-76: Moderación y edición manual de productos | SHOULD |
| | US-77: View basic statistics | WOULD | RF-77: Tablero de métricas y estadísticas | WOULD |
