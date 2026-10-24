"""Compara el rendimiento de Insertion Sort y Merge Sort."""

import time
from collections.abc import Callable

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 5
Algoritmo = Callable[[list[int]], tuple[list[int], int]]


def medir_algoritmo(
    algoritmo: Algoritmo, datos: list[int]
) -> tuple[list[int], int, float]:
    """Ejecuta el algoritmo cinco veces y calcula el tiempo promedio.

    Args:
        algoritmo: Función de ordenamiento que se medirá.
        datos: Lista de entrada, igual en todas las repeticiones.

    Returns:
        La lista ordenada, las comparaciones y el tiempo promedio.
    """
    mediciones = []
    resultado = []
    comparaciones = 0

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        resultado, comparaciones = algoritmo(datos)
        fin = time.perf_counter()
        mediciones.append(fin - inicio)

    return resultado, comparaciones, sum(mediciones) / REPETICIONES


def main() -> None:
    """Mide ambos algoritmos y genera la gráfica comparativa."""
    tiempos_insertion = []
    tiempos_merge = []
    comparaciones_insertion = []
    comparaciones_merge = []

    for n in TAMANOS:
        datos = generar_aleatorio(n)
        orden_insertion, comp_insertion, tiempo_insertion = medir_algoritmo(
            insertion_sort, datos
        )
        orden_merge, comp_merge, tiempo_merge = medir_algoritmo(
            merge_sort, datos
        )
        assert orden_insertion == orden_merge

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)
        comparaciones_insertion.append(comp_insertion)
        comparaciones_merge.append(comp_merge)

    print(f"\nRESULTADOS PARTE 4 - PROMEDIO DE {REPETICIONES} EJECUCIONES")
    print("-" * 80)
    for i, n in enumerate(TAMANOS):
        print(
            f"n={n:5d} | "
            f"Insertion: {tiempos_insertion[i]:.6f}s | "
            f"Merge: {tiempos_merge[i]:.6f}s | "
            f"Comp. Insertion: {comparaciones_insertion[i]:10d} | "
            f"Comp. Merge: {comparaciones_merge[i]:10d}"
        )

    plt.figure(figsize=(10, 6))
    plt.plot(TAMANOS, tiempos_insertion, marker="o", label="Insertion Sort")
    plt.plot(TAMANOS, tiempos_merge, marker="o", label="Merge Sort")
    plt.title("Tiempo promedio: Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.savefig("graficas/parte4_tiempo.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("\nGráfica generada correctamente.")


if __name__ == "__main__":
    main()
