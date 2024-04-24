monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

respuesta = 'y'

while respuesta == 'y':
    respuesta = input("Continue? (y/n) ")
else:
    print("Gracias")

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        break
    print(letra)

print("\n Second loop")
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)