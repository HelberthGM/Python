# Flujo de ejecucion, Condicionales, IF Else
print ("Verificacion de edad")

age = int(input("Cuantos años tienes? "))

if age < 18:
	print ("No puedes acceder al sistema")
elif age > 110:
	print("Error de edad")
else:
 	print("Puedes acceder al sistema.")

print ("FIN")