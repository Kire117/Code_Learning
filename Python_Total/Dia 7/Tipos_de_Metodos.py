class Pajaro():
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    # metodos de instancia
    def piar(self):
        print('pio')

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} mts")
        self.piar()
    #metodos de instancia
    def pintar_nregro(self):
        self.color = 'negro'
        print(f"el pajaro es {self.color}")

    # metodo de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        ''' sin embargo los metodos de clase pueden modificas a los atributos de clase como a continuacion'''
        cls.alas = False
        print(Pajaro.alas) # output = False

    # metodo estatico
    @staticmethod # estos metodos no se refieren ni a la clase ni a la instancia, tampoco pueden acceder tanto a
    # los atributos de instancia como tampoco los atributos de clase
    def mirar():
        print("El pajaro mira")



############ Metodos de instancia
piolin = Pajaro('amarillo', 'canario')
piolin.pintar_nregro()
piolin.volar(5)

piolin.alas = False
print(piolin.alas)
#########################
# Metodos de clase
#si no existiese una instancia como tal, se puede llamar directamente el metodo de clase con el objeto, es decir
Pajaro.poner_huevos(3) #donde poner_huevos es un metodo de clase
# los metodos de clase no pueden accede a los atributos de la instancia

# metodo static
Pajaro.mirar()
