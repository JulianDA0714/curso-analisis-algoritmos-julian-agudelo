import random
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
SEMILLA = 42


def generar_datos(n: int) -> list[int]:
    generador = random.Random(SEMILLA + n)
    return [generador.randint(-100, 100) for _ in range(n)]


def medir_tiempo(funcion, *args) -> tuple[tuple[int, int, float], float]:
    inicio = time.perf_counter()
    resultado = funcion(*args)
    fin = time.perf_counter()

    return resultado, fin - inicio


def main():
    tiempos_fuerza_bruta = []
    tiempos_divide_venceras = []

    print("\nRESULTADOS DE MEDICION")
    print("-" * 70)

    for n in TAMANOS:
        valores = generar_datos(n)

        resultado_fuerza, tiempo_fuerza = medir_tiempo(
            subarreglo_fuerza_bruta,
            valores
        )

        resultado_divide, tiempo_divide = medir_tiempo(
            subarreglo_maximo,
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

    plt.title("Tiempo de ejecución vs tamaño de entrada")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
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