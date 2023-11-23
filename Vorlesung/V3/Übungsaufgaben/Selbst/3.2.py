#3.2.1
n = 5
liste = []
for i in range(1, n+1):
    liste.append(i**2)

print(liste)

#3.2.2
a = []
def differenz(a):
    d = 0
    for i in range(1, len(liste)):
        d = liste[i] - liste[i-1]
        a.append(d)
    return a

print(differenz(a))


#3.3
def pascal(n):
    n = 6
    s = 0
    z = 1
    for i in range(n+1):
        s = s + z
        z = z*2
    return s

print(pascal(n))

def pascal2(n):
    p = [1]
    print(p)

    for i in range(1, n):
        p = p + [1]
        neu = [1] * len(p)
        for j in range(1, len(p)-1):
            neu[j] = p[j-1] + p[j]
        p = neu
        print(p)
pascal2(5)