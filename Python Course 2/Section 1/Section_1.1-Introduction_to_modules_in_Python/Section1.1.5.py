# 1.1.5 Importing a module: continued

import math

print(math.sin(math.pi / 2))


# math.pi
# math.sin()

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.1416

print(sin(pi / 2))
print(math.sin(math.pi / 2))

print(math.e)

# new technique
from math import sin, pi

print(sin(pi / 2))

pi = 3.1416


def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None


print(sin(pi / 2))

# Another test
pi = 3.1416


def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None


print(sin(pi / 2))

from math import sin, pi

print(sin(pi / 2))