number=int(input("Intoduce un numero positivo: "))
suma=0

while number>0:
	suma=number+suma
	number=int(input("Intoduce otro numero positivo:"))
print ("La suma de todos los numero intoducidos es",suma)