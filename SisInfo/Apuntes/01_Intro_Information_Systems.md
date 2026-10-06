[← Volver a Curso.md](../Curso.md)
**Fuente:** [BIS 3233 - Chapter 1: Introduction to Information Systems](https://youtu.be/X898qHM2uP0)

# 01. Introducción a los Sistemas de Información

**Términos clave:** `Information System`, `IT`, `ERP`, `DSS`, `TPS`, `ESS`, `Expert System`, `KMS`, `Process`, `Project`, `Supply Curve`.

## Definiciones y Reglas Operativas
* **Information System (IS)**: Sistema que recolecta, procesa, almacena, analiza y disemina información para un propósito específico [00:06:02]. 
* **Flujo Operativo (IS)**: Entrada de datos $\rightarrow$ Procesamiento $\rightarrow$ Salida de datos [00:06:12].
* **Information Technology (IT)**: Componentes físicos y digitales que incluyen Hardware, Software, Bases de Datos y Redes (`Networking`) [00:17:14].
* **Ecuación Estructural**: $\text{IS} = \text{IT} + \text{Personas} + \text{Procesos}$ [00:19:05].
* **Proceso (`Process`)**: Tarea continua y repetitiva **sin fecha de fin** (ej. cálculo del sistema de nómina) [00:09:50].
* **Proyecto (`Project`)**: Esfuerzo temporal con **fecha de inicio, fin y meta específica** (ej. construir un sistema nuevo) [00:09:50].
* **Impacto Microeconómico de la Tecnología**: Hacer más eficientes los procesos productivos desplaza la curva de oferta hacia la derecha (incremento de `Supply`), lo que disminuye el precio y aumenta la cantidad accesible en el mercado [00:26:32].
* **Reducción de Costos (COGS)**: Utilizar un IS integrado entre proveedores y clientes reduce el costo transaccional (ej. no tener que llamar manualmente para realizar un pedido) [00:20:18].

## Síntesis de Sistemas de Información
| Sistema | Acrónimo | Función y Propósito Core |
| :--- | :--- | :--- |
| **Enterprise Resource Planning** | `ERP` | Integra las operaciones vitales de una empresa para reducir tiempos de espera y desperdicio [00:07:18]. |
| **Decision Support System** | `DSS` | Provee evidencia para tomar decisiones sugiriendo resultados probables. **Nunca** toma decisiones de forma autónoma [00:13:21]. |
| **Transaction Processing System**| `TPS` | Registra metadatos de las ventas (montos, método de pago) previniendo pérdida de ingresos o cobros omitidos [00:13:56]. |
| **Executive Support System** | `ESS` | Cuadros de mando diseñados para las necesidades exclusivas de la alta gerencia corporativa (ej. liquidez disponible en tiempo real) [00:14:22]. |
| **Expert System** | `ES` | Base de datos diagnóstica adaptada a una profesión, producto o tarea técnica altamente específica (ej. manual de reparación de hardware) [00:15:02]. |
| **Knowledge Management System** | `KMS` | Sistema para almacenar, mantener y transferir el conocimiento organizacional explícito [00:15:42]. |
| **Financial Market System** | `FMS` | Plataforma de proyecciones y análisis bursátil en tiempo real (ej. Terminales Bloomberg) [00:16:14]. |

## Arquitectura Modular de un ERP (Core 6)
* **Finanzas y Contabilidad**: Tracking de variables financieras, ingresos y gastos corporativos [00:07:40].
* **Recursos Humanos**: Información de nómina, beneficios corporativos, tiempo de permanencia y reclutamiento [00:08:00].
* **Manufactura**: Refiere a la **actividad comercial primaria** (`Primary Business Activity`), sea manufacturar productos físicos o prestar servicios [00:08:44].
* **Supply Chain Management (SCM)**: Control lógico y físico del inventario (materia prima, trabajos en progreso y producto terminado) [00:09:28].
* **Gestión de Proyectos**: Manejo de iniciativas temporales con ciclos de vida definidos dentro de la organización [00:09:50].
* **Customer Relationship Management (CRM)**: Registro de hábitos de compra, tiempos e identidad del cliente para optimizar el retorno del presupuesto publicitario [00:10:43].

## Recursos Visuales

```mermaid
graph TD
    A[Information System - IS] --> B(Information Technology - IT)
    A --> C(Personas / Usuarios)
    A --> D(Procesos / Reglas de uso)
    B --> B1(Hardware)
    B --> B2(Software)
    B --> B3(Bases de Datos)
    B --> B4(Redes / Networking)