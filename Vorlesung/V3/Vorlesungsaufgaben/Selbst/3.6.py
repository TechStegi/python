

def a(x, y):
    x = 3*x - 4*y
    return x

def b(x, y):
    x = a(x, y) + a(y, x)
    y = x*x
    return y

x = 2
y = 5

z = b(x, y)
print(z)

# 1. Zuweisen des Endwerts der Funktion b mit den Argumenten x und y
# 1.1 Aufrufen der Funktion b mit den Argumenten x und y, das heißt 2 und 5
# 1.2 Aufrufen der Funktion a(x, y) und a(y, x) in der Funktin b(x, y), und Zuweisen des Endwerts zu der Variable x in b(x,y)
# 2.1 Die Funktion a(2, 5) liefert den Wert -14
# 2.2 Die Funktion a(5, 2) liefert den Wert 7
# 3.1 Die Variable x in der Funktion b(2, 5) erhält den Wert -7
# 3.2 Die Funktion b(2, 5) liefert den Wert 49
# 4. Die Variable z erhält den Wert der Funktion b(2, 5), also 49, und wird ausgedruckt
