def count(text):
    wort = 0
    for zeichen in text:
        if zeichen == " ":
            wort = wort + 1
    if text[len(text) - 1] != " ":
        wort = wort + 1
    return wort


print(count("Das ist ein Satz."))
