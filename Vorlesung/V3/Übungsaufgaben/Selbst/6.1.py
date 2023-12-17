d1 = {"hello": 1, "wassup": 3, "i am nice": 6, "generalist": "yes"}
d2 = {"oil": 2.0, "brown": False, "specialist": 10, "monoton": True}


# 6.1.1
def merge(a, b):
    neu = {}
    for el in a:
        neu[el] = a[el]
    for el2 in b:
        neu[el2] = b[el2]
    return neu

print(merge(d1, d2))


# 6.1.2
zahlen = {"y": 5, "z": 8, "x": 6, "k": 10}

def dictmin(x):
    values = list(x.values())
    minvalue = values[0]
    for s in x:
        if x[s] <= minvalue:
            minvalue = x[s]
            minkey = s
    return minkey

print(dictmin(zahlen))


