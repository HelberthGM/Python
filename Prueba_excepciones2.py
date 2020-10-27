def divide():
    try:
        num1=(float(input("Introduce el primer numero: ")))
        num2=(float(input("Introduce el segundo numero: ")))
        print("La division es:" + str(num1/num2))
    except ValueError:
        print("Valor introducido erroneo, Solo se aceptan numeros.")
    except ZeroDivisionError:
        print("No se puede dividir entre 0. Tal vez es igual a Infinito.")
    finally: # Se ejecuca siempre, haya o no un error
        print("Calculo finalizado")

divide()