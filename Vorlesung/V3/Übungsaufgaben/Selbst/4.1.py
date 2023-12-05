


def umkehren(s):
    a = ""
    for i in range(len(s)-1, -1, -1):
        a = a + s[i]
    return a

print(umkehren("test"))


def entfernen(s, c):
    a = ""
    for i in range(len(s)):
        if s[i] != c:
            a = a + s[i]
    return a

print(entfernen("Alle L löschen", "l"))

