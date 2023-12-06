def c(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


print(c(5))
print(c(c(5)))
print(c(c(c(5))))
print(c(c(c(c(((5)))))))
print(c(c(c(c(c((5)))))))
# 6 mal aufgerufen
print(c(c(c(c(c(c((5))))))))
print(c(c(c(c(c(c(c((5)))))))))
print(c(c(c(c(c(c(c(c((5))))))))))
print(c(c(c(c(c(c((c(c(c(5)))))))))))
# 10mal aufgerufen
print(c(c(c(c(c(c(c(c(c(c((5))))))))))))
