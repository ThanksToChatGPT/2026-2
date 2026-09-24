[← Volver a Curso.md](./Curso.md) | [← Ver Teoría de Formulación](./02_Formulacion_Modelos_PL_Teoria.md)

# 📝 Catálogo de Modelos Aplicados de Programación Lineal (29 Ejemplos)

> **Documento fuente:** `02 optimización Clase 2 y 3.pdf` (Facultad de Ingeniería, Universidad Nacional de Colombia)  
> **Estructura para cada ejemplo:** Enunciado sintético $\rightarrow$ Variables de decisión $\rightarrow$ Función objetivo $\rightarrow$ Restricciones funcionales y de signo.

---

## Bloque 1: Modelos Introductorios y Gestión Operativa

### Ejemplo 1: Optimización de Boletos de Viaje de Negocios (Págs. 6–9)
- **Resumen del Enunciado:** Un ejecutivo debe viajar durante 5 semanas consecutivas entre las ciudades A y B, saliendo de A los lunes y regresando los miércoles. Un viaje redondo regular cuesta $\$400$, pero si abarca un fin de semana tiene un $20\%$ de descuento ($\$320$). Un boleto sencillo cuesta $75\%$ de la tarifa regular ($\$300$). Se busca determinar la estrategia de compra que minimice el costo total.
- **Variables de Decisión:**
  - $A_1, A_2, A_3$: Elección de la estrategia de compra de pasajes (evaluación de alternativas discretas factibles).
  - En formulación lineal continua: $x_1$ = boletos redondos regulares A-B-A; $x_2$ = boletos sencillos; $x_3$ = boletos redondos cruzados B-A-B con fin de semana.
- **Función Objetivo:**
  $$\operatorname{Min} Z = \text{Costo total de traslado durante las 5 semanas } [\$]$$
- **Restricciones:**
  1. *Cobertura semanal:* Garantizar salida de A el lunes y retorno el miércoles para cada semana $t \in \{1, 2, 3, 4, 5\}$.
  2. *Validez tarifaria:* Aplicar descuento del $20\%$ únicamente si la estadía entre ida y vuelta cubre sábado y domingo.
- **Evaluación del Caso:**
  - Alternativa 1 (5 boletos redondos regulares): $Z_1 = 5 \times 400 = \$2000$.
  - Alternativa 2 (1 sencillo A-B, 4 redondos con descuento B-A-B, 1 sencillo B-A): $Z_2 = 300 + 4(320) + 300 = \$1880$.
  - Alternativa 3 (1 redondo A-B-A que cubre semana 1 a 5 con descuento + 4 redondos intermedios B-A-B con descuento): $Z_3 = 5 \times 320 = \mathbf{\$1600}$ *(Solución Óptima)*.

---

### Ejemplo 2: Dieta Saludable en Comida Rápida (Caso Super Size Me) (Págs. 22–25)
- **Resumen del Enunciado:** Diseñar una comida nutricionalmente equilibrada al menor costo en McDonald's eligiendo entre: Hamburguesa ($H$, $\$1.00$), Big Mac ($B$, $\$3.00$), McChicken ($M$, $\$2.50$), Ensalada César ($C$, $\$3.00$) y Papas Pequeñas ($R$, $\$1.00$). Requerimientos: calorías entre 600 y 900 kcal; menos del $40\%$ de calorías de grasa; sodio diario menor o igual al $50\%$ del límite de 2300 mg ($\le 1150\text{ mg}$); al menos 30 g de proteína.
- **Variables de Decisión:**
  - $H$: Cantidad de porciones de hamburguesa a consumir [unidades].
  - $B$: Cantidad de porciones de Big Mac a consumir [unidades].
  - $M$: Cantidad de porciones de McChicken a consumir [unidades].
  - $C$: Cantidad de porciones de ensalada César con pollo a consumir [unidades].
  - $R$: Cantidad de porciones de papas fritas pequeñas a consumir [unidades].
  - $F$: Calorías totales de la comida [kcal].
- **Función Objetivo:**
  $$\operatorname{Min} Z = H + 3B + 2.5M + 3C + R \quad [\$]$$
- **Restricciones:**
  1. *Calorías totales:* $250H + 770B + 360M + 190C + 230R = F$
  2. *Rango calórico:* $600 \le F \le 900$
  3. *Límite de grasa ($\le 40\%$ de $F$):* $81H + 360B + 144M + 45C + 99R \le 0.4F$
  4. *Límite de sodio ($\le 1150\text{ mg}$):* $480H + 1170B + 800M + 580C + 160R \le 1150$
  5. *Aporte mínimo de proteína:* $31H + 44B + 14M + 27C + 3R \ge 30$
  6. *No negatividad:* $H, B, M, C, R \ge 0$
- **Resultados presentados:**
  - *Solución PL Continua:* $H = 1.13, \; B = 0.41 \implies Z = \$2.37$.
  - *Solución Entera:* $H = 1, \; R = 2 \implies Z = \$3.00$.

---

### Ejemplo 3: Programación Cíclica de Trabajadores Postales (Págs. 26–30)
- **Resumen del Enunciado:** El correo postal opera los 7 días. Cada cartero trabaja 5 días consecutivos y descansa 2 días seguidos semanalmente. Demandas mínimas por día: Lun: 17, Mar: 13, Mié: 15, Jue: 19, Vie: 14, Sáb: 16, Dom: 11. Se busca minimizar el total de trabajadores contratados.
- **Variables de Decisión:**
  - $x_j$: Número de trabajadores postales que inician su turno de 5 días de trabajo en el día $j$ ($j = 1:\text{Lun}, 2:\text{Mar}, \dots, 7:\text{Dom}$) [trabajadores/semana].
- **Función Objetivo:**
  $$\operatorname{Min} Z = x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7 \quad [\text{trabajadores}]$$
