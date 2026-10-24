# Laboratorio evaluativo 03 — Estructuras de datos

**Estudiante:** Julián David Agudelo Acevedo  
**Curso:** Análisis de algoritmos

## Cómo ejecutar el laboratorio

Desde la carpeta principal del repositorio, activar el entorno virtual que venimos usando en el curso:

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS o Linux:**

```bash
source .venv/bin/activate
```

Si el entorno todavía no existe, crearlo con `python -m venv .venv`. Instalar las dependencias desde la raíz del repositorio:

```bash
python -m pip install -r requirements.txt
python -m pip install pycodestyle
```

Después entrar a `lab3-estructuras-datos` y ejecutar:

```bash
python pruebas.py
python medicion.py
python -m pycodestyle estructuras.py pruebas.py medicion.py
```

El archivo `medicion.py` vuelve a generar las dos gráficas. Los tiempos pueden variar un poco dependiendo del equipo y de lo que esté ejecutando al mismo tiempo.

## Parte 1 — Implementación y pruebas

**Código:** [estructuras.py](estructuras.py) | [pruebas.py](pruebas.py)

La idea era comparar una lista enlazada con una tabla hash para buscar guías de una empresa de envíos. En `estructuras.py` hice las clases `Nodo`, `ListaEnlazada` y `TablaHash`. La lista agrega las guías al inicio y para buscar recorre sus nodos. La tabla calcula la casilla con `guia % m` y, cuando varias guías caen en la misma, las guarda en una lista enlazada.

En las pruebas revisé búsquedas que sí encuentran una guía y otras que no, la colisión de las guías 10, 24 y 17 con siete casillas, el factor de carga y 20 colecciones aleatorias. También comparé las respuestas de ambas estructuras. Todas las pruebas pasaron y el código pasó la revisión de PEP 8.

## Parte 2 — Mediciones y gráficas

**Código:** [medicion.py](medicion.py)

Para medir utilicé `time.perf_counter()`. En cada caso hice 200 búsquedas de guías inexistentes y repetí la medición tres veces para sacar el promedio. Usé semillas fijas para poder repetir los experimentos. El tiempo de crear las estructuras y generar las guías no se incluyó en la medición.

### Experimento A — Lista frente a tabla hash

Para cada cantidad de guías usé una tabla con un número primo de casillas cercano a `n / 2`, buscando que el factor de carga quedara alrededor de 2.

| Guías (n) | Casillas (m) | α | Lista (ms) | Tabla hash (ms) |
|---:|---:|---:|---:|---:|
| 100 | 53 | 1.887 | 0.004058 | 0.000223 |
| 500 | 251 | 1.992 | 0.019060 | 0.000258 |
| 1000 | 503 | 1.988 | 0.038760 | 0.000322 |
| 5000 | 2503 | 1.998 | 0.195986 | 0.000305 |
| 20000 | 10007 | 1.999 | 0.776075 | 0.000322 |
| 50000 | 25013 | 1.999 | 2.325159 | 0.000325 |

![Comparación del tiempo de búsqueda entre lista y tabla hash](graficas/lista_vs_tabla.png)

La curva de la tabla casi no se distingue del eje horizontal porque sus tiempos son mucho menores que los de la lista. Por eso también dejé los valores exactos en la tabla.

### Experimento B — Efecto del factor de carga

En este caso dejé fijas 20.000 guías y cambié la cantidad de casillas para observar qué pasaba con las colisiones.

| Casillas (m) | α | Tabla hash (ms) |
|---:|---:|---:|
| 40009 | 0.500 | 0.000259 |
| 20011 | 0.999 | 0.000299 |
| 5003 | 3.998 | 0.000386 |
| 2003 | 9.985 | 0.000907 |

![Tiempo de búsqueda según el factor de carga](graficas/tiempo_vs_alfa.png)

## Parte 3 — Análisis

### 1. ¿Por qué cambia el costo de búsqueda?

En una lista enlazada, si una guía no existe, toca revisar todos los nodos para estar seguros. Por eso el tiempo crece con la cantidad de guías y se representa como Θ(n).

Con la tabla hash primero calculamos en qué casilla buscar y después revisamos únicamente esa lista. Si las guías quedan bien repartidas entre las casillas, el costo esperado es Θ(1 + α), siendo α la cantidad de guías dividida por las casillas. Esto depende de que la función hash distribuya las claves de manera más o menos uniforme. Si todas terminaran en la misma casilla, volveríamos a recorrer una lista grande y el peor caso sería Θ(n).

