import timeit
from random import randint


def median(lst_obj):
    temp_list = lst_obj
    for i in range(len(lst_obj) // 2):
        temp_list.remove(max(temp_list))
    return max(temp_list)


m = int(input('Enter m: '))
my_list = [randint(0, 100) for i in range(2 * m + 1)]
print(my_list)
print(f'Median - {median(my_list[:])}')
print(timeit.timeit("median(my_list[:])", globals=globals(), number=1000))
