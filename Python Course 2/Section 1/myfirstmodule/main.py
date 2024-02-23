from module import suml, prodl
from sys import path

path.append('..\\myfirstmodule')
# print(module.counter) output = 0
import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.suml(zeroes))
print(module.prodl(ones))






