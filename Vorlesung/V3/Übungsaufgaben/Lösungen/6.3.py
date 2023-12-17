 # Initialisierung
n = 100
prim = {}
prim [0] = False
prim [1] = False

for i in range(2,n+1):
    prim[i] = True

# Sieben
for i in range(2, n+1 ):
    if prim[i]:
        for j in range(2*i, n+1, i):
            prim[j] = False
    
# Ergebnis ausgeben
print("Primzahlen zwischen 1 und",n)
for k in prim:
    if prim[k]:
        print(k, end=' ')

