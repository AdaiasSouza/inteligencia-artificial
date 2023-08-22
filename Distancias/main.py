from math import sqrt
from scipy.spatial.distance import euclidean, cityblock, chebyshev
from numpy import random


def euclidian_distance(atributes_a, atributes_b):
	""" Retorna distância euclidiana entre dois pontos"""	

	distance = sqrt(sum([ pow((row_0-row_1), 2) for row_0, row_1 in zip(atributes_a, atributes_b)])) 
	return distance
	

def manhattan_distance(atributes_a, atributes_b):
	""" Retorna a distância manhattan entre dois pontos"""

	distance = sum([ abs((row_0-row_1)) for row_0, row_1 in zip(atributes_a, atributes_b)])
	return distance

def chebyshev_distance(atributes_a, atributes_b):
	""" Retorna a distancia de Chebyshev entre dois pontos"""

	distance = max([ abs((row_0-row_1)) for row_0, row_1 in zip(atributes_a, atributes_b)])
	return distance



def main():
	"""Metodo principal de chamada para os demais métodos"""

	# gerando valores aleatórios para as entradas dos métodos
	x_0 = random.randint(1000, size=100)
	x_1 = random.randint(1000, size=100)

	print("Distância: ")
	print("x_0 -> ", x_0)
	print("x_1 -> ", x_1)
	print("\n")

	print("Distancia Euclidiana: ")
	print("Módulo Scipy Euclidean: ",euclidean(x_0, x_1))
	print("Método criado: ", euclidian_distance(x_0, x_1))
	print("\n")
	
	print("Distancia Manhattan: ")
	print("Módulo Scipy Cityblock: ", cityblock(x_0, x_1))
	print("Método criado: ", manhattan_distance(x_0, x_1))
	print("\n")	


	print("Distancia Chebyshev: ")
	print("Módulo Scipy Chebyshev: ", chebyshev(x_0, x_1))
	print("Método criado: ", chebyshev_distance(x_0, x_1))
	print("\n")	

if __name__ == '__main__':
	main()