# Bucle for
print("y por si no nos vemos...")
for trumanHi in ["Dias","Tardes","Noches"]:
	print("Buenas " + trumanHi,end=" ")

counter=0
userEmail=input("Introduce tu email: ")

for i in userEmail:
	if (i=="@" or i=="."):
		counter=counter+1

if counter==2: # es email==True
	print("El email es correcto")
else:
	print("eL email no es correcto")

for i in range(5):
	print("hola")

for i in range(5,50,5):# Del 5 al 50 de a 5
	print(f"valor de la variable {i}")

valid=False

for i in range(len(userEmail)):
	if userEmail[i]=="@":
		valid=True

if valid:
	print("Email valido")
else:
	print("Email no valido")
