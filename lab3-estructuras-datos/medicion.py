"""Mediciones de busqueda en lista enlazada y tabla hash."""

import random
import time
from pathlib import Path

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash


REPETICIONES = 3
BUSQUEDAS = 200
ESTADOS = ["en bodega", "en reparto", "entregado"]


def generar_guias(n: int, semilla: int = 42) -> list[int]:
    """Genera guias distintas de diez digitos.

    Args:
        n: Cantidad de guias.
        semilla: Semilla para reproducir los datos.

    Returns:
        Lista de guias sin repetidos.
    """
    azar = random.Random(semilla)
    return azar.sample(range(10**9, 10**10), n)


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cuantas guias inexistentes generar.
        semilla: Semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []

    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)

    return inexistentes


def es_primo(numero: int) -> bool:
    """Determina si un numero es primo.

    Args:
        numero: Numero que se desea evaluar.

    Returns:
        True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False

    divisor = 2

    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 1

    return True


def primo_cercano(numero: int) -> int:
    """Busca un numero primo igual o mayor al indicado.

    Args:
        numero: Valor desde el cual se busca.

    Returns:
        El primer numero primo encontrado.
    """
    candidato = max(2, numero)

    while not es_primo(candidato):
        candidato += 1

    return candidato


def medir_busquedas(
    estructura: ListaEnlazada | TablaHash,
    guias: list[int],
) -> float:
    """Mide el tiempo medio de busquedas inexistentes.

    Args:
        estructura: Lista enlazada o tabla hash.
        guias: Guias inexistentes que se consultaran.

    Returns:
        Tiempo medio por busqueda en segundos.
    """
    tiempos: list[float] = []

    for _ in range(REPETICIONES):
        inicio = time.perf_counter()

        for guia in guias:
            estructura.buscar(guia)

        fin = time.perf_counter()
        tiempos.append((fin - inicio) / len(guias))

    return sum(tiempos) / len(tiempos)


def experimento_a() -> None:
    """Compara los tiempos de lista enlazada y tabla hash."""
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []

    print("EXPERIMENTO A - LISTA FRENTE A TABLA")

    for n in tamanos:
        guias = generar_guias(n)
        existentes = set(guias)
        inexistentes = generar_guias_inexistentes(
            existentes, BUSQUEDAS
        )

        lista = ListaEnlazada()
        m = primo_cercano(n // 2)
        tabla = TablaHash(m)

        for guia in guias:
            lista.insertar(guia, "en bodega")
            tabla.insertar(guia, "en bodega")

        for guia in guias[:10]:
            assert lista.buscar(guia) == tabla.buscar(guia)

        tiempo_lista = medir_busquedas(lista, inexistentes)
        tiempo_tabla = medir_busquedas(tabla, inexistentes)

        tiempos_lista.append(tiempo_lista * 1000)
        tiempos_tabla.append(tiempo_tabla * 1000)

        print(
            f"n={n}, m={m}, alfa={tabla.factor_carga():.3f}, "
            f"lista={tiempo_lista * 1000:.6f} ms, "
            f"tabla={tiempo_tabla * 1000:.6f} ms"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, marker="s", label="Tabla hash")
    plt.title("Tiempo de busqueda: lista enlazada vs tabla hash")
    plt.xlabel("Numero de guias (n)")
    plt.ylabel("Tiempo medio por busqueda (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/lista_vs_tabla.png")
    plt.close()


def experimento_b() -> None:
    """Mide el efecto del factor de carga sobre la busqueda."""
    n = 20000
    factores = [0.5, 1, 4, 10]
    tiempos: list[float] = []
    alfas_reales: list[float] = []

    guias = generar_guias(n)
    inexistentes = generar_guias_inexistentes(
        set(guias), BUSQUEDAS
    )

    print("\nEXPERIMENTO B - FACTOR DE CARGA")

    for alfa in factores:
        m = primo_cercano(round(n / alfa))
        tabla = TablaHash(m)

        for guia in guias:
            tabla.insertar(guia, "en bodega")

        for guia in guias[:10]:
            assert tabla.buscar(guia) == "en bodega"

        tiempo = medir_busquedas(tabla, inexistentes)
        alfa_real = tabla.factor_carga()

        alfas_reales.append(alfa_real)
        tiempos.append(tiempo * 1000)

        print(
            f"m={m}, alfa={alfa_real:.3f}, "
            f"tiempo={tiempo * 1000:.6f} ms"
        )

    plt.figure(figsize=(9, 5))
    plt.plot(alfas_reales, tiempos, marker="o", label="Tabla hash")
    plt.title("Tiempo de busqueda segun el factor de carga")
    plt.xlabel("Factor de carga (alfa = n / m)")
    plt.ylabel("Tiempo medio por busqueda (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("graficas/tiempo_vs_alfa.png")
    plt.close()


def main() -> None:
    """Ejecuta los experimentos y genera las graficas."""
    Path("graficas").mkdir(exist_ok=True)

    experimento_a()
    experimento_b()

    print("\nGraficas generadas correctamente.")


if __name__ == "__main__":
    main()
