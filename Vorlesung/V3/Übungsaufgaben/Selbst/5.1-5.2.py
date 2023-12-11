def quadrat(x):
    return x * x


def istTeiler(a, b):
    return True if a % b == 0 else False


def potenzen(x, n):
    if n % 2 == 0:
        return (x ** (n / 2)) ** 2
    elif n % 2 != 0:
        return x * x ** (n - 1)
    elif n == 1:
        return x


def potenz(x, n):
    if n == 1:
        return x
    elif istTeiler(n, 2):
        return quadrat(potenz(x, n / 2))
    else:
        return x * potenz(x, n - 1)


def summeDerTeiler(t, summe, n):
    if t == n:
        return summe
        # if summe == n:
        #     return True
        # else:
        #     return False
    else:
        if istTeiler(n, t):
            return summeDerTeiler(t + 1, summe + t, n)
        else:
            return summeDerTeiler(t + 1, summe, n)


def vollkommen(zahl):
    return zahl == summeDerTeiler(1, 0, zahl)


print(vollkommen(6))

# def vollkommen(zahl):
#     s = 0
#     for i in range(1, zahl):
#         if istTeiler(zahl, i):
#             s = s + i
#     return True if s == zahl else False
