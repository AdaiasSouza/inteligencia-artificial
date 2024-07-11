def norma_min_max(atributes, new_min, new_max):
	for row in atributes:
		part_one = ((row - min(atributes))/(max(atributes)-min(atributes)))
		part_two = (new_max-new_min) + new_min

		norma_value = part_one*part_two

		return norma_value

def norma_z_score(atributes):
	 



