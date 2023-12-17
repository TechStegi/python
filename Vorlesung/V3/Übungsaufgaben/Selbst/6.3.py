def primzahlen(n):
    d = {}
    teiler = 0

    d[0], d[1] = False, False
    for i in range(2, n + 1):
        d[i] = True  # 3: True
        print(i, d[i])
        for j in range(2, i + 1):  # für j werden 2 und 3 durchlaufen
            if (i % j == 0):  # 3 / 2 = 1.5 --> Rest von 0.5, nächste runde # 3 / 3 = 1, kein Rest
                teiler += 1  # teiler = 2
                if teiler > 1:
                    d[i] = False
                    print("hier kam es rein", i)
        if d[i] == True:
            for k in range(2*i, n+1, i):
                d[k] = False
        teiler = 0
    return d


print(primzahlen(10))
