

def a(x, y):
    x = x + 2*y
    b = 2 + x
    return b * b

def b(x, y):
    d = a(x+2, y-2)
    if y > 0:
        e = b(x+y, -2)
    z = x
    x = y
    y = z
    return x+y

def c(u, v):
    x = a(u, v) + b(v, u)
    return x 

x = 1
y = 2 
z = 3

z = c(x, y)
print(z)


# 1. Aufrufen der Funktion c(1, 2)
# 2.1 Aufrufen der Funktion a(1, 2) und b(2, 1) sowie Zuordnen der Summe der beiden Endwerte zu der Variable x
# 3.1 a(1, 2) liefert den Wert 49
# 3.2 b(2, 1) liefert den Wert ... 
# 3.3 c(1, 2) liefert ...