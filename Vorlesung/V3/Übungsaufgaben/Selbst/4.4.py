text = open("simpleText.txt", "r").readlines()


def extracount(file):
    zeilen_count = 0
    wörter_count = 0
    zeichen_count = 0

    for zeile in file:
        # zähle Zeilen
        zeilen_count += 1

        # zähle Wörter
        for i in range(1, len(zeile)):
            if zeile[i] == " ":
                wörter_count += 1
        if zeile[-1] != " ":
            wörter_count += 1

        # zähle Zeichen
        for zeichen in zeile:
            zeichen_count += 1
    return zeilen_count, wörter_count, zeichen_count


print(extracount(text))
