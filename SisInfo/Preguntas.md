# Cuestionario de Validación y Aclaración de Requerimientos: LOARD Construcciones S.A.S.

El presente documento consolida las dudas, vacíos de información, supuestos operativos y decisiones críticas identificadas a partir del diagnóstico y la especificación inicial del **Hito 1 (Sistemas de Información)**. Su propósito es servir como guía de entrevista y mesa de trabajo con la Gerencia General, la Dirección Operativa, la Coordinación de Calidad/SIG y los Responsables de SST de **Loard Construcciones S.A.S.**

---

## 1. Alcance del Sistema y Fronteras del Proyecto

### 1.1. Inclusión formal de la Gestión Documental del SIG y el Módulo de SST
* **La cuestión:**  
  En el documento de Hito 1 (Secciones 1.3, 1.6.9, 1.7.2 y 4.1), el foco inicial acordado con la empresa era la **gestión operativa de campo/taller** y la **gestión comercial/gerencial**. Sin embargo, durante el análisis de la cadena de valor y el diagnóstico de Dropbox emergió que la gestión documental del SIG (ISO 9001:2015, control de versiones, auditoría) y el control de SST (Decreto 1072, cursos de alturas/espacios confinados, exámenes médicos) representan riesgos legales y de auditoría inminentes (clasificados como necesidades MUST: NEC-12 a NEC-19). El documento señala explícitamente que su inclusión definitiva en el sistema tiene el carácter de *«ampliación pendiente de confirmar con la empresa»*.
* **Por qué surge:**  
  Incorporar estos dos dominios incrementó el backlog en 15 requerimientos funcionales (RF-35 a RF-49) y 10 historias de usuario (HU-19 a HU-23, HU-34 a HU-37), de las cuales la mayoría son de prioridad alta (*MUST*).
* **Impacto si no se aclara:**  
  Si la empresa no aprueba esta ampliación, se estaría diseñando e invirtiendo esfuerzo de desarrollo en funcionalidades fuera de contrato o expectativa; por el contrario, si se excluyen pero el cliente sigue dependiendo de Dropbox para auditorías del RUC y Chevron, persistirán las multas o no conformidades que amenazan la facturación.
* **Preguntas para LOARD:**
  1. ¿Aprueba la Gerencia que el sistema incluya formalmente los módulos de **Gestión Documental del SIG** y **Control de SST/Talento Humano**, o deben considerarse fases posteriores?
  Rta: en principio si serequiere el sig, el sst y talento si se necesita. 

  2. En caso de priorizar, ¿se prefiere un despliegue por fases (Fase 1: Operaciones y Dossier; Fase 2: SIG y SST)?
  Rta: Sig y SST por que es una configuracion mas robusta se necesita primero

---

