# Guía Integral: Inteligencias Artificiales de Decisión (Modelos System 1)

---

## 1. Fundamentos y Cambio de Paradigma

Los **modelos de decisión de IA** (o modelos *System 1*) representan un cambio en la arquitectura de software de inteligencia artificial: abandonan la generación abierta de texto token a token para especializarse en resolver **juicios semánticos discretos, tipados y delimitados** a ultra-baja latencia y con un costo computacional mínimo.

### El problema del enfoque generativo tradicional (System 2)
Hasta ahora, resolver tareas como clasificar un ticket, moderar un mensaje o seleccionar una herramienta implicaba forzar a un LLM conversacional a generar texto:
* **Latencia secuencial innecesaria:** Un LLM estándar evalúa y genera tokens de manera secuencial. Incluso con *Structured Outputs* (esquemas JSON forzados), el motor debe decodificar comillas, llaves y campos sintácticos, elevando los tiempos de respuesta a rangos de 1 a 4 segundos.
* **Costo por tokens de salida:** Los proveedores cobran por cada token emitido, encareciendo operaciones de alta frecuencia donde solo se requería una etiqueta o un booleano.
* **Falta de probabilidades matemáticas nativas:** Los LLMs emiten texto que aparenta confianza, pero no exponen de manera nativa una distribución de probabilidad matemática real sobre un espacio finito de opciones.

### Principios de los modelos de decisión (System 1)
1. **Espacio cerrado a priori:** El software define las respuestas válidas (`Choice`, `Predicate`, `Score`) antes de la inferencia; es estructuralmente imposible que el modelo alucine una categoría fuera del esquema.
2. **Evaluación paralela en una sola pasada:** No hay generación token a token. El modelo procesa la evidencia y evalúa las preguntas de forma directa y paralela.
3. **Distribución matemática calibrada:** Cada respuesta incluye un valor de confianza o distribución de probabilidad real (de 0.0 a 1.0), lo que permite fijar umbrales deterministas para automatizar o derivar a revisión.
4. **Cero costo de salida:** Al no emitir prosa ni JSON arbitrario, los tokens de salida no tienen costo ($0.00/M).

```
Flujo Tradicional (LLM Generativo):
Input ──> Decodificación token a token (JSON) ──> Parseo sintáctico ──> Manejo de alucinaciones

Flujo de Decisión (System 1):
Input + Contrato cerrado ──> Evaluación paralela directa ──> Valor tipado + Distribución probabilística
```

---

## 2. Proveedores y Modelos Principales

### 2.1 TypeSafe AI — Jev (`jev-1.13`)
Jev es el primer modelo público concebido desde su base exclusivamente como un **modelo nativo System 1**, entrenado íntegramente con datos sintéticos para procesar estados desestructurados contra esquemas tipados.

* **Primitivas base:**
  * `Choice`: Selección categórica dentro de un catálogo predefinido (hasta 255 opciones).
  * `Score`: Ubicación de la entrada sobre una rúbrica u escala ordenada (hasta 10 niveles).
  * `Noul`: Predicado booleano que devuelve la probabilidad matemática calibrada (0.0 a 1.0) de que una afirmación sea verdadera.
* **Rendimiento:** Latencias de **70 a 500 ms**.
* **Precios:** **$0.042 por millón de tokens de entrada** / **$0.00 por tokens de salida**.
* **Garantía estructural:** El espacio de respuesta está acotado matemáticamente por el contrato previo a la llamada; no emite texto libre.

### 2.2 OpenAI — Decisions API (`gpt-6-luna`)
Presentada en el DevDay, la Decisions API de OpenAI implementa una **capa de interfaz acotada** sobre su modelo base general (GPT-6 Luna).

* **Mecanismo:** La llamada recibe un bloque de evidencia (texto, JSON o imágenes) y un arreglo de preguntas tipadas (`predicate`, `choice`, `score`).
* **Métricas:** Devuelve la opción elegida, la distribución de probabilidades entre las alternativas y un índice de confianza.
* **Diferencia con Structured Outputs:** *Structured Outputs* sigue generando texto secuencial restringido a un esquema JSON en el motor de chat. La Decisions API prescinde del diseño de documentos de salida y evalúa directamente las preguntas en la capa de decisión.

### 2.3 Liquid AI — Liquid `d1`
Modelo nativo System 1 enfocado en inferencia ultrarrápida y multimodalidad.
* **Características:** Sin tokens de salida ($0.04/M entrada, $0.00 salida), evaluación calibrada de opciones y booleanos.
* **Soporte de visión:** Permite evaluar imágenes nativamente frente a preguntas de clasificación, control de calidad o moderación sin requerir un VLM generativo pesado.
* **Disponibilidad:** Disponible vía API propia y a través del endpoint estándar `/v1/systemone` en OpenRouter.

