import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """
    Genera n índices de riesgo distintos en orden aleatorio.
    """
    datos = list(range(1, n + 1))

    generador = random.Random(semilla)
    generador.shuffle(datos)

    return datos


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """
    Genera aproximadamente un 98% de datos ordenados
    y un 2% de nuevos resultados desordenados.
    """
    datos = list(range(n, 0, -1))

    cantidad_nuevos = max(1, int(n * 0.02))

    parte_ordenada = datos[:-cantidad_nuevos]
    nuevos = datos[-cantidad_nuevos:]

    generador = random.Random(semilla)
    generador.shuffle(nuevos)

    return parte_ordenada + nuevos


def generar_inverso(n: int) -> list[int]:
    """
    Genera los datos en el orden contrario al requerido.
    """
    return list(range(1, n + 1))