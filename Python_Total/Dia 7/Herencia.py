class Animal():
    def __init__(self, edad, color):
        self.color = color
        self.edad = edad


    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass

piolin = Pajaro(2, 'amarillo')

piolin.nacer()

print(piolin.color)