- **Restricciones:**
  1. *Lunes (descansan cohortes 2 y 3):* $x_1 + x_4 + x_5 + x_6 + x_7 \ge 17$
  2. *Martes (descansan 3 y 4):* $x_1 + x_2 + x_5 + x_6 + x_7 \ge 13$
  3. *Miércoles (descansan 4 y 5):* $x_1 + x_2 + x_3 + x_6 + x_7 \ge 15$
  4. *Jueves (descansan 5 y 6):* $x_1 + x_2 + x_3 + x_4 + x_7 \ge 19$
  5. *Viernes (descansan 6 y 7):* $x_1 + x_2 + x_3 + x_4 + x_5 \ge 14$
  6. *Sábado (descansan 7 y 1):* $x_2 + x_3 + x_4 + x_5 + x_6 \ge 16$
  7. *Domingo (descansan 1 y 2):* $x_3 + x_4 + x_5 + x_6 + x_7 \ge 11$
  8. *No negatividad e integralidad:* $x_j \ge 0, \; x_j \in \mathbb{Z} \quad (\forall j = 1, \dots, 7)$

---

## Bloque 2: Finanzas, Calidad y Manufactura Básica

### Ejemplo 4: Selección de Cartera / Inversión Financiera (Págs. 32–33)
- **Resumen del Enunciado:** Asignar un capital de $\$5.000.000\text{ USD}$ entre dos valores: A (rentabilidad 9%, índice de riesgo 5) y B (rentabilidad 15%, índice de riesgo 8). La rentabilidad total mínima debe ser del $12\%$ y el riesgo promedio no debe superar 6.
- **Variables de Decisión:**
  - $X_1$: Cantidad invertida en el valor A [USD].
  - $X_2$: Cantidad invertida en el valor B [USD].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 0.09 X_1 + 0.15 X_2 \quad [\text{USD/año}]$$
- **Restricciones:**
  1. *Presupuesto total:* $X_1 + X_2 = 5.000.000$
  2. *Riesgo combinado máximo:* $5X_1 + 8X_2 \le 6(5.000.000) \iff 5X_1 + 8X_2 \le 30.000.000$
  3. *Rentabilidad mínima:* $0.09X_1 + 0.15X_2 \ge 0.12(5.000.000) \iff 0.09X_1 + 0.15X_2 \ge 600.000$
  4. *No negatividad:* $X_1, X_2 \ge 0$

---

### Ejemplo 5: Inspección y Control de Calidad Diario (Págs. 34–35)
- **Resumen del Enunciado:** Inspeccionar al menos 1500 piezas en 8 horas. Inspector Grado I: 20 piezas/h, precisión 96% (error 4%), salario $\$5/\text{h}$, disponibilidad hasta 10. Inspector Grado II: 14 piezas/h, precisión 92% (error 8%), salario $\$4/\text{h}$, disponibilidad hasta 15. Cada error cuesta $\$3$ a la empresa.
  - Costo/hora Grado I = $5 + 3(0.04)(20) = 7.40\text{ USD/h} \implies 59.20\text{ USD/día}$.
  - Costo/hora Grado II = $4 + 3(0.08)(14) = 7.36\text{ USD/h} \implies 58.88\text{ USD/día}$.
- **Variables de Decisión:**
  - $x_1$: Número de inspectores de Grado I asignados [inspectores].
  - $x_2$: Número de inspectores de Grado II asignados [inspectores].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 59.20 x_1 + 58.88 x_2 \quad [\text{USD/día}]$$
- **Restricciones:**
  1. *Disponibilidad Grado I:* $x_1 \le 10$
  2. *Disponibilidad Grado II:* $x_2 \le 15$
  3. *Piezas mínimas inspeccionadas (8h):* $20(8)x_1 + 14(8)x_2 \ge 1500 \iff 160x_1 + 112x_2 \ge 1500$
  4. *No negatividad e integralidad:* $x_1, x_2 \ge 0, \quad x_1, x_2 \in \mathbb{Z}^+$

---

### Ejemplo 6: Dieta / Mezcla para Alimento de Animales (Págs. 36–37)
- **Resumen del Enunciado:** Determinar la proporción de piedra caliza ($L$, costo 10¢/kg), maíz ($C$, costo 30.5¢/kg) y harina de soya ($S$, costo 90¢/kg) en 1 kg de mezcla para cumplir: calcio entre $0.8\%$ y $1.2\%$, proteína mínimo $22\%$ y fibra máximo $5\%$.
- **Variables de Decisión:**
  - $L, C, S$: Proporciones (fracción en peso) de piedra caliza, maíz y soya en la mezcla [adimensional / kg de insumo por kg de mezcla].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 10L + 30.5C + 90S \quad [\text{centavos/kg}]$$
- **Restricciones:**
  1. *Calcio mínimo (0.8%):* $0.38L + 0.001C + 0.002S \ge 0.008$
  2. *Calcio máximo (1.2%):* $0.38L + 0.001C + 0.002S \le 0.012$
  3. *Proteína mínima (22%):* $0.09C + 0.50S \ge 0.22$
  4. *Fibra máxima (5%):* $0.02C + 0.08S \le 0.05$
  5. *Conservación de masa:* $L + C + S = 1$
  6. *No negatividad:* $L, C, S \ge 0$

---

