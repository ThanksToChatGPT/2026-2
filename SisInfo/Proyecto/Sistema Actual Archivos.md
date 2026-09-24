# Arquitectura y Diagnóstico del Gestor Documental Actual (Dropbox)
## Loard Construcciones S.A.S. — Diagnóstico y Contexto del Negocio

---

## 1. Introduccion

Actualmente, la compañía utiliza **Dropbox** como su repositorio centralizado en la nube sincronizado en estaciones de trabajo bajo la carpeta raíz `Dropbox/`. Dicho almacenamiento funciona como el **Gestor Documental de facto** del **Sistema Integrado de Gestión (SIG)** y de toda la operación técnica, comercial, humana y administrativa de la empresa.

Para diseñar e implementar una solución de software adecuada, es indispensable comprender la lógica de negocio, las normativas bajo las cuales fue estructurado el sistema documental, el sistema de codificación de archivos y las limitaciones críticas del modelo actual.

---

## 2. Perfil y Contexto de la Organización

### 2.1 Identidad de la Empresa
* **Razón Social:** Loard Construcciones S.A.S.
* **Sector / Industria:** Obras civiles, montajes mecánicos, mantenimiento de infraestructura de hidrocarburos, tuberías de transporte y tanques de almacenamiento de combustibles en Colombia.

### 2.2 Clientes Principales y Sector Económico
La empresa trabaja en un entorno de **alta criticidad técnica y seguridad industrial (Oil & Gas)**. Sus principales clientes documentados son:
* **Chevron Petroleum Company / Chevron:** Contratos marco, órdenes de trabajo de mantenimiento rutinario y proyectos mayores no rutinarios.
* **Primax Colombia S.A.:** Obras civiles e hidráulicas en terminales de combustibles, diques de contención, adecuación de plantas y líneas de recibo/despacho.
* Otros clientes industriales y contratistas especializados (ej. Urigo, interfaces técnicas Tie-In).

### 2.3 Cobertura Geográfica y Sedes Operativas
Las operaciones y registros documentales de la empresa se encuentran distribuidos a nivel nacional en 5 centros principales:
1. **Cartagena** (Base de operaciones costera, refinerías, terminales marítimas).
2. **Bogotá** (Sede administrativa / proyectos centro).
3. **Medellín** (Proyectos regionales y plantas de distribución).
4. **Yumbo** (Zona industrial y terminales del Valle del Cauca).
5. **Buenaventura** (Terminal marítima y de transferencia de combustibles).

---

## 3. Marco Normativo y Estándares (ISO, OHSAS y Técnicos)

### 3.1 Normas que Rigen la Estructura Documental

#### 1. ISO 9001:2015 — Calidad
* La estructura de control de la información está alineada con los requisitos de gestión por procesos y control de información documentada (evidenciado en el procedimiento `SG-PR05 v6 Procedimiento de información documentada`).
* Contempla auditorías internas periódicas (`SG-PR06`), control de producto/servicio no conforme (`SG-PR16`), oportunidades de mejora (`SG-PR013`) y revisiones de la dirección.

#### 2. OHSAS 18001 — Seguridad y Salud Ocupacional
* El componente de seguridad y salud en el trabajo fue estructurado originalmente y se mantiene bajo el estándar **OHSAS 18001**
* Se articula de manera directa con la legislación nacional colombiana: **SG-SST (Decreto 1072 de 2015)** y los requisitos de evaluación del **RUC** (Registro Único de Contratistas del Consejo Colombiano de Seguridad):
  * **Matriz IPER:** Identificación de Peligros, Evaluación y Control de Riesgos.
  * **Control de Tareas Críticas de Alto Riesgo:** Espacios confinados, trabajo en alturas, izajes mecánicos, trabajos en caliente (soldadura y corte) y riesgo eléctrico.
  * **Políticas Corporativas SSTA:** Actualizadas año a año (con versiones continuas desde 2019 hasta 2026):
    * `GG-PL01`: Política SSTA.
    * `GG-PL02`: Prevención del consumo de alcohol, tabaco y sustancias psicoactivas.
    * `GG-PL03`: Uso de Equipos de Protección Personal (EPP).
    * `GG-PL06`: Política de Desconexión Laboral (Ley 2191 de 2022).
    * `GG-PL07`: Prevención del Acoso Laboral, Sexual y Violencias en el Trabajo (Ley 1010 de 2006).

#### 3. ISO 14001:2015 — Medio Ambiente
* Integra la evaluación y control de impacto ambiental en frentes de obra (`3.1 Gestion del Riesgo\Matriz Ambiental`), planes de emergencia ante derrames en diques de almacenamiento y disposición de residuos peligrosos.

