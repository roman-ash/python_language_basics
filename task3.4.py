def my_func1(x, y):  # способ 1
    return x ** abs(y)


print(my_func1(5, -3))


def my_func2(x, y):  # способ 2
    i = 1
    result = 1
    while i <= abs(y):
        result *= x
        i += 1
    return result


print(my_func2(5, -3))
