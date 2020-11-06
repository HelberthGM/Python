# Numeros pares
# Con Función
#def pares (limit):
	#num=1
	#myList=[]

	#while num<limit:
		#myList.append(num*2)
		#num=num+1
	#return myList

#print(pares(10))

# Con Generador
def pair(end):

	number=1

	while number<end:
		yield number*2
		number=number+1

backPairs=pair(10)

print(next(backPairs))

print("Aqui puede ir mas codigo")

print(next(backPairs))

print("Aqui puede ir mas codigo")

print(next(backPairs))

print("Aqui puede ir mas codigo")

print(next(backPairs))

#for i in devuelvePares:
	#print(i)