from memory_profiler import profile
import random


@profile
def my_min1(lst):  # 12.8 MiB
    # O(N^2)
    min_num1 = 0                             # O(1)
    for i in range(len(lst)):                # O(N)
        for j in lst:                        # O(N^2)
            if lst[i] > j and min_num1 > j:  # O(1)
                min_num1 = j                 # O(1)
    return min_num1                          # O(1)


@profile
def my_min2(lst):  # 12.8 MiB
    # O(N)
    min_num2 = lst[0]     # O(1)
    for i in lst:         # O(N)
        if min_num2 > i:  # O(1)
            min_num2 = i  # O(1)
    return min_num2       # O(1)


print(my_min1([3, 6, 9, 0, 1, 8]))
print(my_min2([3, 6, 9, 0, 1, 8]))


@profile
def check_2(lst_obj):  # 14.5 MiB
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(N).
    """
    for j in range(len(lst_obj)):          # O(N)
        if lst_obj[j] in lst_obj[j+1:]:    # O(N)
            return False                   # O(1)
    return True                            # O(1)


@profile
def check_3(lst_obj):  # 14.5 MiB
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(N log N)
    """
    lst_copy = list(lst_obj)                 # O(N)
    lst_copy.sort()                          # O(N log N)
    for i in range(len(lst_obj) - 1):        # O(N)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)


for j in (50, 500, 1000, 5000, 10000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_2(lst))
print(check_3(lst))


@profile
def func_1(nums):  # 14.5 MiB
    """O(n)"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):  # 14.5 MiB
    """O(n)"""
    return [i for i, j in enumerate(nums) if j % 2 == 0]


my_list = [1, -4, 6, 8, -10]
print(func_1(my_list))
print(func_2(my_list))

"""В данном примере скрипты, выполняющие одинаковые задачи, занимают опинаковое количество памяти"""
