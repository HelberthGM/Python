age = int(input("Inserta tu edad: "))

if  0 < age < 150:
	print("La edad es correcta")
else:
	print("La edad es incorrecta")

salariy_president=int(input("Introduce salario del Presidente: "))
print("Salario del Presidente:" + str(salariy_president))

salariy_director=int(input("Introduce salario del Director: "))
print("Salario del Director:" + str(salariy_director))

salariy_area_boss=int(input("Introduce salario del Jefe de Área: "))
print("Salario del Jefes de Área:" + str(salariy_area_boss))

salariy_admin=int(input("Introduce salario del Administrativo: "))
print("Salario del Administrativo:" + str(salariy_admin))

if salariy_president>salariy_director>salariy_area_boss>salariy_admin:
	print("Todo bien, Todo correcto")
else:
	print("Aqui hay gato encerrado 🙄🙄")

print("Programa de becas imaginarias")

distance = int(input("Introduce la distancia a la universidad en Km: "))
print(distance,"Km")

brosOrSist= int(input("Introduce el numero de hermanos: "))
print(brosOrSist)

familySalary=int(input("Introduce el salario anual bruto: "))
print(familySalary,"Pesos")

if distance>40 and brosOrSist>2 or familySalary<=2000000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")

print("Asignaturas optativas imaginarias")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la Asignatura escogida: ")
Asignatura=opcion.lower()

if Asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
	print("Asignatura elegida: "+Asignatura)
else:
	print("La asignatura elegida no esta contemplada")

