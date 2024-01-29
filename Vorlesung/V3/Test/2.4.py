
def muster(n):
    for i in range(n):
        for j in range(1, i+2):
            print("*", end="")
        print()
        
    for k in range(n-1):
        for l in range(n-k-1, 0, -1):
            print("*", end='')
        print()
muster(5)