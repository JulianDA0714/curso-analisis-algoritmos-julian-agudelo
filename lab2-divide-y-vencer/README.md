# Laboratorio evaluativo 02 — Dividir y vencer

**Nombre:** Julián David Agudelo Acevedo

## Instrucciones para reproducir el laboratorio

El laboratorio está en la carpeta `lab2-divide-y-vencer`.

Primero se activa el entorno virtual desde la raíz del repositorio.

En Windows usando Git Bash:

```bash
source venv/Scripts/activate
```

En Windows usando PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source venv/bin/activate
```

Después se entra a la carpeta:

```bash
cd lab2-divide-y-vencer
```

Para ejecutar las pruebas:

```bash
python pruebas.py
```

Para realizar las mediciones y generar la gráfica:

```bash
python medicion.py
```

La gráfica se guarda en la carpeta `graficas`.

---

# Parte 1 — Implementación y pruebas

Para resolver el problema de la cooperativa hice las dos soluciones que pide la guía: fuerza bruta y divide y vencerás.

El código de los algoritmos está en [`subarreglo.py`](subarreglo.py) y las verificaciones están en [`pruebas.py`](pruebas.py).

En fuerza bruta se revisan los posibles tramos de días y se va acumulando su suma. Así no hay que volver a sumar desde cero todos los valores de cada tramo.

En divide y vencerás se separa la lista en dos partes. Después se busca la mejor racha de la izquierda, la de la derecha y la que cruza el punto medio. Al final se escoge la que tenga la mayor suma.

Para revisar que funcionaran probé el ejemplo de los ocho días, una lista con un solo elemento, listas con todos los valores negativos y positivos, un caso cruzado y 20 listas aleatorias. En estas últimas comparé las sumas que devolvían ambos algoritmos.

Con el ejemplo `[-3, 5, -2, 8, -6, 3, 9, -4]`, los dos obtuvieron la suma máxima de **17**.

Al ejecutar `python pruebas.py` salió:

```text
Todas las pruebas pasaron correctamente.
```

---

# Parte 2 — Medición y gráfica

El código de esta parte está en [`medicion.py`](medicion.py).

Se probaron siete tamaños: **10, 50, 100, 500, 1000, 4000 y 8000** elementos. Los valores se generaron entre -100 y 100 usando un generador inicializado con la semilla fija **42**. Para cada tamaño se utilizó exactamente la misma lista en los dos algoritmos.

El tiempo se tomó con `time.perf_counter()` solamente durante la ejecución de cada algoritmo. No se incluyó la generación de los datos. Para reducir el efecto de variaciones de una sola ejecución, cada algoritmo se ejecutó **5 veces por tamaño** y se utilizó el tiempo promedio. También comprobé que las sumas obtenidas por ambos algoritmos coincidieran.

| Tamaño | Fuerza bruta (s) | Divide y vencerás (s) |
|---:|---:|---:|
| 10 | 0,000006 | 0,000012 |
| 50 | 0,000068 | 0,000065 |
| 100 | 0,000238 | 0,000138 |
| 500 | 0,006404 | 0,000765 |
| 1.000 | 0,024652 | 0,001598 |
| 4.000 | 0,401170 | 0,007020 |
| 8.000 | 1,973235 | 0,014414 |

![Tiempo de ejecución de ambos algoritmos](graficas/tiempo_vs_n.png)

---

# Parte 3 — Análisis

## 3.1 Recurrencia y complejidad

En divide y vencerás se crean dos subproblemas de aproximadamente la mitad del tamaño. Además, hay que revisar el tramo que cruza el punto medio. Como para encontrarlo se recorren las dos mitades, ese paso cuesta `Θ(n)`.

La recurrencia queda así:

```text
T(n) = 2T(n/2) + Θ(n)
```

Para aplicar el método maestro tenemos `a = 2`, `b = 2` y `f(n) = Θ(n)`. Al calcular `n^(log₂ 2)` se obtiene `n`. Como `f(n)` tiene el mismo crecimiento que `n^(log₂ 2)`, se cumple el segundo caso del método maestro. Por eso el resultado es **Θ(n log n)**.

En fuerza bruta se usan dos ciclos: uno escoge el inicio del tramo y el otro recorre los posibles finales. Aunque la suma se va acumulando, se revisan aproximadamente `n(n + 1)/2` tramos. Por eso su complejidad es **Θ(n²)**.

## 3.2 Lo medido frente a lo esperado

En la gráfica se nota que fuerza bruta empieza a crecer mucho más rápido. Divide y vencerás también aumenta su tiempo, pero la diferencia entre los dos se vuelve cada vez mayor.

Por ejemplo, al pasar de **4.000 a 8.000 elementos**, fuerza bruta pasó de **0,401170** a **1,973235 segundos**. Eso significa que tardó unas **4,92 veces** más.

En divide y vencerás se pasó de **0,007020** a **0,014414 segundos**, aproximadamente **2,05 veces** más.

Esto mantiene la tendencia esperada: fuerza bruta crece mucho más rápido por su `Θ(n²)`, mientras que divide y vencerás queda cerca de duplicar su tiempo, como se espera de `Θ(n log n)`. Los valores no tienen que dar exactamente el factor teórico porque son tiempos medidos y pueden variar según la ejecución y el equipo.

## 3.3 Tamaños pequeños

En mis pruebas divide y vencerás empezó a mostrar ventaja desde los **50 elementos**, aunque en ese tamaño los tiempos todavía fueron prácticamente iguales: **0,000068 segundos** para fuerza bruta y **0,000065 segundos** para divide y vencerás.

Con 10 elementos fuerza bruta fue más rápida. Esto puede pasar porque dividir la lista y hacer llamadas recursivas también tiene un costo. En listas pequeñas ese trabajo adicional puede pesar más que la diferencia de complejidad, pero cuando aumenta la cantidad de datos la ventaja de divide y vencerás se hace mucho más clara.

## 3.4 ¿Siempre conviene dividir?

No necesariamente. Si solamente necesitamos encontrar el número más grande de una lista, podemos recorrerla una vez y guardar el mayor. Eso ya cuesta `Θ(n)`.

Si la dividimos en dos, encontramos el máximo de cada mitad y al final comparamos ambos resultados. En ese caso la recurrencia sería:

```text
T(n) = 2T(n/2) + Θ(1) = Θ(n)
```

El costo de combinar es constante porque solamente se comparan dos valores. Entonces dividir no mejora el orden de crecimiento frente a recorrer la lista directamente. En el subarreglo máximo sí aporta una mejora importante frente a la fuerza bruta.

## 3.5 Recomendación para la cooperativa

Para la cooperativa escogería **divide y vencerás** porque el equipo también quiere analizar series mucho más grandes. Con **8.000 elementos**, fuerza bruta tardó en promedio **1,973235 segundos**, mientras que divide y vencerás necesitó **0,014414 segundos**.

Para estimar qué pasaría con **1.000.000 de registros** tomé esos tiempos como referencia y apliqué el crecimiento de cada algoritmo. No es una medición real con un millón de datos.

El tamaño aumenta **125 veces**. En fuerza bruta, por su crecimiento cuadrático, el factor sería `125²`. Eso daría aproximadamente **30.832 segundos**, es decir, **8,6 horas**.

En divide y vencerás utilicé la proporción entre `1.000.000 log₂(1.000.000)` y `8.000 log₂(8.000)`. Con esa aproximación el tiempo sería de unos **2,77 segundos**.

Por eso recomendaría divide y vencerás para este caso. Aunque con pocos datos la diferencia no es tan grande, las mediciones muestran que con listas más extensas fuerza bruta deja de ser una buena opción. Antes de usarlo en un sistema real también haría una prueba con un volumen cercano al esperado.
