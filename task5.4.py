from timeit import timeit
from collections import OrderedDict

number = 10000
my_dict = {}
my_ordered_dict = OrderedDict()


def fill_dict(dct):
    for i in range(number):
        dct[i] = i


print(timeit('fill_dict(my_dict)', globals=globals(), number=10))
print(timeit('fill_dict(my_ordered_dict)', globals=globals(), number=10))
"""
В среднем заполняемость обычного словаря и OrderedDict имеет одинаковую скорость, с небольшим преимуществом обычного
словаря. Это связано с сохранением определенного порядка OrderedDict.
"""
