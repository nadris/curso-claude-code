# Curso Claude Code

Registro de los desafíos del curso de Claude Code.

**Autor:** Never Adrian Sossa

## Progreso

- [x] Sesión 01 — Ciclo de contrato, crítica y revisión sobre un cambio real
- [x] Sesión 02 — Regla con alcance por ruta
- [x] Sesión 03 — Presupuestar contexto: amplio vs. dirigido
- [ ] Sesión 04
- [ ] Sesión 05
- [ ] Sesión 06
- [ ] Sesión 07
- [ ] Sesión 08
- [ ] Sesión 09

Las sesiones 03 a 09 se irán agregando a medida que se resuelvan sus desafíos.

## Sesión 01 — Ciclo de contrato, crítica y revisión sobre un cambio real

Carpeta: [`desafios/sesion 01/`](desafios/sesion%2001/)

Desafío: [`desafio-opcional.md`](desafios/sesion%2001/desafio-opcional.md) —
elegir una tarea real, pequeña y reversible, y ejecutarla con un contrato
explícito, una crítica previa, ejecución dirigida en una rama corta y
revisión con evidencia ejecutable.

Qué se hizo:

- Se escribió [`contrato.md`](desafios/sesion%2001/contrato.md) antes de tocar
  código: resultado observable, fuentes, alcance, archivos intocables,
  restricciones y verificación ejecutable.
- Se hizo una [`critica.md`](desafios/sesion%2001/critica.md) del contrato,
  encontrando decisiones sin resolver y formas en que la verificación podría
  dar falso verde, y se ajustó el contrato solo con lo justificable.
- Se ejecutó el cambio real (rama `practica/s01-contrato`, luego mezclada a
  `main`): `save_note` en
  [`desafios/sesion 02/app/persistence.py`](desafios/sesion%2002/app/persistence.py)
  ahora rechaza texto vacío y recorta espacios, con tests que primero fallaron
  (rojo) y luego pasaron (verde) contra el Postgres real del `docker-compose`
  de la sesión 02.
- Se documentó todo el log y las respuestas a las preguntas del desafío en
  [`evidencia.md`](desafios/sesion%2001/evidencia.md).

## Sesión 02 — Regla con alcance por ruta

Carpeta: [`desafios/sesion 02/`](desafios/sesion%2002/)

Desafío: [`desafio-opcional.md`](desafios/sesion%2002/desafio-opcional.md) — mover
convenciones de tests fuera del contexto global usando `.claude/rules/` y
comprobar que solo se cargan al trabajar con rutas que coinciden con su patrón.

Qué se hizo:

- Se creó [`.claude/rules/testing.md`](desafios/sesion%2002/.claude/rules/testing.md)
  con `paths: ["tests/**/*.py"]`, acotando dos convenciones propias de tests:
  que la persistencia se prueba contra PostgreSQL real (no SQLite) y que una
  regresión debe fallar por el comportamiento ausente antes de corregirla.
- Se armó un proyecto mínimo (`app/`, `tests/`) para que la regla tuviera algo
  real que escopear, y un [`CLAUDE.md`](desafios/sesion%2002/CLAUDE.md) local
  con la única convención transversal (no abrir `.env`).
- Se verificó en vivo que al leer `tests/test_health.py` la regla se inyecta en
  el contexto citando su archivo de origen, y que no aplica al trabajar solo
  con `app/main.py`.
- Se materializó la convención de persistencia con un test real contra
  PostgreSQL, orquestado con [`docker-compose.yml`](desafios/sesion%2002/docker-compose.yml)
  (Postgres + runner de pytest en contenedores, sin instalar nada en el host).

Cómo correr los tests de esta sesión:

```bash
cd "desafios/sesion 02"
docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
```

## Sesión 03 — Presupuestar contexto: amplio vs. dirigido

Carpeta: [`desafios/sesion 03/`](desafios/sesion%2003/)

Desafío: [`desafio-opcional.md`](desafios/sesion%2003/desafio-opcional.md) —
comparar dos presupuestos de contexto sobre la misma pregunta de solo lectura
(misma pregunta, modelo, commit e instrucciones de proyecto) y formular una
regla propia a partir de evidencia verificada, no de la idea de que menos
contexto siempre es mejor.

Qué se hizo:

- Se comparó un recorrido de **contexto amplio** (archivo completo, dos
  archivos relacionados, log de tests completo, README general) contra uno de
  **contexto dirigido** (solo el archivo con `save_note`, su test y una
  restricción en una frase) sobre la misma pregunta: "¿Por qué `save_note`
  maneja el texto en blanco así? Cita código e historial."
- Se verificó cada cita de archivo:línea y de commit contra el working tree y
  `git show` reales. El recorrido amplio encontró una relación válida que el
  dirigido omitió (por qué `TEXT NOT NULL` no basta para rechazar texto en
  blanco), pero también produjo la única cita de historial no verificable de
  los dos recorridos (una ruta de archivo que no existía en el commit citado).
- Se documentó la comparación completa, la tabla de criterios y la regla
  operativa resultante en [`evidencia.md`](desafios/sesion%2003/evidencia.md),
  incluida una nota de método sobre cómo se adaptó el desafío (pensado para
  dos sesiones interactivas de la CLI) a dos subagentes aislados sin memoria
  compartida.