### 2.4 Command Code — `Agr` y `Agr-flash` (Pesos Abiertos)
Familia de modelos abiertos disponibles en Hugging Face para despliegues locales y autosoportados (*self-hosted*).
* **Variantes:**
  * `Agr` (31B): Orientado a máxima precisión en sistemas agentic complejos.
  * `Agr-flash` (360M): Ultraligero, diseñado para correr localmente en CPU/edge a latencias sub-50ms.
* **Enfoque:** Diseñados específicamente para orquestación de agentes (selección de herramientas / *tool routing* y bifurcación condicional en pipelines de código).

---

## 3. Estado del Ecosistema: Nativos vs. Adaptadores

| Proveedor | Modelo / Endpoint | Tipo de Implementación | Probabilidades Reales | Ejecución Local / Self-hosted |
| :--- | :--- | :--- | :--- | :--- |
| **TypeSafe AI** | Jev (`jev-1.13`) | Nativo (*System 1* dedicado) | Sí (Calibradas) | No (Solo API) |
| **OpenAI** | Decisions API (`gpt-6-luna`) | Nativo (Capa de decisión en endpoint) | Sí (Distribución + confianza) | No (Solo API) |
| **Liquid AI** | Liquid `d1` | Nativo (*System 1* con visión) | Sí (Nativas) | No (API / OpenRouter) |
| **Command Code** | `Agr` (31B) / `Agr-flash` (360M) | Nativo (*Open weights*) | Sí (Nativas) | **Sí** (Hugging Face) |
| **Google** | Gemini Flash-Lite vía AI SDK | Adaptador (LLM generativo + JSON) | No (Aproximación en texto) | No |
| **Anthropic** | Claude Haiku vía AI SDK | Adaptador (LLM generativo + JSON) | No (Aproximación en texto) | No |
| **DeepSeek** | No implementado | Ninguno (Enfoque en *System 2* / R1) | N/A | N/A |
| **xAI (Grok)** | No implementado | Ninguno (Modelos generativos/multimodales) | N/A | N/A |

### ¿Cómo funcionan los adaptadores de Google y Anthropic?
Ni Google ni Anthropic han lanzado endpoints nativos System 1. Frameworks como el AI SDK de Vercel permiten utilizarlos mediante adaptadores sobre sus modelos más rápidos (`gemini-3.5-flash-lite` y `claude-haiku-4-5`). Estos adaptadores empaquetan las preguntas en un único prompt tradicional con instrucciones de formato JSON estricto y desactivan el razonamiento (`reasoning: none`). Aunque son rápidos para el estándar de un LLM, mantienen la sobrecarga de emitir tokens secuenciales y pagan el costo de salida.

---

## 4. Frameworks de Integración

* **Vercel AI SDK (`experimental_decide`):** Capa unificada multimodelo. Permite alternar entre proveedores (`typesafe-ai/jev`, `openai`, adaptadores) y aplicar reglas de enrutamiento con fallbacks condicionales en el *AI Gateway* si la confianza es baja.
* **Pydantic AI (`DecisionModel`):** Separa la lógica de orquestación en agentes: un modelo System 1 decide qué herramientas invocar o si cerrar un ciclo, reservando los LLMs generativos únicamente para redactar el texto final.
* **Perplexity Decisions API:** Orientado al enrutamiento semántico de intenciones de búsqueda y filtrado de fuentes en pipelines de recuperación (RAG).

---

## 5. Guía de Uso e Implementación

### 5.1 Implementación en Python con OpenAI Decisions API

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Entrada a evaluar (puede ser texto, JSON o imágenes)
ticket = "Mi tarjeta fue cobrada dos veces en el pedido #104. ¡Devuélvanme el dinero ya!"

response = client.decisions.create(
    model="gpt-6-luna",
    input=ticket,
    questions=[
        {
            "name": "area_destino",
            "type": "choice",
            "instructions": "¿A qué departamento debe derivarse este ticket?",
            "options": [
                {"id": "facturacion", "description": "Cargos dobles, pagos, reembolsos o facturas"},
                {"id": "soporte_tecnico", "description": "Fallas en la aplicación o cuenta bloqueada"},
                {"id": "otros", "description": "Cualquier consulta general o no contemplada"}
            ]
        },
        {
            "name": "es_urgente",
            "type": "predicate",
            "instructions": "¿El cliente expresa reclamos de dinero o alta urgencia?"
        },
        {
            "name": "gravedad",
            "type": "score",
            "instructions": "Nivel de gravedad del reclamo",
            "levels": ["Bajo", "Moderado", "Crítico"]
        }
    ]
)

