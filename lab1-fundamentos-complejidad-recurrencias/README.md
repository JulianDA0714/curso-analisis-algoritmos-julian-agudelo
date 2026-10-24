# Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias

**Nombre:** Julián David Agudelo Acevedo

## Instrucciones para reproducir el laboratorio

El laboratorio está dentro de la carpeta `lab1-fundamentos-complejidad-recurrencias`

Primero se activa el entorno virtual desde la raíz del repositorio.

En Windows con Git Bash:

```bash
source venv/Scripts/activate
```

En Windows con PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source venv/bin/activate
```

Después se entra a la carpeta del laboratorio

```bash
cd lab1-fundamentos-complejidad-recurrencias
```

Para correr la Parte 3

```bash
python parte3_casos.py
```

Para correr la Parte 4

```bash
python parte4_complejidad.py
```

Las gráficas quedan guardadas en la carpeta `graficas`

---

# Parte 1 — Analizar el algoritmo antes de comprar hardware

En este caso hay algo que me parece importante separar desde el principio

Una cosa es que el algoritmo sea correcto y otra es que alcance a hacer su trabajo dentro del tiempo que tiene disponible

Insertion Sort es correcto porque finalmente puede dejar los registros en el orden que Tamiza necesita. El problema es que ahora hay **1.200.000 registros** y todos tienen que quedar organizados de mayor a menor riesgo entre las **2:00 a. m. y las 6:00 a. m.**

Entonces la restricción que se está incumpliendo es la ventana de **4 horas**

Como el algoritmo actual tiene un comportamiento que puede crecer mucho cuando aumenta la cantidad de datos, que haya funcionado durante ocho años no significa que siga siendo una buena opción para la cantidad de información que maneja actualmente Tamiza

Duplicar la velocidad del servidor puede ayudar a que el proceso tarde menos, pero no cambia el algoritmo que está haciendo el trabajo. Es como poner un equipo más rápido a hacer una tarea que cada vez se vuelve mucho más grande. Al principio puede alcanzar, pero si la cantidad de registros sigue creciendo el mismo problema puede volver a aparecer

Por eso antes de gastar en hardware revisaría primero el algoritmo. Si el problema está en la forma como crece el tiempo de ejecución, lo más lógico es mirar esa parte primero y después pensar si todavía hace falta más capacidad de servidor

Un caso real que conocí en mi trabajo fue una consulta SQL del CORE financiero, relacionada con la información de facturación. En una revisión se observó que la consulta `retrieveLoanInvoiceDataListByTransactionId` podía tardar alrededor de **27 segundos por transacción**. Aunque devolvía los datos esperados, ese tiempo era un problema cuando el proceso necesitaba consultar varias transacciones. La restricción era obtener la información a tiempo para que el proceso operativo pudiera continuar, no solamente que el resultado fuera correcto. Por eso era importante revisar cómo se ejecutaba la consulta y sus posibilidades de optimización antes de pensar solamente en aumentar los recursos del servidor. No estoy afirmando que el problema ya se haya solucionado ni que se procesara una cantidad específica de transacciones.

---

# Parte 2 — Responsabilidad ambiental y ética

Cuando se escoge un algoritmo para un sistema como Tamiza no solamente se debería mirar si funciona. También hay que pensar en lo que pasa como consecuencia del tiempo que dura ejecutándose

Un servidor que está procesando información durante más tiempo también está consumiendo energía durante más tiempo. En una ejecución puede que la diferencia no parezca tan grande, pero Tamiza hace este proceso todas las madrugadas. Como el proceso se repite todos los días durante años, ese consumo también se va acumulando

Por eso usar un algoritmo que necesite mucho más tiempo puede terminar teniendo un impacto ambiental mayor. No es solamente lo que consume una ejecución sino todas las ejecuciones que se van acumulando con el tiempo

También está la parte ética porque aquí los datos pertenecen a personas y el orden de la lista define quién se llama primero

Un primer problema sería que un paciente con un índice de riesgo alto no quede dentro de la lista a tiempo o quede en una posición que no corresponde. Como el centro de contacto empieza desde arriba de la lista, esa persona podría recibir la llamada más tarde de lo que debería. En este caso el costo lo termina asumiendo el paciente

Otro problema puede caer sobre las personas que trabajan en el centro de contacto. Si la lista queda incompleta o desordenada, los operadores pueden tener que revisar información por otros medios o trabajar con una lista que no está lista para usar. Ahí el costo lo asume el operador y también la Secretaría porque el proceso de atención se vuelve más complicado

Además hay algo que hace que este caso sea un poco más delicado. El orden no se usa solamente para organizar información. El orden decide a quién se contacta primero. Entonces el algoritmo debe respetar realmente el índice de riesgo porque una persona con mayor riesgo debería conservar esa prioridad en la lista. Esto impone una obligación adicional de corrección: además de terminar a tiempo, hay que comprobar que **no quede un paciente con mayor índice de riesgo detrás de otro con menor índice**. Una lista completa pero mal ordenada tampoco sería un resultado correcto para este proceso.

---

# Parte 3 — Peor caso, mejor caso y caso promedio

## 3.1 Explicación

El **mejor caso** es la entrada que para un tamaño determinado hace que el algoritmo trabaje lo menos posible

El **peor caso** es la entrada que para ese mismo tamaño hace que el algoritmo trabaje lo máximo posible

El **caso promedio** considera el costo sobre las diferentes entradas posibles de un mismo tamaño. Para una lista con elementos distintos, se puede definir promediando sobre **todas las permutaciones** de esos elementos, si se supone que cada una tiene la misma probabilidad. El escenario aleatorio del laboratorio es una aproximación experimental, no un cálculo exacto de ese promedio

En este punto el tamaño debe mantenerse fijo. Por ejemplo si estoy mirando entradas de 1.000 elementos, comparo entre las posibles entradas de esos mismos 1.000 elementos. No sería correcto comparar una entrada de 100 elementos con otra de 1.000 y decir que una es el mejor caso solamente por tener menos datos

Para decidir si Tamiza puede utilizar el algoritmo en producción yo tendría en cuenta principalmente el **peor caso**. Esto es porque la ventana de **4 horas** es fija. No se puede asumir que todos los días los datos van a llegar de la mejor manera posible. Como el canal puede cambiar, el algoritmo debería poder responder también cuando la entrada sea desfavorable

Antes de hacer las pruebas mi predicción fue esta

- **Escenario A — aleatorio:** aproximación al caso promedio
- **Escenario B — casi ordenado:** mejor caso o muy cercano al mejor caso
- **Escenario C — inverso:** peor caso

La idea era que Insertion Sort debería comportarse mucho mejor cuando la lista ya viene ordenada. Como en el escenario B el **98 %** está ordenado y el otro **2 %** está al final, esperaba que necesitara muchas menos comparaciones

En cambio en el escenario C los datos llegan exactamente al contrario del orden que Tamiza necesita. Como cada elemento tiene que ir pasando sobre muchos elementos anteriores, esperaba que este fuera el peor caso

El código usado para esta parte está en [`parte3_casos.py`](parte3_casos.py)

El algoritmo está en [`algoritmos.py`](algoritmos.py) y los generadores están en [`datos.py`](datos.py)

## 3.2 Resultados

Se probaron siete tamaños de entrada

**100, 200, 400, 800, 1600, 3200 y 6400 elementos**

El tiempo se tomó solamente durante la ejecución del algoritmo usando `time.perf_counter()`. La generación de los datos se hizo antes de empezar a medir. Cada tiempo corresponde al **promedio de cinco ejecuciones** con `time.perf_counter()`. Las comparaciones se cuentan dentro del algoritmo; para cada tamaño se utiliza la misma entrada en las cinco repeticiones.

### Comparaciones

| Tamaño | Aleatorio | Casi ordenado | Inverso |
|---:|---:|---:|---:|
| 100 | 2.542 | 100 | 4.950 |
| 200 | 9.970 | 203 | 19.900 |
| 400 | 40.436 | 417 | 79.800 |
| 800 | 160.484 | 866 | 319.600 |
| 1.600 | 648.481 | 1.851 | 1.279.200 |
| 3.200 | 2.533.103 | 4.172 | 5.118.400 |
| 6.400 | 10.276.753 | 10.277 | 20.476.800 |

![Comparaciones de Insertion Sort](graficas/parte3_comparaciones.png)

### Tiempo

| Tamaño | Aleatorio (s) | Casi ordenado (s) | Inverso (s) |
|---:|---:|---:|---:|
| 100 | 0,000284 | 0,000009 | 0,000424 |
| 200 | 0,000850 | 0,000019 | 0,001757 |
| 400 | 0,003769 | 0,000044 | 0,006978 |
| 800 | 0,016813 | 0,000095 | 0,029012 |
| 1.600 | 0,063159 | 0,000206 | 0,119634 |
| 3.200 | 0,251765 | 0,000452 | 0,535610 |
| 6.400 | 1,012051 | 0,001076 | 1,935171 |

![Tiempo de Insertion Sort](graficas/parte3_tiempo.png)

### Lo que muestran las pruebas

Los resultados fueron como esperaba

El escenario B fue el que menos comparaciones tuvo. También fue el que menos tiempo necesitó. Esto tiene sentido porque el **98 % de los datos ya estaba ordenado** y solamente se agregó el **2 %** restante al final

El escenario C fue todo lo contrario. Tuvo la mayor cantidad de comparaciones y también el mayor tiempo. Con **6.400 elementos** llegó a **20.476.800 comparaciones**

Entonces para el orden de mayor a menor que se escogió en este laboratorio, el escenario C representa el peor caso

El escenario A quedó entre los dos. Por eso se puede tomar como una aproximación al caso promedio

En la gráfica de tiempo, las curvas se ven casi pegadas al comienzo porque las diferencias son de fracciones de milisegundo y el eje vertical también debe representar los tiempos mucho mayores del escenario inverso. Cuando crece el tamaño, la curva inversa sube con más fuerza hasta acercarse a **1,94 segundos** con 6.400 datos, la aleatoria llega a **1,01 segundos** y la casi ordenada permanece cerca del eje horizontal, con apenas **0,001076 segundos**.

Algo que se nota bastante en la gráfica es como el tiempo empieza a crecer rápido cuando aumenta la cantidad de datos. En el escenario inverso se pasa de **5.118.400 comparaciones con 3.200 elementos** a **20.476.800 con 6.400 elementos**. Es decir, al duplicar el tamaño las comparaciones aumentan aproximadamente cuatro veces

Eso es justamente lo que se espera de un comportamiento cuadrático

---

# Parte 4 — Complejidad de Merge Sort e Insertion Sort

## 4.1 Cálculo teórico

Para Merge Sort se tiene la siguiente recurrencia

```text
T(n) = 2T(n/2) + Θ(n)
```

El `2T(n/2)` aparece porque el algoritmo divide la lista en dos partes. Como son dos partes, se tienen dos problemas y cada uno tiene aproximadamente `n/2` elementos

Después viene la parte de mezclar las dos listas. Como para hacer esa mezcla hay que revisar los elementos de las dos partes, ese trabajo tiene un costo de `Θ(n)`

Para resolver la recurrencia usé el **árbol de recurrencia**

El árbol muestra cuánto cuesta mezclar en cada nivel. Para simplificar, supongo que `n` es una potencia de 2; si no lo es, el resultado asintótico se mantiene.

```text
Nivel 0:                T(n)                     costo total: c·n
                       /    \nNivel 1:           T(n/2)   T(n/2)               2·c(n/2) = c·n
                   /  \      /  \
