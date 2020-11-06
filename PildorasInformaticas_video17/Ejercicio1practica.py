number1=int(input("Inserte el primer numero entero: "))
number2=int(input("Inserte el segundo numero: "))

while number1<number2:
	number1=number2
	number2=int(input("Inserte un número mayor que "+str(number1)+": "))
print(number2,"No es mayor que",number1)
