# Correo electronico, NO esta terminado
email=input("Inserte su email: ")
countA=0
countP=0

for i in range(len(email)):
	if email[i]=="@":
		countA=countA+1
	if email[i]==".":
		countP=1

print(countP,countA)

if countP==0 or countA!=1:
	print ("El email no es valido")
else:
	print("El email es valido")
