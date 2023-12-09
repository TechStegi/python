

def sum(a):
    sum = 0
    for x in a:
        sum = sum + x
    return sum

def schnittmuster(komb):
    liste = []
    while sum(liste) < 220:
        liste.append(23)
    if liste not in komb:
        komb.append(liste)
        return schnittmuster(komb)
    else:
        for i in range(len(liste)):
            if liste[i] != 23:
                liste[i] = 23
            elif liste[i] != 31:
                liste[i] = 31
            elif liste[i] != 39:
                liste[i] = 39
        return schnittmuster(komb)
komb = []
print(schnittmuster(komb))