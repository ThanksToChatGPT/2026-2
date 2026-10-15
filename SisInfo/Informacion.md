# Información y Reglas del Sistema: LOARD Construcciones S.A.S.

## 1. Alcance, Fases y Fronteras del Sistema
* El sistema debe priorizar en su primera fase de desarrollo los módulos de Gestión Documental del Sistema Integrado de Gestión (SIG) y de Seguridad y Salud en el Trabajo (SST), posponiendo la gestión de compras y cotizaciones comerciales para una segunda fase.
* El sistema queda delimitado fuera de la contabilidad financiera, facturación formal y liquidación de nómina.
* El sistema no requiere replicar un formato contable rígido, pero debe generar reportes estructurados y organizados de horas trabajadas por persona y consumos de materiales para alimentar al área financiera.
* Los clientes externos (como Chevron) no tendrán usuarios directos ni acceso interactivo al sistema; el intercambio documental se mantiene exclusivamente por canales externos habituales (correo electrónico o ventanillas de radicación).
* El sistema no debe contemplar un portal de autoservicio ni roles de usuario para interventorías externas.

## 2. Infraestructura Tecnológica, Dispositivos y Conectividad
* La captura de información operativa, elaboración de informes y gestión administrativa se realiza principalmente desde computadores de oficina con sistema operativo Windows en cada facilidad.
* El uso de dispositivos móviles (celulares) queda restringido exclusivamente a tareas puntuales de campo: inspecciones técnicas de equipos y verificaciones de Seguridad y Salud en el Trabajo (SST).
* En los dispositivos móviles utilizados en campo predomina el sistema operativo Android, existiendo presencia aislada de iOS.
* No se cuenta con dispositivos móviles intrínsecamente seguros (antiexplosión / ATEX); existen zonas clasificadas dentro de las plantas donde está terminantemente prohibido el ingreso de teléfonos celulares.
* Todos los supervisores de obra disponen de planes de datos corporativos activos; el único frente con problemas críticos de cobertura celular e Internet es Buenaventura.
* La pérdida de conectividad a Internet es excepcional y no supera un tiempo límite de 6 horas continuas en Buenaventura.

## 3. Seguridad, Salud en el Trabajo (SST) y Datos Médicos
* El sistema debe bloquear de manera estricta e intransigente la asignación, registro o ejecución de actividades de cualquier trabajador que cuente con su curso de trabajo en alturas, espacios confinados o examen médico laboral vencido.
* El sistema no debe permitir bajo ninguna excepción autorizaciones manuales o dispensas temporales para trabajadores con certificaciones de alto riesgo vencidas.
* El sistema debe emitir una alerta preventiva media al cumplirse 30 días (1 mes) antes del vencimiento de un curso o examen médico.
* El sistema debe escalar a una alerta crítica alta cuando resten 15 días para el vencimiento de una certificación o examen ocupacional.
* Los ingenieros residentes, supervisores de obra y clientes únicamente podrán visualizar si el colaborador se encuentra "Apto" o "No Apto" para la labor asignada y la fecha de vigencia de dicho concepto.
* El sistema debe restringir totalmente la visualización de diagnósticos clínicos, paraclínicos o historias médicas, garantizando el acceso confidencial exclusivo al trabajador y al Coordinador de Gestión (Edward).
* La custodia física de las carpetas de salud ocupacional recae en la Auxiliar Administrativa (Olga).

## 4. Operación de Obra, Reportes y Avances
* Los operarios y cuadrillas no realizan reportes en el sistema; el registro y carga de información de campo es responsabilidad exclusiva de los supervisores e ingenieros residentes.
* El reporte de avance no opera bajo frecuencia diaria estricta en todas las obras: en proyectos específicos se realiza con corte semanal y en contratos marco se reporta mediante corte mensual.
* El sistema debe simplificar la carga de avances frente al formato tradicional "Reporte Diario de Actividades", reduciendo el tiempo operativo de diligenciamiento en obra.
* La revisión y aprobación de los informes de avance está a cargo del Director de Proyectos (Yonny).
* El sistema no debe bloquear los registros operativos subsecuentes por demoras en la aprobación de informes por parte de la Dirección de Proyectos.
* El sistema debe centralizar la carga de informes de obra para sustituir el mecanismo informal actual de seguimiento verbal y telefónico.
* El avance físico de la obra se debe medir calculando directamente las cantidades ejecutadas frente a las cantidades e ítems presupuestados en la cotización base.
* El sistema debe disparar una alerta urgente de desviación temporal y rentabilidad cuando el porcentaje de tiempo transcurrido supere el porcentaje de avance físico ejecutado (por ejemplo, alcanzar el 50% del plazo estimado sin lograr el 50% del avance).
* El componente de costo más crítico y determinante para la rentabilidad de los proyectos de la empresa es la mano de obra.