# Consumo directo de la respuesta tipada
print("Área elegida:", response.answers["area_destino"].value)
print("Confianza:", response.answers["area_destino"].confidence)
print("Probabilidad de urgencia:", response.answers["es_urgente"].probability)
print("Nivel de gravedad:", response.answers["gravedad"].score)
```

---

### 5.2 Implementación en Python con TypeSafe AI (Jev vía HTTP)

```python
import os
import httpx

api_key = os.environ.get("TYPESAFE_API_KEY")

payload = {
    "model": "jev-1.13.0",
    "state": "Mi tarjeta fue cobrada dos veces en el pedido #104. ¡Devuélvanme el dinero ya!",
    "questions": {
        "enrutamiento": {
            "type": "choice",
            "instructions": "Selecciona el equipo responsable.",
            "criteria": {
                "facturacion": "Cobros duplicados, reembolsos y pagos",
                "soporte": "Errores técnicos o bugs del sistema",
                "general": "Otras dudas generales"
            }
        },
        "reclamo_financiero": {
            "type": "noul",
            "instructions": "¿El mensaje reclama una pérdida económica?",
            "criteria": {
                "true": "El usuario reclama cobro indebido o exige reembolso",
                "false": "No hay disputa de dinero"
            }
        }
    }
}

response = httpx.post(
    "[https://api.typesafe.ai/v1/systemone](https://api.typesafe.ai/v1/systemone)",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json=payload
)

data = response.json()

# Jev resuelve todas las preguntas en paralelo en una sola pasada (~100 ms)
print("Resultado enrutamiento:", data["answers"]["enrutamiento"]["value"])
print("Probabilidades:", data["answers"]["enrutamiento"]["probabilities"])
print("Probabilidad reclamo:", data["answers"]["reclamo_financiero"]["probability"])
```

---

### 5.3 Implementación Unificada en TypeScript con Vercel AI SDK

```typescript
import { experimental_decide as decide } from 'ai';

interface ResultadoTicket {
  categoria: string;
  requiereRevisionHumana: boolean;
}

async function procesarTicket(textoEntrada: string): Promise<ResultadoTicket> {
  const result = await decide({
    model: 'typesafe/jev-1.13.0', // Alternativa: 'openai/gpt-6-luna-decisions'
    state: textoEntrada,
    questions: {
      categoria: {
        type: 'choice',
        options: ['facturacion', 'soporte_tecnico', 'general']
      },
      fraude_potencial: {
        type: 'predicate',
        instructions: '¿El reporte sugiere suplantación de identidad o actividad fraudulenta?'
      }
    }
  });

  const categoria = result.answers.categoria.value;
  const riesgoFraude = result.answers.fraude_potencial.probability;
  const confianza = result.answers.categoria.confidence;

  // Lógica de automatización determinista basada en umbrales matemáticos
  const requiereRevisionHumana = riesgoFraude > 0.70 || confianza < 0.85;

  return {
    categoria,
    requiereRevisionHumana
  };
}
```

---

## 6. Arquitectura de Decisión y Control en Producción

El principio de diseño fundamental en este paradigma es la **separación estricta de responsabilidades**: el modelo de decisión aporta criterio probabilístico y semántico, pero la lógica determinista del software retiene el control de ejecución.

```
                  ┌──────────────────────────────┐
                  │    Entrada No Estructurada   │
                  │   (Texto, JSON o Imágenes)   │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
                  ┌──────────────────────────────┐
                  │      Modelo de Decisión      │
                  │       (System 1 / Jev)       │
                  └──────────────┬───────────────┘
                                 │
                     Valores Tipados + Certeza
                                 │
                                 ▼
                       ¿Confianza ≥ Umbral?
                          (ej. ≥ 0.85)
                                 │
                ┌────────────────┴────────────────┐
                │                                 │
              [ SÍ ]                            [ NO ]
                │                                 │
                ▼                                 ▼
  ┌───────────────────────────┐     ┌───────────────────────────┐
  │   Ejecución Determinista  │     │   Escalamiento / Fallback │
  │   - Disparo de Webhook    │     │   - Modelo System 2 (LLM) │
  │   - Enrutamiento directo  │     │   - Cola de revisión      │
  │   - Escritura en DB       │     │     humana manual         │
  └───────────────────────────┘     └───────────────────────────┘
```

Esta arquitectura previene ejecuciones imprevistas de agentes ante entradas ambiguas, manteniendo tiempos de respuesta de decenas de milisegundos para los casos determinables y reservando los recursos computacionales pesados únicamente para las excepciones.