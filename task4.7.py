def fact(n):
    f = 1
    for i in range(n):
        f *= n
        n -= 1
    yield f


for el in fact(4):
    print(el)
