
def ggT(a, b):
    if b == 0:
        return a
    else:
        return ggT(b, a % b)
