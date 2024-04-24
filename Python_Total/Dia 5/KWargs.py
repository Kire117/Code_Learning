def suma(**kwargs):
    total = 0
    print(type(kwargs))
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=3, y=5, z=2))


def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

''' los args tambien pueden admitir lista y los kwargs pueden admitir diccionarios ya que hacen el cast por defecto
con dichos valores. args(list) kwargs(dict) '''

args = [10,20,30,40,50]
kwargs= {'a':'one', 'b':'two', 'c':'three'}
print(suma(x=3, y=5, z=2))
prueba(15, 50, 100, 200, 300, 400, x='uno', y='dos', z='tres')
prueba(1 ,2 , *args, **kwargs)