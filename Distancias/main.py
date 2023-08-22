from math import sqrt
from scipy.spatial.distance import euclidean
from numpy import random
from matplotlib.pyplot as plt

def euclidian_distance(atributes_a, atributes_b):
	""" Retorna distância euclidiana entre dois pontos"""		
	distance = sqrt(sum([ pow((row_0-row_1), 2) for row_0, row_1 in zip(atributes_a, atributes_b)])) 
	return distance
	

def manhattan_distance(atributes_a, atributes_b):
	""" Retorna a distância manhattan entre dois pontos"""
	return None 

def chebyshev_distance(atributes_a, atributes_b):
	""" Retorna a distancia de Chebyshev entre dois pontos"""
	return None



def main():
	"""Metodo principal de chamada para os demais métodos"""

	# gerando valores aleatórios para as entradas dos métodos
	x_0 = random.randint(10, size=5)
	x_1 = random.randint(10, size=5)

	print("Distância: ")
	print("x_0 -> ", x_0)
	print("x_1 -> ", x_1)
	print("Módulo Scipy: ",euclidean(x_0, x_1))
	print("Método criado: ", euclidian_distance(x_0, x_1))
	




if __name__ == '__main__':
	main()