### 2. ¿Qué muestran los tiempos frente a la teoría?

En la primera gráfica la lista va aumentando bastante, mientras que la tabla hash se mantiene casi plana. Entre 1.000 y 5.000 guías, la cantidad de datos se multiplicó por 5 y el tiempo de la lista pasó de 0,038760 a 0,195986 ms, unas 5,06 veces. Eso se parece al crecimiento lineal que esperábamos.

En la tabla hash, para esos mismos tamaños, el tiempo pasó de 0,000322 a 0,000305 ms, unas 0,95 veces. El tiempo prácticamente se mantuvo igual porque el factor de carga siguió cerca de 2. Esto era lo que esperábamos según la teoría.

En la segunda gráfica, al subir α de 0,500 a 9,985, el tiempo aumentó de 0,000259 a 0,000907 ms, unas 3,50 veces. La expresión 1 + α aumentó aproximadamente 7,32 veces, pero eso no significa que el cronómetro deba dar exactamente ese factor: también hay operaciones fijas y pequeñas variaciones al medir. Lo importante es que con más guías por casilla las búsquedas se vuelven más lentas.

### 3. ¿Qué pasa cuando hay colisiones?

Una colisión ocurre cuando dos guías diferentes terminan en la misma casilla. Puede pasar incluso si sobran espacios, porque la función hash no garantiza una casilla distinta para cada guía. Por ejemplo, con `m = 7`, las guías 10, 24 y 17 dan residuo 3.

En el encadenamiento, como hicimos aquí, las tres se guardan en la lista de esa casilla. La ventaja es que se pueden seguir insertando guías aunque haya muchas colisiones; la desventaja es que se necesitan nodos adicionales y una cadena larga tarda más en recorrerse.

Con direccionamiento abierto no se crea otra lista, sino que se busca una casilla libre dentro del mismo arreglo siguiendo una secuencia de sondeo. La ventaja es que no necesitamos crear nodos adicionales, pero si la tabla empieza a llenarse, encontrar una casilla disponible puede tomar más tiempo.

### 4. ¿Sirve la tabla hash para buscar rangos?

Para buscar una guía exacta sí sirve, pero para pedir todas las guías entre X y Y no es tan útil porque no las mantiene ordenadas. Habría que revisar muchas casillas. Un árbol de búsqueda binario permite aprovechar el orden y consultar un rango en O(h + k), donde h es la altura del árbol y k son los resultados encontrados.

El problema es que un árbol común puede quedar desbalanceado. Si insertamos 400.000 guías ya ordenadas, quedaría prácticamente como una lista, con altura 399.999. Una búsqueda al final podría necesitar unas 400.000 comparaciones. Si contamos todas las comparaciones para construirlo de esa forma, serían aproximadamente 79.999.800.000.

En un árbol equilibrado, la altura estaría cerca de 19 aristas y una búsqueda necesitaría alrededor de 19 o 20 comparaciones, no cientos de miles. Por eso, para consultar rangos, me parece mejor utilizar un árbol balanceado y evitar que termine funcionando como una lista.

### 5. ¿Qué le recomendaría a la empresa?

Para las consultas del call center usaría una tabla hash con encadenamiento, porque normalmente buscan una guía exacta. Para el supervisor, que necesita consultar rangos, la complementaría con un árbol balanceado. Así cada necesidad tendría una estructura adecuada.

Con 50.000 guías la lista tardó 2,325159 ms por búsqueda inexistente. Como la gráfica muestra un crecimiento aproximadamente lineal, pasar a 5.000.000 de guías (100 veces más) daría una estimación de unos 232,5 ms por búsqueda. No es una medición real, sino una proyección basada en esa tendencia.

La tabla hash tardó 0,000325 ms con 50.000 guías y α cercano a 2. Si para 5.000.000 de guías aumentamos las casillas hasta aproximadamente 2.500.000 y las claves siguen bien distribuidas, el costo esperado podría seguir en el mismo orden, alrededor de 0,000325 ms. Igualmente, esto es una estimación y no significa que en la práctica vaya a dar exactamente ese tiempo, porque también depende del equipo y de otros factores.
