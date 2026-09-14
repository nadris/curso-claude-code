# Evidencia de ejecución

Cambio real ejecutado en la rama `practica/s01-contrato` siguiendo
`contrato.md` (ajustado en `critica.md`).

## Ciclo rojo → verde

**Antes del cambio** (`docker compose up` en `desafios/sesion 02/`):

```
FAILED tests/test_persistence.py::test_save_note_rejects_blank_text - Failed: DID NOT RAISE ValueError
FAILED tests/test_persistence.py::test_save_note_strips_whitespace - AssertionError: assert ['  hola  '] == ['hola']
2 failed, 2 passed in 0.21s
```

Falló por el comportamiento ausente (sin validación, sin recorte), no por
montaje ni sintaxis — cumple la regla de `.claude/rules/testing.md`.

**Después del cambio**:

```
tests/test_persistence.py::test_save_and_fetch_notes_against_real_postgres PASSED
tests/test_persistence.py::test_save_note_rejects_blank_text PASSED
tests/test_persistence.py::test_save_note_strips_whitespace PASSED
4 passed in 0.26s
```

## Revisión (paso 5, fuera de la conversación)

```
$ git status --short
 M "desafios/sesion 02/app/persistence.py"

$ git diff --check
(sin salida — sin errores de espacios en blanco)

$ git diff -- "desafios/sesion 02/app/persistence.py"
@@ -8,8 +8,12 @@ def get_connection():
 def save_note(conn, text: str) -> None:
+    normalized = text.strip()
+    if not normalized:
+        raise ValueError("text no puede estar vacío")
+
     with conn.cursor() as cur:
-        cur.execute("INSERT INTO notes (text) VALUES (%s)", (text,))
+        cur.execute("INSERT INTO notes (text) VALUES (%s)", (normalized,))
     conn.commit()
```

El diff toca únicamente `save_note`, dentro del alcance y las
restricciones del contrato (misma firma, sin dependencias nuevas, sin
tocar el esquema).

## Preguntas

**¿Qué decisión faltaba en tu primera versión del encargo?**
Qué hacer con texto no-`str` (por ejemplo `None`). Se resolvió en la crítica
como fuera de alcance, apoyándose en el type hint ya existente.

**¿Qué parte del resultado quedó demostrada por un comando?**
Todo el resultado observable: el rechazo de texto en blanco y el recorte de
espacios están cubiertos por los dos tests nuevos, corridos contra Postgres
real vía `docker compose up`.

**¿Qué parte todavía depende de revisión humana?**
Si el mensaje de `ValueError("text no puede estar vacío")` es el tono/idioma
correcto para el resto del código, y si esta convención de validación debería
replicarse en otros puntos de entrada del proyecto (fuera de alcance aquí).

**¿El agente encontró una restricción real que tú no habías considerado?**
Sí: la verificación no es instantánea. Requiere Docker Desktop corriendo y
~15-20s por corrida (levantar Postgres + instalar dependencias del runner),
algo que hay que presupuestar dentro de los 30 minutos de la tarea.

**Nota sobre "interrumpir ante la primera desviación":** en esta ejecución
quien escribió el contrato y quien lo ejecutó fue el mismo asistente en la
misma sesión, así que no hubo una desviación real que interrumpir. El punto
de control equivalente fue la autocrítica del paso 3, hecha antes de tocar
código.

## Comprueba

- [x] La tarea cabía en 30 minutos y en una rama corta.
- [x] El contrato definía resultado, fuentes, alcance, restricciones y verificación.
- [x] La comprobación fallaba (2 failed) y mostraba el problema antes del cambio.
- [x] Se revisó el único archivo modificado (`persistence.py`) con `git diff`.
- [x] Riesgo residual registrado: el mensaje de validación y si debe
      replicarse en otras entradas del proyecto quedan pendientes de
      revisión humana (ver preguntas arriba).

## Limpieza

Cambio pequeño, reversible y con verificación en verde: se conserva la rama
`practica/s01-contrato` para que pueda revisarse o mezclarse a `main`; no se
elimina.
