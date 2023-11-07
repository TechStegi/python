

# t = 3, a = 2, b = 3
# t = 7, a = 3, b = 7
# t = 22, a = 7, b = 22


# 1 + 4 + 9 = 14

k = 1
s = 0
for i in range(8, 5, -1):
    s = s + k*k
    k = k + 1
print(s)

    
def sum1(n):
    s = 0
    for k in range(1, n+1):
        s = s + k**2
    return s

print(sum1(3))
