

i = 0
n = 5
speicher = 0
while i <= n:
    speicher = speicher + (2*i+1)/(2*i+1 + (-1)**i)
    i = i + 1
print(speicher)


storage = 0
for j in range(6):
    storage = storage + (2*j+1)/(2*j+1 + (-1)**j)
print(storage)


