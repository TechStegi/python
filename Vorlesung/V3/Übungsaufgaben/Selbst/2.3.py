

def istPerfekt(n):
    summe = 0
    for k in range(1, n/2+1):
        if (n % k == 0):
            summe = summe + k
    return summe == n