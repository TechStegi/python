

def leibniz(n):
    s = 0
    for k in range(n+1):
        s = s + (-1)**k/(2*k+1)
    return s

def recniz(n):
    if n == 0:
        return 1
    else:
        return ((-1)**n)/(2*n+1)+recniz(n-1)
    
print(leibniz(300))
print(recniz(10))