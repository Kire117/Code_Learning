class Pajaro():
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f"El pajara ha volado {metros} mts")

piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(15)