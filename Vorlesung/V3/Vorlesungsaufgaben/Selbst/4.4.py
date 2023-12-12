# 4.4

file = open("RaisingHell.txt", "r").readlines()


def clean(text):
    b = "hello".split("\n")
    print(b)
    index = 0
    characters_to_replace = [".", ",", ";", "!", "?", ":", "'", "-"]
    whitespaces_to_replace = []
    n = 6
    for i in range(2, n):
        whitespaces_to_replace.append(" " * i)

    for zeile in text:
        if "\n" in zeile:
            zeile = zeile.replace("\n", " ")
            text[index] = zeile
        for char in characters_to_replace:
            zeile = zeile.replace(char, "")
            text[index] = zeile
        for zeichen in zeile:
            if zeichen.isupper():
                zeile = zeile.replace(zeichen, zeichen.lower())
                text[index] = zeile
        index += 1
    text = "".join(text)
    for x in whitespaces_to_replace:
        text = text.replace(x, " ")
    return text

    # for i in range(len(text)):
    #     if text[i] != "\n":


print(clean(file))
