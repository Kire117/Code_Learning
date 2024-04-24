from pathlib import Path

base = Path.home()
# path lo que hace es transformar objetos, es este caso, colecciones de string a un formato de ruta de acceso
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_familia.txt"))
guia2 = guia.with_name("la_pedrera.txt")
print(guia)
print(guia2)
print(base)

print(guia.parent.parent.parent)
print("antes del for loop")
guia3 = Path(Path.home(), "PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 6\\Europa")

# glob es una metodo global y * significa todos
# al agregar mas astericos, es decir, "**/*.txt" le dara acceso a todos los archivos y subdirectorios
for txt in Path(guia3).glob("**/*.txt"):
    print(txt)
guia4 = Path("Europa", "España", "Barcelona",
             "sagrada_familia.txt")

en_europa = guia4.relative_to(Path("Europa"))
en_espania = guia4.relative_to(Path("Europa", "España"))
# el metodo relative_to regresa un nuevo objeto path relacionado con el argumento indeterminado
print("metodo relative_to")
print(en_europa)
print(en_espania)