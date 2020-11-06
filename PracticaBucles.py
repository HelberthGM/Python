# Continue
name="Pildoras informaticas"
counter=0
print(len(name))
for letter in name:
	if letter==" ":
		continue
	counter+=1
	print(counter)

# Pass , Rompe un bucle, hace un clase nula,no se tiene en cuenta

# Else , Funciona cuando el bucle termina
email=input("introduce tu email: ")
arroba=False

for i in email:
	if i=="@":
		a=True
		break;# Al llegar al la @ se acaba el bucle
else:
	arroba=False

print(arroba)