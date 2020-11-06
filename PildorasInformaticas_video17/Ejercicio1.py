welcome=print("Bienvenido al programa, Inserte numeros cada vez mayores")
number=int(input("Inserte el primer numero entero: "))

while number>0:
	number1=int(input("Inserte el siguiente numero: "))
	print("Numero anterior ",str(number)," Siguiente numero ",str(number1))
	number=number1
	print(number)
	print(number1)

	if number<0 or number1<0:
		print("Error, Solo se aceptan numeros positivos")
	if number<number1:
		print("Fin del programa")
		break;	
