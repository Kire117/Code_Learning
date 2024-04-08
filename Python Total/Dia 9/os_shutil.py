import shutil, send2trash, os

# shutil.move("C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia "
            #"9\\Proyecto+del+Día+9.pdf",
            #'/Python Total/Dia 9/PDF')

# send2trash.send2trash('C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia
# 9\\texto.txt')

path = "C:\\Users\\Aleja\\PycharmProjects\\pythonProject\\Code Learning\\Python Total\\Dia 9"

for carpeta, subcarpeta, archivo in os.walk(path):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')