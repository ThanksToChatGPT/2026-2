# Especificación de Requerimientos de Software y Análisis del Sistema

**Proyecto:** Web Platform for Outfit Search (Plataforma Web para Búsqueda y Creación de Outfits)  
**Asignatura:** Ingeniería de Software II  
**Institución:** Universidad Nacional de Colombia — Sede Bogotá  
**Documento Fuente:** `Project_Proposal.pdf` (Septiembre 2026)  
**Equipo de Desarrollo:**
- Omar Nicolás Guerrero Guerrero (*Scrum Master*)
- Jonathan Felipe López Núñez (*Developer*)
- Yeswah González Tapia (*Developer*)
- José Alejandro Ordóñez Bolaños (*Developer*)
- Nathalia Chaves Piarpuezán (*Developer*)

---

## 1. Resumen Ejecutivo y Visión del Sistema

### 1.1. Problema y Justificación
Comprar ropa en línea suele ser un proceso fragmentado e ineficiente. Cuando una persona desea armar un atuendo completo (*outfit*), comúnmente debe abrir múltiples pestañas de tiendas diferentes, contrastar precios de forma manual, recordar tallas, colores y cortes disponibles, e intentar proyectar mentalmente si las prendas combinan armoniosamente. No existe una solución unificada que centralice la búsqueda, comparación y composición visual en tiempo real, lo que genera fricción, pérdida de tiempo e incertidumbre al comprar.

### 1.2. Propuesta de Valor y Solución
La plataforma web para búsqueda de outfits centraliza y resuelve este flujo en un único entorno digital:
1. **Descubrimiento Centralizado:** Recolecta y unifica catálogos de diferentes tiendas en línea mediante web scraping programado y APIs públicas de comercio electrónico.
2. **Comparación Inteligente:** Detecta prendas equivalentes o idénticas en distintas tiendas y compara precios, tallas, materiales, colores y valoraciones.
3. **Creador Visual de Outfits (*Outfit Builder*):** Permite ensamblar prendas (superior, inferior, calzado y accesorios), reemplazar piezas al instante y visualizar la composición en estilo *flat-lay* o sobre un maniquí/avatar virtual.
4. **Personalización y Mezcla de Estilos:** Adapta los resultados a las preferencias del usuario (marcas preferidas y excluidas, presupuesto máximo, fit, ocasión, temporada) y permite combinar estilos (ej. *Streetwear* + *Minimalist*).
5. **Decisión y Redirección:** Proporciona desgloses de precios con enlaces directos a las tiendas de origen para completar la compra.

---

## 2. Actores del Sistema

| Actor | Tipo | Descripción |
| :--- | :--- | :--- |
| **Usuario Final (Shopper / Comprador)** | Humano (Primario) | Usuario registrado o invitado que busca prendas, aplica filtros, define su perfil y preferencias, compone outfits interactivos, compara precios entre tiendas y guarda sus combinaciones favoritas. Es redirigido a las tiendas externas para la compra. |
| **Tiendas Colaboradoras / Externas (Partner Stores)** | Sistema Externo (Secundario) | Sitios web y APIs de comercio electrónico de terceros. Son la fuente primaria de datos de productos (nombres, precios, stock, imágenes, tallas, materiales, ratings). La compra final siempre concluye en su plataforma. |
| **Motor de Extracción y Sincronización (Scraper / Ingestion Worker)** | Sistema Automatizado Interno | Servicio en segundo plano (Python/Puppeteer) que ejecuta extracciones programadas, normaliza catálogos, detecta similitudes de productos y actualiza disponibilidad y precios. |
| **Administrador del Sistema** | Humano (Secundario) | Usuario con privilegios para supervisar la salud de los scrapers, gestionar fuentes de tiendas habilitadas, auditar métricas del sistema y moderar el catálogo indexado. |

---

## 3. Catálogo Completo de Requerimientos Funcionales (RF)

### Módulo 1: Gestión de Usuarios, Autenticación y Preferencias de Estilo
- **RF-01: Registro y Autenticación de Usuarios**
  - **Descripción:** El sistema debe permitir a los usuarios crear una cuenta personal mediante correo electrónico y contraseña segura, o mediante proveedores OAuth (ej. Google), así como iniciar y cerrar sesión.
  - **Prioridad:** Alta (Must Have).
  - **Precondiciones:** El correo electrónico no debe estar previamente registrado.
  - **Reglas de Negocio:** Las contraseñas deben cifrarse con algoritmos seguros (bcrypt/argon2). Se debe emitir un token JWT con tiempo de expiración para sesiones seguras.
- **RF-02: Perfil y Panel de Preferencias de Estilo y Compras**
  - **Descripción:** El usuario debe poder configurar y editar en cualquier momento su panel de preferencias personales, incluyendo: marcas favoritas, marcas excluidas/no deseadas, estilos de vestir preferidos, colores predilectos, tallas habituales (superior, inferior, calzado), tipo de ajuste/fit, ocasión de uso, temporada y presupuesto límite total o por prenda.
  - **Prioridad:** Alta (Must Have).
  - **Precondiciones:** Usuario autenticado en la plataforma.
  - **Reglas de Negocio:** Las preferencias guardadas deben servir como criterio predeterminado de filtrado y ponderación en los módulos de búsqueda y recomendación.
