file = open("RaisingHell.txt", "r").readlines()

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
}

d = {}


# 6.3
def häufigste(n, txt):
    text = ""
    for zeile in txt:
        zeile = zeile.replace("!", "")
        zeile = zeile.replace("?", "")
        zeile = zeile.replace(";", "")
        zeile = zeile.replace(",", "")
        zeile = zeile.replace(".", "")
        zeile = zeile.replace("(", "")
        zeile = zeile.replace(")", "")
        zeile = zeile.replace("'", "")
        zeile = zeile.replace('"', "")
        zeile = zeile.replace('"', "")
        wortliste = zeile.split()
        for w in wortliste:
            w = w.lower()
            w = w.strip()
            if w in d:
                d[w] = d[w] + 1
            else:
                d[w] = 1

    print(valuesortiert(d))
    for i in range(n):
        wort = valuesortiert(d)[0]
        vorkommen = valuesortiert(d)[1]
        print(wort, vorkommen)
        del d[wort]
        del wort
    return "Done"


# 6.2
def valuesortiert(dict):
    values = list(dict.values())
    values.sort()
    values.reverse()
    for k in dict:
        if dict[k] == values[0]:
            return [k, dict[k]]


print(häufigste(5, file))


# 6.4
def maxnkey(d, n):
    l = []
    for i in range(n):
        ch = valuesortiert(d)[0]
        l.append(ch)
        del d[ch]
    l.reverse()
    return l


print(maxnkey(dict, 5))
