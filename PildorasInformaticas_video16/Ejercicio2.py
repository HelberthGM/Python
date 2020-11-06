# Contraseña especifica
counter=0
password=input("Inserte su nueva contraseña con minimo 8 caracteres sin espacios: ")

for i in range(len(password)):
	if password[i]==" ":
		counter=1

if len(password)<8 or counter>0 :
	print("Contraseña errónea")
else:
	print("Contraseña OK")
