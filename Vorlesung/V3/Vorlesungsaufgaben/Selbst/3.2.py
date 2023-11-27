

liste = [13, 10, 5, 20, 14, 12, 15, 10]


def maxindex(a):
    s = a[0]
    index = 0
    for i in range(1, len(a)): 
        if s < a[i]:
            s = a[i]
            index = i
    return index

print("maxindex", maxindex(liste))


def minindex(a):
    s = a[0]
    index = 0
    for i in range(1, len(a)):
        if s > a[i]:
            s = a[i]
            index = i
    return index

print("minindex", minindex(liste))