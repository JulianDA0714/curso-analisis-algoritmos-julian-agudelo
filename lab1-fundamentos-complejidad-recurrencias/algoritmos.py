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

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """
    Ordena una lista de enteros de mayor a menor utilizando
    Merge Sort.

    Retorna:
        - Una nueva lista ordenada.
        - La cantidad de comparaciones entre elementos.
    """

    if len(datos) <= 1:
        return datos.copy(), 0

    mitad = len(datos) // 2

    izquierda, comparaciones_izquierda = merge_sort(datos[:mitad])
    derecha, comparaciones_derecha = merge_sort(datos[mitad:])

    resultado = []
    comparaciones_merge = 0

    i = 0
    j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones_merge += 1

        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    total_comparaciones = (
        comparaciones_izquierda
        + comparaciones_derecha
        + comparaciones_merge
    )

    return resultado, total_comparaciones