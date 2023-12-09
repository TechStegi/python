file_path = "simpleText.txt"

file = open(file_path, "r")
text = file.readlines()

# text =  ["hallio ich heißße tim", "ich mag fußball"]

simple_text = open("simpleText.txt", "r").readlines()


# 4.1
def count_upper_letters():
    zeichen_count = 0
    for zeile in text:
        for zeichen in zeile:
            if zeichen.isupper():
                zeichen_count += 1
    return zeichen_count


print(count_upper_letters())


# 4.2
def count():
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    count = 0
    for zeile in simple_text:
        for zeichen in zeile:
            if zeichen == "a":
                a = a + 1
            if zeichen == "e":
                e = e + 1
            if zeichen == "i":
                i = i + 1
            if zeichen == "o":
                o = o + 1
            if zeichen == "u":
                u = u + 1
    return (a, e, i, o, u)


print(count())


# 4.3
def singles(some_text):
    print("vorher:", some_text)
    new_text = ""
    for zeile in some_text:
        new_line = zeile[0]
        for i in range(1, len(zeile)):
            if zeile[i] != zeile[i - 1]:
                new_line += zeile[i]
        new_text += new_line + "\n"
    return new_text


print(singles(simple_text))


# 4.5
def find(insert_text):
    x = "are st"
    count = 0
    for zeile in insert_text:  # durch jede Zeile = Array Element
        for i in range(len(zeile)):  # durch jedes Zeichen der Zeile
            if zeile[i] == x[0]:
                count = 1
                for j in range(1, len(x)):  # erstes Zeichen von x wurde in insert_text an der Position gefunden, vergleiche ab da jedes Zeichen von x mit jedem Zeichen von insert_text an den Positionen i+j nach dem ersten gefunden Buchstaben
                    if i + j < len(zeile) and zeile[i + j] == x[j]:
                        count += 1
                    else:
                        count = 0
                        break
                    if count == len(x):
                        return "Gefunden"
    return "Keine Zeichenkette x gefunden."


print(find(simple_text))
