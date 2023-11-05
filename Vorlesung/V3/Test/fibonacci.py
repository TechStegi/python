
def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a = b # nach 1. Runde: a = 1, b = 2
        b = a+b # nach 2. Runde: a = 2, b = 2+2 = 4
    return a

print(fib(2))