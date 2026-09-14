# Crítica del encargo (antes de tocar código)

Revisión del `contrato.md` buscando decisiones que faltaban y formas en que la
verificación podría dar verde con el trabajo incompleto.

## Decisiones que todavía había que adivinar

1. El contrato no dice qué pasa si `text` no es un `str` (por ejemplo `None`).
   El type hint de `save_note` ya declara `text: str`, así que se resuelve
   como fuera de alcance: no se valida tipo, solo contenido.
2. No estaba escrito si el recorte de espacios (`strip`) debía verificarse
   con su propio test o alcanzaba con inferirlo del código. Se decide
   exigir un test explícito (`test_save_note_strips_whitespace`), porque sin
   él una implementación que solo comprobara "está vacío" sin recortar el
   texto guardado pasaría igual la verificación.

## Formas en que la verificación podría dar verde sin estar completo

- Una implementación que lance `ValueError` **siempre** (incluso con texto
  válido) pasaría el test de texto en blanco. Esto ya queda descartado por
  el test existente `test_save_and_fetch_notes_against_real_postgres`, que
  sigue corriendo en la misma suite y exige que un texto válido se guarde
  sin error.
- Si el test de espacios en blanco no se ejecuta contra la tabla real (por
  ejemplo con un mock), podría pasar aunque el `INSERT` real fallara por
  otra razón. Se mantiene la restricción del contrato de correr todo contra
  el Postgres real del `docker-compose.yml`.

## Restricción real no considerada al escribir el contrato

La verificación no es instantánea: requiere Docker Desktop corriendo y
~15-20s por corrida (levantar Postgres + instalar dependencias del runner).
Eso hay que contarlo dentro de los 30 minutos de la tarea, no es gratis como
un test unitario en memoria.

## Ajuste incorporado al contrato

Se agrega a `contrato.md` una línea aclarando que la validación de tipo
(`None`, no-`str`) queda fuera de alcance, ya que es una decisión que sí se
puede justificar (el type hint existente) y evita ambigüedad durante la
ejecución.
