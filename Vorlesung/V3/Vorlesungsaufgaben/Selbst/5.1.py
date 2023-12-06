

def f(x):
    if x < 3:
        return 1
    elif x % 2 == 0:
        return f(x-1)+1
    else:
        return f(x-1)*(x-1)
    
print(f(3), f(4), f(5), f(6), f(7), f(8), f(9))


def g(x):
    if x > 10:
        return 10
    elif x <= 0:
        return 0
    elif x % 2 == 0:
        return (g(x-1)+g(x+1))/2
    else:
        return x/2

print(g(3), g(4), g(5), g(6), g(7), g(8), g(9))


def h(x):
    if x <= 1:
        return 1
    elif h(x-1) > x:
        return h(x-1)-2
    elif h(x-1) == x:
        return h(x-2)
    elif h(x-1) < x:
        return h(x-1) + 3

print(h(3), h(4), h(5), h(6), h(7), h(8), h(9))

