
import math as m

a = 3*m.sqrt(3)
b = (3/2)*m.sqrt(3)

def harmonischesMittel(a, b):
    return (2*a*b)/(a+b)

def geometrischesMittel(a, b):
    return m.sqrt(a*b)

print(harmonischesMittel(a, b))