
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza (self):
        print("voy caminando") 

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Ando moviendome en bicicleta")               

def main():

    persona = Persona("David")
    persona.avanza()

    ciclista = Ciclista("Anita")
    ciclista.avanza()




if __name__ == "__main__":
    main()        