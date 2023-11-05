def muster3(n):
    # erste Zeile: Nur Sternchen
    for k in range(2 * n):
        print("*", end="")
    print("*")

    # oberer Teil
    for k in range(n):
        # * zu Beginn der Zeile
        print("*", end="")
        # Schleife mit n-k-1 Durchläufen, Sternchen
        for j in range(n - k - 1):
            print("*", end="")
        # Schleife mit 2*k+1 Durchläufen, Leerzeichen
        for j in range(2 * k + 1):
            print(" ", end="")
        # Schleife mit n-k-1 Durchläufen, Sternchen
        for j in range(n - k - 1):
            print("*", end="")
        # * am Ende der Zeile
        print("*")

    # unterer Teil
    for k in range(n - 2, -1, -1):
        # * zu Beginn der Zeile
        print("*", end="")
        # Schleife mit n-k-1 Durchläufen, Sternchen
        for j in range(n - k - 1):
            print("*", end="")
        # Schleife mit 2*k+1 Durchläufen, Leerzeichen
        for j in range(2 * k + 1):
            print(" ", end="")
        # Schleife mit n-k-1 Durchläufen, Sternchen
        for j in range(n - k - 1):
            print("*", end="")
        # * am Ende der Zeile
        print("*")

    # letzte Zeile: Nur Sternchen
    for k in range(2 * n):
        print("*", end="")
    print("*")


muster3(10)
