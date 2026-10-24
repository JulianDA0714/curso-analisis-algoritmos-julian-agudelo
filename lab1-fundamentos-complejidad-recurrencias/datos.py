"""Generadores reproducibles de datos para las pruebas."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera índices de riesgo distintos en orden aleatorio.

    Args:
        n: Cantidad de índices que se generan.
        semilla: Semilla para reproducir el orden aleatorio.

    Returns:
        Una lista con los números de 1 a n, mezclados.
    """
    datos = list(range(1, n + 1))
    generador = random.Random(semilla)
    generador.shuffle(datos)
    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera una lista descendente con el tramo final mezclado.

    Args:
        n: Cantidad de índices que se generan.
        semilla: Semilla para reproducir el tramo mezclado.

    Returns:
        Una lista con aproximadamente el 98 % inicial ordenado.
    """
    datos = list(range(n, 0, -1))
    cantidad_nuevos = max(1, int(n * 0.02))
    parte_ordenada = datos[:-cantidad_nuevos]
    nuevos = datos[-cantidad_nuevos:]
    generador = random.Random(semilla)
    generador.shuffle(nuevos)
    return parte_ordenada + nuevos


def generar_inverso(n: int) -> list[int]:
    """Genera índices en orden contrario al requerido.

    Args:
        n: Cantidad de índices que se generan.

    Returns:
        Una lista ascendente desde 1 hasta n.
    """
    return list(range(1, n + 1))
