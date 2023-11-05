import time

# from math import sqrt


# 64 Nachkommastellen von pi
pi64 = 3.1415926535897932384626433832795028841971693993751058209749445923

# n = 1000
# mypi = 0
# fehlerschranke = abs(pi - mypi) > 0.0001
# von Gottfried Wilhelm Leibnitz
# def leibnitz(n):
#     mypi = 0
#     for k in range(n+1):
#         mypi = mypi + (-1)**k/(2*k+1)
#     return mypi


def leibnitz2(eps):
    wert = 0.0
    k = 0
    while abs(wert * 4 - pi64 > eps):
        wert = wert + ((-1) ** k) / (2 * k + 1)
        k = k + 1
    return wert * 4


# von Kelallur Nilakantha Somayaji
# def somayaji(n):
#     run1 = n*4
#     b = 3
#     s2 = 0
#     for l in range(3, run1+1, 4):
#         b = b + 4/(l**3-l)
#         s2 = s2 - 4/((l+2)**3-(l+2))
#         mypi = b + s2
#     return mypi


def somayaji2(eps):
    mypi = 3
    k = 1
    while abs(mypi - pi64) > eps:
        mypi = mypi + ((-1) ** (k + 1) * 4) / ((2 * k + 1) ** 3 - (2 * k + 1))
        k = k + 1
    return mypi


fehlergrenze = 10 ** (-6)

for i in range(12):
    fehlergrenze = 10 ** (-i)
    print("*" * 10, fehlergrenze, "*" * 10)
    tic = time.perf_counter()
    print("Leibniz:   Abweichung", leibnitz2(fehlergrenze) - pi64)
    toc = time.perf_counter()
    print("           Berechnungsdauer", toc - tic, "Sekunden")

    tic = time.perf_counter()
    print("Somayaji:  Abweichung", somayaji2(fehlergrenze) - pi64)
    toc = time.perf_counter()
    print("           Berechnungsdauer", toc - tic, "Sekunden")
