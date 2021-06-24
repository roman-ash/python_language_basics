from timeit import timeit


def func_1(nums):
    """O(n)"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """O(n)"""
    return [i for i, j in enumerate(nums) if j % 2 == 0]


my_list = [1, -4, 6, 8, -10]
print(timeit("func_1(my_list)", globals=globals()))
print(timeit("func_2(my_list)", globals=globals()))
"""В func_2, используя list comprehension, мы избегаем использования метода append, который замедяет код"""
