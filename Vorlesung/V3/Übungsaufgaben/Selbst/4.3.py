def mediumwordlength(text):
    length_of_one_word = 0
    avg = 0
    runs = 0
    zeichen = 0
    for i in range(len(text)):
        if text[i] != " ":
            zeichen += 1
        else:
            runs = runs + 1
            avg = avg + zeichen
            zeichen = 0
    # für das letzte Wort
    avg = avg + zeichen
    if text[-1] != " ":
        runs = runs + 1

    # gesammelte wortzahl durch anzahl der wörter teilen --> Durchschnittslänge der Worte
    avg = avg / runs

    return avg, runs


print(mediumwordlength("Thisd notes ra"))
