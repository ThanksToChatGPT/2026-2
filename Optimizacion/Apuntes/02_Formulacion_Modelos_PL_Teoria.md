[← Volver a Curso.md](./Curso.md) | [Ir a Ejemplos Prácticos de Formulación →](./02_Formulacion_Modelos_PL_Ejemplos.md)

# 📌 Fundamentos y Metodología de Formulación en Programación Lineal

> **Documento fuente:** `02 optimización Clase 2 y 3.pdf` (Facultad de Ingeniería, Universidad Nacional de Colombia)  
> **Tema:** Metodología científica de modelado en I.O., taxonomía de restricciones, análisis dimensional y arquetipos de modelos lineales.

---

## 1. Metodología Científica del Modelado en I.O.

### 1.1 Proceso Simplificado de Modelado (3 Fases)
El modelado es un proceso cíclico de abstracción controlada:
```
[Modelo Simple] ──────> [Mejoras Iterativas] ──────> [Modelo Mejorado]
(Representación básica)   (Refinamiento progresivo)    (Precisión suficiente)
```
- **Modelo Simple:** Abstracción inicial que captura la dinámica central omitiendo factores marginales.
- **Mejoras Iterativas:** Calibración sucesiva de parámetros, descomposición de relaciones y adición de restricciones operativas.
- **Modelo Mejorado:** Punto de convergencia donde el modelo alcanza **precisión suficiente** para soportar decisiones sin sobrecostos de cómputo ni sobrediseño.

### 1.2 Enfoque Científico de I.O. y Recursos Escasos
- **Definición de I.O.:** Aplicación sistemática del **método científico** a la toma de decisiones para diseñar y operar sistemas que requieren **asignación óptima de recursos escasos** (capital, mano de obra, capacidad de máquina, materias primas, tiempo).
- **Tríada operativa:**
  $$\mathbf{Modelos\ Matemáticos} \longrightarrow \mathbf{Soluciones\ Factibles} \longrightarrow \mathbf{Optimización}$$

### 1.3 Componentes Fundamentales de un Modelo Matemático
$$\mathbf{Parámetros} \text{ (Datos conocidos)} \;\longrightarrow\; \mathbf{Modelo} \begin{cases} \text{Variables de decisión} \\ \text{Restricciones} \\ \text{Función objetivo} \end{cases} \;\longrightarrow\; \mathbf{Solución} \text{ (Conclusiones / Políticas)}$$

| Componente | Definición | Símbolo / Expresión | Rol Operativo |
| :--- | :--- | :---: | :--- |
| **Variables de Decisión** | Incógnitas controlables por el decisor | $x_1, x_2, \dots, x_n$ | Cuantifican los niveles de actividad del sistema. |
| **Función Objetivo (FO)** | Medida de desempeño global a optimizar | $\operatorname{Max} Z \text{ o } \operatorname{Min} Z$ | Evalúa la efectividad económica o técnica. |
| **Restricciones** | Límites físicos, técnicos, normativos o de mercado | $\sum a_{ij} x_j \lesseqgtr b_i$ | Acotan la región de combinaciones factibles. |
| **Parámetros** | Constantes numéricas exógenas conocidas | $c_j, a_{ij}, b_i$ | Coeficientes de costo, tasas técnicas y disponibilidades. |

### 1.4 Ventajas y Advertencias del Modelado
- **Ventajas:**
  - **Concisión:** Describe problemas multidimensionales en formulaciones compactas.
  - **Claridad estructural:** Revela interrelaciones y dependencias causa-efecto del sistema.
  - **Foco en datos clave:** Identifica parámetros críticos que requieren medición rigurosa.
  - **Manejo holístico:** Gestiona trade-offs entre subsistemas en conflicto.
  - **Apalancamiento computacional:** Permite el uso de solvers algorítmicos de alta escala.
- ⚠️ **Principio de validez (Simplificación vs Realidad):** Dado que todo modelo es una simplificación de la realidad, debe verificarse permanentemente que sea una **representación válida** del problema operativo.

---

## 2. Resolución, Validación e Implantación

### 2.1 Optimizar vs Satisfizar
- **Optimizar:** Enfoque matemático que busca la mejor solución absoluta en el espacio de búsqueda.
- **Satisfizar (Herbert Simon):** Enfoque pragmático que selecciona una solución **suficientemente buena** que cumpla los criterios mínimos ante límites de tiempo, costo o información.
- > *"Optimizar es la ciencia de lo absoluto; Satisfizar es el arte de lo factible."* — Samuel Eilon
- **Procedimientos Heurísticos:** Algoritmos de búsqueda aproximada que proporcionan **soluciones subóptimas de alta calidad** en tiempos computacionales reducidos.

