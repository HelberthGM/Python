# Tuples, Listas que no se pueden modificar, NO son necesarios los ()
miTupla=("Alejandro", 5, 12, 2002)
# Desempaquetado de tuple
nombre, dia, mes, agno=miTupla
print(dia,nombre,agno,mes)
# Convertir una tupla a lista
miLista=list(miTupla)
print(miLista)
# Convertir de tupla a lista Igual q arriba solo q tuple en vez de list
# cuantas veces esta un elemento en la lista
print(miTupla.count(12))
# Cuantos elemnetos hay en una tupla
print(len(miTupla))
