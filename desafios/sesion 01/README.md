# Sesión 01 — Aplicar el ciclo de la sesión a un cambio real

Desafío: [`desafio-opcional.md`](desafio-opcional.md) — elegir una tarea real,
pequeña y reversible, y ejecutarla con un contrato explícito, una crítica
previa, ejecución dirigida y revisión con evidencia.

## Documentos generados

- [`contrato.md`](contrato.md) — resultado observable, fuentes, alcance,
  restricciones y verificación, escrito antes de tocar código.
- [`critica.md`](critica.md) — revisión del contrato buscando decisiones
  faltantes y formas en que la verificación podría dar falso verde.
- [`evidencia.md`](evidencia.md) — log rojo → verde, revisión del diff,
  respuestas a las preguntas del desafío y checklist final.

## Tarea elegida

Añadir una validación de entrada a `save_note` en
[`desafios/sesion 02/app/persistence.py`](../sesion%2002/app/persistence.py):
rechaza texto vacío o solo de espacios (`ValueError`) y recorta espacios
externos antes de guardar. Ejecutada en la rama `practica/s01-contrato`
(mezclada a `main` tras la revisión) siguiendo la regla de
`desafios/sesion 02/.claude/rules/testing.md` de probar persistencia contra
PostgreSQL real.

Verificación:

```bash
cd "desafios/sesion 02"
docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
```