- **RF-03: Navegación en Modo Invitado**
  - **Descripción:** El sistema debe permitir a usuarios no registrados explorar el catálogo general, utilizar el buscador y probar el constructor de outfits, requiriendo registro únicamente para guardar combinaciones, almacenar preferencias o crear alertas.
  - **Prioridad:** Media (Should Have).

### Módulo 2: Búsqueda Multitienda, Catálogo Unificado y Filtros
- **RF-04: Búsqueda Multitienda Unificada**
  - **Descripción:** El sistema debe permitir buscar prendas ingresando palabras clave en una barra de búsqueda, consultando el catálogo agregado de todas las tiendas indexadas y devolviendo un listado integrado y consistente de resultados.
  - **Prioridad:** Alta (Must Have).
  - **Entradas:** Texto de búsqueda (ej. "chaqueta denim oversize").
  - **Salidas:** Lista de tarjetas de productos consolidadas con imagen, nombre, marca, tienda de origen y precio.
- **RF-05: Filtrado Avanzado y Facetado**
  - **Descripción:** El sistema debe proporcionar filtros multifaceta que permitan refinar los resultados de búsqueda por: rango de precio, marca, tienda, material, color, talla disponible, categoría/subcategoría de prenda y calificación/rating de la tienda o producto.
  - **Prioridad:** Alta (Must Have).
  - **Reglas de Negocio:** Los filtros deben aplicarse de forma aditiva y dinámica actualizando el contador de resultados sin recargar la página completa.
- **RF-06: Ordenamiento de Resultados**
  - **Descripción:** El usuario debe poder ordenar los productos por precio (menor a mayor / mayor a menor), calificación promedio, novedad en el catálogo y relevancia/afinidad con sus preferencias de perfil.
  - **Prioridad:** Media (Should Have).

### Módulo 3: Detección de Similares, Comparación de Precios y Enlace de Compra
- **RF-07: Agrupación y Detección de Productos Similares / Equivalentes**
  - **Descripción:** El sistema debe analizar los atributos (nombre, categoría, color, corte, material) de las prendas de distintas tiendas para agrupar ítems idénticos o con alta similitud visual y funcional en una única vista consolidada.
  - **Prioridad:** Alta (Must Have).
  - **Reglas de Negocio:** Se debe calcular un índice de coincidencia o similitud para evitar falsos positivos en prendas con descripciones genéricas.
- **RF-08: Vista Comparativa de Precios por Prenda**
  - **Descripción:** Para una prenda seleccionada o grupo de equivalentes, el sistema debe desplegar una tabla comparativa que desglose: tienda que lo comercializa, precio actual, costos de envío estimados (si están disponibles), tallas en stock y enlace directo al comercio externo.
  - **Prioridad:** Alta (Must Have).
  - **Salidas:** Tabla con orden ascendente de precio y botón de acción "Comprar en [Tienda]".
- **RF-09: Redirección Segura a Tienda Externa**
  - **Descripción:** Al hacer clic en una opción de compra, el sistema debe abrir en una nueva pestaña el enlace exacto a la página de detalle del producto en la tienda de origen, registrando el evento de clic con fines analíticos sin interceptar transacciones financieras.
  - **Prioridad:** Alta (Must Have).

### Módulo 4: Creador Visual de Outfits (*Outfit Builder*) y Mezcla de Estilos
- **RF-10: Constructor de Outfits Interactivo (Lienzo / Canvas)**
  - **Descripción:** El sistema debe ofrecer un espacio interactivo de diseño de atuendos donde el usuario pueda seleccionar y posicionar al menos 4 slots principales: Parte Superior (*Top*), Parte Inferior (*Bottom*), Calzado (*Footwear*) y Accesorios (*Accessories*).
  - **Prioridad:** Alta (Must Have).
- **RF-11: Reemplazo Dinámico de Prendas en Tiempo Real**
  - **Descripción:** El usuario debe poder sustituir individualmente cualquier prenda del outfit por otra alternativa sugerida o seleccionada del catálogo, actualizándose instantáneamente la previsualización visual y el precio total acumulado del conjunto.
  - **Prioridad:** Alta (Must Have).
- **RF-12: Mezcla y Fusión de Estilos (*Style-Mixing*)**
  - **Descripción:** El sistema debe permitir al usuario seleccionar dos o más estilos simultáneos (ej. *Streetwear* + *Minimalist*, o *Casual* + *Formal*) para ponderar las recomendaciones de prendas y outfits sugeridos acordes a dicha combinación híbrida.
  - **Prioridad:** Media (Should Have).
- **RF-13: Visualización de Outfit (Flat-lay y Maniquí/Avatar)**
  - **Descripción:** El sistema debe presentar la composición de prendas en dos modos de visualización:
    1. *Flat-lay*: Composición plana armónica de las imágenes de las prendas sin fondo.
    2. *Maniquí/Avatar virtual*: Superposición básica proporcional de las prendas sobre una silueta de maniquí bidimensional para juzgar el look completo.
  - **Prioridad:** Alta para Flat-lay (Must Have); Media para Maniquí (Should Have).
