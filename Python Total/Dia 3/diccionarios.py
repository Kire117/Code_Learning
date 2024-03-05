diccionario = {'c1': 'valor1', 'c2': 'valor2'}
print(type(diccionario))

resultado = diccionario['c2']
print(resultado)

cliente = {'nombre': 'Kire', 'apellido': 'Ovando', 'peso': 67, 'altura': 1.75}
consulta = cliente['apellido']
print(consulta)

dic = {'c1': 55, 'c2': [10, 20, 30], 'c3': {'s1': 100, 's2': 200}}
print(dic['c2'][1])
print(dic['c3']['s2'])


n_dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}

print(n_dic['c2'][1].upper())

n1_dic = {1: 'a', 2: 'b'}
print(n1_dic)
n1_dic[3] = 'c'
print(n1_dic)
n1_dic[2] = 'B'
print(n1_dic)

print(n1_dic.keys())
print(n1_dic.values())
print(n1_dic.items())