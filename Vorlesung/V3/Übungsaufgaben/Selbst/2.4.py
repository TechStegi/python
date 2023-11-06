

def summe(m, n):
    s = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            s = s + (i * j)
    return s


print(summe(5, 3))
