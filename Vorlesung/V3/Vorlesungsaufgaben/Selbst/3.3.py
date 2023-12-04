liste = [13, 10, 5, 20, 14, 12, 15, 10]
print(liste)

def tausch(a, i, j):
    a[i], a[j] = a[j], a[i]
    return (a[i], a[j])

tausch(liste, 2, 4)
print(liste)
tausch(liste, 2, 4)


def tausch2(a, i, j):
    if i < 0 or j < 0:
        print("tausch: Mindestens ein Index ist zu klein")
        return
    if i >= len(a) or j >= len(a):
        print("Mindestens ein Index ist zu groß")
        return
    
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return (a[i], a[j])

tausch2(liste, 2, 4)
print(liste)