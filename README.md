# Sistema multiagente de soporte con LangChain + Langfuse — Proyecto Integrador M3 (AI Engineering, Henry)

Un **Agente Orquestador** clasifica la intención de cada consulta de soporte interno de **Nimbus Cloud** (una empresa SaaS ficticia) y la **delega de forma condicional** al **Agente RAG especializado** correcto —**RR.HH.**, **Soporte Técnico** o **Finanzas**—, que responde únicamente con la documentación de su dominio. Todo el flujo está implementado con **LangChain (LCEL)** y queda **trazado completo en Langfuse**. Como bonus, un **Agente Evaluador** puntúa cada respuesta de 1 a 10 y registra el puntaje en la traza con la **Score API** de Langfuse.

**Problema que resuelve:** en soporte, muchas consultas se enrutan mal (preguntas de RR.HH. que terminan en IT, consultas financieras que llegan a Legal). Este sistema clasifica automáticamente, responde con conocimiento específico por área (reduciendo alucinaciones), permite depurar cada enrutamiento errado mirando su traza y detecta respuestas de baja calidad antes de que lleguen al cliente.

```
consulta ─► [Orquestador] ─► RunnableBranch ─┬─► [Agente HR]       ─┐
            (clasifica,      (ruteo           ├─► [Agente TECH]     ─┼─► respuesta ─► [Evaluador] ─► Score API
             1..3 rutas)      condicional,    ├─► [Agente FINANCE]  ─┘                 (1-10)        (Langfuse)
                              en paralelo)    └─► [Fallback OUT_OF_SCOPE]
                       └──────────── todo en UNA traza de Langfuse ────────────┘
```

## Estructura del repositorio

```
.
├── multi_agent_system.ipynb     # Notebook principal (6 secciones, ejecutado con salidas)
├── src/
│   ├── multi_agent_system.py    # Sistema completo: orquestación + routing + evaluación
│   ├── agents/
│   │   ├── orchestrator.py      # Orquestador: clasificación de intención (salida estructurada)
│   │   ├── rag_agent.py         # Agente RAG genérico (cadena LCEL: retriever → prompt → LLM)
│   │   ├── hr_agent.py          # Especialista RR.HH.
│   │   ├── tech_agent.py        # Especialista Tecnología / IT
│   │   └── finance_agent.py     # Especialista Finanzas
│   ├── knowledge_base.py        # Carga de documentos, chunking y vector stores (Chroma)
│   ├── evaluator.py             # (BONUS) Agente evaluador + Score API de Langfuse
│   ├── tracing.py               # Integración con Langfuse (traza raíz, callbacks, metadata)
│   └── config.py                # Configuración y variables de entorno
├── data/
│   ├── hr_docs/                 # 5 documentos → 144 chunks
│   ├── tech_docs/               # 5 documentos → 123 chunks
│   └── finance_docs/            # 5 documentos → 114 chunks
├── test_queries.json            # 14 consultas de prueba con categoría esperada
├── run_tests.py                 # Ejecuta las pruebas y mide routing + calidad
├── outputs/                     # Resultados reales de las corridas (test_results.json, notebook_results.json)
├── requirements.txt
├── .env.example
└── .gitignore
```

## Instalación