- **RF-14: Resumen de Costo Total del Outfit**
  - **Descripción:** El constructor debe calcular y exhibir en tiempo real el precio total del outfit resultante de la suma de las prendas seleccionadas, indicando si se ajusta o excede el presupuesto máximo configurado en las preferencias del usuario.
  - **Prioridad:** Alta (Must Have).

### Módulo 5: Guardado, Favoritos y Gestión de Colecciones
- **RF-15: Guardado de Outfits en Colecciones Personales**
  - **Descripción:** El usuario registrado debe poder guardar combinaciones completas de outfits con un nombre personalizado, fecha de creación y etiquetas de ocasión (ej. "Entrevista de trabajo", "Salida fin de semana").
  - **Prioridad:** Alta (Must Have).
- **RF-16: Lista de Prendas Favoritas (*Wishlist*)**
  - **Descripción:** El usuario debe poder marcar prendas individuales con un icono de "favorito" para almacenarlas en su lista personal de deseos y utilizarlas posteriormente en el creador de outfits.
  - **Prioridad:** Alta (Must Have).
- **RF-17: Historial y Gestión de Outfits Guardados**
  - **Descripción:** El usuario debe contar con un panel donde pueda listar, filtrar, editar (modificar prendas del conjunto) y eliminar outfits previamente guardados.
  - **Prioridad:** Media (Should Have).

### Módulo 6: Extracción, Normalización y Actualización de Catálogo
- **RF-18: Ingesta Automatizada de Productos (Scraping y APIs)**
  - **Descripción:** El subsistema de datos debe extraer de forma programada y automatizada la información de catálogos desde las tiendas soportadas mediante scripts de scraping (BeautifulSoup/Scrapy/Puppeteer) o APIs públicas.
  - **Prioridad:** Alta (Must Have).
- **RF-19: Normalización y Limpieza de Atributos**
  - **Descripción:** El sistema debe procesar los datos crudos extraídos para estandarizar categorías, formatos de tallas (conversión S/M/L/numéricas), nombres de colores, unidades de moneda e URLs canónicas de imágenes.
  - **Prioridad:** Alta (Must Have).
- **RF-20: Verificación de Disponibilidad y Alertas de Stock Desactualizado**
  - **Descripción:** El sistema debe actualizar periódicamente el estado de disponibilidad y precio de los productos cacheados; si una prenda guardada en un outfit queda sin stock en la tienda externa, el sistema debe notificar al usuario y sugerir un reemplazo similar.
  - **Prioridad:** Baja (Could Have).

---

## 4. Catálogo Completo de Requerimientos No Funcionales (RNF)

| Código | Categoría (ISO/IEC 25010) | Requerimiento No Funcional | Métrica / Criterio de Verificación |
| :--- | :--- | :--- | :--- |
| **RNF-01** | **Rendimiento (Tiempo de Respuesta)** | Las búsquedas por catálogo y aplicación de filtros deben retornar resultados y renderizar las tarjetas de producto en el frontend en un tiempo menor a **1.5 segundos** bajo condiciones normales de red. | Percentil 95 ($P_{95}$) de latencia en peticiones `/api/search` $< 1200\text{ ms}$. |
| **RNF-02** | **Rendimiento (Interactividad)** | En el *Outfit Builder*, el reemplazo de una prenda y el recálculo dinámico del costo total deben ejecutarse en menos de **200 milisegundos** sin recarga completa de la interfaz (*First Input Delay / INP óptimo*). | Interacción de swap reactiva en cliente $< 200\text{ ms}$. |
| **RNF-03** | **Escalabilidad y Concurrencia** | La arquitectura backend y la base de datos deben soportar un mínimo de **100 usuarios concurrentes** realizando búsquedas simultáneas sin degradación del servicio ni aumento de errores HTTP 5xx. | Tasa de errores HTTP $< 0.1\%$ en pruebas de carga con Locust o k6 a 100 VU. |
| **RNF-04** | **Disponibilidad** | La plataforma web debe mantener una disponibilidad mensual mínima del **99.0%** en horario productivo, excluyendo ventanas de mantenimiento previamente anunciadas. | Uptime verificado por monitor externo (ej. UptimeRobot / BetterStack) $\ge 99.0\%$. |
| **RNF-05** | **Seguridad (Cifrado y Autenticación)** | Todas las comunicaciones cliente-servidor deben usar exclusivamente protocolo seguro **HTTPS/TLS 1.3**. Las contraseñas de usuarios deben almacenarse con hashing salteado mediante **bcrypt (cost factor $\ge 12$)** o **Argon2id**. | Auditoría de tráfico y base de datos: cero credenciales en texto plano; calificación SSL Labs 'A'. |
| **RNF-06** | **Seguridad (Protección de APIs)** | La API REST de backend debe implementar limitación de tasa (*Rate Limiting*) para mitigar ataques de fuerza bruta y DoS (máximo 60 peticiones por minuto por IP para endpoints públicos y 120 para autenticados). | Respuestas HTTP 429 *Too Many Requests* ante ráfagas anómalas. |
| **RNF-07** | **Usabilidad y Accesibilidad** | La interfaz de usuario desarrollada en React/Next.js con Tailwind CSS debe ser completamente adaptable (*Responsive Design* para resoluciones móviles $\ge 375\text{px}$, tablets y desktop) y cumplir con las pautas **WCAG 2.1 Nivel AA** en contraste de color y navegación por teclado. | Puntuación de Accesibilidad en Google Lighthouse $\ge 90/100$. |
| **RNF-08** | **Mantenibilidad y Modularidad** | El código fuente debe estructurarse siguiendo una separación clara de responsabilidades (capa de presentación frontend, API gateway/servicios backend, módulo de scraping desacoplado y capa de persistencia). La cobertura de pruebas unitarias sobre la lógica de negocio y normalización debe ser $\ge 70\%$. | Reporte de cobertura de tests (Jest/Vitest/PyTest) $\ge 70\%$; linter ESLint/Prettier sin errores. |
| **RNF-09** | **Confiabilidad y Tolerancia a Fallos** | Si una tienda externa falla, bloquea una petición de scraping o modifica su maquetación, el sistema central debe aislar la falla sin interrumpir la operación del catálogo general, registrando un log de advertencia y manteniendo el último caché válido del producto. | Manejo de excepciones en workers de scraping; cero caídas en cascada del servidor API principal. |
| **RNF-10** | **Ética de Extracción (Scraping Politeness)** | Los scrapers implementados en Python/Puppeteer deben respetar los encabezados de cortesía (*robots.txt*, retardos mínimos entre peticiones de 1 a 2 segundos por dominio y rotación moderada de User-Agents) para evitar sobrecargar los servidores de las tiendas externas. | Configuración de concurrencia y delay en `scrapy` o `beautifulsoup` auditada en repositorio. |
| **RNF-11** | **Portabilidad y Compatibilidad** | La aplicación web debe ser compatible y funcionar sin alteraciones en las últimas dos versiones estables de los navegadores más utilizados: Google Chrome, Mozilla Firefox, Apple Safari y Microsoft Edge. | Validación cruzada en BrowserStack o pruebas manuales en Chromium, WebKit y Gecko. |

