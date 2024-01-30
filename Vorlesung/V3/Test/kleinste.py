


a = [4, 3, 9, 5, 2, 1]

def größte(l):
    min = l[0]
    index = 0
    for i in range(1, len(l)):
        if l[i] < min:
            min = l[i]
            index = i
    return min, index

print(größte(a))