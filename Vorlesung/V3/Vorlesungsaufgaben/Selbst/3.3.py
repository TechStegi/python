liste = [13, 10, 5, 20, 14, 12, 15, 10]


def tausch(a, i, j):
    a[i], a[j] = a[j], a[i]
    return (a[i], a[j])

print(tausch(liste, 2, 4))