---

## 5. Historias de Usuario (User Stories) y Criterios de Aceptación (Acceptance Criteria)

Las historias de usuario siguen el estándar ágil:  
`Como [Rol del Actor], quiero [Funcionalidad/Acción], para [Beneficio o Valor Obtenido]`.  
Los criterios de aceptación se especifican bajo la sintaxis **Gherkin (Dado que / Cuando / Entonces)** para garantizar su verificabilidad en pruebas automatizadas y funcionales.

---

### Épica 1: Gestión de Identidad y Preferencias de Estilo

#### **US-01: Registro y Configuración de Preferencias Iniciales**
- **Enunciado:** **Como** nuevo usuario interesado en moda, **quiero** registrarme en la plataforma y definir mis preferencias de estilo, marcas y presupuesto, **para** que las prendas y outfits sugeridos se adapten a mi identidad y capacidad económica.
- **RF / RNF Asociados:** RF-01, RF-02, RNF-05, RNF-07.
- **Criterios de Aceptación:**
  - **Escenario 1 (Registro Exitoso y Cuestionario de Preferencias):**
    - **Dado que** un usuario no registrado ingresa al formulario de registro con un correo válido y una contraseña que cumple los requisitos mínimos de seguridad (8+ caracteres, mayúscula y número),
    - **Cuando** confirma el formulario y completa la selección de marcas preferidas, estilos (ej. Urbano, Minimalista) y tallas,
    - **Entonces** el sistema crea la cuenta, persiste las preferencias asociadas en la base de datos, inicia sesión emitiendo un token seguro y redirige al usuario a la pantalla principal con recomendaciones adaptadas.
  - **Escenario 2 (Intento con Correo Duplicado):**
    - **Dado que** se ingresa un correo que ya existe en el sistema,
    - **Cuando** el usuario envía el formulario,
    - **Entonces** el sistema rechaza la solicitud, muestra un mensaje de alerta legible sin revelar información sensible y no crea registros duplicados.

#### **US-02: Edición Dinámica de Preferencias y Marcas Excluidas**
- **Enunciado:** **Como** usuario registrado, **quiero** modificar mis preferencias en cualquier momento y marcar marcas que no me gustan o no deseo comprar, **para** no ver productos de dichas marcas en mis búsquedas.
- **RF / RNF Asociados:** RF-02, RNF-01.
- **Criterios de Aceptación:**
  - **Escenario 1 (Exclusión de Marcas):**
    - **Dado que** el usuario ingresa a su panel de preferencias y añade la marca "Marca X" a la lista de marcas no deseadas,
    - **Cuando** guarda los cambios y realiza una nueva búsqueda en el catálogo,
    - **Entonces** ningún producto de la "Marca X" debe aparecer en los resultados ni en los outfits sugeridos.

---

### Épica 2: Exploración Multitienda y Comparación Inteligente

