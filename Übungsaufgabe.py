# Aufgabe 1.2
n = int(input("Punktzahl eingeben: "))


def note(n):
    note = 1
    if n == 5:
        note = 1
    elif n == 4:
        note = 2
    elif n == 3:
        note = 3
    elif n == 2:
        note = 4
    elif n == 1 or n == 0:
        note = 5
    else:
        return "Punktzahl gibt es nicht"
    return note


print(note(n))


# Aufgabe 1.3
punktzahl = int(input("Punktzahl des Schülers: "))


def klausurnote(punktzahl):
    note = 1
    if punktzahl > 100:
        return "Es hat nicht so viele Punkte gegeben"
    elif punktzahl > 89:
        note = 1
    elif punktzahl > 79:
        note = 2
    elif punktzahl > 69:
        note = 3
    elif punktzahl > 59:
        note = 4
    elif punktzahl <= 59:
        note = 5
    else:
        return "Punktzahl gibt es nicht!"
    return note


print("Der Schüler hat die Note", klausurnote(punktzahl))


# Aufgabe 1.4
def BMI(gewicht, größe):
    bmi = gewicht / (größe**2)
    if bmi > 25:
        print("overweight")
    elif bmi >= 19:
        print("normal")
    else:
        print("underweight")


BMI(79, 1.75)


# Aufgabe 1.5
def BMI_alter(gewicht, größe, alter):
    bmi = gewicht / (größe**2)
    if alter < 19:
        print(
            "You are too young. The minimum age for calculating your BMI is 18 years."
        )
    elif alter < 25:
        if 19 <= bmi < 25:
            print("Normal")
        elif bmi < 19:
            print("under normal BMI")
        else:
            print("Above normal BMI")
    elif alter < 35:
        if 20 <= bmi < 26:
            print("normal")
        elif bmi < 20:
            print("Under")
        else:
            print("Above")
    elif alter < 45:
        if 21 <= bmi < 27:
            print("Normal")
        elif bmi < 21:
            print("under")
        else:
            print("Above")
    elif alter < 55:
        if 22 <= bmi < 28:
            print("normal")
        elif bmi < 22:
            print("under")
        else:
            print("above")
    elif alter < 65:
        if 23 <= bmi < 29:
            print("normal")
        elif bmi < 23:
            print("under")
        else:
            print("above")
    else:
        if 24 <= bmi < 30:
            print("Normal")
        elif bmi < 24:
            print("under")
        else:
            print("above")


BMI_alter(66, 1.73, 50)
