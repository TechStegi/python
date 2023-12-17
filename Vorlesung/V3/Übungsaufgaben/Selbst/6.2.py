# x = {"one":1, "unique": 5, "hi":True, "for alle": "yes", "one":1, "hi": True}
x = ["hi", 5, True, "was geht", "hi", True, 5]


def duplikateentfernen(x):
    d = {}
    for el in x:
        d[el] = 1
    keys = list(d.keys())
    return keys


print(duplikateentfernen(x))