#### **US-03: Búsqueda Multitienda con Filtros Facetados**
- **Enunciado:** **Como** comprador en línea, **quiero** buscar prendas por término y filtrar por talla, color, precio y material en un catálogo que reúne múltiples tiendas, **para** encontrar exactamente lo que busco sin abrir decenas de sitios web.
- **RF / RNF Asociados:** RF-04, RF-05, RF-06, RNF-01, RNF-07.
- **Criterios de Aceptación:**
  - **Escenario 1 (Búsqueda y Filtrado Simultáneo):**
    - **Dado que** el usuario escribe "Pantalón cargo" en el buscador y selecciona los filtros: Talla "M", Color "Negro" y Rango de Precio "$50.000 - $150.000",
    - **Cuando** se aplican los filtros,
    - **Entonces** el catálogo muestra en menos de 1.5 segundos únicamente productos que coinciden con todos los criterios seleccionados, indicando claramente la tienda de origen y precio de cada uno.
  - **Escenario 2 (Búsqueda sin Resultados):**
    - **Dado que** la combinación de filtros no produce coincidencias,
    - **Cuando** concluye la consulta,
    - **Entonces** la interfaz muestra un estado vacío amigable con sugerencias para relajar los filtros aplicados.

#### **US-04: Comparación de Precios de Productos Equivalentes y Enlace de Compra**
- **Enunciado:** **Como** comprador consciente de mi presupuesto, **quiero** ver las diferentes tiendas que venden una misma prenda o ítems muy similares junto a sus precios, **para** elegir la opción más económica y ser dirigido a la tienda a comprarla.
- **RF / RNF Asociados:** RF-07, RF-08, RF-09, RNF-01.
- **Criterios de Aceptación:**
  - **Escenario 1 (Visualización de Tabla Comparativa):**
    - **Dado que** el usuario selecciona una prenda que posee equivalentes en 3 tiendas distintas,
    - **Cuando** abre el modal o vista de comparación de precios,
    - **Entonces** el sistema muestra una lista ordenada de menor a mayor precio con el nombre de cada tienda, costo y disponibilidad de tallas.
  - **Escenario 2 (Redirección Externa):**
    - **Dado que** el usuario hace clic sobre el botón "Comprar en [Tienda Z]",
    - **Cuando** se dispara la acción,
    - **Entonces** el navegador abre una nueva pestaña (`target="_blank" rel="noopener noreferrer"`) apuntando a la URL directa del producto en Tienda Z.

---

### Épica 3: Creador Visual de Outfits (*Outfit Builder*) y Mezcla de Estilos

#### **US-05: Construcción Interactiva y Reemplazo en Tiempo Real**
- **Enunciado:** **Como** usuario aficionado a la moda, **quiero** combinar prendas superiores, inferiores, calzado y accesorios en un lienzo visual e intercambiar cualquier prenda con un clic, **para** ver instantáneamente cómo luce el atuendo y cómo varía el precio total.
- **RF / RNF Asociados:** RF-10, RF-11, RF-14, RNF-02, RNF-07.
- **Criterios de Aceptación:**
  - **Escenario 1 (Reemplazo Instantáneo de una Prenda):**
    - **Dado que** el usuario tiene un outfit armado con una camiseta blanca, jean azul y zapatillas,
    - **Cuando** hace clic en el slot del jean y selecciona un pantalón negro alternativo,
    - **Entonces** la imagen del pantalón se sustituye en el lienzo en menos de 200 ms y la suma del precio total del outfit se actualiza automáticamente.
  - **Escenario 2 (Alerta de Presupuesto Excedido):**
    - **Dado que** el usuario fijó un presupuesto máximo de $200.000 en sus preferencias,
    - **Cuando** la suma de las prendas del outfit actual alcanza $225.000,
    - **Entonces** el sistema resalta el monto con una advertencia visual indicando que se ha superado el presupuesto por $25.000.

#### **US-06: Mezcla de Estilos Combinados (*Style-Mixing*)**
- **Enunciado:** **Como** creador de estilo versátil, **quiero** activar dos estilos simultáneos (ej. *Streetwear* + *Minimalist*), **para** recibir sugerencias de prendas que equilibren ambas corrientes de moda en mi outfit.
- **RF / RNF Asociados:** RF-12, RF-05.
- **Criterios de Aceptación:**
  - **Escenario 1 (Fusión de Dos Estilos):**
    - **Dado que** el usuario selecciona las etiquetas de estilo "Streetwear" y "Minimalista" en el selector de mezcla,
    - **Cuando** solicita sugerencias automáticas para completar su outfit,
    - **Entonces** el recomendador prioriza prendas que contengan atributos compatibles con ambos estilos (ej. cortes holgados en paletas monocromáticas o neutras).

#### **US-07: Visualización de Outfit en Flat-lay y Maniquí Virtual**
- **Enunciado:** **Como** usuario visual, **quiero** alternar entre una vista de composición plana (*flat-lay*) y una silueta sobre maniquí, **para** evaluar de manera realista el contraste y proporciones de las prendas antes de decidirme.
- **RF / RNF Asociados:** RF-13, RNF-07.
- **Criterios de Aceptación:**
  - **Escenario 1 (Cambio de Modo de Visualización):**
    - **Dado que** el usuario tiene un conjunto de prendas en el lienzo,
    - **Cuando** conmuta el selector de "Modo Flat-lay" a "Modo Maniquí",
    - **Entonces** las imágenes de las prendas se ordenan y escalan proporcionalmente sobre la silueta anatómica de referencia sin deformarse ni perder resolución.

---

### Épica 4: Guardado, Colecciones y Gestión Personal

