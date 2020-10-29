class Vehiculos():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, 
        "\nEn marcha:", self.enmarcha,"\nAcelerar", self.acelera,
        "\nFrenar:",self.frena)

class Furgoneta(Vehiculos):

    def carga(self,cargar):
        self.cargado=cargar
        if self.cargado:
            return "La furgoneta esta cargada"
        else:
            return"La furgoneta no está cargada"

# Clase herada de veliculos
class Moto(Vehiculos): 
    caballito=""
    def hcaballito(self):
        self.caballito="Voy haciendo el caballito"

    def estado(self): # se sobreescrobe el metodo heradado.
        print("Marca:", self.marca, "\nModelo:", self.modelo, 
        "\nEn marcha:", self.enmarcha,"\nAcerar", self.acelera,
        "\nFrenar:",self.frena,"\n",self.caballito)

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

miMoto=Moto("Honda","CBR")

miMoto.hcaballito()

miMoto.estado()

miFurgoneta=Furgoneta("Renault","Kangoo")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))
# Herencia Multiple
class BicicletaElectrica(VElectricos,Vehiculos): # Preferencia por el primero
    pass

miBici=BicicletaElectrica("Poseidon","Fixie")

miBici.estado()
#print(isinstance(miBici, Moto) ) #  miBici Perteneca a Moto 