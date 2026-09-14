# Desafío Opcional: Presupuestar una Tarea Real

Práctica para después de clase. No se entrega y no es requisito para la sesión 4.

## Objetivo

Comparar dos presupuestos de contexto sobre la misma pregunta de solo lectura y
formular una regla propia a partir de evidencia, no de la idea de que menos
siempre es mejor.

## Tiempo Estimado

40 a 50 minutos.

## Por Qué Importa

En una tarea real no sabes de antemano cuánto repositorio necesita la respuesta.
Cargar todo aumenta coste y ruido; cargar demasiado poco puede ocultar una
dependencia. Vas a mantener constantes la pregunta, el modelo y la fuente, y
cambiar únicamente la selección inicial de contexto.

## Preparación

Elige un repositorio que puedas inspeccionar sin exponer secretos y una pregunta
que exija citar evidencia. Usa el modo **Manual** (`default`) y no autorices cambios.

Ejemplos:

- "¿Por qué esta función maneja este caso así? Cita código e historial."
- "¿Qué consumidores rompería si cambia la firma de esta función?"
- "¿Qué rutas dependen de esta variable de configuración?"

Guarda antes de empezar:

- pregunta literal;
- formato de respuesta esperado;
- versión de Claude Code;
- modelo mostrado por `/status`;
- commit actual del repositorio.

Usa la misma instalación, modelo, commit e instrucciones de proyecto en ambos
recorridos. No compares tiempos ni redacción: pueden variar aunque el contexto
sea idéntico.

## Parte 1: Contexto Amplio

Abre una conversación vacía. Antes de preguntar, incorpora deliberadamente:

- el archivo completo que contiene la función;
- dos o tres archivos relacionados;
- un log o salida de tests completa;
- el README general.

Usa referencias `@` para los archivos y pega la salida solo una vez. Ejecuta:

```text
/context all
```

Registra la composición visible. Haz la pregunta literal y exige archivo y línea
para cada afirmación técnica.

## Parte 2: Contexto Dirigido

Etiqueta el recorrido anterior y empieza vacío:

```text
/clear contexto-amplio
```

Esta vez aporta solo:

- el archivo que contiene la función o símbolo inicial;
- el test que cubre el comportamiento, si existe;
- una restricción pertinente en una frase.

No cargues preventivamente los demás archivos. Permite que Claude explore una
fuente adicional solo cuando pueda explicar qué pregunta resolverá con ella.

Ejecuta `/context all`, haz la misma pregunta literal y conserva el mismo formato
de respuesta.

## Parte 3: Verificar y Comparar

No califiques por seguridad aparente ni extensión. Comprueba las citas y completa:

| Criterio | Contexto amplio | Contexto dirigido |
|---|---|---|
| Composición antes de preguntar | | |
| Citas técnicas correctas | | |
| Dependencias relevantes encontradas | | |
| Afirmaciones sin respaldo | | |
| Fuentes adicionales que necesitó | | |
| Correcciones humanas | | |

Responde:

- ¿El contexto amplio encontró una relación que el dirigido omitió?
- ¿El dirigido evitó alguna afirmación irrelevante o sin fuente?
- ¿Qué archivo cargaste en el recorrido amplio y no cambió ninguna decisión?
- ¿Qué señal justificó ampliar el recorrido dirigido?

Cualquiera de los dos puede producir la mejor respuesta. El resultado útil es
saber qué información pagó su coste en esta clase de tarea.

## Parte 4: Formular una Regla Operativa

Escribe una regla que puedas aplicar mañana. Debe incluir punto de partida y
condición para ampliar, por ejemplo:

> Para analizar una regresión, empiezo con el test que la reproduce, la traza y
> el archivo señalado. Amplío cuando una cita o una dependencia concreta queda
> sin comprobar.

Evita reglas como "cargar poco" o "no superar 50 %": no indican qué decisión
tomar ni se transfieren entre modelos y proyectos.

## Comprueba

- [ ] La pregunta, el modelo, el commit y el formato fueron iguales.
- [ ] Ambas conversaciones empezaron vacías y cargaron las mismas instrucciones de proyecto.
- [ ] Registraste la composición con `/context all`.
- [ ] Verificaste las citas contra código o historial.
- [ ] Tu conclusión reconoce una compensación y una condición para ampliar.
- [ ] El repositorio no recibió cambios.

## Limpieza

```bash
git status --short
```

Debe estar vacío. Si el agente editó algo, no lo conserves como parte del
experimento: registra la desviación y revisa cómo formulaste el alcance de solo
lectura.
