

def summe1(n):
    s = 0
    for i in range(1, n+1):
        s = s+i
    return s

print(summe1(5))


def summe2(n):
    s = 0
    k = 1
    while k < n+1:
        s = s+k
        k = k + 1
    return s

print(summe2(5))
        

def summe_rekursiv(n):
    if n == 1:
        return 1
    else:
        return n+summe_rekursiv(n-1)
    
print(summe_rekursiv(5))



def textaufgabe():
    s = ""
    liste = ["hello", "i", "am", "michael"]
    for i in range(len(liste)):
        s = s + liste[i] + " "
    return s


print(textaufgabe())
    