
def summe2(n):
    k = 1
    speicher = 0
    while k <= n:
        speicher = speicher + (k * k)
        k = k + 1
    return speicher

print(summe2(5))


