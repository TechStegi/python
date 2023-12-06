raisingHell = open("RaisingHell.txt", "r").readlines()
mobyDick = open("MobyDick.txt", "r").readlines()
dieVerwandlung = open("DieVerwandlung.txt", "r").readlines()


def zaehlen(text):
    new_file = []
    wort = []
    anzahl = []
    for zeile in text:
        new_file = new_file + zeile.split()
    # gehe durch die Wörter der Liste new_file
    for i in range(len(new_file)):
        # update jedes Wort auf dasselbe Wort ohne ein Satzzeichen
        new_file[i] = new_file[i].replace(".", "")
        new_file[i] = new_file[i].replace(",", "")
        new_file[i] = new_file[i].replace(";", "")
        new_file[i] = new_file[i].replace("!", "")
        new_file[i] = new_file[i].replace("?", "")
        new_file[i] = new_file[i].replace(":", "")
        new_file[i] = new_file[i].replace("'", "")
        new_file[i] = new_file[i].replace("-", "")
        # prüfe ob das wort new_file[i] bereits in die wort-Liste aufgenommen wurde
        # wenn ja, schaue an welchem index new_file[i] in der wort-Liste bereits enthalten ist, und erhöhe die Anzahl des Wortes um 1
        if new_file[i] in wort:
            index = wort.index(new_file[i])
            anzahl[index] += 1
        else:
            # wenn nein, dann füge das wort new_file[i] an das Ende der Liste wort an, und füge 1 an das Ende der Liste anzahl an
            wort.append(new_file[i])
            anzahl.append(1)

    # suche in der anzahl-Liste nach dem größten Wert, dieser ist gleich dem häufigsten Wort
    höchste = 0
    for i in range(1, len(anzahl)):
        if anzahl[i] > anzahl[i - 1]:
            höchste = anzahl[i]
    print(höchste)

    # anzahl_kopie = anzahl.copy()
    # print("Wort:", wort, "Vorkommen", anzahl)
    # return wort, anzahl


# print(zaehlen(raisingHell))
# print(zaehlen(mobyDick))
print(zaehlen(dieVerwandlung))
