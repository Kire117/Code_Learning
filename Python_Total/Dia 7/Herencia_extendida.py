class Animal():
    def __init__(self, edad , color):
        self.color = color
        self.edad = edad
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"el pajaro vuela {metros} metros")

piolin = Pajaro(2, 'amarillo', 60)
mi_animal = Animal(3, 'naranja')
piolin.nacer()
piolin.hablar()
piolin.volar(100)
