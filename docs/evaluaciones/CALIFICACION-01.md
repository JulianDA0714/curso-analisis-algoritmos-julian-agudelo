# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Julián David Agudelo Acevedo · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `4cc23cf`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 19 / 25 |
| Corrección de la implementación | 12 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Separa bien "correcto" de "a tiempo" y nombra la ventana de 4 horas como la restricción que se incumple.
- Explica que un servidor más rápido no cambia la forma en que crece el trabajo del algoritmo.
- En la Parte 2 relaciona el tiempo con la energía acumulada día tras día y da dos perjuicios (el paciente y el operador), diciendo quién asume el costo.
- Señala que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (500.000 pedidos) es hipotético ("supongamos"). Se pedía un sistema que usted use, conozca o haya programado, con sus datos y su restricción.
- Falta la tensión sobre corrección: no dice qué obligación adicional impone que el orden sea exacto, más allá de decir que debe respetar el índice de riesgo.

## 2. Calidad de la explicación teórica (19 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio con el tamaño fijo, elige el peor caso para decidir la producción y deja su predicción escrita antes de medir.
- Plantea la recurrencia de merge sort explicando cada término y la resuelve con el árbol hasta `Θ(n log n)`.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El árbol es incompleto: no se ve el costo de cada nivel dibujado ni el total sumado (n por log n niveles) de forma explícita.
- Insertion sort no se calculó línea a línea: debía indicar cuántas veces se ejecuta cada línea de su código y sumar. Usted contó solo comparaciones.
- Al definir el caso promedio no dice sobre qué conjunto de entradas se promedia (todas las permutaciones).

## 3. Corrección de la implementación (12 / 20)
**Lo que hizo bien:**
- Ambos algoritmos ordenan bien, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`. Merge sort tiene su propia mezcla recursiva.
- Los generadores dan listas de números distintos y el aleatorio usa semilla.

**Lo que puede mejorar:**
- Los docstrings no siguen el estilo Google (faltan las secciones `Args` y `Returns`) y los de `datos.py` tampoco describen los parámetros.
- Las funciones de `parte3_casos.py` y `parte4_complejidad.py` no tienen docstring ni *type hints*.
- Faltan líneas en blanco entre funciones (PEP 8).

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes con unidades, leyenda y las curvas en los mismos ejes.
- Identifica con datos el peor caso (inverso), el mejor (casi ordenado) y el promedio (aleatorio), y lo contrasta con su predicción.
- Concluye con la gráfica que merge sort conviene y lo relaciona con `O(n²)` y `O(n log n)`.
- El concepto técnico recomienda merge sort, responde a la propuesta del servidor con un dato medido (9,6 h bajaría a unas 4,8 h) y declara la extrapolación como estimación. También habla de la memoria.

**Lo que puede mejorar:**
- Los tiempos son de una sola corrida; repetir cada medición y promediar daría curvas más confiables.
- No explica por qué las curvas se ven casi pegadas en tamaños pequeños.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Carpeta y archivos con los nombres correctos, README en el orden pedido, gráficas incrustadas con ruta que sí funciona y enlaces al código en cada parte.
- Cinco commits que tocan el laboratorio, con mensajes claros.

**Lo que puede mejorar:**
- Las instrucciones activan el entorno con una ruta de Windows (`venv/Scripts`); conviene indicar también la de macOS/Linux.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan correctamente y generan las tres gráficas. Los resultados coinciden con lo que muestra su informe.

## Para el próximo laboratorio
- Escriba docstrings estilo Google (con `Args` y `Returns`) y *type hints* en todas las funciones, incluidas las de los scripts de medición.
- Pase `pycodestyle` antes de entregar.
- Cuando le pidan un cálculo línea a línea, anote cuántas veces se ejecuta cada línea y sume.
- Use ejemplos reales y con cifras cuando se pida un caso propio.
- Repita las mediciones de tiempo y grafique el promedio.
