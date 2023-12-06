
# 1.
def summe(k):
    if k == 1: 
        return 1
    else:
        return k+summe(k-1)

print(summe(1), summe(2), summe(3), summe(4), summe(5))

# 2.
def summe2(k):
    if k == 1:
        return 1
    else: 
        return k**2+summe2(k-1)

print(summe2(1), summe2(2), summe2(3), summe2(4), summe2(5))


# 3.
def summe3(k):
    if k == 1:
        return 1
    else:
        return 1/k+summe3(k-1)
    
print(summe3(1), summe3(2), summe3(3), summe3(4), summe3(5))

