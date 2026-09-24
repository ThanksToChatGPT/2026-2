[← Volver a Curso.md](../Curso.md)

# 01. Introducción a la Investigación de Operaciones y Modelos de PL

> **Fuente**: [01 Investigacion_de_Operaciones_Clase1.pdf](../Documentos/01%20Investigacion_de_Operaciones_Clase1.pdf)  
> **Tema**: Paradigma de optimización, componentes de un modelo, clasificación (PL, PNL, PLE) y formulación matemática básica.

---

## 📌 1. Fundamentos de la Investigación de Operaciones (IO)

- **Origen**: Segunda Guerra Mundial (Reino Unido) -> análisis científico de radar, operaciones navales (convoyes) y tácticas antisubmarinas.
- **Evolución**: Consolidación académica en el MIT y fundación de **ORSA** (*Operations Research Society of America*).
- **Definición**: Aplicación de métodos analíticos avanzados, matemáticos e ingenieriles para la **toma óptima de decisiones** en sistemas complejos bajo incertidumbre o gran escala de datos.
- **Pilares metodológicos**:
  - `Modelado Matemático`: Traducir el problema real a variables, funciones y restricciones.
  - `Optimización`: Algoritmos determinísticos para hallar la mejor alternativa.
  - `Modelos Probabilísticos`: Análisis estocástico y teoría de colas / riesgo.

---

## ⚙️ 2. El Paradigma de Optimización

Todo modelo de optimización matemática se compone de 3 elementos esenciales:

```
[ Variables de Decisión ] ---> [ Restricciones (Técnicas / Físicas) ] ---> [ Función Objetivo (Max / Min) ]
```

1. **Variables de Decisión ($x_j$)**:
   - Factores controlables por el decisor.
   - Representan cantidades medibles con unidad física o temporal (ej. unidades a producir, horas asignadas, dinero invertido).
2. **Función Objetivo ($z = f(x)$)**:
   - Medida cuantitativa de desempeño para jerarquizar soluciones alternativas.
   - Sentido: **Maximizar** (utilidad, beneficio, cobertura) o **Minimizar** (costos, mermas, tiempo, distancias).
3. **Restricciones ($g_i(x) \lesseqgtr b_i$)**:
   - Limitaciones estructurales que definen el espacio factible:
     - **Reglas de negocio / mercado**: Capacidad máxima de demanda, turnos máximos continuos, presupuesto.
     - **Leyes físicas / técnicas**: Conservación de balance de materia/inventario, disponibilidad de horas-máquina.
4. **Condiciones de No Negatividad ($x_j \ge 0$) / Integralidad**:
   - Garantizan consistencia física en el mundo real (no existe producción ni tiempo negativo).

---

## 🧩 3. Clasificación de Modelos de Programación Matemática

| Tipo de Modelo | Función Objetivo | Restricciones | Variables | Ejemplo / Forma |
| :--- | :--- | :--- | :--- | :--- |
| **Programación Lineal (PL)** | Lineal: $c_1 x_1 + \dots + c_n x_n$ | Lineales ($\le, =, \ge$) | Continuas $\ge 0$ | $\max 3x_1 + 4x_2$ s.a. $2x_1 + x_2 \le 10$ |
| **Programación No Lineal (PNL)** | No lineal (al menos un término) | No lineales (al menos una) | Continuas | $\max x_1 x_2$ s.a. $x_1 - x_2^2 \ge 10$ |
| **Programación Lineal Entera (PLE)** | Lineal | Lineales | Enteras o Binarias ($x_j \in \mathbb{Z}$) | $\max 3x_1 + 4x_2$ s.a. $x_1 \in \{0,1\}$ |

> ⚠️ **Reglas Críticas de Programación Lineal (PL)**:
> - **Prohibidas desigualdades estrictas**: NO se permite $<$ ni $>$. Las restricciones deben ser cerradas ($\le, \ge, =$).
> - **Prohibidas no linealidades**: Términos con potencias ($x^2$), raíces ($\sqrt{x}$), productos entre variables ($x_1 x_2$) o valores absolutos ($|x|$) transforman el modelo en **PNL**.

---

## 🎯 4. Espacio de Soluciones: Factibilidad vs. Optimalidad

- **Solución Factible**: Asignación de valores numéricos a las variables que **satisface todas y cada una** de las restricciones simultáneamente.
- **Solución Infactible**: Cualquier asignación que viole al menos una restricción.
- **Solución Óptima**: Solución factible que produce el valor más favorable de la función objetivo ($z^*$). Puede ser única o existir múltiples óptimos alternativos.

