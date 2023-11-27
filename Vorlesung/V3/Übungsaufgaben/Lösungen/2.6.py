from math import sqrt
from math import pi


def harmonischesMittel(a, b):
    return (2 * a * b) / (a + b)


def geometrischesMittel(a, b):
    return sqrt(a * b)


a = 3 * sqrt(3)
b = (3 / 2) * sqrt(3)

for n in range(30):
    a = harmonischesMittel(a, b)
    b = geometrischesMittel(a, b)
    print(n, a, b, pi - a, pi - b)