### Ejemplo 7: Mezcla de Combustibles en Refinería (Págs. 38–39)
- **Resumen del Enunciado:** Refinería produce gasolinas A (octanaje $\ge 93$, precio $\$37.5/\text{B}$) y B (octanaje $\ge 85$, precio $\$28.5/\text{B}$) a partir de 5 stocks con octanajes [70, 80, 85, 90, 99], costos [\$9, \$12.5, \$12.5, \$27.5, \$27.5] y disponibilidades [2000, 4000, 4000, 5000, 3000] barriles. La materia prima no usada se vende a su mismo costo.
- **Variables de Decisión:**
  - $X_{iA}, X_{iB}$: Barriles de materia prima $i$ ($i = 1, \dots, 5$) mezclados para combustible A y B [barriles].
  - $Y_i$: Barriles de stock $i$ no utilizados y vendidos al costo [barriles].
  - $F_A, F_B$: Barriles totales obtenidos de combustible A y B [barriles].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 9Y_1 + 12.5Y_2 + 12.5Y_3 + 27.5Y_4 + 27.5Y_5 + 37.5 F_A + 28.5 F_B \quad [\$]$$
- **Restricciones:**
  1. *Disponibilidad de stocks:* $X_{iA} + X_{iB} + Y_i = \text{Disp}_i \quad (\forall i = 1, \dots, 5)$
  2. *Volumen total producido:* $\sum_{i=1}^5 X_{iA} = F_A, \quad \sum_{i=1}^5 X_{iB} = F_B$
  3. *Octanaje Gasolina A:* $70X_{1A} + 80X_{2A} + 85X_{3A} + 90X_{4A} + 99X_{5A} \ge 93F_A$
  4. *Octanaje Gasolina B:* $70X_{1B} + 80X_{2B} + 85X_{3B} + 90X_{4B} + 99X_{5B} \ge 85F_B$
  5. *No negatividad:* $X_{iA}, X_{iB}, Y_i, F_A, F_B \ge 0$

---

