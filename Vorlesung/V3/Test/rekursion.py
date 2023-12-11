# def fakultaet(n):
#     if n <= 1:
#         return 1
#     if n > 1:
#         return n*fakultaet(n-1)

# print(fakultaet(5))


def fakit(produkt, zaehler, ende):
    if zaehler > ende:
        return produkt
    if zaehler <= ende:
        return fakit(produkt * zaehler, zaehler + 1, ende)

def fak(n):
    return fakit(1, 1, n)

print(fak(5))

def quadrat(x):
    return x*x

def istTeiler(a, b):
    return True if a % b == 0 else False

def potenz(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        return quadrat(potenz(x, (n/2)))
    else:
        return x * potenz(x, n-1)
    
print(potenz(2, 3))

