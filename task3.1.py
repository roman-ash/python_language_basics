def div_func(a, b):
    return round((a / b), 2)


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(div_func(num1, num2))
except ZeroDivisionError:
    print("На ноль делить нельзя!")
except ValueError:
    print("Введите два числа!")
