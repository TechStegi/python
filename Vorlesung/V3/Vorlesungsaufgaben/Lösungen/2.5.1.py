
# i steht für die Zeilen, j für die Sternchen, n für die gewollte Anzahl an Sternchen in der mittleren Reihe

def muster1(n):
    # oberes Dreieck
    for i in range(n):  # i-Schleife ist für den Zeilenwechsel zuständig
        for j in range(i+1): # j-Schleife ist für die Anzahl der Sternchen zuständig
            print("*", end='')
        print() 

    # unteres Dreieck
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            print("*", end='')
        print("")
        
muster1(10)