Requiere **Python 3.11+**, una cuenta de **OpenAI** (API key) y una cuenta gratuita de **Langfuse** (https://cloud.langfuse.com).

```bash
git clone <URL_DE_ESTE_REPO>
cd multi-agent-support-router
python -m venv .venv
# Windows: .venv\Scripts\activate      |  macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

### Configurar las API keys

```bash
cp .env.example .env      # en Windows: copy .env.example .env
```

Editá `.env` y completá:

| Variable | De dónde sale |
|---|---|
| `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | Langfuse → Project Settings → API Keys → *Create new API key* |
| `LANGFUSE_HOST` | `https://cloud.langfuse.com` (o tu instancia self-hosted) |

> El `.env` está en `.gitignore`: **nunca** se sube al repositorio. Si faltan las claves de Langfuse, el sistema funciona igual pero **sin trazas** (muestra un aviso).

## Cómo ejecutar

### Opción A — Notebook (recomendada)
```bash
jupyter notebook multi_agent_system.ipynb
```
Ejecutá las celdas **de arriba hacia abajo**, en orden:

| Sección | Qué hace | Celdas |
|---|---|---|
| 1. Setup e imports | Carga `.env` y verifica configuración | 1ª celda de código |
| 2. Documentos y vector stores | Cuenta chunks por dominio (mín. 50) y muestra un chunk | 2ª–3ª |
| 3. Definición de agentes | Construye vector stores (la primera vez calcula embeddings) y agentes | 4ª |
| 4. Orquestador y routing | Muestra el prompt de clasificación y prueba el ruteo | 5ª–6ª |
| 5. Pruebas y ejemplos | Corre las 14 consultas de `test_queries.json` | 7ª–9ª |
| 6. Langfuse + evaluador | Resume calidad, trazas y guarda resultados | 10ª–12ª |

### Opción B — Línea de comandos
```bash
python run_tests.py              # corre las 14 consultas; imprime routing y calidad
python run_tests.py --no-eval    # sin evaluador (más rápido/barato)
python run_tests.py --rebuild    # reconstruye los vector stores
```
```python
# Uso programático
from src.multi_agent_system import SupportSystem
system = SupportSystem()
out = system.answer("¿Cuántos días de vacaciones me corresponden tras un año de antigüedad?")
print(out["routing"], out["answer"], out["evaluation"]["overall"], out["trace_url"])
```

## Resultados reales (corrida incluida en `outputs/`)

Corrida real con OpenAI (`gpt-4o-mini`) y Langfuse Cloud sobre las 14 consultas de `test_queries.json` (detalle completo en `outputs/test_results.json`; la corrida del notebook, en `outputs/notebook_results.json`):

| Métrica | Resultado |
|---|---|
| Ruteo correcto (intención elegida = esperada) | **14 / 14 (100 %)** |
| Calidad promedio del evaluador (1-10) | **9.2** sobre 12 respuestas RAG |
| Consultas fuera de alcance manejadas con fallback | 2 / 2 (receta de milanesa y "ayuda") |
| Consulta multi-área (sueldos + VPN) | HR/Finanzas + Tecnología en paralelo, una sola respuesta |
| Consulta en inglés | enrutada correctamente a Tecnología |

| # | Tipo | Esperado | Elegido | Calidad |
|---|---|---|---|---|
| 1 | directa | hr | HR | 10 |
| 2 | directa | hr | HR | 9 |
| 3 | directa | tech | TECH | 10 |
| 4 | directa | tech | TECH | 9 |
| 5 | directa | finance | FINANCE | 9 |
| 6 | directa | finance | FINANCE | 9 |
| 7 | directa | tech | TECH | 9 |
| 8 | directa | hr | HR | 10 |
| 9 | multi-dominio | finance + tech | FINANCE, TECH | 10 |
| 10 | redacción de portal | hr | HR | 9 |
| 11 | ambigua | finance | FINANCE | 7 |
| 12 | fuera de alcance | out_of_scope | OUT_OF_SCOPE | - |
| 13 | idioma inglés | tech | TECH | 10 |
| 14 | vaga ("ayuda") | out_of_scope | OUT_OF_SCOPE | - |

### Mejora iterativa (ciclo de la lección de tracing)

La **primera corrida dio 13/14**. Al abrir la traza del caso #10 (duelo + "cargo el pedido en el portal") se vio que el orquestador devolvía dos rutas: `HR` y `OUT_OF_SCOPE` (tomaba "el portal" como tema de IT). Se corrigió en dos niveles: (1) reglas más explícitas en el prompt del orquestador (los procedimientos en el portal pertenecen al área dueña del trámite; `OUT_OF_SCOPE` solo puede ir sola) y (2) una guarda en código (`_merge_routes`) que descarta `OUT_OF_SCOPE` cuando hay áreas reales y fusiona rutas duplicadas. Re-corrida con el mismo dataset: **14/14**. Esa es la lógica del *golden dataset*: cada cambio se mide contra las mismas consultas (`run_tag` = `golden-run-v1`).

## Decisiones técnicas

**Arquitectura multiagente (roles claros).** El orquestador *solo clasifica* (no responde) y cada agente es experto en un único dominio con su propia base de conocimiento. Esto da mayor precisión por dominio, aísla fallas (un problema en Finanzas no afecta a Soporte Técnico) y permite agregar un nuevo agente sin rediseñar el sistema.

**Por qué LangChain (LCEL) y no `initialize_agent`.** El curso muestra el patrón con `initialize_agent(AgentType.OPENAI_FUNCTIONS)` y `Tools` que envuelven `RetrievalQA`; esa API fue eliminada en LangChain 1.x, así que se implementó el mismo patrón (orquestador + especialistas como herramientas/ramas) con salida estructurada y `RunnableBranch`, que además es más fácil de trazar y testear.

**Por qué LangChain (LCEL).** Se usaron componentes estándar en lugar de código propio frágil: `ChatPromptTemplate`, `ChatOpenAI`, `OpenAIEmbeddings`, `Chroma` + `as_retriever`, `RecursiveCharacterTextSplitter`, `StrOutputParser`, `RunnablePassthrough.assign` y `RunnableBranch`. LCEL hace cada paso componible, con `run_name` propio (se lee bien en Langfuse) y propagación automática de callbacks.

**Estrategia de routing.** El orquestador usa `with_structured_output` (Pydantic): devuelve rutas validadas `{department, sub_question}` + `confidence` + `reasoning`, en lugar de parsear texto libre. El enrutamiento es **condicional** con `RunnableBranch`. Soporta **delegación en paralelo** (`.batch`) cuando una consulta mezcla áreas (ej. sueldos + VPN) y un **fallback `OUT_OF_SCOPE`** para consultas ajenas (no inventa respuestas). Las rutas repetidas de un mismo área se fusionan, y si el orquestador falla el sistema degrada de forma segura al fallback registrando el error.

**Configuración de RAG.** Chunks de 800 caracteres con 120 de solapamiento (~15 %), cortando primero por títulos/párrafos para no partir una política a la mitad; embeddings `text-embedding-3-small`; Chroma persistido por dominio; `k=4`. El prompt obliga a responder **solo con el contexto** y a decir explícitamente cuándo la documentación no alcanza (anti-alucinación), sugiriendo el contacto del área.

**Observability con Langfuse.** Cada consulta genera **una traza** (`support-query`) con `session_id`, `user_id` y tags. Un `CallbackHandler` de LangChain anida dentro de ella: el span del orquestador, el `RunnableBranch`, el span de cada agente (`hr-agent`, `tech-agent`, `finance-agent`) con su paso `retrieve` (chunks recuperados) y `generate`, las *generations* del LLM (prompt, tokens, latencia) y el juez del evaluador. Se agrega metadata de depuración: tags `dept:<ÁREA>` y `misclassified`, y `expected_intent` vs `actual_intent`, para listar de golpe todos los enrutamientos errados y abrir la traza.

**Evaluador (bonus).** LLM-as-judge con salida estructurada que recibe *consulta + contexto recuperado + respuesta* y devuelve `relevance`, `completeness`, `accuracy` y `overall` (1-10) con justificación. Se registran con `langfuse.create_score(trace_id=…, name="quality" | "relevance" | "completeness" | "accuracy")`, de modo que se pueden filtrar y graficar en Langfuse para detectar respuestas de baja calidad (umbral: `< 6`).

## Cómo depurar una consulta mal enrutada en Langfuse

1. *Traces* → filtrar por tag `misclassified` (o por `user_id` / `session_id`).
2. Abrir la traza: el span `orchestrator-routing` muestra la consulta, la decisión y su `reasoning`/`confidence`.
3. Comparar `expected_intent` vs `actual_intent` en la metadata y mirar qué agente corrió.
4. Si el ruteo fue correcto pero la respuesta es mala: abrir `<agente>:retrieve` (ej. `hr-agent:retrieve`) y revisar los chunks recuperados.
5. Corregir (prompt del orquestador o documentos del agente), volver a correr `run_tests.py` y comparar.

## Limitaciones conocidas

- El corpus es **estático y ficticio** (Nimbus Cloud); en producción habría que reindexar automáticamente ante cambios en los documentos.
- El orquestador es un clasificador por prompt: acierta en temas claros, pero en consultas realmente **ambiguas** puede elegir un área distinta de la esperada (se registra la `confidence` para auditarlo).
- No hay **memoria conversacional** entre turnos: cada consulta es independiente (el `session_id` agrupa trazas pero los agentes no comparten estado).
- El evaluador usa el mismo modelo que los agentes; para evaluación crítica convendría un modelo juez distinto o revisión humana sobre una muestra.
- Chroma local es adecuado para este volumen (~380 chunks); a mayor escala convendría un vector store gestionado.
- Los resultados pueden variar levemente entre corridas (LLM); se usa `temperature=0` para minimizarlo.
