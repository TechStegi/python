
# 4.4

file = open("RaisingHell.txt", "r").readlines()
print(file)
def clean(text):
    b = "hello".split('\n')
    print(b)
    index = 0
    characters_to_replace = [".", ",", ";", "!", "?", ":", "'", "-"]
    whitespaces_to_replace = []
    n = 6
    for i in range(2, n):
        whitespaces_to_replace.append(" "*i)
        
    for zeile in text:
        if "\n" in zeile:
            zeile = zeile.replace("\n", " ")
            text[index] = zeile
        for x in whitespaces_to_replace:
            zeile.replace(x, " ")
            text[index] = zeile
        for char in characters_to_replace:
            zeile = zeile.replace(char, "")
            text[index] = zeile
            print(zeile)
        for zeichen in zeile: 
            if zeichen.isupper():
                zeile = zeile.replace(zeichen, zeichen.lower())
                print(zeile)
                text[index] = zeile
        index += 1

    return text

    
    # for i in range(len(text)):
    #     if text[i] != "\n":
print(clean(file))
