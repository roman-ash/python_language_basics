from time import time
my_list = []
my_dict = {}
"""Все функции имеют линейую сложность и примерно одинаковую скорость выполнения"""


def timeit(f):
    def timed(*args, **kwargs):
        start = time()
        res = f(*args, **kwargs)
        end = time()
        print(f'Time is {end - start}')
        return res
    return timed


@timeit
def to_list(l, n):  # O(n)
    for i in range(1, n + 1):
        l.append(i)
    return l


@timeit
def to_dict(d, n):  # O(n)
    for i in range(1, n + 1):
        d[i] = i
    return d


print(to_list(my_list, 5))
print(to_dict(my_dict, 5))


@timeit
def mix_list(l):  # O(n)
    """the function shuffles the elements of the list"""
    for i in l:
        l.append(i)
        l.remove(i)
    return l


print(mix_list(my_list))


@timeit
def dict_func(d):  # O(n)
    """removes the first three elements"""
    for i in range(1, 4):
        d.pop(i)
    return d


print(dict_func(my_dict))
