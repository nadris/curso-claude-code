# Desafío Opcional: Sesión 1

## Objetivo

Aplicar el ciclo de la sesión a un cambio pequeño de un repositorio propio y
producir evidencia que otra persona pueda revisar.

## Tiempo Estimado

30 a 45 minutos.

## Por Qué Importa

El laboratorio trae un ticket y una comprobación preparados. En el trabajo real
la parte difícil suele ocurrir antes: elegir un cambio acotado, descubrir qué
decisiones faltan y encontrar una señal confiable de que terminó.

## Encargo

Elige una tarea real que puedas revertir y completar en menos de 30 minutos. Son
buenas candidatas:

- corregir un caso límite ya reproducible;
- añadir una validación a una entrada;
- eliminar una advertencia del linter sin desactivarla;
- documentar un flujo cuyo comando puedas ejecutar.

Evita autenticación, migraciones destructivas, despliegues y cambios que toquen
datos reales.

### 1. Crear una rama

```bash
git status --short
git switch -c practica/s01-contrato
```

Empieza desde un repositorio limpio.

### 2. Escribir el contrato

Antes de abrir Claude, deja por escrito:

- resultado observable;
- fuentes del repositorio;
- alcance y archivos intocables;
- restricciones;
- verificación ejecutable.

### 3. Pedir una crítica del encargo

```text
Revisa este contrato de tarea sin editar código. Señala decisiones que todavía
tendrías que adivinar y formas en que la verificación podría dar verde con el
trabajo incompleto.
```

Ajusta el contrato solo con observaciones que puedas justificar.

### 4. Ejecutar y dirigir

Entrega el contrato. Interrumpe ante la primera desviación y registra qué señal
te hizo intervenir.

### 5. Revisar

Ejecuta la verificación fuera de la conversación y revisa:

```bash
git status --short
git diff --check
git diff
```

## Preguntas

- ¿Qué decisión faltaba en tu primera versión del encargo?
- ¿Qué parte del resultado quedó demostrada por un comando?
- ¿Qué parte todavía depende de revisión humana?
- ¿El agente encontró una restricción real que tú no habías considerado?

## Comprueba

- [ ] La tarea cabía en 30 minutos y en una rama corta.
- [ ] El contrato definía resultado, fuentes, alcance, restricciones y verificación.
- [ ] La comprobación fallaba o mostraba el problema antes del cambio.
- [ ] Revisaste cada archivo modificado.
- [ ] Registraste al menos un riesgo residual; "ninguno" exige justificación.

## Limpieza

Vuelve a la rama anterior cuando termines:

```bash
git switch -
```

Conserva la rama si el cambio merece revisión. Si no, elimínala solo después de
confirmar que no contiene trabajo útil.
