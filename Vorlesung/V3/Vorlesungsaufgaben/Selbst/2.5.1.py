g = 4

# print aufsteigende Sterne
for i in range(1, g + 1):
    print("*" * i)

# print absteigende Sterne
j = g
for j in range(g - 1, 0, -1):
    print("*" * j)
