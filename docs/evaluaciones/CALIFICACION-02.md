# Retroalimentación — Laboratorio 02 · Dividir y vencer

**Estudiante:** Julián David Agudelo Acevedo · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `71ffacb`

Muy buen trabajo: el laboratorio está completo, ordenado y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **94 / 100** |
| **Nota (0–5)** | **4.70** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Identifica que con 50 elementos los tiempos son casi iguales y que desde 100 elementos divide y vencerás empieza a ganar, con sus datos.
- Explica por qué con 10 elementos la fuerza bruta es más rápida (el costo de dividir y hacer llamadas recursivas).
- En la comparación con el máximo de un arreglo, justifica con el costo de combinar (constante) y la recurrencia.
- Recomienda divide y vencerás, declara que el valor para 1.000.000 de registros es una estimación y no usa una regla de tres lineal.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 plantea la recurrencia del máximo pero no explica qué caso del método maestro la resuelve, y deja sin comentar si dividir tiene algún costo extra (las llamadas recursivas).
  → *Cómo corregirlo:* identifique `a`, `b` y `f(n)` de esa recurrencia, diga qué caso aplica y compare el resultado con el recorrido simple, mencionando si hay algún costo adicional al dividir.
- La estimación para 1.000.000 usa un solo punto medido (n = 8.000) y no habla de cuánta confianza tiene en ella.
  → *Cómo corregirlo:* agregue una frase sobre qué puede hacer que el tiempo real se aleje de su estimación (por ejemplo, el comportamiento con datos muy grandes).

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Explica de dónde sale cada término de `T(n) = 2T(n/2) + Θ(n)`: dos subproblemas de tamaño `n/2` y un caso cruzado que cuesta `Θ(n)`.
- Resuelve con el método maestro, calcula `n^(log₂ 2)`, compara con `f(n)` y concluye `Θ(n log n)` indicando el caso aplicado.
- Justifica el `Θ(n²)` de la fuerza bruta contando los tramos revisados, `n(n + 1)/2`.

**Lo que puede mejorar (y cómo corregirlo):**
- No muestra cómo el recorrido de las dos mitades en el caso cruzado suma exactamente un recorrido de tamaño `n`, ni escribe el paso final de `Θ(n²)` desde la suma de tramos.
  → *Cómo corregirlo:* indique cuántos elementos recorre cada barrido y sume ambos; escriba también la suma `n + (n-1) + ... + 1` y cómo se reduce a su orden de crecimiento.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días, un elemento, todos negativos, todos positivos y un caso cruzado.
- Ambos algoritmos coinciden en las 20 listas aleatorias de sus pruebas y también en cientos de listas aleatorias adicionales.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta, y ninguna función modifica la lista recibida.
- Todas las funciones tienen *type hints*, *docstring* con `Args` y `Returns` y dos líneas en blanco entre ellas.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Sus cifras del informe (cerca de 2 segundos para fuerza bruta en 8.000 y casi pegada al eje para divide y vencerás) coinciden con lo que muestra la gráfica.
- Calcula el factor de crecimiento al duplicar `n` (4.000 a 8.000) para ambos algoritmos y lo compara con los factores teóricos 4 y 2,17.

**Lo que puede mejorar (y cómo corregirlo):**
- El factor de la fuerza bruta (4,92) queda por encima del 4 esperado y no lo explica; solo comenta la diferencia de divide y vencerás.
  → *Cómo corregirlo:* agregue una explicación de por qué el factor medido de la fuerza bruta se aleja del teórico y calcule el factor en otro par de tamaños que se dupliquen para ver si es un caso aislado.
- La gráfica es lineal y los tamaños pequeños quedan pegados al eje; solo la tabla permite verlos.
  → *Cómo corregirlo:* apóyese en la tabla (como ya hace) citando los valores de los tamaños pequeños cuando afirme algo sobre ellos.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` está en la raíz con todos los archivos del entregable y la gráfica en `graficas/`.
- El informe sigue el orden pedido, con su nombre, instrucciones para reproducir y enlaces a `subarreglo.py`, `pruebas.py` y `medicion.py`.
- La gráfica está incrustada con ruta relativa que funciona, e indica que repitió cada medición 5 veces y usó el promedio.
- Tiene varios commits descriptivos sobre el laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y las dos funciones calculan la mejor racha correctamente, incluso comparadas con una referencia independiente. La medición usa semilla fija, cronometra solo los algoritmos y genera la gráfica.
