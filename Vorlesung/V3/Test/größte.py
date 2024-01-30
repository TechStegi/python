

a = [4, 3, 9, 5, 2, 1]

def größte(l):
    max = l[0]
    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            max = l[i]
    return max

print(größte(a))