menor = min(1,2,3,4,5)
mayor = max(1,2,3,4,5)
print(menor)
print(mayor)

mi_lista= [58, 96, 72, 64, 35]
print(f"el menor es {min(mi_lista)} y el mayor es {max(mi_lista)}")


nombres = ['juan', 'pablo', 'alicia','carlos']
print(min(nombres)) #lo que funciona aqui es que tomara la primera letra en orden alfabetico, por ejemplo,
# la persona que tiene la letra a en su nombre es alicia, es por eso que dara como autput el nombre de alicia

#OJO con este dato------------------------
nombre = 'CArlos'
print(min(nombre)) # cuando en el string exista una letra mayuscula siempre dara como output dicha letra, de igual forma,
# en orden alfabetico

dic = {'c1': 45, 'c2': 11}
print(min(dic))

print(min(dic.values()))
