

def summe3(n):
    k=1
    speicher = 0
    while k <= n:
        speicher = speicher + (1/k)
        k = k + 1
    return speicher

print(summe3(5))
    
    