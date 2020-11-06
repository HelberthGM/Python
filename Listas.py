fruits=["Fresa", "Manzana", "Naranja", "Mora", 5, True, 20.25]*2

# Agregar elementos
fruits.append("Pera")
# Agregar elemento en cierto indice
fruits.insert(2,"Maracuya")
# Concatenar una lista
fruits.extend(["Uvas","Sandia","Mango"])
# Eliminar elemntos
fruits.remove(5)
# Eliminar el ultimo elemento
fruits.pop()

# Lista completa
print(fruits[:])
# Elemento especifico de la lista[elemento a acceder]
print(fruits[2])
# Porcion de lista
print(fruits[0:2])
# Indice de un elemento
print(fruits.index("Mora"))
# Comoprobar si hay un elemnto en la lista
print("Mora" in fruits)

