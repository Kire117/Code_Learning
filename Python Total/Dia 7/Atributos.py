class Pajaro:
    alas = True  # atributo de clase

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro('naranja', 'Tucan')  # atributo de instancia

print(mi_pajaro.especie)
print(mi_pajaro.color)
print(f"mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
print("la siguiente linea es un atributo de clase")
print(Pajaro.alas)
print("la siguiente linea es un atributo de instancia")
print(mi_pajaro.alas)
