"""Pruebas de lista enlazada y tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash


def probar_busquedas() -> None:
    """Verifica busquedas exitosas e infructuosas."""
    lista = ListaEnlazada()
    tabla = TablaHash(7)

    lista.insertar(1000000010, "en bodega")
    tabla.insertar(1000000010, "en bodega")

    assert lista.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000010) == "en bodega"

    assert lista.buscar(1000000099) is None
    assert tabla.buscar(1000000099) is None

    assert lista.tamano == 1
    assert tabla.tamano == 1


def probar_colisiones() -> None:
    """Verifica tres guias que caen en la misma casilla."""
    tabla = TablaHash(7)

    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3

    for guia in (10, 24, 17):
        assert tabla.buscar(guia) == "en bodega"

    assert tabla.casillas[3].tamano == 3
    assert tabla.tamano == 3
    assert tabla.factor_carga() == 3 / 7
    assert tabla.buscar(99) is None


def probar_colecciones_aleatorias() -> None:
    """Compara las estructuras en veinte colecciones aleatorias."""
    azar = random.Random(42)
    estados = ["en bodega", "en reparto", "entregado"]

    for _ in range(20):
        lista = ListaEnlazada()
        tabla = TablaHash(53)

        guias = azar.sample(range(10**9, 10**9 + 10000), 30)
        registros = []

        for guia in guias:
            estado = azar.choice(estados)
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            registros.append((guia, estado))

        for guia, estado in registros:
            assert lista.buscar(guia) == estado
            assert tabla.buscar(guia) == estado

        inexistentes = azar.sample(
            range(2 * 10**9, 2 * 10**9 + 10000), 10
        )

        for guia in inexistentes:
            assert lista.buscar(guia) is None
            assert tabla.buscar(guia) is None

        assert lista.tamano == 30
        assert tabla.tamano == 30


def main() -> None:
    """Ejecuta todas las pruebas del laboratorio."""
    probar_busquedas()
    probar_colisiones()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    main()
