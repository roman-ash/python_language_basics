from collections import deque
from timeit import timeit


num = 10000
my_list = []
my_deque = deque()


def fill_list(l):
    for i in range(num):
        l.insert(0, i)
    return l


def fill_deque(d):
    for i in range(num):
        d.appendleft(i)
    return d


print(timeit('fill_list(my_list)', globals=globals(), number=10))
print(timeit('fill_deque(my_deque)', globals=globals(), number=10))

"""
Двусторонняя очередь работает значительно быстрее обычного списка. Операция insert имеет линейную сложность, 
а операция вставки в начало для двусторонней функции - константную сложность. 
"""
