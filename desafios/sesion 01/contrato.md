# Contrato de tarea

Rama: `practica/s01-contrato`.

Tarea elegida de la lista de candidatas: **añadir una validación a una
entrada**.

## Resultado observable

`save_note(conn, text)` (en `desafios/sesion 02/app/persistence.py`) deja de
aceptar texto vacío o compuesto solo de espacios: lanza `ValueError` en ese
caso. Para texto válido, se recortan los espacios externos antes de guardarlo
(`" hola "` se guarda como `"hola"`).

Fuera de alcance (ajustado tras la crítica en `critica.md`): no se valida el
tipo de `text` (por ejemplo `None`); el type hint existente ya lo declara
`str`.

## Fuentes del repositorio

- `desafios/sesion 02/app/persistence.py` — función a modificar.
- `desafios/sesion 02/tests/test_persistence.py` — suite donde vive la
  evidencia de persistencia (regida por
  `desafios/sesion 02/.claude/rules/testing.md`: los tests de persistencia
  corren contra PostgreSQL real, no SQLite).

## Alcance y archivos intocables

Tocar únicamente los dos archivos listados arriba. No tocar:

- `desafios/sesion 02/app/main.py`
- `desafios/sesion 02/docker-compose.yml`
- `desafios/sesion 02/.claude/rules/testing.md`
- `desafios/sesion 02/CLAUDE.md`
- Cualquier archivo fuera de `desafios/sesion 02/`.

## Restricciones

- No cambiar la firma pública de `save_note(conn, text)`.
- No agregar dependencias nuevas (usar solo `psycopg2`, ya presente).
- No modificar el esquema de la tabla `notes`.
- No desactivar ni relajar la regla de `tests/**/*.py` sobre usar PostgreSQL
  real; la verificación debe seguir corriendo contra el contenedor de
  Postgres, no un mock ni SQLite.

## Verificación ejecutable

```bash
cd "desafios/sesion 02"
docker compose up --abort-on-container-exit --exit-code-from tests
docker compose down -v
```

Antes del cambio, un test nuevo (`test_save_note_rejects_blank_text`) debe
**fallar** porque `save_note` no lanza `ValueError` con texto en blanco.
Después del cambio, toda la suite (incluido ese test y uno que confirme el
recorte de espacios) debe pasar en verde.
