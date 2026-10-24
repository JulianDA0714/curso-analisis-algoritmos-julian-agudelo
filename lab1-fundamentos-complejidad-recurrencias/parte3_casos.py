"""Compara Insertion Sort en tres escenarios de entrada."""

import time
from collections.abc import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 5
Generador = Callable[[int], list[int]]
Resultados = dict[str, dict[str, list[float] | list[int]]]


def medir_escenario(
    generador: Generador, tamanos: list[int]
) -> tuple[list[float], list[int]]:
    """Mide el tiempo promedio y las comparaciones de un escenario.

    Args:
        generador: Función que crea los datos del escenario.
        tamanos: Tamaños de entrada que se evaluarán.

    Returns:
        Los tiempos promedio y las comparaciones por tamaño.
    """
    tiempos = []
    comparaciones = []

    for n in tamanos:
        datos = generador(n)
        mediciones = []
        cantidad_comparaciones = 0

        for _ in range(REPETICIONES):
            inicio = time.perf_counter()
            _, cantidad_comparaciones = insertion_sort(datos)
            fin = time.perf_counter()
            mediciones.append(fin - inicio)

        tiempos.append(sum(mediciones) / REPETICIONES)
        comparaciones.append(cantidad_comparaciones)

    return tiempos, comparaciones


def crear_grafica_comparaciones(resultados: Resultados) -> None:
    """Guarda la gráfica de comparaciones por escenario.

    Args:
        resultados: Mediciones de los tres escenarios.
    """
    plt.figure(figsize=(10, 6))
    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS, datos["comparaciones"], marker="o", label=nombre
        )

    plt.title("Insertion Sort - Comparaciones por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)
    plt.savefig(
        "graficas/parte3_comparaciones.png", dpi=150,
        bbox_inches="tight"
    )
    plt.close()


def crear_grafica_tiempo(resultados: Resultados) -> None:
    """Guarda la gráfica de tiempos promedio por escenario.

    Args:
        resultados: Mediciones de los tres escenarios.
    """
    plt.figure(figsize=(10, 6))
    for nombre, datos in resultados.items():
        plt.plot(TAMANOS, datos["tiempos"], marker="o", label=nombre)

    plt.title("Insertion Sort - Tiempo promedio por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig(
        "graficas/parte3_tiempo.png", dpi=150, bbox_inches="tight"
    )
    plt.close()


def main() -> None:
    """Ejecuta las mediciones y genera las dos gráficas."""
    escenarios: dict[str, Generador] = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Inverso": generar_inverso
    }
    resultados: Resultados = {}

    for nombre, generador in escenarios.items():
        tiempos, comparaciones = medir_escenario(generador, TAMANOS)
        resultados[nombre] = {
            "tiempos": tiempos,
            "comparaciones": comparaciones
        }

    print(f"\nRESULTADOS PARTE 3 - PROMEDIO DE {REPETICIONES} EJECUCIONES")
    print("-" * 70)
    for nombre, datos in resultados.items():
        print(f"\n{nombre}")
        for i, n in enumerate(TAMANOS):
            print(
                f"n={n:5d} | "
                f"comparaciones={datos['comparaciones'][i]:10d} | "
                f"tiempo={datos['tiempos'][i]:.6f} segundos"
            )

    crear_grafica_comparaciones(resultados)
    crear_grafica_tiempo(resultados)
    print("\nGráficas generadas correctamente.")


if __name__ == "__main__":
    main()
