def c(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def c1(n, folge):
    if n == 1:
        return folge
    elif n % 2 == 0:
        return c1(n / 2, folge + 1)
    else:
        return c1(3 * n + 1, folge + 1)


# go = True
# input = int(input("Enter a number greater than 1: "))
# print(c1(input, folge_start))


# Ich habe die Listen folge_liste und die Zahlen i
def laengste_folge(a):
    maxfolge = a[0]
    maxindex = 0
    for i in range(1, len(a)):
        if a[i] > maxfolge:
            maxfolge = a[i]
            maxindex = i
    return [maxfolge, maxindex]


def c2(folge_start, ende):
    folge_liste = []
    # Schleife für Durchgänge für alle Zahlen 1 bis N, i steht dabei für die Anzahl der Durchgänge
    for i in range(1, ende + 1):
        folge_liste.append(c1(i, folge_start))
        if i == ende:
            return (
                "Die längste Folge zwischen 1 und N ist: "
                + str(laengste_folge(folge_liste)[0])
                + " von den Folgen "
                + str(folge_liste)
                + " für die Zahl i bzw. n = "
                + str(laengste_folge(folge_liste)[1] + 1)
            )
    return "something went wrong"


folge_start_wert = 0
ende_input = int(
    input(
        "Gib eine Zahl größer als 1 ein, bis wohin die Zahl der Folgen jeweils berechnet werden sollen: "
    )
)
print(c2(folge_start_wert, ende_input))


# print(c(5))
# print(c(c(5)))
# print(c(c(c(5))))
# print(c(c(c(c(((5)))))))
# print(c(c(c(c(c((5)))))))
# print(c(c(c(c(c(c((5))))))))
# print(c(c(c(c(c(c(c((5)))))))))
# print(c(c(c(c(c(c(c(c((5))))))))))
# print(c(c(c(c(c(c((c(c(c(5)))))))))))

# # 10mal aufrufen
# print(c(c(c(c(c(c(c(c(c(c((5))))))))))))