### 2.2 Protocolo de Validación y Prueba del Modelo
Las primeras versiones de modelos complejos contienen errores dimensionales o lógicos. Recomendaciones:
1. **Inspección global:** Análisis panorámico de orden de magnitud y coherencia general.
2. **Revisión por pares externos:** Evaluación por un analista independiente ajeno a la formulación.
3. **Contraste con el problema:** Cotejar supuestos directivos contra las ecuaciones.
4. **Análisis dimensional estricto:** Garantizar homogeneidad de unidades en cada término sumado o igualado.
5. **Pruebas de plausibilidad y perturbación:** Variar parámetros de entrada y verificar que las respuestas sigan la dirección esperada.
6. **Prueba retrospectiva:** Correr el modelo con datos históricos para comprobar si las soluciones hubieran mejorado las decisiones reales tomadas.

### 2.3 Preparación para la Aplicación (Módulos Integrados del DSS)
Un sistema de optimización operativo integra 6 subsistemas:
```
  ┌─────────────────────────────────────────────────────────┐
  │       SISTEMA INTEGRADO DE SOPORTE A DECISIONES (DSS)   │
  ├────────────────────────────┬────────────────────────────┤
  │ 1. Programas de Interfaz   │ 2. Bases de Datos / ERP    │
  ├────────────────────────────┼────────────────────────────┤
  │ 3. Motores de Solución     │ 4. Reportes Gerenciales    │
  ├────────────────────────────┼────────────────────────────┤
  │ 5. Automatización Salidas  │ 6. Escenarios What-If      │
  └────────────────────────────┴────────────────────────────┘
```

### 2.4 Fases de Implementación y División de Roles
```
[1. Explicación] ────> [2. Procedimientos] ────> [3. Capacitación] ────> [4. Supervisión]
  (Equipo I.O.)          (I.O. + Admin)             (Administración)        (Equipo I.O.)
```
1. **Explicación operativa (I.O.):** Demostración del funcionamiento y beneficios a la línea de mando.
2. **Desarrollo procedural (I.O. + Administración):** Definición conjunta de protocolos de operación (SOPs).
3. **Capacitación (Administración):** Entrenamiento formal del personal en la entrada de datos y uso de salidas.
4. **Supervisión y auditoría (I.O.):** Seguimiento inicial para ajustes, calibración y mejoras futuras.

---

## 3. Taxonomía de Restricciones y Análisis Dimensional

### 3.1 Clasificación Formal de Restricciones
1. **Restricciones Funcionales / Estructurales:** Modelan limitaciones físicas, técnicas, económicas y de mercado:
   $$\sum_{j=1}^n a_{ij} x_j \le b_i \quad \text{(capacidad)}, \quad \sum_{j=1}^n a_{ij} x_j \ge b_i \quad \text{(requerimiento)}, \quad \sum_{j=1}^n a_{ij} x_j = b_i \quad \text{(balance)}$$
2. **Restricciones de Signo / No Negatividad:** Viabilidad física de las variables:
   $$x_j \ge 0 \quad \text{(no negatividad)}, \quad x_j \le 0 \quad \text{(no positividad)}, \quad x_j \in \mathbb{R} \quad \text{(irrestricta en signo)}$$

### 3.2 Principio de Homogeneidad Dimensional
⚠️ **Regla crítica:** En toda ecuación o inecuación, cada término sumado debe tener **estrictamente la misma unidad compuesta**.
- **En la Función Objetivo:**
  $$[Z] = [c_j] \times [x_j] = \left(\frac{\$}{\text{unidad}}\right) \times \left(\frac{\text{unidades}}{\text{período}}\right) = \frac{\$}{\text{período}}$$
- **En las Restricciones:**
  $$[a_{ij}] \times [x_j] = \left(\frac{\text{recurso } i}{\text{unidad } j}\right) \times \left(\frac{\text{unidades } j}{\text{período}}\right) = \frac{\text{recurso } i}{\text{período}} \lesseqgtr [b_i] \left(\frac{\text{recurso } i}{\text{período}}\right)$$

### 3.3 Desglose Económico de la Función Objetivo
$$\text{Utilidad Neta } (Z) = \text{Ingresos Semanales} - \text{Costos MP} - \text{Costos Variables}$$
$$Z = \sum_{j=1}^n (P_j - CMP_j - CV_j) x_j = \sum_{j=1}^n c_j^{\text{neto}} x_j$$

---

## 4. Arquetipos Clásicos de Modelos Lineales

### 4.1 Modelo Producto-Insumo (*Product-Mix*)
- **Objetivo:** Maximizar el margen de contribución sujeto a capacidades limitadas en talleres, materias primas y horas-hombre:
  $$\operatorname{Max} Z = \sum_{j=1}^n c_j x_j \quad \text{s.a.} \quad \sum_{j=1}^n a_{ij} x_j \le b_i \; (\forall i), \quad x_j \ge 0$$
- **Cálculo de capacidad en Horas-Hombre:**
  $$b_i = N_{\text{operarios}} \times h_{\text{diarias/operario}} \times d_{\text{días laborados/semana}}$$
- **Condiciones de mercado:** Demandas mínimas obligatorias ($x_j \ge D_{j,\min}$) y cuotas máximas de absorción ($x_j \le D_{j,\max}$).

