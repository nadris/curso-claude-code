# Desafío Opcional: Regla con Alcance por Ruta

## Objetivo

Mover convenciones de tests fuera del contexto global y comprobar que solo se
cargan cuando Claude trabaja con archivos correspondientes.

## Tiempo Estimado

25 a 35 minutos.

## Por Qué Importa

Una regla útil para tests puede ser ruido —o incluso una mala decisión— cuando
Claude trabaja en producción. `.claude/rules/` permite versionar instrucciones y
activar algunas solo al leer rutas que coinciden con sus patrones.

## Parte 1: Identificar una Regla Local

Elige dos convenciones que apliquen exclusivamente a `tests/`. Por ejemplo:

- los tests de persistencia usan PostgreSQL real;
- una regresión debe fallar por la capacidad ausente, no por montaje o sintaxis.

No copies reglas transversales como "no abrir `.env`": esas pertenecen a la raíz.

## Parte 2: Crear la Regla

Crea `.claude/rules/testing.md`:

```markdown
---
paths:
  - "tests/**/*.py"
---

# Reglas de pruebas

- Los tests de persistencia se ejecutan contra PostgreSQL, no SQLite.
- Antes de corregir una regresión, confirma que el test falla por el comportamiento ausente.
```

Confirma el artefacto:

```bash
git add .claude/rules/testing.md
git commit -m "Acota las reglas de pruebas a su ruta"
```

## Parte 3: Comprobar la Carga

Abre una sesión nueva y ejecuta `/context` antes de leer tests. Anota si la regla
aparece bajo **Memory files** y si `/memory` la enumera entre las instrucciones
cargadas. Antes de abrir una ruta coincidente no debería aparecer en ninguna de
las dos vistas.

Después pide:

```text
Lee tests/test_health.py y explica qué reglas específicas se aplican a este
archivo. Cita el archivo de instrucciones; no edites nada.
```

Vuelve a ejecutar `/context`. La regla debe aparecer después de que Claude lea
una ruta coincidente; `/memory` permite revisar su contenido.

## Parte 4: Probar el Límite

Inicia otra sesión y pide que lea solo `app/main.py`. Comprueba que la regla de
tests no se aplique como si fuera una convención general.

Si aparece cargada desde el inicio, revisa:

- que el frontmatter tenga `paths`;
- que el patrón esté entre comillas;
- que no exista una copia de la misma regla en el `CLAUDE.md` raíz;
- que la sesión no haya leído tests antes de tu comprobación.

## Comprueba

- [ ] La regla contiene solo decisiones propias de tests.
- [ ] El archivo está versionado bajo `.claude/rules/`.
- [ ] `/context` permite identificar cuándo se cargó.
- [ ] La regla se activa al leer `tests/test_health.py`.
- [ ] No se trata como regla global al trabajar solo con `app/main.py`.

## Limpieza

Conserva la regla si su alcance fue correcto. Si duplicaba el archivo raíz o no
aportaba una decisión real, elimínala en un commit que explique el motivo.
