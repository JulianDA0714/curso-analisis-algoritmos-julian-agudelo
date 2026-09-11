import time
import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import (
    generar_aleatorio,
    generar_casi_ordenado,
    generar_inverso
)


TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def medir_escenario(generador, tamanos):
    tiempos = []
    comparaciones = []

    for n in tamanos:
        datos = generador(n)

        inicio = time.perf_counter()
        _, cantidad_comparaciones = insertion_sort(datos)
        fin = time.perf_counter()

        tiempos.append(fin - inicio)
        comparaciones.append(cantidad_comparaciones)

    return tiempos, comparaciones


def crear_grafica_comparaciones(resultados):
    plt.figure(figsize=(10, 6))

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["comparaciones"],
            marker="o",
            label=nombre
        )

    plt.title("Insertion Sort - Comparaciones por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/parte3_comparaciones.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def crear_grafica_tiempo(resultados):
    plt.figure(figsize=(10, 6))

    for nombre, datos in resultados.items():
        plt.plot(
            TAMANOS,
            datos["tiempos"],
            marker="o",
            label=nombre
        )

    plt.title("Insertion Sort - Tiempo de ejecución por escenario")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)

    plt.savefig(
        "graficas/parte3_tiempo.png",
        dpi=150,
        bbox_inches="tight"
    )

    plt.close()


def main():
    escenarios = {
        "A - Aleatorio": generar_aleatorio,
        "B - Casi ordenado": generar_casi_ordenado,
        "C - Inverso": generar_inverso
    }

    resultados = {}

    for nombre, generador in escenarios.items():
        tiempos, comparaciones = medir_escenario(
            generador,
            TAMANOS
        )

        resultados[nombre] = {
            "tiempos": tiempos,
            "comparaciones": comparaciones
        }

    print("\nRESULTADOS PARTE 3")
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