#### **US-08: Guardado de Outfit y Favoritos**
- **Enunciado:** **Como** usuario registrado, **quiero** guardar mis outfits creados con un nombre y fecha, y marcar prendas favoritas, **para** poder consultarlos, editarlos o comprarlos en el futuro.
- **RF / RNF Asociados:** RF-15, RF-16, RF-17, RNF-03.
- **Criterios de Aceptación:**
  - **Escenario 1 (Guardado Exitoso de Outfit):**
    - **Dado que** un usuario autenticado ha compuesto un outfit completo y presiona "Guardar Outfit",
    - **Cuando** ingresa el nombre "Look Concierto 2026" y selecciona la ocasión "Casual / Fiesta",
    - **Entonces** el outfit queda registrado en su perfil y accesible desde su galería personal de outfits guardados.
  - **Escenario 2 (Intento de Guardado por Usuario Invitado):**
    - **Dado que** un usuario no autenticado presiona "Guardar Outfit",
    - **Cuando** se ejecuta la acción,
    - **Entonces** se despliega una ventana modal amigable invitándolo a registrarse o iniciar sesión, preservando temporalmente en memoria el outfit compuesto para no perder el progreso.

---

### Épica 5: Infraestructura de Datos, Ingesta y Calidad

#### **US-09: Sincronización Automática y Resiliencia de Scraping**
- **Enunciado:** **Como** administrador de la plataforma, **quiero** que los scrapers ejecuten sincronizaciones periódicas con manejo de errores y respeto a las tiendas, **para** mantener precios y stock actualizados sin incurrir en bloqueos ni caídas del sistema.
- **RF / RNF Asociados:** RF-18, RF-19, RNF-09, RNF-10.
- **Criterios de Aceptación:**
  - **Escenario 1 (Extracción y Normalización):**
    - **Dado que** el worker de scraping inicia su tarea programada,
    - **Cuando** extrae el catálogo de una tienda asociada,
    - **Entonces** normaliza los campos obligatorios (nombre, precio en COP/USD, imagen en alta resolución, tallas, enlace) y los inserta o actualiza en la base de datos sin generar registros duplicados.
  - **Escenario 2 (Tolerancia a Falla de una Tienda):**
    - **Dado que** una de las tiendas asociadas responde con un error HTTP 503 o bloqueo de IP,
    - **Cuando** el worker detecta la anomalía,
    - **Entonces** interrumpe reintentos destructivos, genera un log estructurado de advertencia y el resto del catálogo y la aplicación web continúan operando con normalidad.

---

## 6. User Story Mapping para Planificación del Proyecto

El *User Story Mapping* organiza el trabajo a lo largo de las actividades clave del viaje del usuario (*User Journey*) en el eje horizontal, y prioriza las funcionalidades por releases iterativos en el eje vertical (MVP, Release 2 y Release 3).

```
+-----------------------------------------------------------------------------------------------------------------------------+
|                                           USER STORY MAPPING - PLATAFORMA DE OUTFITS                                         |
+-----------------------------------------------------------------------------------------------------------------------------+
| ACTIVIDADES   | 1. Cuenta y Perfil  | 2. Búsqueda y       | 3. Creación Visual | 4. Comparación y    | 5. Guardado y       |
| DEL USUARIO   |    de Estilo        |    Exploración      |    de Outfits      |    Decisión         |    Persistencia     |
+---------------+---------------------+---------------------+--------------------+---------------------+---------------------+
| PASOS /       | • Registrarse /     | • Buscar por texto  | • Seleccionar slot | • Ver tiendas       | • Guardar outfit    |
| TAREAS        |   Iniciar sesión    | • Filtrar catálogo  | • Sustituir prenda |   disponibles       | • Marcar favoritos  |
|               | • Fijar marcas y    | • Ordenar precio /  | • Previsualizar    | • Comparar precios  | • Ver biblioteca de |
|               |   presupuesto       |   popularidad       |   conjunto         | • Clic de compra    |   combinaciones     |
+===============+=====================+=====================+====================+=====================+=====================+
| RELEASE 1     | US-01: Registro y   | US-03: Búsqueda     | US-05: Outfit      | US-04: Comparación  | US-08: Guardado de  |
| (MVP)         | login básico con    | unificada multitienda| Builder básico con | de precios y link   | outfits y lista de  |
| "Core         | preferencias        | con filtros clave   | 4 slots y cálculo  | de redirección a    | favoritos básica.   |
| Experience"   | esenciales.         | (precio, talla,     | de costo total.    | tienda externa.     |                     |
|               |                     | color).             |                    |                     |                     |
+---------------+---------------------+---------------------+--------------------+---------------------+---------------------+
| RELEASE 2     | US-02: Marcas       | Filtros avanzados   | US-06: Mezcla de   | US-09: Ingesta      | Gestión avanzada:   |
| "Refinement & | excluidas, tallas   | por material,       | estilos (Style-    | automatizada de     | carpetas, etiquetas |
| Discovery"    | múltiples y ocasión | rating y afinidad   | Mixing: Streetwear | scraping con        | por evento y filtro |
|               | de uso específica.  | de perfil.          | + Minimalist).     | detección de stock. | de guardados.       |
+---------------+---------------------+---------------------+--------------------+---------------------+---------------------+
| RELEASE 3     | Onboarding social   | Recomendaciones     | US-07: Modo        | Alertas de baja de  | Compartir outfits   |
| "Enhancements | interactivo y modo  | basadas en historial| maniquí / avatar   | precio y detección  | públicamente /      |
| & Polish"     | invitado fluido.    | de navegación.      | 2D interactivo.    | semántica avanzada. | enlace web público. |
+-----------------------------------------------------------------------------------------------------------------------------+
```

