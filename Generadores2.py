def backCities(*cities): # el * indica quese crea una tupla ilimitada
	for element in cities:
		#for subElement in element:
			yield  from element 

citiesBack=backCities("Bogotá","Cali","Medellin","Cartagena")

print(next(citiesBack))
print(next(citiesBack))
