def find(text, x):
    n = 0
    while n < len(text) - len(x):
        i = 0
        while i < len(x) and n + i < len(text) and text[n + i] == x[i]:
            i = i + 1
        if i == len(x):
            print("gefunden")
            return
        n = n + 1
    print("nicht gefunden")


file = open("simpleText.txt", "r")
text = file.read()
x = "are"

find(text, x)
