import math as m


# Aufgabe 1.1
def f(a, b, c):
    x = 9813 * a + 1233 * b
    y = m.sqrt(c*x)
    z = (x+y) / (a*b*c)
    a = x*(y/z)
    b = x + y + z
    c = 2*x + 2*y + 2*z
    y1 = (-b + m.sqrt(b*b - 4*a*c)) / (2*a)
    y2 = (-b - m.sqrt(b*b - 4*a*c)) / (2*a)
    x = abs(y1-y2)
    return x    

# print(f(1, 2, 3))


#Aufgabe 1.2
def betrag(x):
    return abs(x)

print(betrag(-5))


def größere(x, y):
    if x > y:
        return x
    else:
        return y    
    
# print(größere(5, 9))


def kleinste(x, y, z):
    if x > y and y < z:
        return y
    elif x > z:
        return z
    else:
        return x

# print(kleinste(3, 6, 1))


def betragsgrößte(x, y, z):
    if abs(x) > abs(y) and abs(x) > abs(z):
        return x
    elif abs(y) > abs(x) and abs(y) > abs(z):
        return y
    else:
        return z
    
# print(betragsgrößte(-5, 6, -20))


#Aufgabe 1.3
def wert(x, y):
    if (x <= 1/3 and y <= 1/3) or (x <= 1/3 and y > 2/3):
        return 0
    elif (x > 2/3 and y < 1/3) or (x > 2/3 and y > 2/3):
        return 2
    else:
        return 1
    
    
print(wert(0.7, 0.8))

# - + * /
# m.sqrt(zahl)
# abs(zahl)
    