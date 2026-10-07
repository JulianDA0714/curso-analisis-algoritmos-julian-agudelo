"""Subarreglo maximo: fuerza bruta y divide y venceras."""


def subarreglo_fuerza_bruta(
    valores: list[float]
) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de dias (i, j).

    Args:
        valores: variacion diaria de caja, una por dia. Tiene al menos
            un elemento.

    Returns:
        Una tupla (inicio, fin, suma) con los indices inclusivos del
        tramo de mayor suma y el valor de esa suma.
    """
    mejor_suma = float("-inf")
    mejor_inicio = 0
    mejor_fin = 0

    for i in range(len(valores)):
        suma_actual = 0

        for j in range(i, len(valores)):
            suma_actual += valores[j]

            if suma_actual > mejor_suma:
                mejor_suma = suma_actual
                mejor_inicio = i
                mejor_fin = j

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float],
    inicio: int,
    medio: int,
    fin: int
) -> tuple[int, int, float]:
    """Encuentra el mejor tramo que cruza el punto medio.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango considerado.
        medio: indice del ultimo elemento de la mitad izquierda.
        fin: indice final del rango considerado.

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo cruzado.
    """
    suma = 0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio

    for i in range(medio, inicio - 1, -1):
        suma += valores[i]

        if suma > mejor_suma_izquierda:
            mejor_suma_izquierda = suma
            mejor_inicio = i

    suma = 0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1

    for j in range(medio + 1, fin + 1):
        suma += valores[j]

        if suma > mejor_suma_derecha:
            mejor_suma_derecha = suma
            mejor_fin = j

    return (
        mejor_inicio,
        mejor_fin,
        mejor_suma_izquierda + mejor_suma_derecha
    )


def subarreglo_maximo(
    valores: list[float],
    inicio: int,
    fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha usando divide y venceras.

    Args:
        valores: variacion diaria de caja.
        inicio: indice inicial del rango a considerar.
        fin: indice final del rango a considerar.

    Returns:
        Una tupla (inicio, fin, suma) del mejor tramo encontrado.
    """
    if inicio == fin:
        return inicio, fin, valores[inicio]

    medio = (inicio + fin) // 2

    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzado = suma_cruzada(valores, inicio, medio, fin)

    if izquierda[2] >= derecha[2] and izquierda[2] >= cruzado[2]:
        return izquierda

    if derecha[2] >= izquierda[2] and derecha[2] >= cruzado[2]:
        return derecha

    return cruzado
