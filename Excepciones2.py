import math

def evaluateAge(edad):

    if edad < 0:
        raise TypeError("No se permiten edades negativas")

    if edad < 18:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "Cuidate..."

#print(evaluateAge(-20))

# Prueba 2

def raizCuadrada (num1):
    if num1<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))

try:
    print(raizCuadrada(op1))
except ValueError as ErrorNumeroNegaativo:
    print(ErrorNumeroNegaativo)

print("Fin del programa")