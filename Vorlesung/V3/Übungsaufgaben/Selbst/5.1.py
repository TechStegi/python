def quadrat(x):
    return x * x


def istTeiler(a, b):
    return True if a % b == 0 else False


print(istTeiler(2, 1))


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


# bei potenz(2, 0) kommt 1 raus, 0 durch 2 ist 0 --> kein Rest, gerade Zahl --> 2 hoch 0/2 sind 1, 1 hoch 2 sind 1 --> Ergebnis: 1
