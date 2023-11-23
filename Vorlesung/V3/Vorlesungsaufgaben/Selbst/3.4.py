liste = [14, 10, 5, 20, 14, 12, 15, 10]


def replaceall(a, x, y):
    for element in a:
        if element == x:
            a[a.index(x)] = y
    return a

print(replaceall(liste, 14, 4))


def removeAll(a, x):
    i = 0
    while i < len(a):
        if a[i] == x:
            del a[i]
        else:
            i = i + 1
    return a
print(removeAll(liste, 4))

