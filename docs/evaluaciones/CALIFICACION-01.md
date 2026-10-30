# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Julián David Agudelo Acevedo · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `172116e`

Muy buen trabajo: el informe está completo, ordenado y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 23 / 25 |
| Corrección de la implementación | 20 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **92 / 100** |
| **Nota (0–5)** | **4.60** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Separa con claridad que el algoritmo es correcto pero no cumple la ventana de 4 horas, y nombra esa restricción.
- En la Parte 2 relaciona el tiempo de ejecución con el consumo de energía acumulado por correr todas las madrugadas durante años.
- Identifica dos perjuicios concretos (el paciente de alto riesgo llamado tarde y el operador con una lista incompleta) y dice quién asume el costo de cada uno.
- Discute bien la obligación extra de corrección: nadie con mayor riesgo debe quedar detrás de alguien con menor riesgo.

**Lo que puede mejorar (y cómo corregirlo):**
- El segundo ejemplo propio (la consulta del sistema financiero) dice cuánto tardaba una consulta, pero no cuántos datos o transacciones se procesaban ni cuál era el límite de tiempo que se incumplía. Por eso queda un poco abstracto.
  → *Cómo corregirlo:* agregue, aunque sea aproximado, cuántas transacciones o registros había que procesar y en cuánto tiempo debía terminar el proceso, para que se vea qué restricción concreta se rompía.
- La explicación de por qué duplicar el servidor no resuelve el problema de fondo es correcta pero general ("puede ayudar al principio").
  → *Cómo corregirlo:* explique qué pasa con el tiempo cuando el algoritmo sigue igual y los datos siguen creciendo, y por qué una máquina el doble de rápida solo cambia una constante y no la forma en que crece el tiempo.

## 2. Calidad de la explicación teórica (23 / 25)
**Lo que hizo bien:**
- Define mejor, peor y caso promedio indicando sobre qué entradas se toma cada uno y con el tamaño fijo, y justifica que usaría el peor caso por la ventana estricta.
- Deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort explicando cada término, la resuelve con árbol de recursión mostrando el costo por nivel, el número de niveles y la suma final.
- Cuenta línea a línea las ejecuciones de insertion sort en mejor y peor caso, y presenta la tabla de complejidades.

**Lo que puede mejorar (y cómo corregirlo):**
- El caso promedio de insertion sort se afirma como cuadrático, pero no se muestra por qué.
  → *Cómo corregirlo:* piense cuántos de los elementos anteriores, en promedio, tiene que recorrer cada elemento nuevo si el orden es aleatorio, y súmelo para todos los elementos.
- En el dibujo del árbol, la fila del nivel 1 quedó mal escrita (aparece un `\n` suelto) y se pierde la forma del árbol.
  → *Cómo corregirlo:* revise ese bloque de código del `README.md` y ponga cada nivel en su propia línea.

## 3. Corrección de la implementación (20 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan de mayor a menor, devuelven una lista nueva sin cambiar la original y cuentan solo comparaciones entre elementos (para una lista ya en el orden pedido, insertion sort hace exactamente n − 1).
- No usan `sorted()` ni `list.sort()`, y `merge_sort` tiene su propia mezcla recursiva.
- Los tres generadores dan listas del tamaño pedido, con valores distintos y semilla reproducible.
- Todas las funciones tienen *docstring* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes rotulados y leyenda, y muestran las curvas pedidas en los mismos ejes.
- Identifica con evidencia que el escenario C es el peor caso (unos 20,5 millones de comparaciones en n = 6400), el B el mejor y el A un aproximado del promedio, y contrasta con su predicción.
- Concluye que merge sort conviene, describe lo que hace cada curva y lo conecta con O(n²) frente a O(n log n), con un chequeo numérico del factor al duplicar el tamaño.
- Extrapola a 1.200.000 registros explicando el razonamiento y declarando que es una estimación, y muestra que ni con el servidor al doble de velocidad insertion sort cabría en las 4 horas.
- Menciona la memoria adicional de merge sort como consideración distinta del tiempo.

**Lo que puede mejorar (y cómo corregirlo):**
- Al responder a la propuesta del servidor usa una estimación, pero no cita la gráfica ni el valor medido del que parte.
  → *Cómo corregirlo:* nombre explícitamente la gráfica `parte4_tiempo.png` y el tamaño de entrada de donde toma el dato medido antes de pasar a la estimación.
- Afirma que merge sort es "más estable" frente a los escenarios, pero no lo respalda con una medición propia (solo tiene mediciones de merge sort en el escenario A).
  → *Cómo corregirlo:* mida merge sort también en los escenarios B y C y cite esos tiempos, o reformule la frase indicando que es una expectativa teórica.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada y tiene todos los archivos del entregable.
- El `README.md` tiene su nombre, instrucciones de reproducción y las partes en orden, con las gráficas incrustadas con rutas que funcionan.
- Enlaza `parte3_casos.py`, `parte4_complejidad.py`, `algoritmos.py` y `datos.py` donde corresponde.
- Tiene seis commits descriptivos sobre el laboratorio.

## ¿El código funciona?
Sí. Ambos algoritmos ordenan correctamente en pruebas con listas pequeñas y aleatorias, y los dos scripts corren sin errores y generan las gráficas.
