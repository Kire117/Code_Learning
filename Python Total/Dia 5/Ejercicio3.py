def return_true(*args):
    num_list = list(args)
    if num_list.count(0) == 2:
        return True
    else:
        return False


print(return_true(5, 6, 1, 0, 0, 9, 3, 5))
print(return_true(6, 0, 5, 1, 0, 3, 0, 1))

''' Otra forma de hacerlo seria...'''


def ceros_vecinos(*args):
    prev_num = None
    for num in args:
        if num == 0 and prev_num == 0:
            return True
        prev_num = num
    return False

print(return_true(5, 6, 1, 0, 0, 9, 3, 5))
print(return_true(6, 0, 5, 1, 0, 3, 0, 1))


''' Solucion en el curso'''
def ceros_vecinos2(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


print(return_true(5, 6, 1, 0, 0, 9, 3, 5))
print(return_true(6, 0, 5, 1, 0, 3, 0, 1))