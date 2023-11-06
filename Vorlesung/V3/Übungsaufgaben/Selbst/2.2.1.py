
def summe1(n):
    s = 0
    for k in range(1, n+1, 1):
        s = s + k**2
    return s

print(summe1(3))