Nivel 2:        T(n/4) ... T(n/4)               4·c(n/4) = c·n
                   ...       ...
Nivel k:       n subproblemas T(1)               costo total: Θ(n)
```

En el nivel `i` hay `2^i` subproblemas de tamaño `n/2^i`, de modo que el trabajo de mezcla de ese nivel suma `2^i · c(n/2^i) = c·n`. Se puede dividir hasta llegar a subproblemas de tamaño 1: `n/2^k = 1`, por lo que `k = log₂(n)`.

Hay aproximadamente `log₂(n)` niveles de mezcla, cada uno con costo `Θ(n)`, más `n` casos base de costo constante. La suma explícita es:

```text
T(n) = c·n + c·n + ... + c·n + Θ(n)
       └── log₂(n) niveles ──┘
     = c·n·log₂(n) + Θ(n)
     = Θ(n log n)
```

Por eso **Merge Sort tiene complejidad Θ(n log n)**

y la cota de Merge Sort es

```text
O(n log n)
```

### Insertion Sort línea por línea

Para contar las ejecuciones uso la implementación real de [`algoritmos.py`](algoritmos.py), que ordena de mayor a menor. Este es el bloque relevante, numerado para explicar cada instrucción:

```python
# 1  resultado = datos.copy()
# 2  comparaciones = 0
# 3  for i in range(1, len(resultado)):
# 4      clave = resultado[i]
# 5      j = i - 1
# 6      while j >= 0:
# 7          comparaciones += 1
# 8          if resultado[j] < clave:
# 9              resultado[j + 1] = resultado[j]
# 10             j -= 1
# 11         else: break
# 12     resultado[j + 1] = clave
# 13 return resultado, comparaciones
```

La línea 3 tiene `n-1` iteraciones (más la comprobación final del ciclo). Las líneas 4, 5 y 12 se ejecutan `n-1` veces, y las líneas 1, 2 y 13 una vez cada una. El número de ejecuciones del cuerpo del `while` cambia según la entrada:

| Línea u operación | Mejor caso (ya descendente) | Peor caso (ascendente) |
|---|---:|---:|
| 1: copiar la lista | 1 | 1 |
| 2: inicializar contador | 1 | 1 |
| 3: iteraciones del `for` | n − 1 | n − 1 |
| 4: guardar `clave` | n − 1 | n − 1 |
| 5: asignar `j` | n − 1 | n − 1 |
| 6: evaluar `j >= 0` | 2(n − 1) | (n − 1)(n + 2)/2 |
| 7: aumentar contador | n − 1 | n(n − 1)/2 |
| 8: comparar elementos | n − 1 | n(n − 1)/2 |
| 9: desplazar elemento | 0 | n(n − 1)/2 |
| 10: decrementar `j` | 0 | n(n − 1)/2 |
| 11: ejecutar `break` | n − 1 | 0 |
| 12: insertar `clave` | n − 1 | n − 1 |
| 13: retornar | 1 | 1 |

En el **mejor caso**, el `while` compara una vez y sale por `break` en cada vuelta del `for`. Sumando las ejecuciones indicadas en la tabla (sin contar aparte la comprobación final del `for`) se obtiene `3 + 9(n − 1) = 9n − 6`, que crece como **Θ(n)**.

En el **peor caso**, para cada `i` el `while` desplaza `i` elementos. Por eso las líneas 7, 8, 9 y 10 se ejecutan `1 + 2 + ... + (n − 1) = n(n − 1)/2` veces cada una. La línea 6 se evalúa una vez adicional para salir del ciclo en cada iteración exterior. La suma de la tabla es `3 + 5(n − 1) + (n − 1)(n + 2)/2 + 4n(n − 1)/2`, es decir, **Θ(n²)**.

En el caso promedio, considerando las permutaciones de una lista de valores distintos con la misma probabilidad, los desplazamientos también crecen cuadráticamente: **Θ(n²)**.

> El conteo anterior trata la copia de la lista como una instrucción ejecutada una vez; copiar sus `n` elementos cuesta realmente Θ(n), lo cual no cambia ninguna de las cotas finales.

### Tabla de complejidades

| Algoritmo | Mejor caso | Caso promedio | Peor caso |
|---|---|---|---|
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |

---

## 4.2 Validación con las pruebas

Para esta parte comparé Insertion Sort y Merge Sort usando el escenario A, con los mismos tamaños de la Parte 3. **Los tiempos corresponden al promedio de cinco ejecuciones por tamaño**, usando la misma lista aleatoria para ambos algoritmos. La generación de datos no se incluye en el tiempo medido.

El código utilizado para esta comparación está en [`parte4_complejidad.py`](parte4_complejidad.py)

La implementación de los algoritmos se encuentra en [`algoritmos.py`](algoritmos.py)

| Tamaño | Insertion Sort (s) | Merge Sort (s) |
|---:|---:|---:|
| 100 | 0,000231 | 0,000141 |
| 200 | 0,000859 | 0,000308 |
| 400 | 0,003539 | 0,000683 |
| 800 | 0,015540 | 0,001562 |
| 1.600 | 0,070713 | 0,003312 |
| 3.200 | 0,246888 | 0,006966 |
| 6.400 | 0,970828 | 0,014821 |

![Comparación de tiempos entre Insertion Sort y Merge Sort](graficas/parte4_tiempo.png)

En la gráfica actualizada, Merge Sort permanece cerca del eje horizontal mientras la curva de Insertion Sort sube cada vez más, especialmente en los tamaños grandes. En tamaños pequeños ambas curvas se ven cercanas porque los tiempos son muy bajos en la escala usada. En estas pruebas Merge Sort fue más rápido que Insertion Sort en todos los tamaños

Lo que más se nota es como la diferencia va aumentando cuando también aumenta el tamaño de la entrada. Con **6.400 elementos** Insertion Sort tardó **0,970828 segundos**, mientras que Merge Sort tardó **0,014821 segundos**

Esto coincide con lo que salió en el análisis teórico. Insertion Sort tiene un crecimiento `O(n²)` para el caso promedio mientras que Merge Sort tiene `O(n log n)`

En tamaños pequeños las curvas parecen casi juntas por la escala del eje vertical, aunque Merge Sort ya es más rápido en las mediciones. También tiene costos de llamadas recursivas y creación de listas. Al llegar a 6.400 elementos, Insertion Sort tarda unas **65,5 veces** más que Merge Sort. Al duplicar de 3.200 a 6.400, Merge Sort pasa de **0,006966** a **0,014821 segundos**, un factor medido de **2,13**; para `n log₂(n)` el factor teórico es aproximadamente **2,17**. La pequeña diferencia es esperable porque los tiempos reales fluctúan.

---

# 4.3 Memo técnico para el equipo de ingeniería

Para Tamiza recomiendo utilizar **Merge Sort** como algoritmo principal de ordenamiento

La decisión la tomo pensando principalmente en que el canal de entrada puede cambiar. No se puede garantizar que los registros siempre van a llegar casi ordenados como pasa en el escenario B. Hoy puede funcionar así y mañana el flujo puede cambiar

Insertion Sort tiene un comportamiento muy bueno cuando los datos están casi ordenados. El problema es que cuando llegan aleatorios o en orden inverso el tiempo aumenta bastante

Esto se puede ver en las mediciones. Con **6.400 elementos** y el escenario A, Insertion Sort tardó **0,970828 segundos** mientras que Merge Sort tardó **0,014821 segundos**. Como el tamaño aumenta la diferencia también se vuelve más grande

Para los **1.200.000 registros** no se hizo una medición directa. Por eso los valores que siguen son una **estimación** basada en las pruebas realizadas

Para Insertion Sort se tomó el tiempo de **0,970828 segundos** con 6.400 elementos y se utilizó el comportamiento cuadrático que mostró el algoritmo. Pasar de 6.400 a 1.200.000 elementos significa aumentar el tamaño unas **187,5 veces**. Si el tiempo crece aproximadamente con el cuadrado de ese factor, el resultado queda cerca de **9,5 horas**

Para el escenario inverso la estimación es todavía mayor. Tomando los **1,935171 segundos** medidos con 6.400 elementos, el tiempo estimado para 1.200.000 registros sería aproximadamente **18,9 horas**

Estos valores no son mediciones directas. Son estimaciones hechas a partir de la forma de crecimiento observada

Para Merge Sort se tomó como referencia el tiempo de **0,014821 segundos** con 6.400 elementos y se utilizó el crecimiento `n log n`. Con esta aproximación el tiempo para 1.200.000 elementos queda cerca de **4,44 segundos**. Nuevamente esto es una estimación y no una ejecución real con 1.200.000 registros

Con estos resultados no veo suficiente la propuesta de simplemente comprar un servidor con el doble de velocidad

Por ejemplo, si se toma la estimación de **9,5 horas** para Insertion Sort y se supone que un servidor del doble de velocidad reduce el tiempo exactamente a la mitad, todavía quedarían unas **4,75 horas**. Eso sigue estando por encima de las **4 horas** que tiene Tamiza

Entonces el cambio de hardware podría ayudar pero no soluciona de fondo el crecimiento del algoritmo

Hay otro punto que también se debe tener en cuenta y es la memoria. Merge Sort necesita memoria adicional para dividir y mezclar las listas. Ese es un costo que Insertion Sort no tiene de la misma forma. Aun así, en este caso considero que vale más la pena asumir ese costo de memoria que mantener un algoritmo que puede tardar demasiado cuando aumente la cantidad de registros

También me parece importante que Merge Sort sea una opción más estable frente a los diferentes escenarios. Como no depende de que la lista llegue casi ordenada, el cambio en el canal de entrada no afecta de la misma manera su comportamiento

Por todo esto la recomendación es utilizar **Merge Sort** y hacer una prueba final con una cantidad de datos cercana a los **1.200.000 registros** antes de llevar el cambio a producción. Así se podría comprobar directamente el consumo de memoria y el tiempo real del proceso en un ambiente controlado


---

**Actualización para recalificación:** mediciones repetidas cinco veces por tamaño, tablas actualizadas con los resultados obtenidos y gráficas regeneradas con los promedios.
