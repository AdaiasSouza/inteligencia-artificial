from numpy import random
from distancias import Distancias


def main():
    """Metodo principal de chamada para os demais métodos"""

    # gerando valores aleatórios para as entradas dos métodos

    x_0 = random.randint(1000, size=100)
    x_1 = random.randint(1000, size=100)
    random.seed(42)

    d = Distancias(x_0, x_1)

    print("Distancia Euclidiana: ")
    print(d.euclidian_distance())
    print("\n")

    print("Distancia Manhattan: ")
    print(d.manhattan_distance())
    print("\n")

    print("Distancia Chebyshev: ")
    print(d.chebyshev_distance())
    print("\n")


if __name__ == '__main__':
    main()
