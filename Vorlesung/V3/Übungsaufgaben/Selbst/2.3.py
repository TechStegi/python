

def vollkommen(zahl):
    summe = 0
    for k in range(1, zahl):
        if (zahl % k == 0):
            summe = summe + k
    return summe == zahl



print(vollkommen(6))


