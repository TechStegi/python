
arr = [3, 10, 5, 20, 14, 12, 15, 10]

def max(a):
    s = a[0]
    for i in range(1, len(a)):
        if s < a[i]:
            s = a[i]
    return s

print(max(arr))


def min(a):
    s = a[0]
    for i in range(1, len(a)):
        if s > a[i]:
            s = a[i]
    return s 

print(min(arr))

