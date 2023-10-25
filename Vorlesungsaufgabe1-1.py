import math as m


# Aufgabe 1.1
def f(a, b, c):
    x = 9813 * a + 1233 * b
    y = m.sqrt(c * x)
    z = (x + y) / (a * b * c)
    a = (x * y) / z
    b = x + y + z
    c = 2 * x + 2 * y + 2 * z
    y1 = (-b + m.sqrt((b * b) - 4 * a * c)) / (2 * a)
    y2 = (-b - m.sqrt((b * b) - 4 * a * c)) / (2 * a)
    x = abs(y1 - y2)
    return x


print("Ergebnis Aufgabe 1.1:", f(1, 2, 3))


# Aufgabe 1.2
def betrag_berechnen(x):
    return abs(x)


print("Berechneter Betrag:", betrag_berechnen(-5))


def größere(x, y):
    if x < y:
        return y
    elif x == y:
        return str(x) + " und " + str(y) + " sind gleich groß"
    else:
        return x


print("Größte Zahl:", größere(5, 5))


def kleinste(x, y, z):
    if x <= y and x <= z:
        return x
    else:
        if y <= z:
            return y
        else:
            return z


print("Kleinste Zahl:", kleinste(11, 3, 23))


def betrags_größte(x, y, z):
    if abs(x) > y and abs(x) > z:
        return x
    elif abs(y) > x and abs(y) > z:
        return y
    elif abs(z) > y and abs(z) > x:
        return z


print("Betragsgrößte Zahl:", betrags_größte(-20, 5, -3))


# Aufgabe 1.3


def wert(x, y):
    if x < 1 / 3 and (y < 1 / 3 or y > 2 / 3):
        w = 0
    elif x > 2 / 3 and (y < 1 / 3 or y > 2 / 3):
        w = 2
    elif x >= 1 or y >= 1:
        return "Values are too high! Enter a value lower than 1"
    elif x == 1 / 3 or x == 2 / 3 or y == 1 / 3 or y == 2 / 3:
        return "These borders are not defined. Please enter a decimal number and no fractions."
    else:
        w = 1
    return w


print("Grenze:", wert(1.2, 0.4))


# Aufgabe 1.4


def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def mal(x, y):
    return x * y


def geteilt(x, y):
    return x / y


print(
    "Ergebnis Arithmetische Rechnung:",
    int(plus(mal(plus(3, 9), 4), geteilt(minus(17, 5), 3))),
)

# Zusatz: Ich gehe von der äußersten Klammer zur innersten Klammer der Funktion(en)
