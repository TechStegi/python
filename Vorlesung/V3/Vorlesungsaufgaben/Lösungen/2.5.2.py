# wie viele Leerzeichen und * stehen in Zeile k

# k   Leerzeichen     *
# 1   3               1
# 2   2               3
# 3   1               5
# 4   0               7

# n ist die Zahl der Zeilen für das obere Dreieck, hier n = 4

# Anzahl der Leerzeichen --> n-k-1
# Anzahl der * --> 2*k+1


def muster2(n):
    # oberer Teil
    for k in range(n):
        # Schleife mit n-k-1 Durchläufen, Leerzeichen
        for j in range(n - k - 1):
            print(" ", end="")
        # Schleife mit 2*k+1 Durchläufen, Sternchen
        for j in range(2 * k + 1):
            print("*", end="")
        # Zeilenumbruch
        print("")

    # unterer Teil
    for k in range(n - 2, -1, -1):
        # Schleife mit n-k-1 Durchläufen, Leerzeichen
        for j in range(n - k - 1):
            print(" ", end="")
        # Schleife mit 2*k+1 Durchläufen, Sternchen
        for j in range(2 * k + 1):
            print("*", end="")
        # Zeilenumbruch
        print("")


muster2(5)
