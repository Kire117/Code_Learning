from pathlib import Path, PureWindowsPath

carpeta = Path('C:/Users/Aleja/PycharmProjects/pythonProject/Code Learning/Python Total/Dia 6/otra_carpeta/Prueba1.txt')

print(carpeta.read_text())
print(carpeta.name)  # dara como output el nombre del archivo
print(carpeta.suffix)
'''dara como output el sufijo es decir, la extension del archivo, en este caso tenemos un  archivo de texto, 
el output sera .txt'''
print(carpeta.stem) # dara como output el nombre del archivo sin la extension
''' Metodo para ver psi el archivo no existe'''

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe!")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)




