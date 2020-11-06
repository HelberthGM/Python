# Diccionarios 
countriesCapitals={"Alemania":"Berlin","Colombia":"Bogota","Francia":"Paris","España":"Madrid"}
#print (countriesCapitals["Alemania"])
# Agregar elementos
countriesCapitals["Italia"]="Lisboa"
# Modificar valores, se sobreescriben
countriesCapitals["Italia"]="Roma"
# Eliminar elementos
del countriesCapitals["España"]

diccionario1={"Cristiano": 7,"Apellido":"Ronaldo","Balon de oro":{"años":[2012,2013,2014,2015,2016]}}
print(diccionario1.keys())
print(diccionario1.values())
print(len(diccionario1))
print(diccionario1["Balon de oro"])