### Planificación de Sprints y Asignación de Roles del Equipo

Basado en la conformación del equipo del documento fuente:
- **Omar Nicolás Guerrero Guerrero:** *Scrum Master* (Gestión del backlog, facilitador de sprints, control de impedimentos y aseguramiento de calidad de entregables).
- **Jonathan Felipe López Núñez & Yeswah González Tapia:** *Desarrollo Backend, Ingesta & Base de Datos* (APIs REST en Node.js/Express, arquitectura de datos en MongoDB/PostgreSQL, scripts de scraping en Python/Puppeteer y normalización).
- **José Alejandro Ordóñez Bolaños & Nathalia Chaves Piarpuezán:** *Desarrollo Frontend & Experiencia de Usuario* (Interfaz Next.js/React, Tailwind CSS, lienzo interactivo del Outfit Builder, filtros facetados y visualización de maniquí/flat-lay).

#### Asignación de Releases e Iteraciones:
- **Sprint 1 & 2 (Fundaciones y MVP - Release 1):**
  - Configuración de repositorio, pipelines CI/CD y despliegue base (Vercel / Render).
  - Implementación de modelo de datos de usuarios, productos y autenticación JWT (US-01).
  - Ingesta inicial de 2 tiendas de prueba mediante scraping básico.
  - Frontend: Catálogo de búsqueda con filtros esenciales y tarjeta de producto (US-03).
  - Lienzo inicial del Outfit Builder con slots y cálculo de presupuesto (US-05).
  - Tabla comparativa de precios y enlace saliente (US-04).
  - Guardado de outfits en base de datos (US-08).
- **Sprint 3 & 4 (Evolución y Optimización - Release 2):**
  - Panel completo de preferencias y exclusión de marcas (US-02).
  - Módulo de Style-Mixing algorítmico (US-06).
  - Robustecimiento del worker de scraping con reintentos y tolerancia a fallos (US-09).
  - Pruebas de rendimiento (RNF-01, RNF-02) y accesibilidad WCAG (RNF-07).
- **Sprint 5 (Pulimento y Extras - Release 3):**
  - Implementación del modo silueta / maniquí virtual (US-07).
  - Alertas de cambio de stock y optimización de caché.
  - Pruebas de integración extremo a extremo y entrega final.

---

## 7. Matriz de Trazabilidad y Referencias Cruzadas (Traceability Matrix)

Esta matriz vincula cada requerimiento funcional y no funcional con su respectiva historia de usuario, criterios de verificación, componente tecnológico responsable y fase de release:

