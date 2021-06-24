from timeit import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print(timeit("revers_1(12340)", globals=globals()))
print(timeit("revers_2(12340)", globals=globals()))
print(timeit("revers_3(12340)", globals=globals()))

cProfile.run("revers_1(987600000)")
cProfile.run("revers_2(987600000)")
cProfile.run("revers_3(987600000)")
"""Функция revers_3 самая быстрая и эффективная из-за использования среза.
 revers_1 менее эффективна из-за рекурсии и арифметических операций,
 а revers_2 из-за цикла и арифметических операций."""
