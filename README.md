# Curso Claude Code

Registro de los desafíos del curso de Claude Code.

**Autor:** Never Adrian Sossa

## Progreso

- [x] Sesión 01 — Regla con alcance por ruta
- [ ] Sesión 02
- [ ] Sesión 03
- [ ] Sesión 04
- [ ] Sesión 05
- [ ] Sesión 06
- [ ] Sesión 07
- [ ] Sesión 08
- [ ] Sesión 09

Las sesiones 02 a 09 se irán agregando a medida que se resuelvan sus desafíos.

## Sesión 01 — Regla con alcance por ruta

Carpeta: [`desafios/sesion 01/`](desafios/sesion%2001/)

Desafío: [`desafio-opcional.md`](desafios/sesion%2001/desafio-opcional.md) — mover
convenciones de tests fuera del contexto global usando `.claude/rules/` y
comprobar que solo se cargan al trabajar con rutas que coinciden con su patrón.

Qué se hizo:

- Se creó [`.claude/rules/testing.md`](desafios/sesion%2001/.claude/rules/testing.md)
  con `paths: ["tests/**/*.py"]`, acotando dos convenciones propias de tests:
  que la persistencia se prueba contra PostgreSQL real (no SQLite) y que una
  regresión debe fallar por el comportamiento ausente antes de corregirla.
- Se armó un proyecto mínimo (`app/`, `tests/`) para que la regla tuviera algo
  real que escopear, y un [`CLAUDE.md`](desafios/sesion%2001/CLAUDE.md) local
  con la única convención transversal (no abrir `.env`).
- Se verificó en vivo que al leer `tests/test_health.py` la regla se inyecta en
  el contexto citando su archivo de origen, y que no aplica al trabajar solo
  con `app/main.py`.
- Se materializó la convención de persistencia con un test real contra
  PostgreSQL, orquestado con [`docker-compose.yml`](desafios/sesion%2001/docker-compose.yml)
  (Postgres + runner de pytest en contenedores, sin instalar nada en el host).

Cómo correr los tests de esta sesión:

```bash
cd "desafios/sesion 01"
docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
```
