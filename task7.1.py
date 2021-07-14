import timeit
import random


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


def bubble_sort1(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n - 1):
            if lst_obj[i] > lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


my_list = [random.randint(-100, 100) for i in range(1000)]
print(timeit.timeit("bubble_sort(my_list[:])", globals=globals(), number=100))
print(timeit.timeit("bubble_sort1(my_list[:])", globals=globals(), number=100))
"""Вторая функция оптимизирована за счет сокращения числа итераций. Качественных изменений в скорости при этом нет.
21.784827873999998
21.443577403000003
"""