#### 4. Códigos y Estándares de Ingeniería de Campo
* **API 650 / API 653:** Ensayos de verticalidad, redondez, peaking y banding, y reparación de fondos en tanques de almacenamiento.
* **ASME Sección IX / AWS D1.1:** Procedimientos calificados de soldadura (WPS/PQR) y libros de control de juntas (*Weld Book* / `GT-FR64`).
* **SSPC / NACE:** Preparación de superficies (SSPC VIS 1) y ensayos de recubrimientos (adherencia, Holiday test y medición de espesores DFT).

---

## 4. Estructura y Taxonomía del Repositorio en Dropbox

El repositorio corporativo en Dropbox contiene más de **23.000 archivos** organizados bajo la siguiente jerarquía de procesos:

```
Dropbox/
├── 1. Gestión Gerencial/       --> Dirección estratégica, políticas, presupuestos y actas
├── 2. Sistema de Gestion/       --> SSTA (OHSAS 18001, ISO 9001/14001), matrices de riesgo, auditorías
├── 3. Gestión Comercial/        --> Cotizaciones (con/sin AIU), contratos (Chevron, Primax)
├── 4. Gestion Humana/           --> Contratación, nómina, planillas PILA, hojas de vida y bienestar
├── 5. Gestion Administrativa/   --> Compras, proveedores, logística y reportes por sedes
├── 6. Gestión Técnica/          --> Instructivos de obra, QA/QC, bitácoras, Weld Book y registros por ciudad
└── Espacio familiar/            --> Carpeta aislada de uso personal (acceso directo)
```

### 4.1 Estándar de Codificación de Documentos
Los documentos oficiales siguen una convención alfanumérica de nomenclatura estricta:

$$\text{[Prefijo Proceso]}-\text{[Tipo Documental]}\text{[Número]} \quad \text{v[Versión]} \quad \text{[Nombre Descriptivo]}.[\text{ext}]$$

#### Prefijos de Proceso:
* `GG`: Gestión Gerencial
* `SG`: Sistema de Gestión (Calidad / SSTA)
* `GC`: Gestión Comercial
* `GH`: Gestión Humana
* `GA`: Gestión Administrativa
* `GT`: Gestión Técnica

#### Tipos de Documento:
* `PL`: Política institucional
* `MN`: Manual corporativo (ej. `GG-MN01 v8 Manual SSTA`)
* `CR`: Caracterización del proceso (ej. `GT-CR01 v2 Caracterizacion Gestion Tecnica`)
* `PR`: Procedimiento documentado (ej. `SG-PR05 v6 Procedimiento de información documentada`)
* `IN`: Instructivo técnico de trabajo (ej. `GT-IN01 v1 Instructivo para el lavado de tanques`)
* `FR`: Formato estándar / plantilla en blanco (ej. `GT-FR48 v1 Informe Diario de Actividades`)
* `Registros`: Formatos diligenciados, reportes firmados y evidencias, organizados por año, proyecto o sede.

---

## 5. Inventario Detallado por Proceso

### 5.1 `Dropbox/1. Gestión Gerencial`
* **Objetivo:** Definir el direccionamiento estratégico, asignación presupuestal y gobierno legal de la organización.
* **Estructura interna:**
  * `1. Directrices organizacionales/`: Políticas de la empresa actualizadas periódicamente (carpetas históricas desde 2019 hasta 2026). Cada año se emite la versión actualizada en `.doc` y `.pdf` firmado.
  * `2. Objetivos y Metas/`: Cuadros de seguimiento a metas corporativas e indicadores gerenciales.
  * `3. Recursos/`: Presupuestos anuales asignados a operaciones y al sistema de gestión (`Presupuestos/` y `Registros/`).
  * `4. Reglamentos Loard/`: Reglamento Interno de Trabajo formal y Reglamento de Higiene y Seguridad Industrial.
  * `5. Requisitos legales y de otra indole/`: Matrices legales actualizadas frente a las exigencias del marco jurídico colombiano.
  * `6. Formatos/` y `7. Registros/`: Actas de junta y reuniones gerenciales (histórico 2017–2025) y actas de *Revisión por la Dirección*.

