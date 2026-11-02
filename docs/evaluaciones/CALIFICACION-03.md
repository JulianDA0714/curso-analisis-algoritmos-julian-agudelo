# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Julián David Agudelo Acevedo · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `c14120b`

Muy buen trabajo: entregó todo con la estructura pedida y un análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **97 / 100** |
| **Nota (0–5)** | **4.85** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explicó bien qué es una colisión y usó el ejemplo de las guías 10, 24 y 17 con `m = 7`.
- Justificó que la tabla hash no sirve para rangos y que un árbol de búsqueda sí (`O(h + k)`).
- Estimó la altura del árbol degenerado (399.999), las comparaciones (~80 mil millones en total) y la del equilibrado (~19).
- Recomendó tabla hash más árbol balanceado y declaró sus cifras a 5.000.000 como estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- La comparación entre encadenamiento y direccionamiento abierto es corta: no explica por qué una tabla de direccionamiento abierto se degrada al llenarse ni qué pasa al borrar claves.
  → *Cómo corregirlo:* piense qué ocurre con la secuencia de sondeo cuando la tabla está casi llena y cuando se elimina una guía, y agregue una o dos frases sobre cada caso.
- En la estimación de la lista a 5.000.000 usó "100 veces más, 100 veces más tiempo" apoyándose en la gráfica, pero no mencionó que a esa escala la memoria y la caché del computador pueden hacer que el tiempo real sea mayor.
  → *Cómo corregirlo:* agregue una frase sobre qué factores podrían alejar el tiempo real de la proyección lineal.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justificó el `Θ(n)` de la lista para una guía inexistente.
- Nombró el supuesto de distribución uniforme de la función hash y explicó el peor caso `Θ(n)` si todas las guías caen en una casilla.

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: búsquedas exitosas e infructuosas, colisión forzada con `m = 7`, `factor_carga` correcto y veinte colecciones aleatorias donde lista y tabla coinciden.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`.
- Buscar es iterativo con `while`, así que no hay problema con listas largas.
- Todas las funciones tienen *docstring* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

**Lo que puede mejorar (y cómo corregirlo):**
- En las pruebas, las guías inexistentes salen de un rango distinto al de las existentes, así que el caso "inexistente que cae en una casilla ocupada" casi no se prueba a fondo.
  → *Cómo corregirlo:* genere inexistentes con `generar_guias_inexistentes` o de un rango que comparta residuos con las existentes.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados y leyenda; la primera tiene seis valores de `n` con ambas curvas en los mismos ejes y la segunda cuatro valores de `α`.
- Calculó factores de crecimiento (5,06 veces en la lista y 0,95 en la tabla) y los contrastó con `Θ(n)` y `Θ(1)`.
- Sus cifras coinciden con las gráficas publicadas (por ejemplo, la lista llega a unos 2,3 ms en n = 50.000) y agregó tablas con los valores exactos, lo que ayuda porque la curva de la tabla se ve pegada al eje.
- Notó con honestidad que el tiempo no crece en la misma proporción que `1 + α`.

**Lo que puede mejorar (y cómo corregirlo):**
- Entre `α = 0,5` y `α = 10` el tiempo creció 3,5 veces mientras `1 + α` creció 7,3, y lo atribuye a "operaciones fijas" sin comprobarlo.
  → *Cómo corregirlo:* compare también un par de valores consecutivos de `α` y piense qué parte del tiempo no depende de `α` (por ejemplo, calcular la casilla) para ver si explica la diferencia.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada (`lab3-estructuras-datos/` con los cinco archivos y la carpeta `graficas/`).
- El `README.md` sigue el orden pedido, trae su nombre, las instrucciones para reproducir y enlaces al código en cada parte.
- Las dos gráficas se ven con ruta relativa correcta.
- Hubo cinco commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan, `medicion.py` corre sin errores y genera las dos gráficas, y las respuestas de la lista y la tabla coinciden.
