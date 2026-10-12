"""
run_tests.py — Ejecuta las consultas de test_queries.json contra el sistema multiagente.

Uso:
    python run_tests.py                # corre todas las consultas
    python run_tests.py --no-eval      # sin evaluador (más rápido y barato)
    python run_tests.py --rebuild      # reconstruye los vector stores antes de correr

Imprime una tabla de resultados y guarda el detalle completo en outputs/test_results.json.
Cada caso tiene `expected_intent` (hr | tech | finance | out_of_scope; "finance+tech" si la consulta
mezcla áreas) y, para casos ambiguos, `acceptable_intents` con áreas alternativas válidas.
Una consulta se considera "ruteada correctamente" si TODAS las áreas elegidas están entre las aceptadas.
Toda la corrida se etiqueta en Langfuse con un mismo `run_tag` (golden-run-vN) para compararla con otras versiones.
"""

import argparse
import json
import sys

RUN_TAG_DEFAULT = "golden-run-v1"


def accepted_intents(case: dict) -> list:
    """Áreas válidas para un caso (en mayúsculas, como las usa el orquestador)."""
    base = case["expected_intent"].upper().split("+")
    extra = [a.upper() for a in case.get("acceptable_intents", [])]
    return base + extra

from src import config, tracing
from src.multi_agent_system import SupportSystem


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--no-eval", action="store_true", help="No ejecutar el agente evaluador")
    parser.add_argument("--rebuild", action="store_true", help="Reconstruir los vector stores")
    parser.add_argument("--run-tag", default=RUN_TAG_DEFAULT, help="Tag de Langfuse para toda la corrida (ej. golden-run-v2)")
    args = parser.parse_args()

    if not tracing.langfuse_enabled():
        print("AVISO: no hay claves de Langfuse en .env; se ejecuta SIN trazas.", file=sys.stderr)

    queries = json.loads(config.TEST_QUERIES_PATH.read_text(encoding="utf-8"))
    system = SupportSystem(rebuild_index=args.rebuild, evaluate=not args.no_eval)

    results, correct = [], 0
    for q in queries:
        expected = accepted_intents(q)
        out = system.answer(
            q["query"], session_id=args.run_tag, user_id="test-suite",
            expected_intent=q["expected_intent"].upper().split("+"), run_tag=args.run_tag,
        )
        chosen = out["routing"]["departments"]
        ok = all(d in expected for d in chosen)
        correct += ok
        score = out["evaluation"]["overall"] if out["evaluation"] else "-"
        print(f"[{'OK ' if ok else 'ERR'}] #{q['id']:>2} esperado={q['expected_intent']} elegido={chosen} "
              f"conf={out['routing']['confidence']:.2f} calidad={score}  | {q['query'][:60]}")
        results.append({"test": q, "ok": ok, **out})

    print(f"\nRouting correcto: {correct}/{len(queries)} ({correct / len(queries):.0%})")
    scored = [r["evaluation"]["overall"] for r in results if r["evaluation"]]
    if scored:
        print(f"Calidad promedio (evaluador, 1-10): {sum(scored) / len(scored):.1f} sobre {len(scored)} respuestas RAG")

    config.OUTPUTS_DIR.mkdir(exist_ok=True)
    out_path = config.OUTPUTS_DIR / "test_results.json"
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Detalle guardado en {out_path}")
    tracing.flush()


if __name__ == "__main__":
    main()
