

zahlen = {'drei':3, 'eins':1, 'neun':9, 'zwei':2}

print("unsortiert")
for k in zahlen:
    print(k, zahlen[k])        
    

def valuesortiert(dict):
    values = list(dict.values())
    values.sort()
    for v in values:
        for k in dict:
            if dict[k] == v:
                print(k, dict[k])

print("nach value sortiert")
valuesortiert(zahlen)

print("nach keys sortiert")

def keysortiert(dict):
    keys = list(dict.keys())
    keys.sort()
    for k in keys:
        print(k, dict[k])
keysortiert(zahlen)