| ID Requerimiento | Tipo | Descripción Breve | Historia de Usuario (US) | Módulo / Componente Técnico | Criterio de Verificación / Acceptance | Release |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| **RF-01** | Funcional | Registro y login de usuarios | US-01 | Backend (Node/Express) + DB | Pruebas de autenticación JWT y hashing bcrypt | R1 (MVP) |
| **RF-02** | Funcional | Preferencias de estilo y presupuesto | US-01, US-02 | Backend (Preferences API) + Frontend | Persistencia en DB y aplicación en filtros | R1 / R2 |
| **RF-03** | Funcional | Navegación como invitado | US-08 | Frontend (Local State / Next.js) | Acceso a búsqueda y builder sin login previo | R1 (MVP) |
| **RF-04** | Funcional | Búsqueda multitienda unificada | US-03 | Search Service + MongoDB/PostgreSQL | Query de texto indexado en tiempo $< 1.5\text{ s}$ | R1 (MVP) |
| **RF-05** | Funcional | Filtrado multifaceta | US-03 | Frontend Filter Component + API | Filtrado por precio, color, talla y material | R1 (MVP) |
| **RF-06** | Funcional | Ordenamiento de resultados | US-03 | Frontend / API Query Params | Orden por precio, rating y relevancia | R1 (MVP) |
| **RF-07** | Funcional | Detección de productos similares | US-04 | Backend Matching Service | Agrupación por atributos coincidentes | R1 (MVP) |
| **RF-08** | Funcional | Tabla comparativa de precios | US-04 | Frontend Comparison Modal | Lista ordenada de menor a mayor precio | R1 (MVP) |
| **RF-09** | Funcional | Redirección a tienda externa | US-04 | Frontend Anchor Tag (`_blank`) | Redirección con URL original sin intermediación | R1 (MVP) |
| **RF-10** | Funcional | Outfit Builder interactivo (4 slots) | US-05 | React Canvas / State Manager | Carga y renderizado de top, bottom, shoes, acc | R1 (MVP) |
| **RF-11** | Funcional | Reemplazo de prenda en tiempo real | US-05 | React Component State | Sustitución visual reactiva $< 200\text{ ms}$ | R1 (MVP) |
| **RF-12** | Funcional | Mezcla de estilos (*Style-Mixing*) | US-06 | Recommendation Filter Service | Filtrado híbrido por múltiples tags de estilo | R2 |
| **RF-13** | Funcional | Visualización Flat-lay y Maniquí | US-07 | Frontend SVG/Canvas Layer | Conmutación visual entre flat-lay y silueta 2D | R1 / R3 |
| **RF-14** | Funcional | Cálculo de presupuesto en tiempo real| US-05 | React Memoized Calculation | Suma acumulada y alerta ante superación de tope| R1 (MVP) |
| **RF-15** | Funcional | Guardado de outfits en colecciones | US-08 | Backend Outfits API + DB | Registro relacional/documental por usuario | R1 (MVP) |
| **RF-16** | Funcional | Lista de prendas favoritas (*Wishlist*) | US-08 | Backend Favorites API + DB | Marcado instantáneo de prenda favorita | R1 (MVP) |
| **RF-17** | Funcional | Gestión y edición de outfits guardados| US-08 | Frontend Library View | Operaciones CRUD de outfits guardados | R2 |
| **RF-18** | Funcional | Ingesta por Scraping y APIs | US-09 | Python Scraping / Puppeteer Worker | Extracción exitosa y carga periódica a base | R1 (MVP) |
| **RF-19** | Funcional | Normalización de datos extraídos | US-09 | ETL Data Cleaning Pipeline | Unificación de tallas, colores y moneda en DB | R1 (MVP) |
| **RF-20** | Funcional | Alerta de stock desactualizado | US-09 | Worker de verificación | Detección de enlaces 404 / sin stock | R3 |
| **RNF-01** | No Func. | Tiempo de búsqueda $< 1.5\text{ s}$ | US-03 | API Gateway + DB Indexing | Benchmarks de latencia $P_{95} < 1200\text{ ms}$ | R1 (MVP) |
| **RNF-02** | No Func. | Interactividad de swap $< 200\text{ ms}$| US-05 | Next.js / Tailwind Client | Medición INP / FID en consola de navegador | R1 (MVP) |
| **RNF-03** | No Func. | Concurrencia de 100 usuarios | US-03 | Node.js Server + Connection Pool | Test de estrés con Locust / k6 a 100 VU | R2 |
| **RNF-04** | No Func. | Disponibilidad $\ge 99.0\%$ | Todas | Infraestructura Cloud (Vercel/Render)| Monitor de uptime continuo | R2 |
| **RNF-05** | No Func. | Hashing bcrypt y HTTPS TLS 1.3 | US-01 | Auth Module + SSL Cert | Inspección de seguridad y prueba de penetración | R1 (MVP) |
| **RNF-06** | No Func. | Rate Limiting en API | US-01, US-03 | Express Middleware (express-rate-limit)| Código HTTP 429 ante $> 60\text{ req/min}$ | R2 |
| **RNF-07** | No Func. | Responsive Design y WCAG 2.1 AA | Todas | Tailwind CSS + Accessible Components | Puntuación Lighthouse $\ge 90$ en Accesibilidad | R1 (MVP) |
| **RNF-08** | No Func. | Cobertura de tests unitarios $\ge 70\%$| Todas | Jest / Vitest / PyTest | Reporte de coverage integrado en GitHub Actions | R2 |
| **RNF-09** | No Func. | Tolerancia a fallas de tiendas | US-09 | Worker de Ingesta Asíncrono | Falla aislada no tumba el servidor web | R2 |
| **RNF-10** | No Func. | Scraping ético y politeness | US-09 | Scrapy / Python Worker Config | Delay de 1-2 s y respeto a robots.txt | R1 (MVP) |
| **RNF-11** | No Func. | Compatibilidad en navegadores | Todas | Frontend Build (Babel/PostCSS) | Pruebas exitosas en Chrome, Firefox, Safari, Edge| R1 (MVP) |

---

## 8. Referencias y Documentación Asociada

1. **Documento Base del Proyecto:** `Project_Proposal.pdf` — Universidad Nacional de Colombia, Departamento de Ingeniería de Sistemas y Computación, Asignatura Ingeniería de Software II (Septiembre 2026).
2. **Estándar de Calidad del Producto de Software:** ISO/IEC 25010:2011 (*Systems and software engineering — Systems and software Product Quality Requirements and Evaluation - SQuaRE*).
3. **Pautas de Accesibilidad para el Contenido Web:** W3C Web Content Accessibility Guidelines (WCAG) 2.1 Nivel AA.
4. **Metodología de Desarrollo y Estimación:** Scrum Framework y *User Story Mapping: Discover the Whole Story, Build the Right Product* (Jeff Patton).
5. **Tecnologías del Stack Definidas:**
   - Frontend: [Next.js](https://nextjs.org/) + [React](https://react.dev/) + [Tailwind CSS](https://tailwindcss.com/)
   - Backend: [Node.js](https://nodejs.org/) + [Express](https://expressjs.com/)
   - Base de Datos: [MongoDB](https://www.mongodb.com/) / [PostgreSQL](https://www.postgresql.org/)
   - Extracción de Datos: [Python](https://www.python.org/) ([BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) / [Scrapy](https://scrapy.org/)) o [Puppeteer](https://pptr.dev/)
   - Despliegue y Control de Versiones: [GitHub](https://github.com/), [Vercel](https://vercel.com/) / [Render](https://render.com/).