### 5.2 `Dropbox/2. Sistema de Gestion`
* **Objetivo:** Administrar el aseguramiento de calidad (ISO 9001), medio ambiente (ISO 14001) y seguridad ocupacional (OHSAS 18001 / SG-SST).
* **Estructura interna:**
  * `2. SSTA/1. Calidad/`:
    * Procedimientos de información documentada (`SG-PR05`), auditorías internas (`SG-PR06`), producto/servicio no conforme (`SG-PR16`) y oportunidades de mejora (`SG-PR013`).
    * Registros de auditorías internas, auditorías de clientes y entes externos, actas de aprobación y control de documentos externos.
  * `2. SSTA/3. Administración riesgo/`:
    * `3.1 Gestion del Riesgo`: Matriz IPER (Identificación de Peligros y Evaluación de Riesgos) y Matriz de Aspectos e Impactos Ambientales.
    * `3.2 Tratamiento del Riesgo`: Programas de gestión específicos:
      * `3.2.3`: Programas de riesgos prioritarios (alturas, confinados, izajes, soldadura).
      * `3.2.4`: Salud en el trabajo (exámenes ocupacionales y vigilancia epidemiológica).
      * `3.2.6`: Seguridad en el trabajo.
      * `3.2.7`: Planes de contingencia y emergencias.
      * `3.2.8`: Gestión ambiental.
      * `3.2.9`: Cronogramas de capacitación.
      * `3.2.11`: Mantenimientos de equipos y maquinaria.
  * `2. SSTA/4. Evaluación y Monitoreo/`:
    * Investigación y reporte de incidentes y accidentes de trabajo/ambientales (`4.1`).
    * Inspecciones periódicas de seguridad (`4.4`).
    * Tableros estadísticos mensuales de accidentalidad consolidados y por ciudad (Bogotá, Medellín, Cartagena, Yumbo, Buenaventura) (`4.6`).
  * `2. SSTA/Documentos Obsoletos/`: Repositorio histórico donde se custodian las versiones previas de formatos y documentos que han perdido vigencia.

### 5.3 `Dropbox/3. Gestión Comercial`
* **Objetivo:** Licitaciones, presupuestos comerciales, órdenes de compra y gestión contractual con clientes.
* **Estructura interna:**
  * `1. Procedimientos/` y `2. Formatos/`: Modelos de cotización formal (`GC-FR04 v1`) distinguiendo propuestas **CON AIU** (Administración, Imprevistos y Utilidades) y **SIN AIU**, además de certificados RUP (Registro Único de Proponentes).
  * `3. Resgistros/`: Historial de cotizaciones radicadas, actas de entrega, encuestas de satisfacción y órdenes de compra emitidas.
  * `Contratos chevron/`: Carpetas organizadas por frentes de trabajo y contratos con Chevron (proyectos identificados numéricamente: 3, 6, 7, 8, 11, 13, 14, 15, 20 y órdenes no rutinarias).
  * `Orden de compra Primax/`: Expedientes comerciales, órdenes de servicio y actas de proyectos para Primax Colombia (obras en tanques, placas de diques de combustible y adecuaciones de planta).
  * `DUBER CARTAGENA/`: Información operativa y comercial de contratos gestionados por personal clave en la regional Cartagena.

### 5.4 `Dropbox/4. Gestion Humana`
* **Objetivo:** Administración de nómina, contratación, bienestar laboral y cumplimiento de la seguridad social.
* **Estructura interna:**
  * `1. Procedimientos/`: Procedimiento de selección y contratación (`GH-PR08`), inducción para personal nuevo o de corta duración SSE (`GH-PR09`), y evaluación de funciones (`GH-PR01`).
  * `2. Formatos/`: Plantillas de entrevistas, actas de entrega de dotación y EPP, actas de descargos y liquidaciones de personal.
  * `3. Registros/`:
    * Hojas de vida del personal técnico y administrativo con soportes académicos y laborales.
    * Comprobantes de pago de Seguridad Social integral (planillas PILA mensuales).
    * Control de ausentismos e incapacidades médicas.
    * Organigramas de la empresa.
    * Perfiles sociodemográficos de los colaboradores.
    * Registros fotográficos de jornadas de bienestar y seguridad SSTA (carpetas anuales de 2021 a 2025).

### 5.5 `Dropbox/5. Gestion Administrativa`
* **Objetivo:** Abastecimiento, compras, control de proveedores y reportes de gestión por sedes.
* **Estructura interna:**
  * `1. Compras y control de proveedores/`: Procedimiento de compras y selección de contratistas (`GA-PR06 v6`), formatos de evaluación y reevaluación periódica de proveedores.
  * `2. Reportes/`: Informes administrativos y operativos clasificados por centro de trabajo:
    * `Bogota/`
    * `Cartagena/`
    * `Medellin/`
    * `Yumbo/`
    * `Bventura/` (Buenaventura)
    * Proyectos de ingeniería específicos como `Bottom Loading` (sistemas de llenado por fondo para carrotanques).
  * `3. Registros/`: Control y radicación de correspondencia oficial interna y externa.

