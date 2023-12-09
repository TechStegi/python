raisingHell = open("RaisingHell.txt", "r").readlines()
mobyDick = open("MobyDick.txt", "r").readlines()
dieVerwandlung = open("DieVerwandlung.txt", "r").readlines()


def maxindex(liste):
    maxindex = 0
    maxnumber = liste[0]
    for i in range(len(liste)):
        if liste[i] > maxnumber:
            maxnumber = liste[i]
            maxindex = i
        # print("new round", maxindex)
    return maxindex


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
    for i in range(0, 10):
        wordindex = maxindex(anzahl)
        häufigstes_wort = wort[wordindex]
        print(str(i + 1) + ". Wort:", häufigstes_wort, "Vorkommen", anzahl[wordindex])
        del wort[wordindex]
        del anzahl[wordindex]

    # anzahl_kopie = anzahl.copy()
    # return wort, anzahl


# print(zaehlen(raisingHell))
# print(zaehlen(mobyDick))
print(zaehlen(dieVerwandlung))
