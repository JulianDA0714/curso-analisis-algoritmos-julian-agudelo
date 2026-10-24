# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Julián David Agudelo Acevedo · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `19c0b95`

Muy buen trabajo: el laboratorio está completo, ordenado y con un análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 19 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 22 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **93 / 100** |
| **Nota (0–5)** | **4.65** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Compara con el máximo de un arreglo y explica bien que combinar cuesta solo una comparación, por lo que dividir no mejora `Θ(n)`.
- La recomendación (divide y vencerás) está justificada con sus datos, y la estimación a 1.000.000 de registros está declarada como estimación y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- Dice que divide y vencerás gana "desde 50 elementos", pero allí los tiempos son casi iguales (0,000068 s contra 0,000065 s). La ventaja clara aparece desde 100 elementos; conviene decirlo así.

## 2. Calidad de la explicación teórica (19 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)`, explica de dónde sale cada término y la resuelve con el método maestro verificando que `f(n)` crece como `n^(log₂ 2)`.
- Justifica el `Θ(n²)` de la fuerza bruta contando los tramos revisados.

**Lo que puede mejorar:**
- Podría decir de forma más explícita por qué las dos llamadas recursivas son de tamaño `n/2` (se parte la lista por la mitad).

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, no modifican la lista, y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- Hay type hints y docstrings en las funciones, y las pruebas incluyen 20 listas aleatorias.

## 4. Calidad del análisis de las gráficas (22 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y siete tamaños.
- Calcula el factor al duplicar `n` (4,92 veces para fuerza bruta y 2,05 para divide y vencerás) y lo relaciona con `Θ(n²)` y `Θ(n log n)`.

**Lo que puede mejorar:**
- Los valores del análisis salen de su tabla, no de lo que se lee en la gráfica; conviene citar también lo que se ve en ella (por ejemplo, que fuerza bruta llega a cerca de 2 s en n = 8000 y la otra curva queda pegada al eje).
- Para n = 4000 a 8000, el factor 2,05 se acerca más a 2 que a lo que predice `n log n` (un poco más de 2); sería bueno comentarlo.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, README en el orden pedido, gráfica incrustada con ruta relativa que funciona, enlaces al código en cada parte, instrucciones de reproducción y varios commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan y las dos funciones coinciden con una referencia en listas aleatorias. La medición corre sin errores y genera la gráfica.

## Para el próximo laboratorio
- Cuando señale un tamaño "desde el cual gana" un algoritmo, verifique que la diferencia sea clara y no un empate.
- Apoye cada afirmación también en lo que se ve en la gráfica, además de la tabla.
- Compare el factor medido con el valor teórico exacto (por ejemplo, el de `n log n`) y comente la diferencia.
