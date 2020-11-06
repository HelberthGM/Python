# Numero mayor
number1 = int(input("Inserte el primer numero: "))
number2 = int(input("Inserte el segundo numero: "))

def devuelveMax(number1, number2) :
	if number1 > number2:
		print ("El numero mayor es",number1)
	elif number2 > number1:
		print ("El numero mayor es",number2)
	else:
		print ("Ambos numeros son iguales")

devuelveMax(number1, number2)