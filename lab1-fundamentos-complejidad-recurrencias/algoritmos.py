def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """
    Ordena una lista de enteros de mayor a menor utilizando
    el algoritmo de ordenamiento por inserción.

    Retorna:
        - Una nueva lista ordenada.
        - La cantidad de comparaciones entre elementos.
    """

    resultado = datos.copy()
    comparaciones = 0

    for i in range(1, len(resultado)):
        clave = resultado[i]
        j = i - 1

        while j >= 0:
            comparaciones += 1

            if resultado[j] < clave:
                resultado[j + 1] = resultado[j]
                j -= 1
            else:
                break

        resultado[j + 1] = clave

    return resultado, comparaciones