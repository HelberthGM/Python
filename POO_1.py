class Carro():
    def __init__(self): #Constructor, el estado inicial de los objetosConstructor, el estado inicial de los objetos
# se Encapsulo con __, no es accesible afuera de la clase
        self.__largoChasis=250 # 4 Propiedades
        self.__anchoChasis=120
        self.__ruedas=4 
        self.__enmarcha=False 

    def arrancar(self,arrancamos):   # 3Comportamientos, arrancar y estado
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeoInterno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__enmarcha and chequeo==False):
                return "Hay un error en el chequeo, No podemos arrancar."
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas. Tiene un ancho de", self.__anchoChasis,"y un largo de", self.__largoChasis)

    def __chequeoInterno(self):
        print("Realizando chequeo interno...")

        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"
        
        if (self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False

miCoche=Carro()

print(miCoche.arrancar(True))

miCoche.estado()

print("---------------- Creación del Segundo Objeto -------------------")

miCoche2=Carro()

print (miCoche2.arrancar(False))

miCoche2.__ruedas=3

miCoche2.estado()