### 1.2. Frontera con el Área Financiera y Contable
* **La cuestión:**  
  El documento excluye explícitamente del alcance al área financiera, la contabilidad general, la facturación electrónica, el pago a proveedores y la nómina (Sección 1.3.1 Tabla 5, Sección 1.7.2 y WON'T de MoSCoW). Sin embargo, el sistema contempla el registro de costos directos de obra, tarifas de insumos/horas, requisiciones de compra y seguimiento al avance financiero (NEC-09, RF-30, HU-30).
* **Por qué surge:**  
  Existe una línea delgada entre el costeo operativo de proyectos y la contabilidad corporativa. En empresas de ingeniería, si el ERP de obra no dialoga con el software contable (ej. Siigo, World Office, SAP, Excel contable), se produce una duplicación de digitación de facturas, compras y consumos.
* **Impacto si no se aclara:**  
  Riesgo de reprocesos dobles entre los residentes/almacenistas y los contadores en Bogotá, o desajustes entre lo que la gerencia ve en el tablero operativo vs. los balances financieros oficiales.
* **Preguntas para LOARD:**
  1. ¿Qué sistema o software contable utiliza actualmente la empresa para registrar gastos, facturación y compras?
  Rta: La parte financiera revisa las partes escencials, que personas, cuanto material, no importa como este esta info, solo entregarla de manera organizada
  2. ¿Basta con que el nuevo sistema permita exportar reportes de costos en formato Excel/CSV estructurado, o se requerirá a mediano plazo una interfaz de integración (API/exportador automático) con dicho sistema contable (RNF-26)?
  Rta: La entrega actualmente se hace con un formato, no es necesario mantener un formato exacto, lo que importa es entregar la informacion, 

---

### 1.3. Nivel de Acceso y Participación de Clientes Petroleros e Interventorías
* **La cuestión:**  
  El Customer Journey Map incluye como actor al «Cliente Petrolero» (Chevron, Primax) que revisa informes de avance, aprueba actas de obra y recibe el dossier de calidad (Sección 1.4.2). En los procesos As-Is y To-Be (BPMN), se modela la radicación de actas y entrega documental.
* **Por qué surge:**  
  No está definido si el cliente/interventor accederá con un usuario restringido a la plataforma para aprobar actas y consultar el dossier en línea, o si la interacción continuará siendo externa (descarga de expedientes PDF foliados para radicación por ventanilla/correo/plataforma propia del cliente).
* **Impacto si no se aclara:**  
  Afecta el diseño de la arquitectura de seguridad, licenciamiento, concurrencia y cumplimiento de políticas de ciberseguridad corporativas exigidas por multinacionales como Chevron.
* **Preguntas para LOARD:**
  1. ¿Las interventorías de Chevron o Primax aceptarían ingresar a un portal web de Loard para revisar y visar documentos, o por exigencia contractual obligan a radicar expedientes en sus propias plataformas (ej. Ariba, correos formales o carpetas compartidas)?
  Rta: la comunicacion con los clientes es por correo actualmente, no se necesita que chevron vea nada, chevron pide la informacion y el supervisor se la envia

  2. ¿El alcance del sistema debe contemplar un rol de usuario «Interventor Externo» con permisos de solo lectura?


---

## 2. Operación en Campo, Conectividad y Condiciones Técnicas

### 2.1. Conectividad Real en Frentes Críticos y Modo Offline
* **La cuestión:**  
  Se asume la necesidad de funcionalidad fuera de línea (*offline*) con sincronización posterior (RF-05, RNF-07, HU-03) debido a frentes de trabajo remotos como Buenaventura o zonas de almacenamiento de hidrocarburos con señal celular débil o restringida. Además, el documento identifica un error de numeración donde se referencia una inexistente «NEC-20» en RF-05 y RNF-07.
* **Por qué surge:**  
  En plantas de hidrocarburos rigen normas intrínsecas de seguridad (zonas ATEX/clasificadas) donde el uso de teléfonos puede estar prohibido o limitado a cuartos de control. Además, la cobertura en ciertas zonas del puerto o tanques de combustible puede ser nula.
* **Impacto si no se aclara:**  
  Construir un soporte *offline-first* con resolución de colisiones y base de datos local en el navegador/móvil eleva considerablemente la complejidad del desarrollo frente a una aplicación web estándar. Si los frentes cuentan con Wi-Fi en campamento o buena cobertura 4G/5G, el requerimiento podría sobredimensionarse.
* **Preguntas para LOARD:**
  1. ¿Cómo es exactamente la conectividad a Internet en cada uno de los frentes actuales (Bogotá, Cartagena, Medellín, Yumbo y Buenaventura)?
  Rta: Todos los supervisores tienen plan de datos asignados, solo hay problema de internet en beunaventura
  2. ¿Existen restricciones de seguridad industrial (SST/ATEX) en los frentes de Chevron que impidan llevar dispositivos móviles al área de tuberías/tanques, obligando a diligenciar los datos al final de la jornada en oficina de campo?
  Rta: se tiene un computador oficina en cada lugar donde se hacen los informes, si hay restricciones de llevar celulares a zonas especificas, no se tienen celulares especiales para zonas prohibidas
  3. En caso de operar sin conexión, ¿cuál es el tiempo máximo razonable que un supervisor permanece sin señal antes de sincronizar (horas, un turno de trabajo, días)?
  Rta: 6 horas, es raro

---

### 2.2. Dispositivos de Trabajo y Modelo de Adopción (BYOD vs. Corporativos)
* **La cuestión:**  
  Los requerimientos RF-01, RNF-22, RNF-23 y HU-01 definen que los operarios y supervisores registrarán el informe diario desde dispositivos móviles vía navegador web o PWA.
* **Por qué surge:**  
  Se señala que existe arraigo en el uso de papel/WhatsApp y una «baja resiliencia digital» en personal técnico como soldadores o tuberos (Perspectiva BSC 4).
* **Impacto si no se aclara:**  
  Si se pretende que los obreros utilicen sus teléfonos personales (BYOD), surgen problemas de compatibilidad (gamas bajas, almacenamiento lleno), resistencia sindical/laboral o riesgos de seguridad de la información. Si la empresa suministra equipos, debe presupuestarse la dotación.
* **Preguntas para LOARD:**
  1. ¿Quién realiza materialmente el reporte diario de cuadrilla? ¿El operario/líder de cuadrilla o el ingeniero residente/supervisor de obra?
  Rta: Los supervisores, generalmente los residentes de cada facilidad
  2. ¿La empresa suministra smartphones o tablets corporativas a los frentes de obra, o el personal utiliza sus celulares personales?
  Rta: Actualmente no, en el futuro si
  3. ¿Qué sistema operativo predomina (Android vs. iOS) y qué capacidades mínimas tienen dichos dispositivos?
  Rta: EN LOS CELULARES SOLO SE NECESITARIAN COSAS DE SST, INSPECCIONES DE EQUIPOS, EL RESTO EN EL PC, puro android, en cartagena hay un supervisor de apple , pc solo windows

---

## 3. Dinámica de Procesos Operativos (BPMN As-Is / To-Be)

### 3.1. Flujo de Revisión, Aprobación y Rechazo de Reportes de Campo
* **La cuestión:**  
  En el BPMN To-Be (Figura 5, pág. 44) y la HU-04, se establece una compuerta de decisión: el ingeniero residente revisa el reporte diario y, si lo aprueba, el sistema actualiza automáticamente inventarios, avances y tableros; si lo rechaza, regresa a la cuadrilla.
* **Por qué surge:**  
  En la pág. 38 y 40 se advierte que: *«El orden detallado de las revisiones, las devoluciones por información incompleta (...) son supuestos de modelado que deben confirmar los responsables del proceso. No se ha realizado observación directa ni medición de tiempos»*.
* **Impacto si no se aclara:**  
  Un cuello de botella humano en la aprobación del residente podría paralizar la visibilidad de los costos en el tablero gerencial y desactualizar el saldo de inventarios en tiempo real.
* **Preguntas para LOARD:**
  1. ¿Con qué frecuencia revisa hoy el residente los reportes de avance y qué motivos comunes provocan devoluciones o correcciones?
  Rta: los avances dependen, si es una obra o proyecto semanalmente, si es de marco, por corte de obra mensual. Los informes son muy puntuales, no hay muchos errores
  2. Si un reporte diario no es revisado en 24 o 48 horas, ¿debe el sistema bloquear registros posteriores, generar una alerta a la Gerencia o permitir un avance provisional?
  Rta: No con los diarios, son semanales o mensuales, el que revisa suele ser director de proyectos, no hay problema en demora, el director de proyectos siempre se entera por voz de los avances. y eso es lo importante.
  Seria deseable que suban el informe y revisar en lugar de enterarse por voz

---

### 3.2. Reglas de Negocio para el Ciclo de Compras y Requisiciones
* **La cuestión:**  
  El requerimiento RF-27 y la historia HU-27 definen: *«El sistema debe enrutar cada requisición por un flujo de aprobación según el monto»*, pero no se especifican los umbrales de dinero ni los cargos aprobadores.
* **Por qué surge:**  
  Las compras urgentes en frentes aislados (como Buenaventura) generan sobreprecios severos por falta de flujo formal de compras (NEC-08, Tabla 4).
* **Impacto si no se aclara:**  
  No es posible codificar las reglas del motor de compras sin conocer los niveles de autoridad financiera.
* **Preguntas para LOARD:**
  1. ¿Cuáles son los montos límites para las compras directas en frente de obra vs. compras que requieren cotización triple o autorización de Gerencia? (Ejemplo: ¿Menos de \$1.000.000 COP aprueba Residente; hasta \$10.000.000 COP Director de Obra; más de \$10.000.000 COP Gerencia General?).
  Rta: el residente puede 250k directo y despues pide pagos por administracion, solo hay directores de obra cuando hay proyectos grandes. Lo que se hace es darles caja menor de 3 a 5millones, y si se pasan, pasan el reporte y se les da mas plata de caja menor, si hacen compra superior a 250k piden autorizacion a bogota
  2. ¿Quiénes son los roles habilitados para emitir órdenes de compra y autorizar despachos?
  Rta: El residente siempre  pide la cotizacion y la orden de compra la hace la auxiliar administrativa y el pago lo hace la gerencia
---

### 3.3. Logística de Almacén, Consumibles y Desperdicios
* **La cuestión:**  
  Los requerimientos RF-08 a RF-11 y HU-11 a HU-13 establecen el control de consumibles críticos (electrodos, discos de corte, gases) por frente de obra para evitar el problema histórico de que *«falta dinero al cierre del proyecto»*.
* **Por qué surge:**  
  En obras de tubería e infraestructura metálica existe un desperdicio natural (puntas de electrodo quemadas, cilindros de gas con presión residual, mermas de láminas).
* **Impacto si no se aclara:**  
  Si el sistema asume un consumo teórico 1:1 sin contemplar un factor de merma o desecho estándar en los APU, el sistema alertará falsos sobrecostos o desabastecimientos irreales.
* **Preguntas para LOARD:**
  1. ¿Existe físicamente un almacenista en cada frente de obra, o el mismo residente o supervisor gestiona la entrega de insumos?
  Rta: Por ejemplo en cartagena se compraron varillas, eso lo maneja el residente directamente, no es necesario almacenista
  2. ¿Cómo se controla hoy la entrega de electrodos y consumibles especiales (se exige la devolución de colillas/discos gastados para entregar nuevos)?
  Rta: Generalmente cada facilidad pide y se le envia desde bogota, no hay retorno
  3. ¿Cuál es el margen de desperdicio técnico o merma aceptable contemplado en los presupuestos de soldadura y tubería?
  Rta: Generalmente 5% pero depende de los materiales

---

## 4. Dossier de Calidad, Ensayos No Destructivos (END) y Firmas

### 4.1. Recepción y Homologación de Ensayos No Destructivos (Terceros)
* **La cuestión:**  
  El cuello de botella crítico CB-05 (pág. 40) y las necesidades NEC-05 / RF-15 / HU-15 señalan que los laboratorios terceros entregan reportes de ensayos (radiografías industriales, líquidos penetrantes, ultrasonido, pruebas hidrostáticas, probetas de concreto) que hoy se transcriben manualmente a Excel.
* **Por qué surge:**  
  Cada laboratorio de ensayos no destructivos (END) emite formatos propios en PDF escaneado o físico.
* **Impacto si no se aclara:**  
  Si los laboratorios externos no estandarizan un formato de entrega o no se define qué datos clave deben indexarse, la consolidación del Weld Book y Dossier seguirá exigiendo un esfuerzo manual intensivo.
* **Preguntas para LOARD:**
  1. ¿Quiénes son los principales subcontratistas de END que trabajan con Loard y en qué formato entregan sus informes finales?
  Rta: en medellin hay una empresa llamada y en cartagena otra en buenavrentura y jumbo hay una empresa de bogota que ayuda con ultrasonido o tinbtas, generalmenrwe mandan pdf
  2. ¿El personal de Loard transcribirá únicamente el número de certificado, junta, fecha y veredicto (Aceptado/Rechazado) adjuntando el PDF del tercero, o se espera que el sistema capture parámetros técnicos detallados del ensayo?
  Rta: Si es un proyecto hay qwue pasar una cartilla de soldadura, en el plano se pone la soldadura, se enumera, se pone la marca del soldador y cuales se probaron. Se almacena el pdf. Seria super bueno extraer info por que facilita el trabajo

---

### 4.2. Estandarización del Libro de Tubería (*Weld Book*) y Estructura del Dossier
* **La cuestión:**  
  RF-16 y HU-16 contemplan la gestión del formato GT-FR64 (*Weld Book*), vinculando junta, soldador (estampa), electrodo/colada y ensayos aplicados. Además, RF-18 y HU-18 buscan verificar que el dossier contenga los entregables obligatorios antes de exportar.
* **Por qué surge:**  
  Clientes de alta exigencia (como Chevron) suelen imponer tablas de trazabilidad y manuales de entrega documental particulares que pueden diferir de otros clientes (ej. Primax o consorcios de infraestructura).
* **Impacto si no se aclara:**  
  Desarrollar una estructura rígida de Dossier podría ser rechazada en contratos específicos si el cliente exige un orden foliado o plantillas propietarias.
* **Preguntas para LOARD:**
  1. ¿El formato GT-FR64 del *Weld Book* es un estándar universal de Loard aceptado por todos los clientes, o Chevron impone un formato o estructura de carpetas diferente?
  Rta Si, se basa en la api 1104
  2. ¿Cuáles son los entregables contractuales mínimos y universales que deben conformar un Dossier de Calidad completo para habilitar la radicación de un acta?
  Rta: Documentos contractuales, orden de servicio el contrato, polizas, todo lo contractual, actas de corte (cada cobro que se hace), planos (si hay mecanicos, si hay electricos), certificados de conformidad, informes semanales e informe final (creados por el residente), memorias de calculo, los planos certificados de conformidad, los planos de diseño y los planos as built por ejemplo en "C:\Users\Computador\Dropbox\6. Gestión Técnica\4. Registros\2. Bogotá\DOSSIER TANQUE 108749\1. INFORMACIÓN ADMINISTRATIVA" esta todo lo contractual

---

### 4.3. Validez Legal del Mecanismo de Firma (Ley 527 de 1999)
* **La cuestión:**  
  Los requerimientos RF-42, RNF-19 y HU-22 exigen: *«Aprobar y firmar digitalmente actas y autorizaciones con validez probatoria y sello de tiempo conforme a la Ley 527 de 1999, erradicando la firma manuscrita pegada como imagen»*.
* **Por qué surge:**  
  La Ley 527 de 1999 y el Decreto 2364 de 2012 en Colombia distinguen entre **Firma Electrónica** (código OTP, contraseña, firma biométrica) y **Firma Digital** (emitida por una Entidad de Certificación Acreditada por ONAC, como Certicámara o GSE, con sello cronológico y costo recurrente por firma).
* **Impacto si no se aclara:**  
  Implementar una firma digital abierta con entidad certificadora implica costos de transacción recurrentes y trámites de tokens criptográficos para los directivos y residentes. Si el cliente petrolero solo exige firma electrónica avanzada auditable (con hafsh de integridad, usuario, IP y estampa de tiempo UTC), el costo y la fricción disminuyen radicalmente.
* **Preguntas para LOARD:**
  1. ¿Qué nivel de firma exige contractualmente Chevron para las actas de obra (GT-FR47) y el dossier: certificado digital emitido por entidad acreditada (Certicámara) o una firma electrónica interna trazable con evidencia de auditoría?
  Rta: ACTUALMENTE SE USAN FOTOS, Y FUNCIONA
  2. ¿Quiénes dentro de la empresa están facultados legalmente para firmar las actas de corte de obra y los dossieres de calidad?
  Rta: gerenta y repre legal

---

## 5. Gestión Comercial, APU y Márgenes

### 5.1. Reglas del Catálogo Único de APU y Modificaciones en Obra
* **La cuestión:**  
  Los requerimientos RF-19 a RF-25 y HU-24 a HU-26 buscan centralizar el catálogo de Análisis de Precios Unitarios (APU) para evitar que cada residente elabore ofertas en plantillas dispersas de Excel.
* **Por qué surge:**  
  En contratos marco de hidrocarburos suelen existir tarifas fijadas previamente por ítem (contratos a precios unitarios fijos), mientras que en otros proyectos se cotiza bajo la modalidad de obra civil tradicional con AIU (Administración, Imprevistos y Utilidad) o contratos de administración delegada.
* **Impacto si no se aclara:**  
  Un modelo de APU que no distinga entre proyectos con lista de precios marco y proyectos licitados a todo costo no servirá al área comercial para estructurar sus propuestas en el formato GC-FR04.
* **Preguntas para LOARD:**
  1. ¿Cómo se estructuran habitualmente los contratos con Chevron: listas de precios unitarios fijos pactados contractualmente, o se cotiza cada orden de trabajo con un APU individualizado?
  2. ¿Quién tiene la potestad de autorizar cambios en las tarifas unitarias estándar de mano de obra y equipos en el catálogo general?

---

### 5.2. Determinación y Desglose del Margen de Imprevistos (7% - 10%)
* **La cuestión:**  
  En las Secciones 1.1.3, 1.3 (NEC-10) y 1.7.1 se destaca que la empresa compite con un margen límite de rentabilidad no negociable y aplica un margen de imprevistos empírico de entre el 7% y el 10% en sus cotizaciones.
* **Por qué surge:**  
  La empresa carece de estadísticas históricas que demuestren si ese 7-10% es suficiente, excesivo (perdiendo licitaciones frente a rivales) o insuficiente (asumiendo sobrecostos imprevistos en campo).
* **Impacto si no se aclara:**  
  El cálculo de desviaciones del tablero gerencial (RF-31, HU-31) necesita una fórmula consensuada para comparar lo cotizado contra lo ejecutado.
* **Preguntas para LOARD:**
  1. ¿Cuáles son los rubros que históricamente consumen ese 7% a 10% de imprevistos (fletes imprevistos, compras urgentes de consumibles, jornadas extra por mal tiempo, reprocesos en soldadura)?
  2. ¿Qué margen mínimo de rentabilidad bruta o neta considera la gerencia como umbral de alarma crítica para un proyecto?

---

## 6. Talento Humano, SST y Privacidad de Datos Médicos (Ley 1581)

### 6.1. Tratamiento y Confidencialidad de Exámenes Médicos de Ingreso/Periódicos
* **La cuestión:**  
  El requerimiento RF-47 y la HU-36 definen que el sistema debe controlar la vigencia de los exámenes médicos ocupacionales de los trabajadores, advirtiendo explícitamente: *«No debe mostrar el contenido clínico a roles no autorizados»* para cumplir con la Ley 1581 de 2012 (Datos Sensibles de Salud) y la Resolución 2346 de 2007.
* **Por qué surge:**  
  El personal de operaciones de campo necesita saber si un soldador o tubero es *«APTO para trabajo en alturas/espacios confinados»*, pero bajo ninguna circunstancia puede tener acceso al diagnóstico clínico, paraclínicos o historia médica del colaborador.
* **Impacto si no se aclara:**  
  Incurrir en una violación de la Ley de Protección de Datos Personales (habeas data) acarrearía sanciones graves de la Superintendencia de Industria y Comercio (SIC).
* **Preguntas para LOARD:**
  1. ¿Quién administra y custodia hoy las carpetas de salud ocupacional de los colaboradores?
  2. ¿Se confirma que los residentes e ingenieros solo podrán visualizar un indicador booleano de aptitud (Apto / No Apto / Con restricciones) y la fecha de vigencia del concepto médico, sin acceso al archivo clínico?

---

### 6.2. Reglas de Advertencia vs. Bloqueo en Asignación de Tareas Críticas
* **La cuestión:**  
  El requerimiento RF-48 y la HU-09 indican que el sistema debe emitir una *advertencia* cuando se asigna una tarea crítica (alturas, espacios confinados, soldadura estructural) a una persona con certificado o examen médico vencido.
* **Por qué surge:**  
  En el sector de hidrocarburos, permitir que un trabajador ejecute labores de alto riesgo sin certificación vigente (Res. 4272/2021 de alturas, Res. 0491/2020 de confinados) conlleva suspensión inmediata del contrato por parte del cliente y responsabilidades penales en caso de accidente.
* **Impacto si no se aclara:**  
  Existe una gran diferencia funcional entre emitir una simple «alerta visual» (que el usuario puede ignorar) o ejecutar un «bloqueo duro» del sistema que impida guardar la cuadrilla si no cumple los requisitos de SST.
* **Preguntas para LOARD:**
  1. ¿La asignación de una persona no habilitada debe generar únicamente una advertencia registrable en auditoría o debe **bloquear de forma estricta** la inclusión de esa persona en el informe diario?
  2. ¿Con cuántos días de anticipación requiere SST recibir las alertas de vencimiento para programar recertificaciones o exámenes médicos (los 30 días propuestos son suficientes)?

---

## 7. Migración de Datos y Transición desde Dropbox

### 7.1. Criterios de Selección, Limpieza y Alcance de los 23.000 Archivos
* **La cuestión:**  
  El requerimiento RNF-25 fija como criterio de verificación que: *«Los más de 23.000 archivos migran con su código, versión y estructura. El conteo y la suma de verificación coinciden en un 100%»*. No obstante, el diagnóstico describe múltiples archivos duplicados, carpetas de «Documentos Obsoletos», versiones en conflicto (ej. formato GT-FR25) y nomenclaturas inconsistentes.
* **Por qué surge:**  
  Migrar a una base de datos relacional y a un gestor documental estructurado 23.000 archivos "tal como están" transferirá el desorden actual a la nueva plataforma (el principio clásico de ingeniería: *«garbage in, garbage out»*).
* **Impacto si no se aclara:**  
  El esfuerzo técnico y el costo de almacenamiento para migrar archivos obsoletos, borradores o archivos temporales inflará los tiempos y los costos del proyecto innecesariamente.
* **Preguntas para LOARD:**
  1. ¿Es indispensable migrar la totalidad de los 23.000 archivos históricos existentes en Dropbox, o se debe fijar una ventana de corte (por ejemplo: migrar únicamente formatos vigentes del SIG y proyectos activos de los últimos 2 a 3 años)?
  2. ¿Quién en Loard (probablemente la Coordinación del SIG) se encargará de realizar la depuración, validación y depuración de documentos obsoletos previa a la carga masiva?

---

## 8. Métricas de Línea Base y Metas del Balanced Scorecard

### 8.1. Cuantificación de la Línea Base Actual (Estado As-Is)
* **La cuestión:**  
  Tanto en el Balanced Scorecard (Pág. 32-34) como en el Discovery OST (Pág. 34-36) se plantean metas porcentuales ambiciosas:
  - Reducir $\ge 20\%$ el tiempo de ciclo para la entrega del Dossier de Calidad y Weld Book.
  - Capturar digitalmente el $\ge 80\%$ (o $\ge 95\%$) de los informes el mismo día.
  - Reducir el ciclo de aprobación de actas de 5 días a $<24$ horas.
  - Mantener la desviación del costo real vs. APU por debajo del 5%.
  Sin embargo, la Sección 1.6.9 y la Sección 3.1 reconocen explícitamente que **no se cuenta con una línea base medida ni con tiempos cronometrados reales**.
* **Por qué surge:**  
  No es posible comprobar una reducción del 20% o del 50% si no se conoce cuántas horas exactas toma hoy en día armar un dossier o cuántos días se tarda un acta en ser firmada.
* **Impacto si no se aclara:**  
  Los criterios de aceptación de éxito del proyecto no podrán medirse de forma objetiva ante la Gerencia al finalizar la implementación.
* **Preguntas para LOARD:**
  1. En promedio, ¿cuántas horas/hombre o días de trabajo le toma actualmente al equipo de calidad consolidar un Dossier de Calidad para un corte de obra típico?
  2. ¿Cuántos días transcurren actualmente desde que finaliza el período del corte hasta que las actas y soportes son radicados formalmente ante el cliente?
  3. ¿Cuántos reportes de avance físico se reciben hoy oportunamente el mismo día en que se realizan las actividades?

---

## 9. Gobernanza, Priorización y Adopción del Cambio

### 9.1. Validación de la Priorización MoSCoW del Backlog
* **La cuestión:**  
  El catálogo de especificación técnica reúne 37 historias de usuario (HU-01 a HU-37), de las cuales **22 han sido categorizadas preliminarmente como MUST (60%)**, 14 como SHOULD y 1 como COULD. La metodología ágil recomienda que las historias *MUST* no excedan el 60% de la capacidad disponible para garantizar contingencia ante desvíos.
* **Por qué surge:**  
  Los requerimientos de control documental estricto (bloqueo por *check-in / check-out*, metadatos obligatorios, inmutabilidad de logs) fueron clasificados como MUST por los analistas para garantizar la norma ISO 9001, aunque en el catálogo de necesidades original NEC-13 y NEC-14 eran identificadas como SHOULD (Sección 4.1.2).
* **Impacto si no se aclara:**  
  Si el alcance *MUST* es demasiado rígido, el primer ciclo de desarrollo (MVP / Piloto) corre el riesgo de retrasarse o no cumplir las expectativas de entrega temprana.
* **Preguntas para LOARD:**
  1. ¿Coincide la Gerencia con el orden inicial de prioridades propuesto (iniciar con el núcleo de seguridad/documental, captura de campo y dossier)?
  2. ¿Cuáles son las 3 funcionalidades más urgentes e inaplazables cuya ausencia hoy le cuesta más dinero o genera más dolores de cabeza a la compañía?

---

### Resumen de Próximos Pasos Recomendados
Una vez concertadas estas preguntas en sesión de trabajo con los líderes de proceso de **Loard Construcciones S.A.S.**, se procederá a:
1. Ajustar el alcance formal del sistema y congelar la especificación técnica de requerimientos.
2. Definir los parámetros de prueba para las alternativas del *Opportunity Solution Tree* (OST).
3. Establecer las líneas base cuantitativas de los KPI del *Balanced Scorecard*.
4. Formalizar el plan de migración y depuración del repositorio documental.




1.	En los contratos principales que manejan (como con Chevron), ¿las tarifas y precios ya están fijos y pactados de antemano en una lista maestra para todo el contrato, o para cada orden de trabajo les toca armar y cotizar un nuevo Análisis de Precios Unitarios (APU) desde cero?
a.	En el marco los precios están establecidos de TODO lo que se hace, si no existen se hace el unitario, Fuera del marco si se hace
2.	¿Quién dentro de la empresa tiene la autorización final para modificar o actualizar los precios oficiales de mano de obra, materiales y alquiler de equipos que se usan de base para hacer las cotizaciones?
a.	Se tiene la plantilla marco de cotización, lo que hacen los residentes es adaptarlo a lo que necesitan, se lo pasan a Yonny y el lo revisa
3.	En las cotizaciones se suele incluir entre un 7% y un 10% para imprevistos; según la experiencia de obras pasadas, ¿cuáles son los sobrecostos que con mayor frecuencia se comen ese porcentaje (por ejemplo: fletes urgentes a lugares apartados, materiales comprados a última hora, turnos extra por lluvias, o arreglos y reprocesos en soldadura)?
a.	Cambios de precios(1%), perdidas de tiempo por lluvia, tiempo en permisos, tiempo perdido en obra y caulquer cosa que no se haya listado en el unitario
4.	¿A partir de qué porcentaje de sobrecosto o pérdida en una obra considera la Gerencia que el sistema debería disparar una alarma urgente indicando que la rentabilidad del proyecto está en riesgo crítico?
a.	La alerta se necesita cuando se empiezan a demorar mas, si se planea para 40 dias, si a los 20 dias no se tienen el 50% entonces se necesita la alerta. Nuestro rubro es la mano de obra. En las cotizaciones siempre se tiene un item, una descripción y una cantidad, siempre es fácil medir el avance en base a esa cantidad de la cotizacion
5.	En el día a día, ¿quién es la persona responsable de recibir, custodiar y llevar el control de las carpetas de salud ocupacional, exámenes médicos de ingreso y periódicos de los trabajadores?
a.	Por legislación solo puede ser el encargado (los coordinadores de gestion, las carpetas Olga
6.	Para proteger la privacidad médica de los trabajadores según la ley, ¿están de acuerdo en que los ingenieros residentes y supervisores en campo solo puedan ver en pantalla si el trabajador está "Apto" o "No Apto" y la fecha de vencimiento de su certificado, sin tener acceso a los diagnósticos o documentos clínicos detallados?
a.	Eso es lo regulado, lo único que conoce el residente y empresas solo ven aptos. Lo mismo para espacios confinados y alturas. El medico le manda a Edward. El único que conoce la info es el trabajador y el coordinador de gestion
7.	Si un trabajador tiene vencido su curso de alturas, espacios confinados o su examen médico laboral, ¿el sistema debe bloquear completamente que el supervisor lo asigne a esa labor en la obra, o prefieren que solo muestre una advertencia en pantalla permitiendo asignarlo bajo la responsabilidad registrada de quien lo autorice?
a.	Si el curso esta vencido, NO puede ejecutar nada
8.	¿Con cuántos días de anticipación necesita el área de SST recibir las alertas automáticas antes de que se venza un curso o examen médico de un trabajador para alcanzar a programar la renovación a tiempo (por ejemplo: 30 días, 15 días o 45 días)?
a.	Alerta media en 1 mes y alta en 15 dias
9.	En Dropbox actualmente tienen más de 23.000 archivos (muchos de ellos duplicados, borradores o proyectos antiguos ya cerrados); ¿es indispensable o que tan urgente es pasar todos esos archivos al nuevo sistema, o consideran mejor trasladar únicamente los formatos vigentes de calidad y los proyectos activos de los últimos 2 o 3 años, dejando el resto como histórico de consulta en Dropbox?
a.	Ultimos 3 años en principio, depende, hay cosas que no cambian como los procedimientos de soldadura. Hay algunos documentos super viejos que se necesitan
10.	¿Quién dentro de Loard (por ejemplo, la Coordinación de Calidad/SIG) se encargará de revisar y seleccionar cuáles son los formatos y documentos oficiales vigentes antes de cargarlos a la nueva plataforma para no transferir versiones viejas o duplicadas?
a.	Tocaria revisar documento por documento. :(
11.	En promedio, ¿cuántos días o cuántas horas de trabajo le toma hoy al equipo de calidad reunir todos los soportes, certificados de ensayos y soldaduras para armar y tener listo el Dossier de Calidad de un corte de obra?
a.	El dossier es al final de la obra, por contrato se tienen 10 dias, se arman a medida que se va trabajando y se van agregando los certificados. DEPENDE DE LA OBRA LAS HORAS DE TRABAJO
12.	Una vez finalizan los trabajos de un corte o período de obra, ¿cuántos días suelen tardar en promedio entre recopilar las firmas, completar los anexos y radicar formalmente el acta de cobro ante el cliente?
a.	Generalmente lo que se hace es facturar y luego va el dossier, los pagos con petroleras van a 30 dias, se hace acta de facturación, cuando la aceptan se tienen 10 dias para entregar el dossier 
13.	Ya que los reportes de obra no se consolidan estrictamente día a día sino de forma semanal o por corte mensual, ¿con qué frecuencia real revisa el director de proyectos el avance y los costos de cada frente, y cuántos días suelen pasar entre lo que ocurre en la obra y el momento en que se entera la oficina en Bogotá?
a.	Se hace es por cortes, la comunicación es directa entonces el director de proyectos sabe que hace falta y cual es el siguiente paso. El tiempo entre que algo ocurre y el director se entera es casi tiempo real, llamadas diarias, si son cosas fáciles las llamadas son semanales, depende de la complejidad. Se tiene un formato de reporte diario y mensual de obra. Llenarlos implica tiempo y en obra lo que hace falta es tiempo. El archivo se llama “reporte diario de actividades”, el formato es extenso y tiene muchas cosas. Hay obras donde no se necesita ese reporte, en otras si. 
14.	Teniendo en cuenta que mencionaron que los módulos de Calidad (SIG) y Seguridad/Talento Humano (SST) son los más urgentes y robustos para la empresa, ¿están de acuerdo en que la primera versión del sistema se concentre exclusivamente en organizar los documentos oficiales, el control de cursos y exámenes del personal y la generación del dossier de calidad, dejando para una segunda fase las cotizaciones y compras?
a.	Si, lo que hay que optimizar mas es la parte de seguridad industrial y medio ambiente
15.	Si tuvieran que elegir los 3 problemas operativos o administrativos que hoy en día les hacen perder más dinero, les generan más demoras o les causan más dolores de cabeza, ¿cuáles serían esos 3 puntos que el sistema debería solucionar de forma prioritaria?
a.	No hay respuesta



Dilan es el de los dossieres, el tiene todo mas claro
Yonny es director de proyectos
Edward y Johana son coordinadores de gestion
Olga es auxiliar administrativa


Loard tiene alrededor de 40 empleados
