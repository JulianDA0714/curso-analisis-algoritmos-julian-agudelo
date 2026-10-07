import random
import time
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
SEMILLA = 42
REPETICIONES = 5
Resultado = tuple[int, int, float]


def generar_datos(n: int, generador: random.Random) -> list[int]:
    """Genera una lista de valores aleatorios para las mediciones.

    Args:
        n: Cantidad de elementos que tendrá la lista.
        generador: Generador aleatorio inicializado con una semilla fija.

    Returns:
        Una lista de enteros entre -100 y 100.
    """
    return [generador.randint(-100, 100) for _ in range(n)]


def medir_tiempo(
    funcion: Callable[..., Resultado],
    *args: Any
) -> tuple[Resultado, float]:
    """Mide el tiempo de una ejecución de un algoritmo.

    Args:
        funcion: Algoritmo que se va a medir.
        *args: Argumentos que recibe el algoritmo.

    Returns:
        El resultado del algoritmo y el tiempo de ejecución en segundos.
    """
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()

    return resultado, fin - inicio


def medir_promedio(
    funcion: Callable[..., Resultado],
    repeticiones: int,
    *args: Any
) -> tuple[Resultado, float]:
    """Ejecuta varias mediciones y calcula el tiempo promedio.

    Args:
        funcion: Algoritmo que se va a medir.
        repeticiones: Número de veces que se ejecutará el algoritmo.
        *args: Argumentos que recibe el algoritmo.

    Returns:
        El resultado del algoritmo y el tiempo promedio en segundos.
    """
    tiempos = []
    resultado: Resultado | None = None

    for _ in range(repeticiones):
        resultado, tiempo = medir_tiempo(funcion, *args)
        tiempos.append(tiempo)

    assert resultado is not None
    return resultado, sum(tiempos) / len(tiempos)


def main() -> None:
    """Ejecuta las mediciones y genera la gráfica comparativa."""
    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []
    generador = random.Random(SEMILLA)

    print("\nRESULTADOS DE MEDICION")
    print(f"Promedio de {REPETICIONES} ejecuciones por tamaño")
    print("-" * 70)

    for n in TAMANOS:
        valores = generar_datos(n, generador)

        resultado_fuerza, tiempo_fuerza = medir_promedio(
            subarreglo_fuerza_bruta,
            REPETICIONES,
            valores
        )

        resultado_divide, tiempo_divide = medir_promedio(
            subarreglo_maximo,
            REPETICIONES,
            valores,
            0,
            len(valores) - 1
        )

        assert resultado_fuerza[2] == resultado_divide[2]

        tiempos_fuerza_bruta.append(tiempo_fuerza)
        tiempos_divide_venceras.append(tiempo_divide)

        print(
            f"n={n:5d} | "
            f"Fuerza bruta={tiempo_fuerza:.6f}s | "
            f"Divide y venceras={tiempo_divide:.6f}s"
        )

    plt.figure(figsize=(10, 6))
    plt.plot(
        TAMANOS,
        tiempos_fuerza_bruta,
        marker="o",
        label="Fuerza bruta"
    )
    plt.plot(
        TAMANOS,
        tiempos_divide_venceras,
        marker="o",
        label="Divide y venceras"
    )
    plt.title("Tiempo promedio de ejecución vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(
        "graficas/tiempo_vs_n.png",
        dpi=150,
        bbox_inches="tight"
    )
    plt.close()

    print("\nGrafica generada correctamente.")


if __name__ == "__main__":
    main()
