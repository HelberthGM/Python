# Flujo de ejecucion, Condicionales
print ("Evalucion de Notas de Alumnos")
gradeAlum = int(input("Intorduce la nota del alumno: "))

def evaluation(grade):
	evaluate= "Felicitaciones aprobaste!!"
	if grade < 5:
		evaluate="Perdiste, suerte a la proxima"
	return evaluate

print (evaluation(gradeAlum))