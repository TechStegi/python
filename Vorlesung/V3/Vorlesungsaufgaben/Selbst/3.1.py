
arr = [3, 10, 5, 20, 14, 12, 15, 10]

def max(a):
    s = 0
    for i in range(len(a)):
        if s < a[i]:
            s = a[i]
    return s

print(max(arr))


def min(a):
    s = 100
    for i in range(len(a)):
        if s > a[i]:
            s = a[i]
    return s 

print(min(arr))