### Ejemplo 8: Juguetería de Madera – Soldados y Trenes (Págs. 40–54)
- **Resumen del Enunciado:** Una juguetería produce soldados ($x_1$) y trenes ($x_2$). Soldado: venta $\$27$, MP $\$10$, costos variables $\$14$ (margen $\$3$); requiere 2h acabado, 1h carpintería; demanda máxima 40 u/semana. Tren: venta $\$21$, MP $\$9$, costos variables $\$10$ (margen $\$2$); requiere 1h acabado, 1h carpintería; demanda ilimitada. Disponibilidad: 100h acabado y 80h carpintería por semana.
- **Variables de Decisión:**
  - $x_1$: Cantidad de soldados a fabricar por semana [soldados/semana].
  - $x_2$: Cantidad de trenes a fabricar por semana [trenes/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = (27 - 10 - 14)x_1 + (21 - 9 - 10)x_2 = 3x_1 + 2x_2 \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Horas de acabado:* $2x_1 + x_2 \le 100$
  2. *Horas de carpintería:* $x_1 + x_2 \le 80$
  3. *Límite de demanda de soldados:* $x_1 \le 40$
  4. *No negatividad:* $x_1, x_2 \ge 0$

---

## Bloque 3: Modelos Producto-Insumo (*Product-Mix*)

### Ejemplo 9: Compañía SIGMA – Pupitres, Sillas y Mesas (Págs. 56–58)
- **Resumen del Enunciado:** SIGMA fabrica pupitres ($X_1$), sillas ($X_2$) y mesas ($X_3$) con utilidades unitarias de $\$5.000, \$6.000, \$3.000$. Disponibilidad semanal: 150 m de madera, 120 m de tubo y 200 horas-hombre. Requerimientos: Pupitre (5m madera, 3m tubo, 4h-h), Silla (3m madera, 4m tubo, 5h-h), Mesa (2m madera, 3m tubo, 1h-h).
- **Variables de Decisión:**
  - $X_1$: Pupitres a fabricar por semana [u/semana].
  - $X_2$: Sillas a fabricar por semana [u/semana].
  - $X_3$: Mesas a fabricar por semana [u/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 5000 X_1 + 6000 X_2 + 3000 X_3 \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Madera:* $5X_1 + 3X_2 + 2X_3 \le 150$
  2. *Tubo:* $3X_1 + 4X_2 + 3X_3 \le 120$
  3. *Horas-hombre:* $4X_1 + 5X_2 + X_3 \le 200$
  4. *No negatividad:* $X_1, X_2, X_3 \ge 0$

---

### Ejemplo 10: Compañía BETA – Puertas, Ventanas y Claraboyas (Págs. 59–62)
- **Resumen del Enunciado:** Capacidad disponible semanal liberada: 200h corte, 150h empaque, 240h soldadura. Artículos: Puertas ($X_1$, $\$5000$), Ventanas ($X_2$, $\$3000$), Claraboyas ($X_3$, $\$4000$). Mercadeo exige vender al menos 20 ventanas y máximo 10 claraboyas.
  - Puerta: 2h corte, 5h empaque, 3h soldadura.
  - Ventana: 5h corte, 1h empaque, 4h soldadura.
  - Claraboya: 4h corte, 3h empaque, 2h soldadura.
- **Variables de Decisión:**
  - $X_1$: Puertas a producir por semana [u/semana].
  - $X_2$: Ventanas a producir por semana [u/semana].
  - $X_3$: Claraboyas a producir por semana [u/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 5000 X_1 + 3000 X_2 + 4000 X_3 \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Corte:* $2X_1 + 5X_2 + 4X_3 \le 200$
  2. *Empaque:* $5X_1 + X_2 + 3X_3 \le 150$
  3. *Soldadura:* $3X_1 + 4X_2 + 2X_3 \le 240$
  4. *Demanda mínima ventanas:* $X_2 \ge 20$
  5. *Demanda máxima claraboyas:* $X_3 \le 10$
  6. *No negatividad:* $X_1, X_2, X_3 \ge 0$

---

### Ejemplo 11: Compañía ALFA – Lotes de Artículos de Escritorio (Págs. 63–65)
- **Resumen del Enunciado:** Fabrica esferos, estilógrafos y plumillas modelados en paquetes de 10 unidades. Talleres: Montaje (100 h/mes) y Decoración (175 h/mes). Tiempos por paquete: Esferos (1h montaje, 1.5h dec.), Estilógrafos (2h montaje, 3h dec.), Plumillas (1.5h montaje, 2.5h dec.). Utilidades por paquete de 10: Esferos $\$2.000$ ($10 \times \$200$), Estilógrafos $\$2.500$ ($10 \times \$250$), Plumillas $\$2.250$ ($10 \times \$225$).
- **Variables de Decisión:**
  - $X_1$: Paquetes de 10 esferos a producir por mes [paquetes/mes].
  - $X_2$: Paquetes de 10 estilógrafos a producir por mes [paquetes/mes].
  - $X_3$: Paquetes de 10 plumillas a producir por mes [paquetes/mes].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 2000 X_1 + 2500 X_2 + 2250 X_3 \quad [\$/\text{mes}]$$
- **Restricciones:**
  1. *Montaje:* $X_1 + 2X_2 + 1.5X_3 \le 100$
  2. *Decoración:* $1.5X_1 + 3X_2 + 2.5X_3 \le 175$
  3. *No negatividad:* $X_1, X_2, X_3 \ge 0$

---

### Ejemplo 12: Compañía GAMA – Camisas y Blusas (Págs. 66–68)
- **Resumen del Enunciado:** Fabrica camisas ($X_1$, utilidad $\$7.000$) y blusas ($X_2$, utilidad $\$9.000$). Jornada: 8 h/día, 5 días/semana (40 h/trabajador-semana). Plantilla asignada: Corte: 40 operarios ($40 \times 40 = 1600\text{ h}$); Ensamble: 80 operarios ($80 \times 40 = 3200\text{ h}$); Empaque: 20 operarios ($20 \times 40 = 800\text{ h}$).
  - Camisa: 1h corte, 3h ensamble, 0.5h empaque.
  - Blusa: 0.5h corte, 4h ensamble, 1h empaque.
- **Variables de Decisión:**
  - $X_1$: Cantidad de camisas a fabricar por semana [u/semana].
  - $X_2$: Cantidad de blusas a fabricar por semana [u/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 7000 X_1 + 9000 X_2 \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Corte:* $X_1 + 0.5 X_2 \le 1600$
  2. *Ensamble:* $3X_1 + 4X_2 \le 3200$
  3. *Empaque:* $0.5X_1 + X_2 \le 800$
  4. *No negatividad:* $X_1, X_2 \ge 0$

---

### Ejemplo 13: Compañía OMEGA – Pupitres Uni y Bipersonales (Págs. 69–71)
- **Resumen del Enunciado:** Manufactura pupitres unipersonales ($X_1$, utilidad $\$3.000$) y bipersonales ($X_2$, utilidad $\$5.000$). Disponibilidad semanal de insumos: 300 m madera, 500 m ángulo metálico y 200 m paño.
  - Unipersonal: 2m madera, 3m ángulo, 1m paño.
  - Bipersonal: 3m madera, 5m ángulo, 4m paño.
- **Variables de Decisión:**
  - $X_1$: Cantidad de pupitres unipersonales a fabricar semanalmente [u/semana].
  - $X_2$: Cantidad de pupitres bipersonales a fabricar semanalmente [u/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 3000 X_1 + 5000 X_2 \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Madera:* $2X_1 + 3X_2 \le 300$
  2. *Ángulo:* $3X_1 + 5X_2 \le 500$
  3. *Paño:* $X_1 + 4X_2 \le 200$
  4. *No negatividad:* $X_1, X_2 \ge 0$

---

## Bloque 4: Dietas y Mezclas Físico-Químicas (*Blending*)

### Ejemplo 14: "Mi Dieta" – Consumo Diario de Golosinas (Págs. 72–105)
- **Resumen del Enunciado:** Minimizar el costo de una dieta basada en 4 golosinas: chocolate ($x_1$, 50¢), helado ($x_2$, 20¢), cola ($x_3$, 30¢) y pastel ($x_4$, 80¢). Requerimientos diarios: calorías $\ge 500$, chocolate $\ge 6\text{ oz}$, azúcar $\ge 10\text{ oz}$ y grasa $\ge 8\text{ oz}$.
- **Variables de Decisión:**
  - $x_1$: Barras de chocolate consumidas al día [barras/día].
  - $x_2$: Bolas de helado de chocolate ingeridas al día [bolas/día].
  - $x_3$: Botellas de bebida cola tomadas al día [botellas/día].
  - $x_4$: Rebanadas de pastel de queso consumidas al día [rebanadas/día].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 50x_1 + 20x_2 + 30x_3 + 80x_4 \quad [\text{centavos/día}]$$
- **Restricciones:**
  1. *Calorías:* $400x_1 + 200x_2 + 150x_3 + 500x_4 \ge 500$
  2. *Chocolate:* $3x_1 + 2x_2 \ge 6$
  3. *Azúcar:* $2x_1 + 2x_2 + 4x_3 + 4x_4 \ge 10$
  4. *Grasas:* $2x_1 + 4x_2 + x_3 + 5x_4 \ge 8$
  5. *No negatividad:* $x_j \ge 0 \quad (\forall j = 1, \dots, 4)$

---

### Ejemplo 15: Dietas en Jardín Infantil Cervecero (Págs. 106–108)
- **Resumen del Enunciado:** Alimentar a los niños con leche ($x_1$, $\$1000/\text{L}$), huevos ($x_2$, $\$150/\text{u}$) y compota ($x_3$, $\$600/\text{frasco}$). Requerimientos diarios por niño: calcio $\ge 25\text{ mg}$, hierro $\ge 15\text{ mg}$, vitaminas entre $24\text{ mg}$ y $30\text{ mg}$.
- **Variables de Decisión:**
  - $x_1$: Litros de leche por niño al día [L/niño-día].
  - $x_2$: Cantidad de huevos por niño al día [huevos/niño-día].
  - $x_3$: Frascos de compota por niño al día [frascos/niño-día].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 1000 x_1 + 150 x_2 + 600 x_3 \quad [\$/\text{niño-día}]$$
- **Restricciones:**
  1. *Calcio:* $2x_1 + 4x_2 + 6x_3 \ge 25$
  2. *Hierro:* $3x_1 + 5x_2 + x_3 \ge 15$
  3. *Vitaminas mínimo:* $x_1 + 3x_2 + 2x_3 \ge 24$
  4. *Vitaminas máximo:* $x_1 + 3x_2 + 2x_3 \le 30$
  5. *No negatividad:* $x_1, x_2, x_3 \ge 0$

---

### Ejemplo 16: Mezcla Siderúrgica – Horno de 2 Toneladas (Págs. 109–111)
- **Resumen del Enunciado:** Cargar un horno de $2.000\text{ kg}$ con hierro ($x_1$, $\$1000/\text{kg}$), tungsteno ($x_2$, $\$4000/\text{kg}$), níquel ($x_3$, $\$3000/\text{kg}$) y carbono ($x_4$, $\$3400/\text{kg}$). Requerimientos de la aleación: cobre entre 15% y 20%, fósforo máximo 17%.
- **Variables de Decisión:**
  - $x_1, x_2, x_3, x_4$: Kilogramos de hierro, tungsteno, níquel y carbono cargados al horno [kg].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 1000 x_1 + 4000 x_2 + 3000 x_3 + 3400 x_4 \quad [\$]$$
- **Restricciones:**
  1. *Capacidad total del horno:* $x_1 + x_2 + x_3 + x_4 = 2000$
  2. *Cobre mínimo (15%):* $0.07x_1 + 0.11x_2 + 0.19x_3 + 0.04x_4 \ge 300$
  3. *Cobre máximo (20%):* $0.07x_1 + 0.11x_2 + 0.19x_3 + 0.04x_4 \le 400$
  4. *Fósforo máximo (17%):* $0.09x_1 + 0.03x_2 + 0.08x_3 + 0.17x_4 \le 340$
  5. *No negatividad:* $x_j \ge 0 \quad (\forall j = 1, \dots, 4)$

---

### Ejemplo 17: Refinería de Petróleo Crudo y Refinado (Págs. 112–114)
- **Resumen del Enunciado:** Refinería elabora corriente ($j=1$, $\$4000/\text{gal}$), extra ($j=2$, $\$4500/\text{gal}$) y acpm ($j=3$, $\$4100/\text{gal}$) a partir de crudo ($i=1$, disp. 5000 gal, costo $\$3000$) y refinado ($i=2$, disp. 7000 gal, costo $\$3500$). Composiciones exactas de crudo: corriente 40%, extra 30%, acpm 50%.
- **Variables de Decisión:**
  - $x_{ij}$: Galones de producto $j$ obtenidos a partir del petróleo tipo $i$ [galones/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 1000 x_{11} + 500 x_{21} + 1500 x_{12} + 1000 x_{22} + 1100 x_{13} + 600 x_{23} \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Crudo disponible:* $x_{11} + x_{12} + x_{13} \le 5000$
  2. *Refinado disponible:* $x_{21} + x_{22} + x_{23} \le 7000$
  3. *Proporción Corriente (40% crudo / 60% refinado):* $0.60 x_{11} - 0.40 x_{21} = 0$
  4. *Proporción Extra (30% crudo / 70% refinado):* $0.70 x_{12} - 0.30 x_{22} = 0$
  5. *Proporción ACPM (50% crudo / 50% refinado):* $0.50 x_{13} - 0.50 x_{23} = 0$
  6. *No negatividad:* $x_{ij} \ge 0 \quad (\forall i \in \{1, 2\}, j \in \{1, 2, 3\})$

---

### Ejemplo 18: Mezcla de Combustibles ROMA (Págs. 115–117)
- **Resumen del Enunciado:** Produce gasolina blanca ($j=1$, $\$4800$), roja ($j=2$, $\$5100$) y ACPM ($j=3$, $\$4300$) usando Crudo A ($i=1$, disp. 3000 gal, costo $\$2500$) y Crudo B ($i=2$, disp. 4500 gal, costo $\$3200$). Calidades de Crudo A exigidas: blanca 30%, roja 35%, ACPM 60%.
- **Variables de Decisión:**
  - $X_{ij}$: Galones de combustible $j$ fabricados con crudo tipo $i$ [galones/semana].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 2300 X_{11} + 1600 X_{21} + 2600 X_{12} + 1900 X_{22} + 1800 X_{13} + 1100 X_{23} \quad [\$/\text{semana}]$$
- **Restricciones:**
  1. *Crudo A:* $X_{11} + X_{12} + X_{13} \le 3000$
  2. *Crudo B:* $X_{21} + X_{22} + X_{23} \le 4500$
  3. *Calidad Blanca:* $0.70 X_{11} - 0.30 X_{21} = 0$
  4. *Calidad Roja:* $0.65 X_{12} - 0.35 X_{22} = 0$
  5. *Calidad ACPM:* $0.40 X_{13} - 0.60 X_{23} = 0$
  6. *No negatividad:* $X_{ij} \ge 0$

---

### Ejemplo 19: Mezcla de Aleación Z a partir de 9 Aleaciones (Pág. 118)
- **Resumen del Enunciado:** Producir exactamente 1 kg de aleación Z con: 30% metal A, 30% metal B y 40% metal C, comprando entre 9 aleaciones comerciales disponibles de costo conocido al mínimo gasto total.
- **Variables de Decisión:**
  - $x_k$: Kilogramos de la aleación comercial $k$ ($k = 1, \dots, 9$) a utilizar [kg].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 82x_1 + 86x_2 + 116x_3 + 120x_4 + 152x_5 + 152x_6 + 146x_7 + 138x_8 + 146x_9 \quad [\$]$$
- **Restricciones:**
  1. *Masa total:* $\sum_{k=1}^9 x_k = 1$
  2. *Metal A (30%):* $0.10x_1 + 0.10x_2 + 0.40x_3 + 0.60x_4 + 0.30x_5 + 0.30x_6 + 0.30x_7 + 0.50x_8 + 0.20x_9 = 0.30$
  3. *Metal B (30%):* $0.10x_1 + 0.30x_2 + 0.50x_3 + 0.30x_4 + 0.30x_5 + 0.40x_6 + 0.20x_7 + 0.40x_8 + 0.30x_9 = 0.30$
  4. *Metal C (40%):* $0.80x_1 + 0.60x_2 + 0.10x_3 + 0.10x_4 + 0.40x_5 + 0.30x_6 + 0.50x_7 + 0.10x_8 + 0.50x_9 = 0.40$
  5. *No negatividad:* $x_k \ge 0 \quad (\forall k = 1, \dots, 9)$

---

## Bloque 5: Transporte, Redes y Asignación Regional

### Ejemplo 20: Transporte Embotelladora Cervecería (Págs. 119, 124–125)
- **Resumen del Enunciado:** 3 plantas de producción (Bogotá: 5000, Tocancipá: 3500, Barranquilla: 6000 cajas/semana) abastecen a 4 distribuidores (Pasto: 2000, Riohacha: 3200, Zipaquirá: 1700, Cali: 1800 cajas/semana) minimizando el costo de flete.
- **Variables de Decisión:**
  - $X_{ij}$: Cajas de cerveza enviadas de la planta $i$ ($1:\text{Bog}, 2:\text{Toc}, 3:\text{Bar}$) al distribuidor $j$ ($1:\text{Pas}, 2:\text{Rio}, 3:\text{Zip}, 4:\text{Cal}$) [cajas/semana].
- **Función Objetivo:**
  $$\begin{aligned}
  \operatorname{Min} Z = & \ 75X_{11} + 90X_{12} + 9X_{13} + 67X_{14} + 78X_{21} + 85X_{22} + 4X_{23} + 65X_{24} \\
  & + 150X_{31} + 17X_{32} + 65X_{33} + 147X_{34} \quad [\$/\text{semana}]
  \end{aligned}$$
- **Restricciones:**
  1. *Capacidad plantas:* $\sum_{j=1}^4 X_{1j} \le 5000, \quad \sum_{j=1}^4 X_{2j} \le 3500, \quad \sum_{j=1}^4 X_{3j} \le 6000$
  2. *Demanda distribuidores:* $\sum_{i=1}^3 X_{i1} = 2000, \; \sum_{i=1}^3 X_{i2} = 3200, \; \sum_{i=1}^3 X_{i3} = 1700, \; \sum_{i=1}^3 X_{i4} = 1800$
  3. *No negatividad:* $X_{ij} \ge 0$

---

### Ejemplo 21: Planeación Agrícola – Confederación Sur de Kibbutzim (Págs. 120–123)
- **Resumen del Enunciado:** Tres kibbutzim (1: 400 acres, 600 pies-acre agua; 2: 600 acres, 800 agua; 3: 300 acres, 375 agua) cultivan remolacha ($x_1, x_2, x_3$, rend. $\$1000$, agua 3, cuota 600 acres), algodón ($x_4, x_5, x_6$, rend. $\$750$, agua 2, cuota 500 acres) y sorgo ($x_7, x_8, x_9$, rend. $\$250$, agua 1, cuota 325 acres). Se impone que cada kibbutz siembre la misma proporción de su tierra irrigable.
- **Variables de Decisión:**
  - $x_1, x_2, x_3$: Acres de remolacha en kibbutz 1, 2, 3 [acres].
  - $x_4, x_5, x_6$: Acres de algodón en kibbutz 1, 2, 3 [acres].
  - $x_7, x_8, x_9$: Acres de sorgo en kibbutz 1, 2, 3 [acres].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 1000(x_1+x_2+x_3) + 750(x_4+x_5+x_6) + 250(x_7+x_8+x_9) \quad [\$]$$
- **Restricciones:**
  1. *Tierra por kibbutz:* $x_1+x_4+x_7 \le 400; \; x_2+x_5+x_8 \le 600; \; x_3+x_6+x_9 \le 300$
  2. *Agua por kibbutz:* $3x_1+2x_4+x_7 \le 600; \; 3x_2+2x_5+x_8 \le 800; \; 3x_3+2x_6+x_9 \le 375$
  3. *Cuotas máximas cultivo:* $\sum_{k=1}^3 x_k \le 600; \; \sum_{k=4}^6 x_k \le 500; \; \sum_{k=7}^9 x_k \le 325$
  4. *Equidad proporcional:* $\frac{x_1+x_4+x_7}{400} = \frac{x_2+x_5+x_8}{600} = \frac{x_3+x_6+x_9}{300}$
  5. *No negatividad:* $x_k \ge 0 \quad (\forall k = 1, \dots, 9)$

---

### Ejemplo 22: Distribución Multiatributo – Manufacturera de Computadores (Págs. 126–128)
- **Resumen del Enunciado:** 3 plantas (I: 1000 u, costo $\$7000$; II: 1200 u, costo $\$9500$; III: 597 u, costo $\$7200$) distribuyen a 4 clientes (A: $\$10000$; B: $\$15000$; C: $\$14000$; D: $\$18000$). Costos de transporte unitarios conocidos. Demanda conjunta A y B $\ge 600$; C $\le 550$; D entre 310 y 380 unidades. Se busca maximizar la utilidad neta.
- **Variables de Decisión:**
  - $X_{ij}$: Equipos producidos en planta $i$ y enviados a distribuidor $j$ [unidades/mes].
- **Función Objetivo:**
  $$\operatorname{Max} Z = \sum_{i=1}^3 \sum_{j=1}^4 (P_j - CP_i - CT_{ij}) X_{ij} \quad [\$/\text{mes}]$$
- **Restricciones:**
  1. *Capacidades:* $\sum_{j=1}^4 X_{1j} \le 1000; \; \sum_{j=1}^4 X_{2j} \le 1200; \; \sum_{j=1}^4 X_{3j} \le 597$
  2. *Demanda A y B conjunta:* $\sum_{i=1}^3 X_{i1} + \sum_{i=1}^3 X_{i2} \ge 600$
  3. *Demanda C máxima:* $\sum_{i=1}^3 X_{i3} \le 550$
  4. *Demanda D rango:* $310 \le \sum_{i=1}^3 X_{i4} \le 380$
  5. *No negatividad:* $X_{ij} \ge 0$

---

### Ejemplo 23: Logística Compañía JOTA de Computadores (Págs. 129–131)
- **Resumen del Enunciado:** Plantas en Bogotá (3000 u), Cali (1500 u) y Barranquilla (4000 u) envían a Medellín (demanda 3200 u) y Pasto (demanda 5700 u). Costos de flete conocidos. Minimizar costo total de envío.
- **Variables de Decisión:**
  - $X_{ij}$: Equipos enviados de la planta $i$ al distribuidor $j$ [u/semana].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 3000 X_{11} + 5000 X_{12} + 2500 X_{21} + 3900 X_{22} + 2100 X_{31} + 7000 X_{32} \quad [\$]$$
- **Restricciones:**
  1. *Capacidades de oferta:* $X_{11}+X_{12} \le 3000; \; X_{21}+X_{22} \le 1500; \; X_{31}+X_{32} \le 4000$
  2. *Demanda:* $X_{11}+X_{21}+X_{31} = 3200; \; X_{12}+X_{22}+X_{32} = 5700$
  3. *No negatividad:* $X_{ij} \ge 0$

---

## Bloque 6: Personal, Horarios, Finanzas y Holguras

### Ejemplo 24: Personal Multiperíodo – Asistentes de Vuelo en 6 Meses (Págs. 132–135)
- **Resumen del Enunciado:** Demanda mensual de horas-vuelo: Ene: 8000, Feb: 9000, Mar: 8000, Abr: 10000, May: 9000, Jun: 12000. Entrenamiento dura 1 mes y cada aprendiz consume 100 horas de supervisión por una experimentada (150h/mes disponibles). Se inicia enero con 60 experimentadas. Al final de cada mes se retira el 10% de experimentadas. Costo: $\$800/\text{mes}$ por experimentada y $\$400/\text{mes}$ por aprendiz.
- **Variables de Decisión:**
  - $Y_t$: Asistentes experimentadas al inicio del mes $t$ ($t = 1, \dots, 6$) [asistentes].
  - $X_t$: Asistentes aprendices contratadas al inicio del mes $t$ ($t = 1, \dots, 6$) [asistentes].
- **Función Objetivo:**
  $$\operatorname{Min} Z = 800 \sum_{t=1}^6 Y_t + 400 \sum_{t=1}^6 X_t \quad [\$]$$
- **Restricciones:**
  1. *Demanda horas de vuelo:* $150 Y_t - 100 X_t \ge \text{Demanda}_t \quad (\forall t = 1, \dots, 6)$
  2. *Condición inicial:* $Y_1 = 60$
  3. *Balance de personal intermensual (deserción 10%):* $0.9 Y_t + X_t = Y_{t+1} \quad (\forall t = 1, \dots, 5)$
  4. *No negatividad e integralidad:* $Y_t, X_t \ge 0, \; Y_t, X_t \in \mathbb{Z}^+$

---

### Ejemplo 25: Asignación Biyectiva – Alcaldía de Bogotá (Págs. 136–138)
- **Resumen del Enunciado:** Asignar 4 proyectos urbanos (Parque, Edificio, Puente, Túnel) a 4 constructoras (Colmena, Conavi, Villas, Davivienda) con matriz de costos ofertados conocida. Cada contratista debe recibir exactamente un proyecto y cada proyecto debe asignarse una sola vez.
- **Variables de Decisión:**
  - $X_{ij}$: Variable binaria (1 si se asigna el proyecto $i$ al contratista $j$, 0 en caso contrario).
- **Función Objetivo:**
  $$\operatorname{Min} Z = \sum_{i=1}^4 \sum_{j=1}^4 C_{ij} X_{ij} \quad [\$]$$
- **Restricciones:**
  1. *Un contratista por proyecto:* $\sum_{j=1}^4 X_{ij} = 1 \quad (\forall i = 1, \dots, 4)$
  2. *Un proyecto por contratista:* $\sum_{i=1}^4 X_{ij} = 1 \quad (\forall j = 1, \dots, 4)$
  3. *Naturaleza binaria / No negatividad:* $X_{ij} \ge 0 \quad (\text{garantiza } X_{ij} \in \{0, 1\})$

---

### Ejemplo 26: Turnos Solapados – Policía Antonio Nariño (Págs. 139–142)
- **Resumen del Enunciado:** Cobertura de 24 horas en 6 bloques de 4 horas: 00-04h (40 agentes), 04-08h (25), 08-12h (100), 12-16h (80), 16-20h (60) y 20-24h (45). Turnos de 8 horas consecutivas.
- **Variables de Decisión:**
  - $X_k$: Agentes de policía que inician su turno en el bloque $k$ ($k = 1, \dots, 6$) [policías].
- **Función Objetivo:**
  $$\operatorname{Min} Z = X_1 + X_2 + X_3 + X_4 + X_5 + X_6 \quad [\text{policías}]$$
- **Restricciones:**
  1. *Turno 1 (00–04h):* $X_1 \ge 40$
  2. *Turno 2 (04–08h):* $X_1 + X_2 \ge 25$
  3. *Turno 3 (08–12h):* $X_2 + X_3 \ge 100$
  4. *Turno 4 (12–16h):* $X_3 + X_4 \ge 80$
  5. *Turno 5 (16–20h):* $X_4 + X_5 \ge 60$
  6. *Turno 6 (20–24h):* $X_5 + X_6 \ge 45$
  7. *No negatividad e integralidad:* $X_k \ge 0, \; X_k \in \mathbb{Z}^+$

---

### Ejemplo 27: Turnos Solapados – Defensa Civil (Págs. 143–145)
- **Resumen del Enunciado:** Requerimientos en bloques de 4 horas: 00-04h (20 voluntarios), 04-08h (25), 08-12h (15), 12-16h (12), 16-20h (18) y 20-24h (30). Turnos continuos de 8 horas.
- **Variables de Decisión:**
  - $X_k$: Voluntarios que inician labores al comienzo del bloque horario $k$ [voluntarios].
- **Función Objetivo:**
  $$\operatorname{Min} Z = X_1 + X_2 + X_3 + X_4 + X_5 + X_6 \quad [\text{voluntarios}]$$
- **Restricciones:**
  1. *Bloque 1:* $X_1 \ge 20$
  2. *Bloque 2:* $X_1 + X_2 \ge 25$
  3. *Bloque 3:* $X_2 + X_3 \ge 15$
  4. *Bloque 4:* $X_3 + X_4 \ge 12$
  5. *Bloque 5:* $X_4 + X_5 \ge 18$
  6. *Bloque 6:* $X_5 + X_6 \ge 30$
  7. *No negatividad e integralidad:* $X_k \ge 0, \; X_k \in \mathbb{Z}^+$

---

### Ejemplo 28: Préstamo Bancario y Riesgo Crediticio – Bank One (Págs. 146–150)
- **Resumen del Enunciado:** Bank One dispone de hasta $\$12\text{ millones}$ para 5 líneas de crédito: Personal (14% interés, 10% mora), Automóvil (13%, 7% mora), Casa (12%, 3% mora), Agrícola (12.5%, 5% mora) y Comercial (10%, 2% mora). La cartera morosa se pierde en su totalidad y no devenga intereses. Agrícola + Comercial deben ser al menos 40% del total prestado. Préstamos de casa deben ser al menos 50% de (personal + automóvil + casa). La morosidad global no puede superar el 4%.
- **Variables de Decisión:**
  - $x_1$: Préstamos personales [millones USD].
  - $x_2$: Préstamos de automóvil [millones USD].
  - $x_3$: Préstamos de casa [millones USD].
  - $x_4$: Préstamos agrícolas [millones USD].
  - $x_5$: Préstamos comerciales [millones USD].
- **Función Objetivo:**
  $$\operatorname{Max} Z = \text{Interés cobrado} - \text{Deuda impagable} = 0.026 x_1 + 0.0509 x_2 + 0.0864 x_3 + 0.06875 x_4 + 0.078 x_5$$
- **Restricciones:**
  1. *Presupuesto prestable:* $x_1 + x_2 + x_3 + x_4 + x_5 \le 12$
  2. *Cuota agrícola y comercial ($\ge 40\%$):* $0.4x_1 + 0.4x_2 + 0.4x_3 - 0.6x_4 - 0.6x_5 \le 0$
  3. *Fomento vivienda ($\ge 50\%$ de pers + auto + casa):* $0.5x_1 + 0.5x_2 - 0.5x_3 \le 0$
  4. *Riesgo de morosidad global ($\le 4\%$):* $0.06x_1 + 0.03x_2 - 0.01x_3 + 0.01x_4 - 0.02x_5 \le 0$
  5. *No negatividad:* $x_j \ge 0 \quad (\forall j = 1, \dots, 5)$

---

### Ejemplo 29: Producción con Penalización por Faltantes – Ropa Invernal (Págs. 151–154)
- **Resumen del Enunciado:** Fabricar chamarras con capucha ($x_1$, margen $\$30$, faltante $-\$15$, pedido 800), chamarras de plumas ($x_2$, margen $\$40$, faltante $-\$20$, pedido 750), pantalones ($x_3$, margen $\$20$, faltante $-\$10$, pedido 600) y guantes ($x_4$, margen $\$10$, faltante $-\$8$, pedido 500). Capacidad de 1000 horas en 4 talleres: corte, aislamiento, costura y empaque. Si la demanda no se cubre, se incurre en penalización por unidad insatisfecha ($s_j$).
- **Variables de Decisión:**
  - $x_j$: Prendas confeccionadas del producto $j$ en el período [unidades].
  - $s_j$: Unidades no surtidas / faltantes de demanda del producto $j$ [unidades].
- **Función Objetivo:**
  $$\operatorname{Max} Z = 30x_1 + 40x_2 + 20x_3 + 10x_4 - (15s_1 + 20s_2 + 10s_3 + 8s_4) \quad [\$]$$
- **Restricciones:**
  1. *Corte:* $0.30x_1 + 0.30x_2 + 0.25x_3 + 0.15x_4 \le 1000$
  2. *Aislamiento:* $0.25x_1 + 0.35x_2 + 0.30x_3 + 0.10x_4 \le 1000$
  3. *Costura:* $0.45x_1 + 0.50x_2 + 0.40x_3 + 0.22x_4 \le 1000$
  4. *Empaque:* $0.15x_1 + 0.15x_2 + 0.10x_3 + 0.05x_4 \le 1000$
  5. *Balance demanda y déficit:*
     $$x_1 + s_1 = 800, \quad x_2 + s_2 = 750, \quad x_3 + s_3 = 600, \quad x_4 + s_4 = 500$$
  6. *No negatividad:* $x_j \ge 0, \; s_j \ge 0 \quad (\forall j = 1, \dots, 4)$
