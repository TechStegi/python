
def valuesortiert(dict):
    values = list(dict.values())
    values.sort()
    values.reverse()
    for k in dict:
        if dict[k] == values[0]:
            return [k, dict[k]]

print(valuesortiert({"hello":1, "hi": 3}))