## 5. Abastecimiento, Compras y Manejo de Insumos
* Los ingenieros residentes cuentan con autonomía para compras directas de emergencia de hasta $250.000 COP con cargo a la caja menor de obra.
* Las cajas menores asignadas a los frentes de obra manejan montos globales de entre $3.000.000 y $5.000.000 COP.
* Toda compra o gasto que supere los $250.000 COP debe contar con autorización previa de la oficina central en Bogotá.
* En el flujo de compras: el ingeniero residente solicita la cotización, la Auxiliar Administrativa (Olga) genera la orden de compra y la Gerencia General autoriza el desembolso o pago.
* El rol de Director de Obra solo se habilita en proyectos de gran escala; en la operación habitual la relación es directa entre el residente y Bogotá.
* Las obras no cuentan con almacenista dedicado; la recepción, custodia y entrega de consumibles la realiza directamente el ingeniero residente.
* El suministro de consumibles (electrodos, discos, gases) se realiza de forma centralizada despachando desde Bogotá hacia cada frente; no existe proceso de devolución ni retorno de sobrantes o mermas a la sede principal.
* El porcentaje estándar de desperdicio técnico o merma presupuestado en consumibles de soldadura y tubería es del 5%.

## 6. Dossier de Calidad, Soldadura y Ensayos Técnicos
* El formato del Libro de Tubería (*Weld Book* - GT-FR64) se rige formalmente bajo la norma API 1104.
* Los laboratorios externos de Ensayos No Destructivos (END) entregan sus reportes técnicos en formato PDF.
* En proyectos de tubería se elabora una cartilla de soldadura sobre planos donde se identifican, enumeran y asocian las juntas, la estampa del soldador y los ensayos realizados.
* Es deseable pero no necesario que el sistema debe almacenar los archivos PDF de los ensayos no destructivos y permitir la extracción de datos clave de dichos informes.
* El Dossier de Calidad se conforma progresivamente durante el desarrollo de la obra integrando los siguientes documentos obligatorios:
  * Documentación contractual y legal (contrato, orden de servicio, pólizas).
  * Actas de corte de obra.
  * Planos de ingeniería (mecánicos, eléctricos, de diseño y planos finales *as-built*).
  * Certificados de calidad y conformidad de materiales y equipos.
  * Informes técnicos semanales e informe final de obra elaborados por el residente.
  * Memorias de cálculo.
* La entrega formal del Dossier de Calidad ante el cliente se efectúa al culminar la obra, contando con un plazo contractual límite de 10 días tras la aceptación del acta de facturación.
* El trámite financiero inicia con la radicación y aprobación del acta de facturación, la cual cuenta con un plazo de pago de 30 días por parte de las petroleras.
* Para la firma de actas y documentos contractuales se utiliza la inserción de imágenes de firma manuscrita, siendo este mecanismo aceptado contractualmente por los clientes actuales.
* Las únicas personas autorizadas en la empresa para firmar legalmente las actas de corte y los dossieres de calidad son la Gerente General y el Representante Legal.

## 7. Gestión Comercial, APU y Márgenes
* En los contratos marco las tarifas de todos los ítems de ejecución están preestablecidas y congeladas contractualmente; solo se generan nuevos Análisis de Precios Unitarios (APU) para ítems no contemplados en el marco o para obras licitadas fuera de este.
* Las cotizaciones se elaboran a partir de una plantilla marco oficial, la cual es adaptada por los ingenieros residentes y revisada por el Director de Proyectos (Yonny).
* El porcentaje de imprevistos (entre 7% y 10%) en las ofertas absorbe variaciones de precios (aprox. 1%), suspensiones por lluvia, demoras en permisos de trabajo en sitio, tiempos muertos operativos e imprevistos técnicos no desglosados en el APU inicial.

## 8. Gestión Documental y Transición desde Dropbox
* La migración de archivos desde Dropbox no incluirá la totalidad de los 23.000 archivos históricos; se restringirá a los registros y proyectos de los últimos 3 años.
* Aquellos documentos técnicos permanentes e históricos indispensables (como los Procedimientos de Soldadura WPS / PQR) deben migrarse sin importar su antigüedad.
* La selección de formatos y documentos vigentes del SIG para el nuevo repositorio requerirá un proceso de depuración manual exhaustivo archivo por archivo.

## 9. Roles y Personal Clave de la Organización
* La empresa cuenta con una nómina aproximada de 40 trabajadores.
* Dilan es el que tiene mas conocimiento sobre como estructurar los dossieres de calidad.
* Yonny es el Director de Proyectos, responsable de validar cotizaciones, avances e informes de obra.
* Edward y Johana son los Coordinadores de Gestión, encargados de la administración del SIG y de la gestión de SST y conceptos médicos.
* Olga es la Auxiliar Administrativa, responsable de las órdenes de compra y de custodiar los archivos físicos del personal.
* La Gerente General y el Representante Legal tienen a su cargo la aprobación final de pagos de compras y la firma de actas contractuales.