### 5.6 `Dropbox/6. Gestión Técnica`
* **Objetivo:** Ejecución de obras, aseguramiento de calidad (QA/QC) y control de ingeniería en frentes de trabajo. Es el módulo de mayor volumen y criticidad.
* **Estructura interna:**
  * `1. Procedimientos/`: Procedimiento general de gestión técnica (`GT-PR01`) y custodia de la propiedad del cliente (`GT-PR02`).
  * `2. Instructivos/`: Catálogo exhaustivo de métodos de trabajo:
    * *Espacio confinado:* Lavado de tanques (`GT-IN01`), aislamiento y drenaje (`GT-IN02`), desgasificación con eductor (`GT-IN03`), reparación de fondos de tanques (`GT-IN04`).
    * *Tuberías:* Soldadura de líneas (`GT-IN06`), pruebas hidrostáticas (`GT-IN11`), montaje de líneas (`GT-IN13`), torque de bridas (`GT-IN26`), flushing (`GT-IN42`).
    * *Soldadura y Pailería:* Soldadura general (`GT-IN05`), inspección visual de soldadura (`GT-IN17`), pailería (`GT-IN36`), procedimientos formales WPS/PQR (`GT-PR-04`).
    * *Tratamiento de Superficies y Pintura:* Limpieza y aplicación de pintura (`GT-IN10`), bajo estándares SIKA y SSPC.
    * *Obras Civiles y Eléctricas:* Movimiento de tierras (`GT-IN20`), tubería conduit (`GT-IN21`), bancos de ductos (`GT-IN22`), puesta a tierra (`GT-IN23`), figurado de hierro (`GT-IN28`), mezclas de concreto (`GT-IN30`).
  * `3. Formatos/`:
    * `GT-FR48`: Informe Diario de Actividades (documento esencial de avance y soporte de facturación).
    * `GT-FR46`: Informe Semanal de Actividades.
    * `GT-FR47`: Acta de Liquidación Técnica de Obras.
    * `GT-FR64`: Libro de Tubería / *Weld Book* (trazabilidad de cada junta soldada, soldador, electrodo y ensayos).
    * `GT-FR25`: Protocolo de Prueba Hidrostática.
    * Batería de formatos de ensayos de pintura: Adherencia (`GT-FR52`), Holiday detector (`GT-FR53`), Curado silicato de zinc (`GT-FR54`), Espesores película seca DFT (`GT-FR56`), Contaminación de sales (`GT-FR57`/`58`), Comparador visual SSPC (`GT-FR60`).
    * Formatos de concreto: Ensayo de rotura de cilindros (`GT-FR62`).
  * `4. Registros/`: Evidencias de campo clasificadas por sedes (`1. Cartagena/`, `2. Bogotá/`, `3. Medellin/`, `4. Yumbo/`, `5. Buenaventura/`), Actas de Servicio firmadas por clientes, y matriz de Certificados de Competencias del personal (cursos de trabajo en alturas, espacios confinados, calificación de soldadores).


---

## 6. Diagnóstico Técnico: Limitaciones y Puntos de Dolor del Modelo Actual (Dropbox)

Para el equipo de desarrollo, la transición a una plataforma de software formal debe resolver los siguientes problemas inherentes al almacenamiento en carpetas compartidas:

| Dimensión | Situación Actual en Dropbox | Riesgo / Impacto Operativo |
| :--- | :--- | :--- |
| **Control de Concurrencia** | Generación recurrente de archivos duplicados por colisión de sincronización (ej. `GT-FR25 v1 Prueba hidrostática (Copia en conflicto de Edwin...)`). | Riesgo de pérdida de información de pruebas críticas y sobrescritura de reportes diarios. |
| **Control de Versiones** | Versionado manual en el nombre del archivo (`v1`, `v2`, `v6`). El archivo de versiones anteriores depende de trasladar manualmente los archivos a la carpeta `Documentos Obsoletos`. | Uso inadvertido de formatos obsoletos por personal en campo, generando no conformidades en auditorías. |
| **Metadatos y Consultas** | Estructura basada estrictamente en carpetas anidadas del sistema de archivos. No existen etiquetas dinámicas ni atributos relacionales. | Imposibilidad de generar búsquedas cruzadas (ej. consultar todos los reportes de "Chevron" en "Cartagena" del "2023" sin recorrer decenas de carpetas). |
| **Seguridad y Permisos (RBAC)** | Permisos a nivel general de carpeta en Dropbox. Quien tiene acceso puede alterar, mover o eliminar inadvertidamente archivos críticos. | Exposición de información confidencial (salarios, historias de salud ocupacional en Gestión Humana, márgenes y tarifas en Gestión Comercial). |
| **Flujos de Aprobación y Firmas** | Firmas manuales o escaneadas en PDFs. Las actas y autorizaciones requieren impresión física, firma manuscrita y posterior escaneo. | Ineficiencia en tiempos de respuesta; ausencia de firma digital con validez probatoria y estampado cronológico. |
| **Trazabilidad y Auditoría (Audit Trail)** | Dropbox no ofrece un registro inmutable a nivel de datos sobre quién consultó, modificó o descargó documentos específicos. | Dificultad para sustentar trazabilidad formal en auditorías de clientes petroleros. |
