import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_algoritmo(algoritmo, datos):
    inicio = time.perf_counter()
    resultado, comparaciones = algoritmo(datos)
    fin = time.perf_counter()

    return resultado, comparaciones, fin - inicio


def main():
    tiempos_insertion = []
    tiempos_merge = []

    comparaciones_insertion = []
    comparaciones_merge = []

    for n in TAMANOS:
        datos = generar_aleatorio(n)

        _, comp_insertion, tiempo_insertion = medir_algoritmo(
            insertion_sort,
            datos
        )

        _, comp_merge, tiempo_merge = medir_algoritmo(
            merge_sort,
            datos
        )

        tiempos_insertion.append(tiempo_insertion)
        tiempos_merge.append(tiempo_merge)

        comparaciones_insertion.append(comp_insertion)
        comparaciones_merge.append(comp_merge)

    print("\nRESULTADOS PARTE 4")
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

    plt.plot(
        TAMANOS,
        tiempos_insertion,
        marker="o",
        label="Insertion Sort"
    )

    plt.plot(
        TAMANOS,
        tiempos_merge,
        marker="o",
        label="Merge Sort"
    )

    plt.title("Comparación de tiempo: Insertion Sort vs Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/parte4_tiempo.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()

    print("\nGráfica generada correctamente.")


if __name__ == "__main__":
    main()