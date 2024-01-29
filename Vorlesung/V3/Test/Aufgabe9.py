

def q(a):
    b = a.copy()
    for i in range(len(b)):
        b[i] = b[i]**2
    return b

a = [1, 2, 3, -4, -5]
print(q(a))