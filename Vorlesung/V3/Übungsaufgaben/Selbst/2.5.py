

def summe(n):
    s = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            s = s + j
    return s

print(summe(3))