---

## 📝 5. Metodología de Formulación Estándar

1. **Paso 1: Declarar Variables**:
   - Definir simbología, nombre y unidades (ej. $x_1$: número de sillas tipo A a fabricar por semana).
2. **Paso 2: Formular Función Objetivo**:
   - Expresar la meta global con su operador: $\max z = \dots$ o $\min z = \dots$
3. **Paso 3: Formular Restricciones del Sistema**:
   - Agrupar por recursos o condiciones: $a_1 x_1 + a_2 x_2 \le \text{Capacidad}$.
4. **Paso 4: Delimitar el Dominio de las Variables**:
   - Declarar $x_j \ge 0$ (o $x_j \in \mathbb{Z}^+$ según aplique).

---

## 💡 6. Modelos de Aplicación Vistos en Clase

### Caso A: Concurso de Pasteles (Max)
- **Contexto**: Tiempo límite de 60 minutos. Tarta requiere 2 min y da 4 pts. Pastel requiere 3 min y da 5 pts.
- **Variables**:
  - $x$: Cantidad de tartas consumidas.
  - $y$: Cantidad de pasteles consumidos.
- **Modelo**:
  $$\max z = 4x + 5y$$
  $$\text{s.a.} \quad 2x + 3y \le 60 \quad \text{(Tiempo máximo)}$$
  $$x \ge 0, \quad y \ge 0 \quad \text{(No negatividad)}$$
- **Análisis de factibilidad**:
  - $(x=10, y=10) \implies 2(10) + 3(10) = 50 \le 60$ -> **Factible** ($z = 90$).
  - $(x=10, y=15) \implies 2(10) + 3(15) = 65 > 60$ -> **Infactible**.
- **Solución Óptima**:
  - Tasa de rendimiento por minuto: Tarta = $4/2 = 2\text{ pts/min}$; Pastel = $5/3 \approx 1.67\text{ pts/min}$.
  - Conviene comer solo tartas: $x^* = 30, \; y^* = 0 \implies z^* = 120\text{ puntos}$.

---

### Caso B: David's Tool Corporation (DTC)
Fabricante de kits de hondas/resorteras ($K$) y escudos de piedra ($S$).

#### Matriz de Parámetros
| Proceso / Recurso | Hondas ($K$) | Escudos ($S$) | Capacidad Disponible |
| :--- | :---: | :---: | :---: |
| **Recolección** | 2 h | 3 h | 100 h |
| **Alisado / Pulido** | 1 h | 2 h | 60 h |
| **Entrega** | 1 h | 1 h | 50 h |
| **Demanda Máxima** | 40 unidades | 30 unidades | Mercado |
| **Beneficio Unitario** | **3 Shekels** | **5 Shekels** | **Maximizar** |

#### Formulación Matemática Completa
- **Variables**:
  - $K$: Número de kits de hondas a fabricar.
  - $S$: Número de escudos de piedra a fabricar.
- **Función Objetivo**:
  $$\max z = 3K + 5S$$
- **Restricciones Técnicas**:
  $$2K + 3S \le 100 \quad \text{[Horas Recolección]}$$
  $$K + 2S \le 60 \quad \text{[Horas Alisado]}$$
  $$K + S \le 50 \quad \text{[Horas Entrega]}$$
  $$K \le 40 \quad \text{[Límite Demanda Hondas]}$$
  $$S \le 30 \quad \text{[Límite Demanda Escudos]}$$
  $$K \ge 0, \quad S \ge 0 \quad \text{[No Negatividad]}$$

---

## ⚠️ 7. Puntos Críticos para Evaluaciones y Parcial

1. **Condición de Linealidad Estricta**:
   - ¿Por qué $|x_1| \ge 0$ no es PL? Porque el valor absoluto contiene una discontinuidad en pendiente (no lineal).
   - ¿Por qué $\max x^2$ no es PL? Grado de la función cuadrático ($>1$).
   - ¿Por qué $x_1 x_2 \le 5$ no es PL? Producto de dos variables de decisión.
2. **Definición rigurosa de variables**:
   - Error típico: Definir $x_1$ = "Producción" (ambiguo).
   - Correcto: $x_1$ = "Cantidad de unidades producidas del producto A por semana".
3. **No Negatividad Obligatoria**:
   - Todo problema físico debe incluir explícitamente $x_j \ge 0$. Su omisión resta puntos en formulación.
