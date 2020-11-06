# While es un blucle indeterminado
import math 

n=1

while n <= 10:
	print("Prueba de codigo " + str(n))
	n=n+1 # igual a n+=1

print("Fin de la prueba")

age=int(input("Introduce tu edad: "))

while age<4 or age>110:
	print("Has introducido una edad incorrecta, Vuelve a intentarlo")
	age=int(input("Introduce tu edad: "))

print("Gracias por colaborar.")
print("Edad del aspirante: "+str(age))

# Raiz Cuadrada
print("Programa de Raiz Cuadrada")
number= int(input("Introduce un numero entero: "))
attempts=0

while number<0:
	print ("No se pude hallar la raiz de un numero negativo,seria un numero imaginario")
	if attempts==2:
		print("Has realizado demasiados intentos, Fin del programa")
		break;
	number=int(input("Introduce un numero entero: "))
	if number<0:
		attempts=attempts+1

if attempts<2:
	resolve=math.sqrt(number)
	print("La raíz cuadrada de "+str(number)+" es "+str(resolve))