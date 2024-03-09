serie = 'N-02'

match serie:
    case 'N-01':
        print('Samsung')
    case 'N-02':
        print('Nokia')
    case ' N-03':
        print('Motorola')
    case _:
        print('No existe ese producto')


cliente = {'nombre': 'Kire', 'edad':19, 'ocupacion':'Programmer'}

pelicula = {'titulo': 'Matrix', 'ficha-tecnica': {'protagonista': 'Keanu Reeves', 'director': 'Lana y lilly '
                                                                                                 'wachowski'}}

elementos = [cliente, pelicula, 'libro']
for e in elementos:
    match e:
        case{'nombre': nombre,
             'edad': edad,
             'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion)

        case {'titulo': titulo,
              'ficha-tecnica': {'protagonista': protagonista,
                                 'director': director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No es que es esto")
