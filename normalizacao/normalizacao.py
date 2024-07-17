class Normalizacao():

    """docstring for Normalizacao"""

    def __init__(self, atribute):
        self.atribute = atribute

    def norma_min_max(atribute, new_min, new_max):

        for row in atribute:
            part_one = (
                (row - min(atribute)) / (max(atribute) - min(atribute)))
            part_two = (new_max - new_min) + new_min

            norma_value = part_one * part_two

            return norma_value

    def norma_z_score(atributes):
        pass

    def normal_decimal():
        pass

    def norma_robust():
        pass

    def norma_log():
        pass

    def __str__(self):
        pass


x = [1, 2, 4, 100, 34]
c = Normalizacao(x)
print(c)
