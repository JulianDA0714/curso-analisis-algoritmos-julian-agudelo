import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def probar_serie_ejemplo():
    valores = [-3, 5, -2, 8, -6, 3, 9, -4]

    fuerza_bruta = subarreglo_fuerza_bruta(valores)
    divide_venceras = subarreglo_maximo(valores, 0, len(valores) - 1)

    assert fuerza_bruta[2] == 17
    assert divide_venceras[2] == 17


def probar_un_elemento():
    valores = [8]

    assert subarreglo_fuerza_bruta(valores)[2] == 8
    assert subarreglo_maximo(valores, 0, 0)[2] == 8


def probar_todos_negativos():
    valores = [-8, -3, -10, -2, -6]

    assert subarreglo_fuerza_bruta(valores)[2] == -2
    assert subarreglo_maximo(valores, 0, len(valores) - 1)[2] == -2


def probar_todos_positivos():
    valores = [2, 4, 1, 5, 3]
    suma_esperada = 15

    assert subarreglo_fuerza_bruta(valores)[2] == suma_esperada
    assert (
        subarreglo_maximo(valores, 0, len(valores) - 1)[2]
        == suma_esperada
    )


def probar_caso_cruzado():
    valores = [-4, 6, 3, -2, 5, -8]

    fuerza_bruta = subarreglo_fuerza_bruta(valores)
    divide_venceras = subarreglo_maximo(valores, 0, len(valores) - 1)

    assert fuerza_bruta[2] == 12
    assert divide_venceras[2] == 12


def probar_listas_aleatorias():
    random.seed(42)

    for _ in range(20):
        tamano = random.randint(5, 30)
        valores = [random.randint(-100, 100) for _ in range(tamano)]

        fuerza_bruta = subarreglo_fuerza_bruta(valores)
        divide_venceras = subarreglo_maximo(
            valores, 0, len(valores) - 1
        )

        assert fuerza_bruta[2] == divide_venceras[2]


def main():
    probar_serie_ejemplo()
    probar_un_elemento()
    probar_todos_negativos()
    probar_todos_positivos()
    probar_caso_cruzado()
    probar_listas_aleatorias()

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()