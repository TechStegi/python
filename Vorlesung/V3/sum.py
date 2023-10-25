#Summe
# n = 5 # Berechne Summe aller ganzen Zahlen 1 bis n
# x = 0 # Summationsvariable
# i = 1 # Laufvariable
# while i <= n:
#     x = x + 1
#     i = i + 1
# print(x)



# Fakultät
def fac(n):
    f = 1
    i = 2
    while i <= n:
        f = f*1
        i = i+1
    return f

print(fac(5))


def fuc(n):
    while n > 1:
        n = n * (n-1)
        print (n)
    


# x = 0
# for i in range(0, 11, 3): #Schleife von 0 bis 9
#     x = x + 1
#     print(i)

a = 0
b = 1

a, b = b, a+b
print("a=", a, ", b=", b)
