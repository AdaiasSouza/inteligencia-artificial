from math import sqrt


class Distancias():

    """docstring for Distancias"""

    def __init__(self, x_atribute, y_atribute):
        self.x_atribute = x_atribute
        self.y_atribute = y_atribute

    def euclidian_distance(self):
        """ Retorna distância euclidiana entre dois pontos """
        try:
            distance = sqrt(
                sum(
                    [pow((row_0 - row_1), 2)
                        for row_0, row_1
                        in zip(self.x_atribute,
                               self.y_atribute)]))
            return distance
        except Exception as e:
            return f'Erro: {e}'

    def manhattan_distance(self):
        """ Retorna a distância manhattan entre dois pontos"""
        try:
            distance = sum(
                [abs((row_0 - row_1))
                    for row_0, row_1
                    in zip(self.x_atribute, self.y_atribute)])
            return distance
        except Exception as e:
            return f'Erro: {e}'

    def chebyshev_distance(self):
        """ Retorna a distancia de Chebyshev entre dois pontos"""
        try:

            distance = max(
                [abs((row_0 - row_1))
                 for row_0, row_1
                 in zip(self.x_atribute, self.y_atribute)])
            return distance
        except Exception as e:
            return f'Erro: {e}'