### 4.2 Modelos de Dieta y Nutrición
- **Objetivo:** Minimizar el costo de adquisición de una canasta de alimentos asegurando umbrales nutricionales:
  $$\operatorname{Min} Z = \sum_{j=1}^n c_j x_j \quad \text{s.a.} \quad \sum_{j=1}^n a_{ij} x_j \ge b_i^{\min} \quad \text{y} \quad \sum_{j=1}^n a_{ij} x_j \le b_i^{\max}, \quad x_j \ge 0$$

### 4.3 Modelos de Mezcla (*Blending Problems*) y Linealización
- **Conservación de masa/volumen:** Para un lote fijado $Q_{\text{total}}$: $\sum_{j=1}^n x_j = Q_{\text{total}}$.
- **Linealización de restricciones de porcentaje/calidad:** Las divisiones entre variables totales se linealizan por multiplicación cruzada:
  $$\frac{\sum_{j} q_j x_j}{\sum_{j} x_j} \ge Q^* \iff \sum_{j} (q_j - Q^*) x_j \ge 0$$
  $$\frac{x_{kj}}{\sum_{i} x_{ij}} = p \iff (1 - p) x_{kj} - p \sum_{i \neq k} x_{ij} = 0$$

### 4.4 Modelos de Transporte y Distribución (Red Bipartita)
- **Estructura:** $m$ plantas de oferta y $n$ distribuidores de demanda:
  $$\operatorname{Min} Z = \sum_{i=1}^m \sum_{j=1}^n c_{ij} X_{ij} \quad \text{s.a.} \quad \sum_{j=1}^n X_{ij} \le a_i \; (\forall i), \quad \sum_{i=1}^m X_{ij} = b_j \; (\forall j), \quad X_{ij} \ge 0$$
- **Variante Multiatributo / Beneficio Neto:** Cuando se conocen precios de venta en destino ($p_j$) y costos fabriles ($c_i^{\text{prod}}$):
  $$\operatorname{Max} Z = \sum_{i=1}^m \sum_{j=1}^n \left( p_j - c_i^{\text{prod}} - c_{ij}^{\text{trans}} \right) X_{ij}$$

### 4.5 Modelos de Planificación Regional con Equidad Proporcional
- **Condición de equidad:** Obliga a que distintas comunidades (o unidades $k$) siembren exactamente la misma fracción de su tierra disponible:
  $$\frac{\sum_c X_{c,1}}{\text{Tierra}_1} = \frac{\sum_c X_{c,2}}{\text{Tierra}_2} = \dots = \frac{\sum_c X_{c,K}}{\text{Tierra}_K}$$

### 4.6 Modelos de Asignación Biyectiva (1 a 1)
- Variables binarias $X_{ij} \in \{0, 1\}$. Matriz totalmente unimodular:
  $$\sum_{j=1}^n X_{ij} = 1 \; (\forall i: \text{proyecto a un contratista}), \quad \sum_{i=1}^n X_{ij} = 1 \; (\forall j: \text{contratista a un proyecto})$$

### 4.7 Modelos de Programación de Turnos Continuos Solapados
- Jornadas laborales de duración $T$ (ej. 8h) que inician cada $\Delta t$ (ej. 4h), cubriendo requerimientos horarios variables en bloques $k$:
  $$X_{k-1} + X_k \ge \text{Requerimiento}_k \quad (\forall k)$$

### 4.8 Modelos Multiperíodo de Personal y Recursos Humanos
- **Variables dinámicas:** $Y_t$ (experimentados al inicio del mes $t$), $X_t$ (aprendices contratados al mes $t$).
- **Horas netas disponibles:** Horas de experimentados menos horas dedicadas a supervisar aprendices ($h_{\text{sup}}$):
  $$h_{\text{exp}} Y_t - h_{\text{sup}} X_t \ge \text{Demanda}_t$$
- **Ecuación de inventario con tasa de retiro voluntario $\alpha$:**
  $$Y_{t+1} = (1 - \alpha) Y_t + X_t$$

### 4.9 Modelos de Gestión de Riesgo Crediticio y Cartera
- **Retorno neto esperado:** Intereses cobrados sobre préstamos al corriente menos pérdida total por mora:
  $$\operatorname{Max} Z = \sum_j \left[ r_j(1 - \delta_j) - \delta_j \right] x_j$$
- **Control de riesgo global:** La mora total ponderada no debe superar la cuota máxima permitida ($\delta_{\max}$):
  $$\sum_j (\delta_j - \delta_{\max}) x_j \le 0$$

### 4.10 Modelos con Penalización por Demanda Insatisfecha
- Inclusión de variables de holgura/déficit $s_j \ge 0$ penalizadas en la función objetivo:
  $$\operatorname{Max} Z = \sum_j c_j x_j - \sum_j p_j s_j \quad \text{s.a.} \quad x_j + s_j = D_j \quad (\forall j)$$
